---
title: Test-Time Compute (Inference Scaling)
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, reasoning, inference, scaling, chain-of-thought]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
confidence: high
---

# Test-Time Compute (Inference Scaling)

A new axis for scaling model intelligence that emerged with OpenAI's o1 in 2024. Instead of only scaling compute during training, models spend additional compute at inference time to reason, think, and correct themselves.

## The Breakthrough

Chain-of-thought at inference time is a **completely emergent behavior** — no one trained models to do it. By putting models in constrained RL environments and funneling compute, they spontaneously developed the ability to reason step-by-step and self-correct.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## The Three Scaling Laws

1. **Pre-training scaling** — more compute, more data, bigger models
2. **Post-training scaling** — more RL compute, better alignment
3. **Test-time scaling** — more inference compute per query, better reasoning

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Combined with Tool Use → AI Co-workers

Reasoning + tool use (Claude Code, Deep Research) → agents that reason and work for long periods of time → AI co-workers.

## Related Concepts

- [[reasoning-models]]
- [[rlvr]]
- [[post-training]]
- [[continual-learning]]
- [[pre-training]]
