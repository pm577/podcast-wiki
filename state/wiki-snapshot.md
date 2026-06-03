---
type: State
timestamp: 2026-06-03T00:06:43Z
check: hourly-health
---

## Podcast Wiki Snapshot

### MCP Stats
- **Total episodes:** 1,824
  - 20VC: 1,463
  - Lenny: 351
  - Newsletters: 10
- **Total guests:** 1,808
- **Total topics:** 180

### FAISS / Semantic Index
- **Total vectors:** 14,191
- **Total chunks:** 14,191
- **FAISS file:** /workspace/.hermes/podcast-wiki/data/faiss_index.bin (20 MB)
- **FAISS v2 dir:** /workspace/.hermes/podcast-wiki/data/faiss_v2/ (71 MB)
- **Status:** Healthy (via MCP podcast_wiki_semantic_stats)

### Disk
- **Free space:** ~37 GB (50% used on overlay)
- **Threshold:** 1 GB — OK

### Distill Status
- **Last distill:** 2026-06-01T19:44:55 UTC (~28h ago)
- **Threshold:** within 24h — **FAILED** (>24h since last run)

### Snapshot Script
- **Expected:** ~/.hermes/podcast-wiki/scripts/wiki_snapshot.sh
- **Actual path:** /workspace/.hermes/podcast-wiki/scripts/
- **Script exists:** No — **FAILED** (script missing, manually assembled)

### Health Checks
| Check | Status |
|-------|--------|
| 1. FAISS index (>10K chunks) | ✅ 14,191 vectors |
| 2. MCP server reachable | ✅ Stats + semantic all OK |
| 3. Disk space (>=1GB) | ✅ ~37 GB free |
| 4. Wiki snapshot | ⚠️ Script missing — data assembled manually |
| 5. Recent distill (<24h) | ❌ Last: 2026-06-01T19:44 (~28h ago) |
| 6. Deep guardian (5am only) | ⏭️ Skipped (00:06 UTC) |
