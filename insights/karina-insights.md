# Karina — Insights

*Extracted from podcast appearances.*

### Insight: Model training is more an art than a science, and data quality is one of the mos...
**Claim:** Model training is more an art than a science, and data quality is one of the most important things in model training.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion about how models are created and common misunderstandings.

### Insight: Debugging models is very similar to debugging software; you need to balance trad...
**Claim:** Debugging models is very similar to debugging software; you need to balance trade-offs between making the model helpful and not harmful.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Example of model confusion when taught it has no physical body but also function calls like setting an alarm.

### Insight: The scaling in post-training via reinforcement learning is not hitting a wall be...
**Claim:** The scaling in post-training via reinforcement learning is not hitting a wall because there are infinite tasks to teach the model.
**Audience:** investor | **Actionability:** 5/10 | **Confidence:** 0.85
**Source:** karina-nguyen
**Context:** Discussion about synthetic data and whether models will stop getting smarter.

### Insight: Creative thinking and aesthetic/visual design skills are hard to teach models an...
**Claim:** Creative thinking and aesthetic/visual design skills are hard to teach models and will remain valuable.
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Answer to what skills will be most valuable for product teams going forward.

### Insight: Pre-trained models learn to compress knowledge and model the world, not just mem...
**Claim:** Pre-trained models learn to compress knowledge and model the world, not just memorize data.
**Audience:** general | **Actionability:** 4/10 | **Confidence:** 0.85
**Source:** karina-nguyen
**Context:** Explanation of why the 'data wall' may not be a problem.

### Insight: The scaling in post-training is not hitting the wall because we can generate inf...
**Claim:** The scaling in post-training is not hitting the wall because we can generate infinite tasks via reinforcement learning, making models super intelligent.
**Audience:** investor | **Actionability:** 3/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on o1 series and post-training scaling

### Insight: The bottleneck is in evaluations; benchmarks like GPQA are saturating, so we nee...
**Claim:** The bottleneck is in evaluations; benchmarks like GPQA are saturating, so we need new frontier evals.
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on benchmarks hitting the wall

### Insight: Synthetic data training is useful for rapid model iteration for similar product ...
**Claim:** Synthetic data training is useful for rapid model iteration for similar product outcomes, but human data is still needed for hard tasks requiring expert knowledge.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on synthetic vs human data

### Insight: For Canvas, we identified three core behaviors: triggering Canvas appropriately,...
**Claim:** For Canvas, we identified three core behaviors: triggering Canvas appropriately, updating documents with targeted edits, and making comments on documents.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on how Canvas was built with synthetic training

### Insight: To teach the model to update documents, we had to teach it to find specific sect...
**Claim:** To teach the model to update documents, we had to teach it to find specific sections and edit them, and we biased towards rewrites initially because quality was higher.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on teaching model to edit documents

### Insight: We used o1 to generate synthetic training data for comments by having it produce...
**Claim:** We used o1 to generate synthetic training data for comments by having it produce a document and then inject a user prompt to critique it.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on synthetic data generation for comments

### Insight: Product managers can create spreadsheets with current vs ideal behavior, and o1 ...
**Claim:** Product managers can create spreadsheets with current vs ideal behavior, and o1 can use that to teach itself good behavior.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on how product teams can create evals

### Insight: Prompting is a new way of product development or prototyping for designers and f...
**Claim:** Prompting is a new way of product development or prototyping for designers and for product managers.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** karina-nguyen
**Context:** Karina describes how she prototyped the file uploads feature at Anthropic by prompting the model in her local browser, which led to a successful demo and API request.

### Insight: To design a new AI feature, you start by prototyping the desired behavior via pr...
**Claim:** To design a new AI feature, you start by prototyping the desired behavior via prompting, then extract the information the model needs (e.g., time, action) and design a JSON schema for the tool.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Karina explains the design process for the tasks feature: starting with a prompted prototype, then defining the tool spec and JSON schema.

### Insight: Relying purely on synthetic data for training is more scalable and cheaper than ...
**Claim:** Relying purely on synthetic data for training is more scalable and cheaper than collecting human data; you sample from the model to teach core behaviors, which generalizes to diverse coverage.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** karina-nguyen
**Context:** Karina discusses using synthetic data for evals and training, noting it's less than half the cost and scalable.

### Insight: When launching a beta feature, you learn from user behavior and shift your synth...
**Claim:** When launching a beta feature, you learn from user behavior and shift your synthetic data distribution to match real usage, improving the feature for GA.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Karina describes the feedback loop from beta to GA for Canvas and tasks.

### Insight: The most robust evals are those where prompted baselines get the lowest score, s...
**Claim:** The most robust evals are those where prompted baselines get the lowest score, so that a trained model can hill-climb on that eval without regressing on other intelligence evals.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** karina-nguyen
**Context:** Karina explains how to measure model progress with evals, emphasizing the importance of avoiding 'brain damage' in other areas.

### Insight: Product development is shifting from 'here's a spec PRD, let's build it' to 'AI,...
**Claim:** Product development is shifting from 'here's a spec PRD, let's build it' to 'AI, build this thing for me and here's what correct looks like,' with PMs spending time on defining evals.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Lenny summarizes the shift in product development based on conversations, and Karina agrees.

### Insight: For features like tasks, the timeline from zero to one can be as short as two mo...
**Claim:** For features like tasks, the timeline from zero to one can be as short as two months, while more complex features like Canvas take four to five months.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** karina-nguyen
**Context:** Karina shares the development timelines for tasks and Canvas at OpenAI.

### Insight: The cost of reasoning and intelligence is drastically going down; small models a...
**Claim:** The cost of reasoning and intelligence is drastically going down; small models are becoming smarter than large models due to distillation research, making AI more accessible and unblocking work bottlenecked by intelligence.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on trends in AI cost reduction and model distillation.

### Insight: Build product ideas such that by the time models are really good, the product wi...
**Claim:** Build product ideas such that by the time models are really good, the product will work well; iterate fast, listen to users, and invent new ways of training models.
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.85
**Source:** karina-nguyen
**Context:** Advice on building for the future and iterating quickly.

### Insight: Creative thinking, listening to users, and rapidly iterating are key skills that...
**Claim:** Creative thinking, listening to users, and rapidly iterating are key skills that AI will not replace; focus on building great experiences for specific users.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on valuable skills for product teams.

### Insight: AI research progress is bottlenecked by research management, prioritization, and...
**Claim:** AI research progress is bottlenecked by research management, prioritization, and communication; people skills like empathy and collaboration remain crucial.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** karina-nguyen
**Context:** Reflection on what makes AI research progress and the importance of management.

### Insight: Education will have massive implications as people can learn almost anything fro...
**Claim:** Education will have massive implications as people can learn almost anything from AI models, such as new languages or building apps.
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.85
**Source:** karina-nguyen
**Context:** Discussion on the impact of AI on education.

### Insight: AI is not yet good at creativity, aesthetics, or high-quality writing; these are...
**Claim:** AI is not yet good at creativity, aesthetics, or high-quality writing; these areas remain human strengths.
**Audience:** general | **Actionability:** 4/10 | **Confidence:** 0.8
**Source:** karina-nguyen
**Context:** Comparison of AI capabilities vs human creativity.

### Insight: Models struggle with creative writing and design discrimination because there ar...
**Claim:** Models struggle with creative writing and design discrimination because there aren't enough people with high taste and creativity to teach them.
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion on why AI writing and design quality is lacking; Karina attributes it to lack of expert training data.

### Insight: Strategy is something AI will become great at because it can aggregate user feed...
**Claim:** Strategy is something AI will become great at because it can aggregate user feedback, internal metrics, and other inputs to create plans and recommendations.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Lenny asks if AI can take over strategy; Karina agrees and gives example of Canvas using AI to summarize top pain points.

### Insight: The most valuable human skills to focus on are soft skills like creativity, mana...
**Claim:** The most valuable human skills to focus on are soft skills like creativity, managing influence, collaboration, and pattern recognition.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Lenny summarizes the thread and Karina agrees, adding that organizing teams effectively is key.

### Insight: Anthropic's culture emphasizes craft and curation of model behavior, leading to ...
**Claim:** Anthropic's culture emphasizes craft and curation of model behavior, leading to Claude's distinct personality, while OpenAI is more innovative and risk-taking with bottoms-up product freedom.
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Karina compares her experiences at Anthropic and OpenAI, noting differences in prioritization and innovation.

### Insight: Early prototypes like Claude in Slack allowed for rapid iteration and learning a...
**Claim:** Early prototypes like Claude in Slack allowed for rapid iteration and learning about prompting, and features like weekly channel summaries were valuable form factors.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Karina recalls early Anthropic days and the Slack integration, which was sunset but had potential.

### Insight: The next paradigm shift in AI is moving from synchronous real-time answers to as...
**Claim:** The next paradigm shift in AI is moving from synchronous real-time answers to asynchronous agents that build trust over time and learn user preferences.
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Karina discusses the need for new product experiences for o-series models and the importance of trust and collaboration.

### Insight: The model's ability to operate a computer via pixels is still very hard because ...
**Claim:** The model's ability to operate a computer via pixels is still very hard because visual perception is not as scalable as language.
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion about the difficulty of building agents that control a computer, operating on pixels instead of language.

### Insight: Deriving human intent correctly is a key challenge: the model must know when to ...
**Claim:** Deriving human intent correctly is a key challenge: the model must know when to ask follow-up questions vs. complete the task, and teaching it people skills is hard.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Discussion about the challenges of building agents that can complete tasks on a virtual computer.

### Insight: A product idea: pair programming with a model that can talk to you, draw specifi...
**Claim:** A product idea: pair programming with a model that can talk to you, draw specific sections of code, and teach you in different modes.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** karina-nguyen
**Context:** Karina expresses desire for a pair programming product where the model can operate the computer and teach.

### Insight: Content transformation across media (e.g., sci-fi story to audiobook) is a compe...
**Claim:** Content transformation across media (e.g., sci-fi story to audiobook) is a compelling use case, inspired by Westworld where writing a story generates a 3D virtual reality on the fly.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** karina-nguyen
**Context:** Discussion about transforming content from one media to another, with a specific example from Westworld.

### Insight: Chat as an interface scales well with increasingly intelligent models because it...
**Claim:** Chat as an interface scales well with increasingly intelligent models because it is flexible and social, similar to human conversation.
**Audience:** general | **Actionability:** 4/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Lenny and Karina discuss how chat remains a powerful paradigm for interacting with AI as models get smarter.

### Insight: The 'tasks' feature is a general feature that will scale nicely as models develo...
**Claim:** The 'tasks' feature is a general feature that will scale nicely as models develop new capabilities, such as better searches, creative writing, and generating HTML apps.
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** karina-nguyen
**Context:** Karina explains how tasks can scale with model improvements, enabling daily puzzles or continuing stories.

### Insight: A simulated persona of an expert (e.g., Sam Altman) could provide technical ment...
**Claim:** A simulated persona of an expert (e.g., Sam Altman) could provide technical mentorship or answer questions, similar to Lennybot trained on podcast and newsletter content.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** karina-nguyen
**Context:** Discussion about computer use agents and the idea of simulating a persona for mentorship or Q&A.

### Insight: You can apply for roles on Karina's team by DMing her on Twitter or emailing her...
**Claim:** You can apply for roles on Karina's team by DMing her on Twitter or emailing her via her website, even if no formal job description is posted yet.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** karina-nguyen
**Context:** Karina Nguyen mentions she is hiring for research engineers, research scientists, and machine learning engineers, and that the best way to apply is to DM her on Twitter.

### Insight: Karina's team, Frontier Product Research, trains models and develops new methods...
**Claim:** Karina's team, Frontier Product Research, trains models and develops new methods for product-oriented outcomes, offering a unique blend of research and product engineering.
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** karina-nguyen
**Context:** Karina describes her team's focus on training models and developing methods for product outcomes.

### Insight: Listeners can find Karina on Twitter at KarinaNguyen and email her via her websi...
**Claim:** Listeners can find Karina on Twitter at KarinaNguyen and email her via her website for follow-ups.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** karina-nguyen
**Context:** Karina provides her contact information at the end of the conversation.
