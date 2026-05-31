---
title: Synthetic Data Generation
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, data, training, synthetic, rl, post-training]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
confidence: medium
---

# Synthetic Data Generation

The practice of using AI models to generate training data for other AI models. As we've hit the "data wall" on pre-training data, synthetic data has become a key lever for improving model performance.

## Current Approaches

1. **Explode primary sources** — take original documents and generate orders of magnitude more tokens
2. **RL generator-verifier gap** — use the gap between what a model can generate and what can be verified as correct to create training signals
3. **Code as synthetic data** — easy: hold out unit tests, have model attempt, run tests. No humans needed.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Market View

The data market is tough because better models create better synthetic data pipelines, compressing margins. Successful data companies pivot to the next wave: robotics data, egocentric data, etc.

## Related Concepts

- [[pre-training-scaling-laws]]
- [[rlvr]]
- [[post-training]]
- [[model-evals]]
