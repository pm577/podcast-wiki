#!/usr/bin/env python3
"""
Podcast Distillation Pipeline — reads raw transcripts, extracts structured content,
updates wiki pages, re-indexes FAISS.

Usage:
    python3 scripts/distill.py                    # Process ALL unprocessed transcripts
    python3 scripts/distill.py --episode <slug>   # Process a single episode
    python3 scripts/distill.py --podcast lenny    # Process one podcast

Architecture:
    Raw transcript → extract guest profile → extract insights → extract quotes
    → cross-reference topics → write wiki pages → re-index FAISS → write state
"""

import os, sys, json, time, hashlib, difflib
from pathlib import Path
from datetime import datetime, timezone

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))

def chunk_transcript(text, chunk_size=12000, overlap=500):
    if len(text) <= chunk_size:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks
RAW_DIR = WIKI_DIR / "raw" / "transcripts"
STATE_DIR = WIKI_DIR / "state"
SCRIPTS_DIR = WIKI_DIR / "scripts"

# Ensure state directory exists
STATE_DIR.mkdir(parents=True, exist_ok=True)

# ── Configuration ───────────────────────────────────────────────────────────

# Processed transcript tracking (by content hash to detect re-downloads)
PROCESSED_FILE = STATE_DIR / "processed_transcripts.json"

# Extraction quality thresholds
QUOTE_VERIFY_MIN_LENGTH = 10  # Min chars for quote substring verification

# ── Helper: DeepSeek API ────────────────────────────────────────────────────

def call_deepseek(prompt: str, system: str = None, max_tokens: int = 4096) -> str:
    """Call DeepSeek API. Reads API key from Hermes config or environment."""
    import urllib.request
    
    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        # Try to read from Hermes .env file
        env_path = Path.home() / ".hermes" / ".env"
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("DEEPSEEK_API_KEY="):
                        api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                        break
    
    if not api_key:
        # Try to read from Hermes config
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
        raise RuntimeError("DEEPSEEK_API_KEY not found. Set it in ~/.hermes/.env or environment.")
    
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    
    body = json.dumps({
        "model": "deepseek-chat",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.3,
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


def call_deepseek_with_retry(prompt, system=None, max_tokens=4096, max_retries=2):
    """Call DeepSeek with exponential backoff retry on parse failures."""
    for attempt in range(max_retries + 1):
        try:
            response = call_deepseek(prompt, system=system, max_tokens=max_tokens)
            # Verify it's valid JSON (as expected for all extraction prompts)
            json.loads(response)
            return response
        except (ValueError, KeyError, TypeError, json.JSONDecodeError):
            if attempt < max_retries:
                time.sleep(2 ** attempt)
                continue
            return None
    return None

# ── Stage 1: Guest Extraction ───────────────────────────────────────────────

GUEST_SYSTEM_PROMPT = """You extract structured guest profiles from podcast transcripts.
Return ONLY valid JSON. Every field must be traceable to the transcript.
Use verbatim quotes for key beliefs. Mark confidence 0-1 per field.
If multiple guests: extract ALL guests in a guests[] array."""

GUEST_EXTRACTION_PROMPT = """Extract guest profile from this transcript:

{transcript_chunk}

Return this JSON structure:
{{
  "guests": [
    {{
      "name": "Full name",
      "role": "Current role/title",
      "company": "Current company",
      "key_beliefs": [
        {{"belief": "verbatim quote showing the belief", "confidence": 0.9}}
      ],
      "evolution": "How their thinking has changed (or null if no change evident)",
      "new_insights": ["Specific actionable insight from this episode"],
      "confidence": 0.8
    }}
  ],
  "extraction_notes": "any issues or uncertainties"
}}

IMPORTANT:
- Every key_belief must be a verbatim quote from the transcript
- If a field is uncertain, set confidence < 0.7
- Do not fabricate information not in the transcript"""

def extract_guests(transcript_text: str) -> dict:
    """Extract guest profiles from transcript text."""
    # Use first 8000 chars for guest extraction (guests usually introduced early)
    chunk = transcript_text[:8000]
    prompt = GUEST_EXTRACTION_PROMPT.replace("{transcript_chunk}", chunk)
    
    response = call_deepseek(prompt, system=GUEST_SYSTEM_PROMPT, max_tokens=2048)
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {"guests": [], "extraction_notes": "JSON parse failed", "raw": response}

# ── Stage 2: Insight Extraction ─────────────────────────────────────────────

INSIGHT_SYSTEM_PROMPT = """You extract actionable insights from podcast transcripts.
Return ONLY valid JSON. Every insight must be traceable to a specific passage.
Classify each insight by audience and actionability."""

INSIGHT_EXTRACTION_PROMPT = """Extract the 3-7 most actionable insights from this transcript:

{transcript_chunk}

Return this JSON:
{{
  "insights": [
    {{
      "claim": "The specific insight (near-verbatim from transcript)",
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

def extract_insights(transcript_text: str) -> list:
    """Extract actionable insights from transcript using chunking for full coverage."""
    # Use chunking to cover entire transcript, not just first 12K chars
    chunks = chunk_transcript(transcript_text, chunk_size=12000, overlap=500)
    all_insights = []
    seen_claims = set()
    for chunk in chunks:
        prompt = INSIGHT_EXTRACTION_PROMPT.replace("{transcript_chunk}", chunk)
        response = call_deepseek(prompt, system=INSIGHT_SYSTEM_PROMPT, max_tokens=3072)
        try:
            data = json.loads(response)
            chunk_insights = data.get("insights", [])
            for insight in chunk_insights:
                key = insight.get("claim", "")[:80].lower().strip()
                if key and key not in seen_claims:
                    seen_claims.add(key)
                    all_insights.append(insight)
        except json.JSONDecodeError:
            continue
    return all_insights

# ── Stage 3: Quote Extraction ───────────────────────────────────────────────

QUOTE_SYSTEM_PROMPT = """You extract verbatim quotes from podcast transcripts.
Return ONLY valid JSON. Every quote MUST be an exact substring of the transcript.
Verify each quote by checking it appears verbatim in the source text."""

QUOTE_EXTRACTION_PROMPT = """Extract the 3-5 most impactful verbatim quotes from this transcript.
IMPORTANT: Each quote MUST appear verbatim in the transcript. 
If you're not 100% sure a quote is verbatim, don't include it.

{transcript_chunk}

Return this JSON:
{{
  "quotes": [
    {{
      "quote": "exact verbatim text from transcript",
      "speaker": "who said it",
      "timestamp": "MM:SS or null",
      "context": "what was being discussed",
      "category": "framework|prediction|contrarian|advice|story",
      "verified": true
    }}
  ]
}}"""

def extract_quotes(transcript_text: str) -> list:
    """Extract verbatim quotes from transcript using chunking for full coverage."""
    MIN_QUOTE_LENGTH = 50
    # Use chunking to cover entire transcript
    chunks = chunk_transcript(transcript_text, chunk_size=10000, overlap=500)
    all_quotes = []
    seen_quotes = set()
    for chunk in chunks:
        prompt = QUOTE_EXTRACTION_PROMPT.replace("{transcript_chunk}", chunk)
        response = call_deepseek(prompt, system=QUOTE_SYSTEM_PROMPT, max_tokens=2048)
        try:
            data = json.loads(response)
            chunk_quotes = data.get("quotes", [])
            for q in chunk_quotes:
                key = q.get("quote", "")[:60].lower().strip()
                if key and key not in seen_quotes:
                    seen_quotes.add(key)
                    # Verify using difflib SequenceMatcher
                    quote_text = q.get("quote", "")
                    if len(quote_text) < MIN_QUOTE_LENGTH:
                        q["verified"] = False
                        q["verification_note"] = "Too short to verify"
                    elif quote_text in transcript_text:
                        q["verified"] = True
                    else:
                        ratio = difflib.SequenceMatcher(None, quote_text, transcript_text).ratio()
                        q["verified"] = ratio > 0.85
                        q["verification_note"] = f"Sequence match: {ratio:.0%}"
                    all_quotes.append(q)
        except json.JSONDecodeError:
            continue
    return all_quotes

# ── Stage 4: Topic Cross-Referencing ─────────────────────────────────────────

def cross_reference_topics(transcript_text: str) -> dict:
    """Identify topics discussed in transcript and link to existing topic pages."""
    # Read existing topic slugs
    topics_dir = WIKI_DIR / "topics"
    existing_topics = {}
    if topics_dir.exists():
        for topic_file in topics_dir.glob("*.md"):
            slug = topic_file.stem
            content = topic_file.read_text()[:500]
            existing_topics[slug] = content.lower()
    
    # Simple keyword-based topic detection
    transcript_lower = transcript_text.lower()
    matched_topics = []
    for slug, content in existing_topics.items():
        if slug.replace("-", " ") in transcript_lower or slug in transcript_lower:
            matched_topics.append({
                "slug": slug,
                "relevance": 7
            })
    
    return {
        "matched_topics": matched_topics[:10],
        "new_topic_candidates": []  # TODO: LLM-based new topic detection
    }

# ── Page Writers ─────────────────────────────────────────────────────────────

def update_guest_page(guest_data: dict, podcast: str, episode_slug: str):
    """Update or create a guest page with new episode appearance."""
    name = guest_data.get("name", "")
    if not name:
        return None
    
    slug = name.lower().replace(" ", "-").replace(".", "").replace("'", "")
    guest_file = WIKI_DIR / "guests" / f"{slug}.md"
    
    entry = f"- [[{episode_slug}]] — {guest_data.get('role', 'Guest')} at {guest_data.get('company', 'Unknown')}"
    
    if guest_file.exists():
        content = guest_file.read_text()
        if episode_slug not in content:
            # Add appearance to list
            content = content.replace(
                "**Appears in:**",
                f"**Appears in:**\n{entry}"
            )
            guest_file.write_text(content)
    else:
        # Create new guest page
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
            conf = belief.get("confidence", 0)
            frontmatter += f"- {belief['belief']} (confidence: {conf})\n"
        
        frontmatter += f"""
**Appears in:**
{entry}
"""
        guest_file.parent.mkdir(parents=True, exist_ok=True)
        guest_file.write_text(frontmatter)
    
    return slug

def update_insights_page(guest_name: str, insights: list, episode_slug: str):
    """Write extracted insights for a guest."""
    if not insights or not guest_name:
        return
    
    slug = guest_name.lower().replace(" ", "-").replace(".", "").replace("'", "")
    insights_file = WIKI_DIR / "insights" / f"{slug}-insights.md"
    
    lines = [f"# {guest_name} — Insights", "", f"*Extracted from podcast appearances.*", ""]
    for i, insight in enumerate(insights):
        conf = insight.get("confidence", 0)
        audience = insight.get("audience", "general")
        actionability = insight.get("actionability", 5)
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
    """Write verified quotes for a guest."""
    verified = [q for q in quotes if q.get("verified")]
    if not verified or not guest_name:
        return
    
    slug = guest_name.lower().replace(" ", "-").replace(".", "").replace("'", "")
    quotes_file = WIKI_DIR / "quotes" / f"{slug}-quotes.md"
    
    lines = [f"# {guest_name} — Quotes", "", "*Verbatim quotes verified against transcripts.*", ""]
    for q in verified:
        category = q.get("category", "advice")
        lines.append(f"> {q['quote']}")
        lines.append(f"— {q.get('speaker', guest_name)}, {episode_slug} ({category})")
        lines.append("")
    
    quotes_file.parent.mkdir(parents=True, exist_ok=True)
    quotes_file.write_text("\n".join(lines))

def rebuild_faiss():
    """Trigger FAISS index rebuild."""
    import subprocess
    index_script = SCRIPTS_DIR / "semantic_index.py"
    if index_script.exists():
        subprocess.run(
            ["python3", str(index_script)],
            cwd=str(WIKI_DIR),
            timeout=600
        )
        return True
    return False

# ── State Tracking ───────────────────────────────────────────────────────────

def load_processed():
    """Load set of processed transcript hashes."""
    if PROCESSED_FILE.exists():
        return set(json.loads(PROCESSED_FILE.read_text()))
    return set()

def save_processed(hashes):
    """Save processed transcript hashes."""
    PROCESSED_FILE.write_text(json.dumps(list(hashes)))

def content_hash(path: Path) -> str:
    """Generate content hash for a transcript."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


QUERY_LOG = WIKI_DIR / "state" / "mcp-query-log.jsonl"

def get_priority_guests(lookback_minutes=1440, max_guests=5):
    """Read recent MCP queries and return guest slugs that were asked about.
    
    Ordered by query count descending. Falls back to empty list if no log.
    """
    if not QUERY_LOG.exists():
        return []
    from datetime import timedelta
    cutoff = datetime.now() - timedelta(minutes=lookback_minutes)
    guest_queries = {}
    for line in QUERY_LOG.read_text().strip().split("\n"):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
            ts = datetime.fromisoformat(rec.get("ts", ""))
            if ts < cutoff:
                continue
            q = rec.get("query", "").lower()
            for candidate in ["marc andreessen", "sam altman", "paul graham", "reid hoffman",
                              "lenny rachitsky", "elon musk", "jeff bezos", "peter thiel",
                              "bill gurley", "ben horowitz", "jack dorsey", "mark zuckerberg",
                              "andrew chen", "patrick collison", "tobi lutke", "brian chesky",
                              "casey winters", "rahul vohra", "shreyas doshi", "matt mochary",
                              "david sacks", "naval ravikant", "steve blank", "eric ries",
                              "sam altman", "paul graham", "garry tan", "aaron levie",
                              "alexis ohanian", "kevin systrom", "jason fried",
                              "elad gil", "david heinemeier hansson", "ryan petersen"]:
                if candidate in q:
                    slug = candidate.replace(" ", "-")
                    guest_queries[slug] = guest_queries.get(slug, 0) + 1
        except (json.JSONDecodeError, ValueError, KeyError):
            continue
    sorted_guests = sorted(guest_queries.items(), key=lambda x: -x[1])
    return [g for g, c in sorted_guests[:max_guests]]

def find_new_transcripts():
    """Find transcripts not yet processed, sorted by MCP query priority."""
    processed = load_processed()
    new = []
    for transcript in RAW_DIR.rglob("*.md"):
        h = content_hash(transcript)
        if h not in processed:
            new.append((transcript, h))
    
    # Priority: process guests queried via MCP first
    priority_guests = get_priority_guests()
    if priority_guests:
        priority = []
        rest = []
        for path, h in new:
            matched = any(pg in str(path).lower() for pg in priority_guests)
            if matched:
                priority.append((path, h))
            else:
                rest.append((path, h))
        new = priority + rest
        if priority:
            print(f"Priority ordering: {len(priority)} by query demand ({', '.join(priority_guests)})")
    
    return new, processed

def write_state(phase: str, stats: dict):
    """Write current state to state/distiller-last-run.md."""
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

# ── Main Pipeline ────────────────────────────────────────────────────────────

def process_transcript(transcript_path: Path, podcast: str) -> dict:
    """Run full distillation pipeline on a single transcript."""
    stats = {"guests_updated": 0, "insights_extracted": 0, 
             "quotes_verified": 0, "topics_matched": 0, "errors": 0}
    
    try:
        text = transcript_path.read_text()
        episode_slug = transcript_path.stem
        
        # Stage 1: Guest extraction
        guest_result = extract_guests(text)
        for guest in guest_result.get("guests", []):
            from agent_lock import acquire_lock, release_lock
            if not acquire_lock("agent1"):
                print("WARNING: Could not acquire lock. Skipping guest update.")
            else:
                try:
                    update_guest_page(guest, podcast, episode_slug)
                finally:
                    release_lock("agent1")
                stats["guests_updated"] += 1
            
            # Stage 2: Insights (per guest)
            insights = extract_insights(text)
            if insights:
                update_insights_page(guest.get("name"), insights, episode_slug)
                stats["insights_extracted"] += len(insights)
            
            # Stage 3: Quotes (per guest)
            quotes = extract_quotes(text)
            verified = sum(1 for q in quotes if q.get("verified"))
            if verified > 0:
                update_quotes_page(guest.get("name"), quotes, episode_slug)
                stats["quotes_verified"] += verified
        
        # Stage 4: Topic cross-referencing
        topics = cross_reference_topics(text)
        stats["topics_matched"] += len(topics.get("matched_topics", []))
        
    except Exception as e:
        stats["errors"] += 1
        error_log = STATE_DIR / "distiller-errors.log"
        with open(error_log, "a") as f:
            f.write(f"{datetime.now().isoformat()} | {transcript_path} | {e}\n")
    
    return stats

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Podcast distillation pipeline")
    parser.add_argument("--episode", help="Process a single episode by slug")
    parser.add_argument("--podcast", help="Process transcripts from one podcast (lenny/20vc)")
    parser.add_argument("--max", type=int, default=3,
                        help="Max transcripts per run. Default 3 to avoid cron timeout.")
    args = parser.parse_args()
    
    if args.episode:
        # Single episode mode
        path = None
        for candidate in RAW_DIR.rglob(f"*{args.episode}*.md"):
            path = candidate
            break
        if not path:
            print(f"Episode not found: {args.episode}")
            return
        stats = process_transcript(path, "unknown")
        print(f"Processed {args.episode}: {stats}")
        return
    
    # Batch mode: process all new transcripts
    new_transcripts, processed_hashes = find_new_transcripts()
    
    if not new_transcripts:
        print("No new transcripts to process.")
        return
    
    print(f"Processing {len(new_transcripts)} new transcripts...")
    total_stats = {"transcripts_processed": 0, "guests_updated": 0,
                   "insights_extracted": 0, "quotes_verified": 0,
                   "topics_matched": 0, "errors": 0, "faiss_signal": False}
    
    for i, (path, h) in enumerate(new_transcripts):
        if args.max and i >= args.max:
            print(f"Hit --max limit ({args.max}), {len(new_transcripts) - args.max} remaining for next run.")
            break
        # Determine podcast from path
        podcast = "unknown"
        if "lenny" in str(path).lower():
            podcast = "lenny"
        elif "20vc" in str(path).lower():
            podcast = "20vc"
        elif "newsletter" in str(path).lower():
            podcast = "newsletters"
        
        stats = process_transcript(path, podcast)
        if stats.get("errors", 0) > 0:
            # Record failure — do NOT mark as processed
            with open(str(STATE_DIR / "failed-transcripts.md"), "a") as f:
                f.write(f"- {path} — {datetime.now().isoformat()}\n")
            # Check if we need to alert (3+ failures)
            with open(str(STATE_DIR / "failed-transcripts.md")) as f:
                failure_count = len([l for l in f.readlines() if l.startswith("- ")])
            if failure_count >= 3 and failure_count % 3 == 0:
                print(f"WARNING: {failure_count} transcript failures in state/failed-transcripts.md")
            continue
        for k, v in stats.items():
            total_stats[k] += v
        total_stats["transcripts_processed"] += 1
        processed_hashes.add(h)
        # Incremental state save — prevents losing progress on timeout/crash
        save_processed(processed_hashes)
        write_state("running", total_stats)
    
    # Signal that FAISS needs rebuilding
    with open(str(WIKI_DIR / "state" / "faiss-needs-rebuild"), "w") as f:
        f.write("1")
    
    # Save final state
    save_processed(processed_hashes)
    write_state("complete", total_stats)
    
    print(f"""
Distillation complete:
  Transcripts: {total_stats['transcripts_processed']}
  Guests: {total_stats['guests_updated']}
  Insights: {total_stats['insights_extracted']}
  Quotes verified: {total_stats['quotes_verified']}
  Topics: {total_stats['topics_matched']}
  FAISS rebuild: signalled
  Errors: {total_stats['errors']}
""")

if __name__ == "__main__":
    main()
