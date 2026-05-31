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
    title_match = re.search(r'# (.+)', content)
    title = title_match.group(1) if title_match else filename.replace('.md', '')
    
    date_match = re.search(r'20vc-(\d{4}-\d{2}-\d{2})', filename)
    date = date_match.group(1) if date_match else None
    
    # Extract guest from filename or title
    guest_match = re.search(r'with\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', title)
    guest = guest_match.group(1) if guest_match else None
    
    # Extract tags from YAML frontmatter
    tags = []
    tag_match = re.search(r'tags:\s*\[(.+?)\]', content)
    if tag_match:
        tags = [t.strip().strip("'") for t in tag_match.group(1).split(',')]
    
    # Extract summary section
    summary = ""
    summary_match = re.search(r'## Summary\s*\n(.*?)(?:\n##|\Z)', content, re.DOTALL)
    if summary_match:
        summary = summary_match.group(1).strip()
    
    # Extract quoted text
    quotes = []
    for match in re.finditer(r'"([^"]{20,500})"', content):
        quotes.append(match.group(1))
    
    # Extract key topics/entities mentioned
    # Look for patterns like "covers X, Y, and Z" or bullet point summaries
    topics = set()
    topic_patterns = [
        r'(?:covers?|discusses?|talks? about|deep dive into)\s+(.+?)(?:\.|,)',
        r'(?:topics?|themes?|subjects?):\s*(.+?)(?:\n|\.)',
    ]
    for pat in topic_patterns:
        for m in re.finditer(pat, content, re.IGNORECASE):
            topics.add(m.group(1).strip()[:100])
    
    year = date[:4] if date else "unknown"
    
    return {
        "filename": filename,
        "title": title,
        "date": date,
        "year": year,
        "guest": guest,
        "tags": tags,
        "topics": list(topics),
        "has_summary": bool(summary),
        "summary_preview": summary[:200] if summary else "",
        "quotes": quotes,
        "word_count": len(content.split()),
    }

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    all_episodes = []
    guests_to_episodes = {}
    years_to_episodes = {}
    
    for fpath in sorted(RAW_DIR.glob("*.md")):
        content = fpath.read_text(encoding='utf-8', errors='replace')
        meta = extract_episode_metadata(content, fpath.name)
        all_episodes.append(meta)
        
        # Index by guest
        if meta["guest"]:
            gname = meta["guest"].lower().replace(" ", "-")
            guests_to_episodes.setdefault(gname, []).append(meta["filename"])
        
        # Index by year
        years_to_episodes.setdefault(meta["year"], []).append(meta["filename"])
    
    # Write full index
    with open(OUTPUT_DIR / "episode_index.json", 'w') as f:
        json.dump(all_episodes, f, indent=2)
    
    # Write guest index
    with open(OUTPUT_DIR / "guest_index.json", 'w') as f:
        json.dump({k: v for k, v in sorted(guests_to_episodes.items()) if len(v) > 1}, f, indent=2)
    
    # Write year index
    with open(OUTPUT_DIR / "year_index.json", 'w') as f:
        json.dump(dict(sorted(years_to_episodes.items())), f, indent=2)
    
    # Statistics
    total = len(all_episodes)
    with_summary = sum(1 for e in all_episodes if e["has_summary"])
    with_quotes = sum(1 for e in all_episodes if e["quotes"])
    with_guest = sum(1 for e in all_episodes if e["guest"])
    multi_guests = {g: eps for g, eps in guests_to_episodes.items() if len(eps) > 1}
    
    print(f"=== 20VC Content Analysis ===")
    print(f"Total episodes: {total}")
    print(f"With summary section: {with_summary}")
    print(f"With extractable quotes: {with_quotes}")
    print(f"With identifiable guest: {with_guest}")
    print(f"")
    print(f"Year distribution:")
    for year in sorted(years_to_episodes.keys()):
        print(f"  {year}: {len(years_to_episodes[year])} episodes")
    print(f"")
    print(f"Guests with 2+ appearances: {len(multi_guests)}")
    for g, eps in sorted(multi_guests.items(), key=lambda x: -len(x[1]))[:15]:
        print(f"  {g}: {len(eps)} episodes")
    print(f"")
    print(f"Average word count per show note: {sum(e['word_count'] for e in all_episodes) // total}")
    print(f"Total extractable quotes: {sum(len(e['quotes']) for e in all_episodes)}")
    
    # Save top guests list for enrichment phase
    top_guests = sorted(guests_to_episodes.items(), key=lambda x: -len(x[1]))[:60]
    with open(OUTPUT_DIR / "top_guests.json", 'w') as f:
        json.dump([{"guest": g, "appearances": len(eps), "episodes": eps} for g, eps in top_guests], f, indent=2)
    
    print(f"\nTop 60 guests saved to data/20vc-structured/top_guests.json")
    print(f"\nEpisode index: data/20vc-structured/episode_index.json")

if __name__ == "__main__":
    main()
