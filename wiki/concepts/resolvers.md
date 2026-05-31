---
title: Resolvers
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, agents, gstack, context, skills]
sources:
  - raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md
confidence: medium
---

# Resolvers

A mechanism to keep agent context small by loading skill instructions only when needed, rather than keeping everything in the system prompt. When Claude.md hits 40K tokens, resolvers fix it.

## How It Works

Instead of "always write the changelog this way" (in Claude.md), the resolver says: "Anytime you need to write to the changelog, load changelog.md." The instruction is loaded only when the relevant task comes up.

## Why It Matters

This is the core of a great agent — not having everything in context all the time, but knowing where to find the right instruction when needed. Maps to org chart in a company: who handles what?

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

## Related Concepts

- [[gstack]]
- [[skillify]]
- [[agentic-company]]
- [[software-factory]]
