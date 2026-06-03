#!/usr/bin/env python3
"""Wrapper script that reads DEEPSEEK_API_KEY from .env and runs distill.py."""
import os, sys, subprocess
from pathlib import Path

# Read API key from .env
env_path = Path.home() / ".hermes" / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line.startswith("DEEPSEEK_API_KEY="):
            key = line.split("=", 1)[1].strip().strip('"').strip("'")
            os.environ["DEEPSEEK_API_KEY"] = key
            break

# Verify it's set
if not os.environ.get("DEEPSEEK_API_KEY"):
    print("ERROR: DEEPSEEK_API_KEY not found", file=sys.stderr)
    sys.exit(1)

# Run the distiller
wiki_dir = Path.home() / ".hermes" / "podcast-wiki"
result = subprocess.run(
    [sys.executable, "-u", str(wiki_dir / "scripts" / "distill.py")] + sys.argv[1:],
    cwd=str(wiki_dir),
    capture_output=False,
    text=True
)
sys.exit(result.returncode)
