---
title: AI Agents
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [concept, ai, agents]
sources:
  - lenny-2026-01-01-jason-m-lemkin
  - lenny-2025-09-08-scott-wu
  - lenny-2026-01-12-alexander-embiricos
  - lenny-2025-10-09-jason-droege
  - lenny-2025-09-14-ethan-smith
confidence: high
---

# AI Agents

## Synthesis

1. **AI agents can replace entire functional teams when scoped correctly.** Jason Lemkin (SaaStr) replaced his sales team with 20 AI agents and documented the results. The key insight: agents work best when they handle structured, repetitive workflows with clear success criteria (lead qualification, follow-up sequences). Creative or highly relational work still needs humans.

2. **"Infinite AI interns" change engineering economics.** Scott Wu (Cognition CEO) describes Devin as an AI engineer that never sleeps. The key insight is that AI agents shift engineering from a constraint (people-hours) to a coordination problem — the bottleneck becomes how well humans can specify and review agent work, not how fast agents can generate it.

3. **Agent architectures are evolving from single-prompt to multi-step reasoning.** Alexander Embiricos's approach to Codex involves planning work, parallelizing subtasks, and chaining agent calls. Modern agents don't just respond — they plan, execute, verify, and iterate.

4. **Guardrails are essential but failing in practice.** Sander Schulhoff (HackAPrompt CEO) demonstrates that securing AI agents is harder than expected. Agentic systems introduce new attack surfaces: prompt injection in tool calls, data exfiltration through agent actions, and unintended behavior chains across multiple steps.

5. **The shift from chat to agents is the biggest platform change in 2025-2026.** Jason Droege (Scale AI) observes that frontier labs are building agentic systems that call APIs, run code, and manage workflows autonomously. The winners will be companies that figure out reliability, evaluation, and human-in-the-loop patterns for agentic workflows.

## Key Disagreements

- **Level of autonomy:** Some guests advocate fully autonomous agents (Lemkin's sales team); others insist on human-in-the-loop for any consequential action.
- **Build vs. buy for agent frameworks:** Some recommend building custom agent frameworks; others point to standardized frameworks like LangChain as sufficient.

## Related Concepts

- [[llm]], [[ai-ml]], [[evals]], [[prompt-engineering]], [[saas]], [[automation]]
