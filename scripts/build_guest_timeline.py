#!/usr/bin/env python3
"""Build guest timeline files — groups 20VC episodes by guest name and
creates a timeline JSON file for each guest with 2+ appearances."""

import json
import os
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
EPISODE_INDEX = os.path.join(DATA_DIR, "20vc-structured", "episode_index.json")
GUEST_INDEX = os.path.join(DATA_DIR, "20vc-structured", "guest_index.json")
OUTPUT_DIR = os.path.join(DATA_DIR, "guest-timelines")


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def slugify(name):
    return name.lower().replace(" ", "-").replace(".", "-").replace(",", "").replace("'", "")


def build_timelines():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    episodes = load_json(EPISODE_INDEX)
    guest_index = load_json(GUEST_INDEX)  # slug -> [filenames]

    # Build mapping: filename -> episode data
    ep_by_filename = {}
    for ep in episodes:
        ep_by_filename[ep["filename"]] = ep

    # Group episodes by actual guest name (from episode data)
    guest_episodes = defaultdict(list)
    for ep in episodes:
        guest_name = ep.get("guest")
        if guest_name:
            guest_episodes[guest_name].append(ep)

    # Also ensure we cover guests from guest_index who might have no guest field
    # (some episodes in guest_index may have guest=null in episode_index)
    # Build reverse map: filename -> guest slug
    filename_to_slug = {}
    for slug, filenames in guest_index.items():
        for fn in filenames:
            filename_to_slug[fn] = slug

    # For episodes with guest=null, try to recover from guest_index
    for slug, filenames in guest_index.items():
        for fn in filenames:
            ep = ep_by_filename.get(fn)
            if ep and not ep.get("guest"):
                # The guest_index slug IS the guest identity; reconstruct name
                # We'll use slug as the key, but try to get proper name from first quote
                guest_episodes[f"unknown-{slug}"].append(ep)

    # Build timelines
    timelines_created = 0
    multi_guest_names = [name for name, eps in guest_episodes.items() if len(eps) >= 2]

    for guest_name in multi_guest_names:
        guest_eps = guest_episodes[guest_name]
        slug = slugify(guest_name)

        # Sort by date
        guest_eps.sort(key=lambda e: e.get("date", ""))

        timeline = {
            "guest": guest_name,
            "slug": slug,
            "appearance_count": len(guest_eps),
            "appearances": []
        }

        for ep in guest_eps:
            quotes = ep.get("quotes", [])
            # Filter quotes to meaningful text (skip very short metadata-only entries)
            meaningful_quotes = [q for q in quotes if len(q) > 50]

            appearance = {
                "filename": ep["filename"],
                "title": ep.get("title", ""),
                "date": ep.get("date", ""),
                "url": "",
                "topics": ep.get("topics", []),
                "tags": ep.get("tags", []),
                "quotes": meaningful_quotes if meaningful_quotes else quotes
            }

            # Extract URL from quotes if present
            for q in quotes:
                if q.startswith("http"):
                    appearance["url"] = q
                    break

            timeline["appearances"].append(appearance)

        out_path = os.path.join(OUTPUT_DIR, f"{slug}.json")
        with open(out_path, "w") as f:
            json.dump(timeline, f, indent=2, ensure_ascii=False)

        timelines_created += 1

    print(f"Created {timelines_created} guest timeline files in {OUTPUT_DIR}")
    print(f"Guests with 2+ appearances: {len(multi_guest_names)}")

    # Write summary index
    summary = []
    for guest_name in sorted(multi_guest_names):
        slug = slugify(guest_name)
        guest_eps = guest_episodes[guest_name]
        summary.append({
            "guest": guest_name,
            "slug": slug,
            "appearance_count": len(guest_eps),
            "date_range": f"{guest_eps[0].get('date', '')} to {guest_eps[-1].get('date', '')}"
        })

    summary_path = os.path.join(OUTPUT_DIR, "_index.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"Wrote timeline index to {summary_path}")


if __name__ == "__main__":
    build_timelines()
