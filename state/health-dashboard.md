# Podcast Wiki Health Dashboard

**Last checked:** 2026-06-03T00:06 UTC

## Status: ⚠️ 2 FAILURES

### 1. FAISS Index
- **File:** /workspace/.hermes/podcast-wiki/data/faiss_index.bin (20 MB)
- **Vectors:** 14,191 (via MCP semantic_stats)
- **Result:** ✅ HEALTHY

### 2. MCP Server
- **Total episodes:** 1,824 (20VC: 1,463, Lenny: 351, Newsletters: 10)
- **Total guests:** 1,808
- **Total topics:** 180
- **Result:** ✅ HEALTHY (get_podcast_stats + semantic_stats OK)

### 3. Disk Space
- **Filesystem:** overlay
- **Available:** ~37 GB of 75 GB (50% used)
- **Threshold:** >1 GB
- **Result:** ✅ HEALTHY

### 4. Snapshot Script
- **Expected:** ~/.hermes/podcast-wiki/scripts/wiki_snapshot.sh
- **Found:** Script does not exist at any path
- **Result:** ❌ FAILED — script missing

### 5. Distill Freshness
- **Last distill:** 2026-06-01T19:44:55 UTC
- **Current:** 2026-06-03T00:06:43 UTC
- **Elapsed:** ~28 hours
- **Threshold:** <24 hours
- **Result:** ❌ FAILED — distill hasn't run in 28+ hours

### 6. Deep Guardian
- **Result:** ⏭️ Skipped (not 5am UTC)

### Alert Summary
- **Failing checks:** 2 (snapshot script missing, distill stale)
