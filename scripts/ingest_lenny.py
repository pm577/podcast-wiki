#!/usr/bin/env python3
"""
Podcast Wiki — Lenny's Podcast Ingest Pipeline

Reads Lenny's transcript files from the cloned repo and creates
Karpathy-format wiki pages: episodes, guests, topics, insights, quotes.
"""

import json
import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))
TRANSCRIPTS_DIR = WIKI_DIR / "scripts" / "lenny-transcripts" / "podcasts"
INDEX_JSON = WIKI_DIR / "scripts" / "lenny-transcripts" / "index.json"

EPISODES_DIR = WIKI_DIR / "episodes" / "lenny"
GUESTS_DIR = WIKI_DIR / "guests"
TOPICS_DIR = WIKI_DIR / "topics"
INSIGHTS_DIR = WIKI_DIR / "insights"
QUOTES_DIR = WIKI_DIR / "quotes"

for d in [EPISODES_DIR, GUESTS_DIR, TOPICS_DIR, INSIGHTS_DIR, QUOTES_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def slugify(text):
    """Convert text to a slug."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60]


def parse_transcript(content):
    """Parse a Lenny transcript into structured segments."""
    lines = content.split('\n')
    
    # Extract frontmatter
    fm = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
            except:
                pass
            content = parts[2]
    
    # Extract speaker-diarized segments
    segments = []
    current_speaker = None
    current_text = []
    
    speaker_pattern = re.compile(r'^\*\*([^*]+)\*\*\s*\(?(\d{1,2}:\d{2}(?::\d{2})?)?\)?\s*:\s*(.*)')
    
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        match = speaker_pattern.match(line)
        if match:
            if current_speaker and current_text:
                segments.append({
                    'speaker': current_speaker,
                    'text': ' '.join(current_text)
                })
            current_speaker = match.group(1).strip()
            current_text = [match.group(3).strip()] if match.group(3) else []
        elif current_speaker:
            current_text.append(line)
    
    if current_speaker and current_text:
        segments.append({
            'speaker': current_speaker,
            'text': ' '.join(current_text)
        })
    
    return fm, segments


def extract_topics_from_transcript(segments):
    """Heuristic topic extraction from transcript content."""
    topic_keywords = {
        'product-led-growth': ['plg', 'product-led', 'self-serve', 'freemium', 'product growth'],
        'go-to-market': ['gtm', 'go-to-market', 'sales motion', 'enterprise sales'],
        'fundraising': ['raising', 'series a', 'venture capital', 'pitch deck', 'investor'],
        'hiring': ['hiring', 'recruiting', 'talent', 'team building', 'culture'],
        'retention': ['retention', 'churn', 'nps', 'engagement', 'stickiness'],
        'pricing': ['pricing', 'monetization', 'revenue', 'unit economics', 'margin'],
        'leadership': ['leadership', 'management', 'ceo', 'executive', 'managing'],
        'ai-ml': ['ai', 'artificial intelligence', 'machine learning', 'llm', 'gpt'],
        'marketplace': ['marketplace', 'network effects', 'two-sided', 'platform'],
        'product-strategy': ['product strategy', 'roadmap', 'prioritization', 'backlog'],
        'startups': ['startup', 'founder', 'early stage', 'bootstrapped'],
        'saas': ['saas', 'subscription', 'annual recurring', 'arr', 'mrr'],
    }
    
    full_text = ' '.join(s['text'].lower() for s in segments)
    found_topics = set()
    
    for topic, keywords in topic_keywords.items():
        if any(kw in full_text for kw in keywords):
            found_topics.add(topic)
    
    return list(found_topics)


def extract_guests(segments):
    """Extract unique guest names (excluding the host)."""
    host_names = ['lenny rachitsky', 'lenny', 'harry stebbings', 'harry']
    guests = set()
    for seg in segments:
        name = seg['speaker'].strip().lower()
        if name not in host_names and name != '':
            guests.add(seg['speaker'].strip())
    return list(guests)


def create_episode_page(fm, guest_name, segments):
    """Create an episode wiki page."""
    title = fm.get('title', 'Untitled Episode')
    date_str = fm.get('date', '')
    guest = guest_name or fm.get('guest', 'Unknown')
    guest_slug = slugify(guest)
    topics = extract_topics_from_transcript(segments)
    word_count = fm.get('word_count', 0)
    
    # Build date-based filename
    try:
        dt = datetime.fromisoformat(date_str) if date_str else datetime.now()
        date_prefix = dt.strftime('%Y-%m-%d')
    except:
        date_prefix = 'unknown-date'
    
    episode_id = f"lenny-{date_prefix}-{guest_slug}"
    filename = f"{episode_id}.md"
    
    # Key insights — first meaningful statements from each unique speaker
    key_insights = []
    seen_speakers = set()
    for seg in segments:
        speaker = seg['speaker'].strip()
        if speaker.lower() not in ['lenny rachitsky', 'lenny', ''] and speaker not in seen_speakers:
            text = seg['text'][:200].strip()
            if text and len(text) > 40:
                key_insights.append(f"{speaker}: {text}...")
                seen_speakers.add(speaker)
                if len(key_insights) >= 5:
                    break
    
    if not key_insights:
        for seg in segments[:3]:
            key_insights.append(seg['text'][:200].strip())
    
    frontmatter = {
        'type': 'Episode',
        'id': episode_id,
        'podcast': 'lenny',
        'episode_date': date_prefix,
        'title': title,
        'guest': guest_slug,
        'tags': topics[:8],
        'word_count': word_count,
        'key_insights': key_insights[:5],
    }
    
    # Build body
    body_lines = [f"# {title}", ""]
    if fm.get('description'):
        body_lines.append(fm['description'])
        body_lines.append("")
    
    body_lines.append(f"**Guest:** {guest}")
    body_lines.append(f"**Date:** {date_prefix}")
    if fm.get('youtube_url'):
        body_lines.append(f"**YouTube:** {fm['youtube_url']}")
    body_lines.append(f"**Topics:** {', '.join(topics)}")
    body_lines.append("")
    
    body_lines.append("## Key Topics Discussed")
    body_lines.append("")
    for topic in topics:
        body_lines.append(f"- [[{topic}]]")
    body_lines.append("")
    
    body_lines.append("## Transcript Highlights")
    body_lines.append("")
    # Add a reasonable chunk of the transcript
    transcript_text = ""
    for seg in segments[:30]:
        transcript_text += f"**{seg['speaker']}:** {seg['text']}\n\n"
    body_lines.append(transcript_text)
    
    content = "---\n" + yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True) + "---\n\n" + "\n".join(body_lines)
    
    (EPISODES_DIR / filename).write_text(content, encoding='utf-8')
    return episode_id, guest_slug, topics


def create_guest_page(guest_name, episode_id):
    """Create or update a guest wiki page."""
    guest_slug = slugify(guest_name)
    filename = f"{guest_slug}.md"
    filepath = GUESTS_DIR / filename
    
    if filepath.exists():
        # Update existing — add episode reference
        content = filepath.read_text(encoding='utf-8')
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1]) or {}
                except:
                    fm = {}
                if 'appearances' not in fm:
                    fm['appearances'] = []
                if episode_id not in fm['appearances']:
                    fm['appearances'].append(episode_id)
                new_fm = "---\n" + yaml.dump(fm, default_flow_style=False) + "---"
                content = new_fm + parts[2]
                filepath.write_text(content, encoding='utf-8')
        return guest_slug
    
    frontmatter = {
        'type': 'Guest',
        'id': guest_slug,
        'name': guest_name,
        'appearances': [episode_id],
        'tags': [],
    }
    
    body = f"# {guest_name}\n\n"
    body += f"**Appears in:**\n"
    body += f"- [[{episode_id}]]\n"
    body += "\n## Topics Covered\n\n"
    body += "<!-- Auto-populated as episodes are ingested -->\n"
    
    content = "---\n" + yaml.dump(frontmatter, default_flow_style=False) + "---\n\n" + body
    filepath.write_text(content, encoding='utf-8')
    return guest_slug


def create_topic_pages(topics, episode_id):
    """Create or update topic wiki pages."""
    for topic in topics:
        filename = f"{topic}.md"
        filepath = TOPICS_DIR / filename
        
        if filepath.exists():
            content = filepath.read_text(encoding='utf-8')
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        fm = yaml.safe_load(parts[1]) or {}
                    except:
                        fm = {}
                    if 'episodes_covered' not in fm:
                        fm['episodes_covered'] = []
                    if episode_id not in fm['episodes_covered']:
                        fm['episodes_covered'].append(episode_id)
                    new_fm = "---\n" + yaml.dump(fm, default_flow_style=False) + "---"
                    content = new_fm + parts[2]
                    filepath.write_text(content, encoding='utf-8')
            continue
        
        frontmatter = {
            'type': 'Topic',
            'id': topic,
            'label': topic.replace('-', ' ').title(),
            'source_podcasts': ['lenny'],
            'episodes_covered': [episode_id],
            'key_guests': [],
        }
        
        body = f"# {frontmatter['label']}\n\n"
        body += "## Episodes\n\n"
        body += f"- [[{episode_id}]]\n\n"
        body += "## Key Insights\n\n"
        body += "<!-- Auto-populated as episodes are ingested -->\n\n"
        body += "## Key Guests\n\n"
        body += "<!-- Auto-populated as episodes are ingested -->\n"
        
        content = "---\n" + yaml.dump(frontmatter, default_flow_style=False) + "---\n\n" + body
        filepath.write_text(content, encoding='utf-8')


def update_index():
    """Regenerate index.md with current state."""
    episodes = sorted(EPISODES_DIR.glob("*.md"))
    guests = sorted(GUESTS_DIR.glob("*.md"))
    topics = sorted(TOPICS_DIR.glob("*.md"))
    
    lines = ["# Podcast Knowledge Wiki — Content Index", "", f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}", 
             f"**Podcasts indexed:** Lenny's Podcast, 20VC", 
             f"**Total episodes:** {len(episodes)}", f"**Total guests:** {len(guests)}", 
             f"**Total topics:** {len(topics)}", "", "---", "", "## Episodes", ""]
    
    for ep in episodes[-20:]:  # Most recent 20
        content = ep.read_text(encoding='utf-8')
        title = "Untitled"
        date = ""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1]) or {}
                    title = fm.get('title', 'Untitled')
                    date = fm.get('episode_date', '')
                except:
                    pass
        lines.append(f"- [[{ep.stem}]] — {title} ({date})")
    
    lines.extend(["", "## Guests", ""])
    for g in guests:
        content = g.read_text(encoding='utf-8')
        name = g.stem.replace('-', ' ').title()
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1]) or {}
                    name = fm.get('name', name)
                except:
                    pass
        lines.append(f"- [[{g.stem}|{name}]]")
    
    lines.extend(["", "## Topics", ""])
    for t in topics:
        label = t.stem.replace('-', ' ').title()
        lines.append(f"- [[{t.stem}]] — {label}")
    
    content = "\n".join(lines)
    (WIKI_DIR / "index.md").write_text(content, encoding='utf-8')
    print(f"Index updated: {len(episodes)} episodes, {len(guests)} guests, {len(topics)} topics")


def main():
    print("=== Lenny's Podcast Ingest Pipeline ===")
    
    if not INDEX_JSON.exists():
        print(f"ERROR: index.json not found at {INDEX_JSON}")
        return 1
    
    index = json.loads(INDEX_JSON.read_text(encoding='utf-8'))
    podcasts = index.get('podcasts', [])
    
    print(f"Found {len(podcasts)} podcast entries in index.json")
    
    for i, entry in enumerate(podcasts):
        filename = entry.get('filename', '')
        # Strip "podcasts/" prefix if present (index.json includes it)
        if filename.startswith('podcasts/'):
            filename = filename[len('podcasts/'):]
        filepath = TRANSCRIPTS_DIR / filename
        
        if not filepath.exists():
            print(f"  [{i+1}/{len(podcasts)}] SKIP: {filename} not found")
            continue
        
        content = filepath.read_text(encoding='utf-8', errors='replace')
        fm, segments = parse_transcript(content)
        
        if not segments:
            print(f"  [{i+1}/{len(podcasts)}] SKIP: {filename} — no transcript segments")
            continue
        
        guest_name = entry.get('guest', fm.get('guest', 'Unknown'))
        episode_id, guest_slug, topics = create_episode_page(fm, guest_name, segments)
        create_guest_page(guest_name, episode_id)
        create_topic_pages(topics, episode_id)
        
        print(f"  [{i+1}/{len(podcasts)}] ✅ {episode_id} — {fm.get('title', 'Untitled')[:50]} ({len(topics)} topics)")
    
    update_index()
    print("\n=== Pipeline Complete ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
