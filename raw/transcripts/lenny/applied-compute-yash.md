---
type: Episode
podcast: lenny
guest: yash
date: 2026-05-30
title: "Yash from Applied Compute on RLVR, continual learning, and the future of enterprise AI"
tags: [ai-ml, venture-capital, startups, model-training, rlvr, enterprise]
url: ""
---

# Yash (Applied Compute) — Interview Transcript

**Note:** Course guest lecture (Stanford). Yash is co-founder of Applied Compute, previously at OpenAI leading agentic coding research (Codex).

**On the transformer era:** The transformer was the moment where researchers at Google Brain came up with a new architecture that allowed scaling language model training. It was way more performant on existing hardware — could run on GPUs. Compared to RNNs or LSTMs, they employed attention which led to way better performance in next token prediction and could scale to massively long sequences.

2018-2019 was the era of pre-training — taking massive corpuses of text and teaching models to predict the next token by optimizing on loss. Then scaling laws from OpenAI showed that making models really big gives much better performance — proved out with GPT-3, the first model that seemed to have some level of general intelligence. Then Chinchilla scaling laws showed there's a compute-optimal way: scale parameter size AND train on much more data.

Then came the era of RLHF and preference tuning to steer these models. Base models just do next token prediction — they hallucinate, don't answer your question, may say unaligned things. GPT-4 was the next step change in quality.

**On reasoning models:** In 2024, OpenAI came out with o1 — a new axis for scaling model intelligence: test-time compute. Chain of thought is a completely emergent behavior. No one trained the model to reason, correct itself, or spend time thinking. By putting it in constrained RL environments and funneling compute, you got models with the emergent property to reason. Combining that with tool use (Claude Code, Deep Research) gives you agents that can reason and work for long periods — what people call AI co-workers today.

**On bottlenecks:** The bottlenecks went from: compute → architecture → pre-training data → preference tuning (RLHF) → RL environments (today) → continual learning (future). Continual learning is the holy grail: being extremely data efficient with real-world interactions. Like burning your hand on a stove — you only need to do it once.

**On why code:** RL training requires verifiable rewards. You need a deterministic way to check if the model did the correct thing. Code and math are really good for this — you can compile code, run unit tests. Code also has great synthetic data scale. Many researchers think coding models are AGI-complete.

**On pre-training vs post-training:** Pre-training takes orders of magnitude more compute. DeepSeek V3: ~2.5M H800 hours. DeepSeek R1 (RL): ~150K H800 hours — 5% of pre-training compute. But post-training scaling is increasing — people doing data-center-wide RL runs.

**On the compute/scale economics of Nvidia:** Their chips have 75% margins. Labs could in-source chip design. Even if chips are 80% as effective, at 2x quantity they'd win on volume.

**On Applied Compute:** Started a year ago with co-founders from Stanford/OpenAI. Thesis: general models set the floor, specialization sets the ceiling. DoorDash example: 100K+ merchants/year with unstructured menu data. General models couldn't handle DoorDash's style guide. Solution: train against ground truth, optimize directly on error rate.
