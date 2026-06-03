# Shreya Shankar — Insights

*Extracted from podcast appearances.*

## Insight 1: Evals is a way to systematically measure and improve an AI application. It's dat...
**Claim:** Evals is a way to systematically measure and improve an AI application. It's data analytics on your LLM application and a systematic way of looking at that data, and where necessary, creating metrics around things so you can measure what's happening, and then so you can iterate and do experiments and improve.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Defining what evals are at the start of the conversation.

## Insight 2: Before evals, you would be left with guessing. You would maybe fix a prompt and ...
**Claim:** Before evals, you would be left with guessing. You would maybe fix a prompt and hope that you're not breaking anything else with that prompt, and you might rely on vibe checks. Vibe checks are good and you should do vibe checks initially, but it can become very unmanageable very fast because as your application grows, it's really hard to rely on vibe checks.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Explaining the problem evals solve, contrasting with vibe checks.

## Insight 3: Evals help you create metrics that you can use to measure how your application i...
**Claim:** Evals help you create metrics that you can use to measure how your application is doing and kind of give you a way to improve your application with confidence. That you have a feedback signal in which to iterate against.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Describing the benefit of evals for iterative improvement.

## Insight 4: Evals is a big spectrum of ways to measure application quality. Unit tests are o...
**Claim:** Evals is a big spectrum of ways to measure application quality. Unit tests are one way of doing this. Maybe there are some non-negotiable functionalities that you want your AI assistant to have, and unit tests are going to be able to check that. But evals could also be a way of looking at your data regularly to find new cohorts of people, or metrics that you just want to track over time.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya expanding on the definition of evals beyond unit tests.

## Insight 5: It's really important that we don't think of evals as just tests. There's a comm...
**Claim:** It's really important that we don't think of evals as just tests. There's a common trap that a lot of people fall into.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Hamel warning against a narrow view of evals.

## Insight 6: The goal is not to do evals perfectly, it's to actionably improve your product....
**Claim:** The goal is not to do evals perfectly, it's to actionably improve your product.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya stating the purpose of evals.

## Insight 7: You can appoint one person whose taste that you trust. It should be the person w...
**Claim:** You can appoint one person whose taste that you trust. It should be the person with domain expertise. Oftentimes, it is the product manager. You don't want to make this process so expensive that you can't do it.
**Framework:** benevolent dictator
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel discussing how to avoid committee paralysis in eval design.

## Insight 8: Don't think of evals as just tests; start with data analysis to ground what you ...
**Claim:** Don't think of evals as just tests; start with data analysis to ground what you should test, because LLMs are stochastic and have a large surface area.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel explaining the common trap of jumping straight to writing tests for LLMs.

## Insight 9: Use error analysis: sample logs from your LLM application, write informal notes ...
**Claim:** Use error analysis: sample logs from your LLM application, write informal notes about what's wrong, focusing on the most upstream error first.
**Framework:** Error analysis
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel demonstrating how to analyze traces from Nurture Boss.

## Insight 10: Product people must be involved in error analysis because they understand the us...
**Claim:** Product people must be involved in error analysis because they understand the user experience and can identify when the AI's response is not ideal (e.g., not handing off to a human when appropriate).
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel and Lenny discussing why product people should be in the room for error analysis.

## Insight 11: Observability tools (e.g., Braintrust, Phoenix Arize, LangSmith) are essential f...
**Claim:** Observability tools (e.g., Braintrust, Phoenix Arize, LangSmith) are essential for logging traces of AI interactions and enabling error analysis.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel showing the trace in Braintrust and mentioning other tools.

## Insight 12: When analyzing traces, just write down the first thing that's wrong and move on;...
**Claim:** When analyzing traces, just write down the first thing that's wrong and move on; don't try to capture all errors in one trace.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel advising to focus on the most upstream error and not overthink it.

## Insight 13: Error analysis can uncover unexpected issues like garbled text messages causing ...
**Claim:** Error analysis can uncover unexpected issues like garbled text messages causing conversation flow problems, which might otherwise go unnoticed.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Hamel showing a trace where text message splitting caused janky conversation flow.

## Insight 14: The most upstream error is the first thing wrong; capture it and move on, don't ...
**Claim:** The most upstream error is the first thing wrong; capture it and move on, don't worry about all errors.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussing error analysis technique for LLM traces

## Insight 15: Manual error analysis (open coding) is essential; LLMs cannot replace human cont...
**Claim:** Manual error analysis (open coding) is essential; LLMs cannot replace human context for detecting subtle errors like hallucination.
**Framework:** Open coding
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Responding to question about automating error analysis with LLMs

## Insight 16: Appoint a 'benevolent dictator' (domain expert) to do open coding to avoid commi...
**Claim:** Appoint a 'benevolent dictator' (domain expert) to do open coding to avoid committee slowdown.
**Framework:** Benevolent dictator
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Explaining how to make error analysis tractable

## Insight 17: Do at least 100 traces until theoretical saturation (no new error types uncovere...
**Claim:** Do at least 100 traces until theoretical saturation (no new error types uncovered).
**Framework:** Theoretical saturation
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Advising on how many traces to review

## Insight 18: After open coding, use LLMs to categorize notes into axial codes for counting an...
**Claim:** After open coding, use LLMs to categorize notes into axial codes for counting and prioritization.
**Framework:** Axial coding
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Describing next step after manual note-taking

## Insight 19: Basic counting is the most powerful analytical technique; undervalued and approa...
**Claim:** Basic counting is the most powerful analytical technique; undervalued and approachable.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Emphasizing simplicity in data analysis

## Insight 20: Use open coding and axial coding to analyze LLM errors: first capture raw proble...
**Claim:** Use open coding and axial coding to analyze LLM errors: first capture raw problems (open codes), then group them into failure modes (axial codes) to identify the most prevalent issues.
**Framework:** Open coding and axial coding
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion on how to analyze LLM errors using grounded theory methods from social science.

## Insight 21: When generating axial codes with an LLM, you can customize the prompt to make ca...
**Claim:** When generating axial codes with an LLM, you can customize the prompt to make categories more actionable, e.g., 'I want each axial code to actually be some actionable failure mode' or group by stage of user story.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya explaining that you can be detailed in the prompt to get more useful axial codes.

## Insight 22: After getting AI-generated axial codes, manually review and refine them to be mo...
**Claim:** After getting AI-generated axial codes, manually review and refine them to be more specific and actionable (e.g., rename 'capability limitation' to 'tour scheduling issue').
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel showing how he iterates on the axial codes to make them more actionable.

## Insight 23: Use AI to automatically categorize open codes into your refined axial codes usin...
**Claim:** Use AI to automatically categorize open codes into your refined axial codes using a simple prompt in Google Sheets or similar tool, but include a 'none of the above' category to catch missing codes.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel demonstrating automatic categorization with Gemini in Google Sheets, and Shreya suggesting 'none of the above'.

## Insight 24: Open codes must be detailed enough for AI (or humans) to categorize them; avoid ...
**Claim:** Open codes must be detailed enough for AI (or humans) to categorize them; avoid vague terms like 'janky' without context.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya emphasizing the importance of detailed open codes for accurate categorization.

## Insight 25: This error analysis process is not new; it's grounded in decades-old machine lea...
**Claim:** This error analysis process is not new; it's grounded in decades-old machine learning and social science methods. Be wary of entirely new, ungrounded techniques.
**Framework:** Error analysis from Andrew Ng's teachings
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya and Hamel noting that they didn't invent error analysis; it's based on established theory.

## Insight 26: Use pivot tables to count and prioritize failure modes from coded traces, focusi...
**Claim:** Use pivot tables to count and prioritize failure modes from coded traces, focusing on the most impactful issues rather than just the most frequent.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel shows a pivot table of coded traces to identify top problems like conversational flow issues and human handoff issues.

## Insight 27: Before building evals, ground yourself in actual errors from trace analysis; don...
**Claim:** Before building evals, ground yourself in actual errors from trace analysis; don't skip this step and go straight to writing tests.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel warns that people get lost by going straight to evals without analyzing real errors first.

## Insight 28: Use code-based evals (e.g., Python functions) for simple, deterministic checks l...
**Claim:** Use code-based evals (e.g., Python functions) for simple, deterministic checks like output format, and LLM-as-judge for complex, subjective failure modes.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya and Hamel discuss two types of evals: code-based for things like JSON output, LLM-as-judge for nuanced issues like handoff quality.

## Insight 29: When using LLM-as-judge, make the evaluation binary (pass/fail) rather than a sc...
**Claim:** When using LLM-as-judge, make the evaluation binary (pass/fail) rather than a scale (e.g., 1-7) to avoid ambiguity and make metrics actionable.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel advises against rating scales, saying 'Is this good enough or not? Yes or no?' and Shreya agrees that scales lead to confusion.

## Insight 30: LLM judges can be used not just in CI but also for online monitoring by sampling...
**Claim:** LLM judges can be used not just in CI but also for online monitoring by sampling production traces daily to measure real-world failure rates.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya explains that LLM judges can run on production traces to get a specific measure of application quality over time.

## Insight 31: Iterate on your judge prompt with human oversight; use an LLM to help create it ...
**Claim:** Iterate on your judge prompt with human oversight; use an LLM to help create it but don't blindly accept its output.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel says to put yourself in the loop when creating judge prompts, similar to iterating on axial codes.

## Insight 32: Don't blindly accept LLM judge outputs; align the judge to human expectations by...
**Claim:** Don't blindly accept LLM judge outputs; align the judge to human expectations by measuring agreement against human-labeled data.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion on using LLM as a judge and the importance of validating its outputs against human judgments.

## Insight 33: When evaluating LLM judge agreement, don't rely solely on overall agreement perc...
**Claim:** When evaluating LLM judge agreement, don't rely solely on overall agreement percentage; use a confusion matrix to examine false positives and false negatives separately, especially for rare errors.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Explaining why overall agreement can be misleading and how to properly evaluate judge performance.

## Insight 34: Iterate on the LLM judge prompt by examining misalignment cases (false positives...
**Claim:** Iterate on the LLM judge prompt by examining misalignment cases (false positives/negatives) and clarifying the prompt to reduce those errors.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Advice on improving LLM judge prompts based on confusion matrix analysis.

## Insight 35: Use axial coding to manually label a sample of data before creating LLM judges; ...
**Claim:** Use axial coding to manually label a sample of data before creating LLM judges; this provides a ground truth to measure judge alignment.
**Framework:** Axial coding
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Describing the process of manually labeling data to create a reference for evaluating LLM judges.

## Insight 36: Product requirements documents (PRDs) are a useful abstraction but will evolve a...
**Claim:** Product requirements documents (PRDs) are a useful abstraction but will evolve as you uncover failure modes from data; don't expect to define everything upfront.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Discussion on how PRDs relate to evals and the need for flexibility as you see actual outputs.

## Insight 37: Prioritize writing LLM judge evals only for the most pesky or risky failure mode...
**Claim:** Prioritize writing LLM judge evals only for the most pesky or risky failure modes, not for every issue; you have finite resources.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Advice on focusing eval efforts on high-impact areas rather than trying to cover everything.

## Insight 38: Criteria drift is a key challenge: people's opinions of good and bad change as t...
**Claim:** Criteria drift is a key challenge: people's opinions of good and bad change as they review more outputs, so you must be flexible and iterate.
**Framework:** Criteria drift
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Referencing research on how evaluators' criteria evolve over time.

## Insight 39: You can use LLM judges in unit tests and online monitoring to drive continuous p...
**Claim:** You can use LLM judges in unit tests and online monitoring to drive continuous product improvements.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion on what comes after building an LLM judge

## Insight 40: Dogfooding is a form of eval, but it requires deep, visceral engagement to close...
**Claim:** Dogfooding is a form of eval, but it requires deep, visceral engagement to close the feedback loop; many people claim to dogfood but don't do it effectively.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Debate on evals and dogfooding

## Insight 41: A/B tests are a form of eval, but they should be powered by actual error analysi...
**Claim:** A/B tests are a form of eval, but they should be powered by actual error analysis; premature A/B testing without error analysis is common and ineffective.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Discussion on A/B tests vs evals

## Insight 42: Coding agents are fundamentally different from other AI products because the dev...
**Claim:** Coding agents are fundamentally different from other AI products because the developer is the domain expert, allowing them to short-circuit many eval activities.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Debate on evals and coding agents

## Insight 43: Product managers can now build very profitable products by practicing the skill ...
**Claim:** Product managers can now build very profitable products by practicing the skill of systematic data analysis and error analysis.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Discussion on the accessibility of error analysis skills

## Insight 44: People have been burned by evals in the past, often because they used a Likert s...
**Claim:** People have been burned by evals in the past, often because they used a Likert scale LLM judge that didn't align with expectations; this leads to anti-eval sentiment.
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Debate on the controversy around evals

## Insight 45: Ground your A/B tests in actual error analysis rather than hypothetical assumpti...
**Claim:** Ground your A/B tests in actual error analysis rather than hypothetical assumptions about what is important.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion about A/B testing vs. error analysis, with Hamel showing that errors are often not what you think.

## Insight 46: Evals are essentially data science for AI products; use analytic tools to unders...
**Claim:** Evals are essentially data science for AI products; use analytic tools to understand your product rather than treating evals as a separate new thing.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel explaining that evals are just data science thinking applied to AI products.

## Insight 47: Don't rely on generic eval tools or AI to automatically evaluate your applicatio...
**Claim:** Don't rely on generic eval tools or AI to automatically evaluate your application; you need to look at your own data and do error analysis.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel's top misconception: people think they can buy a tool and it will do the eval for them.

## Insight 48: Look at individual traces (data) to understand problems; it always yields insigh...
**Claim:** Look at individual traces (data) to understand problems; it always yields insights.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel's consulting experience: asking clients to look at traces reveals issues 100% of the time.

## Insight 49: There is no one correct way to do evals; the process must be tailored to your pr...
**Claim:** There is no one correct way to do evals; the process must be tailored to your product stage and resources, but always involves error analysis.
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya's third misconception: there are many correct ways to do evals.

## Insight 50: Don't be afraid to look at your data; the goal is actionable improvement, not pe...
**Claim:** Don't be afraid to look at your data; the goal is actionable improvement, not perfection.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Shreya's tip: don't be scared of looking at data, and iterate on your process.

## Insight 51: Use LLMs to help organize thoughts and present information, but not to replace y...
**Claim:** Use LLMs to help organize thoughts and present information, but not to replace your own analysis.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya's tip: use AI to organize product requirements and improve based on open codes.

## Insight 52: The goal of evals is not to have a beautiful eval suite, but to fix your applica...
**Claim:** The goal of evals is not to have a beautiful eval suite, but to fix your application and make it better. If you see something wrong, just go fix it.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel Husain discussing the purpose of evals: 'The whole point is not to have evals, a beautiful eval suite... No, just fix your application, make it better.'

## Insight 53: Initial error analysis takes about three to four days of intensive work, but aft...
**Claim:** Initial error analysis takes about three to four days of intensive work, but after that, maintaining evals can be as little as 30 minutes per week.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya Shankar describing her typical timeline: 'I'll spend three to four days really working... I would say maybe 30 minutes a week after that.'

## Insight 54: When doing error analysis, put your product hat on and be critical of the output...
**Claim:** When doing error analysis, put your product hat on and be critical of the output. Ask if the output is genuinely good, not just technically correct.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel Husain's anecdote about reviewing a recruiting email: 'I said, You know what? I hate this email... is this really good?'

## Insight 55: To reduce costs, replace expensive state-of-the-art models with cheaper alternat...
**Claim:** To reduce costs, replace expensive state-of-the-art models with cheaper alternatives (e.g., GPT-5 nano, 4-mini) for certain tasks while maintaining quality.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Shreya Shankar mentioning cost-optimization: 'How can we replace certain uses of the most expensive GPT-5, with 5-nano, 4-mini whatnot and save a lot of money?'

## Insight 56: Build custom interfaces for error analysis using tools like Claude code or Curso...
**Claim:** Build custom interfaces for error analysis using tools like Claude code or Cursor to quickly visualize and interact with data.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** hamelshreya
**Context:** Shreya Shankar describing course content: 'We go through actual interfaces that we've built and we also live code them on the spot... using Claude code cursor.'

## Insight 57: Remove friction from the process of looking at data to make it as easy as possib...
**Claim:** Remove friction from the process of looking at data to make it as easy as possible, as it is the highest ROI activity.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Hamel Husain: 'make it as easy as possible because, again, it's the most powerful activity that you can engage in. It's the highest ROI activity you can engage in.'

## Insight 58: The process of error analysis and improving AI products is fun and engaging when...
**Claim:** The process of error analysis and improving AI products is fun and engaging when you put your product hat on and critically evaluate outputs.
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.85
**Source:** hamelshreya
**Context:** Hamel Husain: 'I would say this process is a lot of fun, actually... put your product hat on and just being critical, and this is where the fun part is.'

## Insight 59: Use AI-assisted coding tools like Cursor and Claude Code to increase ambition an...
**Claim:** Use AI-assisted coding tools like Cursor and Claude Code to increase ambition and productivity, especially when wearing many hats.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** Discussion about favorite recently discovered products.

## Insight 60: Adopt the motto 'keep learning in, think like a beginner' to maintain curiosity ...
**Claim:** Adopt the motto 'keep learning in, think like a beginner' to maintain curiosity and growth.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Question about favorite life motto.

## Insight 61: Always try to think about the other side's argument and assume a generous interp...
**Claim:** Always try to think about the other side's argument and assume a generous interpretation to foster collaboration rather than conflict.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Shreya's response to favorite life motto.

## Insight 62: Share your successes and case studies with creators to keep them motivated and h...
**Claim:** Share your successes and case studies with creators to keep them motivated and help the community learn from real implementations.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamelshreya
**Context:** How listeners can be helpful to Shreya and Hamel.

## Insight 63: Write blog posts or create content about your learnings in AI evals to help spre...
**Claim:** Write blog posts or create content about your learnings in AI evals to help spread knowledge and amplify the field.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamelshreya
**Context:** Hamel's request for help in teaching evals.
