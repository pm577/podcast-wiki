---
title: Kevin Weil
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: [person, openai, ai, product-management, evals, chatgpt, artificial-intelligence, product-strategy, leadership]
sources:
  - raw/transcripts/lenny/kevin-weil.md
confidence: high
---

# Kevin Weil

**Role:** Chief Product Officer at OpenAI, overseeing ChatGPT, enterprise products, and the API; former Head of Product at Instagram and Twitter; co-creator of the Libra cryptocurrency at Facebook; board member at Planet and Strava  
**Known for:** Product leadership at the center of the AI revolution; pioneering the "evals as unit tests" philosophy for AI products; driving iterative deployment and model maximalism at OpenAI.

## Key Views

### 1. The Models You Use Today Are the Worst You'll Ever Use

Kevin's core operating principle: AI models improve so fast that the model you're using today is the worst one you'll ever use for the rest of your life. Every two months, computers can do something they've never been able to do before. This completely changes how you build products — instead of over-engineering around current model limitations, you should **build on the ragged edge of capability** and trust that the next model will make your marginal product sing. OpenAI tells developers: if your product is right on the edge of what the model can do, keep going — you're doing something right.^[raw/transcripts/lenny/kevin-weil.md]

> "The AI models that you're using today is the worst AI model you will ever use for the rest of your life. Every two months, computers can do something they've never been able to do before." — Kevin Weil

### 2. Evals Are the New Unit Tests — A Core Skill for Product Builders

Kevin argues that writing **evals** (tests that measure model performance on specific use cases) is rapidly becoming an essential product skill. Unlike traditional software (where databases give deterministic outputs), LLMs produce fuzzy, non-deterministic results. You need to know whether your model gets a use case right 60%, 95%, or 99.5% of the time — because each threshold demands a completely different product architecture. Evals let you hill-climb toward a working product by continuously testing and fine-tuning. Kevin envisions a future where broad-based models are fine-tuned on company-specific data, and the quality of your evals determines the quality of your AI product.^[raw/transcripts/lenny/kevin-weil.md]

> "If the model gets it right 60% of the time, you build a very different product than if it gets it right 95% of the time versus 99.5% of the time. You need evals to know which world you're in." — Kevin Weil

### 3. Model Maximalism — Ship First, Trust the Model to Catch Up

OpenAI's product philosophy is **model maximalism**: don't waste time building scaffolding and guardrails around the model's current limitations, because a better model is two months away. Instead, ship the product with minimal wrappers and iterate in public. This runs counter to the instinct of most PMs, who want to polish and de-risk. But Kevin has seen it work repeatedly — from image generation to deep research to reasoning models. The key is **iterative deployment**: co-evolve the product with society by learning together in public, launching when it's 80% there, and letting the next model release fix the remaining 20%.^[raw/transcripts/lenny/kevin-weil.md]

> "We don't spend much time building scaffolding around limitations because in two months there's going to be a better model that blows away whatever the current limitations are." — Kevin Weil

### 4. Chat Is the Universal Interface for Intelligence

Despite the conventional wisdom that "chat is not the future," Kevin makes a compelling counterargument: human conversation scales from very low to very high IQ — you can talk to a toddler and to a Nobel laureate using the same conversational interface. Chat works the same way for AI. It's the universal UI because it adapts to the complexity of the task. The real innovation isn't replacing chat — it's layering different interaction modes on top of it (reasoning chains, deep research, canvas, agentic actions) that all feel like natural extensions of conversation. OpenAI's design philosophy is to observe how humans naturally think and collaborate (brainstorming, step-by-step reasoning, summarizing thoughts) and replicate those patterns in the AI interaction.^[raw/transcripts/lenny/kevin-weil.md]

> "The IQ of a human can span from really low to really high and it all works talking to them. Chat is the same thing — it can work on all kinds of intelligence levels." — Kevin Weil

### 5. The Real Moats Are Industry-Specific Data and Custom Evals

Kevin's perspective on where startups can compete: the foundational model companies are not going to eat every use case. There are more smart people outside any company's walls than inside. Most real-world knowledge is **behind the walls of companies, industries, and governments** — it's not in any training set. The future belongs to companies that can take incredibly capable base models and fine-tune them on proprietary, industry-specific data, then measure performance with custom evals. The gap isn't model intelligence — it's the ability to evaluate and optimize for specific use cases that matter to a particular business or vertical. This is where startups have a massive structural advantage over the platform companies.^[raw/transcripts/lenny/kevin-weil.md]

> "No matter how big your company gets, no matter how incredible the people are, there are way more smart people outside your walls than inside." — Kevin Weil (quoting Ev Williams)

## Episode Appearances

- [[lenny/kevin-weil|OpenAI's CPO on how AI changes must-have skills, moats, coding, startup playbooks, more | Kevin Weil]] — Evals, model maximalism, chat as UI, iterative deployment, where startups can compete

## Related Concepts

- [[artificial-intelligence]]
- [[product-management]]
- [[evals]]
- [[openai]]
- [[product-strategy]]
- [[startup-advice]]
- [[leadership]]
- [[user-experience]]


## Episodes

- **20VC: Kevin Weil on The Biggest Lessons from Leading Product at Instagram and Twitter | How Working ** (2022-10-07)
