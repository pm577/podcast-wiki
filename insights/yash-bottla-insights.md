# Yash Bottla — Insights

*Extracted from podcast appearances.*

## Insight 1: When you join a company, work on the hairiest thing no one wants to work on, bec...
**Claim:** When you join a company, work on the hairiest thing no one wants to work on, because people will like you for it.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Yash's advice on career strategy at OpenAI

## Insight 2: RL training needs verifiable rewards — a deterministic way to check if the model...
**Claim:** RL training needs verifiable rewards — a deterministic way to check if the model did the correct thing. Code and math are ideal because you can compile, run unit tests, check correctness.
**Framework:** Reinforcement Learning with Verifiable Rewards (RLVR)
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Discussion on why all labs converged on software engineering for RL

## Insight 3: Enterprises can define what good and bad looks like for their specific use case,...
**Claim:** Enterprises can define what good and bad looks like for their specific use case, then directly optimize toward reducing error rate using post-training RL, which is much more data-efficient and uses orders of magnitude less compute than pre-training.
**Framework:** Post-training RL
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** DoorDash example of specializing models for menu extraction

## Insight 4: The future is specific to enterprises. General models set the floor; specializin...
**Claim:** The future is specific to enterprises. General models set the floor; specializing them toward individual enterprise needs is how companies differentiate and set the ceiling versus competitors.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Yash's motivation for starting Applied Compute

## Insight 5: Evals set the road map — define the hill you want to climb. RL is an eval-maxing...
**Claim:** Evals set the road map — define the hill you want to climb. RL is an eval-maxing machine: create a training pipeline that looks like the eval, climb that hill, then move to the next eval.
**Framework:** Eval-driven RL
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Discussion on importance of evals and why labs guard them

## Insight 6: Coding models may be AGI-complete — every task, when broken down, is a coding ta...
**Claim:** Coding models may be AGI-complete — every task, when broken down, is a coding task. Models use code as a general language to interact with the real world.
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.7
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Discussion on why models write code instead of doing tool calls

## Insight 7: The holy grail is continual learning: a model that can do something once and lea...
**Claim:** The holy grail is continual learning: a model that can do something once and learn from an extremely sparse reward, like burning your hand on a stove.
**Framework:** Continual learning
**Audience:** investor | **Actionability:** 3/10 | **Confidence:** 0.8
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Discussion on future bottlenecks in model training

## Insight 8: Post-training on a specific task (e.g., bug-catching) with a small model can ach...
**Claim:** Post-training on a specific task (e.g., bug-catching) with a small model can achieve performance of larger models at lower cost and latency.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Discussion of Cognition/Windsurf's bug-catching model

## Insight 9: Application-layer companies innovate on the 'harness' (model + context + harness...
**Claim:** Application-layer companies innovate on the 'harness' (model + context + harness) rather than just the model weights.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Discussion of model + harness + context layers

## Insight 10: Continual learning from extremely sparse rewards can be done by capturing teleme...
**Claim:** Continual learning from extremely sparse rewards can be done by capturing telemetry in production (e.g., user acceptance/rejection of code suggestions) and taking online training steps with large batches.
**Framework:** Continual learning
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Example of Cursor's Composer model

## Insight 11: Using agents to expend compute offline to analyze documents and past traces of h...
**Claim:** Using agents to expend compute offline to analyze documents and past traces of human-agent interactions can improve downstream performance without using more tokens.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Example of Applied Compute's Context Base

## Insight 12: Scaling transformers is working and likely to continue; non-transformer research...
**Claim:** Scaling transformers is working and likely to continue; non-transformer research is experimental and less likely to yield immediate gains.
**Audience:** investor | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Discussion of non-transformer models

## Insight 13: There is a scarcity of compute; massive innovations are coming in energy sources...
**Claim:** There is a scarcity of compute; massive innovations are coming in energy sources for compute and more efficient chips.
**Audience:** founder | **Actionability:** 5/10 | **Confidence:** 0.75
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Rapid fire question on what to build

## Insight 14: The best data founders pivot to the next wave of data needs (e.g., robotics data...
**Claim:** The best data founders pivot to the next wave of data needs (e.g., robotics data, egocentric data) as synthetic data generation becomes easier.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** yash-bottla-applied-compute-stanford-ai-frontier
**Context:** Short position on data market
