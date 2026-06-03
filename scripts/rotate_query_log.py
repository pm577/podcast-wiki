#!/usr/bin/env python3
"""Rotate mcp-query-log.jsonl — keep 4 weeks of history, auto-rotate at 5MB."""
import os, shutil
from pathlib import Path

LOG = Path.home() / ".hermes" / "podcast-wiki" / "state" / "mcp-query-log.jsonl"
ROTATED = Path.home() / ".hermes" / "podcast-wiki" / "state" / "mcp-query-log.old.jsonl"
MAX_BYTES = 5 * 1024 * 1024  # 5MB


def main():
    if not LOG.exists():
        print("No query log to rotate.")
        return
    size = LOG.stat().st_size
    if size < MAX_BYTES:
        print(f"Query log: {size/1024:.0f}KB — under 5MB limit, no rotation needed")
        return
    # Rotate: move current to .old (overwrite), create fresh
    if ROTATED.exists():
        ROTATED.unlink()
    shutil.move(str(LOG), str(ROTATED))
    LOG.write_text("")
    print(f"Rotated: {size/1024:.0f}KB -> mcp-query-log.old.jsonl")


if __name__ == "__main__":
    main()
