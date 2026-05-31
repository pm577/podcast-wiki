---
title: Reinforcement Learning with Verifiable Rewards (RLVR)
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, rl, training, reasoning, post-training]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
  - raw/transcripts/lenny/applied-compute-yash.md
confidence: high
---

# Reinforcement Learning with Verifiable Rewards (RLVR)

A training paradigm that came to prominence in 2025. Unlike RLHF (which uses human preferences as reward), RLVR uses **deterministically verifiable rewards** — checking if a model's output is correct using objective criteria.

## Why It Works

RLVR is the most data-efficient training method today because:
1. **Verifiable rewards** — you can automatically check correctness (compile code, run unit tests, validate math proofs)
2. **Massive parallelism** — roll out a sample hundreds or thousands of times, get a distribution of rewards
3. **Emergent reasoning** — chain-of-thought emerges spontaneously from RLVR training without being explicitly programmed

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Cost Advantage

DeepSeek R1 (RLVR training): ~150K H800 hours vs DeepSeek V3 (pre-training): ~2.5M H800 hours — RLVR is **~5%** of pre-training compute.

^[raw/transcripts/lenny/applied-compute-yash.md]

## Enterprise Application

Enterprises define their own verifiable rewards — what good and bad looks like for their specific use case. Applied Compute uses this to help companies like DoorDash and Cognition.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Related Concepts

- [[post-training]]
- [[pre-training]]
- [[rlhf]]
- [[reasoning-models]]
- [[test-time-compute]]
- [[model-evals]]
- [[continual-learning]]
