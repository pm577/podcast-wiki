# Hamel Husain — Insights

*Extracted from podcast appearances.*

## Insight 1: Evals are a way to systematically measure and improve an AI application, essenti...
**Claim:** Evals are a way to systematically measure and improve an AI application, essentially data analytics on your LLM application.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel defining evals at the start of the conversation.

## Insight 2: Before evals, you would be left with guessing; you might fix a prompt and hope y...
**Claim:** Before evals, you would be left with guessing; you might fix a prompt and hope you're not breaking anything else. Evals give you a feedback signal to iterate against with confidence.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel explaining the problem evals solve.

## Insight 3: Vibe checks are good initially but become unmanageable as your application grows...
**Claim:** Vibe checks are good initially but become unmanageable as your application grows. Evals help create metrics to measure how your application is doing.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Hamel contrasting vibe checks with systematic evals.

## Insight 4: Evals are a spectrum: unit tests for non-negotiable functionalities, plus measur...
**Claim:** Evals are a spectrum: unit tests for non-negotiable functionalities, plus measuring open-ended tasks and tracking metrics over time.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya expanding on the definition of evals.

## Insight 5: A common misconception is that AI can eval itself; it doesn't work....
**Claim:** A common misconception is that AI can eval itself; it doesn't work.
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel responding to Lenny's question about misconceptions.

## Insight 6: Appoint a benevolent dictator (one person with domain expertise, often the PM) t...
**Claim:** Appoint a benevolent dictator (one person with domain expertise, often the PM) to do open coding rather than a committee, to avoid making the process too expensive.
**Framework:** Benevolent dictator
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Hamel discussing how to avoid getting bogged down in committees.

## Insight 7: The goal of evals is not to do them perfectly, but to actionably improve your pr...
**Claim:** The goal of evals is not to do them perfectly, but to actionably improve your product.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya stating the purpose of evals.

## Insight 8: Don't think of evals as just tests; start with data analysis to ground what you ...
**Claim:** Don't think of evals as just tests; start with data analysis to ground what you should test, because LLMs are stochastic and have a larger surface area than traditional software.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel explaining the common trap of jumping straight to writing tests for LLMs instead of starting with data analysis.

## Insight 9: Use error analysis: sample logs from your LLM application, write informal notes ...
**Claim:** Use error analysis: sample logs from your LLM application, write informal notes about what's wrong, focusing on the first most upstream error per trace.
**Framework:** error analysis
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel demonstrating how to analyze traces from Nurture Boss by writing notes like 'Should have handed off to a human' or 'conversation flow is janky because of text message'.

## Insight 10: Product people must be involved in error analysis because they understand the us...
**Claim:** Product people must be involved in error analysis because they understand the user experience and can identify issues that developers might miss, like an AI ending a lead conversation too early.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel and Lenny discussing that product people need to be in the room for error analysis because it's about user experience.

## Insight 11: Observability tools (like Braintrust, Phoenix Arize, LangSmith) are essential fo...
**Claim:** Observability tools (like Braintrust, Phoenix Arize, LangSmith) are essential for logging traces of LLM interactions, including system prompts, tool calls, and responses, to enable error analysis.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel showing a trace in Braintrust that logs the full interaction, including system prompt and tool calls.

## Insight 12: When doing error analysis, don't try to find all problems in a trace; just write...
**Claim:** When doing error analysis, don't try to find all problems in a trace; just write down the first thing that's wrong and move on to the next trace to stay efficient.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel advising to capture the most upstream error and stop, then move on quickly.

## Insight 13: The most upstream error is the first thing you see that's wrong; capture that an...
**Claim:** The most upstream error is the first thing you see that's wrong; capture that and move on. The first two or three can be painful but you can do them fast.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion on error analysis approach for LLM applications

## Insight 14: Do not automate error analysis with an LLM at the open coding stage because LLMs...
**Claim:** Do not automate error analysis with an LLM at the open coding stage because LLMs lack the context to identify product-level errors like hallucination of features.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Example of LLM hallucinating a virtual tour that doesn't exist

## Insight 15: Appoint a 'benevolent dictator' (a domain expert) to do open coding to avoid com...
**Claim:** Appoint a 'benevolent dictator' (a domain expert) to do open coding to avoid committee slowdown and make the process tractable.
**Framework:** Benevolent dictator
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion on who should perform open coding

## Insight 16: Do at least 100 open coding examples to get signal; stop when you reach theoreti...
**Claim:** Do at least 100 open coding examples to get signal; stop when you reach theoretical saturation (no new types of errors).
**Framework:** Theoretical saturation
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Advice on how many traces to review

## Insight 17: After open coding, use basic counting (e.g., with an LLM) to categorize notes in...
**Claim:** After open coding, use basic counting (e.g., with an LLM) to categorize notes into axial codes for actionable insights.
**Framework:** Axial coding
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Next step after open coding

## Insight 18: Use axial coding to group open codes into failure modes, then identify the most ...
**Claim:** Use axial coding to group open codes into failure modes, then identify the most prevalent to attack that problem.
**Framework:** Axial coding
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya explaining the purpose of axial codes: to cluster failure modes and find the most common one to fix.

## Insight 19: When generating axial codes with an LLM, you can specify that each code should b...
**Claim:** When generating axial codes with an LLM, you can specify that each code should be an actionable failure mode, or group by stage of user story.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya discussing how to customize the prompt for axial code generation to get more actionable categories.

## Insight 20: After getting AI-generated axial codes, iterate on them to make them more specif...
**Claim:** After getting AI-generated axial codes, iterate on them to make them more specific and actionable, e.g., rename 'capability limitation' to something like 'tour scheduling issues'.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel showing how he refined generic axial codes into more specific, actionable ones.

## Insight 21: Use an AI (e.g., Gemini in Google Sheets) to automatically categorize open codes...
**Claim:** Use an AI (e.g., Gemini in Google Sheets) to automatically categorize open codes into your refined axial codes, using a prompt like 'categorize the following note into one of the following categories'.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel demonstrating how to automate categorization of open codes using AI in Google Sheets.

## Insight 22: Include a 'none of the above' category when using AI to label open codes, so you...
**Claim:** Include a 'none of the above' category when using AI to label open codes, so you can identify missing axial codes and iterate.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya suggesting to add 'none of the above' to catch uncategorized issues and improve the taxonomy.

## Insight 23: Open codes must be detailed enough for AI (or humans) to categorize; avoid vague...
**Claim:** Open codes must be detailed enough for AI (or humans) to categorize; avoid vague terms like 'janky' without context.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya emphasizing the need for detailed open codes to enable accurate automatic categorization.

## Insight 24: Error analysis for LLMs is grounded in established social science methods (open ...
**Claim:** Error analysis for LLMs is grounded in established social science methods (open coding, axial coding) and classic ML error analysis, not new inventions.
**Framework:** Error analysis
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya and Hamel explaining that their approach is based on existing theory, not new invention, citing Andrew Ng's eight-year-old video.

## Insight 25: Use pivot tables to count and prioritize failure modes from coded traces, focusi...
**Claim:** Use pivot tables to count and prioritize failure modes from coded traces, focusing on the most frequent or severe issues.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel shows a pivot table of coded traces to identify top problems like conversational flow issues.

## Insight 26: For simple, obvious errors (e.g., formatting), fix the prompt directly rather th...
**Claim:** For simple, obvious errors (e.g., formatting), fix the prompt directly rather than building an eval, but consider a code-based eval if it's cheap to automate.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel discusses cost-benefit trade-off: some errors are easy to fix without evals, but code-based evals can be used for formatting checks.

## Insight 27: Build LLM-as-judge evals only for complex, subjective failure modes where code-b...
**Claim:** Build LLM-as-judge evals only for complex, subjective failure modes where code-based evals are infeasible, and scope them to a single binary pass/fail decision.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya and Hamel explain that LLM judges should evaluate one narrow failure mode with a yes/no output, not a scale.

## Insight 28: Use LLM judges not just in pre-deployment tests but also for ongoing production ...
**Claim:** Use LLM judges not just in pre-deployment tests but also for ongoing production monitoring by sampling traces daily to measure real-world failure rates.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya describes using LLM judges on production traces to get a specific measure of application quality over time.

## Insight 29: Iterate on axial codes by allowing the AI to suggest 'none of the above' to iden...
**Claim:** Iterate on axial codes by allowing the AI to suggest 'none of the above' to identify missing categories and refine the coding scheme.
**Framework:** Axial coding
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Speaker e. explains that AI can flag incomplete axial codes, prompting review of open codes to create new categories.

## Insight 30: Perform the trace analysis and coding process weekly, completing it in about 30 ...
**Claim:** Perform the trace analysis and coding process weekly, completing it in about 30 minutes once established, to continuously improve the product.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya says people do this once a week in 30 minutes, leading to significant product improvements.

## Insight 31: Don't blindly accept LLM judge outputs; measure alignment with human-labeled dat...
**Claim:** Don't blindly accept LLM judge outputs; measure alignment with human-labeled data using a confusion matrix to identify false positives and false negatives.
**Framework:** LLM as Judge
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion on validating LLM judges against human axial codes

## Insight 32: When reporting eval agreement, always ask for the confusion matrix because high ...
**Claim:** When reporting eval agreement, always ask for the confusion matrix because high agreement can be misleading if errors are rare.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Warning about misleading agreement metrics

## Insight 33: Iterate on LLM judge prompts by analyzing misalignment (false positives/negative...
**Claim:** Iterate on LLM judge prompts by analyzing misalignment (false positives/negatives) and clarifying rules to reduce errors.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Process of improving judge prompts after measuring agreement

## Insight 34: Use LLM judges as automated, always-running evals that encode product requiremen...
**Claim:** Use LLM judges as automated, always-running evals that encode product requirements, derived from data and human expectations.
**Framework:** Evals as PRDs
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Comparison of evals to product requirements documents

## Insight 35: Expect to uncover new failure modes only after reviewing actual LLM outputs; you...
**Claim:** Expect to uncover new failure modes only after reviewing actual LLM outputs; you cannot anticipate all issues upfront.
**Framework:** Criteria Drift
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Research finding that criteria evolve as more outputs are reviewed

## Insight 36: Prioritize writing LLM judge evals only for the most pesky and risky failure mod...
**Claim:** Prioritize writing LLM judge evals only for the most pesky and risky failure modes, not for everything.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Advice on focusing eval efforts on high-impact areas

## Insight 37: Use spreadsheets for simple data analysis (e.g., counting errors) to drive impro...
**Claim:** Use spreadsheets for simple data analysis (e.g., counting errors) to drive improvements; it's accessible to everyone.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Demonstration of using spreadsheets to analyze handoff failures

## Insight 38: You can use LLM judges in unit tests and for online monitoring to drive continuo...
**Claim:** You can use LLM judges in unit tests and for online monitoring to drive continuous product improvements.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Discussion on what comes after building an LLM judge: using it in unit tests and online monitoring.

## Insight 39: Dogfooding is a form of eval, but it requires a visceral level of engagement to ...
**Claim:** Dogfooding is a form of eval, but it requires a visceral level of engagement to close the feedback loop; many people claim to dogfood but don't do it effectively.
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Debate on evals, where Hamel warns that dogfooding is often superficial.

## Insight 40: A/B tests are a form of eval, but they should be powered by actual error analysi...
**Claim:** A/B tests are a form of eval, but they should be powered by actual error analysis rather than hypothetical product requirements.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Discussion on the straw man argument of evals vs. A/B tests.

## Insight 41: Coding agents are fundamentally different from other AI products because the dev...
**Claim:** Coding agents are fundamentally different from other AI products because the developer is the domain expert, allowing them to short circuit many eval activities.
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Hamel explaining why coding agents' eval process should look different.

## Insight 42: People have been burned by evals in the past, often due to using a Likert scale ...
**Claim:** People have been burned by evals in the past, often due to using a Likert scale LLM judge that didn't align with expectations, leading to distrust.
**Audience:** general | **Actionability:** 4/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya explaining the controversy around evals and why some are anti-evals.

## Insight 43: Product managers can now build very profitable products by practicing the skill ...
**Claim:** Product managers can now build very profitable products by practicing the skill of systematic error analysis and data analysis.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** hamelshreya
**Context:** Shreya emphasizing that anyone can learn this skill and it's empowering for PMs.

## Insight 44: If you're going to do A-B tests, they should be powered by actual error analysis...
**Claim:** If you're going to do A-B tests, they should be powered by actual error analysis, not just based on hypothetical assumptions about what is important.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion about A-B testing vs. error analysis, with Hamel and Shreya emphasizing grounding hypotheses in data.

## Insight 45: Evals are essentially data science for AI products; you don't need to invent new...
**Claim:** Evals are essentially data science for AI products; you don't need to invent new tools, just apply analytic thinking to understand your product.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel explaining that evals are just data science applied to LLMs, causing confusion.

## Insight 46: A common misconception is that you can buy a tool and it will do evals for you a...
**Claim:** A common misconception is that you can buy a tool and it will do evals for you automatically; this doesn't work.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel listing top misconceptions about evals.

## Insight 47: Looking at individual traces (data) is the highest ROI activity; it always revea...
**Claim:** Looking at individual traces (data) is the highest ROI activity; it always reveals problems and insights.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel and Shreya emphasizing the power of examining actual data traces.

## Insight 48: There is no one correct way to do evals; many correct ways exist, but they all i...
**Claim:** There is no one correct way to do evals; many correct ways exist, but they all involve error analysis.
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya adding a third misconception that there's a single correct method.

## Insight 49: Use LLMs to help organize thoughts and improve product requirements, but not to ...
**Claim:** Use LLMs to help organize thoughts and improve product requirements, but not to replace human judgment.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya's tip to leverage AI for organizing the eval process.

## Insight 50: Create your own custom tools to remove friction from looking at data; AI makes i...
**Claim:** Create your own custom tools to remove friction from looking at data; AI makes it cheap and fast to build simple web apps for annotation and analysis.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel showing a custom tool built for Nurture Boss to facilitate data review.

## Insight 51: The highest ROI activity you can engage in with AI is to make it as easy as poss...
**Claim:** The highest ROI activity you can engage in with AI is to make it as easy as possible to look at your data and remove all friction.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion about automating data analysis and making it frictionless.

## Insight 52: When doing evals, if you see something that's wrong, just go fix it. The whole p...
**Claim:** When doing evals, if you see something that's wrong, just go fix it. The whole point is not to have a beautiful eval suite but to make your application better.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel Husain emphasizing that evals should lead to immediate fixes.

## Insight 53: Initial error analysis takes about three to four days of intensive work, but aft...
**Claim:** Initial error analysis takes about three to four days of intensive work, but after that, maintaining it only takes about 30 minutes per week.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya Shankar describing the time investment for setting up evals.

## Insight 54: Put your product hat on and be critical: ask if the AI output is really good, no...
**Claim:** Put your product hat on and be critical: ask if the AI output is really good, not just technically correct.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel Husain's example of critiquing a recruiting email that was technically correct but generic.

## Insight 55: You can replace expensive state-of-the-art models with cheaper ones (e.g., GPT-4...
**Claim:** You can replace expensive state-of-the-art models with cheaper ones (e.g., GPT-4-mini) for certain tasks to save money while maintaining quality.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya Shankar mentioning cost optimization as a special topic in their course.

## Insight 56: Build custom interfaces for error analysis using tools like Claude Code or Curso...
**Claim:** Build custom interfaces for error analysis using tools like Claude Code or Cursor to quickly iterate on data.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** hamelshreya
**Context:** Shreya Shankar describing live coding interfaces for error analysis.

## Insight 57: Use AI-assisted coding tools like Cursor and Claude Code to increase ambition an...
**Claim:** Use AI-assisted coding tools like Cursor and Claude Code to increase ambition and productivity, especially when wearing multiple hats.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya and Hamel discussing favorite products: Cursor and Claude Code.

## Insight 58: Adopt the motto 'keep learning in, think like a beginner' to maintain a growth m...
**Claim:** Adopt the motto 'keep learning in, think like a beginner' to maintain a growth mindset.
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel sharing his favorite life motto.

## Insight 59: When encountering arguments online, try to think about the other side's argument...
**Claim:** When encountering arguments online, try to think about the other side's argument and assume a generous interpretation to foster collaboration.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya discussing her life motto about considering the other side's argument.

## Insight 60: Share your successes and case studies with creators to keep them motivated and h...
**Claim:** Share your successes and case studies with creators to keep them motivated and help the community learn.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya and Hamel asking listeners to share their successes and case studies.

## Insight 61: Create and share blog posts or writing about evals to help spread knowledge and ...
**Claim:** Create and share blog posts or writing about evals to help spread knowledge and amplify the community.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel encouraging others to teach evals and share their learnings.
