#! /home/philip/.yt-env/bin/python3
"""
Podcast Wiki MCP Server (MCP SDK v1.0+)

Proper implementation using the official MCP Python SDK.
Connects to Hermes Agent native MCP client.

Tools:
- search_episodes: Keyword search across all episodes
- get_guest_profile: Get a guest's full profile and appearances
- find_insights: Find episodes on a topic
- ask: Combined Q&A with context
- weekly_summary: Most recent episodes with summaries
- get_podcast_stats: Quick stats on the knowledge base
- search_by_meaning: Semantic search using FAISS embeddings
- semantic_stats: FAISS index health check
"""

import json
import os
import re
import sys
import time
import asyncio
from pathlib import Path
from datetime import datetime, timedelta
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    GetPromptResult,
    Prompt,
    PromptArgument,
    PromptMessage,
    TextContent,
    Tool,
    ListToolsResult,
    CallToolResult,
)

# Lazy-loaded semantic search
_semantic_loaded = False
_semantic_query_fn = None

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))

server = Server("podcast-wiki")


# ── Helpers ─────────────────────────────────────────────────────────────

def find_files(dir_path, pattern="*.md"):
    """Find all markdown files in a directory, sorted by modification time (newest first)."""
    files = list(dir_path.glob(pattern))
    files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return files


def read_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    content = filepath.read_text(encoding='utf-8', errors='replace')
    fm = {}
    body = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                import yaml
                fm = yaml.safe_load(parts[1]) or {}
            except Exception:
                pass
            body = parts[2]
    return fm, body.strip()


def load_semantic():
    """Lazy-load the FAISS index and model for semantic search."""
    global _semantic_loaded, _semantic_query_fn
    if _semantic_loaded:
        return True
    try:
        sys.path.insert(0, str(WIKI_DIR / "scripts"))
        from semantic_index import query_index
        _semantic_query_fn = query_index
        _semantic_loaded = True
        return True
    except Exception:
        return False


# ── Tool Implementations ───────────────────────────────────────────────

def do_search_episodes(query: str, podcast: str | None = None, limit: int = 10) -> list:
    """Search episodes by keyword in title, description, and transcript."""
    query_lower = query.lower()
    results = []
    episodes_dir = WIKI_DIR / "episodes"
    if not episodes_dir.exists():
        return []
    for pod_dir in episodes_dir.iterdir():
        if not pod_dir.is_dir():
            continue
        if podcast and pod_dir.name != podcast.lower():
            continue
        for ep_file in find_files(pod_dir)[:50]:
            fm, body = read_frontmatter(ep_file)
            title = fm.get('title', ep_file.stem)
            desc = fm.get('description', '') or body[:300]
            guest = fm.get('guest', '')
            date = fm.get('publish_date', fm.get('episode_date', ''))
            tags = fm.get('topics', fm.get('tags', fm.get('keywords', '')))
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(',') if t.strip()]
            search_text = f"{title} {desc} {guest} {' '.join(tags)}".lower()
            score = 0
            query_terms = query_lower.split()
            for term in query_terms:
                if term in search_text:
                    score += 1
            if score > 0:
                results.append({
                    'episode_id': ep_file.stem,
                    'podcast': pod_dir.name,
                    'title': title,
                    'date': str(date)[:10],
                    'guest': guest,
                    'tags': tags,
                    'relevance': score / len(query_terms) if query_terms else 0,
                    'snippet': desc[:200],
                })
    results.sort(key=lambda r: r['relevance'], reverse=True)
    return results[:limit]


def do_get_guest_profile(guest_name: str) -> dict:
    """Get a guest's full profile, appearances, and topics."""
    episodes = []
    episodes_dir = WIKI_DIR / "episodes"
    if episodes_dir.exists():
        for pod_dir in episodes_dir.iterdir():
            if not pod_dir.is_dir():
                continue
            for ep_file in pod_dir.glob("*.md"):
                fm, body = read_frontmatter(ep_file)
                ep_guest = fm.get('guest', '')
                if guest_name.lower() in str(ep_guest).lower():
                    episodes.append({
                        'id': ep_file.stem,
                        'title': fm.get('title', ''),
                        'date': str(fm.get('publish_date', fm.get('episode_date', '')))[:10],
                        'podcast': pod_dir.name,
                    })
    if not episodes:
        return {"error": f"No episodes found for guest '{guest_name}'"}
    episodes.sort(key=lambda e: e['date'], reverse=True)
    return {'name': guest_name, 'appearances': len(episodes), 'episodes': episodes[:20]}


def do_find_insights(topic: str, limit: int = 10) -> dict:
    """Find insights and episodes related to a topic."""
    topic_slug = topic.lower().replace(' ', '-')
    topic_file = WIKI_DIR / "topics" / f"{topic_slug}.md"
    topic_info = {}
    if topic_file.exists():
        fm, body = read_frontmatter(topic_file)
        topic_info = {
            'label': fm.get('label', topic),
            'episodes_covered': fm.get('episodes_covered', []),
            'source_podcasts': fm.get('source_podcasts', []),
        }
    matched_episodes = do_search_episodes(topic, limit=limit)
    return {'topic': topic, 'topic_page': topic_info, 'matching_episodes': matched_episodes}


def do_weekly_summary() -> list:
    """Get summaries of the most recent episodes."""
    all_episodes = []
    episodes_dir = WIKI_DIR / "episodes"
    if episodes_dir.exists():
        for pod_dir in episodes_dir.iterdir():
            if not pod_dir.is_dir():
                continue
            for ep_file in find_files(pod_dir)[:10]:
                fm, body = read_frontmatter(ep_file)
                all_episodes.append({
                    'episode_id': ep_file.stem,
                    'podcast': fm.get('podcast', pod_dir.name),
                    'title': fm.get('title', ''),
                    'date': fm.get('episode_date', ''),
                    'guest': fm.get('guest', ''),
                    'tags': fm.get('tags', []),
                    'key_insights': fm.get('key_insights', [])[:3],
                })
    all_episodes.sort(key=lambda e: e['date'], reverse=True)
    return all_episodes[:10]


def do_get_podcast_stats() -> dict:
    """Get quick stats on the knowledge base."""
    stats = {}
    episodes_dir = WIKI_DIR / "episodes"
    if episodes_dir.exists():
        total = 0
        by_podcast = {}
        for pod_dir in episodes_dir.iterdir():
            if not pod_dir.is_dir():
                continue
            count = len(list(pod_dir.glob("*.md")))
            by_podcast[pod_dir.name] = count
            total += count
        stats['total_episodes'] = total
        stats['by_podcast'] = by_podcast
    guests_dir = WIKI_DIR / "guests"
    if guests_dir.exists():
        stats['total_guests'] = len(list(guests_dir.glob("*.md")))
    topics_dir = WIKI_DIR / "topics"
    if topics_dir.exists():
        stats['total_topics'] = len(list(topics_dir.glob("*.md")))
    stats['wiki_path'] = str(WIKI_DIR)
    return stats


def do_ask(query: str) -> dict:
    """Combined Q&A — search + prepare context for LLM synthesis."""
    episodes = do_search_episodes(query, limit=5)
    return {
        'query': query,
        'results': episodes,
        'note': 'Pass these results to your LLM for synthesis. Each result has title, date, guest, and a content snippet.'
    }


def do_search_by_meaning(query: str, limit: int = 10, podcast: str | None = None) -> dict:
    """Semantic search — finds episodes by meaning, not just keywords."""
    if not load_semantic():
        return {"error": "Semantic index not available. Run `python3 scripts/semantic_index.py rebuild` first."}
    t0 = time.time()
    results = _semantic_query_fn(query, k=limit, podcast=podcast)
    t1 = time.time()
    return {'query': query, 'results': results, 'latency_ms': round((t1 - t0) * 1000)}


def do_semantic_stats() -> dict:
    """FAISS index health check."""
    if not load_semantic():
        return {"error": "Semantic index not available"}
    index, chunks, _ = _semantic_query_fn.__globals__.get('load_index', lambda: (None, None, None))()
    return {"total_vectors": index.ntotal if index else 0, "total_chunks": len(chunks) if chunks else 0}


# ── MCP Tool Registration ──────────────────────────────────────────────

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_episodes",
            description="Search episodes by keyword across titles, descriptions, and transcripts",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "podcast": {"type": "string", "description": "Filter by podcast (lenny, 20vc)"},
                    "limit": {"type": "integer", "description": "Max results (default 10)"},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="get_guest_profile",
            description="Get a guest's full profile and list of episode appearances",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Guest name (e.g. 'Elena Verna')"},
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="find_insights",
            description="Find episodes and insights related to a business/tech topic",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "Topic to search (e.g. 'product-led growth')"},
                    "limit": {"type": "integer", "description": "Max results (default 10)"},
                },
                "required": ["topic"],
            },
        ),
        Tool(
            name="ask",
            description="Full Q&A — searches episodes and returns context for LLM synthesis",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Natural language question"},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="weekly_summary",
            description="Get summaries of the most recent episodes",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {"type": "integer", "description": "Max results (default 10)"},
                },
            },
        ),
        Tool(
            name="get_podcast_stats",
            description="Get quick stats — total episodes, guests, topics",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        Tool(
            name="search_by_meaning",
            description="Semantic search — finds episodes by meaning using vector embeddings",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Natural language query"},
                    "limit": {"type": "integer", "description": "Max results (default 10)"},
                    "podcast": {"type": "string", "description": "Filter by podcast (lenny, 20vc)"},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="semantic_stats",
            description="FAISS index health — total vectors and chunks",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    try:
        args = arguments or {}
        if name == "search_episodes":
            result = do_search_episodes(args.get("query", ""), args.get("podcast"), args.get("limit", 10))
        elif name == "get_guest_profile":
            result = do_get_guest_profile(args.get("name", ""))
        elif name == "find_insights":
            result = do_find_insights(args.get("topic", ""), args.get("limit", 10))
        elif name == "ask":
            result = do_ask(args.get("query", ""))
        elif name == "weekly_summary":
            result = do_weekly_summary()
        elif name == "get_podcast_stats":
            result = do_get_podcast_stats()
        elif name == "search_by_meaning":
            result = do_search_by_meaning(args.get("query", ""), args.get("limit", 10), args.get("podcast"))
        elif name == "semantic_stats":
            result = do_semantic_stats()
        else:
            return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]
        return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]
    except Exception as e:
        return [TextContent(type="text", text=json.dumps({"error": str(e)}))]


# ── Main ───────────────────────────────────────────────────────────────

async def main():
    print("Starting Podcast Wiki MCP Server (MCP SDK v2)", file=sys.stderr)
    print(f"Wiki: {WIKI_DIR}", file=sys.stderr)

    # Pre-warm semantic search model
    print("Warming semantic search model...", file=sys.stderr)
    try:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        _model.encode(["warmup"], normalize_embeddings=True)
        print("Semantic search model ready", file=sys.stderr)
    except Exception as e:
        print(f"Model warmup skipped: {e}", file=sys.stderr)

    async with stdio_server() as (read_stream, write_stream):
        print("MCP server ready on stdio", file=sys.stderr)
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
