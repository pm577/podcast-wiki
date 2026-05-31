#!/bin/bash
# Fast MCP wrapper for podcast-wiki
# Warms up the model before Hermes connects
# So the connection test doesn't time out

# Test: just serve the schema fast
if [ "$1" = "--schema" ]; then
    exec /home/philip/.yt-env/bin/python3 /home/philip/.hermes/podcast-wiki/scripts/podcast_mcp_server.py --schema
fi

# Pre-warm the model (takes ~2s when cached, ~10s on cold start)
/home/philip/.yt-env/bin/python3 -c "
from sentence_transformers import SentenceTransformer
try:
    m = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    m.encode(['warm'], normalize_embeddings=True)
except Exception:
    pass
" 2>/dev/null

# Now launch the real MCP server
exec /home/philip/.yt-env/bin/python3 /home/philip/.hermes/podcast-wiki/scripts/podcast_mcp_server.py
