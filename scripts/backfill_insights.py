#!/usr/bin/env python3
"""Backfill insight pages for guests that are missing them.

Reads guest pages → finds transcript files → re-extracts insights using
full transcript text (chunked) → appends to insight page or creates new one.
"""
import os, sys, json, time, re, concurrent.futures, urllib.request
from pathlib import Path
from datetime import datetime

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))
GUESTS_DIR = WIKI_DIR / "guests"
INSIGHTS_DIR = WIKI_DIR / "insights"
RAW_DIR = WIKI_DIR / "raw" / "transcripts"
STATE_DIR = WIKI_DIR / "state"

STATE_DIR.mkdir(parents=True, exist_ok=True)


def call_deepseek(prompt: str, system: str = None, max_tokens: int = 4096) -> str:
    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        env_path = Path.home() / ".hermes" / ".env"
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("DEEPSEEK_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY not found.")
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    body = json.dumps({
        "model": "deepseek-chat",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.2,
        "response_format": {"type": "json_object"}
    }).encode()
    req = urllib.request.Request(
        "https://api.deepseek.com/v1/chat/completions",
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read())["choices"][0]["message"]["content"]


INSIGHT_SYSTEM = """You extract actionable insights from podcast transcripts.
Return ONLY valid JSON. Every insight must be traceable to a specific passage.
Classify each insight by audience and actionability."""

INSIGHT_PROMPT = """Extract the 3-7 most actionable insights from this transcript chunk.
Use the full context of the chunk. Each insight should be specific, not generic.

TRANSCRIPT CHUNK:
{chunk}

Return this JSON:
{{
  "insights": [
    {{
      "claim": "The specific insight (near-verbatim)",
      "framework": "Name of framework if mentioned (or null)",
      "actionability": 8,
      "audience": "founder|investor|operator|engineer|general",
      "source_context": "What they were discussing when this came up",
      "confidence": 0.9
    }}
  ]
}}

Score actionability 1-10: 10 = implementable today, 1 = theoretical.
Classify audience: founder, investor, operator, engineer, or general."""


def chunk_text(text: str, chunk_size: int = 12000, overlap: int = 500) -> list:
    if len(text) <= chunk_size:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks


def extract_insights_full(text: str) -> list:
    """Extract insights from full transcript using chunking."""
    chunks = chunk_text(text, 12000, 500)
    all_insights = []
    seen_claims = set()
    for chunk in chunks:
        prompt = INSIGHT_PROMPT.replace("{chunk}", chunk)
        try:
            response = call_deepseek(prompt, system=INSIGHT_SYSTEM, max_tokens=3072)
            data = json.loads(response)
            for insight in data.get("insights", []):
                key = insight.get("claim", "")[:80].lower().strip()
                if key and key not in seen_claims:
                    seen_claims.add(key)
                    all_insights.append(insight)
        except (json.JSONDecodeError, KeyError, ValueError):
            continue
    return all_insights


def append_insights_page(guest_slug: str, guest_name: str, insights: list, episode_slug: str):
    """Append insights to existing page or create new one."""
    if not insights:
        return False
    insights_file = INSIGHTS_DIR / f"{guest_slug}-insights.md"
    lines = []
    if insights_file.exists():
        existing = insights_file.read_text()
        # Check if this episode already has insights appended
        if f"**Source:** {episode_slug}" in existing:
            return False  # Already processed
        lines.append(existing.rstrip() + "\n")
        lines.append(f"\n## From [[{episode_slug}]]\n")
    else:
        lines.append(f"# {guest_name} — Insights\n")
        lines.append("*Extracted from podcast appearances.*\n")

    for i, insight in enumerate(insights):
        audience = insight.get("audience", "general")
        actionability = insight.get("actionability", 5)
        conf = insight.get("confidence", 0)
        claim = insight.get("claim", "")
        lines.append(f"### Insight: {claim[:80]}...")
        lines.append(f"**Claim:** {claim}")
        if insight.get("framework"):
            lines.append(f"**Framework:** {insight['framework']}")
        lines.append(f"**Audience:** {audience} | **Actionability:** {actionability}/10 | **Confidence:** {conf}")
        lines.append(f"**Source:** {episode_slug}")
        lines.append(f"**Context:** {insight.get('source_context', '')}")
        lines.append("")

    INSIGHTS_DIR.mkdir(parents=True, exist_ok=True)
    insights_file.write_text("\n".join(lines))
    return True


def find_transcript_for_guest(guest_slug: str, guest_content: str) -> list:
    """Find transcript files linked in a guest page's 'Appears in:' section."""
    links = re.findall(r'\[\[([^\]]+)\]\]', guest_content)
    found = []
    for a in links:
        for pod_dir in RAW_DIR.iterdir():
            if not pod_dir.is_dir():
                continue
            tf = pod_dir / f"{a}.md"
            if tf.exists():
                found.append(tf)
                break
    return found


def process_one_guest(guest_slug: str) -> dict:
    """Process one guest: find transcript, extract insights, write page."""
    gp = GUESTS_DIR / f"{guest_slug}.md"
    if not gp.exists():
        return {"slug": guest_slug, "error": "Guest page not found", "status": "skip"}
    
    content = gp.read_text()
    guest_name = guest_slug.replace("-", " ").title()
    transcripts = find_transcript_for_guest(guest_slug, content)
    
    if not transcripts:
        return {"slug": guest_slug, "error": "No transcript found", "status": "skip"}
    
    total_insights = 0
    for tf in transcripts:
        text = tf.read_text()
        insights = extract_insights_full(text)
        episode_slug = tf.stem
        if append_insights_page(guest_slug, guest_name, insights, episode_slug):
            total_insights += len(insights)
    
    return {
        "slug": guest_slug,
        "transcripts": len(transcripts),
        "insights_extracted": total_insights,
        "status": "done"
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Backfill missing insight pages")
    parser.add_argument("--parallel", type=int, default=10)
    parser.add_argument("--limit", type=int, default=0, help="Max guests to process (0 = all)")
    args = parser.parse_args()

    # Find guests without insights
    insight_slugs = set(i.stem.replace("-insights", "") for i in INSIGHTS_DIR.glob("*.md"))
    targets = sorted([gp.stem for gp in GUESTS_DIR.glob("*.md") if gp.stem not in insight_slugs])

    if args.limit:
        targets = targets[:args.limit]

    print(f"Backfilling insights for {len(targets)} guests ({args.parallel} workers)...")
    start = time.time()
    results = {"done": 0, "skip": 0, "insights": 0, "errors": 0}

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as ex:
        futures = {ex.submit(process_one_guest, slug): slug for slug in targets}
        done = 0
        for future in concurrent.futures.as_completed(futures):
            try:
                r = future.result()
            except Exception as e:
                r = {"slug": futures[future], "status": "error", "error": str(e)}
            
            results[r.get("status", "error")] = results.get(r.get("status", "error"), 0) + 1
            results["insights"] += r.get("insights_extracted", 0)
            
            done += 1
            if done % 50 == 0 or done == len(targets):
                elapsed = time.time() - start
                print(f"  {done}/{len(targets)} ({done/elapsed:.1f}/s, {elapsed:.0f}s, {results['insights']} insights so far)")

    elapsed = time.time() - start
    print(f"\nDone in {elapsed:.0f}s ({elapsed/60:.1f}min)")
    print(f"  Guests processed: {results['done']}")
    print(f"  Skipped (no transcript): {results.get('skip', 0)}")
    print(f"  Errors: {results.get('error', 0)}")
    print(f"  New insights extracted: {results['insights']}")


if __name__ == "__main__":
    main()
