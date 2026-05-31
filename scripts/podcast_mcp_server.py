#! /home/philip/.yt-env/bin/python3
"""
Podcast Wiki MCP Server

Provides MCP tools for querying the podcast knowledge base.
Colleagues can connect from Claude Code, Cursor, or any MCP client.

Tools:
- search_episodes: Semantic search across all episodes
- get_guest_profile: Get a guest's full profile and appearances
- find_insights: Find insights on a topic
- ask: Full Q&A that searches the wiki and returns a synthesized answer
- weekly_summary: Most recent episodes with summaries
- get_podcast_stats: Quick stats on the knowledge base

Run: python3 podcast_mcp_server.py
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime, timedelta

# Semantic search (loaded on demand)
_semantic_loaded = False
_semantic_query_fn = None

WIKI_DIR = Path(os.path.expanduser("~/.hermes/podcast-wiki"))


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
            except:
                pass
            body = parts[2]
    
    return fm, body.strip()


def search_episodes(query, podcast=None, limit=10):
    """Search episodes by keyword in title, description, and transcript."""
    query_lower = query.lower()
    results = []
    
    episodes_dir = WIKI_DIR / "episodes"
    if not episodes_dir.exists():
        return {"error": "No episodes directory found", "results": []}
    
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
            
            # Simple keyword scoring
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


def get_guest_profile(guest_name):
    """Get a guest's full profile, appearances, and topics."""
    guest_slug = guest_name.lower().replace(' ', '-')
    
    # Search across Lenny 20VC and newsletter episodes for this guest
    episodes = []
    episodes_dir = WIKI_DIR / "episodes"
    
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
    
    return {
        'name': guest_name,
        'appearances': len(episodes),
        'episodes': episodes[:20],
    }


def find_insights(topic, limit=10):
    """Find insights and episodes related to a topic."""
    topic_slug = topic.lower().replace(' ', '-')
    
    # Check topic page
    topic_file = WIKI_DIR / "topics" / f"{topic_slug}.md"
    topic_info = {}
    
    if topic_file.exists():
        fm, body = read_frontmatter(topic_file)
        topic_info = {
            'label': fm.get('label', topic),
            'episodes_covered': fm.get('episodes_covered', []),
            'source_podcasts': fm.get('source_podcasts', []),
        }
    
    # Search across all episodes for this topic
    matched_episodes = search_episodes(topic, limit=limit)
    
    return {
        'topic': topic,
        'topic_page': topic_info,
        'matching_episodes': matched_episodes,
    }


def weekly_summary():
    """Get summaries of the most recent episodes."""
    all_episodes = []
    
    episodes_dir = WIKI_DIR / "episodes"
    if not episodes_dir.exists():
        return {"error": "No episodes directory"}
    
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


def get_podcast_stats():
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


# ── Semantic Search ──────────────────────────────────────────────────

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
    except Exception as e:
        return False


def search_by_meaning(query, limit=10, podcast=None):
    """Semantic search — finds episodes by meaning, not just keywords."""
    if not load_semantic():
        return {"error": "Semantic index not available. Run `python3 scripts/semantic_index.py rebuild` first."}
    
    t0 = time.time()
    results = _semantic_query_fn(query, k=limit, podcast=podcast)
    t1 = time.time()
    
    return {
        'query': query,
        'results': results,
        'latency_ms': round((t1 - t0) * 1000),
    }


# === MCP Tool Handlers ===

def handle_mcp_request(request):
    """Handle an incoming MCP request and dispatch to the right tool."""
    tool = request.get('tool', '')
    params = request.get('params', {})
    
    if tool == 'search_episodes':
        return search_episodes(
            params.get('query', ''),
            podcast=params.get('podcast'),
            limit=params.get('limit', 10)
        )
    elif tool == 'get_guest_profile':
        return get_guest_profile(params.get('name', ''))
    elif tool == 'find_insights':
        return find_insights(
            params.get('topic', ''),
            limit=params.get('limit', 10)
        )
    elif tool == 'weekly_summary':
        return weekly_summary()
    elif tool == 'get_podcast_stats':
        return get_podcast_stats()
    elif tool == 'ask':
        query = params.get('query', '')
        # Use semantic search for better results, fall back to keyword
        semantic_results = search_by_meaning(query, limit=3)
        keyword_results = search_episodes(query, limit=3)
        
        # Get entity context: find related people from the top results
        related_entities = []
        all_results = (semantic_results.get('results', []) if isinstance(semantic_results, dict) else []) + keyword_results
        for r in all_results[:5]:
            guest = r.get('guest', r.get('entity_name', ''))
            if guest and guest not in related_entities and guest != 'unknown-guest':
                related_entities.append(guest)
            # Also check the results structure from semantic search
            source_id = r.get('source_id', '')
            if source_id and source_id not in related_entities and '_' not in source_id:
                related_entities.append(source_id)
        
        return {
            'query': query,
            'semantic_matches': semantic_results.get('results', semantic_results)[:5] if isinstance(semantic_results, dict) else semantic_results[:5],
            'keyword_matches': keyword_results[:3],
            'related_entities': related_entities[:5],
            'note': 'Results from semantic and keyword search. Use semantic_matches for meaning-based queries, keyword_matches for exact matches.'
        }
    elif tool == 'search_by_meaning':
        return search_by_meaning(
            params.get('query', ''),
            limit=params.get('limit', 10),
            podcast=params.get('podcast'),
        )
    elif tool == 'semantic_stats':
        if not load_semantic():
            return {"error": "Semantic index not available"}
        index, chunks, _ = _semantic_query_fn.__globals__.get('load_index', lambda: (None, None, None))()
        return {"total_vectors": index.ntotal if index else 0, "total_chunks": len(chunks) if chunks else 0}
    else:
        return {"error": f"Unknown tool: {tool}"}


def print_tool_schema():
    """Print the MCP tool schema for discovery."""
    schema = {
        "schema_version": "1.0",
        "server_name": "podcast-wiki",
        "server_description": "Knowledge base for Lenny's Podcast and 20VC. Search episodes, get guest profiles, find insights, get weekly summaries.",
        "tools": [
            {
                "name": "search_episodes",
                "description": "Search episodes by keyword across titles, descriptions, and transcripts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query"},
                        "podcast": {"type": "string", "description": "Filter by podcast (lenny, 20vc)", "optional": True},
                        "limit": {"type": "integer", "description": "Max results", "default": 10}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "get_guest_profile",
                "description": "Get a guest's full profile with episode appearances and topics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Guest name"}
                    },
                    "required": ["name"]
                }
            },
            {
                "name": "find_insights",
                "description": "Find insights and episode recommendations on a topic",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "description": "Topic to research"},
                        "limit": {"type": "integer", "description": "Max results", "default": 10}
                    },
                    "required": ["topic"]
                }
            },
            {
                "name": "weekly_summary",
                "description": "Get summaries of the most recent episodes",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_podcast_stats",
                "description": "Get quick stats on the knowledge base",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "ask",
                "description": "Ask a question and get relevant episodes and insights",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Your question"}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "search_by_meaning",
                "description": "Semantic search — finds episodes by meaning using AI embeddings (not just keyword matching)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Your research question or topic"},
                        "podcast": {"type": "string", "description": "Filter by podcast (lenny, 20vc)", "optional": True},
                        "limit": {"type": "integer", "description": "Max results", "default": 10}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "semantic_stats",
                "description": "Get stats on the semantic search index",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
    }
    print(json.dumps(schema, indent=2))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--schema":
        print_tool_schema()
        return
    
    if len(sys.argv) > 1 and sys.argv[1] == "--stats":
        stats = get_podcast_stats()
        print(json.dumps(stats, indent=2))
        return
    
    if len(sys.argv) > 1 and sys.argv[1] == "--search":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        results = search_episodes(query)
        print(json.dumps(results, indent=2))
        return
    
    # MCP stdio mode — reads JSON requests from stdin, writes JSON responses to stdout
    print("Podcast Wiki MCP Server", file=sys.stderr)
    print(f"Wiki: {WIKI_DIR}", file=sys.stderr)
    
    # Pre-warm semantic search model so first user call is fast
    print("Warming semantic search model...", file=sys.stderr)
    try:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        _model.encode(["warmup"], normalize_embeddings=True)
        print("Semantic search model ready", file=sys.stderr)
    except Exception as e:
        print(f"Model warmup skipped: {e}", file=sys.stderr)
    
    print(f"Ready. Send JSON requests on stdin.", file=sys.stderr)
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            result = handle_mcp_request(request)
            response = json.dumps({"success": True, "result": result})
            print(response, flush=True)
        except json.JSONDecodeError as e:
            print(json.dumps({"success": False, "error": f"Invalid JSON: {e}"}), flush=True)
        except Exception as e:
            print(json.dumps({"success": False, "error": str(e)}), flush=True)


if __name__ == "__main__":
    main()
