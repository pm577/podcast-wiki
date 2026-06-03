# Ronny Kohavi — Insights

*Extracted from podcast appearances.*

## Insight 1: Any code change, even small bug fixes, should be A/B tested because they can hav...
**Claim:** Any code change, even small bug fixes, should be A/B tested because they can have surprising unexpected impact.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Ronny advocating for testing all code changes, citing surprising results from small changes.

## Insight 2: Allocate resources to high-risk, high-reward ideas, understanding that most will...
**Claim:** Allocate resources to high-risk, high-reward ideas, understanding that most will fail (80% of the time).
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Ronny discussing the need to try radical ideas despite high failure rates.

## Insight 3: Trivial changes can have massive impact; prioritize experiments based on ease of...
**Claim:** Trivial changes can have massive impact; prioritize experiments based on ease of implementation, not just perceived potential.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** The Bing ad experiment where moving a line increased revenue by 12%.

## Insight 4: When an experiment shows a surprisingly large positive result, be skeptical and ...
**Claim:** When an experiment shows a surprisingly large positive result, be skeptical and check for bugs before celebrating.
**Framework:** Twyman's law
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Ronny describing the Bing revenue alarm and the need to verify surprising results.

## Insight 5: Institutional memory of winning experiments fades; document and remember past wi...
**Claim:** Institutional memory of winning experiments fades; document and remember past wins to avoid reinventing them.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** ronny-kohavi
**Context:** Ronny noting that the new tab experiment was forgotten and had to be reintroduced at Airbnb.

## Insight 6: Most experiments fail: 80-92% of ideas do not improve key metrics. At Bing, 85% ...
**Claim:** Most experiments fail: 80-92% of ideas do not improve key metrics. At Bing, 85% failure rate; at Airbnb, 92%.
**Audience:** operator | **Actionability:** 6/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Discussion about experiment failure rates at Microsoft, Bing, and Airbnb.

## Insight 7: Incremental improvements (inch by inch) add up to significant gains over time. E...
**Claim:** Incremental improvements (inch by inch) add up to significant gains over time. Example: Bing relevance team improves 2% per year via many small wins; Airbnb achieved 6% revenue improvement from 250 experiments.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Discussion about how most wins are small and cumulative.

## Insight 8: Document surprising experiments (both winners and losers) in a quarterly meeting...
**Claim:** Document surprising experiments (both winners and losers) in a quarterly meeting to build institutional memory. Surprising = large gap between expected and actual result.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Advice on remembering surprises and institutional learning.

## Insight 9: Use a searchable experiment history platform to query past experiments by keywor...
**Claim:** Use a searchable experiment history platform to query past experiments by keywords (e.g., 'Has anyone tested this?').
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** ronny-kohavi
**Context:** Discussion about documenting and searching past experiments.

## Insight 10: Allocate a portfolio of experiments: some incremental (low risk, steady gains) a...
**Claim:** Allocate a portfolio of experiments: some incremental (low risk, steady gains) and some high-risk, high-reward (most will fail, but home runs possible).
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Discussion about balancing incremental vs. big bets.

## Insight 11: Use resources like goodui.org and Microsoft's 'Rules of Thumb' paper to find pat...
**Claim:** Use resources like goodui.org and Microsoft's 'Rules of Thumb' paper to find patterns that often work (e.g., opening links in new tabs).
**Framework:** Rules of Thumb
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.85
**Source:** ronny-kohavi
**Context:** Recommendation of resources for proven experiment patterns.

## Insight 12: Test everything: any code change or feature should be in an experiment because e...
**Claim:** Test everything: any code change or feature should be in an experiment because even small bug fixes can have unexpected negative impacts (e.g., Windows indexer killed battery life).
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Advocacy for testing all changes, with example of battery life impact.

## Insight 13: Unless you have at least tens of thousands of users, the statistics just don't w...
**Claim:** Unless you have at least tens of thousands of users, the statistics just don't work out for most metrics. For detecting 5% changes, you need around 200,000 users.
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Discussion on when to start A/B testing

## Insight 14: Define an Overall Evaluation Criterion (OEC) that is causally predictive of life...
**Claim:** Define an Overall Evaluation Criterion (OEC) that is causally predictive of lifetime value, including countervailing metrics to avoid short-term optimization that harms long-term user experience.
**Framework:** Overall Evaluation Criterion (OEC)
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Discussion on optimizing for long-term growth

## Insight 15: Build a platform where the incremental cost of running an experiment approaches ...
**Claim:** Build a platform where the incremental cost of running an experiment approaches zero, so that everything can be experimented on without hesitation.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** ronny-kohavi
**Context:** Discussion on the cost of A/B testing

## Insight 16: Use constraint optimization to balance trade-offs, e.g., limit ad pixels per pag...
**Claim:** Use constraint optimization to balance trade-offs, e.g., limit ad pixels per page to increase revenue without degrading user experience.
**Framework:** Constraint optimization
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Example of ad placement optimization

## Insight 17: Model the cost of negative user actions (e.g., unsubscribes) to create counterva...
**Claim:** Model the cost of negative user actions (e.g., unsubscribes) to create countervailing metrics that prevent spammy behavior.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** ronny-kohavi
**Context:** Example of email team optimization at Amazon

## Insight 18: Be ready to fail 80% of the time on big ideas, and use controlled experiments as...
**Claim:** Be ready to fail 80% of the time on big ideas, and use controlled experiments as an oracle to decide when to abort.
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** ronny-kohavi
**Context:** Discussion on big bets and failure

## Insight 19: Model the cost of spamming users by measuring the long-term value lost from unsu...
**Claim:** Model the cost of spamming users by measuring the long-term value lost from unsubscribes, and use that as a countervailing metric to optimize email campaigns.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Discussion about email campaign optimization at Amazon, where they modeled the cost of unsubscribes to find that more than half of campaigns were negative.

## Insight 20: When users unsubscribe, offer them the option to unsubscribe from a specific cam...
**Claim:** When users unsubscribe, offer them the option to unsubscribe from a specific campaign (e.g., author emails) rather than all emails, to preserve future lifetime value.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Follow-up insight from the email campaign analysis at Amazon, leading to a new feature that reduces the negative impact of unsubscribes.

## Insight 21: Avoid large redesigns; instead, decompose them into smaller incremental changes ...
**Claim:** Avoid large redesigns; instead, decompose them into smaller incremental changes (one-factor-at-a-time) and test each step to learn what works and avoid large failures.
**Framework:** OFAT (one-factor-at-a-time)
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Discussion about the high failure rate of big redesigns and the recommendation to iterate incrementally.

## Insight 22: Allocate about 20% of resources to high-risk, high-reward big bets, but be prepa...
**Claim:** Allocate about 20% of resources to high-risk, high-reward big bets, but be prepared for an 80% failure rate on such redesigns.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** ronny-kohavi
**Context:** Advice on resource allocation between incremental improvements and big redesigns, with a rule of thumb for failure rate.

## Insight 23: Do not ship experiments that are flat (no statistically significant improvement)...
**Claim:** Do not ship experiments that are flat (no statistically significant improvement), as they add maintenance overhead and complexity without value.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Discussion on the decision to ship or not ship based on experiment results, emphasizing that flat results should not be shipped.

## Insight 24: When legal requirements force a change, run experiments to find the implementati...
**Claim:** When legal requirements force a change, run experiments to find the implementation that hurts the least, rather than accepting the default negative impact.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** ronny-kohavi
**Context:** Advice on handling mandatory changes from legal by testing multiple approaches to minimize harm.

## Insight 25: Everything in the search relevance team at Airbnb was A/B tested; nothing launch...
**Claim:** Everything in the search relevance team at Airbnb was A/B tested; nothing launched without an A/B test.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Discussion of Ronny's experience at Airbnb and how his team operated.

## Insight 26: During crises like Covid, it's even more important to run A/B tests to understan...
**Claim:** During crises like Covid, it's even more important to run A/B tests to understand if changes are actually helping in the current environment.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Lenny asked about experimentation during Covid when fast decisions were needed.

## Insight 27: If in peacetime you're wrong 66-80% of the time, why would you be subtly right i...
**Claim:** If in peacetime you're wrong 66-80% of the time, why would you be subtly right in wartime? So don't abandon data-driven decisions during crises.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Ronny arguing against the idea that crises require abandoning experimentation.

## Insight 28: Trust in the experimentation platform is crucial; it serves as a safety net and ...
**Claim:** Trust in the experimentation platform is crucial; it serves as a safety net and an oracle. Trust is easy to lose.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Discussion of why trust is important in experimentation.

## Insight 29: Sample ratio mismatch is a common red flag: if the split deviates from expected ...
**Claim:** Sample ratio mismatch is a common red flag: if the split deviates from expected (e.g., 50/50), something is wrong with the experiment.
**Framework:** Sample Ratio Mismatch
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Ronny explaining how to detect invalid experiments.

## Insight 30: At Microsoft, about 8% of experiments suffered from sample ratio mismatch, indic...
**Claim:** At Microsoft, about 8% of experiments suffered from sample ratio mismatch, indicating many experiments are invalid.
**Audience:** operator | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Ronny sharing data from a paper on sample ratio mismatches.

## Insight 31: Real-time P-value monitoring inflates false positive rates (e.g., from 5% to 30%...
**Claim:** Real-time P-value monitoring inflates false positive rates (e.g., from 5% to 30%), leading to untrustworthy results.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Critique of Optimizely's early statistical approach.

## Insight 32: Sample ratio mismatch (SRM) is a common issue in A/B tests, often caused by bots...
**Claim:** Sample ratio mismatch (SRM) is a common issue in A/B tests, often caused by bots hitting control and treatment in different proportions.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Discussion about diagnosing sample ratio mismatches in experiments.

## Insight 33: To prevent ignoring SRM, blank out the scorecard and require an explicit click t...
**Claim:** To prevent ignoring SRM, blank out the scorecard and require an explicit click to expose results, but even then people may still present flawed results.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Story about how they implemented SRM detection at Microsoft.

## Insight 34: Twyman's law: if a result looks too good to be true (e.g., >10% movement when no...
**Claim:** Twyman's law: if a result looks too good to be true (e.g., >10% movement when normal is <1%), it is likely wrong; investigate before celebrating.
**Framework:** Twyman's law
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Discussion about Twyman's law and its application to experiment results.

## Insight 35: The common interpretation of p-value as '1 - p = probability treatment is better...
**Claim:** The common interpretation of p-value as '1 - p = probability treatment is better' is incorrect; p-value is conditional on null hypothesis being true.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Explanation of p-value misconceptions.

## Insight 36: False positive risk can be much higher than 5%; e.g., at Airbnb with 8% success ...
**Claim:** False positive risk can be much higher than 5%; e.g., at Airbnb with 8% success rate, a p<0.05 result has 26% chance of being false positive.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Example of false positive risk calculation using historical success rate.

## Insight 37: To reduce false positives, use a stricter p-value threshold (e.g., 0.01) and rep...
**Claim:** To reduce false positives, use a stricter p-value threshold (e.g., 0.01) and replicate experiments, combining p-values via Fisher's or Stouffer's method.
**Framework:** Fisher's method, Stouffer's method
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Recommendation for lowering false positive rate through replication and combined p-values.

## Insight 38: When starting experimentation, use third-party platforms rather than building yo...
**Claim:** When starting experimentation, use third-party platforms rather than building your own, as they are now trustworthy and mature.
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Advice on build vs. buy for experimentation platforms.

## Insight 39: Define a clear Overall Evaluation Criterion (OEC) that everyone agrees on direct...
**Claim:** Define a clear Overall Evaluation Criterion (OEC) that everyone agrees on directionally; if half the room thinks more time on site is good and half thinks it's bad, the OEC is flawed.
**Framework:** OEC
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Discussion about Microsoft.com having multiple goals and the team choosing time on site as OEC without agreement on direction.

## Insight 40: Build a platform for experimentation to bring the marginal cost of experiments d...
**Claim:** Build a platform for experimentation to bring the marginal cost of experiments down to zero, enabling self-service setup and analysis.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Lenny asks about platforms vs. one-off experiments; Ronny explains the motivation to lower marginal cost.

## Insight 41: Use variance reduction techniques like capping metrics (e.g., capping revenue at...
**Claim:** Use variance reduction techniques like capping metrics (e.g., capping revenue at $1000 or nights booked at 30) to get statistically significant results faster with fewer users.
**Framework:** Variance reduction
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Ronny's advice on speeding up experiments: capping skewed metrics.

## Insight 42: Use pre-experiment data (CUPED) to adjust results, reducing variance and requiri...
**Claim:** Use pre-experiment data (CUPED) to adjust results, reducing variance and requiring fewer users for the same statistical power.
**Framework:** CUPED
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** ronny-kohavi
**Context:** Ronny mentions CUPED as a third technique for variance reduction.

## Insight 43: Replace PowerPoint presentations with structured narratives (like Amazon's six-p...
**Claim:** Replace PowerPoint presentations with structured narratives (like Amazon's six-pager) to improve feedback and documentation.
**Framework:** Structured narrative
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Ronny shares a minor change that had big impact: using structured documents instead of PowerPoint.

## Insight 44: Teach the hierarchy of evidence to family and friends to help them critically ev...
**Claim:** Teach the hierarchy of evidence to family and friends to help them critically evaluate claims: anecdotes are least trustworthy, controlled experiments most.
**Framework:** Hierarchy of evidence
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** ronny-kohavi
**Context:** Ronny's advice on applying experimentation mindset to life, emphasizing trust levels of evidence.

## Insight 45: Observational studies are often directionally incorrect; control experiments pro...
**Claim:** Observational studies are often directionally incorrect; control experiments provide more reliable evidence.
**Framework:** Hierarchy of evidence
**Audience:** general | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Discussion about observational studies vs. control experiments

## Insight 46: Share the idea of the hierarchy of evidence with family, kids, and friends....
**Claim:** Share the idea of the hierarchy of evidence with family, kids, and friends.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.8
**Source:** ronny-kohavi
**Context:** Ronny suggests sharing the concept of evidence hierarchy with others

## Insight 47: Use control experiments as a mechanism to make right data-driven decisions....
**Claim:** Use control experiments as a mechanism to make right data-driven decisions.
**Framework:** Control experiments
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Ronny's final request to listeners

## Insight 48: Learn more by reading Ronny's book (proceeds go to charity)....
**Claim:** Learn more by reading Ronny's book (proceeds go to charity).
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.8
**Source:** ronny-kohavi
**Context:** Ronny mentions his book and that proceeds go to charity

## Insight 49: Take Ronny's class on Maven (discount available for podcast listeners)....
**Claim:** Take Ronny's class on Maven (discount available for podcast listeners).
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** ronny-kohavi
**Context:** Ronny mentions his Maven class and discount for listeners
