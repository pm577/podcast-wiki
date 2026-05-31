---
title: Yash (Applied Compute)
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: [person, ai-ml, enterprise, model-training, rlvr, startups]
sources:
  - raw/transcripts/lenny/applied-compute-yash.md
confidence: high
---

# Yash (Applied Compute)

Co-founder of Applied Compute, previously at OpenAI where he led agentic coding research (Codex). Founded the Long Horizon Tasks team at OpenAI. His work focuses on post-training RL for enterprise AI specialization.

## Key Views

### 1. The Bottleneck Has Shifted from Compute to RL Environments to Continual Learning

Yash traces the evolution of bottlenecks in AI: first it was having enough compute, then the right architecture (transformers), then pre-training data scale, then preference tuning (RLHF). Today the bottleneck is RL environments — constructing worlds where models can explore and learn from verifiable rewards. The next frontier is **continual learning**: being extremely data efficient with real-world interactions. "Like burning your hand on a stove — you only need to do it once. Models today are not like that."

^[raw/transcripts/lenny/applied-compute-yash.md]

### 2. RL Training Is Surprisingly Compute-Efficient vs Pre-Training

DeepSeek V3 required ~2.5M H800 hours of pre-training compute. DeepSeek R1 (the RL training that gave it reasoning) required only ~150K H800 hours — about **5%** of the pre-training compute. However, this ratio is shifting as labs run data-center-wide RL runs with massive batch sizes to exploit post-training scaling laws.

^[raw/transcripts/lenny/applied-compute-yash.md]

### 3. Enterprise Specialization Is Where Value Accrues

"General models set the floor, specialization sets the ceiling." At Applied Compute, Yash helps companies like DoorDash and Cognition/Windsurf create specialized models trained on proprietary data. DoorDash example: 100K+ merchants/year with unstructured menu data — general models couldn't handle their specific style guide. Solution: train against ground truth, optimize directly on error rate.

^[raw/transcripts/lenny/applied-compute-yash.md]

### 4. Code Is the Ideal RL Domain Because of Verifiable Rewards

Code and math are uniquely suited for RL training because you can deterministically verify correctness — compile code, run unit tests. This is why all frontier labs focused on software engineering first. Yash believes coding models may be "AGI-complete" — every task, when broken down, is a coding task.

^[raw/transcripts/lenny/applied-compute-yash.md]

### 5. The Hardware Bet: Nvidia Wins but In-Housing Is Coming

Nvidia takes ~75% margin on their chips. The question is whether labs will eventually invest in their own chip design — even chips that are 80% as effective, at 2x quantity, win on volume. Yash is long Nvidia but sees this risk.

^[raw/transcripts/lenny/applied-compute-yash.md]

## Related Concepts

- [[rlvr]]
- [[continual-learning]]
- [[enterprise-ai]]
- [[model-training]]
- [[pre-training]]
- [[post-training]]
