#!/usr/bin/env python3
"""Tag every 20VC episode with its AI/tech era based on date.
Creates data/episode-eras.json and wiki/concepts/era-<name>.md pages."""

import json
import os
from datetime import datetime
from collections import defaultdict, OrderedDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPISODE_INDEX = os.path.join(BASE_DIR, "data", "20vc-structured", "episode_index.json")
OUTPUT_ERAS = os.path.join(BASE_DIR, "data", "episode-eras.json")
CONCEPTS_DIR = os.path.join(BASE_DIR, "wiki", "concepts")

# Eras defined with (name, start_date, end_date, priority)
# Priority: higher number = higher priority when dates overlap
ERAS = [
    ("Post-Financial Crisis Recovery", "2015-01-01", "2016-06-30", 1),
    ("SaaS Scaling Era", "2016-07-01", "2018-12-31", 2),
    ("Late-Stage Boom", "2019-01-01", "2021-06-30", 3),
    ("COVID Era", "2020-03-01", "2021-12-31", 5),  # Higher priority — overlaps with Late-Stage Boom
    ("Correction & Efficiency", "2022-01-01", "2023-06-30", 4),
    ("AI Inflection", "2023-07-01", "2026-12-31", 6),  # Highest — ongoing era
]

# Era descriptions for concept pages
ERA_DESCRIPTIONS = {
    "Post-Financial Crisis Recovery": (
        "The early years of The Twenty Minute VC podcast coincided with a period of steady "
        "recovery from the 2008 financial crisis. Interest rates remained low, and venture capital "
        "was gradually returning to pre-crisis levels. The podcast launched in January 2015, "
        "capturing conversations with early-stage investors, first-time fund managers, and "
        "entrepreneurs navigating a cautious but improving fundraising environment."
    ),
    "SaaS Scaling Era": (
        "By mid-2016 the podcast shifted focus toward the SaaS boom. Cloud infrastructure "
        "(AWS, Azure) had matured, making it cheaper than ever to start a software company. "
        "The 'product-led growth' playbook was being written (Slack, Dropbox, Atlassian), and "
        "VCs were competing to back the next generation of enterprise SaaS companies. Episodes "
        "from this era emphasize unit economics, sales efficiency, and the mechanics of scaling "
        "a subscription business."
    ),
    "Late-Stage Boom": (
        "The late 2010s saw an explosion of mega-rounds,独角兽 (unicorn) companies, and "
        "record-breaking fund sizes. SoftBank's Vision Fund had disrupted traditional VC norms, "
        "pushing startups to 'go big or go home.' The podcast featured many founders of companies "
        "that would go on to IPO, as well as skeptical VCs who warned that the party couldn't last. "
        "Topics include growth at all costs, the WeWork saga, and the changing dynamics of late-stage investing."
    ),
    "COVID Era": (
        "The COVID-19 pandemic triggered a dramatic shift in how startups operated and how VCs "
        "invested. Remote work became the norm, digital adoption accelerated 3-5 years in months, "
        "and sectors like edtech, telehealth, and collaboration tools saw explosive growth. The "
        "podcast captured real-time reactions from founders navigating uncertainty, supply chain "
        "disruption, and a remote-first world. The era also saw a flood of stimulus money into "
        "venture capital, as low interest rates drove LPs to seek higher returns."
    ),
    "Correction & Efficiency": (
        "Beginning in 2022, the macro environment shifted sharply. Interest rates rose, public "
        "market multiples compressed, and the 'growth at all costs' era came to an abrupt end. "
        "Startups were told to focus on profitability, extend runway, and do more with less. The "
        "podcast featured candid conversations about layoffs, down rounds, and the new discipline "
        "of capital efficiency. ZIRP (Zero Interest Rate Phenomenon) was over, and a new playbook "
        "was being written."
    ),
    "AI Inflection": (
        "The public release of ChatGPT in late 2022, followed by GPT-4 in March 2023, triggered "
        "a seismic shift in the tech landscape. AI went from a niche research topic to the central "
        "theme of every boardroom conversation. The podcast's content pivoted dramatically: guests "
        "included AI founders, ML engineers, and investors racing to understand the implications of "
        "foundation models. Topics span agentic systems, inference costs, AI-native companies, "
        "synthetic data, and the geopolitical competition for compute. This era is ongoing."
    ),
}

# Key episodes / highlights per era (placeholder mapping, will be populated from data)
ERA_KEY_NOTABLE = {
    "Post-Financial Crisis Recovery": [
        "First episodes featuring Guy Kawasaki, Kris Jones, and early-stage VC investors",
        "Topics centered on fundraising basics, LP relationships, and angel investing",
        "Raw, early days of the podcast format — shorter episodes, single-guest interviews"
    ],
    "SaaS Scaling Era": [
        "Deep dives on SaaS metrics: CAC, LTV, NPS, and net dollar retention",
        "Rise of PLG (product-led growth) as a dominant GTM motion",
        "Growth of the European VC ecosystem featured prominently"
    ],
    "Late-Stage Boom": [
        "Record fundraising rounds and 独角兽 valuations",
        "SoftBank effect and the $100M+ round phenomenon",
        "IPO readiness, direct listings, and SPAC mania conversations"
    ],
    "COVID Era": [
        "Remote work revolution and distributed team management",
        "Digital acceleration across healthcare, education, and commerce",
        "Resilience and adaptation during global uncertainty"
    ],
    "Correction & Efficiency": [
        "Down rounds, restructurings, and the 'default alive' framework",
        "Capital efficiency and the return of unit economics discipline",
        "AI early-adopter companies (before the ChatGPT explosion)"
    ],
    "AI Inflection": [
        "ChatGPT/GPT-4 analysis and the foundation model race",
        "Agentic systems, AI-native product development, and inference economics",
        "Compute geopolitics: chip bans, data center buildout, and energy constraints"
    ],
}


def parse_date(date_str):
    """Parse a date string (YYYY-MM-DD) to a datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except (ValueError, TypeError):
        return None


def assign_era(episode_date):
    """Assign an era to a date based on the defined eras with priority."""
    dt = parse_date(episode_date)
    if not dt:
        return "Unknown"

    candidates = []
    for name, start, end, priority in ERAS:
        start_dt = parse_date(start)
        end_dt = parse_date(end)
        if start_dt and end_dt and start_dt <= dt <= end_dt:
            candidates.append((priority, name))

    if not candidates:
        return "Unknown"

    # Return highest priority era
    candidates.sort(key=lambda x: (-x[0], x[1]))
    return candidates[0][1]


def build_era_stats(tagged_episodes):
    """Build statistics for each era."""
    era_episodes = defaultdict(list)
    for ep in tagged_episodes:
        era = ep.get("era", "Unknown")
        era_episodes[era].append(ep)

    stats = {}
    for era_name, eps in era_episodes.items():
        years = sorted(set(ep.get("year", "????") for ep in eps))
        top_topics = defaultdict(int)
        guest_count = 0
        seen_guests = set()
        for ep in eps:
            g = ep.get("guest")
            if g and g not in seen_guests:
                guest_count += 1
                seen_guests.add(g)
            for t in ep.get("topics", []):
                # Clean up topic formatting
                topic_clean = t.strip("* ").strip()
                if topic_clean:
                    top_topics[topic_clean] += 1

        # Top 15 topics
        top_topics_sorted = sorted(top_topics.items(), key=lambda x: -x[1])[:15]

        stats[era_name] = {
            "count": len(eps),
            "years": years,
            "guest_count": guest_count,
            "top_topics": [{"topic": t, "count": c} for t, c in top_topics_sorted]
        }

    return stats


def create_concept_page(era_name, stats, all_tagged):
    """Create a wiki concept page for an era."""
    slug = f"era-{era_name.lower().replace(' ', '-').replace('&', 'and').replace(',', '').replace('(', '').replace(')', '')}"
    description = ERA_DESCRIPTIONS.get(era_name, "")
    notable = ERA_KEY_NOTABLE.get(era_name, [])
    era_stats = stats.get(era_name, {})

    # Get episodes for this era (sorted by date, show latest)
    era_eps = [ep for ep in all_tagged if ep.get("era") == era_name]
    era_eps.sort(key=lambda e: e.get("date", ""), reverse=True)
    top_eps = era_eps[:20]  # Show 20 most recent

    lines = [
        f"# {era_name}\n",
        f"Period: {_get_era_date_range(era_name)}\n",
        f"Episode count: **{len(era_eps)}**\n",
        f"Unique guests: **{era_stats.get('guest_count', 0)}**\n",
        f"Year range: {era_stats.get('years', [])}\n",
        "",
        "---\n",
        "",
        "## Overview\n",
        description,
        "",
        "---\n",
        "",
        "## Key Themes & Notable Episodes\n",
    ]

    if notable:
        for item in notable:
            lines.append(f"- {item}")
        lines.append("")

    # Top topics
    top_topics = era_stats.get("top_topics", [])
    if top_topics:
        lines.append("---\n")
        lines.append("## Top Topics Discussed\n")
        lines.append("")
        for t in top_topics[:10]:
            lines.append(f"- **{t['topic']}** — mentioned in {t['count']} episodes")
        lines.append("")

    # Featured episodes
    lines.append("---\n")
    lines.append("## Featured Episodes\n")
    lines.append("")
    for ep in top_eps[:15]:
        title = ep.get("title", "Untitled")
        date = ep.get("date", "")
        guest = ep.get("guest", "Unknown")
        lines.append(f"- **{title}** ({date}) — {guest}")

    lines.append("")
    lines.append("---\n")
    lines.append(f"*This page was auto-generated from episode data. Total episodes tagged: {len(era_eps)}.*\n")

    content = "\n".join(lines)
    out_path = os.path.join(CONCEPTS_DIR, f"{slug}.md")
    with open(out_path, "w") as f:
        f.write(content)

    return out_path, len(era_eps)


def _get_era_date_range(era_name):
    """Get the date range string for an era."""
    for name, start, end, _ in ERAS:
        if name == era_name:
            # Use YYYY-MM format
            return f"{start[:7]} to {end[:7]}"
    return "Unknown"


def main():
    os.makedirs(CONCEPTS_DIR, exist_ok=True)

    # Load episodes
    with open(EPISODE_INDEX, "r") as f:
        episodes = json.load(f)

    print(f"Loaded {len(episodes)} episodes from episode_index.json")

    # Tag each episode with era
    tagged = []
    era_counts = defaultdict(int)
    unknown_episodes = []

    for ep in episodes:
        episode_date = ep.get("date", "")
        era = assign_era(episode_date)

        ep_copy = dict(ep)  # Don't modify original
        ep_copy["era"] = era
        tagged.append(ep_copy)
        era_counts[era] += 1

        if era == "Unknown":
            unknown_episodes.append({
                "filename": ep.get("filename", ""),
                "title": ep.get("title", ""),
                "date": episode_date
            })

    # Build stats
    stats = build_era_stats(tagged)

    # Write episode-eras.json
    output = {
        "total_episodes": len(tagged),
        "eras": {},
        "episodes": tagged
    }

    for era_name, count in sorted(era_counts.items(), key=lambda x: -x[1]):
        era_info = {
            "count": count,
            "stats": stats.get(era_name, {}),
            "percentage": round(count / len(tagged) * 100, 1)
        }
        output["eras"][era_name] = era_info

    with open(OUTPUT_ERAS, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nEra distribution:")
    for era_name, count in sorted(era_counts.items(), key=lambda x: -x[1]):
        pct = round(count / len(tagged) * 100, 1)
        print(f"  {era_name:40s} {count:5d} ({pct:5.1f}%)")
    print(f"  {'Unknown':40s} {era_counts.get('Unknown', 0):5d}")

    if unknown_episodes:
        print(f"\n⚠ {len(unknown_episodes)} episodes with unknown era:")
        for ue in unknown_episodes[:5]:
            print(f"    {ue['filename']} — {ue['date']}")

    # Create concept pages
    print(f"\nCreating era concept pages...")
    pages_created = 0
    total_counted = 0
    for era_name in [e[0] for e in ERAS]:
        count = era_counts.get(era_name, 0)
        if count > 0:
            out_path, ep_count = create_concept_page(era_name, stats, tagged)
            pages_created += 1
            total_counted += ep_count
            print(f"  ✓ {out_path} ({ep_count} episodes)")

    # Also create an era index page
    index_lines = [
        "# AI/Tech Eras\n",
        "The 20VC podcast spans multiple distinct eras in the technology industry. "
        "Each era reflects the dominant investment thesis, founder sentiment, and "
        "macro environment of its time.\n",
        "---\n",
        "## Era Overview\n",
        ""
    ]

    for era_name in [e[0] for e in ERAS]:
        count = era_counts.get(era_name, 0)
        slug = f"era-{era_name.lower().replace(' ', '-').replace('&', 'and').replace(',', '').replace('(', '').replace(')', '')}"
        date_range = _get_era_date_range(era_name)
        pct = round(count / len(tagged) * 100, 1) if count > 0 else 0
        index_lines.append(f"- **[{era_name}]({slug})** ({date_range}) — {count} episodes ({pct}%)")
        if count > 0:
            desc = ERA_DESCRIPTIONS.get(era_name, "").split(".")[0]
            index_lines.append(f"  - {desc}.")

    index_lines.extend([
        "",
        "---\n",
        f"*Total: {len(tagged)} episodes across {len([e for e in era_counts.values() if e > 0])} active eras.*\n"
    ])

    index_path = os.path.join(CONCEPTS_DIR, "eras.md")
    with open(index_path, "w") as f:
        f.write("\n".join(index_lines))
    print(f"  ✓ {index_path} (era index)")

    print(f"\nDone! Created {pages_created} era concept pages + index → {OUTPUT_ERAS}")


if __name__ == "__main__":
    main()
