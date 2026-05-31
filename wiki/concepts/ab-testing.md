---
title: A/B Testing
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [concept, experimentation, growth, analytics]
sources:
  - lenny/ronny-kohavi
  - lenny/ramesh-johari
  - lenny/lauryn-isford
  - lenny/tim-holley
confidence: high
---

# A/B Testing

## Synthesis

1. **Test everything — any code change should be in an experiment.** Ronny Kohavi (Airbnb, Microsoft, Amazon) is the world's leading expert on controlled experiments at scale. His mantra: "Test everything." At Microsoft, he found that a third of experiments that teams expected to improve metrics actually hurt them. A/B testing is not just optimization — it's risk prevention.

2. **Failed experiments are valuable data, not failures.** Ramesh Johari (Stanford) introduces the concept of Bayesian priors in experimentation. Each experiment, even a "failed" one, updates your understanding of what works. Companies that celebrate well-run experiments regardless of outcome build a stronger experimentation culture than those that reward only wins.

3. **Statistical significance is necessary but not sufficient for decision-making.** Ronny Kohavi emphasizes that many teams misuse p-values and sample size calculations. The more dangerous mistake: launching changes based on statistically significant but practically irrelevant effects. A 0.1% improvement in a secondary metric doesn't justify a product launch.

4. **Experimentation culture starts with leadership, not tools.** Lauryn Isford (Airtable) describes how the best experimentation cultures exist at companies where leadership asks "what does the data say?" before making decisions. Tools are table stakes; the culture of hypothesis-driven decision-making is the moat.

5. **Long-term effects often differ from short-term A/B test results.** Tim Holley (Etsy) notes that some changes improve metrics in the first week but degrade them over time (novelty effects). The best organizations run long-duration experiments and track delayed outcomes like retention and lifetime value.

## Key Disagreements

- **Bayesian vs. frequentist statistics:** Debate over which statistical framework is more appropriate for product experimentation.
- **Holdout groups:** Some recommend permanent holdout groups to measure long-term effects; others consider them wasteful.
- **Experimentation at startups:** Some say startups should A/B test everything; others argue early-stage companies should prioritize speed over rigor.

## Related Concepts

- [[analytics]], [[growth]], [[metrics]], [[activation]], [[retention]], [[product-development]], [[data-driven]], [[onboarding]]
