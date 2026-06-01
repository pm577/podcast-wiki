---

title: Hamel Husain & Shreya Shankar
created: 2026-05-31
updated: 2026-06-01
type: entity
tags: [person, ai, evals, product, ml, training, education]
sources:
  - raw/transcripts/lenny/hamel-husain-shreya-shankar.md
  - raw/transcripts/lenny/hamelshreya.md
  - raw/transcripts/lenny/lenny-2025-09-25-hamel-husain-shreya-shankar.md
confidence: high
subtype: person
---

# Hamel Husain & Shreya Shankar

Hamel Husain and Shreya Shankar teach the world's most popular course on AI evals, training over 2,000 PMs and engineers across 500 companies — including large swaths of OpenAI and Anthropic teams. They've been instrumental in shifting evals from an obscure, mysterious subject to one of the most essential skills for AI product builders.

## Key Views

### Evals Are Data Analytics for LLM Applications

Hamel demystifies evals: "Evals is a way to systematically measure and improve an AI application, and it really doesn't have to be scary or unapproachable at all. It really is, at its core, data analytics on your LLM application." The process involves systematically looking at data, creating metrics, and iterating — the same skills PMs already have, applied to AI.^[raw/transcripts/lenny/hamel-husain-shreya-shankar.md]

### The Goal Is Actionable Improvement, Not Perfection

Shreya's key insight: "The goal is not to do evals perfectly, it's to actionably improve your product." Many teams over-engineer eval systems, creating complex frameworks that produce precise measurements but don't drive better decisions. Start simple — measure what matters, improve, iterate. Perfect evals are the enemy of good evals.^[raw/transcripts/lenny/hamel-husain-shreya-shankar.md]

### The Benevolent Dictator Approach

Hamel recommends appointing one person whose taste you trust as the "benevolent dictator" of evals — typically the PM with domain expertise. Committees bog down the process. One person with strong judgment can make quick, good decisions. "You don't want to make this process so expensive that you can't do it." Speed and iteration beat perfect consensus.^[raw/transcripts/lenny/hamel-husain-shreya-shankar.md]

### AI Can't Eval Itself (Yet)

The #1 misconception: "We live in the age of AI. Can't the AI just eval it? But it doesn't work." Hamel explains that LLM-as-judge approaches have significant limitations — they lack domain expertise, can be biased, and miss subtle errors that a domain expert would catch. Human judgment remains essential, especially for nuanced product decisions. The best approach combines AI-assisted analysis with human expertise.^[raw/transcripts/lenny/hamel-husain-shreya-shankar.md]

### Learn by Doing, Once

Hamel and Shreya emphasize that the eval process is a skill that, once learned, compounds. "What's cool about this is you don't need to do this many, many times. For most products, you do this process once and then you build on it." The first eval is the hardest — it requires developing the muscle of looking at LLM outputs critically and systematically. After that, it becomes an integral part of the development process.^[raw/transcripts/lenny/hamel-husain-shreya-shankar.md]

## Notable Quotes

> "This process is a lot of fun. Everyone that does this immediately gets addicted to it." — Hamel Husain

> "People have been burned by evals in the past. People have done evals badly, so then they didn't trust it anymore, and then they're like, 'Oh, I'm anti evals.'" — Shreya Shankar

> "The top one is, 'We live in the age of AI. Can't the AI just eval it?' But it doesn't work." — Hamel Husain


### 1. Start With Data Analysis, Not Tests — The #1 trap Hamel and Shreya see teams fall into: jumping straight to writing eval tests without understanding what needs measuring. With LLMs' stochastic nature, you must ground your eval strategy in actual usage data first — look at real user interactions, identify failure patterns, categorize the types of errors. Only then should you build targeted tests. 'It's a little different than software engineering where you have a lot more expectations of how the system is going to work. With LLMs, it's a lot more surface area.' ^[raw/transcripts/lenny/lenny-2025-09-25-hamel-husain-shreya-shankar.md]

### 2. Vibe Checks Are Fine Initially — But They Don't Scale — Hamel explicitly acknowledges that vibe checks (manually reviewing a handful of outputs) are a legitimate starting point for eval. 'Vibe checks are good and you should do vibe checks initially.' The problem is they become unmanageable fast as the application grows. The transition from vibe checks to systematic evals should happen when you can no longer hold all the failure modes in your head — well before you're experiencing customer-impacting regressions. ^[raw/transcripts/lenny/lenny-2025-09-25-hamel-husain-shreya-shankar.md]

### 3. Evals Span a Spectrum: From Unit Tests to Metric Tracking to Cohort Discovery — Shreya's broader definition: evals are not just tests. They range from simple 'non-negotiable functionality' unit tests to ongoing engagement metrics (thumbs up/down, retention) to cohort discovery (finding new user segments you didn't know existed). Each serves a different purpose, and mature teams use all three layers. The unit test metaphor only captures a small part of the puzzle — the real value is in the ongoing, data-driven improvement loop that evals enable across the entire product lifecycle. ^[raw/transcripts/lenny/lenny-2025-09-25-hamel-husain-shreya-shankar.md]

## Episode Appearances

- [[hamel-husain-shreya-shankar]] — *Why AI evals are the hottest new skill for product builders*
- [[hamelshreya]]
- [[lenny/lenny-2025-09-25-hamel-husain-shreya-shankar.md|Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar — date-prefixed summary]]

## Related Concepts

- [[ai-ml]]
- [[product-development]]
- [[data-science]]
- [[eval]]

---

*Merged from [[hamel]]:*

# Hamel

*This page was migrated from the podcast wiki guest index. Expand with key views and frameworks from episode transcripts.*

## Episode Appearances

- [[lenny/hamel-husain-shreya-shankar|Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar]] — *to be summarized*
