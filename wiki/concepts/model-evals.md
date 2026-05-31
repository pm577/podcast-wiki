---
title: Model Evals (Evaluations)
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, evaluation, benchmarking, training, RL, evals]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
confidence: high
---

# Model Evals (Evaluations)

Benchmarks that define what good and bad look like for a model. With RL training, evals become the most important asset — they **set the road map** for model improvement.

## Why Labs Guard Their Evals

1. Evals define the **hill to climb** — whatever you optimize towards
2. RL is an **eval-maxing machine** — create a training pipeline that mirrors the eval structure
3. SWE-bench started the code model race; new evals have emerged since

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Enterprise Evals

Different from lab evals — each enterprise has its own definition of good and bad:
- JPMorgan and Goldman Sachs have different standards
- Applied Compute helps enterprises define their own evals and optimize toward them

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## The Eval Layer Cake

1. Frontier lab evals (general capabilities)
2. Enterprise evals (specific business outcomes)
3. Specialization layer (Applied Compute) bridges both

## Related Concepts

- [[rlvr]]
- [[post-training]]
- [[reasoning-models]]
- [[pre-training]]
- [[enterprise-ai]]
- [[synthetic-data]]
