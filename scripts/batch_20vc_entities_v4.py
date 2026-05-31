#!/usr/bin/env python3
"""
Final pass - handle remaining edge cases for 20VC name extraction.
"""

import json
import os
import re
import glob

TRANSCRIPTS_DIR = os.path.expanduser("~/.hermes/podcast-wiki/raw/transcripts/20vc")
ENTITIES_DIR = os.path.expanduser("~/.hermes/podcast-wiki/wiki/entities")

def extract_name(title):
    """Extract guest name - handles tough remaining patterns."""
    cleaned = re.sub(r'^(?:20\s*VC\s*(?:FF\s*)?\d*[:\s]*|20VC:?\s*|FF\s+\d+[:\s]*|Founders\s+Friday\s+\d+[:\s]*|Pre-YC\s+Demo\s+Day[:\s]*|This\s+Week\s+in\s+SaaS[:\s]*)', '', title)
    
    # Remove WEEK markers
    cleaned = re.sub(r'^(?:FOUNDRY\s+GROUP\s+)?WEEK\s+\d+[:\s]+', '', cleaned)
    cleaned = re.sub(r'^(?:Y\s+COMBINATOR|BETAWORKS)\s+WEEK[:\s]+', '', cleaned)
    cleaned = re.sub(r'^(?:PART|Part)\s+\d+[:\s]+', '', cleaned)
    
    # Remove LATAM / Special / Exclusive / News / Roundtable markers
    cleaned = re.sub(r'^(?:LATAM\s+)?(?:PART|Part)\s+\d+[:\s]+', '', cleaned)
    cleaned = re.sub(r'^(?:Exclusive|Special|News|Roundtable)[:\s]+', '', cleaned)
    cleaned = re.sub(r'^NEW\s+FORMAT[:\s]+', '', cleaned)
    
    patterns = [
        # "Balderton's James Wise interviews ... Harry Stebbings" - get name after "interviews"
        r'interviews\s+(?:\w+\s+)?(?:Founder|CEO|Co-Founder|Partner),?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.-]|\s*$|\s+on)',
        
        # "Company's Name on topic" — extract Name after 's
        r"'[sS]\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?:on|of|@)",
        
        # "Name @ Company on topic" — title starts with Name @
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+@\s+',
        
        # PART N: Name: 
        r'^(?:PART|Part)\s+\d+[:\s]+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}):\s',
        
        # "Name: topic" at start
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}):\s',
        
        # "Name on topic" at start
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+on\s+',
        
        # "with the {Role}, {Name}" at end
        r'\bwith\s+(?:the\s+)?\w+(?:\s+\w+)?\w*[,:]\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.-].*)?$',
        
        # "with {Name}" at end
        r'\bwith\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.-].*)?$',
        
        # "Name, Role" at start
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}),\s+(?:Co-Founder|Founder|CEO|Partner|GP|Managing|Author|CFO|CTO|Director|Head|General|Former)',
        
        # "Name - " or "Name — "
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s*[—\-]\s+',
        
        # the {role}, {Name}
        r'(?:the\s+(?:legend|king|godfather|queen|prince|master|guru|most\s+\w+\s+\w+)),?\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})(?:\s*[,.\-]|\s+on\s+)',
        
        # "Name, the {Role}"
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}),\s+the\s+',
        
        # Super Angel, {Name}
        r'^(?:Super\s+Angel|Super\s+Angel,)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})',
        
        # "Name of Company" at start
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+of\s+',
        
        # Get name from "Company's Name on" where Company doesn't start with capital letter
        r"'[sS]\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b",
        
        # Name followed by capital letter (not in skip list) for "Frank Meehan Series A"
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?!(?:The|A|An|This|That|Why|How|What|When|Where|Is|Are|Has|Have|Do|Does|Did|Can|Will|Would|Could|Should|May|Might|Must|And|But|Or|For|Nor|Yet|So|In|On|At|To|By|With|From|Of|As|Into|Through|During|Before|After|Above|Out|Off|Over|Under|Then|Once|Here|There|All|Each|Both|Few|More|Most|Other|Some|Such|No|Nor|Not|Only|Own|Same|So|Than|Too|Very|Just|Also|Now|Even|Still|Already|Series|Life|My|Your|His|Her|Its|Our|Their)\b)[A-Z]',
    ]
    
    for pattern in patterns:
        m = re.search(pattern, cleaned)
        if m:
            name = m.group(1).strip().rstrip(',.')
            parts = name.split()
            skip_words = {'The', 'How', 'Why', 'What', 'Inside', 'From', 'Is', 'Are', 'Has', 'This',
                         'That', 'These', 'Those', 'WTF', 'When', 'Where', 'Which', 'Who', 'Whom',
                         'Part', 'Week', 'Foundry', 'Index', 'Homebrew', 'Robinhood',
                         'Uber', 'Digg', 'Pre-YC', 'Immediately', 'Benchmark'}
            if parts[0] not in skip_words and len(parts) >= 2:
                return name
    return None

def make_slug(name):
    return name.lower().replace(' ', '-').replace("'", '').replace('.', '').replace(',', '')

def entity_exists(name):
    slug = make_slug(name)
    return os.path.exists(os.path.join(ENTITIES_DIR, f"{slug}.md"))

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
    
    # Find episodes still needing entities
    existing_entities = set()
    for f in glob.glob(os.path.join(ENTITIES_DIR, '*.md')):
        with open(f) as fh:
            content = fh.read()
            if 'raw/transcripts/20vc/' in content:
                for line in content.split('\n'):
                    m = re.match(r'\s*-\s*\[\[(20vc[^\]]+)\]\]', line)
                    if m:
                        existing_entities.add(m.group(1))
    
    created = 0
    skipped_exists = 0
    skipped_no_guest = 0
    seen_guests = set()
    
    for fpath in transcript_files:
        basename = os.path.splitext(os.path.basename(fpath))[0]
        
        # Skip if this transcript is already referenced
        if basename in existing_entities:
            skipped_exists += 1
            continue
        
        try:
            with open(fpath, 'r') as f:
                content = f.read()
            
            json_match = re.search(r'---\s*\n({.*?})\s*\n---', content, re.DOTALL)
            if not json_match:
                continue
            
            data = json.loads(json_match.group(1))
            title = data.get('title', '')
            tags = data.get('tags', [])
            
            name = extract_name(title)
            
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
                
        except Exception as e:
            skipped_no_guest += 1
    
    print(f"\n=== RESULTS ===")
    print(f"Entities created: {created}")
    print(f"Skipped (already exists/referenced): {skipped_exists}")
    print(f"Skipped (no identifiable guest): {skipped_no_guest}")

if __name__ == '__main__':
    main()
