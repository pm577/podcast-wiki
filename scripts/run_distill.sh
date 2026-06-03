#!/bin/bash
set -e

# Export API key from .env
API_KEY=$(grep '^DEEPSEEK_API_KEY=' ~/.hermes/.env | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")
export DEEPSEEK_API_KEY="$API_KEY"

cd ~/.hermes/podcast-wiki
exec uv run python scripts/distill.py "$@"
