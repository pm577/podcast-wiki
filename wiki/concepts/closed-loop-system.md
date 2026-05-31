---
title: Closed-Loop System (AI Organizations)
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [concept, ai, control-systems, organization, agents, feedback]
sources:
  - raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md
confidence: high
---

# Closed-Loop System (AI Organizations)

In control systems theory, a closed-loop system uses feedback to correct error. Diana Hu argues AI enables companies to transform from open-loop (lossy, error-accumulating) to closed-loop (tight feedback, self-correcting).

## Open-Loop Company
- Information lives in people's heads
- Side conversations, DMs, unwritten notes
- Decisions based on "vibes"
- Error accumulates → goes off the rails

## Closed-Loop Company
- Agent reads every artifact (code, chat, meetings)
- Tight feedback loop into decision-making
- Self-healing: agent flags issues, suggests fixes
- Error stays within check (like PID controllers in robotics)

^[raw/transcripts/stanford-ai-frontier/garry-tan-diana-hu-yc-stanford-ai-frontier.md]

## Implementation

1. Connect agent to all data sources (GitHub, Discord, meeting recordings)
2. Record everything into Gbrain / memory context
3. Agent surfaces action items, bug fixes, next best steps
4. Human DRI makes final call with full context

## Related Concepts

- [[ai-native-org]]
- [[agentic-company]]
- [[gstack]]
- [[gbrain]]
- [[taste]]
