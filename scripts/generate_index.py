#!/usr/bin/env python3
"""
Generate the podcast wiki index page from current episode files.
"""
import os
from pathlib import Path
from datetime import datetime

WIKI_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EPISODES_DIR = WIKI_DIR / 'episodes'

def read_frontmatter(filepath):
    content = filepath.read_text(encoding='utf-8', errors='replace')
    fm = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                import yaml
                fm = yaml.safe_load(parts[1]) or {}
            except:
                pass
    return fm

def main():
    try:
        import yaml
    except ImportError:
        import subprocess
        subprocess.run(['uv', 'pip', 'install', 'pyyaml'], capture_output=True)
        import yaml

    all_episodes = []
    guests = {}
    topics = {}
    
    for pod_dir in sorted(EPISODES_DIR.iterdir()):
        if not pod_dir.is_dir():
            continue
        
        for ep_file in sorted(pod_dir.glob('*.md')):
            fm = read_frontmatter(ep_file)
            
            title = fm.get('title', ep_file.stem)
            guest = fm.get('guest', '')
            date = fm.get('publish_date', fm.get('episode_date', ''))
            date_str = str(date)[:10] if date else ''
            
            tags = fm.get('topics', fm.get('tags', fm.get('keywords', '')))
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(',') if t.strip()]
            
            ep = {
                'id': ep_file.stem,
                'podcast': pod_dir.name,
                'title': title,
                'guest': guest,
                'date': date_str,
                'tags': tags,
            }
            all_episodes.append(ep)
            
            if guest:
                guest_key = guest.lower().strip()
                if guest_key not in guests:
                    guests[guest_key] = {'name': guest, 'count': 0, 'podcasts': set()}
                guests[guest_key]['count'] += 1
                guests[guest_key]['podcasts'].add(pod_dir.name)
            
            for tag in tags:
                tag = tag.strip().lower()
                if tag:
                    topics.setdefault(tag, {'count': 0, 'podcasts': set()})
                    topics[tag]['count'] += 1
                    topics[tag]['podcasts'].add(pod_dir.name)
    
    # Sort episodes by date (newest first), with no-date episodes at the end
    def sort_key(ep):
        if ep['date']:
            return (0, ep['date'])
        return (1, ep['id'])
    
    all_episodes.sort(key=sort_key, reverse=True)
    
    # Count by podcast
    by_podcast = {}
    for ep in all_episodes:
        by_podcast[ep['podcast']] = by_podcast.get(ep['podcast'], 0) + 1
    
    # Build index
    lines = []
    lines.append("# Podcast Wiki Index")
    lines.append("")
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- **Total episodes:** {len(all_episodes)}")
    for pod, count in sorted(by_podcast.items()):
        lines.append(f"  - **{pod}:** {count} episodes")
    lines.append(f"- **Unique guests:** {len(guests)}")
    lines.append(f"- **Unique topics:** {len(topics)}")
    lines.append("")
    lines.append("## By Podcast")
    lines.append("")
    
    for pod in sorted(by_podcast.keys()):
        pod_eps = [ep for ep in all_episodes if ep['podcast'] == pod]
        lines.append(f"### {pod} ({len(pod_eps)} episodes)")
        lines.append("")
        for ep in pod_eps[:50]:  # Show first 50 per podcast
            title_short = str(ep['title'])[:70]
            line = f"- [[{ep['id']}]] — {title_short}"
            if ep['date']:
                line += f" ({ep['date']})"
            lines.append(line)
        if len(pod_eps) > 50:
            lines.append(f"  *...and {len(pod_eps) - 50} more*")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## Top Guests")
    lines.append("")
    lines.append("| Guest | Episodes | Podcasts |")
    lines.append("|-------|----------|----------|")
    
    top_guests = sorted(guests.items(), key=lambda x: x[1]['count'], reverse=True)[:30]
    for key, data in top_guests:
        pods = ', '.join(sorted(data['podcasts']))
        lines.append(f"| {data['name']} | {data['count']} | {pods} |")
    
    lines.append("")
    lines.append("## Top Topics")
    lines.append("")
    for topic, data in sorted(topics.items(), key=lambda x: x[1]['count'], reverse=True)[:30]:
        pods = ', '.join(sorted(data['podcasts']))
        lines.append(f"- **{topic}:** {data['count']} episodes ({pods})")
    
    lines.append("")
    lines.append("---")
    lines.append(f"*{len(all_episodes)} episodes, {len(guests)} guests, {len(topics)} topics*")
    
    index_path = WIKI_DIR / 'index.md'
    with open(index_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    
    print(f"Index written: {index_path}")
    print(f"  {len(all_episodes)} episodes")
    print(f"  {len(guests)} guests")
    print(f"  {len(topics)} topics")

if __name__ == '__main__':
    main()
