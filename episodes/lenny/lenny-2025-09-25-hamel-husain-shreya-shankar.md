---
episode_date: '2025-09-25'
guest: hamel-husain-shreya-shankar
id: lenny-2025-09-25-hamel-husain-shreya-shankar
key_insights:
- 'Hamel Husain: This process is a lot of fun. Everyone that does this immediately
  gets addicted to it. When you''re building an AI application, you just learn a lot....'
- 'Shreya Shankar: The goal is not to do evals perfectly, it''s to actionably improve
  your product....'
podcast: lenny
tags:
- ai-ml
- saas
- leadership
- hiring
- startups
title: 'Why AI evals are the hottest new skill for product builders | Hamel Husain
  & Shreya Shankar (creators of the #1 eval course)'
type: Episode
word_count: 19671
---

# Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar (creators of the #1 eval course)

Why AI evals are the hottest new skill for product builders, covering AI product work, product design, and measurement and analysis.

**Guest:** Hamel Husain & Shreya Shankar
**Date:** 2025-09-25
**YouTube:** https://www.youtube.com/watch?v=BsWxPI9UM4c
**Topics:** ai-ml, saas, leadership, hiring, startups

## Key Topics Discussed

- [[ai-ml]]
- [[saas]]
- [[leadership]]
- [[hiring]]
- [[startups]]

## Transcript Highlights

**Lenny Rachitsky:** To build great AI products, you need to be really good at building evals. It's the highest ROI activity you can engage in.

**Hamel Husain:** This process is a lot of fun. Everyone that does this immediately gets addicted to it. When you're building an AI application, you just learn a lot.

**Lenny Rachitsky:** What's cool about this is you don't need to do this many, many times. For most products, you do this process once and then you build on it.

**Shreya Shankar:** The goal is not to do evals perfectly, it's to actionably improve your product.

**Lenny Rachitsky:** I did not realize how much controversy and drama there is around evals. There's a lot of people with very strong opinions.

**Shreya Shankar:** People have been burned by evals in the past. People have done evals badly, so then they didn't trust it anymore, and then they're like, "Oh, I'm anti evals."

**Lenny Rachitsky:** What are a couple of the most common misconceptions people have with evals?

**Hamel Husain:** The top one is, "We live in the age of AI. Can't the AI just eval it?" But it doesn't work.

**Lenny Rachitsky:** A term that you used in your posts that I love is this idea of a benevolent dictator.

**Hamel Husain:** When you're doing this open coding, a lot of teams get bogged down in having a committee do this. For a lot of situations, that's wholly unnecessary. You don't want to make this process so expensive that you can't do it. You can appoint one person whose taste that you trust. It should be the person with domain expertise. Oftentimes, it is the product manager.

**Lenny Rachitsky:** Today, my guests are Hamel Husain and Shreya Shankar. One of the most trending topics on this podcast over the past year has been the rise of evals. Both the chief product officers of Anthropic and OpenAI shared that evals are becoming the most important new skill for product builders. And since then, this has been a recurring theme across many of the top AI builders I've had on. Two years ago, I had never heard the term evals. Now it's coming up constantly. When was the last time that a new skill emerged that product builders had to get good at to be successful?

**Lenny Rachitsky:** Hamel and Shreya have played a major role in shifting evals from being an obscure, mysterious subject to one of the most necessary skills for AI product builders. They teach the definitive online course on evals, which happens to be the number one course on Maven. They've now taught over 2,000 PMs and engineers across 500 companies, including large swaths of the OpenAI and Anthropic teams along with every other major AI lab.

**Lenny Rachitsky:** In this conversation, we do a lot of show versus tell. We walk through the process of developing an effective eval, explain what the heck evals are and what they look like, address many of the major misconceptions with evals, give you the first few steps you can take to start building evals for your product, and also share just a ton of best practices that Hamel and Shreya have developed over the past few years. This episode is the deepest yet most understandable primer you'll find on the world of evals. And honestly, it got me excited to write evals, even though I have nothing to write evals for. I think you'll feel the same way as you watch this.

**Hamel Husain:** Thank you for having us.

**Shreya Shankar:** Yeah, super excited.

**Lenny Rachitsky:** I'm even more excited. Okay, so a couple years ago, I had never heard the term evals. Now it's one of the most trending topics on my podcast, essentially, that to build great AI products, you need to be really good at building evals. Also, it turns out some of the fastest-growing companies in the world are basically building and selling and creating evals for AI labs. I just had the CEO of Mercor on the podcast. So there's something really big happening here. I want to use this conversation to basically help people understand this space deeply, but let's start with the basics. Just what the heck are evals? For folks that have no idea what we're talking about, give us just a quick understanding of what an eval is, and let's start with Hamel.

**Hamel Husain:** Sure. Evals is a way to systematically measure and improve an AI application, and it really doesn't have to be scary or unapproachable at all. It really is, at its core, data analytics on your LLM application and a systematic way of looking at that data, and where necessary, creating metrics around things so you can measure what's happening, and then so you can iterate and do experiments and improve.

**Lenny Rachitsky:** So that's a really good broad way of thinking about it. If you go one level deeper just to give people a very, even more concrete way of imagining and visualizing what we're talking about, even if you have a example to show would be even better, what's an even deeper way of understanding what an eval is?

**Hamel Husain:** Let's say you have a real estate assistant application and it's not working the way you want. It's not writing emails to customers the way you want, or it's not calling the right tools, or any number of errors. And before evals, you would be left with guessing. You would maybe fix a prompt and hope that you're not breaking anything else with that prompt, and you might rely on vibe checks, which is totally fine.

**Hamel Husain:** And vibe checks are good and you should do vibe checks initially, but it can become very unmanageable very fast because as your application grows, it's really hard to rely on vibe checks. You just feel lost. And so evals help you create metrics that you can use to measure how your application is doing and kind of give you a way to improve your application with confidence. That you have a feedback signal in which to iterate against.

**Lenny Rachitsky:** So just to make very real, so imagining this real estate agent, maybe they're helping you book a listing or go see an open house. The idea here is you have this agent talking to people, it's answering questions, pointing them to things. As a builder of that agent, how do you know if it's giving them good advice, good answers? Is it telling them things that are completely wrong?

**Lenny Rachitsky:** So the idea of evals, essentially, is to build a set of tests that tell you, how often is this agent doing something wrong that you don't want it to do? And there's a bunch of ways you could define wrong. It could be just making up stuff. It could be just answering in a really strange way. The way I think about evals, and tell me if this is wrong, just simply is like unit tests for code. You're smiling. You're like, "No, you idiot."

**Shreya Shankar:** No, that's not what I was thinking.

**Lenny Rachitsky:** Okay. Okay, okay, tell me. Tell me, how does that feel as a metaphor?

**Shreya Shankar:** Okay. I like what you said first, which is we had a very broad definition. Evals is a big spectrum of ways to measure application quality. Now, unit tests are one way of doing this. Maybe there are some non-negotiable functionalities that you want your AI assistant to have, and unit tests are going to be able to check that. Now, maybe you also, because these AI assistants are doing such open-ended tasks, you kind of also want to measure how good are they at very vague or ambiguous things like responding to new types of user requests or figuring out if there's new distributions of data like new users are coming and using your real estate agent that you didn't even know would use your product. And then all of a sudden, you think, "Oh, there's a different way you want to kind of accommodate this new group of people."

**Shreya Shankar:** So evals could also be a way of looking at your data regularly to find these new cohorts of people. Evals could also be like metrics that you just want to track over time, like you want to track people saying, "Yes. Thumbs up. I liked your message." You want very, very basic things that are not necessarily AI-related but can go back into this flywheel of improving your product. So I would say, overall, unit tests are a very small part of that very big puzzle.

**Lenny Rachitsky:** Awesome. You guys actually brought an example of an eval just to show us exactly what the hell we're talking about. We're talking in these big ideas. So how about let's pull one up and show people, "Here's what an eval is."

**Hamel Husain:** Yeah, let me just set the stage for it a little bit. So to echo what Shreya said, it's really important that we don't think of evals as just tests. There's a common trap that a lot of people fall into because they jump straight to the test like, "Let me write some tests," and usually that's not what you want to do. You should start with some kind of data analysis to ground what you should even test, and that's a little bit different than software engineering where you have a lot more expectations of how the system is going to work. With LLMs, it's a lot more surface area. It's very stochastic, so you kind of have a different flavor here.

**Hamel Husain:** And so the example I'm going to show you today, it's actually a real estate example. It's a different kind of real estate example. It's from a company called Nurture Boss. I can share my screen to show you their website just to help you understand this use case a little bit, so let me share my screen. So this is a company that I worked with. It's called Nurture Boss, and it is a AI assistant for property managers who are managing apartments, and it helps with various tasks such as inbound leads, customer service, booking appointments, so on and so forth. It's like all the different sort of operations you might be doing as a property manager, it helps you with that. And so you can see kind of what they do. It's a very good example because it has a lot of the complexities of a modern AI application.

**Hamel Husain:** So there's lots of different channels that you can interact through the AI with like chat, text, voice, but also, there's tool calls, lots of tool calls for booking appointments, getting information about availability, so on and so forth. There's also RAG retrieval, getting information about customers and properties and things like that. So it's pretty fully fleshed in terms of an AI application. And so they have been really generous with me in allowing me to use their data as a teaching example. And so we have anonymized it, but what I'm going to walk through today is, okay, let's do the first part of how we would start to build evals for Nurture Boss. Why would we even want to do that?

