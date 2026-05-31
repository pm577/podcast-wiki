#!/usr/bin/env python3
"""
Ingest 303 ChatPRD Lenny transcripts into the podcast wiki.
Also ingests the 10 newsletter posts from lennysdata repo.
Cleans up dupes (trailing underscores), extracts YAML frontmatter,
creates episode pages, guest profiles, and topic pages.
"""

import os, re, json, shutil, yaml
from datetime import datetime

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHATPRD_DIR = os.path.join(WIKI_DIR, 'chatprd-transcripts', 'episodes')
LENNYSDATA_DIR = os.path.join(WIKI_DIR, 'lennysdata')

EPISODES_DIR = os.path.join(WIKI_DIR, 'episodes', 'lenny')
GUESTS_DIR = os.path.join(WIKI_DIR, 'guests')
TOPICS_DIR = os.path.join(WIKI_DIR, 'topics')
NEWSLETTERS_DIR = os.path.join(WIKI_DIR, 'episodes', 'newsletters')

os.makedirs(EPISODES_DIR, exist_ok=True)
os.makedirs(GUESTS_DIR, exist_ok=True)
os.makedirs(TOPICS_DIR, exist_ok=True)
os.makedirs(NEWSLETTERS_DIR, exist_ok=True)

# Track what we create
guests = {}  # guest_name -> list of episode slugs
topics = {}  # topic_name -> list of episode slugs
stats = {'chatprd_transcripts': 0, 'newsletters': 0, 'deduped': 0, 'guests': set(), 'topics': set()}

def slugify(text):
    """Create a filesystem-safe slug from a string."""
    s = text.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s)
    return s[:80]


def clean_underscore_dupes():
    """Remove episodes with trailing underscore if the normal version exists."""
    pattern = re.compile(r'^(.*?)(_+)$')
    episodes = sorted(os.listdir(CHATPRD_DIR))
    cleaned = 0
    for name in episodes:
        m = pattern.match(name)
        if m:
            base = m.group(1)
            if base in episodes:
                path = os.path.join(CHATPRD_DIR, name)
                shutil.rmtree(path)
                cleaned += 1
                stats['deduped'] += 1
                print(f"  Removed dupe: {name} (kept {base})")
    return cleaned


def yaml_safe_value(v):
    """Format a YAML value safely, quoting if it contains special characters."""
    s = str(v)
    # Check if value needs quoting
    if any(c in s for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`']):
        # Escape internal double quotes and wrap in double quotes
        s_escaped = s.replace('"', '\\"')
        return f'"{s_escaped}"'
    return s


def parse_frontmatter(path):
    """Parse YAML frontmatter from a transcript file."""
    with open(path) as f:
        content = f.read()

    parts = content.split('---')
    if len(parts) < 3:
        return {}, content, '', []

    fm_raw = parts[1].strip()
    body = '---'.join(parts[2:]).strip()

    # Use real YAML parser
    fm = yaml.safe_load(fm_raw)
    if not fm:
        return {}, body, '', []

    # Reconstruct clean frontmatter with proper quoting
    clean_fm_lines = []
    for k in ['guest', 'title', 'publish_date', 'description', 'youtube_url', 'video_id', 'duration', 'keywords']:
        v = fm.get(k)
        if v is not None:
            # Flatten single-element lists to scalar
            if isinstance(v, list):
                v = ', '.join(str(x) for x in v)
            clean_fm_lines.append(f"{k}: {yaml_safe_value(v)}")
    clean_fm_str = '\n'.join(clean_fm_lines)

    # Handle keywords
    keywords_raw = fm.get('keywords', '') or ''
    if isinstance(keywords_raw, list):
        keywords = [str(kw).strip() for kw in keywords_raw if str(kw).strip()]
    else:
        keywords = [kw.strip() for kw in str(keywords_raw).split(',') if kw.strip()]

    return fm, body, clean_fm_str, keywords


def ingest_chatprd_transcripts():
    """Ingest all 303 ChatPRD transcripts."""
    episodes = sorted(os.listdir(CHATPRD_DIR))

    for ep_dir in episodes:
        md_path = os.path.join(CHATPRD_DIR, ep_dir, 'transcript.md')
        if not os.path.isfile(md_path):
            continue

        fm, body, clean_fm, keywords = parse_frontmatter(md_path)

        guest = fm.get('guest', 'Unknown')
        title = fm.get('title', 'Lenny\'s Podcast Episode')
        publish_date = fm.get('publish_date', '')
        youtube_url = fm.get('youtube_url', '')

        # Create slug from guest name
        ep_slug = slugify(guest.split('/')[0].split('(')[0].strip())
        if not ep_slug:
            ep_slug = slugify(ep_dir)

        # Ensure unique filename
        ep_path = os.path.join(EPISODES_DIR, f"{ep_slug}.md")
        base_slug = ep_slug
        counter = 1
        while os.path.exists(ep_path):
            ep_slug = f"{base_slug}-{counter}"
            ep_path = os.path.join(EPISODES_DIR, f"{ep_slug}.md")
            counter += 1

        # Write episode page with clean frontmatter
        episode_content = f"""---
source: lenny
{clean_fm}
source_url: {youtube_url}
wiki_slug: {ep_slug}
---

{body}
"""
        with open(ep_path, 'w') as f:
            f.write(episode_content.strip() + '\n')

        stats['chatprd_transcripts'] += 1

        # Track for guest profiles
        guest_key = guest.lower().strip()
        if guest_key not in guests:
            guests[guest_key] = {'name': guest, 'episodes': [], 'slug': ep_slug.split('-')[0] if '-' in ep_slug else ep_slug}
            stats['guests'].add(guest)

        guests[guest_key]['episodes'].append({
            'slug': ep_slug,
            'title': title,
            'date': str(publish_date)[:10] if publish_date else '',
        })

        # Track for topic pages
        for kw in keywords:
            kw = kw.strip().lower()
            if kw:
                topics.setdefault(kw, []).append({
                    'slug': ep_slug,
                    'guest': guest,
                    'title': title,
                    'date': str(publish_date)[:10] if publish_date else '',
                })
                stats['topics'].add(kw)


def ingest_newsletters():
    """Ingest 10 newsletter posts from lennysdata repo."""
    nw_dir = os.path.join(LENNYSDATA_DIR, 'newsletters')
    if not os.path.isdir(nw_dir):
        print("No newsletters dir found.")
        return

    for fname in sorted(os.listdir(nw_dir)):
        if not fname.endswith('.md'):
            continue

        src = os.path.join(nw_dir, fname)

        with open(src) as f:
            content = f.read()

        # Try to extract title from first line
        lines = content.strip().split('\n')
        title = lines[0].strip('# ').strip() if lines else 'Lenny Newsletter'

        # Create wiki page
        nw_slug = fname.replace('.md', '')
        nw_path = os.path.join(NEWSLETTERS_DIR, f"{nw_slug}.md")

        nw_content = f"""---
source: lenny-newsletter
type: newsletter
title: {title}
source_url: https://www.lennysnewsletter.com
wiki_slug: {nw_slug}
---

{content}
"""
        with open(nw_path, 'w') as f:
            f.write(nw_content.strip() + '\n')

        stats['newsletters'] += 1


def write_guest_profiles():
    """Write/update guest profile pages."""
    for guest_key, data in guests.items():
        guest_name = data['name']
        ep_list = data['episodes']
        slug_base = data['slug']

        ep_list.sort(key=lambda x: x['date'], reverse=True)

        ep_links = []
        for ep in ep_list:
            date_str = ep['date'] if ep['date'] else 'unknown date'
            ep_links.append(f"- [[lenny/{ep['slug']}|{ep['title']}]] ({date_str})")

        profile_path = os.path.join(GUESTS_DIR, f"{slug_base}.md")
        profile_content = f"""---
# Guest profile: {guest_name}
---

# {guest_name}

## Episodes ({len(ep_list)})

{chr(10).join(ep_links)}

---
*Auto-generated from ChatPRD lennys-podcast-transcripts*
"""
        with open(profile_path, 'w') as f:
            f.write(profile_content.strip() + '\n')


def write_topic_pages():
    """Write topic index pages."""
    for topic_name, episodes in topics.items():
        topic_slug = slugify(topic_name)
        topic_path = os.path.join(TOPICS_DIR, f"{topic_slug}.md")

        episodes.sort(key=lambda x: x['date'], reverse=True)

        ep_links = []
        for ep in episodes:
            date_str = ep['date'] if ep['date'] else 'unknown date'
            ep_links.append(f"- [[lenny/{ep['slug']}|{ep['title']}]] — *{ep['guest']}* ({date_str})")

        # Append to existing topics if they exist
        existing = ""
        if os.path.exists(topic_path):
            existing = open(topic_path).read()

        new_content = f"""---
# Topic: {topic_name}
#source: auto-generated
---

# {topic_name}

## Episodes ({len(episodes)})

{chr(10).join(ep_links)}

"""
        # Merge with existing if there
        if existing:
            new_content = existing.rstrip() + '\n\n' + '---\n' + '\n'.join(ep_links) + '\n'

        with open(topic_path, 'w') as f:
            f.write(new_content.strip() + '\n')


def copy_chatprd_topics():
    """Copy the curated ChatPRD topic index pages into wiki topics/."""
    index_dir = os.path.join(WIKI_DIR, 'chatprd-transcripts', 'index')
    if not os.path.isdir(index_dir):
        return

    for fname in sorted(os.listdir(index_dir)):
        if not fname.endswith('.md'):
            continue
        src = os.path.join(index_dir, fname)
        dst = os.path.join(TOPICS_DIR, fname)
        if not os.path.exists(dst):
            with open(src) as f:
                content = f.read()
            # Add source attribution
            content = content.rstrip() + '\n\n---\n*Source: ChatPRD curated topic index*\n'
            with open(dst, 'w') as f:
                f.write(content)
            stats['topics'].add(fname.replace('.md', ''))


if __name__ == '__main__':
    print("=== Cleaning underscore dupes ===")
    cleaned = clean_underscore_dupes()
    print(f"  Cleaned {cleaned} dupes")

    print("\n=== Ingesting ChatPRD transcripts ===")
    ingest_chatprd_transcripts()
    print(f"  Ingested: {stats['chatprd_transcripts']} transcript files")

    print("\n=== Ingesting newsletters ===")
    ingest_newsletters()
    print(f"  Ingested: {stats['newsletters']} newsletters")

    print("\n=== Writing guest profiles ===")
    write_guest_profiles()
    print(f"  Guests: {len(guests)}")

    print("\n=== Writing topic pages ===")
    write_topic_pages()
    print(f"  Topics: {len(topics)}")

    print("\n=== Copying curated ChatPRD topic index ===")
    copy_chatprd_topics()

    print("\n=== Summary ===")
    print(f"  ChatPRD transcripts: {stats['chatprd_transcripts']}")
    print(f"  Newsletters: {stats['newsletters']}")
    print(f"  Deduped: {stats['deduped']}")
    print(f"  Unique guests: {len(guests)}")
    print(f"  Unique topics: {len(topics)}")
    print(f"  Total episodes (lenny dir): {len(os.listdir(EPISODES_DIR))}")
