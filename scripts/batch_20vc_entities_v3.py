#!/usr/bin/env python3
"""
Third pass - more aggressive name extraction for remaining 20VC episodes.
Uses multiple strategies including searching the raw file content.
"""

import json
import os
import re
import glob

TRANSCRIPTS_DIR = os.path.expanduser("~/.hermes/podcast-wiki/raw/transcripts/20vc")
ENTITIES_DIR = os.path.expanduser("~/.hermes/podcast-wiki/wiki/entities")

def extract_name_aggressive(title):
    """Extract guest name from episode title - aggressive multi-strategy."""
    # Remove known prefixes
    cleaned = re.sub(r'^(?:20\s*VC\s*(?:FF\s*)?\d*[:\s]*|20VC:?\s*|FF\s+\d+[:\s]*|Founders\s+Friday\s+\d+[:\s]*|Pre-YC\s+Demo\s+Day[:\s]*)', '', title)
    
    # Also remove "WEEK N:" or "WEEK N: " patterns
    cleaned = re.sub(r'^(?:FOUNDRY\s+GROUP\s+)?WEEK\s+\d+[:\s]+', '', cleaned)
    
    # Also remove "PART N: " or "Part N: " patterns (but keep the name after it)
    cleaned = re.sub(r'^(?:PART|Part)\s+\d+[:\s]+', '', cleaned)
    
    # Also remove "BETAWORKS WEEK:" or similar WEEK patterns
    cleaned = re.sub(r'^(?:Y\s+COMBINATOR|BETAWORKS)\s+WEEK[:\s]+', '', cleaned)
    
    # Remove "Interviews" patterns like "Balderton's James Wise interviews 20VC Founder, Harry Stebbings"
    # In this case, we want "Harry Stebbings"
    m = re.search(r'interviews\s+(?:\w+\s+)?(?:Founder|CEO|Co-Founder),?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.-]|\s*$)', cleaned, re.IGNORECASE)
    if m:
        return m.group(1)
    
    # Remove "interviews" pattern also: "Name interviews Name" — get the second name
    m = re.search(r"\w+\s+interviews\s+(?:\w+\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.-]|\s*$)", cleaned, re.IGNORECASE)
    if m:
        return m.group(1)
    
    patterns = [
        # {Name} of {Company}
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+of\s+',
        # {Name} @ {Company}  
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+@\s+',
        # {Name}: {topic}
        r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}):\s",
        # {Name}, {Role}
        r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}),\s+(?:CEO|Co-Founder|Founder|Partner|GP|Managing|Author|CFO|CTO|Director|Head|General)",
        # {Name} on {topic}
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+on\s+',
        # {Name} - or {Name} — 
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s*[—\-]\s+',
        # {Name}, Former
        r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}),\s+(?:Former)",
        # {Name} XXX where XXX doesn't look like a name
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?!(?:The|A|An|This|That|Why|How|What|When|Where|Is|Are|Has|Have|Do|Does|Did|Can|Will|Would|Could|Should|May|Might|Must|And|But|Or|For|Nor|Yet|So|In|On|At|To|By|With|From|Of|As|Into|Through|During|Before|After|Above|Below|Out|Off|Over|Under|Again|Then|Once|Here|There|All|Each|Every|Both|Few|More|Most|Other|Some|Such|No|Nor|Not|Only|Own|Same|So|Than|Too|Very|Just|Also|Now|Even|Still|Already|Series|Life|My|Your|His|Her|Its|Our|Their)\b)[A-Z]',
        # with {Name} at end (after any content)
        r'\bwith\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.-:;].*)?$',
        # with the {X}, {Name} at end
        r"\bwith\s+(?:the\s+)?\w+(?:\s+\w+)?\w*[,:]\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.-].*)?$",
        # 's {Name} — possessive followed by name
        r"'[sS]\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,\-—(:]|\s+on\s+|\s+of\s+)",
        # Super Angel, {Name}
        r"^(?:Super\s+Angel|Super\s+Angel,)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})",
        # {Name}, the {Role}
        r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}),\s+the\s+",
        # Starting with name followed by 's
        r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})'s\s",
        # "the legend, {Name}" or "the king, {Name}"
        r'(?:the\s+(?:legend|king|godfather|queen|prince|master|guru)),?\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.\-]|\s+on\s+|\s+of\s+)',
        # "Name, Role @ Company" — like "Eric Glyman, Co-Founder & CEO @ Paribus"
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}),\s+(?:Co-Founder|Founder|CEO)\s',
    ]
    
    for pattern in patterns:
        m = re.search(pattern, cleaned)
        if m:
            # Debug
            # print(f"  MATCH [{pattern[:30]}]: '{m.group(1)}' from '{cleaned[:60]}'")
            name = m.group(1).strip().rstrip(',.')
            parts = name.split()
            skip_words = {'The', 'How', 'Why', 'What', 'Inside', 'From', 'Is', 'Are', 'Has', 'This',
                         'That', 'These', 'Those', 'WTF', 'When', 'Where', 'Which', 'Who', 'Whom',
                         'PART', 'Part', 'Week', 'WEEK', 'Foundry', 'Index', 'Homebrew', 'Robinhood',
                         'Uber', 'Digg', 'Pre-YC', 'Immediately'}
            if parts[0] not in skip_words and len(parts) >= 2:
                return name
    
    return None


def make_slug(name):
    return name.lower().replace(' ', '-').replace("'", '').replace('.', '').replace(',', '')


def entity_exists(name):
    slug = make_slug(name)
    path = os.path.join(ENTITIES_DIR, f"{slug}.md")
    return os.path.exists(path)


def create_entity(name, tags, source_file, episode_title):
    slug = make_slug(name)
    path = os.path.join(ENTITIES_DIR, f"{slug}.md")
    
    if os.path.exists(path):
        return False, "already_exists"
    
    all_tags = set(tags) if tags else set()
    all_tags.add('person')
    
    display_title = episode_title[:80] + '...' if len(episode_title) > 80 else episode_title
    
    content = f"""---
title: {name}
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: [{', '.join(sorted(all_tags))}]
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
    seen_guests = set()
    
    for i, fpath in enumerate(transcript_files):
        if (i+1) % 100 == 0:
            print(f"Progress: {i+1}/{len(transcript_files)} ({created} created)...")
        
        try:
            with open(fpath, 'r') as f:
                content = f.read()
            
            json_match = re.search(r'---\s*\n({.*?})\s*\n---', content, re.DOTALL)
            if not json_match:
                continue
            
            data = json.loads(json_match.group(1))
            title = data.get('title', '')
            guest_slug = data.get('guest', 'unknown-guest')
            tags = data.get('tags', [])
            
            # Determine name
            name = None
            
            # 1. Try slug
            if guest_slug and guest_slug not in ('unknown-guest', 'tech', ''):
                parts = guest_slug.split('-')
                name_parts = []
                for p in parts:
                    if p.lower() in ('of', 'the', 'and', 'for', 'with', 'on', 'in', 'at', 'by', 'to', 'a', 'an'):
                        name_parts.append(p.lower())
                    else:
                        name_parts.append(p.capitalize())
                name = ' '.join(name_parts)
            
            # 2. Try aggressive title extraction
            if name is None or len(name.split()) < 2:
                extracted = extract_name_aggressive(title)
                # Also get name from the # heading line (if title extraction fails)
                if not extracted:
                    # Try to get the guest from the markdown ## Summary section
                    summary_match = re.search(r'\*\*Guest:\*\*\s*(.+)', content)
                    if summary_match:
                        extracted = summary_match.group(1).strip()
                
                if extracted and len(extracted.split()) >= 2:
                    name = extracted
            
            # 3. Try the ## Summary markdown
            if name is None or len(name.split()) < 2:
                summary_name = re.search(r'\*\*Guest:\*\*\s*(.+)', content)
                if summary_name:
                    n = summary_name.group(1).strip()
                    if n and len(n.split()) >= 2:
                        name = n
            
            if name is None or len(name.split()) < 2:
                skipped_no_guest += 1
                continue
            
            name = name.strip().rstrip(',.')
            
            guest_key = name.lower()
            if guest_key in seen_guests:
                skipped_exists += 1
                continue
            
            if entity_exists(name):
                skipped_exists += 1
                continue
            
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
