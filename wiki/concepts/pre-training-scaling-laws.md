---
title: Pre-Training Scaling Laws
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, scaling, training, compute, data, kaplan, chinchilla]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
  - raw/transcripts/lenny/applied-compute-yash.md
confidence: high
---

# Pre-Training Scaling Laws

Empirical laws showing that model performance improves predictably with more compute, more data, and larger parameters.

## Kaplan Scaling Laws (OpenAI)

Showed: make models bigger → get much better performance. Proved with GPT-3, the first model that seemed to have some level of general intelligence.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Chinchilla Scaling Laws (DeepMind)

Correction: not just bigger models — there's a **compute-optimal** way to scale. Scale parameter size AND train on proportionally more data.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## The Data Wall

We've run out of accessible internet data. Responses:
1. **Synthetic generation** — explode primary sources into more tokens
2. **New architectures** — better use of existing data
3. **RL environments** — exchange compute for less high-quality data
4. **Real-world data** — libraries, books, egocentric data

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Related Concepts

- [[pre-training]]
- [[post-training]]
- [[test-time-compute]]
- [[synthetic-data]]
- [[continual-learning]]
