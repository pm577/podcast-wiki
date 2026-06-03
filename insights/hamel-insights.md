# Hamel — Insights

*Extracted from podcast appearances.*

### Insight: Evals are a way to systematically measure and improve an AI application, essenti...
**Claim:** Evals are a way to systematically measure and improve an AI application, essentially data analytics on your LLM application.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel defines evals as a systematic method for measuring and improving AI applications.

### Insight: Before evals, you would be left with guessing; you might fix a prompt and hope y...
**Claim:** Before evals, you would be left with guessing; you might fix a prompt and hope you're not breaking anything else, relying on vibe checks which become unmanageable as the application grows.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel explains the problem evals solve: moving from guessing and vibe checks to systematic measurement.

### Insight: Evals help create metrics to measure how your application is doing and give you ...
**Claim:** Evals help create metrics to measure how your application is doing and give you a feedback signal to iterate against with confidence.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel describes the benefit of evals: providing metrics and a feedback signal for confident iteration.

### Insight: Evals are not just unit tests; they are a spectrum including tracking metrics ov...
**Claim:** Evals are not just unit tests; they are a spectrum including tracking metrics over time, looking at data regularly to find new cohorts, and measuring open-ended tasks.
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya corrects the unit test metaphor and broadens the definition of evals.

### Insight: Unit tests are a small part of the eval puzzle; evals also include tracking user...
**Claim:** Unit tests are a small part of the eval puzzle; evals also include tracking user feedback like thumbs up/down and analyzing new user distributions.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya explains that evals encompass more than unit tests, including user feedback and data analysis.

### Insight: The goal is not to do evals perfectly, it's to actionably improve your product....
**Claim:** The goal is not to do evals perfectly, it's to actionably improve your product.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya states the purpose of evals: actionable improvement, not perfection.

### Insight: A common misconception is that AI can eval itself, but it doesn't work....
**Claim:** A common misconception is that AI can eval itself, but it doesn't work.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel identifies the top misconception about evals.

### Insight: Start with data analysis (error analysis) rather than jumping straight to writin...
**Claim:** Start with data analysis (error analysis) rather than jumping straight to writing tests when building evals for LLM applications.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain explaining the common trap of jumping straight to tests and advocating for starting with data analysis to ground what to test.

### Insight: Use observability tools (like Braintrust, Phoenix Arize, LangSmith) to log trace...
**Claim:** Use observability tools (like Braintrust, Phoenix Arize, LangSmith) to log traces of LLM interactions and perform error analysis by manually reviewing sampled traces.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel showing how to use Braintrust to view traces and manually annotate errors.

### Insight: Product people should be involved in error analysis because they understand the ...
**Claim:** Product people should be involved in error analysis because they understand the user experience and can identify when the AI's response is not ideal (e.g., should have handed off to a human).
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel and Lenny discussing that product people need to be in the room for error analysis because it's about user experience.

### Insight: When reviewing traces, write down the first most upstream error you see and move...
**Claim:** When reviewing traces, write down the first most upstream error you see and move on; don't try to capture all errors in one trace.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel explaining the method for error analysis: just write the first thing that's wrong and stop.

### Insight: Error analysis can reveal unexpected issues like garbled text messages causing c...
**Claim:** Error analysis can reveal unexpected issues like garbled text messages causing conversation flow problems, which might otherwise go unnoticed.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel showing a trace where text message splitting caused janky conversation flow.

### Insight: Sample your data for error analysis; you don't need to review all logs to learn ...
**Claim:** Sample your data for error analysis; you don't need to review all logs to learn a lot about your LLM application's issues.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel saying you don't have to do it for all data, just sample and you'll learn a lot.

### Insight: When doing error analysis, focus on the first thing that's wrong (most upstream ...
**Claim:** When doing error analysis, focus on the first thing that's wrong (most upstream error) and stop; don't try to capture all errors at once.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Discussion on how to manually review traces: 'capture the first thing that you see that's wrong, and stop, and move on.'

### Insight: Do not automate the initial error analysis (open coding) with an LLM because it ...
**Claim:** Do not automate the initial error analysis (open coding) with an LLM because it lacks the domain context to identify subtle errors like hallucinations.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar warns against using LLMs for open coding, giving example of hallucinated virtual tour that LLM would miss.

### Insight: Appoint a single domain expert as a 'benevolent dictator' to perform open coding...
**Claim:** Appoint a single domain expert as a 'benevolent dictator' to perform open coding, avoiding committee decision-making that slows progress.
**Framework:** Benevolent Dictator
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain introduces the term 'benevolent dictator' to simplify the open coding process by having one trusted person.

### Insight: Perform at least 100 trace reviews (open coding) until you reach theoretical sat...
**Claim:** Perform at least 100 trace reviews (open coding) until you reach theoretical saturation—when no new error types emerge.
**Framework:** Theoretical Saturation
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel and Shreya recommend 100 as a starting point, and Shreya explains theoretical saturation as the stopping criterion.

### Insight: After manual open coding, use an LLM to categorize the notes into axial codes by...
**Claim:** After manual open coding, use an LLM to categorize the notes into axial codes by simple counting, leveraging LLMs' knowledge of qualitative research terms.
**Framework:** Axial Coding
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel describes using an LLM to analyze a CSV of open codes and create axial codes, noting that LLMs understand the term 'open codes'.

### Insight: Use open coding to capture detailed, specific failure descriptions (avoid vague ...
**Claim:** Use open coding to capture detailed, specific failure descriptions (avoid vague terms like 'janky') so that AI can later categorize them accurately.
**Framework:** Open coding
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya explains that open codes must be detailed for AI to categorize them; vague terms like 'janky' are insufficient.

### Insight: After generating axial codes with an LLM, manually review and refine them to be ...
**Claim:** After generating axial codes with an LLM, manually review and refine them to be more specific and actionable (e.g., rename 'capability limitation' to 'tour scheduling rescheduling issues').
**Framework:** Axial coding
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel shows how he refines generic axial codes from Claude into more specific, actionable categories.

### Insight: Use AI to automatically categorize open codes into refined axial codes by provid...
**Claim:** Use AI to automatically categorize open codes into refined axial codes by providing a comma-separated list of categories and using a prompt like 'categorize the following note into one of the following categories'.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel demonstrates using Gemini in Google Sheets to categorize open codes into refined axial codes automatically.

### Insight: Include a 'none of the above' category when using AI to label open codes, so you...
**Claim:** Include a 'none of the above' category when using AI to label open codes, so you can identify missing axial codes and iterate on your taxonomy.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya recommends adding 'none of the above' to catch open codes that don't fit existing axial codes, prompting refinement.

### Insight: When generating axial codes, you can customize the prompt to specify the desired...
**Claim:** When generating axial codes, you can customize the prompt to specify the desired granularity, such as 'I want each axial code to be an actionable failure mode' or 'group by stage of user story'.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya mentions that you can be detailed in the prompt to get axial codes that are actionable or grouped by user story stage.

### Insight: Error analysis using open and axial coding is a technique grounded in social sci...
**Claim:** Error analysis using open and axial coding is a technique grounded in social science and has been used for stochastic systems for decades; it is not new, and you should be wary of entirely new methods.
**Framework:** Error analysis
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya and Hamel emphasize that they didn't invent error analysis; it's grounded in theory and literature, and new methods should be scrutinized.

### Insight: Use axial coding with a 'none of the above' category to identify gaps in your ca...
**Claim:** Use axial coding with a 'none of the above' category to identify gaps in your categories and refine them.
**Framework:** Axial coding
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Discussion on how AI can say 'none of the above' to indicate incomplete axial codes, prompting refinement.

### Insight: Perform qualitative analysis once a week in 30 minutes to significantly improve ...
**Claim:** Perform qualitative analysis once a week in 30 minutes to significantly improve your product.
**Audience:** operator | **Actionability:** 10/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya says people do this once a week in 30 minutes and product improves dramatically.

### Insight: Use pivot tables to count and prioritize failure modes from coded traces....
**Claim:** Use pivot tables to count and prioritize failure modes from coded traces.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel shows a pivot table counting conversational flow issues and other problems.

### Insight: Don't write evals for obvious engineering errors; fix them directly (e.g., forma...
**Claim:** Don't write evals for obvious engineering errors; fix them directly (e.g., formatting issues in prompts).
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel says some errors like formatting are obvious and don't need evals, just fix the prompt.

### Insight: For complex failure modes, build an LLM as a judge with a binary pass/fail outpu...
**Claim:** For complex failure modes, build an LLM as a judge with a binary pass/fail output, not a scale.
**Framework:** LLM as a judge
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya and Hamel discuss using LLM judges for subjective issues like handoffs, with binary output.

### Insight: Use LLM judges for online monitoring by sampling production traces daily to meas...
**Claim:** Use LLM judges for online monitoring by sampling production traces daily to measure failure rates.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya says LLM judges can be used on production traces to get specific measures of quality.

### Insight: When building an LLM judge prompt, iterate manually and don't blindly accept LLM...
**Claim:** When building an LLM judge prompt, iterate manually and don't blindly accept LLM-generated prompts.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel says to use LLM to help create the prompt but put yourself in the loop and edit it.

### Insight: Don't blindly accept LLM outputs; put yourself in the loop and iterate on prompt...
**Claim:** Don't blindly accept LLM outputs; put yourself in the loop and iterate on prompts.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Discussion on using LLMs to create prompts for evaluating handoff failures, emphasizing human review and iteration.

### Insight: Before releasing an LLM as a judge, measure its alignment with human-labeled dat...
**Claim:** Before releasing an LLM as a judge, measure its alignment with human-labeled data (axial codes) to ensure it agrees with human judgment.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Advice on validating LLM judges by comparing against human-coded data before deployment.

### Insight: Agreement rate is a dangerous metric for rare errors; instead, use a confusion m...
**Claim:** Agreement rate is a dangerous metric for rare errors; instead, use a confusion matrix to examine false positives and false negatives.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Warning that high agreement can be misleading when errors are rare, and recommendation to use a matrix to inspect error types.

### Insight: Iterate on LLM judge prompts to reduce misalignment, aiming to minimize false po...
**Claim:** Iterate on LLM judge prompts to reduce misalignment, aiming to minimize false positives and false negatives in the confusion matrix.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Advice to refine prompts based on confusion matrix results to improve judge accuracy.

### Insight: Evals are derived from data and uncover expectations that couldn't be dreamed up...
**Claim:** Evals are derived from data and uncover expectations that couldn't be dreamed up upfront; PRDs should evolve based on observed failure modes.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Discussion on how data analysis reveals new failure modes, leading to improved product requirements.

### Insight: Prioritize evals for the most pesky and risky failure modes; you don't need an e...
**Claim:** Prioritize evals for the most pesky and risky failure modes; you don't need an eval for everything, only 4-7 per product.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Advice on focusing eval efforts on high-impact areas rather than trying to cover all possible issues.

### Insight: Building an LLM judge is a one-time cost that can be used forever on your applic...
**Claim:** Building an LLM judge is a one-time cost that can be used forever on your application.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Discussion about the cost-benefit of building an LLM judge for evaluation.

### Insight: Data analysis, even basic counting, is accessible to everyone and can drive impr...
**Claim:** Data analysis, even basic counting, is accessible to everyone and can drive improvements quickly.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel explaining that basic data analysis is powerful and accessible.

### Insight: After building an LLM judge, use it in unit tests and online monitoring to drive...
**Claim:** After building an LLM judge, use it in unit tests and online monitoring to drive continuous improvement.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya describing next steps after building an LLM judge.

### Insight: People who do evals badly often use Likert scale LLM judges that don't align wit...
**Claim:** People who do evals badly often use Likert scale LLM judges that don't align with expectations, leading to distrust.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya explaining why some people are anti-evals due to bad experiences.

### Insight: Coding agents are different from other AI products because developers are domain...
**Claim:** Coding agents are different from other AI products because developers are domain experts and can dogfood effectively, so their eval process can be different.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel and Shreya discussing why coding agents don't need the same eval process.

### Insight: A/B tests are a form of evals and should be powered by actual error analysis, no...
**Claim:** A/B tests are a form of evals and should be powered by actual error analysis, not just hypothetical product requirements.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya discussing the relationship between A/B tests and evals.

### Insight: Dogfooding is effective but requires a visceral level of engagement to close the...
**Claim:** Dogfooding is effective but requires a visceral level of engagement to close the feedback loop; many people claim to dogfood but don't do it properly.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel cautioning about the dangers of superficial dogfooding.

### Insight: If you're going to do A-B tests, they should be powered by actual error analysis...
**Claim:** If you're going to do A-B tests, they should be powered by actual error analysis, not just hypothetical assumptions about what's important.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Discussion on A-B testing vs evals, Hamel Husain emphasizing grounding hypotheses in data.

### Insight: Evals are essentially data science for AI products; the confusion comes from tre...
**Claim:** Evals are essentially data science for AI products; the confusion comes from treating them as a new thing separate from traditional data analytics.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain explaining that evals are just data science thinking applied to AI products.

### Insight: A common misconception is that you can buy a tool and it will do evals for you a...
**Claim:** A common misconception is that you can buy a tool and it will do evals for you automatically; in reality, you need to look at your own data.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain listing top misconceptions about evals.

### Insight: Looking at individual traces (error analysis) is the highest ROI activity for im...
**Claim:** Looking at individual traces (error analysis) is the highest ROI activity for improving AI products; it always reveals insights.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain describing how he always starts consulting by looking at traces.

### Insight: There is no one correct way to do evals; you need to adapt based on your product...
**Claim:** There is no one correct way to do evals; you need to adapt based on your product stage and resources, but it always involves error analysis.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar adding a third misconception about evals.

### Insight: Don't be afraid to look at your data; the goal is actionable improvement, not pe...
**Claim:** Don't be afraid to look at your data; the goal is actionable improvement, not perfection, and you will find ways to improve.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar giving tips for starting evals.

### Insight: Use LLMs to help organize your eval process, but not to replace your own analysi...
**Claim:** Use LLMs to help organize your eval process, but not to replace your own analysis; AI is good for creating tools to reduce friction in looking at data.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar and Hamel Husain discussing using AI to build custom eval tools.

### Insight: Make it as easy as possible to look at your data because it's the highest ROI ac...
**Claim:** Make it as easy as possible to look at your data because it's the highest ROI activity you can engage in. With AI, remove all the friction.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Discussion on automating error analysis and making data inspection easy.

### Insight: When doing evals, if you see something wrong, just go fix it. The whole point is...
**Claim:** When doing evals, if you see something wrong, just go fix it. The whole point is not to have a beautiful eval suite but to improve your application.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain teaching that evals should drive immediate fixes.

### Insight: Spend three to four days upfront on initial error analysis and labeling, then ab...
**Claim:** Spend three to four days upfront on initial error analysis and labeling, then about 30 minutes a week to maintain and improve the eval suite.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar describing the time investment for setting up evals.

### Insight: Put your product hat on and be critical: just because the AI is doing the right ...
**Claim:** Put your product hat on and be critical: just because the AI is doing the right thing technically doesn't mean the output is good. Ask 'Is this really good?'
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain's example of a recruiting email that was technically correct but poorly worded.

### Insight: Build your own interfaces for error analysis using tools like Claude code or Cur...
**Claim:** Build your own interfaces for error analysis using tools like Claude code or Cursor, and live code them on the spot for new data.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar describing a special topic in their course on building custom error analysis interfaces.

### Insight: Replace expensive state-of-the-art models with cheaper alternatives (e.g., GPT-5...
**Claim:** Replace expensive state-of-the-art models with cheaper alternatives (e.g., GPT-5 nano, 4-mini) for certain tasks to save costs while maintaining quality.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar discussing cost optimization in evals.

### Insight: Use AI-assisted coding tools like Cursor and Claude Code to increase ambition an...
**Claim:** Use AI-assisted coding tools like Cursor and Claude Code to increase ambition and productivity, especially when wearing multiple hats.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar and Hamel Husain discuss their favorite recently discovered products.

### Insight: Adopt the motto 'Keep learning in. Think like a beginner.' to maintain a fresh p...
**Claim:** Adopt the motto 'Keep learning in. Think like a beginner.' to maintain a fresh perspective and continuous growth.
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain shares his favorite life motto.

### Insight: Always try to think about the other side's argument and assume a generous interp...
**Claim:** Always try to think about the other side's argument and assume a generous interpretation to foster collaboration rather than conflict.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar shares her favorite life motto.

### Insight: Share your successes and case studies with creators to motivate them and keep th...
**Claim:** Share your successes and case studies with creators to motivate them and keep them going.
**Audience:** general | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** hamel-husain-shreya-shankar
**Context:** Shreya Shankar explains how listeners can be helpful.

### Insight: Encourage others to teach evals and share blog posts or writings about their lea...
**Claim:** Encourage others to teach evals and share blog posts or writings about their learnings to amplify the community's knowledge.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** hamel-husain-shreya-shankar
**Context:** Hamel Husain explains how listeners can be helpful.
