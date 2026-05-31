# Podcast Wiki Schema

A Karpathy-style LLM-maintained knowledge base for Lenny's Podcast, 20VC, and Lenny's Newsletter. The LLM (Clio) owns all wiki content. Human curates sources and directs analysis.

## Domain

Startup and product management intelligence — growth, fundraising, product strategy, leadership, AI/ML, go-to-market, hiring, culture, and venture capital. Covers ~1,800+ episodes from Lenny's Podcast and 20VC.

## Three Layers

```
podcast-wiki/
├── SCHEMA.md              # This file — conventions and rules
├── index.md               # Content catalog — every page listed with summary
├── log.md                 # Chronological action record
│
├── raw/                   # Layer 1: Immutable source material
│   └── transcripts/       # Raw episode transcripts (immutable, never modified)
│       ├── lenny/         #   Lenny's Podcast transcripts
│       ├── 20vc/          #   20VC show notes
│       └── newsletters/   #   Lenny's Newsletter posts
│
├── wiki/                  # Layer 2: The wiki — LLM-owned content
│   ├── entities/          #   People, companies, products
│   ├── concepts/          #   Ideas, frameworks, strategies, topics
│   ├── comparisons/       #   Side-by-side analyses
│   ├── queries/           #   Valuable filed queries
│   └── _archive/          #   Superseded content
│
├── episodes/              # (legacy) Episode pages by source — will be migrated
├── guests/                # (legacy) Guest profiles
├── topics/                # (legacy) Topic pages
├── scripts/               # Utility scripts
└── data/                  # FAISS index and chunks
```

## Conventions

- **File names:** lowercase, hyphens, no spaces (e.g., `product-led-growth.md`)
- **Every wiki page** must have YAML frontmatter (see below)
- **Use `[[wikilinks]]`** to link between pages — minimum 2 outbound links per page
- **Bump `updated`** date every time a page is modified
- **Every new page** must be added to `index.md` under the correct section
- **Every action** must be appended to `log.md`
- **Never modify raw/ files** — sources are immutable. Corrections go in wiki pages.
- **Markdown links `[label](path.md)` do NOT create wiki cross-references.** Always add `[[wiki-link]]` alongside markdown links.

## Frontmatter

Every wiki page MUST start with:

```yaml
---
title: Episode Title or Entity Name
created: YYYY-MM-DD         # When this page was first created
updated: YYYY-MM-DD         # Last modification date
type: episode | entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/transcripts/lenny/episode-slug.md]
confidence: high | medium | low
---
```

- `confidence` is optional but recommended. `high` = supported across 3+ sources, `medium` = 1-2 good sources, `low` = single source or speculative.
- Raw source files also get frontmatter: `source_url`, `ingested`, `sha256`

## Tag Taxonomy

All tags must come from this list. Add new tags here before using them.

### People & Orgs
- person, company, investor, founder, executive, vc-firm

### Product & Growth  
- product-strategy, growth, onboarding, retention, monetization, pricing, PLG, go-to-market, saas, marketplace, consumer, enterprise

### Leadership & Culture
- leadership, hiring, culture, team-building, management, remote, diversity, coaching

### AI & Technology
- ai-ml, llm, agents, AI-product, AI-infrastructure, prompt-engineering, evals, code-generation

### Fundraising & Finance
- fundraising, venture-capital, pitch-deck, valuation, unit-economics, revenue, bootstrapping

### Marketing & Sales
- marketing, sales, brand, content-marketing, social-media, community, SEO, PR

### Meta
- comparison, interview, AMA, year-in-review, prediction, controversy, framework, mental-model

## Page Thresholds

- **Create an entity page** when a person/company appears in 2+ episodes OR is the main guest
- **Create a concept page** when a topic is discussed across 3+ episodes with substantive depth
- **Skip** passing mentions, minor details, things outside startup/product domain
- **Split** a page when it exceeds ~200 lines
- **Archive** superseded content to `_archive/`

## Update Policy

When new information conflicts with existing content:
1. Newer sources generally supersede older ones (check dates)
2. If genuinely contradictory, note both positions with dates and sources
3. Mark contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for human review

## Entity Pages

One page per notable person or company. Per Karpathy pattern, include:
- Overview / who they are
- Key views and opinions (with [[wikilinks]] to episodes)
- Relationships to other entities
- Source references with ^[raw/transcripts/...] provenance markers

## Concept Pages

One page per concept or framework. Include:
- Definition / explanation
- Current synthesis across all sources
- Key disagreements or open questions
- Related concepts

## Comparison Pages

Side-by-side analyses of people, companies, or approaches.
- Dimensions of comparison
- Verdict or synthesis

## Query Pages

When someone asks a great question, file the answer. Include:
- The question as title
- Synthesis across relevant pages
- Sources
- Date asked
