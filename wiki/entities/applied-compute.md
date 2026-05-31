---
title: Applied Compute
created: 2026-06-01
updated: 2026-06-01
type: entity
tags: [company, ai-ml, enterprise, model-training, post-training, rlvr, startup]
sources:
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
confidence: high
---

# Applied Compute

Founded ~May 2025 by Yash Bottla, Rhythm, and Lyndon (all former OpenAI). Helps enterprises create specialized AI models by applying frontier post-training techniques (RLVR) to proprietary enterprise data.

## Core Thesis

General models set the floor, specialization sets the ceiling. Enterprise data is the largest untapped resource — companies have proprietary data built up over time. Applied Compute helps them take frontier technology and create their own specialized models.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Key Customers

- **DoorDash** — menu extraction and style guide compliance for 100K+ merchants/year
- **Cognition/Windsurf** — sub-2-second bug-catching model: small model, heavily post-trained, achieves performance of larger models at lower cost and latency

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Approach

1. Collect model outputs on enterprise-specific tasks
2. Humans correct outputs, creating ground truth
3. Calculate delta between model and ground truth
4. Train against error rate directly — optimize toward the outcomes the enterprise wants
5. Define "what good and bad looks like" for each enterprise

## Related Concepts

- [[rlvr]]
- [[post-training]]
- [[enterprise-ai]]
- [[model-training]]
- [[yash]]
- [[continual-learning]]
