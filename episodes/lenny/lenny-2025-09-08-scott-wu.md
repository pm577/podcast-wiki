---
episode_date: '2025-09-08'
guest: scott-wu
id: lenny-2025-09-08-scott-wu
key_insights:
- 'Scott Wu: Our whole team is only like 15 engineers a year. We use a ton of Devin
  when we''re building Devin. Most folks on the team are definitely working with up
  to five Devins at once, and so Devin merges like...'
- 'Brandon Foo: Integrations are mission-critical for AI for two reasons. First, AI
  products need contacts from their customer''s business data such as Google Drive
  files, Slack messages or CRM records. Second, for AI...'
podcast: lenny
tags:
- pricing
- saas
- startups
- ai-ml
- marketplace
- product-led-growth
- leadership
- hiring
title: How Devin replaces your junior engineers with infinite AI interns that never
  sleep | Scott Wu (Cognition CEO)
type: Episode
word_count: 19675
---

# How Devin replaces your junior engineers with infinite AI interns that never sleep | Scott Wu (Cognition CEO)

How Devin replaces your junior engineers with infinite AI interns that never sleep, covering AI product work, product design, and engineering tradeoffs.

**Guest:** Scott Wu
**Date:** 2025-09-08
**YouTube:** https://www.youtube.com/watch?v=7m_xKFqSxTo
**Topics:** pricing, saas, startups, ai-ml, marketplace, product-led-growth, leadership, hiring, retention, fundraising

## Key Topics Discussed

- [[pricing]]
- [[saas]]
- [[startups]]
- [[ai-ml]]
- [[marketplace]]
- [[product-led-growth]]
- [[leadership]]
- [[hiring]]
- [[retention]]
- [[fundraising]]

## Transcript Highlights

**Scott Wu:** Our whole team is only like 15 engineers a year. We use a ton of Devin when we're building Devin. Most folks on the team are definitely working with up to five Devins at once, and so Devin merges like several hundred pull requests into production in the Devin code bases every month.

**Lenny Rachitsky:** What percentage of your PRs are Devin versus humans right now?

**Scott Wu:** It's in the neighborhood of a quarter or so.

**Lenny Rachitsky:** Where do you think this will be at the end of the year?

**Scott Wu:** Honestly, we expect it to be a decent bit more than half.

**Lenny Rachitsky:** You guys are so ahead of how companies work with AI engineers.

**Scott Wu:** AI is going to be the biggest technology shift of our lives, so most of the big tech revolutions that we've had over the last 50 years, like personal computer, and the internet, and the mobile phone, they all had this big hardware component that was a big part of the distribution. Folks who were building for those industries kind of saw their market grow and grow and grow basically steadily year over year as the number of people with mobile phones increased, right, as the number of people connected to the internet increase. One of the things which is already I'd say different in AI, is just how explosive the technology can be. There's no weight on hardware distribution. It means that the space is just growing so exponentially.

**Lenny Rachitsky:** How is the act of being an engineer and building changing?

**Scott Wu:** I think there's going to be way more programmers and way more engineers a few years from now. Pretty quickly. The form factor of what it means to be a programmer obviously is going to change, but at the end of the day, of course the discipline is all about just being able to tell your computer what's do. And so in that lens, I really think that programming is only going to become more and more important as AI gets more powerful.

**Lenny Rachitsky:** Today my guest is Scott Wu. Scott is the co-founder and CEO of Cognition, which makes a product called Devin, the world's first autonomous AI software engineer. Unlike other AI tools that I've highlighted on this podcast, Devin is designed to act like an actual remote engineer that you chat with like you would with any other human engineer through Slack or through its dedicated website. When Devin launched about a year ago, it was very much a junior engineer. Over the past year, they've made a lot of progress and Devin is now being used by tons of companies in production. We chatted about how their engineering team of 15 uses Devins to build Devin, including how every engineer uses about five Devins each to help them code and move faster. How a quarter of their pull requests today are committed by Devins and that they expect this to be over 50% by the end of the year.

**Lenny Rachitsky:** We also talk about how Scott imagines software engineering is going to look in the future and how the role of an engineer changes from a coder to an architect. We also get into the eight pivots that they went through before landing on this path, why Scott believes AI tools like this will lead to more engineer hiring versus less. Also where the name Devin comes from and so much more. This episode is going to blow your mind. I highly recommend you listen to it if you're at all interested about where engineering, product building, and AI is going. A huge thank you to Claire Voue for suggesting a bunch of great questions for this conversation.

**Brandon Foo:** Hey Lenny. Thanks for having me.

**Lenny Rachitsky:** So integrations have become a big deal for AI products. Why is that?

**Brandon Foo:** Integrations are mission-critical for AI for two reasons. First, AI products need contacts from their customer's business data such as Google Drive files, Slack messages or CRM records. Second, for AI products to automate work on behalf of users, AI agents need to be able to take action across these different third-party tools.

**Lenny Rachitsky:** So where does Paragon fit into all this?

**Brandon Foo:** Well, these integrations are a pain to build and that's why Paragon provides an embedded platform that enables engineers to ship these product integrations in just days instead of months across every use case from RAG data ingestion to agentic actions.

**Lenny Rachitsky:** And I know from firsthand experience that maintenance is even harder than just building it for the first time.

**Brandon Foo:** Exactly. We believe product teams should focus engineering efforts and competitive advantages, not integrations. That's why companies like You.com, AI21 and hundreds of others use Paragon to accelerate their integration strategy.

**Lenny Rachitsky:** If you want to avoid wasting months of engineering on integrations that your customers need, check out paragon@useparagon.com/lenny. Scott, thank you so much for being here and welcome to the podcast.

**Scott Wu:** Thanks so much for having me. Excited to be on.

**Lenny Rachitsky:** I'm really excited to have you here because you are building and you've been building something that is very different from what a lot of other AI companies have been doing for a long time, although they are starting to converge to where you guys are now. We're going to talk about that and it's also just such a unique point in the history of AI and just the journey of AI. And so it's really cool to be chatting right now. And I feel like we're going to chat again in a few years and be like, wow, we were so right about so much and so wrong about so much.

**Scott Wu:** Yeah.

**Lenny Rachitsky:** And so I'm excited to have you here. Let's start with talking about Devin, giving people an understanding of just what the heck Devin is, is the main product that you guys build. What is the simplest way to understand what is Devin?

**Scott Wu:** Absolutely. And so Devin is a fully autonomous software engineer that is going to work on tasks end to end, and so there are a lot of great tools for all parts of the stack of the AI code workflow. What Devin does is it is a full asynchronous workflow, and so you can tag Devin on an issue in Slack, you're talking about an issue and you tag Devin, you can tag Devin in Linear, you can have Devin and Devin will make pull requests in your GitHub, and so it's very much built to work with engineering teams as your junior engineer.

**Lenny Rachitsky:** Amazing, okay. So I remember when you guys launched this, there was this big pitch of this is your new AI engineer and it was really good at a lot of stuff. It wasn't great at other things. It's been a year now about since you guys launched, is that right?

**Scott Wu:** Yeah, yeah.

**Lenny Rachitsky:** What's the best way to think about the level of seniority that engineer had back in the day when you guys launched and then the level of seniority of engineer today if that's, I don't know, measure of how to think about Devin?

**Scott Wu:** Yeah, and it's crazy to think about by the way, because a year ago when we did the initial launch, I mean people didn't really believe that an agent was possible. Right. And it was, I mean, it was a very different time. So like start of 2024, things with model capabilities were definitely quite a bit earlier on, reasoning especially was quite a bit earlier on. And yeah, I mean, in the time since then it's obviously developed a lot. I think in terms of practical skills, there's some comparisons we make. Sometimes we kind of say, well, when we got started it was kind of like a high school CS student and then as time went on, it became more of a college intern and now it's like a junior engineer. But I would say though that those are more rough guidelines because I really like the phrase jagged intelligence for example, because obviously there are certain things that it is much better at than a human. There are certain things that it's much worse at than a human.

**Scott Wu:** And I think over the last year we've learned a lot especially about not just coding agents but agents in general just really building out how all of us should be working and interacting with agents as part of our flow. And so a lot of the things that we built, I mean, there was no Slack, there was no GitHub integration, there was no Linear, there was no interactive planning phase working back and forth. There was no way to touch up Devin's code. And so a lot of the features that we've built on the product side since then have really been about basically yeah, figuring out how to make working with Devin and handing off tasks to Devin as smooth of an experience as possible.

**Lenny Rachitsky:** That's so interesting. So a lot of the work has gone not into how do we just make Devin the best possible engineer, but it's how to work with this new type of entity that we haven't ever worked with.

