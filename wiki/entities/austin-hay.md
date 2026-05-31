---

title: Austin Hay
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: ['person', 'growth', 'marketing-technology', 'martech', 'data', 'analytics']
sources:
  - raw/transcripts/lenny/austin-hay.md
confidence: medium
key_finding: MarTech Is Product Management for Your Marketing Systems
subtype: person
---

# Austin Hay

Austin Hay is Head of Marketing Technology at Ramp. Previously he was VP of Business Operations at Runway, VP of Growth at mParticle, and the fourth employee at unicorn Branch Metrics. He teaches MarTech at Reforge and has advised Notion, Airbnb, Walmart, Postmates, and Robinhood on their marketing technology strategies.

## Key Views

**MarTech Is a Product Management Discipline for Systems** — Marketing technology lives at the crossroads of product, growth, engineering, and marketing. It's a product manager whose specific focus is the system — both third-party tools and first-party homegrown platforms. The job is people, process, systems, and platforms — exactly like product management, but for the marketing stack. ^[raw/transcripts/lenny/austin-hay.md]

**The Death of Deterministic Matching** — From 2010-2020, marketers had golden years of deterministic matching (IDFA tied to PII). Now, ad networks have become more complex while it's harder to understand exactly where customers come from. The new skill is making decisions with probabilistic data — building models from 30% of the population and extrapolating to 100%. ^[raw/transcripts/lenny/austin-hay.md]

**MarTech Organization Depends on Company Stage** — At early stage, one person handles all MarTech (email, analytics, ads, attribution) as a generalist. As companies grow, MarTech splits into specialties: lifecycle marketing, growth engineering, data engineering, and platform teams. The inflection point is around 50-100 people when a dedicated MarTech hire becomes essential. ^[raw/transcripts/lenny/austin-hay.md]

**Preferred Tools Stack** — Austin's recommended stack includes: Segment or mParticle for CDP, Braze or Customer.io for lifecycle, Mixpanel or Amplitude for analytics, Google Ads and Meta for paid, and Airflow or dbt for data engineering. The key is having a clean, well-instrumented data layer that connects all tools. ^[raw/transcripts/lenny/austin-hay.md]

**The Best Interview Question for MarTech Hires** — Ask candidates to design the ideal MarTech stack for a hypothetical company at a specific stage. This tests systems thinking, understanding of tool tradeoffs, and ability to prioritize. Great answers include migration paths, cost considerations, and how the stack evolves as the company scales. ^[raw/transcripts/lenny/austin-hay.md]

## Episode Appearances

- [[lenny/austin-hay|The ultimate guide to MarTech | Austin Hay (Reforge, Ramp, Runway)]] — Marketing technology strategy, tools, and team building

## Related Concepts

- [[growth]]
- [[marketing-technology]]
- [[data]]
- [[analytics]]
- [[product-management]]

---

*Merged from [[austin]]:*

# Austin Hay

**Role:** Head of Marketing Technology at Ramp; former VP of Business Operations at Runway, VP of Growth at mParticle; Reforge instructor on MarTech; advisor to Notion, Airbnb, Walmart, Postmates  
**Known for:** Being one of the foremost experts on Marketing Technology (MarTech), the "tools are meant to solve problems" philosophy, the PPS (Problem-People-System) framework, and the "Build AND Buy" approach to system architecture.

## Key Views

### 1. MarTech defined: the cross-functional PM for internal systems

Austin defines Marketing Technology as an "amorphous, cross-functional discipline at the crossroads of product, growth, engineering, and marketing." It's not just managing third-party tools — it's designing, architecting, and building first-party solutions on top of third-party platforms. As companies grow from ~30 to 150+ people, a "village approach" to managing tools breaks down, and a dedicated MarTech person becomes essential. The role is equal parts IC (deepest technical expert on all systems) and cross-functional quarterback (persuading product, data, and engineering to align).

> "At some point as you scale and you're starting to make money, you start to care more about not just how much money you're making but how much money you're losing from SaaS tools." — Austin Hay

### 2. The PPS framework: Problem → People → System — not the other way around

Austin's core framework for any MarTech decision: start with the **problem**, then the **people** involved, then the **system**. Most people jump straight to "I need this tool." Instead, understand: what's the real problem? Who needs to be involved (who needs to give permission? who needs training?)? Only then design the system. This prevents buying tools that solve the wrong problem and avoids creating technical debt from premature architecture decisions.

> "So whenever there's a challenge that comes up … I like to first say what's the problem? Who are the people involved and what system does it impact?" — Austin Hay

### 3. Build AND Buy, not Build vs. Buy

Austin advocates for "Build and Buy" as a consensus-driven approach over the narrow "Build vs. Buy" decision tree. Buy the third-party tool to get 90% of the way there, then build the custom 10% on top to make it truly your own. This creates a partnership with vendors (who are invested in your success) while still delivering differentiation. He uses financial modeling to show that buying at the lowest possible cost and focusing internal engineering on building around the tool often yields more value than building everything in-house.

> "It's B and B as opposed to BVB. … Build and buy means that both of you can win and you can actually create a solution that is not only unique but saves the company time and resources." — Austin Hay

### 4. Thinking Gray: the power of delayed decisions

Inspired by Steven B. Sample's *The Contrarian's Guide to Leadership*, Austin practices "thinking gray" — actively resisting the pressure to decide until you absolutely must. In systems thinking, this means not jumping to a tool selection, org design, or architecture decision before you have enough information. In people evaluation, it means leaving space to change your impression of someone rather than making snap judgments. Patience is the discipline behind it — hard for most people but enormously valuable for avoiding premature commitment to the wrong solution.

> "The concept of thinking gray is actually to not decide for as long as you possibly can before you have to decide." — Austin Hay

### 5. The Golden Stack: B2C and B2B MarTech reference architectures

Austin shares a practical, opinionated stack: **For B2C**: Amplitude (CDP + product analytics), Customer.io (email, upgrade to Braze later), Snowflake (warehouse), Hightouch (reverse ETL to ad networks), AppsFlyer (mobile attribution). **For B2B**: Same base stack but swap AppsFlyer for Branch (web attribution), connect everything to Salesforce, and use Customer.io for as long as possible before migrating to Braze. The golden principle: tools are just meant to solve problems — don't over-rotate on the tool choice; focus on whether it solves your actual problem.

> "Tools are just meant to solve problems. … If you consistently remind yourself that tools are just meant to solve problems, then you really get into a space where you as a systems person can be an advocate for your marketer or your product people." — Austin Hay

## Episode Appearances

- [[lenny/austin-hay|The ultimate guide to Martech | Austin Hay (Reforge, Ramp, Runway)]] — MarTech roles and org design, PPS framework, Build and Buy, Golden Stack

## Related Concepts

- [[growth]]
- [[marketing-technology]]
- [[data-infrastructure]]
- [[saas-tools]]
- [[product-operations]]
