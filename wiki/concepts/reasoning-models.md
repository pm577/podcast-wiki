---
title: Reasoning Models
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, reasoning, chain-of-thought, rl, o1, r1]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
  - raw/transcripts/lenny/applied-compute-yash.md
confidence: high
---

# Reasoning Models

A new class of LLMs that use chain-of-thought reasoning at inference time, enabled by RLVR training. Started with OpenAI's o1 in 2024, followed by DeepSeek R1, Claude (thinking mode), and others.

## Key Insight

Chain-of-thought is **completely emergent** — not explicitly programmed. RLVR training in constrained environments with sufficient compute produces models that spontaneously learn to reason, self-correct, and spend time thinking before answering.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Impact

Moved from:
- **2023**: Instruction-tuned chat models (GPT-4)
- **2024**: Reasoning models (o1, R1)
- **2025+**: Reasoning + tool use → agents → AI co-workers

## Related Concepts

- [[rlvr]]
- [[test-time-compute]]
- [[post-training]]
- [[continual-learning]]
- [[model-evals]]
