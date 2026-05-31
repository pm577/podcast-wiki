---
title: Gstack
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, open-source, coding, agents, software-factory, garry-tan]
sources:
  - raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md
confidence: high
---

# Gstack

Open-source AI software factory created by Garry Tan (CEO, Y Combinator). 87K+ GitHub stars. A framework for building with coding agents that extracts specific personas from the latent space of LLMs and packages them as skills.

## Key Concepts

- **Skills** — runbooks that can call code. Distill specific capabilities from latent space (e.g., Office Hours, Plan-Eng-Review)
- **Resolvers** — load skill instructions only when needed, keeping context small
- **Skillify** — go up one level: write → test → eval → integrate → ship
- **Deterministic + Latent** — code for deterministic work, markdown/LM for latent work, wired together

## Origin Story

Garry saw Steve Yegge's post about 10-100x productivity gains from coding agents. Opened Claude Code, wrote ~1M lines of code. Realized the latent space contains specific personas worth extracting as reusable skills. Gstack was the result of packaging these discoveries.

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

## Related Concepts

- [[gbrain]]
- [[skillify]]
- [[resolvers]]
- [[software-factory]]
- [[agentic-company]]
- [[garry-tan]]
