---
title: Analytics
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [concept, analytics, data, metrics]
sources:
  - lenny-2025-08-31-howie-liu
  - lenny-2025-09-18-brendan-foody
  - lenny-2025-10-05-albert-cheng
  - lenny-2025-11-02-melanie-perkins
confidence: high
---

# Analytics

## Synthesis

1. **Analytics should answer questions, not just produce dashboards.** Howie Liu (Airtable) describes the shift from "data reporting" to "data-informed decision-making." The best analytics orgs start with a decision that needs to be made and work backward to the data needed. Dashboards without decision frameworks are noise.

2. **North Star metrics align the entire organization around a single outcome.** Melanie Perkins (Canva) discusses how Canva's North Star metric — "weekly active creators" — focuses every team on the same outcome. A good North Star is a leading indicator of long-term value, not a lagging one. It should be influenced by every team but owned by none.

3. **AI evals are the new analytics for AI products.** Brendan Foody (Mercor) explains that traditional product analytics break down for AI products because outputs are non-deterministic. The fastest-growing AI companies invest heavily in evaluation frameworks — expert-written test suites that measure model output quality, safety, and alignment.

4. **Cohort analysis reveals the truth that aggregate metrics hide.** Albert Cheng (Duolingo) emphasizes that aggregate metrics like DAU/MAU can mask declining cohort quality. A company can have flat total usage while each new cohort retains worse than the last. Cohort-level retention analysis is the most important analytic tool for understanding product health.

5. **Data democratization accelerates decision-making but requires governance.** Multiple guests note that giving every team member access to data speeds up decisions but creates risks: conflicting metric definitions, data cherry-picking, and analysis paralysis. The solution: a single source of truth for key metrics with clear definitions and ownership.

## Key Disagreements

- **Self-serve analytics vs. centralized data team:** Debate over whether data should be democratized to all teams or controlled by a central analytics function.
- **Quantitative vs. qualitative priority:** Some argue quantitative data should always drive decisions; others emphasize that qualitative insights often reveal what metrics miss.
- **Real-time vs. batch analytics:** Whether real-time dashboards provide enough incremental value over daily or weekly reports to justify the infrastructure cost.

## Related Concepts

- [[metrics]], [[growth]], [[ab-testing]], [[retention]], [[activation]], [[product-led-growth]], [[ai-ml]], [[evals]]
