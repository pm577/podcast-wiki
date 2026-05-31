---
title: Hamel Husain + Shreya Shankar
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: ['person', 'ai-ml', 'evals', 'product-management', 'engineering', 'education']
sources:
  - raw/transcripts/lenny/hamelshreya.md
confidence: medium
key_finding: Evals Are the Highest ROI Activity for AI Product Builders
---

# Hamel Husain + Shreya Shankar

Hamel Husain and Shreya Shankar teach the world's most popular course on AI evals, training over 2,000 PMs and engineers across 500 companies, including large teams at OpenAI, Anthropic, and every other major AI lab. Hamel was previously a staff ML engineer at GitHub. Shreya is a researcher and engineer focused on AI evaluation and reliability.

## Key Views

**Evals Are the Highest ROI Activity in AI Product Building** — To build great AI products, you must be good at evals. It's the single highest-ROI activity. Once you set up a good eval process, you build on it iteratively. Most teams skip evals and ship AI features that are unreliable — then wonder why users don't trust them. Good evals = trustworthy AI. ^[raw/transcripts/lenny/hamelshreya.md]

**Don't Let AI Eval Your AI — It Doesn't Work** — The #1 misconception: "Can't the AI just eval itself?" It doesn't work. LLM-as-judge approaches hallucinate, miss subtle failures, and reinforce the model's blind spots. Human-in-the-loop eval design is essential. The eval is only as good as the human judgment encoded in its design. ^[raw/transcripts/lenny/hamelshreya.md]

**The Benevolent Dictator Approach** — When building evals, don't form a committee. Appoint one person with domain expertise and trusted taste as the "benevolent dictator" who defines what good looks like. In most cases, this is the product manager. Committees produce lowest-common-denominator evals. One good curator produces evals that actually catch meaningful failures. ^[raw/transcripts/lenny/hamelshreya.md]

**Start with One Eval, Not a Suite** — Teams over-engineer eval infrastructure before they've validated that their eval process works. Start with one high-quality eval for the most critical user journey. Run it manually. Understand what it catches and misses. Then add structure and automation. The goal is not perfection — it's actionable improvement. ^[raw/transcripts/lenny/hamelshreya.md]

**Build Evals by Analyzing Real Failures** — The best evals come from analyzing real user failures, not from theoretical taxonomies. When a user reports a bad AI output, trace it back, understand what went wrong, and build an eval that would have caught it. This creates evals that map directly to user experience rather than abstract quality metrics. ^[raw/transcripts/lenny/hamelshreya.md]

## Episode Appearances

- [[lenny/hamelshreya|Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar]] — The definitive guide to building AI evals

## Related Concepts

- [[ai-ml]]
- [[evals]]
- [[product-management]]
- [[ai-engineering]]
- [[testing]]
