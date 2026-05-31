# Stanford AI Frontier: Garry Tan & Diana Hu — Y Combinator

**Episode:** Stanford AI Frontier — The Agentic Company
**Guests:** Garry Tan (CEO, Y Combinator) & Diana Hu (GP, Y Combinator)
**Date:** ~2026
**Format:** Guest lecture / fireside chat

---

**Host:** CS 153 — Security at Scale, now in its 4th year, inspired by the lineage of Stanford entrepreneurship classes: Peter Thiel's CS 183 (Zero to One), YC's version taught by Sam Altman, and Terry Winograd's CS 43N. Full rewrite of systems underway — from energy (Scott Nolan, General Matter) to chips (Jensen Huang last week). One bottleneck: capital.

**Host on the SAFE:** Before YC, venture capital was a mess — firms doing their own deals, negotiating with founders. Paul Graham and Jessica Livingston introduced a new standard: the SAFE (Simple Agreement for Future Equity). A two-page legal document put online for free, standardizing seed-stage funding. At the time it seemed like "whatever legal document." In hindsight, a pivotal moment in Silicon Valley history — standardizing the allocation of capital in the cloud/SaaS era when compute costs had dropped but VCs hadn't caught up. YC became the institution that enforced that standard.

**Host connecting the theme:** Systems design isn't just engineering — you can do it in any domain to accelerate progress and unblock bottlenecks. At Amp, they're considering open-sourcing a "standard agreement for future compute" inspired by what YC did.

---

**Garry Tan:** Stanford class of '03. Fell asleep in this lecture hall many times. Grand shift happening right now — new standards being established. The SAFE was a legal instrument; what we're talking about today is code. Markdown is code.

**Diana Hu:** GP at YC. Living through an exciting time with AI. Unprecedented growth — companies going from zero to tens of millions in revenue within one year (impossible before — would take 4-5 years to get to Series B traction). Will show how founders have done it.

---

**Garry: Personal Story**

2008: got into YC, raised ~$4M, hired 10 people, created Posterous (dead simple blog platform), sold to Twitter 3 years later for $20M. All software over 2 years with 10 people and all that capital.

Now: with a $200/month Claude Code Max plan, anyone in this room could do the same in 5 days instead of 2 years.

A **6-person team** can hit $10M in revenue today.

---

**Garry: Gstack Origin**

Saw Steve Yegge's post: people using AI coding agents are 10-100x more productive (Cursor/Chat); at Anthropic, about 1,000x as productive as Googlers in 2005. Had to try it. Opened Claude Code, ended up writing ~1M lines of code.

**Myths:**
- It's not just "AI slop" — yes, LLMs are verbose, but with a software factory you fight and prevent that
- Yes, hallucinations exist — that's what you control
- Yes, you can make demo code fast — getting to production requires **80-90% test coverage**
- **Plan-Eng-Review** is the #1 skill — used ~20x/day to ship real production code

**LOC controversy:** LOC alone is gameable. But if you have tests, if it works for you and your customers, if they're paying — that's the true metric. Nothing in Claude Code or the model tells it to write as many lines as possible; if anything, the reverse is true.

**Results:** Gstack hit 87,000 GitHub stars; Gbrain: 13,000 stars. Over 100,000 GitHub stars total for someone who wasn't coding at all in December last year. ~15,000 people use it daily.

**The shift:** Last year = co-pilots. Today = a **software factory**.

---

**Garry: Skills as Personas**

The latent space of LLMs contains specific personas. Gstack pulls them out as skills.

**Office Hours skill:** Distillation of what YC partners do — ask questions about problem, customer, evidence, what to build. Took 3-4 months of transcripts across thousands of conversations, distilled down by 90%.

**Plan-Eng-Review:** Asks "what's the 10x version? What's the platonic ideal?" Then builds a roadmap in a straight line from now to there.

**Boil the ocean:** In meetings people say "let's not boil the ocean." With coding agents, the answer is actually: **let's boil the ocean**. You sitting at a terminal can do the work of 500-1,000 people. If that's true, all expectations are 1,000x wrong. It's baked into the model weights — ask Claude Code "how long?" → "3 weeks" → approve the plan → done in an hour.

---

**Garry: Open Claw & Hermes Agent — New Primitives**

Teaching new primitives on how to think about code and markdown working together.

**Deterministic vs latent:** When an agentic system breaks, it always breaks because something was wrong about what he was trying to do. Either doing **deterministic work** (should be code in markdown skills) or **latent work** (should be LLM-in-the-loop).

Example: seating at an 800-person dinner party or 6,000-person Startup School. Can't do in latent space — model hallucinates. Need latent + deterministic working together.

**What is a skill?** Just a runbook. Steps with branching. But the key: it can call code.

**Resolvers:** Claude.md getting 40,000 tokens? Fix: a resolver. Take instructions out of context, load them only when needed. "Anytime you have to write to the changelog, load changelog.md." This is the core of a great agent.

**Skillify:** Go up one level of abstraction. Do something once, get the agent to do it exactly right, then say "skillify." Result: a skill file + code + tests + LLM evals + integration tests + resolver triggers + end-to-end smoke tests + schema.

**Skillify pipeline (10 steps, only 2 are writing):**
1. Write unit tests for code
2. Write LLM evals for skill file
3. Write integration test
4. Ensure resolver trigger in agents.md
5. Test trigger (LLM as judge eval — broad enough?)
6. Check resolvable (avoid duplicates/DRY)
7. End-to-end smoke test
8. Schema — where does this live in memory and repo

**Analogy to company:**
- Skill = employee with a capability
- Resolver = org chart
- Filing rules / brain = internal process
- Check resolvable = audit & compliance
- Trigger eval = performance reviews

---

**Garry: Gbrain — Three-Layer Memory System**

Started with Karpathy's knowledge wiki pattern. It fell over with just grep. Added:
1. **Vector search** (ARR fusion)
2. **Backlinks**
3. **Graph database** as type knowledge graph
4. **(Soon) Epistemology system** — track hunches vs beliefs vs world knowledge, by specific person, and when they manifest

Philosophy: founder's journey = having a hunch nobody believes yet, spending 1-5 years proving it correct. Gbrain should spot that. Building software for himself, open-sourcing it for others.

Next: fully dynamic ontology — schema built for him, but could work for researchers, journalists, politicians — each needs different schema.

---

**Diana: The AI-Native Company**

**Closed-loop vs open-loop systems:**
- Pre-AI companies: open loop. Lossy information — side conversations, DMs, Slack, unwritten meeting notes, vibes. Error accumulates over time.
- AI-native: closed loop. Agents embedded into every decision. Agent needs read access to EVERY artifact (GitHub, Discord, meeting recordings). Agent suggests next items, bug fixes → Gbrain for memory context → system self-heals.

**Stats:** One employee can generate $1-2M in revenue (vs public SaaS comps under $100K/employee). At least 10x improvement.

**YC engineering team:** Cut sprint time in half, 10x amount of work.

**Three roles in an agentic org:**
1. **IC (Individual Contributor)** — everyone ships. Even non-technical people (salesperson building pipeline automation).
2. **DRI (Directly Responsible Individual)** — owns every outcome. Orchestrates ICs. Often the founder.
3. **AI Founder** — lives at the edge of the future, trying all tools, bringing innovations into the company.

**The taste gap:** Cost of shipping code → zero. What doesn't go to zero: **taste** — the discernment to build something good. Manifests as evals. Generic benchmarks (MMLU) don't tell you if your product works. The judge is whether users want it. You need to:
- Capture traces (context-dependent — video vs speech vs B2B)
- Convert failures into evals
- Replay constantly → self-heal → improve automatically

---

**Diana: Starting a Company Now**

Best time in history to start. Unprecedented growth:
- **Salient** — voice agents for loan servicing, closed top US banks
- **Happy Robot** — Series B, 10x revenue in a year, freight forwarding agents
- **Reductem** — document processing (improves RAG, memory, brain for all agents)

**How they did it:** Wedge into painful workflows. Go undercover — shadow or take a job, learn the domain, automate repetitive labor with agents. Most founders didn't have domain backgrounds (Scale AI, Happy Robot founders).

**White space:** Anthropic deployment data — 50% penetration into software, but massive white space in back office, finance, data, academics, cybersecurity, customer service. Hundreds of AI unicorns waiting.

**Growth reality:** In the past, only top 1% of YC companies grew 10% week-over-week (Airbnb). Now companies are 3x-ing within 3 months on average. Never happened before in YC's history.

**Closing:** A one-person frontier lab → a one-person company. That could be you.
