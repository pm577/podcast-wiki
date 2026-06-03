#!/usr/bin/env python3
"""
Podcast Wiki Evaluator — measures retrieval quality, tracks coverage over time.

Usage:
    python3 scripts/eval.py                     # Full eval: sample 100 pages
    python3 scripts/eval.py --quick              # Quick eval: sample 20 pages
    python3 scripts/eval.py --compare            # Compare vs baseline
"""

import os, json, random, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))
EVAL_DIR = WIKI_DIR / "eval"
STATE_DIR = WIKI_DIR / "state"
EVAL_DIR.mkdir(parents=True, exist_ok=True)
STATE_DIR.mkdir(parents=True, exist_ok=True)

GOLDEN_SET_FILE = EVAL_DIR / "golden-set.jsonl"
BASELINE_FILE = EVAL_DIR / "baseline.json"
DASHBOARD_FILE = STATE_DIR / "eval-dashboard.md"

# ── Core Eval Logic ─────────────────────────────────────────────────────────

def load_golden_set() -> list:
    """Load golden Q&A pairs."""
    pairs = []
    if GOLDEN_SET_FILE.exists():
        for line in GOLDEN_SET_FILE.read_text().strip().split("\n"):
            if line.strip():
                pairs.append(json.loads(line))
    return pairs

def save_golden_set(pairs: list):
    """Save golden Q&A pairs."""
    lines = [json.dumps(p) for p in pairs]
    GOLDEN_SET_FILE.write_text("\n".join(lines) + "\n")

def add_to_golden_set(question: str, expected_answer_page: str, source: str = "manual"):
    """Add a new Q&A pair to the golden set."""
    pairs = load_golden_set()
    pairs.append({
        "question": question,
        "expected_answer_page": expected_answer_page,
        "source": source,
        "added": datetime.now(timezone.utc).isoformat()
    })
    save_golden_set(pairs)
    return len(pairs)

def sample_pages(n: int = 100) -> list:
    """Sample N random markdown pages from wiki directories."""
    dirs = [
        WIKI_DIR / "guests",
        WIKI_DIR / "topics",
        WIKI_DIR / "wiki",
        WIKI_DIR / "insights",
    ]
    pages = []
    for d in dirs:
        if d.exists():
            pages.extend(list(d.rglob("*.md")))
    
    random.seed(int(datetime.now().timestamp()))
    return random.sample(pages, min(n, len(pages)))

def query_faiss(question: str) -> dict:
    """Query FAISS via the MCP wrapper and return top result."""
    wrapper = WIKI_DIR / "scripts" / "mcp_wrapper.sh"
    if not wrapper.exists():
        return {"score": 0, "page": None, "error": "mcp_wrapper.sh not found"}
    
    try:
        result = subprocess.run(
            ["bash", str(wrapper), "search_by_meaning", question],
            capture_output=True, text=True, timeout=30,
            cwd=str(WIKI_DIR)
        )
        # Parse JSON output from MCP wrapper
        if result.returncode == 0 and result.stdout.strip():
            data = json.loads(result.stdout)
            results = data.get("results", [])
            if results:
                return {
                    "score": results[0].get("score", 0),
                    "page": results[0].get("metadata", {}).get("source", "unknown"),
                    "answerable": results[0].get("score", 0) > 0.7
                }
    except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception) as e:
        return {"score": 0, "page": None, "error": str(e)}
    
    return {"score": 0, "page": None, "error": "no results"}

def run_eval(sample_size: int = 100) -> dict:
    """Run full evaluation: sample pages, query, measure coverage."""
    pages = sample_pages(sample_size)
    
    results = []
    answerable = 0
    
    for page in pages:
        try:
            content = page.read_text()[:2000]  # First 2000 chars for question gen
            
            # Generate a question this page should answer
            # Simplified: use page title as the query
            title = page.stem.replace("-", " ").replace("_", " ")
            question = f"What does the podcast wiki say about {title}?"
            
            result = query_faiss(question)
            result["page_title"] = title
            result["page_path"] = str(page.relative_to(WIKI_DIR))
            results.append(result)
            
            if result.get("answerable"):
                answerable += 1
        except Exception as e:
            results.append({
                "page_title": page.stem,
                "error": str(e),
                "answerable": False
            })
    
    coverage = answerable / len(results) if results else 0
    
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sample_size": len(results),
        "answerable": answerable,
        "coverage": round(coverage, 3),
        "results": results
    }

def evaluate_golden_set() -> dict:
    """Evaluate against the golden Q&A set."""
    pairs = load_golden_set()
    if not pairs:
        return {"golden_set_size": 0, "accuracy": 0, "message": "Golden set is empty"}
    
    correct = 0
    for pair in pairs:
        result = query_faiss(pair["question"])
        if result.get("page") and pair["expected_answer_page"] in str(result.get("page", "")):
            correct += 1
    
    return {
        "golden_set_size": len(pairs),
        "correct": correct,
        "accuracy": round(correct / len(pairs), 3) if pairs else 0
    }

# ── Dashboard ────────────────────────────────────────────────────────────────

def load_baseline() -> dict:
    """Load or create evaluation baseline."""
    if BASELINE_FILE.exists():
        return json.loads(BASELINE_FILE.read_text())
    return {"coverage": 0, "golden_accuracy": 0, "timestamp": None}

def save_baseline(data: dict):
    """Save evaluation baseline."""
    BASELINE_FILE.write_text(json.dumps(data, indent=2))

def compare_to_baseline(current: dict, baseline: dict) -> dict:
    """Compare current eval to baseline."""
    coverage_delta = current.get("coverage", 0) - baseline.get("coverage", 0)
    golden_delta = current.get("golden_accuracy", 0) - baseline.get("golden_accuracy", 0)
    
    regressed = coverage_delta < -0.05 or golden_delta < -0.02
    
    return {
        "coverage_delta": round(coverage_delta, 3),
        "golden_accuracy_delta": round(golden_delta, 3),
        "regressed": regressed,
        "action": "ALERT: Regression detected" if regressed else "Stable"
    }

def update_dashboard(eval_results: dict, golden_results: dict, baseline: dict):
    """Write evaluation dashboard."""
    comparison = compare_to_baseline({
        "coverage": eval_results["coverage"],
        "golden_accuracy": golden_results["accuracy"]
    }, baseline)
    
    DASHBOARD_FILE.write_text(f"""---
type: State
coverage: {eval_results['coverage']}
golden_accuracy: {golden_results['accuracy']}
timestamp: {eval_results['timestamp']}
---

## Podcast Wiki Eval Dashboard

**Last eval:** {eval_results['timestamp']}
**Coverage:** {eval_results['coverage']*100:.1f}% ({eval_results['answerable']}/{eval_results['sample_size']} pages answerable)
**Golden set:** {golden_results.get('golden_set_size', 0)} Q&A pairs, {golden_results.get('accuracy', 0)*100:.1f}% accuracy

### vs Baseline
- Coverage delta: {comparison['coverage_delta']:+.3f}
- Golden accuracy delta: {comparison['golden_accuracy_delta']:+.3f}
- Status: **{comparison['action']}**

### Previous baselines
- Baseline coverage: {baseline.get('coverage', 0)*100:.1f}%
- Baseline accuracy: {baseline.get('golden_accuracy', 0)*100:.1f}%
""")

# ── MCP Synthesis Quality Evaluation ──────────────────────────────────────────

def eval_mcp_quality(golden_path: str = "eval/golden-set.jsonl", sample: int = 10) -> dict:
    """Query MCP server for each golden-set question and check if expected page appears in results."""
    import random
    
    golden = WIKI_DIR / golden_path
    if not golden.exists():
        return {"error": f"Golden set not found at {golden}", "score": 0}
    
    questions = []
    with open(golden) as f:
        for line in f:
            if line.strip():
                questions.append(json.loads(line))
    
    if len(questions) > sample:
        random.shuffle(questions)
        questions = questions[:sample]
    
    results = []
    sys.path.insert(0, str(WIKI_DIR / "scripts"))
    from podcast_mcp_server_v2 import do_ask
    
    for qa in questions:
        q = qa["question"]
        expected = qa["expected_answer_page"]
        try:
            resp = do_ask(q)
            semantic = resp.get("semantic_matches", [])
            keyword = resp.get("keyword_matches", [])
            all_sources = [s.get("source_id", "") for s in semantic + keyword]
            found = any(expected in src for src in all_sources)
            results.append({
                "question": q, "expected": expected,
                "found": found, "sources": all_sources[:5]
            })
        except Exception as e:
            results.append({"question": q, "expected": expected,
                            "found": False, "error": str(e)})
    
    found_count = sum(1 for r in results if r.get("found"))
    score = found_count / len(results) if results else 0
    
    return {"mode": "mcp_synthesis", "sample_size": len(results),
            "found_count": found_count, "score": round(score, 3), "results": results}


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Podcast wiki evaluator")
    parser.add_argument("--quick", action="store_true", help="Quick eval: 20 pages")
    parser.add_argument("--compare", action="store_true", help="Compare vs baseline")
    parser.add_argument("--set-baseline", action="store_true", help="Set current result as baseline")
    parser.add_argument("--mcp", action="store_true", help="Test MCP synthesis quality instead of FAISS recall")
    args = parser.parse_args()
    
    if args.mcp:
        result = eval_mcp_quality(sample=20)
        print(f"MCP Synthesis Quality: {result.get('score', 0)*100:.0f}% ({result.get('found_count')}/{result.get('sample_size')})")
        mcp_dashboard = STATE_DIR / "mcp-quality-dashboard.md"
        with open(str(mcp_dashboard), "w") as f:
            f.write(f"# MCP Synthesis Quality Dashboard\n\n")
            f.write(f"**Last run:** {datetime.now().isoformat()}\n")
            f.write(f"**Score:** {result.get('score', 0)*100:.0f}% ({result.get('found_count')}/{result.get('sample_size')})\n\n")
            for r in result.get("results", []):
                status = "✅" if r.get("found") else "❌"
                f.write(f"- {status} {r['question'][:80]}\n")
                f.write(f"  Expected: `{r['expected']}`\n")
                if not r.get("found") and r.get("sources"):
                    f.write(f"  Got: `{r['sources'][:3]}`\n")
        print(f"Dashboard written to: {mcp_dashboard}")
        return
    
    sample_size = 20 if args.quick else 100
    
    print(f"Running eval on {sample_size} random pages...")
    eval_results = run_eval(sample_size)
    golden_results = evaluate_golden_set()
    
    print(f"""
Eval complete:
  Coverage: {eval_results['coverage']*100:.1f}% ({eval_results['answerable']}/{eval_results['sample_size']})
  Golden accuracy: {golden_results.get('accuracy', 0)*100:.1f}% ({golden_results.get('correct', 0)}/{golden_results.get('golden_set_size', 0)})
  Golden set size: {golden_results.get('golden_set_size', 0)}
""")
    
    baseline = load_baseline()
    
    if args.set_baseline:
        save_baseline({
            "coverage": eval_results["coverage"],
            "golden_accuracy": golden_results["accuracy"],
            "timestamp": eval_results["timestamp"]
        })
        print("Baseline set.")
    
    if args.compare or not args.set_baseline:
        comparison = compare_to_baseline({
            "coverage": eval_results["coverage"],
            "golden_accuracy": golden_results["accuracy"]
        }, baseline)
        print(f"vs baseline: coverage {comparison['coverage_delta']:+.3f}, golden accuracy {comparison['golden_accuracy_delta']:+.3f}")
        if comparison["regressed"]:
            print("⚠️ REGRESSION DETECTED")
    
    update_dashboard(eval_results, golden_results, baseline)

if __name__ == "__main__":
    main()
