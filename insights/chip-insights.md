# Chip — Insights

*Extracted from podcast appearances.*

### Insight: Talking to users and understanding their needs is more important for improving A...
**Claim:** Talking to users and understanding their needs is more important for improving AI apps than staying up to date with the latest AI news or adopting the newest frameworks.
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Discussion on why the viral table resonated and what actually improves AI apps.

### Insight: When choosing between technologies (e.g., MCP vs. agent-to-agent protocol), firs...
**Claim:** When choosing between technologies (e.g., MCP vs. agent-to-agent protocol), first assess how much improvement the optimal solution provides over a non-optimal one; if the difference is small, don't spend time debating.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip advising on how to evaluate new technologies without overcommitting.

### Insight: Before adopting a new technology, consider how hard it would be to switch away f...
**Claim:** Before adopting a new technology, consider how hard it would be to switch away from it later; if it's untested and would lock you in, think twice.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip's advice on avoiding overcommitment to unproven technologies.

### Insight: Managers at different levels value AI tools differently: line managers prefer he...
**Claim:** Managers at different levels value AI tools differently: line managers prefer headcount over AI subscriptions, while executives prefer AI assistants because they care about broader productivity metrics.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Chip's observation on how productivity measurement varies by management level.

### Insight: Supervised fine-tuning uses demonstration data from human experts to train a mod...
**Claim:** Supervised fine-tuning uses demonstration data from human experts to train a model to emulate desired responses; distillation uses outputs from a strong model instead of human data.
**Framework:** supervised fine-tuning, distillation
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Explanation of post-training techniques like supervised fine-tuning and distillation.

### Insight: Pre-training is about encoding statistical information about language by predict...
**Claim:** Pre-training is about encoding statistical information about language by predicting the next token, which allows the model to learn patterns from vast amounts of text.
**Audience:** general | **Actionability:** 4/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Lenny's simplified explanation of pre-training and Chip's confirmation.

### Insight: Sampling strategy is extremely important and underrated; it can boost performanc...
**Claim:** Sampling strategy is extremely important and underrated; it can boost performance in a huge way.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on how language models predict next token and the importance of sampling strategy for creativity vs. determinism.

### Insight: Post-training is where frontier labs are spending most energy now because pre-tr...
**Claim:** Post-training is where frontier labs are spending most energy now because pre-training data is maxed out on internet text, and post-training differentiates models.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Comparison of pre-training vs. post-training and where the industry focus is shifting.

### Insight: Human feedback for RLHF is more reliable when using comparisons (e.g., which res...
**Claim:** Human feedback for RLHF is more reliable when using comparisons (e.g., which response is better) rather than absolute scores.
**Framework:** RLHF
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Explanation of how human feedback is collected for reinforcement learning.

### Insight: Verifiable rewards (e.g., math problems with correct answers) are a big trend fo...
**Claim:** Verifiable rewards (e.g., math problems with correct answers) are a big trend for training models without human feedback.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on different ways to get signals for reinforcement learning: human feedback, AI feedback, verifiable rewards.

### Insight: Domain-specific expert data (e.g., accounting, legal, engineering) is in high de...
**Claim:** Domain-specific expert data (e.g., accounting, legal, engineering) is in high demand for fine-tuning models, creating economic opportunities for data providers.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Discussion on the need for expert data to train models on specific tasks and the lopsided economics between frontier labs and data startups.

### Insight: Tokenization splits words into subword units (e.g., 'podcasting' into 'podcast' ...
**Claim:** Tokenization splits words into subword units (e.g., 'podcasting' into 'podcast' and 'ing') to balance vocabulary size between characters and words.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Explanation of tokens as a middle ground between characters and words for language modeling.

### Insight: Data labeling companies can have massive AR but are heavily dependent on two or ...
**Claim:** Data labeling companies can have massive AR but are heavily dependent on two or three frontier lab customers, giving them little pricing leverage.
**Audience:** investor | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion about the lopsided economics of data providers vs frontier labs

### Insight: For AI products, you don't need perfect evals to win; being good enough and cons...
**Claim:** For AI products, you don't need perfect evals to win; being good enough and consistent is often sufficient, and the ROI of building evals may be lower than adding new features.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Debate on whether evals are necessary for AI apps

### Insight: Evals are critical when operating at scale where failures can have catastrophic ...
**Claim:** Evals are critical when operating at scale where failures can have catastrophic consequences, and for core competitive features you need rigorous evaluation.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on when evals are important

### Insight: The number of evals needed depends on the product; for complex applications like...
**Claim:** The number of evals needed depends on the product; for complex applications like deep research, you may need hundreds of metrics covering each step (e.g., search query diversity, result relevance, depth).
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Example of evaluating a deep research AI application

### Insight: Evals help uncover opportunities by identifying segments where the model perform...
**Claim:** Evals help uncover opportunities by identifying segments where the model performs poorly, guiding product improvements.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on the goal of evals to guide product development

### Insight: For AI products, focus evals on the most common path users take in your product,...
**Claim:** For AI products, focus evals on the most common path users take in your product, not every feature.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Lenny summarizing Chip's point about focusing on core use case

### Insight: For RAG systems, data preparation is more important than the choice of vector da...
**Claim:** For RAG systems, data preparation is more important than the choice of vector database for answer quality.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen discussing RAG performance factors

### Insight: To improve RAG retrieval, add contextual information like summaries, metadata, o...
**Claim:** To improve RAG retrieval, add contextual information like summaries, metadata, or hypothetical questions to chunks.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen explaining data preparation techniques

### Insight: Rewrite documentation or content into question-answer format to improve AI retri...
**Claim:** Rewrite documentation or content into question-answer format to improve AI retrieval performance.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen giving example of data processing for RAG

### Insight: For AI to understand documentation, add an annotation layer that explains contex...
**Claim:** For AI to understand documentation, add an annotation layer that explains context humans take for granted (e.g., what scale values mean).
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen discussing documentation for AI vs humans

### Insight: Customer-facing AI applications (e.g., booking chatbots) have clearer outcomes a...
**Claim:** Customer-facing AI applications (e.g., booking chatbots) have clearer outcomes and are easier to adopt than internal productivity tools.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Chip Huyen comparing internal vs external AI tool adoption

### Insight: To drive internal AI adoption, invest in upskilling and subscriptions, but expec...
**Claim:** To drive internal AI adoption, invest in upskilling and subscriptions, but expect usage to be lower than hoped.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Chip Huyen on internal AI tool adoption challenges

### Insight: Chunk size in RAG is a trade-off: larger chunks contain more context but fewer c...
**Claim:** Chunk size in RAG is a trade-off: larger chunks contain more context but fewer chunks retrieved; smaller chunks allow more diverse retrieval but may lack context.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen explaining chunk size design

### Insight: Companies should run randomized controlled trials (like the 30-40 person enginee...
**Claim:** Companies should run randomized controlled trials (like the 30-40 person engineering team did with Cursor) to measure AI tool impact on productivity, splitting each performance bucket (high, mid, low) into control and treatment groups.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion of a company that gave half of each performance bucket access to Cursor and observed productivity differences.

### Insight: Senior engineers may get the biggest productivity boost from AI coding tools, bu...
**Claim:** Senior engineers may get the biggest productivity boost from AI coding tools, but they can also be the most resistant due to high standards and opinionatedness; companies should tailor adoption strategies accordingly.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Comparison of two companies' reports: one found senior engineers got biggest boost, another found them most resistant.

### Insight: Restructure engineering orgs so senior engineers focus on peer review, process c...
**Claim:** Restructure engineering orgs so senior engineers focus on peer review, process creation, and system thinking, while junior engineers (or AI) produce code, preparing for a future where only a small group of strong engineers is needed.
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Chip Huyen mentions a company that restructured engineering org to have senior engineers more in review and junior engineers produce code.

### Insight: Invest in developing system thinking and problem-solving skills in engineers, as...
**Claim:** Invest in developing system thinking and problem-solving skills in engineers, as AI can automate coding but not the ability to design step-by-step solutions to complex problems.
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Reference to Professor Sahami's view that CS is about system thinking, not just coding, and that problem-solving will never go away.

### Insight: Use AI tools to gain confidence to try new technologies (e.g., hosting services)...
**Claim:** Use AI tools to gain confidence to try new technologies (e.g., hosting services) but be aware that AI struggles with debugging complex interactions across components; human oversight is still needed.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Chip Huyen's personal experience using AI to deploy an app on a new hosting service: AI gave confidence but failed at debugging complex bugs.

### Insight: Measure AI productivity impact by asking executives whether they prefer AI tool ...
**Claim:** Measure AI productivity impact by asking executives whether they prefer AI tool subscriptions or extra headcount; executives tend to choose AI tools, while managers prefer headcount.
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.7
**Source:** chip-huyen
**Context:** Chip Huyen's observation that when asked, managers prefer headcount but VPs/executives prefer AI tools due to different metrics.

### Insight: When debugging, instead of trying random fixes, take a holistic view of how diff...
**Claim:** When debugging, instead of trying random fixes, take a holistic view of how different components work together to identify the true source of the issue.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Chip Huyen describes debugging a hosting service bug by trying various fixes suggested by AI, only to find the issue was a tier limitation not available in her plan.

### Insight: AI engineers use existing models to build products, unlike ML engineers who buil...
**Claim:** AI engineers use existing models to build products, unlike ML engineers who build models themselves, lowering the entry barrier for integrating AI into products.
**Framework:** AI Engineer vs ML Engineer
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen defines the difference between ML engineers and AI engineers, noting that AI engineers leverage pre-built models.

### Insight: Eval is a system problem that requires collaboration between engineering, produc...
**Claim:** Eval is a system problem that requires collaboration between engineering, product, and marketing teams to reflect what users care about.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen discusses how eval ownership is blurring lines between teams, requiring understanding of user behavior and system architecture.

### Insight: Organizations are restructuring by automating outsourced functions with AI, lead...
**Claim:** Organizations are restructuring by automating outsourced functions with AI, leading to a reevaluation of junior vs senior engineer roles.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Chip Huyen observes that companies are using AI to automate previously outsourced tasks, prompting org restructuring.

### Insight: Base model performance improvements may slow down, so focus on post-training and...
**Claim:** Base model performance improvements may slow down, so focus on post-training and application building for significant gains.
**Audience:** investor | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Chip Huyen predicts that future AI progress will come more from post-training and application layers than from base model scaling.

### Insight: Voice AI presents unique challenges like latency, interruption handling, and reg...
**Claim:** Voice AI presents unique challenges like latency, interruption handling, and regulation disclosure, requiring both engineering and AI solutions.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen explains the complexities of voice chatbots, including multiple hops, natural interruption, and disclosure regulations.

### Insight: To generate ideas for AI products, pay attention to frustrations in your daily w...
**Claim:** To generate ideas for AI products, pay attention to frustrations in your daily work for a week and build micro-tools to address them.
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Chip Huyen suggests a method for coming up with ideas: notice frustrations and build something to address them.

### Insight: Use test-time compute by generating multiple answers and selecting the best one ...
**Claim:** Use test-time compute by generating multiple answers and selecting the best one (e.g., majority voting) to improve model performance without changing the base model.
**Framework:** Test-time compute
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen explains test-time compute as a strategy to allocate more compute during inference for better performance.

### Insight: Organize internal hackathons or challenges to let employees come up with AI use ...
**Claim:** Organize internal hackathons or challenges to let employees come up with AI use cases, but also provide guidelines on how to generate ideas.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Chip Huyen discusses the debate between top-down and bottom-up AI strategy and suggests a mixture, including hackathons with idea generation guidelines.

### Insight: Use AI to create micro-tools that solve niche personal problems, as a practical ...
**Claim:** Use AI to create micro-tools that solve niche personal problems, as a practical way to adopt AI and improve productivity.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Lenny Rachitsky and Chip Huyen discuss building small apps to automate personal frustrations, like extracting images from Google Docs.

### Insight: Invest in multimodal experiences, especially improving voice assistant interrupt...
**Claim:** Invest in multimodal experiences, especially improving voice assistant interruption handling, to make AI interactions more natural.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Lenny Rachitsky expresses excitement for ChatGPT voice mode getting better at interruption, and Chip Huyen notes the lack of good voice assistants at home.

### Insight: In the grand scheme of things, nothing really matters; this perspective is liber...
**Claim:** In the grand scheme of things, nothing really matters; this perspective is liberating and allows you to try things out without fear of failure.
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen discussing her life motto when dealing with hard situations.

### Insight: Creative writing helps improve your ability to anticipate what a different type ...
**Claim:** Creative writing helps improve your ability to anticipate what a different type of audience would want to hear and care about.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen explaining why she started creative writing to become a better writer and anticipate audience reactions.

### Insight: When writing a story, consider the emotional journey of the reader: have a hook ...
**Claim:** When writing a story, consider the emotional journey of the reader: have a hook to keep them reading, but avoid too much drama to prevent emotional exhaustion.
**Framework:** emotional journey
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen learning from an editor about how to structure a story's emotional arc.

### Insight: For novels, character likeability is crucial; making a character vulnerable and ...
**Claim:** For novels, character likeability is crucial; making a character vulnerable and relatable can make them more likable.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen receiving feedback that her character was unlikable and revising by adding vulnerability.

### Insight: Content creation is about predicting user reactions; understanding the emotional...
**Claim:** Content creation is about predicting user reactions; understanding the emotional impact on the audience is key.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen comparing writing a novel to launching a product, both require anticipating user engagement.

### Insight: Starting a Substack or YouTube channel on systems thinking and book reviews can ...
**Claim:** Starting a Substack or YouTube channel on systems thinking and book reviews can help build a community and share valuable insights.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen announcing her plans to start a Substack and YouTube channel.
