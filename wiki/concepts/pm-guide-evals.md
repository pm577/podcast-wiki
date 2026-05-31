---
title: PM Guide to Evals for AI Products
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [concept, ai-product, evals, llm, product-management, testing]
sources:
  - beyond-vibe-checks-a-pms-complete-guide-to-evals
confidence: high
---

# PM Guide to Evals for AI Products

## Synthesis

1. **Evals are the hidden lever behind every exceptional AI product.** Aman Khan (Arize AI, former Spotify/Cruise/Apple) argues that PMs obsess over prompts and models but neglect evals — the structured way to measure AI system quality. Evals quietly decide whether an AI product thrives or dies, and writing great evals is rapidly becoming the defining skill for AI PMs in 2025 and beyond.

2. **Evals are like driving tests, not unit tests.** Traditional software testing is deterministic (pass/fail, like checking if a train stays on tracks). AI eval is non-deterministic (like driving through a busy city — conditions vary, behavior must adapt). Evals test awareness (can it interpret signals?), decision-making (does it make correct choices?), and safety (can it stay on track?).

3. **Three types of evals each have tradeoffs.**
   - **Human evals** (thumbs-up/down, expert labeling): directly tied to user experience but sparse, noisy, and costly.
   - **Code-based evals** (API checks, code validity): cheap and fast but weak for subjective/open-ended tasks.
   - **LLM-based evals** (LLM-as-judge): scalable, natural language-based, and PM-friendly to write. Requires validation against human labels but can generate classification labels automatically.

4. **The four-part eval formula.** Every great eval prompt has: (1) Setting the role — priming the judge LLM; (2) Providing the context — the data to grade; (3) Providing the goal — what "good" looks like; (4) Defining terminology and labels — grounding what specific terms mean in your context.

5. **The iterative eval workflow has four phases.**
   - **Phase 1 (Collection):** Gather real user interactions, document edge cases, build a representative dataset of 10-100 human-labeled examples.
   - **Phase 2 (First-pass evaluation):** Write initial eval prompts, run against dataset, aim for 90%+ accuracy vs. human labels, identify failure patterns.
   - **Phase 3 (Iteration loop):** Refine eval prompts with few-shot examples, expand dataset, use evals to test model or prompt changes.
   - **Phase 4 (Production monitoring):** Run evals continuously on live interactions, compare eval results to actual user outcomes, build dashboards for stakeholders.

6. **Common mistakes:** Making evals too complex too quickly (creates noisy signals), not testing edge cases (use few-shot prompting with good/bad examples), and forgetting to validate against real user feedback.

## Key Disagreements

- **LLM-as-judge reliability:** Whether LLM-based evals are reliable enough for production or need human-in-the-loop validation.
- **Evals vs. vibe checks:** Whether structured evals are always better than hands-on manual testing for early-stage products.

## Related Concepts

- [[ai-product]], [[llm]], [[prompt-engineering]], [[ai-glossary]], [[testing]], [[ai-agents]], [[product-management]]
