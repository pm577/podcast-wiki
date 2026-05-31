#! /home/philip/.yt-env/bin/python3
"""
Semantic Search Indexer v2 — Enriched Index
--------------------------------------------
Rebuilds the FAISS index to include enriched entity and concept pages
(not just raw transcripts), tagging each vector with a source type.

Pipeline:
  1. Walk all episodes, chunk into ~500-word overlapping segments (tagged 'raw')
  2. Walk enriched entity pages (>30 lines) in wiki/entities/, chunk (tagged 'entity')
  3. Walk enriched concept pages (>30 lines) in wiki/concepts/, chunk (tagged 'concept')
  4. Embed each chunk with sentence-transformers (all-MiniLM-L6-v2)
  5. Build FAISS index (IndexIDMap + IndexFlatIP)
  6. Persist index + SQLite metadata to data/faiss_v2/

Usage:
  python3 scripts/semantic_index_v2.py --rebuild          # Full rebuild
  python3 scripts/semantic_index_v2.py --rebuild --limit 10  # Quick test
  python3 scripts/semantic_index_v2.py --query "..."      # Query the v2 index
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
DATA_DIR = WIKI_DIR / "data" / "faiss_v2"
FAISS_PATH = DATA_DIR / "faiss_index.bin"
SQLITE_PATH = DATA_DIR / "chunks.sqlite"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_WORDS = 500
CHUNK_OVERLAP = 100
MIN_LINES_FOR_ENRICHED = 30  # minimum lines to consider a page "enriched"


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


def collect_episode_chunks(limit=None):
    """Walk all podcast episode markdown files and produce chunks tagged 'raw'."""
    episodes_dir = WIKI_DIR / "episodes"
    chunks = []

    if not episodes_dir.exists():
        print(f"WARNING: {episodes_dir} not found")
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
                    continue
                chunks.append({
                    'source_type': 'raw',
                    'source_id': ep_file.stem,
                    'podcast': pod_dir.name,
                    'title': title,
                    'guest': str(guest),
                    'date': date,
                    'chunk_index': i,
                    'chunk_count': len(episode_chunks),
                    'text': chunk_text_content[:2000],
                    'entity_name': '',
                    'concept_name': '',
                })

            total_episodes += 1

    return chunks


def collect_entity_chunks(limit=None):
    """Walk enriched entity pages (>30 lines) in wiki/entities/, produce chunks tagged 'entity'."""
    entities_dir = WIKI_DIR / "wiki" / "entities"
    chunks = []
    if not entities_dir.exists():
        print(f"WARNING: {entities_dir} not found")
        return chunks

    total = 0
    for ef in sorted(entities_dir.glob("*.md")):
        if limit and total >= limit:
            return chunks
        try:
            content = ef.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue

        # Only include enriched pages (>30 lines)
        if len(content.splitlines()) <= MIN_LINES_FOR_ENRICHED:
            continue

        fm, body = read_frontmatter(content)
        if not body.strip():
            continue

        title = fm.get('title', ef.stem)
        tags = fm.get('tags', [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(',') if t.strip()]

        episode_chunks = chunk_text(body)
        for i, chunk_text_content in enumerate(episode_chunks):
            if len(chunk_text_content.split()) < 20:
                continue
            chunks.append({
                'source_type': 'entity',
                'source_id': ef.stem,
                'podcast': '',
                'title': title,
                'guest': title,  # entity name IS the guest
                'date': '',
                'chunk_index': i,
                'chunk_count': len(episode_chunks),
                'text': chunk_text_content[:2000],
                'entity_name': title,
                'concept_name': '',
            })
        total += 1

    return chunks


def collect_concept_chunks(limit=None):
    """Walk enriched concept pages (>30 lines) in wiki/concepts/, produce chunks tagged 'concept'."""
    concepts_dir = WIKI_DIR / "wiki" / "concepts"
    chunks = []
    if not concepts_dir.exists():
        print(f"WARNING: {concepts_dir} not found")
        return chunks

    total = 0
    for cf in sorted(concepts_dir.glob("*.md")):
        if limit and total >= limit:
            return chunks
        try:
            content = cf.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue

        # Only include enriched pages (>30 lines)
        if len(content.splitlines()) <= MIN_LINES_FOR_ENRICHED:
            continue

        fm, body = read_frontmatter(content)
        if not body.strip():
            continue

        title = fm.get('title', cf.stem)
        tags = fm.get('tags', [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(',') if t.strip()]

        episode_chunks = chunk_text(body)
        for i, chunk_text_content in enumerate(episode_chunks):
            if len(chunk_text_content.split()) < 20:
                continue
            chunks.append({
                'source_type': 'concept',
                'source_id': cf.stem,
                'podcast': '',
                'title': title,
                'guest': '',
                'date': '',
                'chunk_index': i,
                'chunk_count': len(episode_chunks),
                'text': chunk_text_content[:2000],
                'entity_name': '',
                'concept_name': title,
            })
        total += 1

    return chunks


def collect_all_chunks(limit=None):
    """Collect all chunks from episodes, entities, and concepts."""
    all_chunks = []

    print("Collecting episode chunks (raw transcripts)...")
    ep_chunks = collect_episode_chunks(limit=limit)
    print(f"  {len(ep_chunks)} raw chunks from episodes")
    all_chunks.extend(ep_chunks)

    print("Collecting entity page chunks...")
    ent_chunks = collect_entity_chunks(limit=limit)
    print(f"  {len(ent_chunks)} entity chunks from wiki/entities/")
    all_chunks.extend(ent_chunks)

    print("Collecting concept page chunks...")
    con_chunks = collect_concept_chunks(limit=limit)
    print(f"  {len(con_chunks)} concept chunks from wiki/concepts/")
    all_chunks.extend(con_chunks)

    print(f"\nTotal: {len(all_chunks)} chunks ({len(ep_chunks)} raw + {len(ent_chunks)} entity + {len(con_chunks)} concept)")
    return all_chunks


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
            source_type TEXT,
            source_id TEXT,
            podcast TEXT,
            title TEXT,
            guest TEXT,
            date TEXT,
            chunk_index INTEGER,
            chunk_count INTEGER,
            text TEXT,
            entity_name TEXT,
            concept_name TEXT
        )
    """)
    conn.executemany(
        "INSERT INTO chunks (id, source_type, source_id, podcast, title, guest, date, chunk_index, chunk_count, text, entity_name, concept_name) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [(i, c['source_type'], c['source_id'], c['podcast'], c['title'], c['guest'],
          c['date'], c['chunk_index'], c['chunk_count'], c['text'],
          c['entity_name'], c['concept_name'])
         for i, c in enumerate(chunks)]
    )
    conn.commit()
    conn.close()
    print(f"  SQLite metadata written: {SQLITE_PATH}")


def load_index():
    """Load FAISS v2 index and SQLite metadata."""
    if not FAISS_PATH.exists() or not SQLITE_PATH.exists():
        print("No v2 index found. Run with --rebuild first.")
        return None, None, None

    index = faiss.read_index(str(FAISS_PATH))

    conn = sqlite3.connect(str(SQLITE_PATH))
    conn.row_factory = sqlite3.Row
    chunks = [dict(row) for row in conn.execute("SELECT * FROM chunks ORDER BY id")]
    conn.close()

    model = SentenceTransformer(MODEL_NAME)

    return index, chunks, model


def query_index(query, k=10, podcast=None, source_type=None):
    """Search the v2 index for semantically similar chunks, optionally filtering by podcast or source_type."""
    index, chunks, model = load_index()
    if index is None:
        return []

    # Embed query
    query_vec = model.encode([query], normalize_embeddings=True)

    # Search — over-fetch for filtering
    overfetch = k * 5 if (podcast or source_type) else k * 3
    scores, ids = index.search(query_vec.astype(np.float32), overfetch)

    results = []
    for score, idx in zip(scores[0], ids[0]):
        if idx == -1:
            continue
        chunk = chunks[int(idx)]

        if podcast and chunk.get('podcast', '') and chunk['podcast'] != podcast.lower():
            continue
        if source_type and chunk.get('source_type', '') != source_type:
            continue

        results.append({
            'score': float(score),
            'source_type': chunk['source_type'],
            'source_id': chunk['source_id'],
            'podcast': chunk.get('podcast', ''),
            'title': chunk.get('title', ''),
            'guest': chunk.get('guest', ''),
            'date': chunk.get('date', ''),
            'entity_name': chunk.get('entity_name', ''),
            'concept_name': chunk.get('concept_name', ''),
            'snippet': chunk.get('text', '')[:300],
            'chunk': chunk.get('chunk_index', 0),
            'chunks_total': chunk.get('chunk_count', 0),
        })

        if len(results) >= k:
            break

    return results


# ── CLI ──────────────────────────────────────────────────────────────

def cmd_rebuild(args):
    print("=== Semantic Index v2 Rebuild ===\n")

    limit = args.limit if args.limit and args.limit > 0 else None
    print(f"Collecting chunks{' (limit: ' + str(limit) + ')' if limit else ''}...")
    chunks = collect_all_chunks(limit=limit)

    if not chunks:
        print("ERROR: No chunks found")
        return

    print("\nBuilding index...")
    index, embeddings, model = build_index(chunks)
    print()

    print("Saving...")
    save_index(index, chunks)

    # Print source breakdown
    from collections import Counter
    st = Counter(c['source_type'] for c in chunks)
    print("\nIndex breakdown by source type:")
    for stype, cnt in sorted(st.items()):
        print(f"  {stype}: {cnt} chunks")

    print("\nDone! v2 index saved to data/faiss_v2/")


def cmd_query(args):
    results = query_index(args.query, k=args.k, podcast=args.podcast, source_type=args.source_type)

    if not results:
        print("No results.")
        return

    print(f"Top {len(results)} results for: '{args.query}'\n")
    for i, r in enumerate(results, 1):
        stype = r['source_type']
        label = r.get('entity_name') or r.get('concept_name') or r['title']
        print(f"{i}. [{stype}] {label}")
        if r['guest']:
            print(f"   Guest: {r['guest']}")
        if r['podcast']:
            print(f"   Podcast: {r['podcast']} ({r['date']})")
        print(f"   Score: {r['score']:.3f}")
        print(f"   {r['snippet'][:200]}...")
        print()


def cmd_stats(args):
    index, chunks, _ = load_index()
    if index is None:
        return
    print(f"Total vectors: {index.ntotal}")
    print(f"Total chunks: {len(chunks)}")

    from collections import Counter
    by_type = Counter(c['source_type'] for c in chunks)
    print("\nBy source type:")
    for stype, cnt in sorted(by_type.items()):
        print(f"  {stype}: {cnt}")

    by_podcast = Counter()
    guests = set()
    for c in chunks:
        if c.get('podcast'):
            by_podcast[c['podcast']] += 1
        if c.get('guest'):
            guests.add(c['guest'])
    if by_podcast:
        print("\nBy podcast:")
        for pod, cnt in sorted(by_podcast.items()):
            print(f"  {pod}: {cnt} chunks")
    print(f"\nUnique guests/entities: {len(guests)}")


def main():
    parser = argparse.ArgumentParser(description="Semantic Search Indexer v2 — includes entity & concept pages")
    sub = parser.add_subparsers(dest='command')

    rebuild = sub.add_parser('rebuild', help='Full index rebuild (episodes + entities + concepts)')
    rebuild.add_argument('--limit', type=int, default=0, help='Limit files per source (for testing)')

    query = sub.add_parser('query', help='Query the v2 index')
    query.add_argument('query', help='Search query')
    query.add_argument('--k', type=int, default=10, help='Number of results')
    query.add_argument('--podcast', help='Filter by podcast (lenny, 20vc)')
    query.add_argument('--source-type', choices=['raw', 'entity', 'concept'], help='Filter by source type')

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
