#!/usr/bin/env python3
"""Standalone FAISS index rebuild, triggered by signal file.

Called by cron every 4 hours. Reads the flag, delegates to semantic_index.py, clears flag.
"""
import os, sys, subprocess

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLAG_FILE = os.path.join(WIKI_DIR, "state", "faiss-needs-rebuild")
VENV_PYTHON = os.path.join(WIKI_DIR, ".venv", "bin", "python3")
SCRIPT = os.path.join(WIKI_DIR, "scripts", "semantic_index.py")


def main():
    if not os.path.exists(FLAG_FILE):
        print("No rebuild needed.")
        return

    python = VENV_PYTHON if os.path.exists(VENV_PYTHON) else "python3"
    print(f"Rebuilding FAISS index (via {python})...")
    result = subprocess.run(
        [python, SCRIPT, "rebuild"],
        cwd=WIKI_DIR,
        timeout=900
    )
    if result.returncode == 0:
        os.remove(FLAG_FILE)
        print("Done. FAISS index rebuilt, signal cleared.")
    else:
        print(f"ERROR: FAISS rebuild failed (exit {result.returncode})")
        sys.exit(1)


if __name__ == "__main__":
    main()
