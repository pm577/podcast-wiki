# Execution Log — MCP-Jobs Synergy Fixes — 2026-06-01

- [x] **Task 1**: MCP server v2 instrumented — `do_ask`, `do_synthesize`, `do_search_by_meaning` all log to `state/mcp-query-log.jsonl` with ts, tool, query, latency_ms, result_count
- [x] **Task 2**: `distill.py` now has `get_priority_guests()` — reads query log, sorts unprocessed transcripts so hot guests (most asked about via MCP) distill first
- [x] **Task 3**: `eval.py` now has `--mcp` flag — queries MCP server with 20 golden-set questions, measures synthesis quality %, writes `state/mcp-quality-dashboard.md`
- [x] **Task 4**: Sunday cron `podcast-contradiction-surfaccer` updated — now runs `rotate_query_log.py` + `eval.py --mcp` after disagreement detection
- [x] **Task 5**: `scripts/rotate_query_log.py` created — auto-rotates at 5MB, keeps 4 weeks of history

## Files created
- `scripts/rotate_query_log.py`

## Files modified
- `scripts/podcast_mcp_server_v2.py` — query logging + log_query helper
- `scripts/distill.py` — get_priority_guests() + priority sorting in find_new_transcripts()
- `scripts/eval.py` — eval_mcp_quality() + --mcp flag + dashboard writer

## Cron updated
- `podcast-contradiction-surfaccer` — now runs rotation + MCP eval after contradiction detection

## Data flow (post-fix)

```
User query → MCP server → logs to state/mcp-query-log.jsonl ← ─ ─ ─ ┐
                              ↓                                        │
                        distill.py (every 30 min)                      │
                          reads log → priority order hot guests        │
                              ↓                                        │
                        New transcripts processed (hot first)          │
                                                                       │
                        eval.py --mcp (Sundays 5am) ───────────────────┘
                          queries MCP with golden set
                          → measures synthesis quality %
                          → writes state/mcp-quality-dashboard.md
```
