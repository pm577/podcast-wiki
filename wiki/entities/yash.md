---

title: Yash Bottla (Applied Compute)
created: 2026-05-31
updated: 2026-06-01
type: entity
tags: [person, ai-ml, enterprise, model-training, rlvr, startups, post-training, reasoning]
sources:
  - raw/transcripts/lenny/applied-compute-yash.md
  - raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md
confidence: high
subtype: person
---

# Yash Bottla (Applied Compute)

Founder & CEO of Applied Compute. Previously at OpenAI where he led the Long Horizon Tasks team and agentic coding research (which became Codex). One of the few undergrads to go directly to OpenAI research after Stanford. Class of '25. Started on evals ("work on the hairiest thing no one wants to work on"), then moved to reasoning models and post-training.

## Key Views

### 1. The Bottleneck Has Shifted from Compute → RL Environments → Continual Learning

Evolution of bottlenecks: compute → architecture (transformer) → pre-training data → preference tuning (RLHF) → RL environments → **continual learning** (sparse rewards, data-efficient real-world learning).

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

### 2. RL Training Is ~5% of Pre-Training Compute (But Growing)

DeepSeek V3: ~2.5M H800 hours pre-training. DeepSeek R1 RL: ~150K H800 hours = **~5%**. But this is shifting — labs now run data-center-wide RL runs with massive batch sizes exploiting post-training scaling laws.

^[raw/transcripts/lenny/applied-compute-yash.md]

### 3. Enterprise Specialization: General Models Set the Floor, Specialization Sets the Ceiling

Applied Compute helps companies (DoorDash, Cognition/Windsurf) create specialized models trained on proprietary data. DoorDash: 100K+ merchants/year with unstructured menu data. Solution: train against ground truth, optimize directly on error rate.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

### 4. Code Is the Ideal RL Domain Because of Verifiable Rewards

Code and math allow deterministic verification (compile, unit tests). Coding models may be **AGI-complete** — every task when broken down is a coding task. This is why Claude and other models write code instead of making tool calls.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

### 5. Chain of Thought Is a Completely Emergent Behavior

No one trained models to reason. By putting them in constrained RL environments and funneling compute, reasoning emerged — the model spends time thinking, correcting itself. Combining reasoning + tool use → agents that work for long periods → AI co-workers.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

### 6. The "Model + Harness + Context" Trinity

Application-layer companies do innovation on the **harness** to squeeze value out of models. **Context** — access to the right data — often determines whether the model knows the right thing to do. You can't focus on just one layer.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

### 7. The Hardware Bet: Long Nvidia, But In-Housing Is Inevitable

Nvidia takes ~75% margin on chips. Labs spending hundreds of billions may eventually invest in their own chip design. Chips at 80% effectiveness at 2x quantity beat the incumbent on volume.

^[raw/transcripts/stanford-ai-frontier/yash-bottla-applied-compute-stanford-ai-frontier.md]

## Related Concepts

- [[rlvr]]
- [[continual-learning]]
- [[enterprise-ai]]
- [[model-training]]
- [[pre-training]]
- [[post-training]]
- [[test-time-compute]]
- [[stanford-ai-frontier]]
- [[reasoning-models]]
- [[model-evals]]
