# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-05-30] restructure | Converted to Karpathy LLM Wiki architecture
- Adopted 3-layer structure: raw/ (immutable), wiki/ (LLM-owned), SCHEMA.md
- Raw transcripts: 351 Lenny + 1,462 20VC + 10 newsletters moved to raw/transcripts/
- SCHEMA.md written with domain conventions, tag taxonomy, page thresholds, update policy
- Proper wiki frontmatter: title, created, updated, type, tags, sources, confidence
- Wiki directories created: entities/, concepts/, comparisons/, queries/, _archive/
- Legacy layers (episodes/, guests/, topics/) preserved for backward compatibility
- Semantic search index rebuilt: 13,445 chunks from 1,823 episodes

## [2026-05-30] ingest | Elena Verna (Lovable) — The AI growth playbook for 2026
- Created [[elena-verna]] entity page with key frameworks, growth stats, notable quotes
- Created [[ai-growth-playbook]] concept page with the 95/5 innovation split, building in public, capability→value→scale framework
- Cross-references: [[Miro]], [[Netlify]], [[Amplitude]], [[Adam Fishman]], [[John Cutler]], [[Gaurav]], [[Mirage]]

## [2026-05-30] ingest | Rachel Lockett — Difficult conversations and talent decisions
- Created [[rachel-lockett]] entity page with Stripe's enthusiastic rehire test, NVC framework, GROW technique, one-page plan
- Created [[talent-decision-framework]] concept page — synthesis across Rachel Lockett, Alisa Cohn, and Carilu Dietrich
- Cross-references: [[Stripe]], [[Netflix]], [[Jerry Colonna]], [[Alisa Cohn]], [[Carilu Dietrich]]

## [2026-05-30] query | filed | Managing an employee holding the company back
- Answer compiled from [[rachel-lockett]], [[alisa-cohn]], [[carilu-dietrich]]
- Filed as [[talent-decision-framework]]


## [2026-05-31 08:23] ingest | Bulk migration from guest/topic stubs
- Pages created: 10
- Details: entity: 10 (Aaron Hirschhorn, Aaron Levie, Aaron Vandevender, Aatish Nayak, Ada...)

## [2026-05-31 08:23] ingest | Bulk migration from guest/topic stubs
- Pages created: 1040
- Details: entity: 1040 (Adam Gross, Adam Pritzker, Adam, Adarsh Hiremath, Additional Leverage...)

## [2026-05-31 08:23] ingest | Bulk migration from guest/topic stubs
- Pages created: 180
- Details: concept: 180 (Ab Testing, Acquisition, Activation, Analytics, Churn...)

2026-05-31 | Created synthesis-quality-standard concept page — quality benchmark for good answers. Exemplar: 19-year-old AI career advice. Includes anti-patterns list and evaluation criteria.
