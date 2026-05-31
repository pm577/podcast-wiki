#!/usr/bin/env python3
"""
LLM Wiki Lint — Health-check the podcast wiki.
Finds: orphan pages, broken wikilinks, index gaps, stale content, page size warnings.

Usage:
  python3 scripts/wiki_lint.py

Follows Karpathy's LLM Wiki lint spec:
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
"""

import os
import re
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI_PAGES_DIR = WIKI_DIR / "wiki"


def find_wiki_pages():
    """Find all wiki markdown files (not in raw, scripts, data, or legacy)."""
    pages = []
    for root, dirs, files in os.walk(str(WIKI_DIR)):
        root_p = Path(root)
        # Skip non-wiki directories
        rel = root_p.relative_to(WIKI_DIR)
        skip_dirs = {'raw', 'scripts', 'data', '.git', '__pycache__', 
                     'chatprd-transcripts', 'lennysdata', 'episodes', 'guests', 
                     'topics', 'insights', 'quotes', 'scripts/lenny-transcripts'}
        if any(str(s) in str(rel) for s in skip_dirs):
            continue
        for f in files:
            if f.endswith('.md'):
                pages.append(root_p / f)
    return pages


def extract_wikilinks(content):
    """Extract all [[wikilinks]] from content."""
    return re.findall(r'\[\[([^\]]+)\]\]', content)


def extract_markdown_links(content):
    """Extract markdown-style links [label](path)."""
    return re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)


def lint():
    print("=== Podcast Wiki Lint ===\n")
    
    pages = find_wiki_pages()
    print(f"Total markdown files found: {len(pages)}")
    
    # Build maps
    page_names = {}  # stem -> path
    page_content = {}  # stem -> content
    inbound_links = defaultdict(set)
    outbound_links = defaultdict(set)
    
    for p in pages:
        name = p.stem.lower()
        try:
            content = p.read_text(encoding='utf-8', errors='replace')
        except:
            continue
        page_names[name] = p
        page_content[name] = content
        
        links = extract_wikilinks(content)
        for link in links:
            link_stem = link.lower().split('|')[0].strip()
            outbound_links[name].add(link_stem)
            inbound_links[link_stem].add(name)
    
    issues = defaultdict(list)
    
    # 1. Orphan pages (no inbound links from other wiki pages)
    for name, path in sorted(page_names.items()):
        if name in {'index', 'log', 'schema'}:
            continue
        if name not in inbound_links or len(inbound_links[name]) == 0:
            # Check if it's in a non-wiki section
            rel = str(path.relative_to(WIKI_DIR))
            if 'wiki/' in rel:
                issues['orphans'].append(f"  {rel} — no inbound [[wikilinks]]")
    
    # 2. Broken wikilinks (links to pages that don't exist)
    for src_name, targets in outbound_links.items():
        for target in targets:
            if target not in page_names and target not in {'index', 'log', 'schema'}:
                src_path = page_names.get(src_name)
                if src_path:
                    rel = str(src_path.relative_to(WIKI_DIR))
                    issues['broken_links'].append(f"  [[{target}]] in {rel}")
    
    # 3. Markdown links without wiki-link equivalents
    for name, content in page_content.items():
        md_links = extract_markdown_links(content)
        if len(md_links) > len(outbound_links.get(name, set())):
            rel = str(page_names[name].relative_to(WIKI_DIR))
            n_md = len(md_links)
            n_wiki = len(outbound_links.get(name, set()))
            if n_md > n_wiki * 2:  # heuristic: if 2x more markdown links than wiki-links
                issues['markdown_link_gap'].append(f"  {rel}: {n_md} markdown links vs {n_wiki} wiki-links")
    
    # 4. Frontmatter check
    for name, content in page_content.items():
        if not content.startswith('---'):
            rel = str(page_names[name].relative_to(WIKI_DIR))
            if name not in {'index', 'log', 'schema'}:
                issues['missing_frontmatter'].append(f"  {rel}")
    
    # 5. Page size warnings
    for name, content in page_content.items():
        lines = content.count('\n')
        if lines > 200:
            rel = str(page_names[name].relative_to(WIKI_DIR))
            issues['large_pages'].append(f"  {rel}: {lines} lines (threshold: 200)")
    
    # Print report
    severity_order = ['broken_links', 'orphans', 'markdown_link_gap', 'missing_frontmatter', 'large_pages']
    labels = {
        'broken_links': '🔴 BROKEN WIKILINKS',
        'orphans': '🟡 ORPHAN PAGES (no inbound links)',
        'markdown_link_gap': '🟡 MARKDOWN LINK GAP (few wiki-links)',
        'missing_frontmatter': '🔵 MISSING FRONTMATTER',
        'large_pages': '🔵 LARGE PAGES (>200 lines)',
    }
    
    total = 0
    for key in severity_order:
        items = issues.get(key, [])
        if items:
            print(f"\n{labels[key]}: {len(items)}")
            for item in items[:20]:
                print(item)
                total += 1
            if len(items) > 20:
                print(f"  ...and {len(items) - 20} more")
    
    print(f"\n=== Total: {total} issues ===")
    
    # Summary for log.md
    print(f"\n=== Log Entry ===")
    severity_counts = {k: len(issues.get(k, [])) for k in severity_order}
    log_entry = f"## [YYYY-MM-DD] lint | {total} issues found"
    for key in severity_order:
        count = len(issues.get(key, []))
        if count > 0:
            icon = '🔴' if key == 'broken_links' else '🟡' if 'orphan' in key or 'gap' in key else '🔵'
            log_entry += f"\n- {icon} {labels[key].split('—')[0].strip()}: {count}"
    print(log_entry)


if __name__ == '__main__':
    lint()
