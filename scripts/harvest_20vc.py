#!/usr/bin/env python3
"""
20VC RSS Harvester — Fetches episode metadata from RSS and creates wiki pages.

Since 20VC doesn't have full transcripts, this creates wiki pages from
show notes and episode metadata. Full transcripts would need a separate
transcription pipeline (OpenAI Whisper / AssemblyAI).
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
import urllib.request
import urllib.error
import html

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))
EPISODES_DIR = WIKI_DIR / "episodes" / "20vc"
GUESTS_DIR = WIKI_DIR / "guests"
TOPICS_DIR = WIKI_DIR / "topics"

for d in [EPISODES_DIR, GUESTS_DIR, TOPICS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

RSS_URLS = [
    "https://thetwentyminutevc.libsyn.com/rss",
    "https://feeds.libsyn.com/61840/rss",
]

TOPIC_KEYWORDS = {
    'venture-capital': ['venture capital', 'vc', 'fundraising', 'series a', 'fund', 'investor'],
    'founder-psychology': ['founder', 'psychology', 'mindset', 'resilience', 'grit', 'leadership'],
    'go-to-market': ['gtm', 'go-to-market', 'sales', 'revenue', 'growth', 'distribution'],
    'product-strategy': ['product', 'roadmap', 'strategy', 'vision', 'build'],
    'hiring-culture': ['hiring', 'talent', 'culture', 'team', 'recruiting', 'people'],
    'marketplaces': ['marketplace', 'network effects', 'platform', 'two-sided'],
    'fintech': ['fintech', 'finance', 'banking', 'payments', 'crypto'],
    'ai-ml': ['ai', 'artificial intelligence', 'machine learning', 'llm', 'gpt', 'model'],
    'biotech-health': ['bio', 'health', 'biotech', 'healthcare', 'pharma'],
    'enterprise-saas': ['enterprise', 'saas', 'b2b', 'software', 'cloud'],
    'deeptech-hardware': ['hardware', 'deep tech', 'robotics', 'semiconductor', 'chip'],
    'consumer': ['consumer', 'b2c', 'social', 'content', 'media'],
}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60]


def extract_topics(title, description):
    """Extract topics from episode title and description."""
    text = f"{title} {description}".lower()
    found = []
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            found.append(topic)
    return found[:5] if found else ['startups']


def fetch_rss(url):
    """Fetch and parse an RSS feed."""
    print(f"Fetching RSS: {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Clio-Podcast-Wiki/1.0'})
        response = urllib.request.urlopen(req, timeout=30)
        return response.read()
    except Exception as e:
        print(f"  Error: {e}")
        return None


def parse_episodes(xml_data):
    """Parse RSS XML into episode list."""
    episodes = []
    root = ET.fromstring(xml_data)
    
    # Handle RSS namespaces
    ns = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
          'content': 'http://purl.org/rss/1.0/modules/content/'}
    
    for item in root.findall('.//item'):
        ep = {}
        
        title_el = item.find('title')
        ep['title'] = html.unescape(title_el.text.strip()) if title_el is not None and title_el.text else 'Untitled'
        
        desc_el = item.find('description')
        ep['description'] = html.unescape(desc_el.text.strip()) if desc_el is not None and desc_el.text else ''
        # Strip HTML tags from description
        ep['description'] = re.sub(r'<[^>]+>', '', ep['description'])[:500]
        
        date_el = item.find('pubDate')
        ep['date'] = date_el.text.strip() if date_el is not None and date_el.text else ''
        
        link_el = item.find('link')
        ep['url'] = link_el.text.strip() if link_el is not None and link_el.text else ''
        
        # Try to extract guest name from title
        ep['guest'] = extract_guest(title_el.text if title_el is not None else '')
        
        # Audio URL
        audio_el = item.find('enclosure')
        if audio_el is not None:
            ep['audio_url'] = audio_el.get('url', '')
        
        # Duration
        dur_el = item.find('itunes:duration', ns)
        ep['duration'] = dur_el.text.strip() if dur_el is not None and dur_el.text else ''
        
        episodes.append(ep)
    
    return episodes


def extract_guest(title):
    """Try to extract guest name from episode title."""
    # 20VC titles often: "Episode Title | Guest Name" or "Guest Name: Episode Title"
    patterns = [
        r'\|\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*$',  # "Title | Guest Name"
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*:',        # "Guest Name: Title"
        r'with\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',       # "Title with Guest Name"
    ]
    for pattern in patterns:
        match = re.search(pattern, title)
        if match:
            return match.group(1).strip()
    return 'Unknown Guest'


def create_episode_page(ep, index):
    """Create a wiki page for a 20VC episode."""
    title = ep['title']
    date_str = ep['date']
    guest_name = ep['guest']
    guest_slug = slugify(guest_name)
    topics = extract_topics(title, ep['description'])
    
    # Parse date
    try:
        from email.utils import parsedate_to_datetime
        dt = parsedate_to_datetime(date_str)
        date_prefix = dt.strftime('%Y-%m-%d')
    except:
        date_prefix = f"2026-{index:02d}"
    
    episode_id = f"20vc-{date_prefix}-{slugify(title[:30])}"
    filename = f"{episode_id}.md"
    
    frontmatter = {
        'type': 'Episode',
        'id': episode_id,
        'podcast': '20vc',
        'episode_date': date_prefix,
        'title': title[:100],
        'guest': guest_slug,
        'tags': topics,
        'url': ep.get('url', ''),
    }
    
    body = [
        f"# {title}",
        "",
        f"**Guest:** {guest_name}",
        f"**Date:** {date_prefix}",
        f"**Topics:** {', '.join(topics)}",
        "",
        "## Summary",
        "",
        ep.get('description', 'No description available.'),
        "",
        "## Links",
        "",
        f"- [Episode URL]({ep.get('url', '')})" if ep.get('url') else "",
        "",
        "<!-- Full transcript not yet available. Will be added when transcribed. -->",
        "",
    ]
    
    content = "---\n" + json.dumps(frontmatter, indent=2) + "\n---\n\n" + "\n".join(body)
    (EPISODES_DIR / filename).write_text(content, encoding='utf-8')
    
    # Create guest page
    guest_file = GUESTS_DIR / f"{guest_slug}.md"
    if not guest_file.exists():
        guest_fm = {
            'type': 'Guest',
            'id': guest_slug,
            'name': guest_name,
            'appearances': [episode_id],
            'tags': topics,
        }
        guest_body = f"# {guest_name}\n\n**Appears in:**\n- [[{episode_id}]]\n"
        guest_content = "---\n" + json.dumps(guest_fm, indent=2) + "\n---\n\n" + guest_body
        guest_file.write_text(guest_content, encoding='utf-8')
    
    # Create topic pages
    for topic in topics:
        topic_file = TOPICS_DIR / f"{topic}.md"
        if not topic_file.exists():
            topic_fm = {
                'type': 'Topic',
                'id': topic,
                'label': topic.replace('-', ' ').title(),
                'source_podcasts': ['20vc'],
                'episodes_covered': [episode_id],
            }
            topic_body = f"# {topic_fm['label']}\n\n## Episodes\n- [[{episode_id}]]\n"
            topic_content = "---\n" + json.dumps(topic_fm, indent=2) + "\n---\n\n" + topic_body
            topic_file.write_text(topic_content, encoding='utf-8')
    
    return episode_id


def main():
    print("=== 20VC RSS Harvester ===\n")
    
    all_episodes = []
    for rss_url in RSS_URLS:
        xml_data = fetch_rss(rss_url)
        if xml_data:
            episodes = parse_episodes(xml_data)
            print(f"  Found {len(episodes)} episodes")
            all_episodes.extend(episodes)
    
    # Process ALL episodes
    recent = all_episodes
    
    print(f"\nProcessing all {len(recent)} episodes...\n")
    
    for i, ep in enumerate(recent):
        episode_id = create_episode_page(ep, i)
        print(f"  [{i+1}/{len(recent)}] ✅ {episode_id} — {ep['title'][:50]}")
    
    # Update index
    episodes_count = len(list(EPISODES_DIR.glob("*.md")))
    guests_count = len(list(GUESTS_DIR.glob("*.md")))
    topics_count = len(list(TOPICS_DIR.glob("*.md")))
    
    print(f"\n=== Done. Wiki now has {episodes_count} 20VC episodes, {guests_count} guests, {topics_count} topics ===")


if __name__ == "__main__":
    main()
