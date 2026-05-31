---
title: AI Evals
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [concept, ai, evals]
sources:
  - lenny-2025-09-18-brendan-foody
  - lenny-2025-09-25-hamel-husain-shreya-shankar
  - lenny-2025-12-07-edwin-chen
  - beyond-vibe-checks-a-pms-complete-guide-to-evals
confidence: high
---

# AI Evals

## Synthesis

1. **AI evals are the fastest-growing skill for product builders.** Hamel Husain and Shreya Shankar, creators of the #1 eval course, argue that systematic evaluation is the critical bottleneck for AI product quality. Without evals, teams rely on "vibe checks" — subjective impressions that don't catch regressions or scale.

2. **Expert-written evals create a competitive moat.** Brendan Foody (Mercor CEO) argues that companies investing in expert-written evaluations — using domain specialists to assess model outputs — are creating the fastest-growing companies. Expert evals provide a quality signal that automated metrics cannot match, especially for nuanced tasks like code generation, writing, and reasoning.

3. **Eval-driven development changes the iteration cycle.** The "Beyond vibe checks" framework from Lenny's Newsletter shows how PMs can build eval suites that measure accuracy, helpfulness, safety, and style. Teams that integrate evals into their CI/CD pipeline iterate faster and ship with higher confidence.

4. **Human preference data is the foundation of alignment.** Edwin Chen (Surge AI) explains that companies like Anthropic and Google rely on human evaluators to train aligned models. The quality, consistency, and scale of human preference data determines how well models align with user expectations.

5. **Evaluation types are proliferating.** The podcast corpus reveals several distinct eval categories: factual accuracy (grounded in sources), behavioral evals (safety, bias), output quality (fluency, coherence), task completion (did the agent achieve the goal?), and adversarial evals (security testing). Most mature AI products use a combination.

## Key Disagreements

- **Automated vs. human evals:** Some argue that LLM-as-judge (using a model to eval another model) is sufficient for most cases; others maintain that expert human evaluation is irreplaceable for high-stakes applications.
- **When to invest in evals:** Early-stage teams debate whether to build evals from day one or wait until they have user traction. The consensus leans toward "start simple with 5-10 eval cases on day one, expand systematically."

## Related Concepts

- [[ai-ml]], [[llm]], [[agents]], [[prompt-engineering]], [[metrics]], [[quality]]
