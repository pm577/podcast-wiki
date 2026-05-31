# Stanford AI Frontier: Yash Bottla — Applied Compute

**Episode:** Stanford AI Frontier — Models & Post-Training
**Guest:** Yash Bottla, Founder & CEO, Applied Compute
**Date:** ~2026
**Format:** Guest lecture / fireside chat

---

**Host:** Today we're going to talk about this part of the stack — models — and how do you build better models for better applications. Our guest is Yash Bottla, founder and CEO of Applied Compute. He was one of the very few undergrads who went directly to OpenAI research after Stanford, was a part of the post-training team, started Applied Compute after OpenAI because of an insight he had during his work there, and has built it into one of the most successful businesses applying his learnings to enterprises.

**Yash:** Thanks for having me.

**Host:** Tell us about your journey.

**Yash:** I was sitting here taking finals not that long ago — class of '25. Grew up in Austin, Texas, came here for school. I was a very good student in high school, a very bad student here — never went to class, watched lectures online. Built stuff on campus, got connected to Sam Altman very serendipitously through mutual friends. One thing about Sam — he has an incredible soft spot for helping young people early in their careers. Hit it off freshman year summer. A friend and I were deciding: do we do summer internships or work on a project? Ended up doing our project. We were looking for money, shot Sam a blind email. He gave us a very small check to cover food and rent. Worked on it for the summer, shut it down. Came back for sophomore year, did Tree Hacks.

Late 2022 — ChatGPT came out. I was playing around with it and thought: "Holy crap, this is the coolest thing I've ever seen. I have to go work on it." Shot Sam another email saying "How do I come work on this?" He put me in touch with the OpenAI residency. Joined OpenAI early 2023 on the post-training team. Started on evals — my tip: whenever you join a company, work on the hairiest thing no one wants to work on, because people will like you for it.

**Host:** People were training reasoning models on competitive math. It was this wow moment — massive performance increases. So a friend and I hacked together an agent that could browse the internet and write code. Showed it to leadership — they were excited. Started a team called Long Horizon Tasks, leading agentic coding research which became Codex. Left to start Applied Compute about a year ago. One year was last Saturday.

**Yash:** We saw this gap: models were getting really smart, but when you apply them inside the enterprise, they're smart geniuses that know nothing about your business. Inside enterprise is where most of the data in the world is — proprietary data built up over time. We're helping companies take frontier technology and create specialized models to enhance their business.

---

**Host:** What is going on at the model layer? Why is advancement in the last four years notable and what is driving it?

**Yash:** Deep learning — AlexNet was the pivotal moment. It's also when we stopped understanding what models actually do. Deep learning lets you learn underlying representations from data — train on data, push compute, get smart models with millions/billions of parameters. You don't know what they do, but they're really good at prediction tasks. Before AlexNet: handcrafted features, rudimentary classifiers detecting edges. AlexNet applied GPUs against ImageNet with neural nets — proved that if you scale compute and data, you get massive gains in predictive accuracy.

**Modern model training timeline:**

**Transformer** — Google Brain researchers created a new architecture that allowed scaling language model training. More performant on existing hardware (GPUs) compared to RNNs/LSTMs. Attention technique led to way better next-token prediction and could scale to massively long sequences.

**2018-2019: Pre-training era** — Taking massive corpora of text, teaching models to predict the next token by optimizing loss. Model predicts next token, compares to ground truth, back-propagates to tweak weights.

**Scaling laws** — OpenAI scaling laws (Kaplan): make models bigger, get much better performance. Proved with GPT-3, first model with some level of general intelligence. Chinchilla scaling laws: not just bigger models — there's a compute-optimal way to scale. Scale parameter size AND train on much more data.

**Post-GPT-3 era** — Making models useful to normal people. Reinforcement learning with human feedback (RLHF), preference tuning to steer models (base models just do next-token prediction — hallucinate, don't answer questions, may say unaligned things).

**GPT-4** — Next-level step change in quality.

**2024: Reasoning models** — OpenAI's o1. New axis for scaling model intelligence: test-time compute. Chain of thought is a **completely emergent behavior** — the model reasons, spends time thinking, corrects itself. No one trained it to do that. By putting it in constrained RL environments and funneling compute, you got models with this emergent property to reason.

Combining reasoning with tool use (Claude Code, Deep Research) → agents that could reason and work for long periods → AI co-workers.

---

**Host:** Multiple ingredients go into a great model: data, compute, talent, algorithms. What is the bottleneck today, what was it in the past, what will it be?

**Yash:** Bottlenecks evolved:
1. Having the **compute** to train
2. The correct **architecture** (transformers) to scale
3. **Pre-training data** — training on the entire internet
4. Making models usable via **preference tuning**
5. Today: **RL environments** — constructing worlds where models explore and learn from verifiable rewards
6. Future: **Continual learning** — being extremely data-efficient with sparse rewards. Like burning your hand on a stove — you only need to do that once. Models today are not like that.

Pre-training is not super data-efficient (read the whole internet). Post-training is more data-efficient. RL environments are the most data-efficient today. The holy grail: a model that can do something once and learn from an extremely sparse reward.

---

**Host:** Why have all the labs converged on software engineering? What is the unique property of code?

**Yash:** RL training needs **verifiable rewards** — a deterministic way to check if the model did the correct thing. Code and math: you can compile, run unit tests, check correctness. Also easy to make synthetic data at scale — tons of code tokens on the internet.

Coding models may be **AGI-complete** — every task, when broken down, is a coding task. That's why Claude and other models write code instead of doing tool calls — they use code as a general language to interact with the real world.

**Host:** Example: making slides. This deck was completely generated with Claude Code. What's the relationship between code and slide generation?

**Yash:** You can combine code outputs with auxiliary rewards. Optimize for functional slides (code execution + structure) AND aesthetics (reward model trained on human preferences of what looks good). Combine rewards and jointly optimize.

---

**Host:** Pre-training vs post-training — break those down.

**Yash:** **Pre-training** — massive training effort: internet-scale data (trillions of tokens), tons of compute through the transformer architecture, train a neural net to learn patterns in language. The thing that falls out is a form of intelligence. It's **compression** — taking all of human knowledge (the internet) and putting it into a set of weights. Takes orders of magnitude more compute than post-training.

**Post-training** — aligning the model. The base model just does next-token prediction. If you write "who should I invite to dinner" it might output random names. Post-training takes the model and tells it what good and bad outputs look like → learns chat format (user/assistant), learns safety guidelines.

**Data is scarce** in both cases. Pre-training: we've run out of data — only so much text on the internet. Frontier labs are the only ones who can do this level of training (huge capex requirements). Post-training: various methods from SFT to RLHF to RLVR (reinforcement learning with verifiable rewards).

---

**Host:** Where do we get more data for future models?

**Yash:** Multiple layers:
1. **Pre-training data** — buying old libraries with ancient books, scanning them. Investment in **synthetic generation** — taking primary source documents and exploding them to orders of magnitude more tokens.
2. **New architectural advances** — making better use of existing data. On principle, you shouldn't need internet-scale data to learn this stuff.
3. **RL environments** — a different type of data. Construct the world the model operates in, have it do things, exchange compute for less high-quality data. Use way more compute and learn more from a single sample/rollout.
4. **The data market** is hard — as models get smarter, creating new tasks to hill-climb gets harder. The generator-verifier gap (e.g., code: hold out unit tests, have model attempt, run tests) doesn't need humans. Smarter models → better synthetic data pipelines.

---

**Host:** Why are evals important? Why do labs guard their evals?

**Yash:** When you train models on reward functions, knowing what good and bad looks like becomes the most important thing. Evals set the **road map** — define the hill you want to climb. SWE-bench started the code model race. RL is an **eval-maxing machine** — create a training pipeline that looks like the eval, climb that hill, on to the next eval.

For enterprises: they have their own idea of what good and bad looks like. JPMorgan vs Goldman Sachs — different standards, different ways of operating. Labs optimize toward their evals, enterprises optimize toward theirs. Applied Compute is that specialization layer.

---

**Host:** What led you to start Applied Compute?

**Yash:** Started with co-founders Rhythm and Lyndon (both Stanford students, all three at OpenAI together). Funny story: Sam asked me "who's the smartest person you know?" — I said Rhythm. Sam asked Rhythm the same thing — he said Lyndon. That's how we all ended up there.

Core idea: the future is specific to enterprises. General models are workhorse models that set the floor. Specializing them toward individual enterprise needs is how people **differentiate**. Going and building trained models, creating specialized systems → set the ceiling versus competitors.

**Example: DoorDash** (customer)
- Onboards 100K+ merchants per year
- Merchants supply unstructured information (menus, menu extraction)
- Going from images to a DoorDash storefront is hard
- DoorDash has a specific style guide for modifiers, add-ons vs special ingredients
- General models couldn't handle it
- Solution: collect model outputs → humans correct menus → calculate delta → during training, check model output against ground truth → quantify loss/reward (error rate) → optimize directly against reducing error rate
- "Define what good and bad looks like, then directly optimize toward outcomes you want"

**Why not wait for GPT-7 to be better out of the box?**
Enterprises care about being at the frontier **at any point in time**. GPT-17 is a long time from here. ROI on training your own models today is compelling: RL has become very data-efficient, uses orders of magnitude less compute than pre-training, and you can optimize performance way more than with SFT or RLHF.

**Cost comparison:** DeepSeek V3 pre-training: ~2.5M H800 hours. DeepSeek R1 RL training: ~150K H800 hours — about **5%** of pre-training compute. But this is changing — data-center-wide RL runs with massive batch sizes, post-training scaling laws.

**Example: Cognition/Windsurf**
- Bug-catching model: runs sub-2-seconds, checks code you wrote, tells you if there's a bug
- Can't get this from a general model (pareto frontier of performance/cost/latency)
- Take a small model, post-train the heck out of it on bug-catching → get benefits of cost/latency AND performance of larger models
- "Model + harness + context" — never focus on just one layer. Application-layer companies do tons of innovation on the harness.

---

**Host:** Continual learning — what is it, why is it the next frontier?

**Yash:** Continual learning = learning from **extremely sparse rewards**. If you have a system deployed in production, how do you understand how the AI model is being used, the downstream consequences of its actions, and use that to update the system so it gets better over time?

This will be gradual — blocked on having access to the right data.

**Example 1: Cursor's Composer model**
- Coding model trained on their own data on top of open-source model
- Put it in production, captured telemetry, took training steps online based on implicit rewards
- "Did the user accept this code suggestion or revert it?" → optimize towards that
- **Hours per step**, each step has a massive batch of samples
- Can't replay environments in production (dynamic) — but massive batches denoise the gradient

**Example 2: Applied Compute's Context Base**
- Use agents to expend compute offline, analyze documents and past traces of human-agent interactions
- Extract learnings to improve downstream performance
- Saw massive performance increases at different reasoning efforts while using the same tokens

**Three layers of innovation:** weight updates, context, and the harness itself.

---

**Host:** Non-transformer models — transformers are inefficient. Is the transformer the dominant way (like airplanes vs birds — heavy but infrastructure is built around it)?

**Yash:** Scaling transformers is **working**. Simple recipe to make them smarter. More likely that AI will tell us what the better architecture is (if we just continue scaling) than us coming up with one ourselves. If there were a wall in what the architecture allows, we'd see innovation. Until then: concentrate on scaling transformers.

**Counterargument (Ilya, Jan LeCun, others):** You don't need pre-training levels of data to learn underlying representations of language. Humans don't need it, therefore there must be a better architecture. But the investments in compute scale-outs are enormous — people are optimizing architectures directly in the chips. Labs are investing more in the transformer. Non-transformer research is experimental.

---

**Host:** Rapid fire — what would you be building if not Applied Compute?

**Yash:** Scarcity of compute. Demand far outpaces supply. Massive innovations coming in energy sources for compute and more efficient chips. We could be making way better hardware to optimize training and chip design. Would look into hardware.

**Long:** Nvidia. 75% margin on chips. Labs spend hundreds of billions. Maybe labs invest in their own chip design — chips 80% as effective at 2x quantity. Hard but possible.

**Short:** The data market is tough. RL tasks: you train models to be smart, then creating new tasks to hill-climb gets harder. Models are getting really good → synthetic data generation. The best data founders are good at pivoting to the next wave (robotics data, egocentric data).

**Favorite AI product:** ImageGPT 2 (Image Duo). For people who can't do design — take a paper, drop it in, get a visual walkthrough. The most beautiful slide in this deck was made with it.
