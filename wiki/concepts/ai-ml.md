---
title: AI/ML
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [concept, ai, machine-learning]
sources:
  - raw/transcripts/lenny/lenny-2026-05-24-dan-shipper.md
  - lenny-2025-10-23-chip-huyen
  - lenny-2025-10-09-jason-droege
  - lenny-2025-09-18-brendan-foody
  - lenny-2026-01-11-aishwarya-naresh-reganti-kiriti-badam
confidence: high
---

# AI/ML

## Synthesis

1. **Feedback loops are the critical missing piece in AI products.** Aishwarya Naresh Reganti and Kiriti Badam (AWS, Google, Amazon) emphasize that most AI products fail because teams don't build actionable feedback loops. Without a system to capture what users actually do with model outputs — thumbs up/down, edits, corrections, or abandonment — teams cannot systematically improve quality or catch regressions. They recommend starting with a simple feedback mechanism on day one, even if it's just a binary satisfaction signal.

2. **Enterprise AI requires solving data quality at scale.** Jason Droege (Scale AI CEO) notes that frontier labs and enterprises invest heavily in high-quality training/evaluation data. The $14B Meta deal underscores that data infrastructure — labeling, curation, and evals — is the bottleneck for AI adoption, not model architecture. Companies that treat data as a first-class engineering concern, rather than an afterthought, consistently outperform those that don't.

3. **AI engineering is distinct from traditional software engineering.** Chip Huyen (Nvidia, Stanford, Netflix) argues that AI product work requires different tradeoffs: outputs are probabilistic rather than deterministic, quality is multidimensional (accuracy, fluency, safety, style, latency), and monitoring needs to track data drift, concept drift, and output quality simultaneously. Traditional software testing frameworks don't apply — teams need eval-driven development instead.

4. **Evaluations are becoming a competitive moat.** Brendan Foody (Mercor) argues that companies investing in expert-written AI evals create the fastest-growing businesses because evals enable faster iteration cycles and higher quality thresholds than competitors. Expert human evaluators catch subtle quality issues that automated metrics miss, creating a defensibility advantage.

5. **The most successful AI deployments use humans-in-the-loop strategically.** Across multiple episodes, the consensus is that AI replaces tasks, not roles — the best products combine AI automation with human oversight for high-stakes decisions, especially in regulated industries. The key is designing the handoff points: where AI autonomously handles routine cases and where it escalates to humans.

## Key Disagreements

- **Build vs. buy for AI infrastructure:** Scale AI argues for specialized data partners, while others like Chip Huyen advocate for building in-house evaluation pipelines for tighter feedback loops.
- **Agent autonomy:** Some guests advise starting with narrow, supervised AI agents; others like Jason Lemkin have replaced entire sales teams with 20 autonomous AI agents, suggesting full autonomy is viable faster than most expect.
- **Open-source vs. proprietary models:** Debate over whether open-weight models (Llama, Mistral) will catch up to frontier labs or whether proprietary advantages in data and infrastructure will persist.

## Related Concepts

- [[llm]], [[agents]], [[evals]], [[prompt-engineering]], [[saas]], [[enterprise]], [[machine-learning]]
