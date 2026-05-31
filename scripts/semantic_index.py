#! /home/philip/.yt-env/bin/python3
"""
Semantic Search Indexer for Podcast Wiki
-----------------------------------------
Inspired by semantic-search/IntelliSenseSearch and pysemantic-search.

Pipeline:
  1. Walk all episodes, chunk them into ~500-word overlapping segments
  2. Embed each chunk with sentence-transformers (all-MiniLM-L6-v2)
  3. Build a FAISS index (IndexIDMap + IndexFlatIP)
  4. Persist index to disk + SQLite metadata store

Usage:
  python3 scripts/semantic_index.py --rebuild    # Full rebuild
  python3 scripts/semantic_index.py --rebuild --limit 20  # Quick test with 20 files
  python3 scripts/semantic_index.py --query "retaining users during freemium"
"""

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

WIKI_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = WIKI_DIR / "data"
FAISS_PATH = DATA_DIR / "faiss_index.bin"
SQLITE_PATH = DATA_DIR / "chunks.sqlite"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_WORDS = 500
CHUNK_OVERLAP = 100


# ── Chunking ──────────────────────────────────────────────────────────

def read_frontmatter(content):
    """Extract YAML frontmatter and body from markdown content."""
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


def chunk_text(text, words_per_chunk=CHUNK_WORDS, overlap=CHUNK_OVERLAP):
    """Split text into overlapping word-level chunks."""
    # Clean markdown artifacts
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # bold
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # links
    text = re.sub(r'#{1,6}\s+', '', text)  # headers
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    words = text.split()
    chunks = []
    
    if len(words) <= words_per_chunk:
        return [' '.join(words)]
    
    start = 0
    while start < len(words):
        end = min(start + words_per_chunk, len(words))
        chunk = ' '.join(words[start:end])
        if chunk.strip():
            chunks.append(chunk)
        start += words_per_chunk - overlap
    
    return chunks


def collect_chunks(limit=None):
    """Walk all podcast episodes and produce chunks with metadata."""
    episodes_dir = WIKI_DIR / "episodes"
    chunks = []
    
    if not episodes_dir.exists():
        print(f"ERROR: {episodes_dir} not found")
        return chunks
    
    total_episodes = 0
    for pod_dir in sorted(episodes_dir.iterdir()):
        if not pod_dir.is_dir():
            continue
        for ep_file in sorted(pod_dir.glob("*.md")):
            if limit and total_episodes >= limit:
                return chunks
            
            try:
                content = ep_file.read_text(encoding='utf-8', errors='replace')
            except Exception:
                continue
            
            fm, body = read_frontmatter(content)
            if not body.strip():
                continue
            
            title = fm.get('title', ep_file.stem)
            guest = fm.get('guest', '')
            date = str(fm.get('publish_date', fm.get('episode_date', '')))[:10]
            
            episode_chunks = chunk_text(body)
            
            for i, chunk_text_content in enumerate(episode_chunks):
                if len(chunk_text_content.split()) < 20:
                    continue  # skip tiny chunks
                chunks.append({
                    'episode_id': ep_file.stem,
                    'podcast': pod_dir.name,
                    'title': title,
                    'guest': str(guest),
                    'date': date,
                    'chunk_index': i,
                    'chunk_count': len(episode_chunks),
                    'text': chunk_text_content[:2000],  # cap at 2000 chars for safety
                })
            
            total_episodes += 1
    
    return chunks


# ── Embedding & Indexing ─────────────────────────────────────────────

def build_index(chunks):
    """Embed chunks and build FAISS index."""
    print(f"Loading model {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    
    texts = [c['text'] for c in chunks]
    
    print(f"Embedding {len(texts)} chunks...")
    t0 = time.time()
    embeddings = model.encode(texts, show_progress_bar=True, normalize_embeddings=True)
    t1 = time.time()
    print(f"  Embedded in {t1-t0:.1f}s ({len(texts)/(t1-t0):.0f} chunks/s)")
    
    dim = embeddings.shape[1]
    print(f"  Dimension: {dim}")
    
    # Build FAISS index (inner product = cosine sim since vectors are normalized)
    index_flat = faiss.IndexFlatIP(dim)
    index = faiss.IndexIDMap(index_flat)
    
    # IDs must be int64
    ids = np.arange(len(chunks), dtype=np.int64)
    index.add_with_ids(embeddings.astype(np.float32), ids)
    
    print(f"  Index size: {index.ntotal} vectors")
    
    return index, embeddings, model


def save_index(index, chunks):
    """Persist FAISS index and SQLite metadata."""
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # Save FAISS
    faiss.write_index(index, str(FAISS_PATH))
    print(f"  FAISS index written: {FAISS_PATH} ({os.path.getsize(FAISS_PATH)/1024:.0f} KB)")
    
    # Save SQLite
    if SQLITE_PATH.exists():
        SQLITE_PATH.unlink()
    
    conn = sqlite3.connect(str(SQLITE_PATH))
    conn.execute("""
        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            episode_id TEXT,
            podcast TEXT,
            title TEXT,
            guest TEXT,
            date TEXT,
            chunk_index INTEGER,
            chunk_count INTEGER,
            text TEXT
        )
    """)
    conn.executemany(
        "INSERT INTO chunks (id, episode_id, podcast, title, guest, date, chunk_index, chunk_count, text) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [(i, c['episode_id'], c['podcast'], c['title'], c['guest'], c['date'],
          c['chunk_index'], c['chunk_count'], c['text'])
         for i, c in enumerate(chunks)]
    )
    conn.commit()
    conn.close()
    print(f"  SQLite metadata written: {SQLITE_PATH}")


def load_index():
    """Load FAISS index and SQLite metadata."""
    if not FAISS_PATH.exists() or not SQLITE_PATH.exists():
        print("No index found. Run with --rebuild first.")
        return None, None, None
    
    index = faiss.read_index(str(FAISS_PATH))
    
    conn = sqlite3.connect(str(SQLITE_PATH))
    conn.row_factory = sqlite3.Row
    chunks = [dict(row) for row in conn.execute("SELECT * FROM chunks ORDER BY id")]
    conn.close()
    
    model = SentenceTransformer(MODEL_NAME)
    
    return index, chunks, model


def query_index(query, k=10, podcast=None):
    """Search the index for semantically similar chunks."""
    index, chunks, model = load_index()
    if index is None:
        return []
    
    # Embed query
    query_vec = model.encode([query], normalize_embeddings=True)
    
    # Search
    scores, ids = index.search(query_vec.astype(np.float32), k * 3)  # over-fetch for filtering
    
    results = []
    for score, idx in zip(scores[0], ids[0]):
        if idx == -1:
            continue
        chunk = chunks[int(idx)]
        
        if podcast and chunk['podcast'] != podcast.lower():
            continue
        
        results.append({
            'score': float(score),
            'episode_id': chunk['episode_id'],
            'podcast': chunk['podcast'],
            'title': chunk['title'],
            'guest': chunk['guest'],
            'date': chunk['date'],
            'snippet': chunk['text'][:300],
            'chunk': chunk['chunk_index'],
            'chunks_total': chunk['chunk_count'],
        })
        
        if len(results) >= k:
            break
    
    return results


# ── CLI ──────────────────────────────────────────────────────────────

def cmd_rebuild(args):
    print("=== Semantic Index Rebuild ===\n")
    
    limit = args.limit if args.limit and args.limit > 0 else None
    print(f"Collecting chunks{' (limit: ' + str(limit) + ' episodes)' if limit else ''}...")
    chunks = collect_chunks(limit=limit)
    print(f"  {len(chunks)} chunks from {len(set(c['episode_id'] for c in chunks))} episodes\n")
    
    if not chunks:
        print("ERROR: No chunks found")
        return
    
    print("Building index...")
    index, embeddings, model = build_index(chunks)
    print()
    
    print("Saving...")
    save_index(index, chunks)
    print("\nDone!")


def cmd_query(args):
    results = query_index(args.query, k=args.k, podcast=args.podcast)
    
    if not results:
        print("No results.")
        return
    
    print(f"Top {len(results)} results for: '{args.query}'\n")
    for i, r in enumerate(results, 1):
        print(f"{i}. [{r['podcast']}] {r['title']} ({r['date']}) — score: {r['score']:.3f}")
        print(f"   Guest: {r['guest']}")
        print(f"   {r['snippet'][:200]}...")
        print()


def cmd_stats(args):
    index, chunks, _ = load_index()
    if index is None:
        return
    print(f"Total vectors: {index.ntotal}")
    print(f"Total chunks: {len(chunks)}")
    by_podcast = {}
    guests = set()
    for c in chunks:
        by_podcast[c['podcast']] = by_podcast.get(c['podcast'], 0) + 1
        if c['guest']:
            guests.add(c['guest'])
    print(f"Unique guests: {len(guests)}")
    for pod, cnt in sorted(by_podcast.items()):
        print(f"  {pod}: {cnt} chunks")


def main():
    parser = argparse.ArgumentParser(description="Semantic Search Indexer")
    sub = parser.add_subparsers(dest='command')
    
    rebuild = sub.add_parser('rebuild', help='Full index rebuild')
    rebuild.add_argument('--limit', type=int, default=0, help='Limit episodes (for testing)')
    
    query = sub.add_parser('query', help='Query the index')
    query.add_argument('query', help='Search query')
    query.add_argument('--k', type=int, default=10, help='Number of results')
    query.add_argument('--podcast', help='Filter by podcast (lenny, 20vc)')
    
    sub.add_parser('stats', help='Index statistics')
    
    # Default to --rebuild if no command given (for cron usage)
    if len(sys.argv) == 1:
        sys.argv.append('rebuild')
    
    args = parser.parse_args()
    
    if args.command == 'rebuild':
        cmd_rebuild(args)
    elif args.command == 'query':
        cmd_query(args)
    elif args.command == 'stats':
        cmd_stats(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
