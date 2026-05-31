---
title: Post-Training
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, training, alignment, fine-tuning]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
confidence: high
---

# Post-Training

The process of taking a pre-trained base model (which only does next-token prediction) and aligning it for useful interaction. Includes SFT, RLHF, RLVR, and preference tuning.

## Why It's Needed

Base models hallucinate, don't answer questions properly, and may produce unaligned or unsafe outputs. Post-training teaches them:
- Chat format (user/assistant interaction)
- Safety guidelines
- What good and bad outputs look like

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Key Methods

- **SFT (Supervised Fine-Tuning)** — training on curated examples
- **RLHF** — reinforcement learning from human preferences
- **RLVR** — reinforcement learning with verifiable rewards (the most data-efficient today)

## Cost Comparison

Pre-training takes orders of magnitude more compute than post-training. DeepSeek V3 pre-training: ~2.5M H800 hours. DeepSeek R1 post-training (RL): ~150K H800 hours.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Scaling Post-Training

Post-training scaling laws are emerging — labs now run data-center-wide RL runs with massive batch sizes. The compute spent on RL is increasing as a percentage of total training budget.

## Related Concepts

- [[pre-training]]
- [[rlvr]]
- [[rlhf]]
- [[reasoning-models]]
- [[continual-learning]]
- [[model-training]]
