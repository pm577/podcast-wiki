#!/usr/bin/env python3
"""
Write-lock coordination between Agent 1 (distiller) and Agent 3 (guest maintainer).

Both write to guests/<name>.md on overlapping cadences. Use file-based locks
in the state/ directory with a 60-second timeout fallback.
"""
import os, time

STATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "state")


def acquire_lock(agent_name, timeout=60):
    """Acquire a named lock file. Returns True if acquired, False if timed out."""
    lock_file = os.path.join(STATE_DIR, f"{agent_name}.lock")
    start = time.time()
    while os.path.exists(lock_file):
        if time.time() - start > timeout:
            return False
        time.sleep(2)
    with open(lock_file, "w") as f:
        f.write(str(os.getpid()))
    return True


def release_lock(agent_name):
    """Release a named lock file."""
    lock_file = os.path.join(STATE_DIR, f"{agent_name}.lock")
    if os.path.exists(lock_file):
        os.remove(lock_file)
