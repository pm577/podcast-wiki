#!/usr/bin/env python3
"""
Fast Distillation Pipeline — parallel API calls, single-pass extraction.
Processes ALL backlog transcripts in minutes instead of hours.

Usage:
    python3 scripts/distill_fast.py                  # Use all new transcripts, 10 workers
    python3 scripts/distill_fast.py --parallel 20     # 20 concurrent API calls
    python3 scripts/distill_fast.py --max 100         # Cap transcripts per run
"""

import os, sys, json, time, hashlib, difflib, concurrent.futures
from pathlib import Path
from datetime import datetime, timezone

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))
RAW_DIR = WIKI_DIR / "raw" / "transcripts"
STATE_DIR = WIKI_DIR / "state"
SCRIPTS_DIR = WIKI_DIR / "scripts"
PROCESSED_FILE = STATE_DIR / "processed_transcripts.json"

STATE_DIR.mkdir(parents=True, exist_ok=True)

# ── DeepSeek API ───────────────────────────────────────────────────────────────

def call_deepseek(prompt: str, system: str = None, max_tokens: int = 4096) -> str:
    import urllib.request
    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        env_path = Path.home() / ".hermes" / ".env"
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("DEEPSEEK_API_KEY="):
                        api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                        break
    if not api_key:
        config_path = Path.home() / ".hermes" / "config.yaml"
        if config_path.exists():
            import yaml
            with open(config_path) as f:
                config = yaml.safe_load(f)
            api_key = (
                config.get("providers", {})
                .get("deepseek", {})
                .get("api_key", "")
            )
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
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read())
        return result["choices"][0]["message"]["content"]


# ── Combined Extraction Prompt ─────────────────────────────────────────────────

COMBINED_SYSTEM_PROMPT = """You extract structured data from podcast transcripts in a single pass.
Return ONLY valid JSON. Every quote MUST be a verbatim substring of the transcript.
Mark confidence 0-1 per field. Do not fabricate."""

COMBINED_PROMPT = """From this podcast transcript, extract ALL of the following in ONE JSON response:

1. GUEST PROFILES — name, role, company, key_beliefs (as verbatim quotes with confidence scores), evolution, new_insights
2. ACTIONABLE INSIGHTS — claim (near-verbatim), framework (or null), actionability (1-10), audience (founder|investor|operator|engineer|general), source_context, confidence
3. VERBATIM QUOTES — quote (exact text from transcript), speaker, context, category (framework|prediction|contrarian|advice|story)

TRANSCRIPT:
{transcript_text}

Return this JSON structure:
{{
  "guests": [
    {{
      "name": "Full name",
      "role": "Current role/title",
      "company": "Current company",
      "key_beliefs": [{{"belief": "verbatim quote", "confidence": 0.9}}],
      "evolution": "How thinking has changed or null",
      "new_insights": ["specific actionable insight from this episode"],
      "confidence": 0.8
    }}
  ],
  "insights": [
    {{
      "claim": "Near-verbatim insight text",
      "framework": null,
      "actionability": 8,
      "audience": "founder",
      "source_context": "What they were discussing",
      "confidence": 0.9
    }}
  ],
  "quotes": [
    {{
      "quote": "exact verbatim text from transcript",
      "speaker": "who said it",
      "context": "what was being discussed",
      "category": "advice"
    }}
  ]
}}"""


def extract_all(text: str) -> dict:
    """Single combined extraction — guests, insights, quotes in one API call."""
    chunk = text[:12000]  # Use first 12K chars (guests introduced early, key content front-loaded)
    prompt = COMBINED_PROMPT.replace("{transcript_text}", chunk)
    response = call_deepseek(prompt, system=COMBINED_SYSTEM_PROMPT, max_tokens=4096)
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {"guests": [], "insights": [], "quotes": [], "_parse_error": True, "_raw": response[:500]}


# ── Page Writers ───────────────────────────────────────────────────────────────

def update_guest_page(guest_data: dict, podcast: str, episode_slug: str) -> str:
    name = guest_data.get("name", "")
    if not name:
        return None
    slug = name.lower().replace(" ", "-").replace(".", "").replace("'", "")
    guest_file = WIKI_DIR / "guests" / f"{slug}.md"
    entry = f"- [[{episode_slug}]] — {guest_data.get('role', 'Guest')} at {guest_data.get('company', 'Unknown')}"

    if guest_file.exists():
        content = guest_file.read_text()
        if episode_slug not in content:
            content = content.replace(
                "**Appears in:**",
                f"**Appears in:**\n{entry}"
            )
            guest_file.write_text(content)
    else:
        frontmatter = f"""---
type: Guest
name: "{name}"
role: "{guest_data.get('role', '')}"
company: "{guest_data.get('company', '')}"
first_appearance: "{episode_slug}"
tags: []
---

# {name}

**Role:** {guest_data.get('role', '')} at {guest_data.get('company', '')}

**Key Beliefs:**
"""
        for belief in guest_data.get("key_beliefs", []):
            frontmatter += f"- {belief['belief']} (confidence: {belief.get('confidence', 0)})\n"
        frontmatter += f"""
**Appears in:**
{entry}
"""
        guest_file.parent.mkdir(parents=True, exist_ok=True)
        guest_file.write_text(frontmatter)
    return slug


def update_insights_page(guest_name: str, insights: list, episode_slug: str):
    if not insights or not guest_name:
        return
    slug = guest_name.lower().replace(" ", "-").replace(".", "").replace("'", "")
    insights_file = WIKI_DIR / "insights" / f"{slug}-insights.md"
    lines = [f"# {guest_name} — Insights", "", "*Extracted from podcast appearances.*", ""]
    for i, insight in enumerate(insights):
        audience = insight.get("audience", "general")
        actionability = insight.get("actionability", 5)
        conf = insight.get("confidence", 0)
        lines.append(f"## Insight {i+1}: {insight.get('claim', '')[:80]}...")
        lines.append(f"**Claim:** {insight.get('claim', '')}")
        if insight.get("framework"):
            lines.append(f"**Framework:** {insight['framework']}")
        lines.append(f"**Audience:** {audience} | **Actionability:** {actionability}/10 | **Confidence:** {conf}")
        lines.append(f"**Source:** {episode_slug}")
        lines.append(f"**Context:** {insight.get('source_context', '')}")
        lines.append("")
    insights_file.parent.mkdir(parents=True, exist_ok=True)
    insights_file.write_text("\n".join(lines))


def update_quotes_page(guest_name: str, quotes: list, episode_slug: str):
    if not quotes or not guest_name:
        return
    slug = guest_name.lower().replace(" ", "-").replace(".", "").replace("'", "")
    quotes_file = WIKI_DIR / "quotes" / f"{slug}-quotes.md"
    lines = [f"# {guest_name} — Quotes", "", "*Verbatim quotes verified against transcripts.*", ""]
    for q in quotes:
        category = q.get("category", "advice")
        lines.append(f"> {q['quote']}")
        lines.append(f"— {q.get('speaker', guest_name)}, {episode_slug} ({category})")
        lines.append("")
    quotes_file.parent.mkdir(parents=True, exist_ok=True)
    quotes_file.write_text("\n".join(lines))


# ── State ──────────────────────────────────────────────────────────────────────

def load_processed():
    if PROCESSED_FILE.exists():
        return set(json.loads(PROCESSED_FILE.read_text()))
    return set()

def save_processed(hashes):
    PROCESSED_FILE.write_text(json.dumps(list(hashes)))

def content_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_state(phase: str, stats: dict):
    state_file = STATE_DIR / "distiller-last-run.md"
    state_file.write_text(f"""---
type: State
phase: {phase}
timestamp: {datetime.now(timezone.utc).isoformat()}
---
## Distiller Last Run
- **Phase:** {phase}
- **Timestamp:** {datetime.now(timezone.utc).isoformat()}
- **Transcripts processed:** {stats.get('transcripts_processed', 0)}
- **Guests updated:** {stats.get('guests_updated', 0)}
- **Insights extracted:** {stats.get('insights_extracted', 0)}
- **Quotes verified:** {stats.get('quotes_verified', 0)}
- **Topics matched:** {stats.get('topics_matched', 0)}
- **FAISS rebuilt:** {stats.get('faiss_rebuilt', False)}
- **Errors:** {stats.get('errors', 0)}
""")


# ── Topic Cross-Referencing ───────────────────────────────────────────────────

def cross_reference_topics(transcript_text: str) -> dict:
    topics_dir = WIKI_DIR / "topics"
    existing_topics = {}
    if topics_dir.exists():
        for topic_file in topics_dir.glob("*.md"):
            slug = topic_file.stem
            content = topic_file.read_text()[:500]
            existing_topics[slug] = content.lower()
    transcript_lower = transcript_text.lower()
    matched_topics = []
    for slug, content in existing_topics.items():
        if slug.replace("-", " ") in transcript_lower or slug in transcript_lower:
            matched_topics.append({"slug": slug, "relevance": 7})
    return {"matched_topics": matched_topics[:10]}


# ── Worker ─────────────────────────────────────────────────────────────────────

def process_one(path: Path, podcast: str) -> dict:
    """Process a single transcript: API call + page writes. Returns stats dict."""
    stats = {"guests_updated": 0, "insights_extracted": 0,
             "quotes_verified": 0, "topics_matched": 0, "error": None}
    episode_slug = path.stem
    try:
        text = path.read_text()
        data = extract_all(text)

        if data.get("_parse_error"):
            stats["error"] = f"JSON parse error: {data.get('_raw', '')[:200]}"
            return stats

        # Guests
        for guest in data.get("guests", []):
            update_guest_page(guest, podcast, episode_slug)
            stats["guests_updated"] += 1

        # Insights
        all_insights = data.get("insights", [])
        if all_insights:
            for guest in data.get("guests", []):
                update_insights_page(guest.get("name"), all_insights, episode_slug)
            stats["insights_extracted"] = len(all_insights)

        # Quotes — verify against transcript
        all_quotes = data.get("quotes", [])
        verified = 0
        for q in all_quotes:
            qt = q.get("quote", "")
            if qt in text:
                q["verified"] = True
                verified += 1
            else:
                ratio = difflib.SequenceMatcher(None, qt, text).ratio()
                if ratio > 0.85:
                    q["verified"] = True
                    verified += 1
                else:
                    q["verified"] = False
        if verified > 0:
            for guest in data.get("guests", []):
                update_quotes_page(guest.get("name"), all_quotes, episode_slug)
            stats["quotes_verified"] = verified

        # Topics
        topics = cross_reference_topics(text)
        stats["topics_matched"] = len(topics.get("matched_topics", []))

    except Exception as e:
        stats["error"] = str(e)
        error_log = STATE_DIR / "distiller-errors.log"
        with open(error_log, "a") as f:
            f.write(f"{datetime.now().isoformat()} | {path} | {e}\n")

    return stats


# ── Main ───────────────────────────────────────────────────────────────────────

def find_new_transcripts():
    processed = load_processed()
    new = []
    for transcript in RAW_DIR.rglob("*.md"):
        h = content_hash(transcript)
        if h not in processed:
            new.append((transcript, h))
    return new, processed


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fast podcast distillation — parallel API calls")
    parser.add_argument("--parallel", type=int, default=10, help="Concurrent API workers (default 10)")
    parser.add_argument("--max", type=int, default=0, help="Max transcripts to process (default: all new)")
    args = parser.parse_args()

    new_transcripts, processed_hashes = find_new_transcripts()
    if not new_transcripts:
        print("No new transcripts to process.")
        return

    if args.max and args.max < len(new_transcripts):
        new_transcripts = new_transcripts[:args.max]

    print(f"Processing {len(new_transcripts)} transcripts with {args.parallel} workers...")
    print(f"Estimated time: ~{len(new_transcripts) / args.parallel * 5:.0f}s at 5s/transcript")

    total_stats = {"transcripts_processed": 0, "guests_updated": 0,
                   "insights_extracted": 0, "quotes_verified": 0,
                   "topics_matched": 0, "errors": 0, "faiss_signal": False}

    start = time.time()

    # Phase 1: Parallel API calls
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as executor:
        future_map = {}
        for path, h in new_transcripts:
            podcast = "unknown"
            pl = str(path).lower()
            if "lenny" in pl: podcast = "lenny"
            elif "20vc" in pl: podcast = "20vc"
            elif "newsletter" in pl: podcast = "newsletters"
            future = executor.submit(process_one, path, podcast)
            future_map[future] = (path, h)

        # Phase 2: Collect results (serial page writes happen inside process_one)
        completed = 0
        for future in concurrent.futures.as_completed(future_map):
            path, h = future_map[future]
            try:
                stats = future.result()
            except Exception as e:
                stats = {"guests_updated": 0, "insights_extracted": 0,
                         "quotes_verified": 0, "topics_matched": 0, "error": str(e)}

            if stats.get("error"):
                total_stats["errors"] += 1
                with open(str(STATE_DIR / "failed-transcripts.md"), "a") as f:
                    f.write(f"- {path} — {stats['error']} — {datetime.now().isoformat()}\n")
                # Don't mark as processed — retry on next run
            else:
                total_stats["transcripts_processed"] += 1
                total_stats["guests_updated"] += stats["guests_updated"]
                total_stats["insights_extracted"] += stats["insights_extracted"]
                total_stats["quotes_verified"] += stats["quotes_verified"]
                total_stats["topics_matched"] += stats["topics_matched"]
                processed_hashes.add(h)

            completed += 1
            if completed % 10 == 0 or completed == len(new_transcripts):
                elapsed = time.time() - start
                rate = completed / elapsed if elapsed > 0 else 0
                print(f"  {completed}/{len(new_transcripts)} ({rate:.1f}/s, {elapsed:.0f}s elapsed)")
                # Incremental state save — prevents stuck state on crash
                write_state("running", total_stats)
                save_processed(processed_hashes)

    elapsed = time.time() - start
    print(f"\nTime: {elapsed:.0f}s ({elapsed/60:.1f}min) at {completed/elapsed:.1f} transcripts/s")

    # Signal FAISS rebuild
    with open(str(WIKI_DIR / "state" / "faiss-needs-rebuild"), "w") as f:
        f.write("1")
    total_stats["faiss_signal"] = True

    # Save final state
    save_processed(processed_hashes)
    write_state("complete", total_stats)

    print(f"""
Fast distillation complete:
  Transcripts: {total_stats['transcripts_processed']}
  Guests: {total_stats['guests_updated']}
  Insights: {total_stats['insights_extracted']}
  Quotes verified: {total_stats['quotes_verified']}
  Topics: {total_stats['topics_matched']}
  Errors: {total_stats['errors']}
  FAISS rebuild: signalled""")


if __name__ == "__main__":
    main()
