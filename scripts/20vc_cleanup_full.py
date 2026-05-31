#!/usr/bin/env python3
"""
20VC Entity Cleanup — Full pipeline (Phase 0-2).
Phase 3 (FAISS rebuild) runs after this completes.

1. Re-extract guest names from all 1,462 episode titles
2. Build old_slug → new_slug mapping
3. Rename/merge entity pages to correct names
4. Update episode frontmatter to point to correct slugs
5. Clean up topic-stubs (move to concepts/ or delete)
"""

import json, re, shutil, sys, time
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path.home() / ".hermes/podcast-wiki"
RAW_DIR = WIKI_DIR / "raw/transcripts/20vc"
ENTITIES_DIR = WIKI_DIR / "wiki/entities"
CONCEPTS_DIR = WIKI_DIR / "wiki/concepts"

tick = time.time()


def slugify(name):
    slug = name.lower().replace(' ', '-').replace("'", '').replace('.', '').replace('&', 'and')
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    return re.sub(r'-+', '-', slug).strip('-')[:60]


# Manual overrides for known edge cases
MANUAL_OVERRIDES = {
    "the-grow": "grow",
    "the-king-of-saas-jason-lemkin-managing-dire": "jason-lemkin",
    "the-most-powerful-woman-in-st": "susan-lyne",
    "the-legend-steve-ohear": "steve-ohear",
    "super-angel": "mike-walsh",
    "techcrunchs-brandon-lipman": "brandon-lipman",
}


NAME_PATTERN = r'[A-Z][a-zA-Z\'\-]+'


def extract_guest(title):
    """Extract guest name from 20VC episode title. Returns (name, confidence)."""
    orig = title
    
    # Step 1: Strip all prefixes
    title = re.sub(r'^(?:20VC|20 VC|20Product|20 Product|20Sales|Founders Friday \w+|The Twenty Minute VC)\s*\d*:?\s*', '', title).strip()
    title = re.sub(r'^\d+:?\s*', '', title).strip()
    title = re.sub(r'^The Memo:\s*', '', title).strip()
    title = re.sub(r'^Special:\s*', '', title).strip()
    
    # For topic-only episodes with no guest, return early
    if title.lower().startswith(('why ', 'how ', 'what ', 'when ', 'the ', 'is ', 'are ')):
        return "", 0.0
    
    NP = NAME_PATTERN
    
    # Pattern A: "Full Person Name on ..." — highest confidence
    m = re.search(rf'^({NP}(?:\s+{NP}){{1,3}})\s+on\s+', title)
    if m:
        name = m.group(1).strip()
        if 5 < len(name) < 50 and not re.search(r'\b(the|and|for|with|how|why|what|when|from|this|that|who|where)\b', name.lower()):
            return name, 0.9
    
    # Pattern B: "... with Guest Name" — high confidence
    m = re.search(rf'with\s+({NP}(?:\s+{NP}){{1,3}})(?:\s*[,\(]|\s*$)', title)
    if m:
        name = m.group(1).strip()
        if 5 < len(name) < 50:
            return name, 0.9
    
    # Pattern C: "... | Guest Name" at end — medium confidence
    m = re.search(rf'\|\s*({NP}(?:\s+{NP}){{1,3}}(?:\s+{NP})?)\s*$', title)
    if m:
        name = m.group(1).strip()
        if 5 < len(name) < 50:
            return name, 0.7
    
    # Pattern D: "Guest Name, Title — ..." — high confidence
    m = re.search(rf'^({NP}(?:\s+{NP}){{1,3}}),\s*(?:CEO|CTO|CPO|COO|CFO|Founder|Co-Founder|Partner|Managing|VP|Head|Chairman|Director|President|GM|GM,|SVP|EVP)', title)
    if m:
        name = m.group(1).strip()
        return name, 0.85
    
    # Pattern E: "Guest Name of Company..." 
    m = re.search(rf'^({NP}(?:\s+{NP}){{1,3}})\s+of\s+', title)
    if m:
        name = m.group(1).strip()
        if 5 < len(name) < 50:
            return name, 0.75
    
    # Pattern F: "Guest Name's ..."
    m = re.search(rf"^({NP}(?:\s+{NP}){{1,3}})'s\s+", title)
    if m:
        name = m.group(1).strip()
        return name, 0.7
    
    # Pattern G: "Interview: Guest Name"
    m = re.search(rf'Interview:\s*({NP}(?:\s+{NP}){{1,3}})', title)
    if m:
        name = m.group(1).strip()
        return name, 0.6
    
    # Pattern H: Any capitalized multi-word name
    candidates = re.findall(rf'({NP}(?:\s+{NP})+)', title)
    if candidates:
        best = max(candidates, key=len).strip()
        if 5 < len(best) < 50 and not re.search(r'(the|and|for|with|how|why|what|when)', best.lower()):
            return best, 0.4
    
    # No match — topic-only episode
    return "", 0.0


def clean_key_views(kvs):
    """Clean up key views — remove show notes cruft, keep insights."""
    cleaned = []
    for kv in kvs:
        kv = re.sub(r'^#\s+.*?\n', '', kv)
        kv = re.sub(r'\*\*Guest:.*?\*\*', '', kv)
        kv = re.sub(r'\*\*Date:.*?\*\*', '', kv)
        kv = re.sub(r'\*\*Topics:.*?\*\*', '', kv)
        kv = re.sub(r'##\s*\w+', '', kv)
        kv = kv.strip()
        if len(kv) > 20:
            # Take first sentence
            m = re.match(r'^(.+?[.!])', kv)
            if m and len(m.group(1)) > 30:
                kv = m.group(1)
            cleaned.append(kv[:200])
    return cleaned[:3]


def main():
    print("=" * 60)
    print("20VC Entity Cleanup — Phase 0-2")
    print(f"Started: {time.strftime('%H:%M:%S')}")
    print("=" * 60)
    
    # ===========================
    # Phase 0: Audit
    # ===========================
    print("\n📊 Phase 0: Audit")
    
    all_entities = list(ENTITIES_DIR.glob('*.md'))
    total_ents = len(all_entities)
    
    # Count 20VC entities (have "source: 20vc" in frontmatter)
    twentyvc_ents = []
    bad_topic_slugs = set()
    for f in all_entities:
        content = f.read_text(encoding='utf-8', errors='replace')
        if 'source: 20vc' in content:
            twentyvc_ents.append(f)
            slug = f.stem
            if re.match(r'^(the|why|how|what|when|where|this|your|from|who|in|on|for)-', slug):
                bad_topic_slugs.add(slug)
    
    print(f"  20VC entities: {len(twentyvc_ents)}")
    print(f"  Bad topic slugs: {len(bad_topic_slugs)}")
    print(f"  Total entities: {total_ents}")
    
    # ===========================
    # Phase 1: Name extraction
    # ===========================
    print(f"\n🔍 Phase 1: Name extraction ({time.strftime('%H:%M:%S')})")
    
    episode_files = sorted(RAW_DIR.glob('*.md'))
    print(f"  Processing {len(episode_files)} episodes...")
    
    mapping = {}  # episode_file -> {old_slug, new_slug, name, confidence, title}
    slug_counts = defaultdict(int)  # new_slug -> count
    
    for f in episode_files:
        content = f.read_text(encoding='utf-8', errors='replace')
        if not content.startswith('---'):
            continue
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
        try:
            fm = json.loads(parts[1])
            title = fm.get('title', '')
            old_slug = fm.get('guest', '')
            
            # Use manual override if the old slug is known-bad
            if old_slug in MANUAL_OVERRIDES:
                new_slug = MANUAL_OVERRIDES[old_slug]
                name = new_slug.replace('-', ' ').title()
                confidence = 0.95
            else:
                name, confidence = extract_guest(title)
                new_slug = slugify(name)
            
            mapping[f.name] = {
                'old_slug': old_slug,
                'new_slug': new_slug,
                'name': name,
                'confidence': confidence,
                'title': title,
            }
            slug_counts[new_slug] += 1
        except Exception as e:
            print(f"  Error on {f.name}: {e}")
    
    changed = sum(1 for v in mapping.values() if v['old_slug'] != v['new_slug'])
    low_conf = sum(1 for v in mapping.values() if v['confidence'] < 0.5)
    
    print(f"  Episodes processed: {len(mapping)}")
    print(f"  Slugs changed: {changed}")
    print(f"  Low confidence (<0.5): {low_conf}")
    print(f"  Distinct guest slugs: {len(slug_counts)}")
    
    if low_conf > 0:
        print(f"\n  Low confidence names (review needed):")
        for f_name, info in sorted(mapping.items(), key=lambda x: -x[1]['confidence']):
            if info['confidence'] < 0.5:
                print(f"    [{info['confidence']:.1f}] {info['title'][:60]}")
                print(f"           → '{info['name']}' (slug: {info['new_slug']})")
    
    # ===========================
    # Phase 2: Fix entities
    # ===========================
    print(f"\n🔧 Phase 2: Fix entities ({time.strftime('%H:%M:%S')})")
    
    # Group by new slug to handle duplicates
    slug_to_episodes = defaultdict(list)
    for f_name, info in mapping.items():
        slug_to_episodes[info['new_slug']].append((f_name, info))
    
    renamed = 0
    merged = 0
    deleted_topic_stubs = 0
    ep_fixed = 0
    skipped_same = 0
    
    # Phase 2a: Fix entity pages
    skipped_no_name = 0
    for new_slug, episodes in sorted(slug_to_episodes.items()):
        info = episodes[0][1]  # Use first episode's info
        name = info['name']
        
        # Skip topic-only episodes with no guest name
        if not name or info['confidence'] == 0.0:
            skipped_no_name += 1
            continue
        
        # Create new entity page from aggregated episode data
        new_path = ENTITIES_DIR / f"{new_slug}.md"
        
        # Check if entity already exists (from previous run or other source)
        content_parts = []
        episode_titles = []
        
        for f_name, ep_info in episodes:
            f_path = RAW_DIR / f_name
            if f_path.exists():
                ep_content = f_path.read_text(encoding='utf-8', errors='replace')
                if ep_content.startswith('---'):
                    ep_parts = ep_content.split('---', 2)
                    if len(ep_parts) >= 3:
                        try:
                            ep_fm = json.loads(ep_parts[1])
                            body = ep_parts[2]
                            summary = ""
                            m = re.search(r'(?i)(?:##\s*)?Summary\s*\n+(.*?)(?:\n##|\n---|$)', body, re.DOTALL)
                            if m:
                                summary = m.group(1).strip()
                            elif body.strip():
                                summary = body.strip()
                            episode_titles.append({
                                'title': ep_fm.get('title', ''),
                                'date': ep_fm.get('episode_date', ''),
                                'summary': summary,
                                'tags': ep_fm.get('tags', []),
                                'url': ep_fm.get('url', ''),
                            })
                        except:
                            pass
        
        # Build aggregate entity page
        if episode_titles:
            all_dates = [e['date'] for e in episode_titles if e['date']]
            all_tags = set()
            all_summaries = []
            for e in episode_titles:
                all_tags.update(e.get('tags', []))
                if e['summary']:
                    all_summaries.append(e['summary'])
            
            first_date = min(all_dates) if all_dates else ''
            last_date = max(all_dates) if all_dates else ''
            
            # Key views from summaries
            kvs = clean_key_views(all_summaries[:3])
            
            frontmatter = {
                'type': 'Entity',
                'id': new_slug,
                'name': name,
                'source': '20vc',
                'appearances': len(episode_titles),
                'first_episode': first_date,
                'last_episode': last_date,
                'tags': sorted(all_tags)[:8],
                'related_concepts': [],
                'key_views': kvs,
            }
            
            body_parts = [f"# {name}", ""]
            body_parts.append(f"**Source:** 20VC Podcast")
            body_parts.append(f"**Appearances:** {len(episode_titles)} episode{'s' if len(episode_titles) > 1 else ''}")
            if first_date:
                body_parts.append(f"**First episode:** {first_date}")
            if last_date:
                body_parts.append(f"**Last episode:** {last_date}")
            body_parts.append(f"**Tags:** {', '.join(sorted(all_tags)[:8])}")
            body_parts.append("")
            body_parts.append("## Episodes")
            body_parts.append("")
            for e in episode_titles:
                body_parts.append(f"- **{e['title']}** ({e['date']})")
            body_parts.append("")
            
            if kvs:
                body_parts.append("## Key Views")
                body_parts.append("")
                for kv in kvs:
                    body_parts.append(f"- {kv}")
                body_parts.append("")
            
            body_parts.append("## Research Context")
            body_parts.append("")
            for e in episode_titles:
                if e['summary']:
                    s = e['summary']
                    s = re.sub(r'\*\*Guest:.*?\*\*', '', s)
                    s = re.sub(r'\*\*Date:.*?\*\*', '', s)
                    s = re.sub(r'\*\*Topics:.*?\*\*', '', s)
                    s = re.sub(r'##\s*\w+', '', s)
                    s = s.strip()
                    if s:
                        body_parts.append(f"From **{e['title']}**:")
                        body_parts.append(s)
                        body_parts.append("")
            
            # YAML frontmatter
            yaml_lines = ['---']
            for k, v in frontmatter.items():
                if isinstance(v, list):
                    if all(isinstance(x, str) for x in v):
                        items = ', '.join(f'"{x}"' for x in v)
                    else:
                        items = str(v)
                    yaml_lines.append(f'{k}: [{items}]')
                elif isinstance(v, str):
                    if any(c in v for c in ':#{}[]'):
                        yaml_lines.append(f'{k}: "{v}"')
                    else:
                        yaml_lines.append(f'{k}: {v}')
                elif isinstance(v, bool):
                    yaml_lines.append(f'{k}: {"true" if v else "false"}')
                else:
                    yaml_lines.append(f'{k}: {v}')
            yaml_lines.append('---')
            
            content = '\n'.join(yaml_lines) + '\n\n' + '\n'.join(body_parts)
        else:
            continue
        
        # Check if target already exists
        if new_path.exists():
            # Merge — add episodes to existing
            existing = new_path.read_text(encoding='utf-8', errors='replace')
            existing_parts = existing.split('---', 2)
            if len(existing_parts) >= 3:
                existing_body = existing_parts[2]
                new_ep_section = '\n'.join(body_parts[body_parts.index("## Episodes"):body_parts.index("## Key Views")]) if "## Episodes" in body_parts else ""
                if new_ep_section and "## Episodes" not in existing_body:
                    existing_body += '\n\n' + new_ep_section
                elif new_ep_section:
                    for ep_item in body_parts:
                        m = re.match(r'^- \*\*(.+?)\*\*', ep_item)
                        if m and m.group(1) not in existing_body:
                            existing_body += '\n' + ep_item
                new_content = existing_parts[0] + '---' + existing_parts[1] + '---' + existing_body
                new_path.write_text(new_content, encoding='utf-8', errors='replace')
            merged += 1
        else:
            new_path.write_text(content, encoding='utf-8', errors='replace')
            renamed += 1
        
        # Delete old entity file if it had a different slug
        old_slug = info['old_slug']
        if old_slug and old_slug != new_slug:
            old_path = ENTITIES_DIR / f"{old_slug}.md"
            if old_path.exists() and old_path != new_path:
                old_path.unlink()
    
    # Phase 2b: Update episode frontmatter
    print(f"\n  Updating episode frontmatter ({time.strftime('%H:%M:%S')})...")
    
    for f_name, info in mapping.items():
        if info['old_slug'] == info['new_slug'] and info['old_slug'] not in ('unknown-guest', 'unknown', 'tbd'):
            skipped_same += 1
            continue
        
        f_path = RAW_DIR / f_name
        if not f_path.exists():
            continue
        
        content = f_path.read_text(encoding='utf-8', errors='replace')
        if not content.startswith('---'):
            continue
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
        try:
            fm = json.loads(parts[1])
            fm['guest'] = info['new_slug']
            new_fm = json.dumps(fm, indent=2)
            new_content = '---\n' + new_fm + '\n---' + parts[2]
            f_path.write_text(new_content, encoding='utf-8', errors='replace')
            ep_fixed += 1
        except:
            pass
    
    # Phase 2c: Delete topic-stubs (entities that aren't real people)
    print(f"\n  Cleaning topic stubs ({time.strftime('%H:%M:%S')})...")
    
    deleted_count = 0
    for f in twentyvc_ents:
        if not f.exists():
            continue
        slug = f.stem
        if slug in bad_topic_slugs:
            content = f.read_text(encoding='utf-8', errors='replace')
            # Check if it's a topic stub (no real person name)
            if content.startswith('---'):
                parts = content.split('---', 2)
                try:
                    fm = json.loads(parts[1])
                    name = fm.get('name', '')
                    appearances = fm.get('appearances', 0)
                    # If name looks like a topic or came from a bad extract
                    if len(name) < 10 or appearances == 0 or slug in bad_topic_slugs:
                        # Check if this slug actually has a proper entity now
                        proper_path = ENTITIES_DIR / f"{slug}.md"
                        if proper_path.exists():
                            f.unlink()
                            deleted_count += 1
                except:
                    pass
    
    # Summary
    print(f"\n{'='*60}")
    print(f"RESULTS ({time.strftime('%H:%M:%S')})")
    print(f"{'='*60}")
    print(f"  Entity pages created: {renamed}")
    print(f"  Entity pages merged: {merged}")
    print(f"  Topic-only (skipped): {skipped_no_name}")
    print(f"  Episode frontmatter fixed: {ep_fixed}")
    print(f"  Topic stubs deleted: {deleted_count}")
    print(f"  Skipped (same slug): {skipped_same}")
    print(f"  Low confidence names: {low_conf}")
    print(f"  Total time: {time.time()-tick:.0f}s")
    print()
    
    # Post-run stats (approximate - just for info)
    all_ents_after = list(ENTITIES_DIR.glob('*.md'))
    print(f"  Entities before: {total_ents}")
    print(f"  Entities after: {len(all_ents_after)}")
    
    # Save status for next phase
    status = {
        'completed_at': time.strftime('%Y-%m-%dT%H:%M:%S'),
        'entities_renamed': renamed,
        'entities_merged': merged,
        'episode_fixes': ep_fixed,
        'topic_stubs_deleted': deleted_count,
        'low_confidence_names': low_conf,
        'total_time_s': time.time() - tick,
    }
    (WIKI_DIR / '.20vc_cleanup_status.json').write_text(json.dumps(status, indent=2))
    print(f"\n  Status saved to .20vc_cleanup_status.json")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
