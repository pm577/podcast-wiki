# Podcast Wiki → "WOW" Report for Harry Stebbings

> **Goal:** Transform the podcast wiki from an episode index into a synthesis engine that answers Harry's deepest questions and makes him say "this is insane."

**Current state:** 1,462 20VC episodes ingested but mostly show notes. FAISS index surfaces episode metadata, not synthesized insights. No cross-episode synthesis exists.

**Target state:** Harry can ask any question about his 1,462 episodes and get a quote-backed, synthesised answer with disagreement maps, era comparisons, and surprise patterns.

**The gap:** Show notes → full transcript ingestion → insight extraction → cross-episode synthesis → disagreement detection → pattern surfacing.

---

## Phase 0: Audit & Diagnostics (2 tasks)

### Task 0.1: Map what 20VC content actually exists

**Objective:** Understand which 20VC episodes have full transcripts vs show notes vs nothing

**Files:**
- Analyze: `raw/transcripts/20vc/`
- Analyze: `wiki/entities/` (20VC guests)
- Analyze: `wiki/queries/` (20VC episode stubs)

**Step 1: Count content depth per episode**

Run: `cd ~/.hermes/podcast-wiki && for f in raw/transcripts/20vc/*.md; do lines=$(wc -l < "$f"); echo "$lines $(basename $f)"; done | sort -n | tail -30`

This shows which episodes have substantive content (>100 lines = likely full transcript or show notes with summary).

**Step 2: Check enriched entity pages for 20VC guests**

Run: `cd ~/.hermes/podcast-wiki && for f in wiki/entities/*.md; do if grep -q "20vc-20" "$f" 2>/dev/null; then lines=$(wc -l < "$f"); if [ "$lines" -gt 30 ]; then echo "ENRICHED: $(basename $f) ($lines)"; fi; fi; done | head -20`

Count how many 20VC guests have enriched entity pages vs stubs.

**Step 3: Report findings**

Summarize:
- `N` episodes with full transcripts (>100 lines)
- `N` episodes with show notes (20-100 lines)  
- `N` episodes with metadata only (<20 lines)
- `N` 20VC guests with enriched entity pages (>30 lines)
- `N` 20VC guests with stubs only

**Step 4: Commit**

```bash
cd ~/.hermes/podcast-wiki
git add docs/plans/2026-06-01-harry-wow-report.md
git commit -m "docs: add Harry WOW report plan"
git push
```

---

### Task 0.2: Identify Harry's "test questions" and current failure modes

**Objective:** For each of Harry's 5 test questions, document exactly what the wiki returns now and what's missing

**Files:**
- Create: `docs/harry-test-results.md`

**Step 1: Run each question through the MCP**

```bash
cd ~/.hermes/podcast-wiki
python3 -c "
from scripts.podcast_mcp_server_v2 import ask_question
questions = [
    'What do top founders say about when to fire a co-founder?',
    'Who is the most controversial 20VC guest and why?',
    \"What's the best advice for a first-time founder raising seed?\",
    'Which guests disagree on AI replacing jobs?',
    'What patterns has Harry not noticed across his own episodes?'
]
for q in questions:
    result = ask_question(q)
    print(f'Q: {q}')
    print(f'Results count: {len(result)}')
    print('---')
"
```

**Step 2: For each question, analyze the gap**

Create `docs/harry-test-results.md`:

```markdown
# Harry's Test Questions — Current State

## Q1: When to fire a co-founder?
- Current: [summarize MCP output]
- Missing: [what a WOW answer needs]
- Needed: [specific content that needs to exist]

## Q2: Most controversial guest
- Current: [summarize MCP output]
- Missing: [what a WOW answer needs]
- Needed: [specific content that needs to exist]

...
```

**Step 3: Commit**

```bash
git add docs/harry-test-results.md
git commit -m "docs: baseline Harry test results, document gaps"
git push
```

---

## Phase 1: Build a 20VC Deep Transcript Pipeline (5 tasks)

> **Core problem:** We have 1,462 20VC episodes but most are just show notes. To answer Harry's questions at depth, we need full transcripts. We can't get them from YouTube (20VC is audio-only podcast). We need to extract what we can from existing content + build a pipeline for future enrichment.

### Task 1.1: Create a 20VC content extractor from show notes

**Objective:** Extract maximum signal from existing 20VC show notes — guest bio, key topics, quotes, timestamps

**Files:**
- Create: `scripts/extract_20vc_content.py`
- Run against: `raw/transcripts/20vc/*.md`

**Step 1: Write the extractor script**

```python
#!/usr/bin/env python3
"""Extract structured content from 20VC show notes markdown files."""
import os
import re
import json
from pathlib import Path

RAW_DIR = Path.home() / ".hermes" / "podcast-wiki" / "raw" / "transcripts" / "20vc"
OUTPUT_DIR = Path.home() / ".hermes" / "podcast-wiki" / "data" / "20vc-structured"

def extract_episode_metadata(content: str, filename: str) -> dict:
    """Extract date, guest name, company, title from show notes."""
    # Extract title from first heading
    title_match = re.search(r'# (.+)', content)
    title = title_match.group(1) if title_match else filename.replace('.md', '')
    
    # Extract date from filename (format: 20vc-YYYY-MM-DD-...)
    date_match = re.search(r'20vc-(\d{4}-\d{2}-\d{2})', filename)
    date = date_match.group(1) if date_match else None
    
    # Extract guest name (often in "with Guest Name" pattern)
    guest_match = re.search(r'with\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', title)
    guest = guest_match.group(1) if guest_match else None
    
    # Extract tags/categories from the content
    tags = []
    tag_section = re.search(r'\*{2}Tags?\*{2}:?\s*(.+?)(?:\n|$)', content, re.IGNORECASE)
    if tag_section:
        tags = [t.strip() for t in tag_section.group(1).split(',')]
    
    return {
        "filename": filename,
        "title": title,
        "date": date,
        "guest": guest,
        "tags": tags,
        "word_count": len(content.split()),
        "has_summary": bool(re.search(r'## Summary', content)),
        "line_count": content.count('\n') + 1
    }

def extract_quotes(content: str) -> list:
    """Extract quoted statements from show notes."""
    quotes = []
    # Look for quoted text
    for match in re.finditer(r'"([^"]{20,500})"', content):
        quotes.append(match.group(1))
    return quotes

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    all_episodes = []
    for fpath in sorted(RAW_DIR.glob("*.md")):
        content = fpath.read_text()
        meta = extract_episode_metadata(content, fpath.name)
        meta["quotes"] = extract_quotes(content)
        all_episodes.append(meta)
    
    # Write structured index
    index_path = OUTPUT_DIR / "episode_index.json"
    with open(index_path, 'w') as f:
        json.dump(all_episodes, f, indent=2)
    
    # Print summary
    with_quotes = sum(1 for e in all_episodes if e["quotes"])
    with_summary = sum(1 for e in all_episodes if e["has_summary"])
    
    print(f"Processed {len(all_episodes)} episodes")
    print(f"  With quotes: {with_quotes}")
    print(f"  With summary section: {with_summary}")
    print(f"  Average word count: {sum(e['word_count'] for e in all_episodes) // len(all_episodes)}")

if __name__ == "__main__":
    main()
```

**Step 2: Run the extractor**

```bash
cd ~/.hermes/podcast-wiki
python3 scripts/extract_20vc_content.py
```

Expected: Shows episode counts, quote counts, summary counts.

**Step 3: Commit**

```bash
git add scripts/extract_20vc_content.py data/
git commit -m "feat: 20VC content extractor from show notes"
git push
```

---

### Task 1.2: Build a "guest career timeline" from 20VC appearances

**Objective:** Some guests appear multiple times across 2015-2026. Map who appeared when, and what they said each time. This enables "how did X's views evolve?" questions.

**Files:**
- Create: `scripts/build_guest_timeline.py`

**Step 1: Write timeline builder**

Build a script that:
1. Groups all 20VC episodes by guest name (fuzzy match multiple appearances)
2. For each guest, creates a timeline of appearances with date, title, extracted quotes
3. Outputs `data/guest-timelines/` — one JSON per multi-appearance guest
4. Highlights guests with 3+ appearances (these are the richest for Harry)

**Step 2: Run**

```bash
cd ~/.hermes/podcast-wiki
python3 scripts/build_guest_timeline.py
```

Expected output: "Found 45 guests with 2+ appearances, 12 with 3+ appearances."

**Step 3: Create enriched entity pages for repeat 20VC guests**

For each guest with 3+ appearances, create/update their entity page with:
- Timeline of appearances
- Evolution of their views
- Key quotes from each era

**Step 4: Commit**

```bash
git add scripts/build_guest_timeline.py data/guest-timelines/
git commit -m "feat: 20VC guest career timelines" 
# If entity pages were updated:
git add wiki/entities/  
git commit -m "feat: enriched repeat 20VC guests with career timelines"
git push
```

---

### Task 1.3: Build episode-era topic models

**Objective:** Tag every 20VC episode with the AI/tech era it belongs to. Enables: "what did the VC landscape look like in 2015?" vs "what did founders worry about in 2022?"

**Files:**
- Create: `scripts/era_tagger.py`

**Step 1: Define era heuristics**

Map date ranges to eras with topic heuristics:

```python
ERAS = [
    {
        "name": "Post-Financial Crisis Recovery",
        "range": ("2015-01", "2016-06"),
        "keywords": ["seed", "crowdfunding", "london tech", "angel"],
        "description": "Early 20VC days — focus on seed funding, UK tech scene, angel investing"
    },
    {
        "name": "SaaS Scaling Era",
        "range": ("2016-07", "2018-12"),
        "keywords": ["saas", "growth", "scale", "series a", "arr"],
        "description": "SaaS metrics, growth at scale, US expansion"
    },
    {
        "name": "Late-Stage Boom",
        "range": ("2019-01", "2021-06"),
        "keywords": ["late stage", "unicorn", "mega round", "ipo", "softbank"],
        "description": "Record valuations, mega rounds, SoftBank effect"
    },
    {
        "name": "COVID Era",
        "range": ("2020-03", "2021-12"),
        "keywords": ["remote", "digital transformation", "work from home", "zoom"],
        "description": "Remote work surge, digital acceleration, SPACs"
    },
    {
        "name": "Correction & Efficiency",
        "range": ("2022-01", "2023-06"),
        "keywords": ["efficiency", "down round", "layoffs", "profitability", "unit economics"],
        "description": "Market correction, focus on profitability, down rounds"
    },
    {
        "name": "AI Inflection",
        "range": ("2023-07", "2026-12"),
        "keywords": ["ai", "gpt", "llm", "foundation model", "agent", "reasoning"],
        "description": "ChatGPT era, AI-native startups, foundation models"
    }
]
```

**Step 2: Run tagger across all 20VC episodes**

Tag every episode with its era. Output to `data/episode-eras.json`.

**Step 3: Create era overview pages**

For each era, create a concept page in `wiki/concepts/era-<name>.md` that:
- Lists key themes
- Links to top episodes from that period
- Links to guests who appeared most during that era
- Links to "next era" and "previous era"

**Step 4: Commit**

```bash
git add scripts/era_tagger.py data/episode-eras.json wiki/concepts/era-*.md
git commit -m "feat: add era tagging and era overview pages for 20VC"
git push
```

---

### Task 1.4: Enrich top 50 most-listened 20VC episodes with full synthesis

**Objective:** Identify the 50 most-important 20VC episodes (recent, high-profile guests, topic coverage) and manually/automatically extract full insights.

**Files:**
- Modify: `wiki/entities/<guest>.md` for top 50 guests
- Read: `raw/transcripts/20vc/<episode>.md`

**Step 1: Identify top 50 episodes**

Criteria:
- Most recent interviews (2024-2026) — freshest for Harry
- High-profile guests (Karpathy, Altman, Andreessen, etc.)
- Episodes with longest show notes (more raw material)
- AI-focused episodes (most relevant to current questions)

**Step 2: For each episode, extract synthesized insights**

For each of the top 50, create a structured insight section in the guest's entity page:

```markdown
### [Year]: [Episode Topic]

*From: 20VC Episode [date] — "[title]"*

Key insights from this conversation:
1. **[Insight 1]** — [synthesis of what they said]
2. **[Insight 2]** — [synthesis]
3. **[Insight 3]** — [synthesis]

[direct quote if available]
^[raw/transcripts/20vc/<episode>.md]
```

**Step 3: Batch process via subagents**

Use 3 parallel `delegate_task` calls, each handling ~17 episodes:

```python
tasks = [
    {"goal": "Enrich 20 20VC guest entity pages with insights from their episode transcripts", "context": "...episodes batch 1..."},
    {"goal": "Enrich 20 20VC guest entity pages...", "context": "...batch 2..."},
    {"goal": "Enrich remaining 10 20VC guest entity pages...", "context": "...batch 3..."},
]
```

**Step 4: Commit after each batch**

```bash
git add wiki/entities/*.md
git commit -m "feat: enrich top 50 20VC guests with episode insights batch N"
git push
```

---

### Task 1.5: Build a disagreement detector

**Objective:** Find opposing views across 20VC episodes. This is the feature that will impress Harry most — "which guests disagree with each other on X?"

**Files:**
- Create: `scripts/disagreement_detector.py`
- Create: `wiki/comparisons/disagreements-yc-vs-traditional-vc.md`
- Create: `wiki/comparisons/disagreements-remote-work.md`
- Create: `wiki/comparisons/disagreements-ai-risk.md`

**Step 1: Write disagreement detector**

The detector works on entity pages (where insights are stored):

```python
"""Scan entity pages for contradictory statements on key topics."""

TOPIC_PAIRS = [
    ("remote work", ["remote", "wfh", "distributed", "in-office", "return to office"]),
    ("VC value add", ["vc value", "venture capital adds", "investor value", "board seat"]),
    ("AI replacing jobs", ["ai replace", "jobs", "automation", "unemployment", "labor"]),
    ("founder vs CEO", ["founder ceo", "replace founder", "professional ceo"]),
    ("raising too much", ["too much funding", "overcapitalized", "blitzscaling", "efficiency"]),
]
```

For each topic, scan all enriched entity pages for insights containing keywords from both sides. Cluster into "pro-X" and "anti-X" buckets. Output structured findings.

**Step 2: Create disagreement comparison pages**

For each topic with meaningful disagreement data, create a comparison page:

```markdown
# Disagreement: [Topic]

## Side A: [Position]

- **[[guest-name]]** — "[quote or summary of their view]"
- **[[guest-name]]** — "[quote]"

## Side B: [Opposing position]

- **[[guest-name]]** — "[quote]"
- **[[guest-name]]** — "[quote]"

## Who Changed Their Mind?

- **[[guest-name]]** — Said X in [year], then said Y in [year]
```

**Step 3: Commit**

```bash
git add scripts/disagreement_detector.py wiki/comparisons/disagreements-*.md
git commit -m "feat: add disagreement detection and comparison pages"
git push
```

---

## Phase 2: Upgrade the Query Engine (3 tasks)

### Task 2.1: Rebuild FAISS index with enriched entity content

**Objective:** The current FAISS index (13,445 vectors) indexes raw transcript chunks. Rebuild to ALSO index enriched entity pages and concept pages — this is where the real synthesis lives.

**Files:**
- Modify: `scripts/semantic_index.py` → `scripts/semantic_index_v2.py`

**Step 1: Design the new indexer**

The V2 indexer should:
1. Index all raw transcripts (existing behavior)
2. ALSO index all enriched entity pages (`wiki/entities/*.md` with >30 lines)
3. ALSO index all enriched concept pages (`wiki/concepts/*.md` with >30 lines)
4. Tag each vector with its source type (raw vs entity vs concept)
5. Weight entity/concept vectors higher in search results (they're more valuable)

**Step 2: Write and run**

```python
SOURCE_WEIGHTS = {
    "raw_transcript": 1.0,
    "entity_page": 2.5,   # Higher weight — synthesized insights
    "concept_page": 2.0,  # Higher weight — synthesized frameworks
}
```

**Step 3: Verify**

After rebuild:
1. Query "when to fire a co-founder" — should now return entity page content, not just episode metadata
2. Query "AI replacing jobs" — should surface disagreement pages

**Step 4: Commit**

```bash
git add scripts/semantic_index_v2.py data/faiss_index_v2/
git commit -m "feat: rebuild FAISS index with enriched entity/concept content, add source weighting"
git push
```

---

### Task 2.2: Add "Synthesis Mode" to the MCP server

**Objective:** When someone asks a question, the MCP server should not just return raw chunks — it should synthesize across sources and present a structured answer.

**Files:**
- Modify: `scripts/podcast_mcp_server_v2.py`

**Step 1: Add a `synthesize` tool that returns structured answers**

New tool: `podcast-wiki-synthesize`

Input: natural language question
Output structure:

```json
{
  "question": "...",
  "synthesis": "2-3 paragraph synthesized answer drawing from multiple episodes",
  "sources": [
    {"guest": "name", "episode": "title", "date": "YYYY-MM-DD", "insight": "what they said"},
    {"guest": "name", "episode": "title", "date": "YYYY-MM-DD", "insight": "what they said"}
  ],
  "disagreements": [
    {"topic": "...", "side_a": "view", "side_b": "opposing view", "guests": ["a", "b"]}
  ],
  "confidence": "high|medium|low"
}
```

**Step 2: Implement synthesis logic**

The synthesis works in 3 stages:
1. **Retrieve** — search FAISS + grep entity pages for relevant content
2. **Cluster** — group results by topic/viewpoint, identify disagreements
3. **Synthesize** — build structured answer from clusters

**Step 3: Test with all 5 Harry questions**

```bash
cd ~/.hermes/podcast-wiki
python3 -c "
from scripts.podcast_mcp_server_v2 import synthesize
result = synthesize('What do top founders say about when to fire a co-founder?')
print(result['synthesis'])
"
```

**Step 4: Commit**

```bash
git add scripts/podcast_mcp_server_v2.py
git commit -m "feat: add synthesis mode to MCP server with structured answers"
git push
```

---

### Task 2.3: Build a "surprise pattern" finder

**Objective:** The hardest question Harry will ask: "What patterns have I not noticed?" This needs to surface non-obvious correlations across episodes.

**Files:**
- Create: `scripts/pattern_finder.py`
- Create: `wiki/queries/surprise-patterns.md`

**Step 1: Write pattern finder**

Scan enriched entity pages for patterns:

```python
PATTERNS = [
    # Topic frequency over time
    "How did mentions of [topic] change year over year?",
    
    # Guest overlap
    "Which guests are referenced by other guests most often?",
    
    # Prediction tracking
    "Which predictions from [year] turned out correct vs wrong?",
    
    # Emotional arc
    "How did founder sentiment change from 2021 (boom) to 2023 (correction)?",
    
    # Recurring metaphors
    "What metaphors do founders use most? (e.g. 'boil the ocean', 'hair on fire')",
    
    # Company mentions
    "Which companies are mentioned most as benchmarks/references?",
]
```

**Step 2: Run and surface top 10 surprise patterns**

Create `wiki/queries/surprise-patterns.md`:

```markdown
# Surprise Patterns Across 1,462 Episodes

> Generated by analyzing 385 enriched entities + 96 enriched concepts across 1,826 episodes.

## 1. [Pattern]
Evidence: [quotes/links]
Why it's surprising: [context]

## 2. [Pattern]
...
```

**Step 3: Commit**

```bash
git add scripts/pattern_finder.py wiki/queries/surprise-patterns.md
git commit -m "feat: add surprise pattern finder, publish top 10 patterns"
git push
```

---

## Phase 3: Create the "WOW" Artifacts (2 tasks)

### Task 3.1: Build a "20VC Era Report" — interactive era comparison

**Objective:** Create a visual/graphical comparison of how the VC landscape evolved across 20VC's 11-year run.

**Files:**
- Create: `wiki/comparisons/20vc-eras-overview.md`

**Step 1: Build the era comparison page**

```markdown
# 20VC Across 11 Years: How VC Changed

## 2015-2016: The Early Days
- Dominant topics: seed funding, London tech scene, angel investing
- Typical raise: $500K-$2M
- Common guests: UK-based angels, early-stage VCs
- "VC was a relationship business, not a data business"
- Key episodes: [[20vc-001]], [[20vc-018]]

## 2017-2018: SaaS Scaling Era
- Dominant topics: growth metrics, ARR, sales efficiency
- Typical raise: $5M-$20M
- Common guests: US-based growth investors, SaaS founders
- "Metrics became the language of fundraising"
- Key episodes: [...]

... (each era with synthesized themes, quotes, key episodes)

## The Complete Arc

| Metric | 2015 | 2020 | 2025 |
|--------|------|------|------|
| Avg seed round | $1M | $3M | $5M+ |
| Time to Series A | 18-24mo | 12-18mo | 6-12mo |
| Top concern | Finding product-market fit | Scaling efficiently | AI moat |
```

**Step 2: Commit**

```bash
git add wiki/comparisons/20vc-eras-overview.md
git commit -m "feat: add 11-year 20VC era comparison report"
git push
```

---

### Task 3.2: Generate a "WOW Report" — the single page Harry sees

**Objective:** One page. Self-contained. Blows him away.

**Files:**
- Create: `HARRY_REPORT.md` (in repo root, so it's the first thing he sees when he opens the repo)

**Step 1: Build the report**

```markdown
# 20VC × Podcast Wiki: The Report

> Hey Harry — 1,462 episodes, 1,593 guests, 11 years of conversations. Here's what your show knows.

## Answering Your Questions

### Q: When to fire a co-founder?

**The consensus across 20VC guests:** [synthesized answer with quotes from 3-4 guests]

- **[[guest-a]]** says fire fast: "..." 
- **[[guest-b]]** says try mediation first: "..."
- **[[guest-c]]** says it depends on role: "..."

*Stored in: [[co-founder-conflict]], [[when-to-fire]]*

### Q: Most controversial guest?

**Based on listener reactions and topic sensitivity:** [name]

*Why:* [explanation with links]

### Q: Best seed round advice?

**Single thing that comes up most:** [synthesis]

*Sources:* [[seed-round-advice]] → links to 12 episodes

### Q: Who disagrees on AI?

**Biggest internal debate across your guests:** [synthesis with disagreement map]

### Q: What patterns have you missed?

**1. [Pattern]:**
Evidence from your episodes: [...]
Why it matters: [...]

**2. [Pattern]:**
...

---

## By the Numbers

| Metric | Value |
|--------|-------|
| Episodes analyzed | 1,462 |
| Unique guests | 1,593 |
| Years covered | 2015-2026 |
| Guests appearing 3+ times | 12 |
| Recurring topics tracked | 96 |
| Disagreements mapped | [N] |
| Surprise patterns found | 10 |

---

## How to Explore

1. **Semantic search:** Open Claude Code, point it at the MCP server, ask anything
2. **Browse the wiki:** Start at `wiki/index.md`, follow `[[wikilinks]]`
3. **Compare eras:** `wiki/comparisons/20vc-eras-overview.md`
4. **Find disagreements:** `wiki/comparisons/disagreements-*.md`
5. **Surprise patterns:** `wiki/queries/surprise-patterns.md`
```

**Step 2: Commit and push**

```bash
cd ~/.hermes/podcast-wiki
git add HARRY_REPORT.md
git commit -m "docs: add WOW report for Harry"
git push
```

**Step 3: Generate a preview for yourself**

```bash
cd ~/.hermes/podcast-wiki
cat HARRY_REPORT.md
```

Copy and send to Harry with your original message.

---

## Phase 4: Polish & Ship (2 tasks)

### Task 4.1: Run the autoresearch ratchet loop

**Objective:** Ensure wiki health score stays high after all changes.

**Files:**
- Run: `~/.hermes/autoresearch/podcast-wiki/train.py`

**Step 1: Run health check**

```bash
cd ~/.hermes/autoresearch/podcast-wiki
python3 prepare.py  # Measures current score
```

**Step 2: Run one improvement cycle**

```bash
python3 train.py  # Makes one hypothesis, keeps if score improves
```

**Step 3: Commit improvements**

```bash
cd ~/.hermes/podcast-wiki
git add -A
git commit -m "refactor: autoresearch improvements after enrichment"
git push
```

---

### Task 4.2: Final verification — test all 5 Harry questions

**Objective:** Confirm the wiki now answers all 5 questions at a "WOW" level.

**Step 1: Test each question via MCP**

For each question, run the MCP `synthesize` tool and grade output:

```python
QUESTIONS = [
    ("When to fire a co-founder?", "Synthesis with 3+ quotes from different guests, disagreement surfaced"),
    ("Most controversial guest?", "Named a guest with explanation of why, linked to episode"),
    ("Best seed round advice?", "Single clear advice point with 3+ supporting sources"),
    ("Who disagrees on AI?", "At least 2 named guests with opposing views, direct quotes"),
    ("Patterns Harry missed?", "At least 3 non-obvious patterns with evidence"),
]

for q, criteria in QUESTIONS:
    result = synthesize(q)
    grade = "PASS" if meets_criteria(result, criteria) else "FAIL"
    print(f"{grade}: {q}")
```

**Step 2: If any fail, diagnose and fix**

- FAIL on synthesis → enrich more entity pages or improve the synthesis logic
- FAIL on depth → add more 20VC transcript insights
- FAIL on disagreement → run disagreement detector with broader matching

**Step 3: Final commit**

```bash
cd ~/.hermes/podcast-wiki
git add -A
git commit -m "final: WOW-level report ready for Harry"
git push
```

---

## Effort Estimate

| Phase | Tasks | Estimated time | Parallelizable |
|-------|-------|---------------|----------------|
| 0: Audit | 2 | 15 min | No |
| 1: Pipeline | 5 | 4-6 hours | Partially (1.1/1.2 parallel, 1.3 serial) |
| 2: Query engine | 3 | 2-3 hours | Partially (2.1/2.3 parallel) |
| 3: WOW artifacts | 2 | 1 hour | Yes |
| 4: Polish | 2 | 30 min | No |
| **Total** | **14** | **~8-11 hours** | |

**Key leverage points (do these first for biggest impact):**
1. Phase 1.4 — Enrich top 50 20VC guests (this is where the depth comes from)
2. Phase 2.2 — Add synthesis mode to MCP (this is where the "wow" comes from)
3. Phase 3.2 — Build the actual report page (this is what Harry sees)

---

## Architecture Decisions

**Why enrich entity pages instead of building a separate DB?**
- Entity pages are already in the wiki, already indexed by FAISS
- Markdown is both human-readable (Harry can browse) and machine-readable (MCP can query)
- They auto-sync via git — zero infrastructure

**Why add synthesis to the MCP instead of a separate query tool?**
- MCP is the interface Harry would actually use (Claude Code)
- One tool that does both retrieval AND synthesis is simpler than a pipeline
- Harry can test it himself by asking Claude Code questions

**Why disagreement pages instead of a dynamic query?**
- Static pages with links are browseable — Harry can share them
- They survive FAISS rebuilds
- They become permanent knowledge artifacts

---

## How to Execute

This plan is designed for `subagent-driven-development`: dispatch fresh subagents per phase, with the full plan as context. Start with Phase 0 to baseline, then Phase 1.4 (highest leverage) before the rest.
