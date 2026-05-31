#!/usr/bin/env python3
"""
Daily podcast harvester — runs automatically to check for new episodes.
RSS poll → download transcripts → ingest into wiki → rebuild semantic index.
"""

import subprocess
import sys
from pathlib import Path

HERMES_PYTHON = str(Path.home() / ".hermes/pdf-venv/bin/python3")
YT_ENV_PYTHON = str(Path.home() / ".yt-env/bin/python3")
SCRIPTS_DIR = Path.home() / ".hermes/podcast-wiki/scripts"


def run_script(name, python=HERMES_PYTHON):
    """Run a python script and return True if successful."""
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"  Script not found: {script_path}")
        return True
    result = subprocess.run(
        [python, str(script_path)],
        capture_output=True, text=True, timeout=300
    )
    print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
    if result.returncode != 0:
        print(f"ERROR: {name} failed:\n{result.stderr}", file=sys.stderr)
        return False
    return True


def main():
    print("=== Podcast Wiki Daily Harvester ===\n")

    # Step 1: Harvest new 20VC episodes from RSS
    print("--- Step 1: 20VC RSS Harvest ---")
    run_script("harvest_20vc.py")

    # Step 2: Check for new ChatPRD transcripts
    print("\n--- Step 2: ChatPRD Transcript Check ---")
    chatprd_dir = SCRIPTS_DIR.parent / "chatprd-transcripts"
    if chatprd_dir.exists():
        result = subprocess.run(
            ["git", "pull"],
            capture_output=True, text=True, timeout=60,
            cwd=str(chatprd_dir)
        )
        print(result.stdout[:500])
        if "Already up to date" not in result.stdout and result.returncode == 0:
            print("New ChatPRD transcripts found! Re-ingesting...")
            run_script("ingest_chatprd.py")
            run_script("ingest_lenny.py")

    # Step 3: Check for Lennysdata repo updates
    print("\n--- Step 3: Lennysdata Check ---")
    lennysdata_dir = SCRIPTS_DIR.parent / "lennysdata"
    if lennysdata_dir.exists():
        result = subprocess.run(
            ["git", "pull"],
            capture_output=True, text=True, timeout=60,
            cwd=str(lennysdata_dir)
        )
        print(result.stdout[:500])
        run_script("ingest_lenny.py")

    # Step 4: Update index (only if any script changed anything)
    print("\n--- Step 4: Update Wiki Index ---")
    run_script("generate_index.py")

    # Step 5: Rebuild semantic search index (always — keeps embedding model warm)
    print("\n--- Step 5: Semantic Index Rebuild ---")
    semantic_result = subprocess.run(
        [YT_ENV_PYTHON, str(SCRIPTS_DIR / "semantic_index.py"), "rebuild"],
        capture_output=True, text=True, timeout=900
    )
    print(semantic_result.stdout[-500:] if len(semantic_result.stdout) > 500 else semantic_result.stdout)
    if semantic_result.returncode != 0:
        print(f"ERROR: Semantic index rebuild failed:\n{semantic_result.stderr}", file=sys.stderr)
    else:
        print("Semantic index rebuilt successfully")

    print("\n=== Harvest Complete ===")


if __name__ == "__main__":
    main()
