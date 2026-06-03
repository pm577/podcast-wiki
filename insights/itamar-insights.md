# Itamar — Insights

*Extracted from podcast appearances.*

### Insight: Use fake door tests, smoke tests, and Wizard of Oz tests to gather evidence befo...
**Claim:** Use fake door tests, smoke tests, and Wizard of Oz tests to gather evidence before building a full product. For Gmail's tabbed inbox, they showed a facade of HTML that sorted messages correctly, which gave evidence to proceed with building.
**Framework:** Fake door test, Smoke test, Wizard of Oz test
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Itamar describes how they tested the tabbed inbox concept with a fake interface to gather evidence.

### Insight: Avoid opinion-based development where you go all in on an idea based on belief a...
**Claim:** Avoid opinion-based development where you go all in on an idea based on belief and early positive indications. Google+ was a massive project with 1000 people that ultimately failed because they didn't test the core assumption that people needed another social network.
**Framework:** Opinion-based development
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Itamar contrasts the failure of Google+ with the success of the tabbed inbox, attributing the failure to opinion-based development.

### Insight: Adopt an evidence-guided approach: focus on customers, generate many ideas, look...
**Claim:** Adopt an evidence-guided approach: focus on customers, generate many ideas, look at data, launch rough betas, and take action based on results. Google's early success came from this approach, but they abandoned it for Google+.
**Framework:** Evidence-guided
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Itamar describes Google's early evidence-guided culture and how it was set aside for Google+.

### Insight: Start with a user-centric goal and problem definition, then generate and test id...
**Claim:** Start with a user-centric goal and problem definition, then generate and test ideas rigorously. For the tabbed inbox, they researched users, established a goal to reduce inbox clutter, and tested ideas on themselves and external testers before building.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Itamar explains how the tabbed inbox project began with understanding user problems and testing ideas.

### Insight: Use dogfooding and external testers to validate ideas early. The Gmail team test...
**Claim:** Use dogfooding and external testers to validate ideas early. The Gmail team tested the tabbed inbox on their own inboxes, then recruited other Googlers, and finally external testers.
**Framework:** Dogfooding
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Itamar describes the testing process for the tabbed inbox, starting with internal dogfooding.

### Insight: When you have a discussion based on opinions, usually the most senior person's o...
**Claim:** When you have a discussion based on opinions, usually the most senior person's opinions will win. If you come with hard data, you can challenge opinions more effectively.
**Framework:** Evidence-Guided
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Discussion about pushing back on founders/execs with data instead of opinions.

### Insight: If you run a secret experiment and show data to a resistant boss, you usually ge...
**Claim:** If you run a secret experiment and show data to a resistant boss, you usually get one of two results: they get mad (in which case you should look for another job) or they are pleasantly surprised and change their mind.
**Framework:** Evidence-Guided
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Advice on how to present counter proposals to executives who are not open to challenge.

### Insight: Telltale signs that you are not evidence-guided include: unclear goals, missing ...
**Claim:** Telltale signs that you are not evidence-guided include: unclear goals, missing user-facing metrics, too much time on roadmapping, lack of experimentation, and disengaged teams focused on output.
**Framework:** Evidence-Guided
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Answering the question about signs that a team is not actually evidence-guided.

### Insight: The GIST model breaks the change to evidence-guided into four parts: Goals, Idea...
**Claim:** The GIST model breaks the change to evidence-guided into four parts: Goals, Ideas, Steps, and Tasks. Goals define what to achieve, ideas are hypotheses, steps are build-measure-learn loops, and tasks are managed in Kanban/Jira.
**Framework:** GIST
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Explanation of the GIST model as an overarching approach to building product.

### Insight: Even Steve Jobs changed his mind when presented with evidence; he was against ph...
**Claim:** Even Steve Jobs changed his mind when presented with evidence; he was against phones and multitouch initially but flipped after seeing demos and data.
**Audience:** founder | **Actionability:** 5/10 | **Confidence:** 0.85
**Source:** itamar-gilad
**Context:** Discussion about whether top-down visionary ideas can work, using iPhone as example.

### Insight: The Gmail promotions tab feature was initially seen as stupid by colleagues who ...
**Claim:** The Gmail promotions tab feature was initially seen as stupid by colleagues who knew how to manage their inbox, but 85-88% of users loved it, showing the importance of testing with the actual user base.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Story about developing the Gmail promotions tab by testing with passive users.

### Insight: Goals should paint the end state and define where you want to end up; they shoul...
**Claim:** Goals should paint the end state and define where you want to end up; they should not be used as a planning session. Many companies use the goals layer as a planning session, talking about what to build by when, which is actually planning work, not goals.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Discussion about the goals layer of GIST and common misuse of goals as planning.

### Insight: Use a value exchange loop model to construct overarching goals for the entire or...
**Claim:** Use a value exchange loop model to construct overarching goals for the entire organization, measuring both value delivered (North Star metric) and value captured (top KPI like revenue).
**Framework:** Value exchange loop
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Explanation of how evidence-guided companies use models for goals, with examples like WhatsApp (messages sent) and Airbnb (nights booked).

### Insight: Create a metrics tree that breaks down the North Star metric and top KPI into su...
**Claim:** Create a metrics tree that breaks down the North Star metric and top KPI into sub-metrics, which helps estimate impact of experiments, align teams, and assign ownership of sub-metrics to teams.
**Framework:** Metrics tree
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Discussion of how metrics trees help with impact assessment, alignment, and team topology.

### Insight: Arrange team topology around goals (metrics tree) rather than software structure...
**Claim:** Arrange team topology around goals (metrics tree) rather than software structure or hierarchy, and readjust from time to time as goals change.
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** itamar-gilad
**Context:** Observation that team topology often reflects software structure, but should be aligned with goals.

### Insight: The North Star metric should measure how much value you create for the market (e...
**Claim:** The North Star metric should measure how much value you create for the market (e.g., messages sent for WhatsApp, nights booked for Airbnb), while the top KPI measures what you get back (e.g., revenue).
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Clarification of the difference between North Star metric and top KPI, with examples.

### Insight: Use ICE (Impact, Confidence, Ease) to evaluate ideas objectively and transparent...
**Claim:** Use ICE (Impact, Confidence, Ease) to evaluate ideas objectively and transparently, avoiding politics and highest-paid person's opinion.
**Framework:** ICE
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Itamar Gilad explains the ideas layer and the need for objective evaluation, introducing ICE as a method to assign three values to each idea.

### Insight: Use the Confidence Meter to assess how much evidence supports your guesses, rang...
**Claim:** Use the Confidence Meter to assess how much evidence supports your guesses, ranging from opinions (0.01/10) to tests (high confidence).
**Framework:** Confidence Meter
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Itamar Gilad introduces the Confidence Meter to help people realize when they have strong vs. weak evidence, tying investment to confidence level.

### Insight: Tie investment in an idea to the level of confidence: start with cheap tests to ...
**Claim:** Tie investment in an idea to the level of confidence: start with cheap tests to gain confidence, then invest more; for low-risk ideas, skip testing.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Itamar Gilad explains that you can tie investment into the idea based on confidence level, and for cheap or low-risk ideas, you can jump to high confidence or launch without testing.

### Insight: Use ICE and the Confidence Meter as an objective way to say no to ideas, by comp...
**Claim:** Use ICE and the Confidence Meter as an objective way to say no to ideas, by comparing impact and confidence scores across ideas.
**Framework:** ICE
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Lenny and Itamar discuss using the tools to stop stupid ideas and say no gently, by showing how other ideas stack up.

### Insight: Do not assume a competitor's feature is validated; they may not know what they a...
**Claim:** Do not assume a competitor's feature is validated; they may not know what they are doing any more than you do.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Itamar Gilad warns against assuming competitors know what they're doing, as part of discussing data as evidence.

### Insight: The metric is not how fast can we get the bits into production, it's about getti...
**Claim:** The metric is not how fast can we get the bits into production, it's about getting the right bits to production. Evidence guided method is far more impactful, faster, and resource efficient than opinion-based method.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Discussion on trade-off between speed of delivery and discovery, and redefining the metric to time to outcomes.

### Insight: Good teams know how to do both learn and build at the same time. The steps layer...
**Claim:** Good teams know how to do both learn and build at the same time. The steps layer is meant to help you do that.
**Framework:** Steps layer
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Explaining that learning and building are not mutually exclusive, and the steps layer helps combine them.

### Insight: For early stage companies, building heavy weighted OKRs and metrics trees may be...
**Claim:** For early stage companies, building heavy weighted OKRs and metrics trees may be overkill; their goal is to find product market fit and iterate towards building their business model.
**Framework:** OKRs, North Star metric
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Advice for different company stages: early stage vs scale.

### Insight: When scaling up, you need a systematic way to evaluate ideas to create order amo...
**Claim:** When scaling up, you need a systematic way to evaluate ideas to create order among many people and money.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** itamar-gilad
**Context:** Contrasting early stage with scale-up needs.

### Insight: Don't try to adopt the whole framework at once; start with the biggest problem y...
**Claim:** Don't try to adopt the whole framework at once; start with the biggest problem you're facing. If goals are unclear, start with goals layer; if debates, start with ideas layer; if building too much without learning, start with steps layer; if team disengaged, start with tasks layer.
**Framework:** Goals, Ideas, Steps, Tasks layers
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Recommendation on how to start adopting evidence-guided methods incrementally.

### Insight: There is a gamut of ways to validate ideas: assessment (e.g., alignment check, I...
**Claim:** There is a gamut of ways to validate ideas: assessment (e.g., alignment check, ICE analysis, assumption mapping), fact-finding (data analysis, surveys, user interviews), tests (fake door, smoke test, Wizard of Oz, concierge test, usability test), experiments (A/B tests), and release (stage release, percent launch). Start early with low-cost methods to poke many ideas quickly.
**Framework:** Steps layer (assessment, fact-finding, tests, experiments, release)
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Detailed explanation of the steps layer and how to validate ideas at different levels of investment.

### Insight: You can learn at a much lower cost than building an elaborate MVP. For example, ...
**Claim:** You can learn at a much lower cost than building an elaborate MVP. For example, at Gmail, they faked the tabbed inbox with a facade of HTML and manually moved emails to test the concept without writing a single line of code.
**Framework:** Steps layer (fake door test)
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Story about validating the tabbed inbox idea with a Wizard of Oz test.

### Insight: Create a GIST board per team with goals (max 4 key results), ideas (with ICE sco...
**Claim:** Create a GIST board per team with goals (max 4 key results), ideas (with ICE scores), and next steps to validate ideas. Update it at least every two weeks and have the team meet around it to discuss progress, ideas, and blockers.
**Framework:** GIST
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Itamar suggests using a GIST board to bridge the gap between planning and execution, involving developers in discovery.

### Insight: Let the team pick which ideas to test first using the ICE process, rather than h...
**Claim:** Let the team pick which ideas to test first using the ICE process, rather than having managers dictate. The product manager is important to guide the choice.
**Framework:** ICE
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** itamar-gilad
**Context:** Itamar recommends that the team should use ICE to choose ideas to test, with the PM playing a key role.

### Insight: Replace release roadmaps with outcome roadmaps that state what outcome you want ...
**Claim:** Replace release roadmaps with outcome roadmaps that state what outcome you want to achieve by a certain time, not which feature to launch. Only commit to a specific feature if it has been validated with high confidence.
**Framework:** Outcome roadmaps
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** itamar-gilad
**Context:** Itamar contrasts release roadmaps with outcome roadmaps, saying the latter allow for learning and evidence-guided decisions.

### Insight: Define steps as learning milestones (e.g., usability test, A/B test) rather than...
**Claim:** Define steps as learning milestones (e.g., usability test, A/B test) rather than engineering milestones. This shifts focus from delivery to learning and builds confidence incrementally.
**Framework:** GIST
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Itamar emphasizes that steps should be learning milestones, not just engineering tasks, to grow confidence and evidence.

### Insight: If a team is very delivery-focused, start by creating a 'step backlog' of valida...
**Claim:** If a team is very delivery-focused, start by creating a 'step backlog' of validation steps (betas, previews) instead of a product backlog. This changes the dynamic from being told what to build to discovering what to build.
**Framework:** GIST
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** itamar-gilad
**Context:** Itamar suggests starting with a step backlog for teams that are too delivery-focused to break the top-down dynamic.

### Insight: Use metrics trees, mission, and team missions to populate OKRs, with a process o...
**Claim:** Use metrics trees, mission, and team missions to populate OKRs, with a process of top-down, bottom-up, and side-to-side alignment. Include supplementary OKRs for health metrics.
**Framework:** OKRs
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.75
**Source:** itamar-gilad
**Context:** Itamar explains how OKRs connect to the GIST framework, using metrics trees and missions to define objectives.

### Insight: Instead of a product backlog, create a step backlog of validation steps, betas, ...
**Claim:** Instead of a product backlog, create a step backlog of validation steps, betas, and previews to break the dynamic of stakeholders telling teams how to build.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** itamar-gilad
**Context:** Discussion on breaking stakeholder-driven development dynamics

### Insight: Ask candidates to design something for a niche audience (e.g., navigation system...
**Claim:** Ask candidates to design something for a niche audience (e.g., navigation system for elderly) to assess customer empathy, creativity, idea evaluation, and ability to find flaws.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Favorite interview question to ask candidates

### Insight: Strive not to be a success, but to be of value (attributed to Albert Einstein). ...
**Claim:** Strive not to be a success, but to be of value (attributed to Albert Einstein). This motto guides product and company decisions.
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.85
**Source:** itamar-gilad
**Context:** Favorite life motto shared by guest

### Insight: Use ElevenLabs to replicate your own voice for narrating audiobooks or online co...
**Claim:** Use ElevenLabs to replicate your own voice for narrating audiobooks or online courses.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Favorite product recently discovered

### Insight: Read books by Silicon Valley Product Group (INSPIRED, EMPOWERED, TRANSFORMED) an...
**Claim:** Read books by Silicon Valley Product Group (INSPIRED, EMPOWERED, TRANSFORMED) and the Lean series (Lean Startup, Lean Enterprise, Lean Analytics, Running Lean) for product management.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** itamar-gilad
**Context:** Books recommended most to others
