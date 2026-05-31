---
title: Scott Wu
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: [person, ai, software-engineering, agentic-coding, startup, devin, cognition]
sources:
  - raw/transcripts/lenny/lenny-2025-09-08-scott-wu.md
confidence: high
---

# Scott Wu

**Role:** Co-founder and CEO of Cognition (makers of Devin)  
**Known for:** Building Devin, the world's first autonomous AI software engineer; leading a team of 15 engineers who each work with up to 5 Devin instances to build Devin itself.

## Key Views

### 1. Engineers as architects, not coders — the role shifts upward

Scott's central thesis: AI will produce **more** programmers, not fewer, because programming is fundamentally about telling computers what to do — and as AI gets more powerful, the ability to specify intent becomes *more* important, not less. He sees the engineer's role evolving from writing every line of code to architecting systems and directing agents. Devin is designed to work as an asynchronous junior engineer: tag it in Slack or Linear, it scopes the task, asks clarifying questions, writes code, runs tests, and submits PRs. Cognition's own team of 15 engineers has ~25% of PRs authored by Devin today and expects over 50% by year-end.

> "There's going to be way more programmers and way more engineers a few years from now. Programming is only going to become more and more important as AI gets more powerful." — Scott Wu

### 2. Treat Devin like a new junior engineer, not a magic tool

Scott's #1 piece of advice for users: **treat Devin like your new junior engineer.** Start with well-defined tasks (not open-ended problems), invest upfront in setup (repo access, CI config, lint rules), and gradually scale the complexity of assignments as Devin builds context. The stickiness comes from Devin learning the codebase over time — building representations of the architecture, understanding deployment workflows, and getting familiar with team conventions. A Devin that's been with a team for months is dramatically more effective than one that just joined.

> "You want to be giving Devin tasks, not problems. Start with the easier ones, understand what things Devin needs to get set up to test its own code, then scale up over time." — Scott Wu

### 3. Jagged intelligence — Devin excels at codebase understanding

Devin exhibits what Scott calls "jagged intelligence": it's staff-level at understanding existing codebases (reading all the files, tracing architecture, answering questions about how things work) but junior-level at other tasks. This makes Devin uniquely valuable for onboarding new engineers — they can ask "dumb questions" without feeling awkward and learn the codebase through Devin's Wiki (an auto-generated, shareable representation of the repository). The Devin Wiki feature also helps PMs and other non-engineers understand the technical landscape.

> "The retrieval and processing a lot of code and a lot of tokens at once is something that language models are really great at. Getting those gains in the places that you need them." — Scott Wu

### 4. Moat = stickiness, not barriers to entry

Scott reframes the common AI moat question: since no hard barriers exist in the AI layer, the real defensibility is **stickiness** — the degree to which Devin becomes more valuable the more you use it. Devin learns your specific codebase, your team's processes, your CI pipeline idiosyncrasies. It integrates into your entire workflow (Slack, Linear, GitHub). The multiplayer aspect creates further stickiness: engineers teach Devin things in Slack threads, Devin helps onboard new hires, and the collective knowledge compounds. His view: stay focused on making the product more useful with every interaction, rather than trying to lock competitors out.

> "There is a lot of just inherent stickiness and learning and buildup over time. It's the same thing with an engineer. If you're joining on day one versus you've been at the company for five years, you wrote half the code yourself." — Scott Wu

### 5. Base intelligence is largely solved — the hard part is real-world idiosyncrasy

Scott's surprising take: the base model intelligence is "basically already there" for autonomous coding. The hard work isn't squeezing more IQ out of models — it's teaching the agent all the **idiosyncrasies of real-world engineering**: how to use Datadog, how to diagnose specific errors, how to handle different CI systems, how to make a proper GitHub PR. Devin's value comes from mirroring the messy complexity of actual software development, not from fundamentally better reasoning. The foundation labs handle the reasoning; Cognition handles the applied engineering knowledge.

> "A lot of what we spend our time on is less about increasing the base IQ of a model and more about teaching it all of the idiosyncrasies of real-world engineering." — Scott Wu

## Episode Appearances

- [[lenny-2025-09-08-scott-wu]] — Inside Devin: The AI engineer that's set to write 50% of its company's code this year

## Related Concepts

- [[ai-engineering]]
- [[agentic-coding]]
- [[software-engineering]]
- [[ai-native-startups]]
- [[devtools]]
