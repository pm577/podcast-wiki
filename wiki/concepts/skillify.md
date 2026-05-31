---
title: Skillify
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, agents, gstack, skills, workflow]
sources:
  - raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md
confidence: high
---

# Skillify

A process for taking a one-off agentic task and packaging it into a reusable skill with tests, evals, resolver triggers, and schema. Garry Tan discovered this pattern while using Open Claw and Hermes Agent.

## The 10-Step Pipeline

1. Write the skill (markdown runbook)
2. Write the code it calls
3. Write **unit tests** for the code
4. Write **LLM evals** for the skill file
5. Write **integration test**
6. Ensure **resolver trigger** in agents.md
7. Test trigger — LLM as judge eval (broad enough scope?)
8. **Check resolvable** — avoid duplicates, DRY
9. **End-to-end smoke test**
10. Define **schema** — where it lives in memory/repo

Only steps 1-2 are "writing." The rest is making the system reliable — analogous to compliance in a finance organization.

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

## Related Concepts

- [[gstack]]
- [[resolvers]]
- [[agentic-company]]
- [[software-factory]]
- [[gbrain]]
