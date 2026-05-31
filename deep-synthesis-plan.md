# Podcast Wiki — Narrative Synthesis Quality Plan

**Goal:** Every podcast wiki answer reads as one coherent truth distilled from hundreds of conversations, not a collection of quotes.

## What was implemented

### 1. Upgraded MCP `synthesize` tool

**File:** `~/.hermes/podcast-wiki/scripts/podcast_mcp_server_v2.py` → pushed to GitHub

**Change:** `do_synthesize` now runs 4 passes before returning data:

| Pass | Mechanism | What it produces |
|------|-----------|-----------------|
| Semantic search | FAISS v2 (14K vectors, raw + enriched) | `transcript_matches` with snippet + podcast + guest |
| Keyword episode search | Title/desc/tag matching | `keyword_matches` for recall |
| Entity/concept scan | Semantic + keyword filtered | `enriched_sources` with Key Views + body text |
| Guest profile lookup | `do_get_guest_profile` per top entity | `episode_refs` with exact titles, dates, podcast names |

**New output fields:** `enriched_sources`, `transcript_matches`, `keyword_matches`, `episode_refs` (nested in enriched sources).

### 2. Created `podcast-wiki-deep-synthesis` skill

**File:** `~/.hermes/skills/research/podcast-wiki-deep-synthesis/SKILL.md`

Encodes the full research-to-output workflow:

- **Research phase:** 5-pass pattern (synthesize → 3-5 semantic angles → keyword search → guest profiles → optional depth)
- **Output standard:** One blended narrative, no bracketed citations in body, disagreements folded in, references only at bottom
- **Prohibited patterns:** "Convergence across guests" language, guest-by-guest listing, methodology talk, bullet lists of findings, JSON dumps

### 3. Updated `podcast-wiki-karpathy` skill

Query section now points to the deep synthesis skill as the primary path.

## How the quality standard is enforced

**Trigger:** When the user asks a substantive question about the podcast wiki, this agent scans available skills. The `podcast-wiki-deep-synthesis` skill description ("Distill 300+ podcast episodes into narrative-quality answers...") should match, triggering auto-load.

**If auto-load fails:** The `podcast-wiki-karpathy` skill's "Query" section explicitly says: load `podcast-wiki-deep-synthesis` first. As long as the karpathy skill gets loaded (which it should for any podcast wiki work), the deep synthesis skill gets referenced.

**The output standard is in the skill file, which is injected into every turn where the skill is loaded.** The agent reads the rules and follows them.

## Verification checklist (from skill)

Every answer passes through:
- [ ] No bracketed citations in the body
- [ ] No "convergence" or "agrees with" meta-language
- [ ] No guest-by-guest listing — voices blend into one argument
- [ ] Disagreement folded into narrative, not a separate section
- [ ] 3-4 `##` sections with natural movement
- [ ] References section at bottom with dates and podcast names
- [ ] Answer reads as one coherent truth, not a collection of quotes
- [ ] No methodology talk ("I searched", "I found", "based on the wiki")
