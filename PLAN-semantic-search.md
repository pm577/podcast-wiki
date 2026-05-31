# SEMANTIC SEARCH UPGRADE — Podcast Wiki

**Inspired by:** semantic-search/IntelliSenseSearch, Typesense_indexing, pysemantic-search

## Architecture

```
Transcripts (1,823 files)
       │ chunk (500 words, 100 overlap)
       ▼
Chunk Store (SQLite) ──→ Sentence Transformers ──→ FAISS Index
       │                       (all-MiniLM-L6-v2)     (384d vectors)
       │                         runs on CPU
       ▼
MCP Tool: search_by_meaning(query, limit=10)
  → embed query with same model
  → FAISS: top-k nearest neighbors
  → return chunks + episode links + similarity scores
```

**$0 API cost.** Everything runs locally on this VPS.

## Files to create/modify

| File | Purpose |
|------|---------|
| `scripts/semantic_index.py` | Build FAISS index from all transcripts |
| `scripts/search_by_meaning.py` | CLI query tool (for testing) |
| `MCP tool: search_by_meaning` | Added to `podcast_mcp_server.py` |
| `data/faiss_index.bin` | Persistent FAISS index (gitignored) |
| `data/chunks.sqlite` | Chunk metadata (episode, guest, text) |

## Technical choices

- **Model:** `all-MiniLM-L6-v2` (384-dim vectors, 80MB, fast CPU inference)
- **Chunk size:** 500 words with 100-word overlap (good balance for transcript paragraphs)
- **FAISS index:** `IndexIDMap` wrapping `IndexFlatIP` (inner product = cosine similarity for normalized vectors)
- **Storage:** FAISS binary for vectors, SQLite for metadata — simple, no dependencies
- **RAM:** ~5,000 chunks × 384 dims × 4 bytes = ~8 MB for FAISS. Total <100 MB.

## Checklist

### Phase 1: Foundation
- [x] Install `sentence-transformers`, `faiss-cpu`
- [x] Build `scripts/semantic_index.py` — chunker + embedder + indexer
- [x] First index run — verify it builds successfully
- [x] Verify index quality with test queries

### Phase 2: MCP Integration
- [ ] Add `search_by_meaning` tool to `podcast_mcp_server.py`
- [ ] Test MCP tool end-to-end
- [ ] Auto-rebuild index on daily harvest (update `daily_harvester.py`)

### Phase 3: Polish (inspired by semantic-search org)
- [ ] Add search-by-podcast filter (only Lenny, only 20VC)
- [ ] Add phrase-level highlighting (show matching sentence within chunk)
- [ ] Log query analytics (most searched topics, hit rates)
- [ ] Persist FAISS index + SQLite in `data/` dir

### Phase 4: Optional Upgrades
- [ ] Typesense hybrid search (keyword + vector) for production use
- [ ] Combined `search_by_keyword` + `search_by_meanin` in one response
- [ ] Embed newsletter posts too
- [ ] Timestamp-level search (find when in an episode something was said)
