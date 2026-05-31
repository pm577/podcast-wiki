#!/usr/bin/env python3
"""
Batch process 20VC transcript show notes into wiki entity pages.
Extracts guest names, creates entity pages with metadata.
"""

import json
import os
import re
import glob

TRANSCRIPTS_DIR = os.path.expanduser("~/.hermes/podcast-wiki/raw/transcripts/20vc")
ENTITIES_DIR = os.path.expanduser("~/.hermes/podcast-wiki/wiki/entities")

def slug_to_name(slug):
    """Convert a slug like 'mike-seibel' to 'Mike Seibel'."""
    if not slug or slug == 'unknown-guest' or slug == 'tech':
        return None
    parts = slug.split('-')
    name_parts = []
    for p in parts:
        if p.lower() in ('of', 'the', 'and', 'for', 'with', 'on', 'in', 'at', 'by', 'to', 'a', 'an'):
            name_parts.append(p.lower())
        else:
            name_parts.append(p.capitalize())
    return ' '.join(name_parts)

def extract_name_from_title(title):
    """Extract guest name from episode title."""
    # Pattern 1: "with {Name}" at end
    m = re.search(r'\bwith\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,-].*)?$', title)
    if m:
        return m.group(1).strip()
    
    # Pattern 2: "with {Name}'s" at end
    m = re.search(r"\bwith\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})'s\b", title)
    if m:
        return m.group(1).strip()
    
    # Pattern 3: "{Name} of {Company}" at start (after episode number)
    m = re.search(r'(?:20\s*VC\s*\d+[:\s]*|20VC:?\s*)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+of\s+', title)
    if m:
        return m.group(1).strip()
    
    # Pattern 4: "{Name} on {Topic}" at start
    m = re.search(r'(?:20\s*VC\s*\d+[:\s]*|20VC:?\s*)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+on\s+', title)
    if m:
        return m.group(1).strip()
    
    # Pattern 5: Title starts with a person's name (for newer format without episode numbers)
    m = re.match(r'(?:20VC:\s*)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}):\s', title)
    if m:
        return m.group(1).strip()
    
    # Pattern 6: "{Name}, {Role}"  
    m = re.search(r'(?:20\s*VC\s*\d+[:\s]*|20VC:?\s*)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}),\s+(?:Co-Founder|Founder|CEO|Partner|Principal|GP|Managing|Author)', title)
    if m:
        return m.group(1).strip()
    
    # Pattern 7: Just name at beginning
    m = re.match(r'(?:20\s*VC\s*\d+[:\s]*|20VC:?\s*)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[-,—]|\s*$)', title)
    if m:
        name = m.group(1).strip()
        # Filter out common non-person starting words
        skip_words = {'The', 'How', 'Why', 'What', 'Inside', 'From', 'Is', 'Are', 'Has', 'This', 'That', 'These'}
        if name not in skip_words:
            return name
    
    return None

def guess_name_from_filepath(episode_file):
    """Try to extract name from the file path itself."""
    basename = os.path.basename(episode_file)
    # Pattern: 20vc-YYYY-MM-DD-20vc-{name}-on-...
    # Or: 20vc-YYYY-MM-DD-{name}-on-...
    m = re.search(r'\d{4}-\d{2}-\d{2}(?:-20vc|-20sales|-20product|-20growth)?-(.+?)(?:-on-|-with-|-of-|-and-|--)', basename)
    if m:
        name_part = m.group(1)
        # Convert hyphens to spaces and capitalize
        parts = name_part.split('-')
        # Filter out known non-name patterns
        junk = {'the', 'how', 'why', 'what', 'inside', 'from', 'is', 'why', 'who', 'and', 'for'}
        filtered = [p.capitalize() for p in parts if p.lower() not in junk]
        if filtered and len(filtered) >= 2:
            return ' '.join(filtered)
    return None

def make_slug(name):
    """Convert a name to a slug."""
    return name.lower().replace(' ', '-').replace("'", '').replace('.', '').replace(',', '')

def entity_exists(name):
    """Check if an entity page already exists."""
    slug = make_slug(name)
    path = os.path.join(ENTITIES_DIR, f"{slug}.md")
    if os.path.exists(path):
        return True
    
    # Also check if it has ## Key Views
    if os.path.exists(path):
        with open(path) as f:
            content = f.read()
            if '## Key Views' in content:
                return True
    return False

def create_entity(name, tags, source_file, episode_title):
    """Create an entity page for a guest."""
    slug = make_slug(name)
    path = os.path.join(ENTITIES_DIR, f"{slug}.md")
    
    # Skip if exists
    if os.path.exists(path):
        # Check if it has ## Key Views
        with open(path) as f:
            content = f.read()
            if '## Key Views' in content:
                return False, "already_complete"
        # Also skip if it already has 20vc source
        if source_file in content:
            return False, "already_exists"
    
    # Build tags list
    all_tags = set(tags) if tags else set()
    all_tags.add('person')
    
    # Extract key topics from episode title
    key_topics = []
    title_lower = episode_title.lower()
    
    topic_map = {
        'venture-capital': ['venture capital', 'vc ', 'fundraising', 'fundraising', 'investing'],
        'ai-ml': ['ai', 'artificial intelligence', 'machine learning', 'llm', 'gpt', 'openai', 'anthropic', 'deep learning'],
        'founder-psychology': ['founder', 'psychology', 'mindset', 'leadership', 'ceo'],
        'go-to-market': ['go-to-market', 'gtm', 'sales', 'marketing', 'growth'],
        'enterprise-saas': ['saas', 'enterprise', 'b2b', 'software'],
        'product-strategy': ['product', 'strategy', 'product-market'],
        'consumer': ['consumer', 'b2c', 'social'],
        'fintech': ['fintech', 'finance', 'banking', 'payments'],
        'marketplaces': ['marketplace', 'platform'],
        'hiring-culture': ['hiring', 'culture', 'talent', 'team'],
    }
    
    for topic, keywords in topic_map.items():
        if any(kw in title_lower for kw in keywords):
            all_tags.add(topic)
    
    tags_list = sorted(all_tags)
    
    # Create the entity content
    content = f"""---
title: {name}
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: [{', '.join(tags_list)}]
sources:
  - raw/transcripts/20vc/{os.path.basename(source_file)}
confidence: medium
---


# {name}

*This page was migrated from the podcast wiki guest index. This guest appeared on 20VC (show notes only, not full transcript).*

## Episode Appearances

- [[{os.path.splitext(os.path.basename(source_file))[0]}]] — *20VC show notes — {episode_title[:80]}...*

## Related Concepts

"""
    
    for tag in sorted(all_tags - {'person'}):
        content += f'- [[{tag}]]\n'
    
    os.makedirs(ENTITIES_DIR, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    
    return True, "created"

def main():
    transcript_files = sorted(glob.glob(os.path.join(TRANSCRIPTS_DIR, "*.md")))
    print(f"Total 20VC transcript files: {len(transcript_files)}")
    
    created = 0
    skipped_exists = 0
    skipped_complete = 0
    skipped_no_guest = 0
    skipped_error = 0
    errors = []
    
    # Track unique guests to avoid duplicate entities for same guest across multiple episodes
    seen_guests = set()
    
    for i, fpath in enumerate(transcript_files):
        if (i+1) % 100 == 0:
            print(f"Progress: {i+1}/{len(transcript_files)} files processed ({created} created so far)...")
        
        try:
            with open(fpath, 'r') as f:
                content = f.read()
            
            # Parse JSON frontmatter
            # Find JSON between --- markers
            json_match = re.search(r'---\s*\n({.*?})\s*\n---', content, re.DOTALL)
            if not json_match:
                skipped_error += 1
                errors.append(f"{os.path.basename(fpath)}: No JSON frontmatter found")
                continue
            
            data = json.loads(json_match.group(1))
            title = data.get('title', '')
            guest_slug = data.get('guest', 'unknown-guest')
            tags = data.get('tags', [])
            
            # Extract name
            name = slug_to_name(guest_slug)
            
            if name is None:
                name = extract_name_from_title(title)
            
            if name is None:
                name = guess_name_from_filepath(fpath)
            
            if name is None or len(name.split()) < 2:
                # Check if there's a named guest in the title at all
                # Some episodes are news roundups with no single guest
                skipped_no_guest += 1
                continue
            
            # Clean up name
            name = name.strip().rstrip(',.')
            
            # Skip duplicates
            guest_key = name.lower()
            if guest_key in seen_guests:
                # Already created an entity for this guest from another episode
                # We could add the episode to the existing entity, but let's keep it simple
                skipped_exists += 1
                continue
            
            # Check if entity already exists
            if entity_exists(name):
                skipped_exists += 1
                continue
            
            # Create entity
            success, status = create_entity(name, tags, fpath, title)
            if success:
                seen_guests.add(guest_key)
                created += 1
            else:
                if status == "already_complete":
                    skipped_complete += 1
                else:
                    skipped_exists += 1
        
        except json.JSONDecodeError as e:
            skipped_error += 1
            errors.append(f"{os.path.basename(fpath)}: JSON parse error: {e}")
        except Exception as e:
            skipped_error += 1
            errors.append(f"{os.path.basename(fpath)}: Error: {e}")
    
    print(f"\n=== RESULTS ===")
    print(f"Total files processed: {len(transcript_files)}")
    print(f"Entities created: {created}")
    print(f"Skipped (already exists): {skipped_exists}")
    print(f"Skipped (already has Key Views): {skipped_complete}")
    print(f"Skipped (no identifiable guest): {skipped_no_guest}")
    print(f"Errors: {skipped_error}")
    
    if errors:
        print(f"\n=== ERRORS (first 20) ===")
        for e in errors[:20]:
            print(f"  {e}")
    
    return created

if __name__ == '__main__':
    main()
