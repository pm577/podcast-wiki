# Chip Huyen — Insights

*Extracted from podcast appearances.*

## Insight 1: Talking to users and understanding their feedback improves AI applications far m...
**Claim:** Talking to users and understanding their feedback improves AI applications far more than keeping up with the latest AI news or adopting new frameworks.
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Discussion on what actually improves AI apps vs what people think improves them.

## Insight 2: Managers prefer an extra headcount over expensive AI coding agent subscriptions,...
**Claim:** Managers prefer an extra headcount over expensive AI coding agent subscriptions, while executives prefer AI assistants because they care about broader productivity metrics.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on measuring productivity and the value of AI tools.

## Insight 3: When choosing between technologies, first estimate how much improvement you get ...
**Claim:** When choosing between technologies, first estimate how much improvement you get from optimal vs non-optimal solutions; if the difference is small, don't spend time debating.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Advice on choosing between technologies like MCP vs agent-to-agent protocol.

## Insight 4: If adopting a new technology would be hard to switch out later and hasn't been w...
**Claim:** If adopting a new technology would be hard to switch out later and hasn't been widely tested, think twice before committing to it.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on the risks of adopting new, unproven technologies.

## Insight 5: Supervised fine-tuning uses demonstration data from human experts or distillatio...
**Claim:** Supervised fine-tuning uses demonstration data from human experts or distillation from stronger models to train a model to emulate desired outputs.
**Framework:** Supervised Fine-Tuning
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Explanation of pre-training vs post-training and fine-tuning.

## Insight 6: Distillation from a strong model to a smaller model is different from training a...
**Claim:** Distillation from a strong model to a smaller model is different from training a model to output like the strong model; it's a big step.
**Framework:** Distillation
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Discussion on open-source models using distillation.

## Insight 7: Language modeling encodes statistical information about language; for example, p...
**Claim:** Language modeling encodes statistical information about language; for example, predicting the next word in a sentence based on probability.
**Audience:** general | **Actionability:** 3/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Explanation of how language models work at a basic level.

## Insight 8: Post-training is where frontier labs are spending most of their energy now, beca...
**Claim:** Post-training is where frontier labs are spending most of their energy now, because pre-training data is maxed out and post-training is where they can differentiate.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on pre-training vs post-training and current industry focus

## Insight 9: Sampling strategy is extremely important and underrated; it can boost performanc...
**Claim:** Sampling strategy is extremely important and underrated; it can boost performance significantly by controlling whether the model picks the most likely token or something more creative.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Explanation of language modeling and token prediction

## Insight 10: Human feedback for reinforcement learning is easier to collect via comparisons (...
**Claim:** Human feedback for reinforcement learning is easier to collect via comparisons (e.g., which response is better) rather than absolute scores, because humans are better at relative judgments.
**Framework:** RLHF
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on reinforcement learning with human feedback

## Insight 11: Verifiable rewards (e.g., math problems with known answers) are a big trend in r...
**Claim:** Verifiable rewards (e.g., math problems with known answers) are a big trend in reinforcement learning, as they provide an automatic signal without human labor.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on different ways to collect signals for reinforcement learning

## Insight 12: There is a massive need for domain expert data (e.g., accounting, physics, legal...
**Claim:** There is a massive need for domain expert data (e.g., accounting, physics, legal) to train models for specific tasks, creating an economic opportunity for data labeling startups.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on domain-specific model training and data needs

## Insight 13: Tokenization splits words into subword units (e.g., 'podcasting' into 'podcast' ...
**Claim:** Tokenization splits words into subword units (e.g., 'podcasting' into 'podcast' and 'ing') to balance vocabulary size between characters and full words.
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Explanation of tokenization in language models

## Insight 14: Data labeling companies are heavily dependent on a few frontier labs, which give...
**Claim:** Data labeling companies are heavily dependent on a few frontier labs, which gives those labs pricing leverage. This creates an uneasy economic dynamic for the data providers.
**Audience:** investor | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion about the economics of data labeling companies and their dependence on a small number of frontier labs.

## Insight 15: For AI products, you don't need perfect evals; you just need to be good enough a...
**Claim:** For AI products, you don't need perfect evals; you just need to be good enough and consistent. The decision to invest in evals depends on ROI: if the expected improvement is small, it may be better to focus on new features.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Debate on whether evals are necessary for AI products; Chip explains that many companies succeed with vibe checks and incremental improvements.

## Insight 16: Evals are critical when operating at scale or when failures can have catastrophi...
**Claim:** Evals are critical when operating at scale or when failures can have catastrophic consequences. In such cases, you need to be 'tyrannical' about understanding failure modes.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip discussing when evals become essential: at scale or high-risk applications.

## Insight 17: Evals should guide product development by uncovering opportunities. For example,...
**Claim:** Evals should guide product development by uncovering opportunities. For example, poor performance on a specific user segment can reveal a messaging issue.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Chip explaining the purpose of evals: to identify areas for improvement.

## Insight 18: Complex AI applications like deep research require multiple evals at each step (...
**Claim:** Complex AI applications like deep research require multiple evals at each step (e.g., search query diversity, result relevance, coverage) rather than a single end-to-end metric.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip using deep research as an example to illustrate the need for granular evals.

## Insight 19: The number of evals needed depends on the product's complexity and the confidenc...
**Claim:** The number of evals needed depends on the product's complexity and the confidence required. Some products have hundreds of metrics to ensure coverage.
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Chip noting that some products have hundreds of evals, but the number should be driven by need.

## Insight 20: Data preparation is the biggest performance driver for RAG solutions, not the ch...
**Claim:** Data preparation is the biggest performance driver for RAG solutions, not the choice of vector database.
**Framework:** RAG
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on RAG and data preparation

## Insight 21: Chunk size in RAG matters: too large chunks limit retrieval diversity, too small...
**Claim:** Chunk size in RAG matters: too large chunks limit retrieval diversity, too small chunks may lack relevant context.
**Framework:** RAG
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on chunk design

## Insight 22: Adding contextual information like summaries, metadata, or hypothetical question...
**Claim:** Adding contextual information like summaries, metadata, or hypothetical questions to chunks improves retrieval.
**Framework:** RAG
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on data processing techniques

## Insight 23: Rewriting data into question-answer format (e.g., for podcasts) can significantl...
**Claim:** Rewriting data into question-answer format (e.g., for podcasts) can significantly improve RAG performance.
**Framework:** RAG
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Example of data processing for podcasts

## Insight 24: Documentation written for humans often lacks context needed for AI; adding an an...
**Claim:** Documentation written for humans often lacks context needed for AI; adding an annotation layer for AI can improve retrieval.
**Framework:** RAG
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Example of documentation for AI

## Insight 25: Customer-facing AI applications (e.g., booking chatbots) have clearer outcomes a...
**Claim:** Customer-facing AI applications (e.g., booking chatbots) have clearer outcomes and are easier to adopt than internal productivity tools.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Discussion on AI tool adoption in companies

## Insight 26: Internal AI tool adoption is tricky; companies invest in subscriptions and upski...
**Claim:** Internal AI tool adoption is tricky; companies invest in subscriptions and upskilling but usage may be low.
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Discussion on internal AI tool adoption challenges

## Insight 27: Measuring productivity from AI tools is very difficult; number of PRs or lines o...
**Claim:** Measuring productivity from AI tools is very difficult; number of PRs or lines of code are not good metrics.
**Audience:** operator | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on challenges of measuring AI tool impact on productivity.

## Insight 28: Managers prefer headcount over AI subscriptions for their teams, but executives ...
**Claim:** Managers prefer headcount over AI subscriptions for their teams, but executives prefer AI tools because they care about business metrics.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Comparison of manager vs. executive preferences for AI tools vs. headcount.

## Insight 29: In a randomized trial, highest-performing engineers got the biggest productivity...
**Claim:** In a randomized trial, highest-performing engineers got the biggest productivity boost from AI coding tools, followed by average performers, while lowest performers got the least benefit.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Example of a company that did a three-bucket test with Cursor.

## Insight 30: Some senior engineers are resistant to using AI tools because they have high sta...
**Claim:** Some senior engineers are resistant to using AI tools because they have high standards and find AI code quality lacking.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Contrasting reports on senior engineer adoption of AI tools.

## Insight 31: Companies are restructuring engineering orgs to have senior engineers focus on p...
**Claim:** Companies are restructuring engineering orgs to have senior engineers focus on peer review and process, while junior engineers produce code with AI.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Discussion on future engineering org structure with AI.

## Insight 32: CS is about system thinking and problem solving, not just coding; these skills w...
**Claim:** CS is about system thinking and problem solving, not just coding; these skills will remain important even as AI automates more.
**Audience:** general | **Actionability:** 4/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Quote from Professor Mehran Sahami on CS education.

## Insight 33: AI tools are good for well-defined tasks but struggle with complex tasks requiri...
**Claim:** AI tools are good for well-defined tasks but struggle with complex tasks requiring interaction with large codebases or debugging.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Personal experience using AI for deployment and debugging.

## Insight 34: When debugging AI systems, focus on understanding how different components work ...
**Claim:** When debugging AI systems, focus on understanding how different components work together and where the source of issue might come from, rather than just trying to fix things from a different component.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion about debugging a hosting service issue where the problem was a tier limitation, not a code bug.

## Insight 35: AI engineers use existing models to build products, while ML engineers build mod...
**Claim:** AI engineers use existing models to build products, while ML engineers build models themselves. This distinction lowers the entry barrier for building AI products.
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Comparison between ML engineer and AI engineer roles.

## Insight 36: Eval is a system problem that requires looking into different components, how th...
**Claim:** Eval is a system problem that requires looking into different components, how they interact, and user behaviors. It should not be owned by a separate team but requires close collaboration between product, engineering, and marketing teams.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on organizational structure and who should own eval and metrics.

## Insight 37: Organizations are restructuring to bring previously distinct functions (engineer...
**Claim:** Organizations are restructuring to bring previously distinct functions (engineering, product, marketing) closer together due to the need for cross-functional collaboration in AI product development.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Predictions about organizational changes in the next few years.

## Insight 38: Base model performance improvement is slowing down; future gains will come from ...
**Claim:** Base model performance improvement is slowing down; future gains will come from post-training and application building phases, not from larger pre-trained models.
**Audience:** investor | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Discussion on the trajectory of AI model improvements.

## Insight 39: Voice AI presents unique challenges beyond text, including latency, natural inte...
**Claim:** Voice AI presents unique challenges beyond text, including latency, natural interruption handling, and regulation around disclosure. These are engineering challenges, not just AI model problems.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion on multimodal AI and voice chatbot difficulties.

## Insight 40: AI is automating outsourced functions, leading to restructuring of engineering o...
**Claim:** AI is automating outsourced functions, leading to restructuring of engineering orgs and rethinking the value of junior vs. senior engineers.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Discussion on automation and organizational restructuring.

## Insight 41: Pay attention to frustrations in your daily workflow and build micro-tools to ad...
**Claim:** Pay attention to frustrations in your daily workflow and build micro-tools to address them, using AI to quickly create solutions.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** chip-huyen
**Context:** Chip Huyen and Lenny Rachitsky discuss how to come up with ideas for building with AI, suggesting noticing frustrations and building small tools to solve them.

## Insight 42: Use test-time compute strategies like generating multiple answers and selecting ...
**Claim:** Use test-time compute strategies like generating multiple answers and selecting the best one, or allowing the model to 'think' longer by generating more tokens, to improve performance without changing the base model.
**Framework:** Test-time compute
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Chip Huyen explains test-time compute as a way to allocate more compute during inference to improve performance, e.g., by generating multiple answers and picking the best.

## Insight 43: Organize hackathons or internal challenges to let employees come up with AI use ...
**Claim:** Organize hackathons or internal challenges to let employees come up with AI use cases, but also provide guidelines on how to generate ideas, such as tracking frustrations over a week.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** chip-huyen
**Context:** Chip Huyen discusses the debate between top-down vs bottom-up AI strategy and shares that many people struggle to come up with ideas, so she provides a method to generate ideas by noticing frustrations.

## Insight 44: The current lack of good voice assistants at home is a notable gap; improving vo...
**Claim:** The current lack of good voice assistants at home is a notable gap; improving voice interaction, especially handling interruptions, is a key area for investment.
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Chip Huyen expresses surprise that better voice assistants aren't available yet, and Lenny agrees that improvements in handling interruptions are needed.

## Insight 45: Reading books like 'The Selfish Gene' and 'From Third World to First' can change...
**Claim:** Reading books like 'The Selfish Gene' and 'From Third World to First' can change how you think about systems, evolution, and policy, providing valuable perspectives for building and leading.
**Audience:** general | **Actionability:** 3/10 | **Confidence:** 0.7
**Source:** chip-huyen
**Context:** Chip Huyen recommends these books as ones that changed her worldview, discussing how they influenced her thinking on procreation and nation-building.

## Insight 46: In the end, nothing really matters. In a billion years, none of us would ever ex...
**Claim:** In the end, nothing really matters. In a billion years, none of us would ever exist. So whatever messy things we do or how bad we do it, no one would remember. It's liberating because it allows you to just try things out.
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Discussion about life motto when dealing with hard things

## Insight 47: Creative writing is about predicting the user's reactions, just like content cre...
**Claim:** Creative writing is about predicting the user's reactions, just like content creation or launching a product.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Answering what she learned from writing a novel

## Insight 48: When writing a story, you need to care about the emotional journey of the reader...
**Claim:** When writing a story, you need to care about the emotional journey of the reader: have a hook to continue reading, but not too much drama to avoid emotional exhaustion.
**Framework:** Emotional journey
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Learning from an editor about emotional journey in storytelling

## Insight 49: For a novel, people care about character likeability. To make a character more l...
**Claim:** For a novel, people care about character likeability. To make a character more likable, put in some vulnerability so readers can relate.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** chip-huyen
**Context:** Feedback from a friend that the character was unlikeable, leading to revisions

## Insight 50: Technical writing focuses entirely on content and argument, and is impersonal. C...
**Claim:** Technical writing focuses entirely on content and argument, and is impersonal. Creative writing requires understanding the emotional bit, how users feel about the story and characters.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** chip-huyen
**Context:** Comparing technical writing to creative writing
