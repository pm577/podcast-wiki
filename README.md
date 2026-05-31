# Podcast Wiki — Connect Guide

A Karpathy-style LLM-maintained knowledge base covering **Lenny's Podcast** and **20VC**.
1,823 episodes, 351 full transcripts, 13K+ semantic searchable chunks.

## For Colleagues: Query via MCP

If you have access to this VPS and Hermes Agent:

```bash
# Search by meaning (not just keywords)
hermes mcp call podcast-wiki search_by_meaning \
  '{"query": "retaining power users during freemium conversion"}'

# Search by keyword
hermes mcp call podcast-wiki search_episodes \
  '{"query": "pricing SaaS", "podcast": "lenny"}'

# Get guest profile
hermes mcp call podcast-wiki get_guest_profile \
  '{"name": "Elena Verna"}'

# Weekly summary of recent episodes
hermes mcp call podcast-wiki weekly_summary '{}'

# Quick stats
hermes mcp call podcast-wiki get_podcast_stats '{}'
```

## Setup for Other MCP Clients

Add this as an MCP server in your MCP client config:

```json
{
  "podcast-wiki": {
    "command": "/home/philip/.yt-env/bin/python3",
    "args": [
      "/home/philip/.hermes/podcast-wiki/scripts/podcast_mcp_server.py"
    ]
  }
}
```

## Manual Queries (on this VPS)

```bash
# Semantic search
~/.hermes/podcast-wiki/scripts/semantic_index.py query "your question here"

# Filter by podcast
~/.hermes/podcast-wiki/scripts/semantic_index.py query "AI agents" --podcast lenny

# Stats
~/.hermes/podcast-wiki/scripts/semantic_index.py stats
```

## Architecture

- **raw/** — Immutable transcripts (351 Lenny + 1,462 20VC + 10 newsletters)
- **wiki/** — LLM-maintained pages (entities, concepts, comparisons, queries)
- **data/** — FAISS semantic search index (13,445 chunks)
- **SCHEMA.md** — Domain conventions, tag taxonomy, update policy

Auto-updates daily at 6am UTC.
