---
title: AI Glossary
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [concept, ai, llm, reference, glossary]
sources:
  - an-ai-glossary
confidence: high
---

# AI Glossary

## Synthesis

1. **This glossary explains 20+ common AI terms in plain language.** Lenny compiled definitions from his own understanding, research, and AI-expert friends. The target audience: anyone who "sort of" knows AI jargon but doesn't really understand it. Key terms covered: Model, LLM, Transformer, Training/Pre-training, Supervised/Unsupervised Learning, Post-training, Fine-tuning, RLHF, Prompt Engineering, RAG, Evals, Inference, MCP, Gen AI, GPT, Token, Agent, Vibe Coding, AGI, Hallucination, Synthetic Data.

2. **Key architectural concepts explained:**
   - **Transformer** (2017 Google discovery) — introduced "attention" mechanism allowing models to process all words simultaneously rather than sequentially, making parallelizable training at scale possible.
   - **Pre-training** — learning general knowledge through next-token prediction on billions of text sequences.
   - **Post-training pipeline** — fine-tuning (specializing for specific tasks), RLHF (aligning with human preferences through reward models).
   - **RAG** — retrieval-augmented generation, giving models open-book access to external data at inference time, reducing hallucinations.

3. **Applied AI concepts decoded:**
   - **Prompt engineering** — crafting inputs to get better outputs; includes both conversational prompts (end-user) and system prompts (developer-baked).
   - **Evals** — structured benchmarks/unit tests for AI outputs; increasingly seen as the most critical AI PM skill.
   - **MCP** (Model Context Protocol) — open standard for AI models to interact with external tools (calendar, CRM, Slack, codebase).
   - **Agent** — AI system that acts proactively, makes its own plan, takes real-world actions, draws on live data, and creates its own feedback loop.
   - **Vibe coding** — building apps by describing what you want in English, often without ever looking at the code.

4. **Frontier concepts:**
   - **AGI** (Artificial General Intelligence) — AI smarter than average humans across most subjects. Some believe we've reached it; AGI to ASI (superintelligence) timeline is debated.
   - **Hallucination** — confident-sounding but factually incorrect outputs. Mitigated by RAG, prompt engineering, and newer model improvements.
   - **Synthetic data** — AI-generated training data used when real data is exhausted or sensitive. Can be indistinguishable from real data to humans.

## Related Concepts

- [[llm]], [[prompt-engineering]], [[ai-agents]], [[evals]], [[ai-infrastructure]], [[code-generation]], [[ai-product]]
