# Hamelshreya — Insights

*Extracted from podcast appearances.*

### Insight: Evals are a way to systematically measure and improve an AI application, at its ...
**Claim:** Evals are a way to systematically measure and improve an AI application, at its core data analytics on your LLM application.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel defining evals as a systematic measurement and improvement process for AI applications.

### Insight: Before evals, you would be left with guessing; you might fix a prompt and hope y...
**Claim:** Before evals, you would be left with guessing; you might fix a prompt and hope you're not breaking anything else, relying on vibe checks which become unmanageable as the application grows.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel explaining the problem evals solve: moving from guesswork and vibe checks to systematic metrics.

### Insight: Evals help you create metrics to measure how your application is doing and give ...
**Claim:** Evals help you create metrics to measure how your application is doing and give you a way to improve with confidence, providing a feedback signal to iterate against.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel describing the benefit of evals: creating metrics for confident iteration.

### Insight: Evals are a big spectrum of ways to measure application quality; unit tests are ...
**Claim:** Evals are a big spectrum of ways to measure application quality; unit tests are a very small part of that puzzle.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya correcting the unit test metaphor, explaining evals include data analysis, tracking metrics, and finding new cohorts.

### Insight: Evals can be a way of looking at your data regularly to find new cohorts of peop...
**Claim:** Evals can be a way of looking at your data regularly to find new cohorts of people, and metrics to track over time like thumbs up, which feed back into improving your product.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya expanding the definition of evals to include ongoing data analysis and tracking user satisfaction metrics.

### Insight: It's important that we don't think of evals as just tests; there's a common trap...
**Claim:** It's important that we don't think of evals as just tests; there's a common trap that a lot of people fall into.
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** hamelshreya
**Context:** Hamel warning against the narrow view of evals as only tests.

### Insight: Don't think of evals as just tests; start with data analysis to ground what you ...
**Claim:** Don't think of evals as just tests; start with data analysis to ground what you should test, because LLMs are stochastic and have more surface area than traditional software.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel Husain explaining the common trap of jumping straight to tests and advocating for starting with data analysis.

### Insight: Use error analysis on sampled logs (traces) to identify issues: look at data, wr...
**Claim:** Use error analysis on sampled logs (traces) to identify issues: look at data, write notes on the first upstream error you see, and don't try to fix everything at once.
**Framework:** Error analysis
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel demonstrating how to analyze traces from Nurture Boss, writing notes like 'Should have handed off to a human' and 'conversation flow is janky because of text message'.

### Insight: Product people should be involved in error analysis because they understand the ...
**Claim:** Product people should be involved in error analysis because they understand the user experience and can identify when the AI's response is not ideal, even if technically correct.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Lenny and Hamel discussing that product people need to be in the room because the AI interaction is the product.

### Insight: Observability tools (like Braintrust, Phoenix Arize, LangSmith) are essential fo...
**Claim:** Observability tools (like Braintrust, Phoenix Arize, LangSmith) are essential for logging traces of AI applications, including system prompts, tool calls, and user interactions, to enable error analysis.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel showing the trace in Braintrust and mentioning other tools, emphasizing the importance of logging all components.

### Insight: When analyzing traces, focus on the most upstream error first and move on quickl...
**Claim:** When analyzing traces, focus on the most upstream error first and move on quickly; you can sample data and learn a lot without analyzing everything.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel advising to write down the first thing that's wrong and stop, and that you can get good at this quickly.

### Insight: When doing error analysis, focus on the most upstream error first, not all error...
**Claim:** When doing error analysis, focus on the most upstream error first, not all errors at once.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel advises to capture the first thing wrong and move on, rather than trying to fix everything at once.

### Insight: Do not automate the initial error analysis with an LLM; manual review is essenti...
**Claim:** Do not automate the initial error analysis with an LLM; manual review is essential because LLMs lack the domain context to identify subtle errors like hallucinations.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya explains that asking an LLM to analyze traces often results in false positives because it doesn't know the product's actual capabilities.

### Insight: Appoint a single domain expert as a 'benevolent dictator' to perform open coding...
**Claim:** Appoint a single domain expert as a 'benevolent dictator' to perform open coding, rather than a committee, to keep the process fast and tractable.
**Framework:** Benevolent dictator
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel and Shreya discuss that having one person with domain expertise do the note-taking avoids expensive committee delays.

### Insight: Use simple counting and LLM-assisted categorization of open codes to derive insi...
**Claim:** Use simple counting and LLM-assisted categorization of open codes to derive insights after manual note-taking.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel describes uploading a CSV of notes and asking an LLM to create axial codes, leveraging the LLM's knowledge of qualitative analysis terms.

### Insight: Continue analyzing traces until you reach theoretical saturation (no new types o...
**Claim:** Continue analyzing traces until you reach theoretical saturation (no new types of errors emerge), which typically requires at least 100 traces to start.
**Framework:** Theoretical saturation
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya and Hamel recommend doing at least 100 traces, but stop when you stop learning new things.

### Insight: Use axial codes to categorize open codes into failure modes, then identify the m...
**Claim:** Use axial codes to categorize open codes into failure modes, then identify the most prevalent to attack.
**Framework:** Error analysis
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya explains the purpose of axial codes: to cluster failure modes and find the most common ones to fix.

### Insight: When generating axial codes with an LLM, you can customize the prompt to get mor...
**Claim:** When generating axial codes with an LLM, you can customize the prompt to get more actionable categories, e.g., by stage of user story.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya suggests tailoring the prompt to get axial codes that are actionable or grouped by user story stage.

### Insight: After getting AI-generated axial codes, manually refine them to be more specific...
**Claim:** After getting AI-generated axial codes, manually refine them to be more specific and actionable, e.g., change 'capability limitation' to 'tour scheduling issues'.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel shows how he renames generic axial codes to be more actionable, like 'tour scheduling' instead of 'capability limitation'.

### Insight: Use AI to automatically categorize open codes into your refined axial codes, but...
**Claim:** Use AI to automatically categorize open codes into your refined axial codes, but include a 'none of the above' category to catch missing codes.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya recommends using AI for labeling with a 'none of the above' option to identify gaps in axial codes.

### Insight: Open codes must be detailed enough for AI to categorize; avoid vague terms like ...
**Claim:** Open codes must be detailed enough for AI to categorize; avoid vague terms like 'janky' without context.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya emphasizes that open codes need to be detailed for AI to categorize them correctly.

### Insight: This error analysis process is grounded in decades-old social science methods, n...
**Claim:** This error analysis process is grounded in decades-old social science methods, not new invention, so it's reliable.
**Framework:** Error analysis
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya and Hamel explain that open and axial coding come from social science, not something they invented.

### Insight: Use pivot tables to count occurrences of each axial code to identify the most fr...
**Claim:** Use pivot tables to count occurrences of each axial code to identify the most frequent problems in your traces.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel shows a pivot table counting coded traces to reveal top issues like conversational flow problems.

### Insight: For each failure mode, decide whether to fix it directly (e.g., prompt fix) or b...
**Claim:** For each failure mode, decide whether to fix it directly (e.g., prompt fix) or build an automated evaluator, considering cost-benefit trade-off.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Discussion on evaluating whether to write an eval for each error, with examples like formatting errors fixable by prompt changes.

### Insight: Use code-based evals (e.g., Python functions) for simple, deterministic failure ...
**Claim:** Use code-based evals (e.g., Python functions) for simple, deterministic failure modes like checking JSON output or markdown formatting.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya explains code-based evals for checking output format, string content, etc.

### Insight: For complex failure modes, use LLM as a judge with a binary pass/fail output, sc...
**Claim:** For complex failure modes, use LLM as a judge with a binary pass/fail output, scoped to a single specific failure mode.
**Framework:** LLM as a judge
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel and Shreya discuss LLM judge for subjective issues like human handoff, emphasizing binary output and narrow scope.

### Insight: Run LLM judges on production traces for monitoring, not just in CI, to measure r...
**Claim:** Run LLM judges on production traces for monitoring, not just in CI, to measure real-world failure rates daily or hourly.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya suggests sampling 1000 production traces daily and running LLM judge to get specific application quality measures.

### Insight: Avoid using multi-point scales (e.g., 1-7) in LLM judges; use binary pass/fail t...
**Claim:** Avoid using multi-point scales (e.g., 1-7) in LLM judges; use binary pass/fail to make metrics actionable and interpretable.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Hamel and Shreya criticize multi-point scales as 'weasel way' and argue for binary decisions to avoid ambiguous metrics.

### Insight: Don't blindly accept LLM outputs; put yourself in the loop and iterate on prompt...
**Claim:** Don't blindly accept LLM outputs; put yourself in the loop and iterate on prompts.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion on using LLMs to create prompts but emphasizing human review and iteration.

### Insight: Before releasing an LLM as a judge, align it to human judgment by measuring agre...
**Claim:** Before releasing an LLM as a judge, align it to human judgment by measuring agreement against axial codes.
**Framework:** LLM as Judge
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Explaining the process of validating LLM judges against human-labeled data.

### Insight: When evaluating LLM judge agreement, don't rely solely on overall agreement perc...
**Claim:** When evaluating LLM judge agreement, don't rely solely on overall agreement percentage; examine the confusion matrix to identify specific error types.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Warning about misleading agreement metrics and recommending matrix analysis.

### Insight: Product managers should ask for the confusion matrix when someone reports LLM ju...
**Claim:** Product managers should ask for the confusion matrix when someone reports LLM judge agreement to ensure errors are properly addressed.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Advice for product managers to scrutinize eval reports.

### Insight: Evals are like PRDs but automated; they encode product requirements and run cons...
**Claim:** Evals are like PRDs but automated; they encode product requirements and run constantly.
**Framework:** Evals as PRDs
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Lenny's observation that evals serve as automated product requirements documents.

### Insight: You cannot know all failure modes upfront; expectations evolve as you review mor...
**Claim:** You cannot know all failure modes upfront; expectations evolve as you review more outputs, so be flexible and iterate.
**Framework:** Criteria Drift
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Discussion on how criteria drift makes eval development iterative.

### Insight: Limit the number of LLM-as-judge evals to 4-7, focusing only on the most pesky f...
**Claim:** Limit the number of LLM-as-judge evals to 4-7, focusing only on the most pesky failure modes that persist despite prompt improvements.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya's recommendation on how many evals to maintain.

### Insight: After building an LLM judge, use it in unit tests and online monitoring to drive...
**Claim:** After building an LLM judge, use it in unit tests and online monitoring to drive continuous product improvements.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya describes what comes next after building an LLM judge: putting it in unit tests and using it for online monitoring with dashboards.

### Insight: Perform error analysis on real data to discover unexpected failure modes before ...
**Claim:** Perform error analysis on real data to discover unexpected failure modes before designing A/B tests.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya warns against premature A/B tests without error analysis, citing that real errors (like handoff issues) are often not what was hypothesized.

### Insight: Dogfooding is only effective if done at a visceral level with a tight feedback l...
**Claim:** Dogfooding is only effective if done at a visceral level with a tight feedback loop; otherwise it's dangerous.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Hamel cautions that many teams claim to dogfood but don't do it deeply enough to close the feedback loop.

### Insight: Coding agents are fundamentally different from other AI products because develop...
**Claim:** Coding agents are fundamentally different from other AI products because developers are domain experts and can short-circuit evals through dogfooding.
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel explains that coding agents allow collapsing eval activities due to developer expertise, which doesn't generalize to other domains.

### Insight: A/B tests are a form of evals and should be powered by prior error analysis to b...
**Claim:** A/B tests are a form of evals and should be powered by prior error analysis to be effective.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya argues that A/B tests are systematic measurement of quality (evals) and need error analysis to inform what to test.

### Insight: Product managers can build profitable AI products by practicing systematic error...
**Claim:** Product managers can build profitable AI products by practicing systematic error analysis and eval skills.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** hamelshreya
**Context:** Shreya states that product managers are now doing this work and can build very profitable products with this skill set.

### Insight: A/B tests should be powered by actual error analysis, not just hypothetical assu...
**Claim:** A/B tests should be powered by actual error analysis, not just hypothetical assumptions about what is important.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion about A/B testing vs evals, with Hamel emphasizing grounding hypotheses in data.

### Insight: Evals are essentially data science for AI products; the term 'evals' causes conf...
**Claim:** Evals are essentially data science for AI products; the term 'evals' causes confusion, but it's just using analytic tools to understand your product.
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel explaining that evals are not a new concept but data science applied to LLMs.

### Insight: A common misconception is that you can buy a tool that automatically does evals ...
**Claim:** A common misconception is that you can buy a tool that automatically does evals for you; it doesn't work.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel listing top misconceptions about evals.

### Insight: Looking at individual traces (data) is the highest ROI activity; people are ofte...
**Claim:** Looking at individual traces (data) is the highest ROI activity; people are often surprised that you actually look at raw data.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel sharing that in consulting, he always starts by looking at traces and learns a lot.

### Insight: There is no one correct way to do evals; many correct ways exist, but all involv...
**Claim:** There is no one correct way to do evals; many correct ways exist, but all involve error analysis and operationalizing metrics based on product stage and resources.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya adding a third misconception that there's a single correct way.

### Insight: Don't be scared of looking at your data; the goal is actionable improvement, not...
**Claim:** Don't be scared of looking at your data; the goal is actionable improvement, not perfection.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya's tip number one for starting evals.

### Insight: Use LLMs to help organize thoughts and present information, but not to replace y...
**Claim:** Use LLMs to help organize thoughts and present information, but not to replace yourself in the eval process.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya's second tip about using AI to assist but not replace human judgment.

### Insight: Make it as easy as possible to look at your data because it's the highest ROI ac...
**Claim:** Make it as easy as possible to look at your data because it's the highest ROI activity you can engage in. With AI, remove all the friction.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion on automating data analysis and reducing friction to encourage engagement with data.

### Insight: When doing evals, if you see something that's wrong, just go fix it. The whole p...
**Claim:** When doing evals, if you see something that's wrong, just go fix it. The whole point is not to have a beautiful eval suite but to fix your application and make it better.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel Husain emphasizing that evals should lead to immediate fixes in the application.

### Insight: Initial error analysis takes three to four days of intensive work, but after tha...
**Claim:** Initial error analysis takes three to four days of intensive work, but after that, maintaining it takes only about 30 minutes per week.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya Shankar describing the time investment for setting up and maintaining evaluation processes.

### Insight: Put your product hat on and be critical: ask if the AI output is actually good, ...
**Claim:** Put your product hat on and be critical: ask if the AI output is actually good, not just technically correct. For example, a recruiting email that says 'given your background' may be generic and ineffective.
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel Husain's anecdote about evaluating a recruiting email and questioning its quality beyond correctness.

### Insight: Cost-optimization: replace expensive state-of-the-art models with cheaper altern...
**Claim:** Cost-optimization: replace expensive state-of-the-art models with cheaper alternatives (e.g., GPT-5 with 5-nano, 4-mini) for certain uses to save money while maintaining quality.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya Shankar mentioning cost-optimization as a special topic in their course.

### Insight: Use AI-assisted coding tools like Cursor and Claude Code to increase ambition an...
**Claim:** Use AI-assisted coding tools like Cursor and Claude Code to increase ambition and productivity, especially when wearing many hats.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya and Hamel discussing favorite products: Cursor and Claude Code for AI-assisted coding.

### Insight: Adopt the motto 'keep learning in, think like a beginner' to maintain a growth m...
**Claim:** Adopt the motto 'keep learning in, think like a beginner' to maintain a growth mindset.
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel sharing his favorite life motto.

### Insight: When encountering arguments, try to think about the other side's argument with a...
**Claim:** When encountering arguments, try to think about the other side's argument with a generous interpretation to foster collaboration.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya sharing her favorite life motto about considering the other side's argument.

### Insight: Share your successes and case studies with creators to keep them motivated and e...
**Claim:** Share your successes and case studies with creators to keep them motivated and engaged.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya and Hamel asking listeners to share their successes and implementations.

### Insight: Encourage others to teach and write about evals to amplify the community's knowl...
**Claim:** Encourage others to teach and write about evals to amplify the community's knowledge.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel expressing desire for others to teach evals and share blog posts.
