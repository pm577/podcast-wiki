---

title: Ronny Kohavi
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: ['person', 'experimentation', 'a-b-testing', 'data-science', 'product-growth', 'platform']
sources:
  - raw/transcripts/lenny/ronny-kohavi.md
confidence: high
key_finding: "Most ideas fail — and that's humbling"
subtype: person
---

# Ronny Kohavi

Ronny Kohavi appeared on Lenny's Podcast to discuss the ultimate guide to a/b testing.

## Key Views

**Most ideas fail — and that's humbling** — Across three major companies Ronny reveals the stark reality: roughly two-thirds of ideas fail at Microsoft overall, 85% at Bing (a mature optimization domain), and 92% at Airbnb search relevance. Every new team believes they'll be the exception. "Overall at Microsoft, about 66%, two thirds of ideas fail. At Bing, which is a much more optimized domain after we've been optimizing it for a while, the failure rate was around 85%. So it's harder to improve something that you've been optimizing for a while. And then at Airbnb, this 92% number is the highest failure rate that I've observed… Very humbling. I know that every group that starts to run experiments, they always start off by thinking that somehow, they're different. And their success rate's going to be much, much higher, and they're all humbled." ^[raw/transcripts/lenny/ronny-kohavi.md]

**Twyman's Law — too good to be true is probably wrong** — When an experiment shows an astonishing result, the most likely explanation is a flaw in the experiment, not a breakthrough. Ronny advises immediate skepticism over celebration — nine out of ten extreme-looking results turn out to be invalid. "If the result looks too good to be true, your normal movement of an experiment is under 1% and you suddenly have a 10% movement, hold the celebratory dinner… Hold that dinner, investigate, see, because there's a large probability that something is wrong with the result. And I will say that nine out of 10, when we call it Twyman's law, it is the case that we find some flaw in the experiment." ^[raw/transcripts/lenny/ronny-kohavi.md]

**The OEC must predict lifetime value** — Rather than optimizing for short-term revenue (which can be gamed), the Overall Evaluation Criterion should be causally predictive of a user's lifetime value, forcing teams to consider long-term health. "To me, the key word is lifetime value, which is you have to define the OEC such that it is causally predictive of the lifetime value of the user. And that's what causes you to think about things properly, which is, am I doing something that just helps me short term, or am I doing something that will help me in the long term?" ^[raw/transcripts/lenny/ronny-kohavi.md]

**Test everything — you need a portfolio of bets** — Ronny advocates putting every code change into an experiment and treating your idea pipeline like an investment portfolio: some resources go to incremental improvements, but some must be allocated to high-risk, high-reward bets that are likely to fail but could be home runs. "I'm very clear that I'm a big fan of test everything, which is any code change that you make, any feature that you introduce has to be in some experiment. Because again, I've observed this surprising result that even small bug fixes, even small changes can sometimes have surprising unexpected impact." ^[raw/transcripts/lenny/ronny-kohavi.md]

**Experiment more during crisis, not less** — Countering the instinct to abandon data-driven decision-making in times of upheaval, Ronny argues that if teams are wrong 66-80% of the time in peacetime, there is no reason to believe they would be right during a crisis — making experiments even more critical. "If in peace time you're wrong two thirds to 80% of the time, why would you be subtly right in wartime, in Covid time? So I don't believe in the idea that because bookings went down materially, the company should suddenly not be data driven and do things differently." ^[raw/transcripts/lenny/ronny-kohavi.md]

## Related Concepts

- [[product-management]]
- [[startups]]
- [[leadership]]

---

*Merged from [[ronny]]:*

# Ronny Kohavi

Ronny Kohavi, PhD, is widely considered the world's leading expert on A/B testing and experimentation. He was VP and Technical Fellow at Airbnb (leading search relevance), Corporate VP at Microsoft (leading the Microsoft Experimentation Platform), and Director of Data Mining and Personalization at Amazon. He is the author of *Trustworthy Online Controlled Experiments* and teaches a live cohort-based course on experimentation.

## Key Views

### 80-90% of Ideas Fail — and That's Normal

Across Ronny's career, failure rates of experiments are consistently 66% (Microsoft overall), 85% (Bing, optimized domain), and 92% (Airbnb search relevance). "Every group that starts to run experiments always starts off by thinking somehow they're different and their success rate's going to be much higher — and they're all humbled." The corollary: build an experimentation culture that celebrates learning from failures, not just winners.^[raw/transcripts/lenny/ronny-kohavi.md]

### Trivial Changes Can Produce Massive Wins

The most impactful experiment in Bing's history was a trivial change: moving the second line of an ad to the first line (increasing the title font size). It took a couple of days to implement and increased revenue by 12% — worth $100M at the time. The idea had languished on the backlog for months because nobody believed it would work. "We are often humbled by how bad we are at predicting the outcome of experiments."^[raw/transcripts/lenny/ronny-kohavi.md]

### Open in New Tab: A Reusable Pattern

The "open in new tab" pattern worked across multiple companies — first at Microsoft (Hotmail, MSN Search), then independently rediscovered at Airbnb for search listings. Ronny compiled these patterns into a "Rules of Thumb" paper and recommends goodui.org as a repository of 140+ tested patterns. Institutional memory is crucial: document surprising experiments quarterly.^[raw/transcripts/lenny/ronny-kohavi.md]

### The Overall Evaluation Criterion (OEC)

Ronny emphasizes defining a single OEC (overall evaluation criterion) that balances multiple metrics. At Bing, search relevance improvements of ~2% per year came from many tiny 0.1-0.2% wins adding up. Most wins come "inch by inch" — not from home runs. But you need guardrail metrics too: the Windows indexer improved relevance but killed laptop battery life.^[raw/transcripts/lenny/ronny-kohavi.md]

### Experimentation Is Not Anti-Innovation

Ronny pushes back on the idea that experimentation leads to micro-optimization at the expense of big innovation. He advocates allocating resources to "high risk, high reward ideas" — things "most likely to fail, but if it does win, it's going to be a home run." The platform enables innovation by providing fast feedback on whether bold ideas actually work, and by documenting surprising results for institutional learning.^[raw/transcripts/lenny/ronny-kohavi.md]

## Episode Appearances

- [[lenny/ronny-kohavi]] — The ultimate guide to A/B testing

## Related Concepts

- [[a-b-testing]]
- [[experimentation]]
- [[data-science]]
- [[growth]]
- [[metrics]]
