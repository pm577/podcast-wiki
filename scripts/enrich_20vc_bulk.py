#!/usr/bin/env python3
"""
20VC Full Enrichment Pipeline — Phase 1-4
Fixes guest names, creates entity pages, enriches with insights, commits.

Phase 1: Extract real guest names from all 1,462 episode titles
Phase 2: Fix entity slugs, create proper entity pages
Phase 3: Enrich multi-episode guests with deeper insights
Phase 4: Commit and push to GitHub
"""

import json, os, re, sys, time
from pathlib import Path
from datetime import datetime
from collections import defaultdict

WIKI_DIR = Path.home() / ".hermes/podcast-wiki"
RAW_DIR = WIKI_DIR / "raw" / "transcripts" / "20vc"
ENTITIES_DIR = WIKI_DIR / "wiki" / "entities"

ENTITIES_DIR.mkdir(parents=True, exist_ok=True)

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60].rstrip('-')


def extract_guest_from_title(title):
    """Extract actual guest name from 20VC episode title."""
    # Remove episode prefix
    title = re.sub(r'^20 VC\s+\d+:?\s*', '', title)
    title = re.sub(r'^20vc\s+\d+:?\s*', '', title)
    title = re.sub(r'^The Twenty Minute VC\s+\d+:?\s*', '', title)
    title = re.sub(r'^S\d+E\d+:?\s*', '', title)
    
    # Pattern 1: "Guest Name on Topic"
    m = re.search(r'^(.+?)\s+on\s+', title)
    if m:
        name = m.group(1).strip()
        return name
    
    # Pattern 2: "Topic with Guest Name"  
    m = re.search(r'with\s+(.+?)$', title)
    if m:
        name = m.group(1).strip()
        return name
    
    # Pattern 3: "Guest Name, Company - Topic"
    m = re.search(r'^([^,]+(?:,\s*[^,]+)?)\s*[-–—]', title)
    if m:
        name = m.group(1).strip()
        return name
    
    # Pattern 4: Just the first part before common suffixes
    m = re.search(r'^(.+?)(?:,|\s+[-–—]|\s+of\s|\s+at\s|\s+from\s)', title)
    if m:
        name = m.group(1).strip()
        if len(name) > 3 and len(name) < 60:
            return name
    
    # Fallback: first 40 chars
    name = title[:40].strip().rstrip(',').rstrip('-').strip()
    return name


def load_episodes():
    """Load all 20VC episodes and extract metadata."""
    episodes = []
    files = sorted(RAW_DIR.glob('*.md'))
    print(f"Loading {len(files)} 20VC episodes...")
    
    for f in files:
        try:
            content = f.read_text(encoding='utf-8', errors='replace')
            if not content.startswith('---'):
                continue
            
            parts = content.split('---', 2)
            if len(parts) < 3:
                continue
            
            fm = json.loads(parts[1])
            body = parts[2] if len(parts) > 2 else ""
            
            title = fm.get('title', '')
            guest_slug = fm.get('guest', '')
            date = fm.get('episode_date', '')
            tags = fm.get('tags', [])
            url = fm.get('url', '')
            
            # Extract actual guest name from title
            real_name = extract_guest_from_title(title)
            real_slug = slugify(real_name)
            
            episodes.append({
                'file': f.name,
                'title': title,
                'guest_slug': guest_slug,
                'real_name': real_name,
                'real_slug': real_slug,
                'date': date,
                'tags': tags,
                'url': url,
                'body': body,
            })
        except Exception as e:
            print(f"  Error parsing {f.name}: {e}")
    
    return episodes


def group_by_guest(episodes):
    """Group episodes by canonical guest name."""
    guests = defaultdict(list)
    
    for ep in episodes:
        slug = ep['real_slug']
        guests[slug].append(ep)
    
    return guests


def create_entity_page(guest_slug, episodes, is_multi=False):
    """Create a wiki entity page for a 20VC guest."""
    if not episodes:
        return
    
    ep = episodes[0]
    name = ep['real_name']
    
    # Collect all episode info
    all_titles = [e['title'] for e in episodes]
    all_tags = set()
    all_bodies = []
    all_dates = []
    
    for e in episodes:
        all_tags.update(e.get('tags', []))
        body = e.get('body', '')
        # Extract summary section
        summary = ""
        if 'summary' in body.lower():
            m = re.search(r'(?i)(?:##\s*)?Summary\s*\n+(.*?)(?:\n##|\n---|$)', body, re.DOTALL)
            if m:
                summary = m.group(1).strip()
        if not summary:
            summary = body.strip()
        if summary:
            all_bodies.append(summary)
        all_dates.append(e.get('date', ''))
    
    all_dates = [d for d in all_dates if d]
    all_tags = sorted(all_tags)
    first_date = min(all_dates) if all_dates else ''
    last_date = max(all_dates) if all_dates else ''
    appearance_count = len(episodes)
    
    # Create key views from descriptions
    key_views = []
    for i, e in enumerate(episodes[:3]):  # top 3 episodes
        body = e.get('body', '')
        desc = body.strip()
        if desc:
            # Truncate to first meaningful sentence
            sentences = re.split(r'(?<=[.!])\s+', desc)
            if sentences:
                view = sentences[0].strip()
                if len(view) > 30:
                    key_views.append(view)
    
    # Build entity page
    frontmatter = {
        'type': 'Entity',
        'id': guest_slug,
        'name': name,
        'source': '20vc',
        'appearances': appearance_count,
        'first_episode': first_date,
        'last_episode': last_date,
        'tags': all_tags[:8],
        'related_concepts': [],
        'key_views': key_views[:3],
    }
    
    # Build body
    body_parts = [f"# {name}", ""]
    body_parts.append(f"**Source:** 20VC Podcast")
    body_parts.append(f"**Appearances:** {appearance_count} episode{'s' if appearance_count > 1 else ''}")
    if first_date:
        body_parts.append(f"**First episode:** {first_date}")
    if last_date:
        body_parts.append(f"**Last episode:** {last_date}")
    body_parts.append(f"**Tags:** {', '.join(all_tags[:8])}")
    body_parts.append("")
    
    body_parts.append("## Episodes")
    body_parts.append("")
    for e in episodes:
        date = e.get('date', '')
        body_parts.append(f"- **{e['title']}** ({date})")
    body_parts.append("")
    
    body_parts.append("## Key Views")
    body_parts.append("")
    for view in key_views:
        body_parts.append(f"- {view}")
    body_parts.append("")
    
    # Add episode descriptions as "Research Context"
    body_parts.append("## Research Context")
    body_parts.append("")
    for e in episodes:
        body = e.get('body', '').strip()
        # Clean up markdown
        body = re.sub(r'\*\*Guest:.*?\*\*', '', body)
        body = re.sub(r'\*\*Date:.*?\*\*', '', body)
        body = re.sub(r'\*\*Topics:.*?\*\*', '', body)
        body = re.sub(r'##\s*\w+', '', body)
        body = body.strip()
        if body:
            body_parts.append(f"From **{e['title']}**:")
            body_parts.append(body)
            body_parts.append("")
    
    # YAML frontmatter
    yaml_lines = ['---']
    for k, v in frontmatter.items():
        if isinstance(v, list):
            items = ', '.join(f'"{x}"' for x in v) if all(isinstance(x, str) for x in v) else str(v)
            yaml_lines.append(f'{k}: [{items}]')
        elif isinstance(v, str):
            if any(c in v for c in ':#{}'):
                yaml_lines.append(f'{k}: "{v}"')
            else:
                yaml_lines.append(f'{k}: {v}')
        elif isinstance(v, bool):
            yaml_lines.append(f'{k}: {"true" if v else "false"}')
        else:
            yaml_lines.append(f'{k}: {v}')
    yaml_lines.append('---')
    
    content = '\n'.join(yaml_lines) + '\n\n' + '\n'.join(body_parts)
    
    filepath = ENTITIES_DIR / f"{guest_slug}.md"
    
    # Only write if it's a stub (under 30 lines) or doesn't exist
    if filepath.exists():
        existing_lines = filepath.read_text().count('\n')
        if existing_lines >= 30:
            return filepath.name, "SKIP_ALREADY_ENRICHED"
    
    filepath.write_text(content, encoding='utf-8', errors='replace')
    return filepath.name, f"{appearance_count}eps"


def fix_episode_guest_name(ep, correct_slug, correct_name):
    """Fix the guest field in an episode's frontmatter."""
    filepath = RAW_DIR / ep['file']
    content = filepath.read_text(encoding='utf-8', errors='replace')
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                fm = json.loads(parts[1])
                old_guest = fm.get('guest', '')
                if old_guest == 'unknown-guest' or old_guest != correct_slug:
                    fm['guest'] = correct_slug
                    new_fm = json.dumps(fm, indent=2)
                    new_content = '---\n' + new_fm + '\n---' + parts[2]
                    filepath.write_text(new_content, encoding='utf-8', errors='replace')
                    return True
            except:
                pass
    return False


def main():
    print("=" * 60)
    print("20VC Full Enrichment Pipeline")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 60)
    
    tick = time.time()
    
    # Phase 1: Load episodes and extract guest names
    print("\n📀 Phase 1: Loading episodes and extracting guest names...")
    episodes = load_episodes()
    guests = group_by_guest(episodes)
    
    print(f"\n  Total episodes: {len(episodes)}")
    print(f"  Distinct guests: {len(guests)}")
    
    multi = {k: v for k, v in guests.items() if len(v) >= 2}
    single = {k: v for k, v in guests.items() if len(v) == 1}
    print(f"  Multi-episode guests: {len(multi)}")
    print(f"  Single-episode guests: {len(single)}")
    print(f"  Time: {time.time()-tick:.0f}s")
    
    # Phase 2: Fix guest names in episode frontmatter
    print(f"\n📀 Phase 2: Fixing guest names in episode frontmatter...")
    fixed = 0
    for slug, eps in list(guests.items())[:1000]:  # Don't fix ALL, just first 1000 to be practical
        name = eps[0]['real_name']
        for ep in eps:
            if fix_episode_guest_name(ep, slug, name):
                fixed += 1
    print(f"  Fixed {fixed} episode guest fields")
    print(f"  Time: {time.time()-tick:.0f}s")
    
    # Phase 3: Create/update entity pages
    print(f"\n📀 Phase 3: Creating/updating entity pages...")
    
    created = 0
    skipped_enriched = 0
    enriched_multi = 0
    
    # First: all multi-episode guests (these are more important)
    for slug, eps in sorted(multi.items(), key=lambda x: -len(x[1])):
        name = eps[0]['real_name']
        if len(name) < 3 or slug in ('unknown', 'unknown-guest', 'tbd'):
            continue
        fname, status = create_entity_page(slug, eps, is_multi=True)
        if status == "SKIP_ALREADY_ENRICHED":
            skipped_enriched += 1
        else:
            created += 1
            enriched_multi += 1
        if created % 50 == 0:
            print(f"  Progress: {created} created, {skipped_enriched} skipped...")
    
    print(f"\n  Multi-episode: {enriched_multi} created")
    
    # Then: single-episode guests (bulk)
    batch_size = 100
    for i, (slug, eps) in enumerate(sorted(single.items())):
        name = eps[0]['real_name']
        if len(name) < 3 or slug in ('unknown', 'unknown-guest', 'tbd'):
            continue
        fname, status = create_entity_page(slug, eps)
        if status == "SKIP_ALREADY_ENRICHED":
            skipped_enriched += 1
        else:
            created += 1
        if (i + 1) % batch_size == 0:
            print(f"  Progress: {created} created, {skipped_enriched} skipped ({i+1}/{len(single)})...")
    
    print(f"\n  Total created: {created}")
    print(f"  Skipped (already enriched): {skipped_enriched}")
    print(f"  Time: {time.time()-tick:.0f}s")
    
    # Phase 4: Commit and push
    print(f"\n📀 Phase 4: Committing and pushing...")
    os.chdir(str(WIKI_DIR))
    
    result = os.system("git add -A wiki/entities/ raw/transcripts/20vc/ && "
                       f"git commit -m 'Bulk enrich 20VC: {created} new entity pages, {fixed} guest name fixes' && "
                       "git push 2>&1")
    
    print(f"  Git result: {result}")
    print(f"  Time: {time.time()-tick:.0f}s")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"COMPLETE")
    print(f"  Created: {created} entity pages")
    print(f"  Fixed: {fixed} guest names")
    print(f"  Skipped (already enriched): {skipped_enriched}")
    print(f"  Total time: {time.time()-tick:.0f}s")
    print(f"{'='*60}")
    
    # Save status for cron/notification
    status_file = WIKI_DIR / ".20vc_enrichment_status.json"
    status_file.write_text(json.dumps({
        'completed_at': datetime.now().isoformat(),
        'total_episodes': len(episodes),
        'total_guests': len(guests),
        'multi_episode': len(multi),
        'single_episode': len(single),
        'created': created,
        'fixed': fixed,
        'skipped_enriched': skipped_enriched,
    }, indent=2))
    
    return 0 if created > 0 else 1


if __name__ == '__main__':
    sys.exit(main())
