---
title: Continual Learning
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, training, rl, agents, online-learning, adaptation]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
confidence: high
---

# Continual Learning

The ability to learn from **extremely sparse rewards** in real-world interactions — the next frontier beyond RL environments. A model that can do something once and learn from the outcome, similar to how humans learn ("burn your hand on the stove once, you know it's hot").

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Why It's Hard

1. **Data access** — you need to understand how the model is being used in production, the downstream consequences of its actions
2. **No replayable environments** — production is dynamic, unlike offline RLVR training where you can roll out a sample thousands of times
3. **Sparse feedback** — most actions don't produce immediate, clean reward signals

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Emerging Approaches

### Cursor's Composer Model
- Training on their own coding data on top of open-source models
- Captured telemetry from production use
- Implicit rewards: "did the user accept this code suggestion or reject it?"
- **Hours per step**, each step has a massive batch of samples to denoise the gradient

### Applied Compute's Context Base
- Use agents to expend compute offline
- Analyze documents and past traces of human-agent interactions
- Extract learnings to improve downstream performance
- Saw massive improvements at different reasoning efforts while using the same tokens

## Three Innovation Layers

1. **Weight updates** — training methodology improvements
2. **Context** — better data access and understanding
3. **Harness** — improvements in how models are deployed and monitored

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Related Concepts

- [[rlvr]]
- [[post-training]]
- [[test-time-compute]]
- [[reasoning-models]]
- [[enterprise-ai]]
- [[model-training]]
