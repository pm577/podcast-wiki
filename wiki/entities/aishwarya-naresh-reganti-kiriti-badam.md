---
title: Aishwarya Naresh Reganti + Kiriti Badam
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: [person, ai, ai-products, machine-learning, enterprise, product-management]
sources:
  - raw/transcripts/lenny/lenny-2026-01-11-aishwarya-naresh-reganti-kiriti-badam.md
confidence: high
---

# Aishwarya Naresh Reganti + Kiriti Badam

**Roles:** Aishwarya — AI leader, startup founder, former AI product lead; Kiriti — former AI engineer at OpenAI, Google, and Amazon  
**Known for:** Building and launching 50+ enterprise AI products; framework for building AI products with a problem-first, iterative approach.

## Key Views

### 1. AI products are fundamentally different from traditional software

The core challenge: AI is non-deterministic on both input (users can express intent in infinite natural language ways) and output (different responses every time). Traditional deterministic testing and QA approaches don't work. Teams must accept that you cannot pre-test every scenario — you need a fundamentally different development lifecycle that combines evals, production monitoring, and human-in-the-loop feedback.

> "The bar to using AI products is much lower because you can be as natural as you would be with humans, but that's also the problem — there are tons of ways we communicate and you want to achieve a deterministic outcome with non-deterministic technology." — Aishwarya Naresh Reganti

### 2. Start with low autonomy, high human control

Their core framework for building AI agents: start at minimal autonomy (V1: human does all work with AI assist) and progressively increase autonomy (V2: multi-step with human review, V3: A/B tested auto-optimized). Jumping straight to full autonomy is the #1 failure mode. This "problem-first" approach forces teams to clarify what they're solving before getting lost in AI complexity. 74% of enterprises cite reliability as their biggest barrier to deploying AI — starting small directly addresses this.

> "When you start small with high human control and low agency, it forces you to think about what is the problem that you're going to solve. One easy slippery slope is to forget the problem and just think about the complexities of the solution." — Kiriti Badam

### 3. The success triangle: leaders + culture + tech

AI product success requires three dimensions working together: **(1) Leaders** must rebuild their intuitions — the CEO needs daily hands-on AI engagement (example: Rackspace CEO blocked 4-6 AM daily for AI). Leaders must be vulnerable about what they don't know. **(2) Culture** must be about empowerment, not fear — subject matter experts won't help build AI if they think it replaces them. Framing it as augmentation vs. replacement is critical. **(3) Technical excellence** — deep workflow understanding, rapid iteration, and building the flywheel.

> "Every technology problem is a people problem first. With companies that build successful AI products, it's these three dimensions: great leaders, good culture, and technical prowess." — Aishwarya Naresh Reganti

### 4. Evals + production monitoring = both are essential, not either/or

Kiriti rejects the false dichotomy between evals (pre-deployment testing) and production monitoring (post-deployment observation). Evals encode your product knowledge into test datasets. Production monitoring catches the infinite failure modes you can't predict. The right process: build eval datasets for known failure modes → deploy → monitor for unknown patterns → build new eval datasets from observed failures → iterate. Neither alone is sufficient.

> "Nobody goes into deploying an application without testing it first. But there is no guarantee that the eval dataset covers all problems. You still need production monitoring to catch different kinds of problems." — Kiriti Badam

### 5. One-click AI agents are pure marketing — real AI deployment takes 4-6 months

Their most practical warning: anyone selling an out-of-the-box agent that will deliver significant ROI in days is overselling. Enterprise data and infrastructure are too messy. Taxonomies are inconsistent, tech debt is everywhere, and the agent needs to learn how your specific systems work. Real AI deployment that replaces any critical workflow takes 4-6 months even with the best data layer. The winning companies are those obsessed with understanding their workflows deeply.

> "If someone's selling you one-click agents, it's pure marketing. I would rather go with a company that says 'We're going to build this pipeline for you that will learn over time.'" — Kiriti Badam

## Episode Appearances

- [[lenny-2026-01-11-aishwarya-naresh-reganti-kiriti-badam]] — Why AI products fail: lessons from 50+ AI deployments at OpenAI, Google & Amazon

## Related Concepts

- [[ai-product-development]]
- [[ai-agents]]
- [[enterprise-ai]]
- [[product-management]]
