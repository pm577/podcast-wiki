#!/usr/bin/env python3
"""
Enhanced batch processor for remaining 20VC episodes.
Better name extraction from episode titles.
"""

import json
import os
import re
import glob

TRANSCRIPTS_DIR = os.path.expanduser("~/.hermes/podcast-wiki/raw/transcripts/20vc")
ENTITIES_DIR = os.path.expanduser("~/.hermes/podcast-wiki/wiki/entities")

def slug_to_name(slug):
    """Convert a slug like 'mike-seibel' to 'Mike Seibel'."""
    if not slug or slug == 'unknown-guest' or slug == 'tech' or slug == '':
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
    """Extract guest name from episode title with comprehensive patterns."""
    # Remove "20 VC " or "20VC: " or "20 VC FF " or "FF " prefixes
    cleaned = re.sub(r'^(?:20\s*VC\s*(?:FF\s*)?\d*[:\s]*|20VC:?\s*|FF\s+\d+[:\s]*|Founders\s+Friday\s+\d+[:\s]*)', '', title)
    
    patterns = [
        # Pattern 1: "with {Name}" at end (name right after "with")
        r'\bwith\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,-].*)?$',
        
        # Pattern 2: "with {Company}'s {Name}" or "with the {X}, {Name}"
        r'\bwith\s+(?:the\s+\w+\s+of\s+)?(?:[A-Z][a-z0-9]*(?:\s+[A-Z][a-z0-9]+)*?\'?s?\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,-].*)?$',
        
        # Pattern 3: "{Name} @ {Company}" (name before @)
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+@\s+',
        
        # Pattern 4: "{Name} of {Company}" at start
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+of\s+',
        
        # Pattern 5: "{Name} on {Topic}" at start
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+on\s+',
        
        # Pattern 6: "{Name}: {Subtitle}" or "{Name}: {Role}"
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}):\s',
        
        # Pattern 7: "{Name}, {Role}" after comma
        r',\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,-].*)?$',
        
        # Pattern 8: "with {Adjective} {Name}, {Surname}" - like "with the King of SaaS, Jason Lemkin"
        r'\bwith\s+(?:the\s+)?\w+(?:\s+\w+)?,\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,-].*)?$',
        
        # Pattern 9: "{Name}, Former {Role}" - like "Mike Jones, Former MySpace CEO"
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}),\s+(?:Former|Co-Founder|Founder|CEO|Partner|GP|Managing|Author|CFO|CTO|Director)',
        
        # Pattern 10: Grab name at very start after all prefixes removed
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s+[—-]|\s+&|\s+on\s+|\s+of\s+|\s+@|\s*$)',
        
        # Pattern 11: "{Name}'s" at end
        r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})'s\s",
        
        # Pattern 12: "CO-FOUNDER {Name}" or "FOUNDER {Name}"
        r'\b(?:Co-Founder|Founder|CEO|Partner|GP)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.-])',
        
        # Pattern 13: "PART {N}: {Name}:" pattern
        r'PART\s+\d+[:\s]+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}):\s',
        
        # Pattern 14: End with name after comma in "with ... , Name" pattern
        r'\bwith\s+.*?,\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s*$',
    ]
    
    for pattern in patterns:
        m = re.search(pattern, cleaned)
        if m:
            name = m.group(1).strip().rstrip(',.')
            # Filter out common non-person starting words
            skip_words = {'The', 'How', 'Why', 'What', 'Inside', 'From', 'Is', 'Are', 'Has', 'This', 
                         'That', 'These', 'Those', 'WTF', 'When', 'Where', 'Which', 'Who', 'Whom',
                         'PART', 'Part', 'Week', 'WEEK', 'Is'}
            parts = name.split()
            if parts[0] in skip_words:
                continue
            # Make sure it has at least first and last name
            if len(parts) >= 2:
                return name
    
    return None

def make_slug(name):
    """Convert a name to a slug."""
    return name.lower().replace(' ', '-').replace("'", '').replace('.', '').replace(',', '')

def entity_exists(name):
    """Check if an entity page already exists."""
    slug = make_slug(name)
    path = os.path.join(ENTITIES_DIR, f"{slug}.md")
    return os.path.exists(path)

def create_entity(name, tags, source_file, episode_title):
    """Create an entity page for a guest."""
    slug = make_slug(name)
    path = os.path.join(ENTITIES_DIR, f"{slug}.md")
    
    # Skip if exists
    if os.path.exists(path):
        return False, "already_exists"
    
    # Build tags list
    all_tags = set(tags) if tags else set()
    all_tags.add('person')
    
    # Sort tags
    tags_list = sorted(all_tags)
    
    # Truncate title for display
    display_title = episode_title[:80] + '...' if len(episode_title) > 80 else episode_title
    
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

- [[{os.path.splitext(os.path.basename(source_file))[0]}]] — *20VC show notes — {display_title}*

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
    skipped_no_guest = 0
    errors = []
    
    # Track unique guests
    seen_guests = set()
    
    for i, fpath in enumerate(transcript_files):
        if (i+1) % 100 == 0:
            print(f"Progress: {i+1}/{len(transcript_files)} ({created} created)...")
        
        try:
            with open(fpath, 'r') as f:
                content = f.read()
            
            # Parse JSON frontmatter
            json_match = re.search(r'---\s*\n({.*?})\s*\n---', content, re.DOTALL)
            if not json_match:
                continue
            
            data = json.loads(json_match.group(1))
            title = data.get('title', '')
            guest_slug = data.get('guest', 'unknown-guest')
            tags = data.get('tags', [])
            
            # Try slug first
            name = slug_to_name(guest_slug)
            
            # Fall back to title extraction
            if name is None:
                name = extract_name_from_title(title)
            
            if name is None or len(name.split()) < 2:
                skipped_no_guest += 1
                continue
            
            name = name.strip().rstrip(',.')
            
            # Skip duplicates
            guest_key = name.lower()
            if guest_key in seen_guests:
                skipped_exists += 1
                continue
            
            # Check if entity exists
            if entity_exists(name):
                skipped_exists += 1
                continue
            
            # Create entity
            success, status = create_entity(name, tags, fpath, title)
            if success:
                seen_guests.add(guest_key)
                created += 1
            else:
                skipped_exists += 1
        
        except Exception as e:
            errors.append(f"{os.path.basename(fpath)}: {e}")
    
    print(f"\n=== RESULTS ===")
    print(f"Entities created: {created}")
    print(f"Skipped (already exists): {skipped_exists}")
    print(f"Skipped (no identifiable guest): {skipped_no_guest}")
    print(f"Errors: {len(errors)}")
    
    if errors:
        print(f"\nFirst 10 errors:")
        for e in errors[:10]:
            print(f"  {e}")
    
    return created

if __name__ == '__main__':
    main()
