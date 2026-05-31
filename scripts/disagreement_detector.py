#!/usr/bin/env python3
"""
Disagreement Detector — Scans enriched entity pages for opposing views on key topics.
Generates comparison pages at wiki/comparisons/disagreements-<topic>.md

Usage:
    python3 scripts/disagreement_detector.py
"""

import os
import re
import textwrap
from collections import defaultdict, OrderedDict
from pathlib import Path

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))
ENTITIES_DIR = WIKI_DIR / "wiki" / "entities"
COMPARISONS_DIR = WIKI_DIR / "wiki" / "comparisons"
SCRIPTS_DIR = WIKI_DIR / "scripts"

MIN_LINES = 30

# ── Topic definitions ──────────────────────────────────────────────────────

TOPICS = [
    {
        "slug": "remote-work",
        "title": "Remote Work vs In-Office",
        "description": "Should teams be remote-first, hybrid, or fully in-office?",
        # Longer, more specific phrases to avoid false positives from words like "remote" or "office"
        "phrases": [
            "remote work", "working remote", "work from home", "wfh",
            "remote-first", "distributed team", "distributed company",
            "in-office", "return to office", "back to the office",
            "remote culture", "virtual meetings", "async communication",
            "hybrid work", "hybrid model", "digital by default",
            "remote sales", "remote meeting",
            "office presence", "physical proximity", "in-person",
            "zoom made", "zoom meeting",
        ],
        "pro_phrases": [
            "remote work", "working remotely", "wfh", "work from home",
            "remote-first", "distributed team", "digital by default",
            "async communication", "remote culture",
        ],
        "anti_phrases": [
            "in-office", "return to office", "back to the office",
            "office presence", "physical proximity", "in-person",
            "against remote work", "remote work.*bs", "remote.*bad",
            "remote reps don't", "remote.*doesn't work",
            "collocated team",
        ],
        "pro_label": "Remote-First / Pro-Remote",
        "anti_label": "In-Office / Pro-Proximity",
    },
    {
        "slug": "vc-value",
        "title": "VC Value: Do VCs Actually Help Startups?",
        "description": "Do venture capitalists genuinely add value beyond capital?",
        "phrases": [
            "vc add value", "venture capital adds", "venture capital adds value",
            "vc do not add value", "vc don't add", "vc value is",
            "vc value-add", "venture capital value",
            "most vcs don't", "vcs don't help",
            "vc useless", "smart money",
            "vc differentiate", "vc package",
            "investor does not add", "vc can't help",
            "venture capital is", "vc industry",
            "vc add", "vcs add",
            "vcs do not", "value extraction",
            "vc doesn't add",
        ],
        "pro_phrases": [
            "vc add value", "value-add", "venture capital adds",
            "smart money", "vc helps", "vc differentiate",
            "investor value",
            "vc adds value",
        ],
        "anti_phrases": [
            "do not add value", "don't add value", "vc useless",
            "doesn't add value", "no value from vc",
            "most vcs don't", "vc can't help",
            "investor does not add",
            "vc package startups", "not add value",
        ],
        "pro_label": "VCs Add Real Value",
        "anti_label": "VCs Don't Add Much Value",
    },
    {
        "slug": "ai-jobs",
        "title": "AI, Automation & Jobs",
        "description": "Will AI replace human jobs or augment them? What's the impact on employment?",
        "phrases": [
            "ai replace", "ai will replace", "ai replacing",
            "automation replace", "automation displaces",
            "ai augment", "ai will augment", "ai create jobs",
            "jobs at risk from ai", "job loss from ai",
            "task loss not job loss", "task loss.*job loss",
            "ai displace", "ai eliminate", "ai eliminate jobs",
            "unemployment", "job destruction",
            "productivity", "ai productivity",
            "people will lose jobs", "jobs will be lost",
            "ai will not replace", "ai won't replace",
            "human workers", "jobs at a premium",
            "demographic collapse.*jobs",
            "ai and jobs", "ai job impact",
        ],
        "pro_phrases": [
            "ai augment", "ai create jobs", "task loss not job loss",
            "job persists", "jobs at a premium",
            "productivity growth", "ai will not replace",
            "ai won't replace", "ai will help",
            "human workers at premium",
        ],
        "anti_phrases": [
            "ai replace", "ai will replace", "automation replace",
            "job loss", "ai displace", "ai eliminate",
            "unemployment", "job destruction",
            "people will lose jobs",
            "ai risk.*job",
        ],
        "pro_label": "AI Augments / Creates Jobs",
        "anti_label": "AI Displaces / Destroys Jobs",
    },
    {
        "slug": "overcapitalized",
        "title": "Overcapitalization: Can You Raise Too Much?",
        "description": "Is raising too much capital dangerous for startups? Blitzscaling vs efficiency.",
        "phrases": [
            "raise too much", "too much capital", "raise too much capital",
            "overcapitalized", "over-capitalized", "overfunded",
            "over-funded", "blitzscaling", "blitzscale",
            "too much money", "bloated teams", "bloated team",
            "dangers of raising", "raise too much",
            "capital efficiency", "runway mask",
            "growth at all costs", "big round",
            "mega round", "mega fund",
            "cash to avoid",
        ],
        "pro_phrases": [
            "blitzscale", "big round", "mega round",
            "expansion of capital", "raise more",
            "capital is healthy", "not too much capital",
            "lots of capital",
        ],
        "anti_phrases": [
            "raise too much", "overcapitalized", "over-funded",
            "too much capital", "bloated teams",
            "dangers of raising too much",
            "capital efficiency", "runway mask",
            "too much money",
            "cash to avoid making hard",
            "over-funding can mask",
        ],
        "pro_label": "Raise Big / Blitzscale",
        "anti_label": "Beware Overcapitalization / Stay Lean",
    },
    {
        "slug": "founder-vs-ceo",
        "title": "Founder CEO vs Professional CEO",
        "description": "Should founders stay as CEO or hand over to a professional manager?",
        "phrases": [
            "founder ceo", "founder CEO", "founder-mode",
            "founder mode", "founder led", "founder-led",
            "professional ceo", "professional CEO",
            "replace founder", "founder should stay",
            "founder.*ceo transition", "ceo transition",
            "ceo succession", "founder can't scale",
            "founder.*step aside", "founder.*hand over",
            "founder.*professional manager",
            "founder.*outperform", "founders outperform",
            "great founder", "great ceo",
        ],
        "pro_phrases": [
            "founder ceo", "founder-led", "founder mode",
            "founders outperform", "great founder",
            "founder should stay", "founder remain",
            "stay close to the product",
            "founder-led companies create better",
        ],
        "anti_phrases": [
            "professional ceo", "professional CEO",
            "replace founder", "ceo transition",
            "ceo succession", "founder can't scale",
            "hand over.*reins", "hire a professional",
            "step aside",
        ],
        "pro_label": "Founder CEOs Are Better",
        "anti_label": "Professional CEOs Are Better at Scale",
    },
    {
        "slug": "ai-risk",
        "title": "AI Risk: Existential Danger or Overblown?",
        "description": "Is AI an existential threat to humanity or is the risk overblown?",
        "phrases": [
            "existential risk", "ai risk", "ai danger",
            "ai safety", "xrisk", "alignment",
            "ai.*extinction", "ai.*catastrophic",
            "ai threat", "ai doomer",
            "risk.*ai.*overblown", "ai.*not dangerous",
            "alignment problem", "ai alignment",
            "should be careful.*ai",
            "existential threat.*ai",
            "dependency risk", "ai.*kill",
        ],
        "pro_phrases": [
            "existential risk", "ai safety", "alignment problem",
            "ai.*catastrophic", "ai.*extinction",
            "existential threat", "ai risk is real",
            "should be careful.*ai",
            "danger.*ai", "ai danger",
        ],
        "anti_phrases": [
            "risk.*overblown", "ai.*not dangerous",
            "overhyped risk", "not existential",
            "ai safety is distraction", "alarmist",
            "doomer", "fear.*unfounded",
        ],
        "pro_label": "AI Is a Serious Risk",
        "anti_label": "AI Risk Is Overblown",
    },
    {
        "slug": "open-source-debate",
        "title": "Open Source vs Closed Source AI",
        "description": "Should AI models and infrastructure be open source or proprietary?",
        "phrases": [
            "open source", "open-source", "closed source",
            "open weight", "open model",
            "closed model", "proprietary model",
            "open source ai", "open source model",
            "fake open source", "real open source",
            "open ecosystem",
            "open source ideals",
            "open source code",
            "open source principles",
            "gpl",
            "open source.*closed",
        ],
        "pro_phrases": [
            "open source", "open weight", "open model",
            "open ecosystem", "real open source",
            "open source ideals", "open source must be defended",
            "truly open source",
            "open source principles",
            "gpl",
        ],
        "anti_phrases": [
            "closed source", "closed model",
            "proprietary model", "proprietary.*model",
            "fake open source", "usage restrictions",
            "source available",
            "safety.*control.*open",
        ],
        "pro_label": "Pro Open Source",
        "anti_label": "Pro Proprietary / Closed",
    },
    {
        "slug": "valuation-bubble",
        "title": "Valuation Bubble: Are Startups Overvalued?",
        "description": "Are current startup valuations in a bubble? Is there an overvaluation crisis?",
        "phrases": [
            "valuation bubble", "startup valuation", "overvalued",
            "overvaluation", "valuation inflated",
            "pricing bubble", "market froth",
            "bubble", "too expensive",
            "correction coming", "not a bubble",
            "fair value", "rational pricing",
            "valuation.*justified", "valuations justified",
            "overpriced", "pricing.*insane",
            "seed pricing", "valuation.*worse",
        ],
        "pro_phrases": [
            "bubble", "overvalued", "overvaluation",
            "valuation inflated", "pricing bubble",
            "market froth", "too expensive",
            "correction coming", "pricing.*worse",
            "inflated pricing",
        ],
        "anti_phrases": [
            "not a bubble", "fair value", "justified",
            "rational pricing", "different this time",
            "sustainable", "valuations.*justified",
            "healthy market",
        ],
        "pro_label": "We're in a Bubble / Overvalued",
        "anti_label": "Valuations Are Justified",
    },
]


def count_lines(filepath):
    with open(filepath, "r") as f:
        return sum(1 for _ in f)


def load_entity_pages():
    pages = []
    for fpath in sorted(ENTITIES_DIR.glob("*.md")):
        if count_lines(fpath) >= MIN_LINES:
            pages.append(fpath)
    return pages


def extract_key_views(content, filename):
    """Extract Key Views from an entity page."""
    views = []

    # Pattern 1: ## Key Views section with numbered ### N. Title items
    key_views_match = re.search(r'##\s+Key\s*Views?\s*\n', content, re.IGNORECASE)
    if key_views_match:
        section_content = content[key_views_match.start():]
        next_heading = re.search(r'\n##\s+(?!Key\s*View)', section_content)
        if next_heading:
            section_content = section_content[:next_heading.start()]

        # ### N. Title\n\nContent
        view_pattern = re.findall(
            r'###\s+\d+\.?\s*(.+?)\n+(.+?)(?=\n###\s+\d+\.?|\n##|\Z)',
            section_content,
            re.DOTALL
        )
        if view_pattern:
            for title, text in view_pattern:
                text = text.strip()
                source_match = re.search(r'\^\[(.+?)\]', text)
                source_ref = source_match.group(1) if source_match else ""
                text_clean = re.sub(r'\^\[.+?\]', '', text).strip()
                if text_clean:
                    views.append((title.strip(), text_clean, source_ref))
            return views

    # Pattern 2: **Title** — description (bold headings, inline format)
    # Used by Marc Andreessen, Matt Mullenweg, etc.
    bold_views = re.findall(
        r'\*\*(.+?)\*\*\s*[—–-]\s*(.+?)(?=\n\*\*|\n##|\Z)',
        content,
        re.DOTALL
    )
    if bold_views:
        for title, text in bold_views:
            text = text.strip()
            source_match = re.search(r'\^\[(.+?)\]', text)
            source_ref = source_match.group(1) if source_match else ""
            text_clean = re.sub(r'\^\[.+?\]', '', text).strip()
            if text_clean:
                views.append((title.strip(), text_clean, source_ref))
        return views

    # Pattern 3: ### Title (no number) with content
    if key_views_match:
        section_content = content[key_views_match.start():]
        next_heading = re.search(r'\n##\s+(?!Key\s*View)', section_content)
        if next_heading:
            section_content = section_content[:next_heading.start()]
        view_pattern = re.findall(
            r'###\s+(.+?)\n+(.+?)(?=\n###|\n##|\Z)',
            section_content,
            re.DOTALL
        )
        for title, text in view_pattern:
            title = title.strip()
            if title.startswith('#'):
                continue
            text = text.strip()
            source_match = re.search(r'\^\[(.+?)\]', text)
            source_ref = source_match.group(1) if source_match else ""
            text_clean = re.sub(r'\^\[.+?\]', '', text).strip()
            if text_clean:
                views.append((title.strip(), text_clean, source_ref))

    return views


def extract_entity_name(content, filename):
    name_match = re.search(r'^title:\s*(.+?)$', content, re.MULTILINE)
    if name_match:
        return name_match.group(1).strip()
    return filename.stem.replace("-", " ").title()


def phrase_matches(text, phrases):
    """Check if any phrase matches in the text (case-insensitive)."""
    text_lower = text.lower()
    for phrase in phrases:
        if phrase.lower() in text_lower:
            return True
    return False


def evaluate_view_on_topic(view_text, view_title, topic):
    """
    Evaluate whether a view expresses a pro or anti stance on the topic.
    Uses phrase-level matching to avoid false positives.
    Returns ('pro', score), ('anti', score), or (None, 0).
    """
    combined = (view_title + " " + view_text).lower()

    # First check if this view is even relevant to the topic
    if not phrase_matches(combined, topic["phrases"]):
        return (None, 0)

    pro_score = 0
    anti_score = 0

    # Score pro phrases
    for phrase in topic["pro_phrases"]:
        matches = len(re.findall(re.escape(phrase.lower()), combined))
        pro_score += matches

    # Score anti phrases
    for phrase in topic["anti_phrases"]:
        matches = len(re.findall(re.escape(phrase.lower()), combined))
        anti_score += matches

    # Negation handling: if "not"/"doesn't"/"don't" appears before a phrase, flip the score
    for phrase in topic["pro_phrases"]:
        neg_pattern = r'(not|doesn\'t|don\'t|won\'t|never)\s+(?:a\s+|an\s+|the\s+)?' + re.escape(phrase.lower())
        if re.search(neg_pattern, combined):
            pro_score -= 1
            anti_score += 1

    for phrase in topic["anti_phrases"]:
        neg_pattern = r'(not|doesn\'t|don\'t|won\'t|never)\s+(?:a\s+|an\s+|the\s+)?' + re.escape(phrase.lower())
        if re.search(neg_pattern, combined):
            anti_score -= 1
            pro_score += 1

    if pro_score > anti_score:
        return ("pro", pro_score)
    elif anti_score > pro_score:
        return ("anti", anti_score)
    elif pro_score > 0:
        return ("pro", pro_score)
    elif anti_score > 0:
        return ("anti", anti_score)

    return (None, 0)


def generate_comparison_page(topic, pro_entries, anti_entries):
    """Generate a Markdown comparison page for a topic."""
    slug = topic["slug"]
    title = topic["title"]
    description = topic["description"]
    pro_label = topic["pro_label"]
    anti_label = topic["anti_label"]

    lines = []
    lines.append("---")
    lines.append(f'title: "{title}"')
    lines.append(f'created: 2026-05-31')
    lines.append(f'updated: 2026-05-31')
    lines.append("type: comparison")
    lines.append("tags:")
    lines.append("  - disagreement-detector")
    lines.append(f"  - {slug}")
    lines.append("confidence: 0.75")
    lines.append("---")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"{description}")
    lines.append("")
    lines.append("*This page was auto-generated by the disagreement detector. It clusters enriched entity pages into opposing camps based on keyword and sentiment analysis of their Key Views sections.*")
    lines.append("")

    total_pro = len(pro_entries)
    total_anti = len(anti_entries)
    lines.append("## At a Glance")
    lines.append("")
    lines.append(f"- **{pro_label}**: {total_pro} guest(s)")
    lines.append(f"- **{anti_label}**: {total_anti} guest(s)")
    lines.append("")

    if total_pro + total_anti == 0:
        lines.append("*No relevant views found for this topic.*")
        lines.append("")
        return "\n".join(lines)

    lines.append("## The Disagreement")
    lines.append("")
    all_guests_pro = ', '.join(e[0] for e in pro_entries)
    all_guests_anti = ', '.join(e[0] for e in anti_entries)
    lines.append(f"| **Side** | **Guests** |")
    lines.append(f"|---|---|")
    if pro_entries:
        lines.append(f"| **{pro_label}** | {all_guests_pro} |")
    if anti_entries:
        lines.append(f"| **{anti_label}** | {all_guests_anti} |")
    lines.append("")

    if pro_entries:
        lines.append(f"## {pro_label}")
        lines.append("")
        for name, content_snippet, source_ref in pro_entries:
            lines.append(f"### {name}")
            lines.append("")
            if content_snippet:
                lines.append(f"> {content_snippet}")
                lines.append("")
            if source_ref:
                lines.append(f"^[{source_ref}]")
                lines.append("")

    if anti_entries:
        lines.append(f"## {anti_label}")
        lines.append("")
        for name, content_snippet, source_ref in anti_entries:
            lines.append(f"### {name}")
            lines.append("")
            if content_snippet:
                lines.append(f"> {content_snippet}")
                lines.append("")
            if source_ref:
                lines.append(f"^[{source_ref}]")
                lines.append("")

    lines.append("## Methodology")
    lines.append("")
    lines.append(f"This comparison was generated by scanning {total_pro + total_anti} enriched entity pages (>={MIN_LINES} lines) for keywords related to this topic.")
    lines.append("Each relevant view was classified as pro or anti based on keyword matching with negation handling.")
    lines.append("")

    return "\n".join(lines)


def main():
    print("=" * 60)
    print("DISAGREEMENT DETECTOR v2")
    print("=" * 60)

    pages = load_entity_pages()
    print(f"\nFound {len(pages)} enriched entity pages (>= {MIN_LINES} lines)")

    COMPARISONS_DIR.mkdir(parents=True, exist_ok=True)

    for topic in TOPICS:
        slug = topic["slug"]
        print(f"\n{'─' * 60}")
        print(f"Topic: {topic['title']}")
        print(f"{'─' * 60}")

        # Use OrderedDict to deduplicate by entity name
        pro_map = OrderedDict()
        anti_map = OrderedDict()

        for fpath in pages:
            try:
                with open(fpath, "r") as f:
                    content = f.read()
            except Exception as e:
                continue

            entity_name = extract_entity_name(content, fpath.name)
            views = extract_key_views(content, fpath.name)
            if not views:
                continue

            entity_pro_score = 0
            entity_anti_score = 0
            best_pro_view = None
            best_anti_view = None

            for view_title, view_text, source_ref in views:
                stance, score = evaluate_view_on_topic(view_text, view_title, topic)
                if stance == "pro" and score > entity_pro_score:
                    entity_pro_score = score
                    best_pro_view = (entity_name, view_text[:400], source_ref)
                elif stance == "anti" and score > entity_anti_score:
                    entity_anti_score = score
                    best_anti_view = (entity_name, view_text[:400], source_ref)

            if entity_pro_score > entity_anti_score and entity_pro_score > 0:
                if entity_name not in pro_map:
                    pro_map[entity_name] = best_pro_view
            elif entity_anti_score > entity_pro_score and entity_anti_score > 0:
                if entity_name not in anti_map:
                    anti_map[entity_name] = best_anti_view
            elif entity_pro_score > 0 and entity_anti_score == 0:
                if entity_name not in pro_map:
                    pro_map[entity_name] = best_pro_view
            elif entity_anti_score > 0 and entity_pro_score == 0:
                if entity_name not in anti_map:
                    anti_map[entity_name] = best_anti_view
            elif entity_pro_score > 0 and entity_anti_score > 0:
                # Both scores positive and equal — entity holds mixed views, show in both
                if entity_name not in pro_map:
                    pro_map[entity_name] = best_pro_view
                if entity_name not in anti_map:
                    anti_map[entity_name] = best_anti_view

        pro_entries = list(pro_map.values())
        anti_entries = list(anti_map.values())

        print(f"  {topic['pro_label']}: {len(pro_entries)} guests")
        for e in pro_entries:
            print(f"    - {e[0]}")
        print(f"  {topic['anti_label']}: {len(anti_entries)} guests")
        for e in anti_entries:
            print(f"    - {e[0]}")

        page_content = generate_comparison_page(topic, pro_entries, anti_entries)
        out_path = COMPARISONS_DIR / f"disagreements-{slug}.md"
        with open(out_path, "w") as f:
            f.write(page_content)
        print(f"  → {out_path}")

    print(f"\n{'=' * 60}")
    print("DONE")
    print(f"{'=' * 60}")
    print(f"\nPages in {COMPARISONS_DIR}/disagreements-*.md")


if __name__ == "__main__":
    main()
