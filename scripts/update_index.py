#!/usr/bin/env python3
"""
Regenerate the podcast wiki index.md with current state.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))


def read_frontmatter(filepath):
    content = filepath.read_text(encoding='utf-8', errors='replace')
    fm = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                fm = json.loads(parts[1])
            except:
                try:
                    import yaml
                    fm = yaml.safe_load(parts[1]) or {}
                except:
                    pass
    return fm


def main():
    episodes_by_podcast = {}
    guests = {}
    topics = {}
    
    episodes_dir = WIKI_DIR / "episodes"
    if episodes_dir.exists():
        for pod_dir in sorted(episodes_dir.iterdir()):
            if not pod_dir.is_dir():
                continue
            episodes = []
            for ep_file in sorted(pod_dir.glob("*.md"), reverse=True):
                fm = read_frontmatter(ep_file)
                episodes.append({
                    'id': ep_file.stem,
                    'title': fm.get('title', 'Untitled'),
                    'date': fm.get('episode_date', ''),
                    'guest': fm.get('guest', ''),
                })
            episodes_by_podcast[pod_dir.name] = episodes
    
    guests_dir = WIKI_DIR / "guests"
    if guests_dir.exists():
        for gf in sorted(guests_dir.glob("*.md")):
            fm = read_frontmatter(gf)
            guests[gf.stem] = {
                'name': fm.get('name', gf.stem),
                'appearances': len(fm.get('appearances', [])),
            }
    
    topics_dir = WIKI_DIR / "topics"
    if topics_dir.exists():
        for tf in sorted(topics_dir.glob("*.md")):
            fm = read_frontmatter(tf)
            topics[tf.stem] = {
                'label': fm.get('label', tf.stem),
                'episodes': len(fm.get('episodes_covered', [])),
                'podcasts': fm.get('source_podcasts', []),
            }
    
    total_episodes = sum(len(eps) for eps in episodes_by_podcast.values())
    
    lines = [
        "# Podcast Knowledge Wiki — Content Index",
        "",
        f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Total episodes:** {total_episodes}",
        f"**Total guests:** {len(guests)}",
        f"**Total topics:** {len(topics)}",
        "",
        "---",
        "",
        "## Quick Start",
        "",
        "Query this wiki with the MCP server:",
        "",
        "```bash",
        "# From Claude Code or any MCP client:",
        '# search for episodes:  {"tool": "search_episodes", "params": {"query": "product-led growth"}}',
        '# get guest profile:   {"tool": "get_guest_profile", "params": {"name": "Lenny Rachitsky"}}',
        '# find insights:       {"tool": "find_insights", "params": {"topic": "go-to-market"}}',
        "# run: python3 ~/.hermes/podcast-wiki/scripts/podcast_mcp_server.py --schema",
        "```",
        "",
        "---",
        "",
    ]
    
    for podcast_name, episodes in episodes_by_podcast.items():
        label = "Lenny's Podcast" if podcast_name == 'lenny' else "20VC" if podcast_name == '20vc' else podcast_name
        lines.append(f"## {label} ({len(episodes)} episodes)")
        lines.append("")
        for ep in episodes[:20]:
            lines.append(f"- [[{ep['id']}]] — {ep['title'][:70]} ({ep['date']})")
        if len(episodes) > 20:
            lines.append(f"- *...and {len(episodes) - 20} more episodes*")
        lines.append("")
    
    lines.extend([
        "---",
        "",
        "## Guests ({})".format(len(guests)),
        "",
    ])
    
    for gid, ginfo in sorted(guests.items(), key=lambda x: x[1]['appearances'], reverse=True)[:20]:
        lines.append(f"- [[{gid}]] — {ginfo['name']} ({ginfo['appearances']} episodes)")
    if len(guests) > 20:
        lines.append(f"- *...and {len(guests) - 20} more guests*")
    
    lines.extend([
        "",
        "---",
        "",
        "## Topics ({})".format(len(topics)),
        "",
    ])
    
    for tid, tinfo in sorted(topics.items(), key=lambda x: x[1]['episodes'], reverse=True):
        lines.append(f"- [[{tid}]] — {tinfo['label']} ({tinfo['episodes']} episodes, {', '.join(tinfo['podcasts'])})")
    
    content = "\n".join(lines)
    (WIKI_DIR / "index.md").write_text(content, encoding='utf-8')
    print(f"Index updated: {total_episodes} episodes, {len(guests)} guests, {len(topics)} topics")


if __name__ == "__main__":
    main()
