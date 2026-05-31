---
title: Garry Tan
created: 2026-05-31
updated: 2026-06-01
type: entity
tags: [person, venture-capital, y-combinator, ai-agents, open-source, gstack, gbrain, founder]
sources:
  - raw/transcripts/20vc/20vc-2016-12-14-20vc-garry-tan-on-the-biggest.md
  - raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md
confidence: high
---

# Garry Tan

CEO of Y Combinator. Stanford class of '03. Founder of Posterous (sold to Twitter for $20M). Created Gstack (87K GitHub stars) and Gbrain (13K stars), two of the most popular open-source AI agent frameworks. Previously product manager at Palantir and Microsoft. Active builder of AI-native tools — discovered skillify, resolvers, and agentic software factory patterns through personal use of Claude Code and Hermes Agent.

## Key Views

### 1. The Software Factory: From Copilot to Autonomous Coding

In December 2025, saw Steve Yegge's post claiming AI coding agents make engineers 10-100x more productive (Cursor), and at Anthropic ~1,000x vs Googlers in 2005. Opened Claude Code and wrote ~1M lines of code. Created Gstack as an open-source software factory. The shift: copilot era → software factory era.

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

### 2. Plan-Eng-Review Is the #1 Skill

Uses it ~20x/day. Key questions: "What's the 10x version? What's the platonic ideal?" Requires 80-90% test coverage to ship production code (not slop). The true metric: does it work? Are customers paying?

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

### 3. Boil the Ocean

In meetings people say "let's not boil the ocean." With coding agents, the answer is actually "let's boil the ocean." One person at a terminal = 500-1,000 people. All expectations are 1,000x wrong. Models themselves haven't caught up — ask "how long?" → "3 weeks" → approve → done in 1 hour.

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

### 4. Skills as Personas from Latent Space

The Office Hours skill distills YC's thousands of partner conversations into a potent prompt. The Plan-Eng-Review pushes for the platonic ideal. Skills are runbooks that can call code — bridging deterministic and latent spaces.

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

### 5. The Skillify Pipeline

10-step process (only 2 are writing): write skill code → write unit tests → LLM evals → integration tests → resolver triggers → check resolvable (DRY) → end-to-end smoke tests → schema → release. Maps to company org: skill = employee, resolver = org chart, check resolvable = audit/compliance, trigger eval = performance review.

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

### 6. Gbrain: Three-Layer Memory System

Started with Karpathy's knowledge wiki, added vector search (ARR fusion), backlinks, graph database as knowledge graph. Upcoming: epistemology system to track hunches vs beliefs vs world knowledge by person and when they manifest. Next: fully dynamic ontology for different users (researchers, journalists, politicians).

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

### 7. LOC Is a Garbage Metric (But Not for the Reasons You Think)

Nothing in coding agents tells them to write more lines — if anything, the reverse is true. The real measure: tests pass, customers use it, they pay. 87K stars on Gstack is evidence the approach works.

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

## Related Concepts

- [[gstack]]
- [[gbrain]]
- [[y-combinator]]
- [[agentic-company]]
- [[safe-agreement]]
- [[skillify]]
- [[resolvers]]
- [[ai-native-org]]
- [[software-factory]]
- [[closed-loop-system]]
