#!/usr/bin/env python3
"""
Agent 3: Guest Maintainer — updates guest pages with new appearance data
and timeline entries from distiller output.

Run: python3 scripts/guest_maintainer.py
"""

import sys, os, json, re, time

# Add parent dir so imports work
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))

sys.path.insert(0, SCRIPT_DIR)
from agent_lock import acquire_lock, release_lock

GUESTS_DIR = os.path.join(WIKI_DIR, "guests")
TIMELINES_DIR = os.path.join(WIKI_DIR, "data", "guest-timelines")
STATE_DIR = os.path.join(WIKI_DIR, "state")
ERROR_LOG = os.path.join(STATE_DIR, "guest-maintainer-errors.md")

AGENT_NAME = "agent3"

def log_error(msg):
    ts = time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime())
    with open(ERROR_LOG, "a") as f:
        f.write(f"- [{ts}] {msg}\n")
    print(f"  ERROR: {msg}", file=sys.stderr)

def read_page(slug):
    path = os.path.join(GUESTS_DIR, f"{slug}.md")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return f.read()

def write_page(slug, content):
    path = os.path.join(GUESTS_DIR, f"{slug}.md")
    if not acquire_lock(AGENT_NAME):
        log_error(f"SKIPPED {slug}: could not acquire lock (timeout)")
        return False
    try:
        # Double-check the file hasn't been modified since we read it
        with open(path, "w") as f:
            f.write(content)
        return True
    except Exception as e:
        log_error(f"WRITE FAILED {slug}: {e}")
        return False
    finally:
        release_lock(AGENT_NAME)

def build_yaml_appearances(slug, timeline):
    """Build the YAML frontmatter appearances list from all timeline episodes sorted by date."""
    appearances = timeline.get("appearances", [])
    # Sort by date ascending
    appearances.sort(key=lambda a: a.get("date", ""))
    # Use the filename without .md
    slugs = [a["filename"].replace(".md", "") for a in appearances]
    return slugs

def update_guest_page(slug, timeline):
    """Update a single guest page with timeline data."""
    content = read_page(slug)
    if content is None:
        log_error(f"SKIPPED {slug}: no guest page found")
        return False
    
    timeline_episodes = timeline.get("appearances", [])
    timeline_episode_ids = set(a["filename"].replace(".md", "") for a in timeline_episodes)
    
    # --- Step 1: Update YAML frontmatter appearances ---
    # Find the YAML block
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not yaml_match:
        log_error(f"SKIPPED {slug}: no YAML frontmatter found")
        return False
    
    yaml_body = yaml_match.group(1)
    
    # Update the appearances array in YAML
    new_slugs = build_yaml_appearances(slug, timeline)
    new_appearances_json = json.dumps(new_slugs)
    
    # Replace appearances in YAML
    old_app_pattern = r'"appearances":\s*\[.*?\]'
    if re.search(old_app_pattern, yaml_body, re.DOTALL):
        new_yaml_body = re.sub(old_app_pattern, f'"appearances": {new_appearances_json}', yaml_body, count=1, flags=re.DOTALL)
    else:
        new_yaml_body = yaml_body
    
    new_content = f"---\n{new_yaml_body}\n---\n{content[yaml_match.end():]}"
    
    # --- Step 2: Update "Appears in" section ---
    appears_header = "**Appears in:**"
    if appears_header in new_content:
        before_appears, after_appears = new_content.split(appears_header, 1)
        
        # Parse existing entries
        appears_lines = after_appears.split('\n')
        appears_entries = {}
        in_appears = True
        rest_lines = []
        
        for line in appears_lines:
            if in_appears:
                link_match = re.match(r'- \[\[(.+?)\]\]', line)
                if link_match:
                    entry_id = link_match.group(1)
                    desc = line[link_match.end():]  # includes the " — description" part
                    appears_entries[entry_id] = line
                elif line.strip() == '' and len(rest_lines) == 0 and not appears_entries:
                    rest_lines.append(line)
                else:
                    in_appears = False
                    rest_lines.append(line)
            else:
                rest_lines.append(line)
        
        # Add missing episodes
        updated = False
        for ep_id in sorted(timeline_episode_ids):
            if ep_id not in appears_entries:
                # Check if entry has a description from the timeline
                ep_data = next((a for a in timeline_episodes if a["filename"].replace(".md", "") == ep_id), None)
                desc = ""
                if ep_data:
                    desc = f" {ep_data.get('date', '')[:7]}"  # just YYYY-MM
                appears_entries[ep_id] = f"- [[{ep_id}]]{desc}"
                updated = True
        
        # Rebuild the section sorted by episode ID
        sorted_entries = sorted(appears_entries.values(), key=lambda x: x)
        new_appears_section = appears_header + "\n" + "\n".join(sorted_entries) + "\n\n"
        
        new_content = before_appears + new_appears_section + "\n".join(rest_lines)
    
    # --- Step 3: Add/update "## Timeline" section ---
    # Check if a "## Timeline" section exists
    if "## Timeline" not in new_content:
        # Check for "## Key Beliefs" section
        if "**Key Beliefs:**" in new_content or "## Key Beliefs" in new_content or "**Key Ideas:**" in new_content:
            # Add timeline after the last section before Appears in
            timeline_entries = []
            for ep in sorted(timeline_episodes, key=lambda a: a.get("date", "")):
                date = ep.get("date", "")
                title = ep.get("title", "")
                # Truncate title if too long
                if len(title) > 120:
                    title = title[:117] + "..."
                url = ep.get("url", "")
                timeline_entries.append(f"- **{date}:** [{title}]({url})")
            
            if timeline_entries:
                timeline_section = "\n\n## Timeline\n\n" + "\n".join(timeline_entries) + "\n\n"
                # Insert before "**Appears in:**" if that exists
                if "**Appears in:**" in new_content:
                    new_content = new_content.replace("**Appears in:**", timeline_section + "**Appears in:**")
                else:
                    new_content += timeline_section
    else:
        # Timeline section exists — update with any new entries
        before_timeline, after_timeline = new_content.split("## Timeline", 1)
        timeline_rest = after_timeline.split("\n## ", 1) if "\n## " in after_timeline[1:] else [after_timeline, ""]
        after_section = timeline_rest[1] if len(timeline_rest) > 1 else ""
        
        # Parse existing timeline entries
        existing_dates = set(re.findall(r'\*\*(\d{4}-\d{2}-\d{2}):\*\*', before_timeline + "## Timeline" + timeline_rest[0]))
        
        new_timeline_entries = []
        for ep in sorted(timeline_episodes, key=lambda a: a.get("date", "")):
            date = ep.get("date", "")
            if date not in existing_dates:
                title = ep.get("title", "")
                if len(title) > 120:
                    title = title[:117] + "..."
                url = ep.get("url", "")
                new_timeline_entries.append(f"- **{date}:** [{title}]({url})")
        
        if new_timeline_entries:
            # Insert after existing timeline entries
            timeline_body = timeline_rest[0]
            timeline_body += "\n" + "\n".join(new_timeline_entries)
            
            if after_section:
                new_content = before_timeline + "## Timeline" + timeline_body + "\n\n## " + after_section
            else:
                new_content = before_timeline + "## Timeline" + timeline_body
    
    # Write updated page
    if write_page(slug, new_content):
        return True
    return False

def main():
    os.makedirs(STATE_DIR, exist_ok=True)
    
    # Load all timeline JSONs
    if not os.path.isdir(TIMELINES_DIR):
        print(f"No timeline directory at {TIMELINES_DIR}")
        return
    
    timeline_files = sorted([f for f in os.listdir(TIMELINES_DIR) if f.endswith('.json') and f != '_index.json'])
    print(f"Found {len(timeline_files)} timeline JSON files\n")
    
    updated = 0
    skipped = 0
    up_to_date = 0
    
    for tf in timeline_files:
        slug = tf.replace('.json', '')
        
        with open(os.path.join(TIMELINES_DIR, tf)) as f:
            timeline = json.load(f)
        
        # Skip non-person entities (companies, topics, etc.)
        timeline_episodes = timeline.get("appearances", [])
        if not timeline_episodes:
            skipped += 1
            continue
        
        # Check if page already has all appearances
        content = read_page(slug)
        if content is None:
            print(f"  NO PAGE: {slug} — creating")
            # Could create a stub page, but that's beyond scope
            skipped += 1
            continue
        
        # Check current state
        appears_section = content.split('**Appears in:**')[-1] if '**Appears in:**' in content else ''
        page_links = set(re.findall(r'\[\[(.+?)\]\]', appears_section))
        
        timeline_ep_ids = set(a["filename"].replace(".md", "") for a in timeline_episodes)
        
        # Check YAML appearances
        yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        yaml_appearances = set()
        if yaml_match:
            yaml_app = re.findall(r'"appearances":\s*\[(.*?)\]', yaml_match.group(1), re.DOTALL)
            if yaml_app:
                yaml_appearances = set(re.findall(r'"([^"]+)"', yaml_app[0]))
        
        missing_page = timeline_ep_ids - page_links
        missing_yaml = timeline_ep_ids - yaml_appearances
        
        # Check for existing timeline section
        has_timeline = "## Timeline" in content
        timeline_missing = False
        if not has_timeline:
            # Only flag as missing if there are >1 episodes or it's the latest episode
            if len(timeline_episodes) > 1:
                timeline_missing = True
        
        if not missing_page and not missing_yaml and not timeline_missing:
            print(f"  UP-TO-DATE: {slug} ({len(timeline_episodes)} eps)")
            up_to_date += 1
            continue
        
        print(f"  UPDATING: {slug}", end="")
        if missing_page:
            print(f" (+{len(missing_page)} missing from Appears in)", end="")
        if missing_yaml:
            print(f" (+{len(missing_yaml)} missing from YAML)", end="")
        if timeline_missing:
            print(f" (+Timeline section)", end="")
        print()
        
        if update_guest_page(slug, timeline):
            updated += 1
        else:
            skipped += 1
    
    # Write summary
    print(f"\n{'='*50}")
    print(f"Summary: {updated} updated, {up_to_date} already current, {skipped} skipped")
    
    # Append summary to error log
    with open(ERROR_LOG, "a") as f:
        f.write(f"\n## Run — {time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime())}\n")
        f.write(f"- {updated} guest pages updated\n")
        f.write(f"- {up_to_date} already current\n")
        f.write(f"- {skipped} skipped\n\n")

if __name__ == "__main__":
    main()
