#!/usr/bin/env python3
"""Add timeline entries to guest pages updated by distiller.

Uses agent_lock for write coordination with agent3."""
import sys, os, re, time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from agent_lock import acquire_lock, release_lock

WIKI_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
GUESTS_DIR = os.path.join(WIKI_DIR, "guests")
STATE_DIR = os.path.join(WIKI_DIR, "state")
ERROR_LOG = os.path.join(STATE_DIR, "guest-maintainer-errors.md")

AGENT_NAME = "agent3"

# Timeline data for new distiller-processed guests
# slug -> [(date, title, url)]
TIMELINE_DATA = {
    "dan-shipper": [
        ("2026-05-24", "The AI paradox: More automation, more humans, more work | Dan Shipper",
         "https://www.lennysnewsletter.com/p/the-ai-paradox-dan-shipper"),
    ],
    "eric-ries": [
        ("2026-05-10", "How to build a company that withstands any era | Eric Ries, Lean Startup author",
         "https://www.lennysnewsletter.com/p/eric-ries-lean-startup-author"),
    ],
    "nikhyl-singhal": [
        ("2026-04-19", "Why half of product managers are in trouble | Nikhyl Singhal (Meta, Google)",
         "https://www.lennysnewsletter.com/p/why-half-of-product-managers-are-in-trouble"),
    ],
    "claire-vo": [
        ("2026-03-29", "From skeptic to true believer: How OpenClaw changed my life | Claire Vo",
         "https://www.lennysnewsletter.com/p/how-openclaw-changed-my-life-claire-vo"),
    ],
}

def log(msg):
    ts = time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime())
    with open(ERROR_LOG, "a") as f:
        f.write(f"- [{ts}] {msg}\n")
    print(msg)

def add_timeline(slug, entries):
    path = os.path.join(GUESTS_DIR, f"{slug}.md")
    if not os.path.exists(path):
        log(f"SKIPPED {slug}: no guest page found")
        return False

    with open(path) as f:
        content = f.read()

    # Check if timeline already exists
    if "## Timeline" in content:
        log(f"SKIPPED {slug}: timeline section already exists")
        return False

    # Build timeline entries sorted by date
    sorted_entries = sorted(entries, key=lambda e: e[0])
    timeline_lines = ["", "## Timeline", ""]
    for date, title, url in sorted_entries:
        timeline_lines.append(f"- **{date}:** [{title}]({url})")
    timeline_lines.append("")

    timeline_section = "\n".join(timeline_lines)

    # Insert timeline before "**Appears in:**"
    if "**Appears in:**" in content:
        new_content = content.replace("**Appears in:**", timeline_section + "\n**Appears in:**")
    else:
        new_content = content + timeline_section

    # Write with lock
    if not acquire_lock(AGENT_NAME):
        log(f"SKIPPED {slug}: could not acquire lock (timeout)")
        return False

    try:
        with open(path, "w") as f:
            f.write(new_content)
        log(f"UPDATED {slug}: added {len(entries)} timeline entries")
        return True
    except Exception as e:
        log(f"WRITE FAILED {slug}: {e}")
        return False
    finally:
        release_lock(AGENT_NAME)

def find_other_recent_guests():
    """Look for guest pages modified after distiller run that don't have timeline sections."""
    distiller_ts = 1717266295  # approximate epoch for 2026-06-01T19:44 UTC
    others = []
    for fname in os.listdir(GUESTS_DIR):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(GUESTS_DIR, fname)
        mtime = os.path.getmtime(fpath)
        slug = fname[:-3]
        # Only check guests not in our timeline data
        if slug in TIMELINE_DATA:
            continue
        if mtime >= distiller_ts:
            with open(fpath) as f:
                content = f.read()
            if "## Timeline" not in content and "**Appears in:**" in content:
                appears = content.split("**Appears in:**")[-1]
                if "lenny-2026" in appears or "20vc-2026" in appears:
                    others.append(slug)
    return others

def main():
    updated = 0
    skipped = 0
    
    for slug, entries in TIMELINE_DATA.items():
        if add_timeline(slug, entries):
            updated += 1
        else:
            skipped += 1
    
    other_guests = find_other_recent_guests()
    if other_guests:
        log(f"OTHER RECENT GUESTS without timeline: {other_guests}")
    
    # Write summary
    with open(ERROR_LOG, "a") as f:
        f.write(f"\n## Timeline Update — {time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime())}\n")
        f.write(f"- {updated} guests updated with timeline entries\n")
        f.write(f"- {skipped} skipped\n\n")
    
    print(f"\n{'='*50}")
    print(f"Complete: {updated} updated, {skipped} skipped")

if __name__ == "__main__":
    main()
