---
title: LLM
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [concept, ai, llm]
sources:
  - lenny-2025-10-23-chip-huyen
  - lenny-2025-10-09-jason-droege
  - lenny-2026-01-12-alexander-embiricos
  - lenny-2026-01-11-aishwarya-naresh-reganti-kiriti-badam
  - lenny-2025-12-07-edwin-chen
confidence: high
---

# LLM

## Synthesis

1. **Context engineering matters more than prompt engineering.** Alexander Embiricos argues that how you structure context for an LLM — chunking, retrieval, ordering — has a larger impact on output quality than prompt phrasing. His "power user's guide to Codex" emphasizes planning workflows and structuring context before generating.

2. **LLMs are not databases — treat them as reasoning engines.** Chip Huyen (Nvidia, Stanford, Netflix) stresses that LLMs should be used for synthesis and reasoning, not for factual recall. Building reliable AI products requires grounding LLM outputs in retrieved context rather than relying on parametric knowledge.

3. **Frontier labs are moving toward agentic workflows.** Jason Droege (Scale AI) reveals that frontier labs are building systems where LLMs don't just answer questions but execute multi-step tasks — calling APIs, running code, and iterating on results. The shift from chat to agents is the biggest architectural change in 2025-2026.

4. **Fine-tuning is declining in favor of prompt/context engineering.** Multiple guests note that few teams fine-tune anymore. RAG (retrieval-augmented generation) plus well-structured system prompts achieves comparable results at lower cost, with easier iteration.

5. **Human preference data is the new moat.** Edwin Chen (Surge AI) explains that companies like Anthropic and Google rely on human feedback to train aligned models. The quality and scale of preference data is becoming the key differentiator between commodity models and differentiated AI products.

## Key Disagreements

- **Open-weight vs. closed models:** Some guests argue open-weight models (Llama, Mistral) are catching up fast; others believe frontier capability gaps will persist due to scale advantages.
- **Fine-tuning utility:** While fine-tuning has declined, some niche use cases (code generation, structured outputs) still benefit from specialized fine-tuned models over general-purpose ones.

## Related Concepts

- [[ai-ml]], [[agents]], [[prompt-engineering]], [[evals]], [[saas]], [[chatgpt]]
