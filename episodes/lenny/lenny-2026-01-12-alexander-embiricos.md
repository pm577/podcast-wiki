---
episode_date: '2026-01-12'
guest: alexander-embiricos
id: lenny-2026-01-12-alexander-embiricos
key_insights:
- 'Alexander Embiricos: Codex is OpenAI''s coding agent. We think of Codex as just
  the beginning of a software engineering teammate. It''s a bit like this really smart
  intern that refuses to read Slack, doesn''t check Datadog u...'
podcast: lenny
tags:
- ai-ml
- saas
- leadership
- hiring
- marketplace
- startups
- retention
- product-strategy
title: 'The power user’s guide to Codex: parallelizing workflows, planning techniques,
  advanced context engineering tips, automating code reviews, and more | Alexander
  Embiricos'
type: Episode
word_count: 17504
---

# The power user’s guide to Codex: parallelizing workflows, planning techniques, advanced context engineering tips, automating code reviews, and more | Alexander Embiricos

How to set up and use Codex in VS Code and terminal environments for both simple and complex coding tasks.

**Guest:** Alexander Embiricos
**Date:** 2026-01-12
**YouTube:** https://www.youtube.com/watch?v=xeZDHGjG5zM
**Topics:** ai-ml, saas, leadership, hiring, marketplace, startups, retention, product-strategy

## Key Topics Discussed

- [[ai-ml]]
- [[saas]]
- [[leadership]]
- [[hiring]]
- [[marketplace]]
- [[startups]]
- [[retention]]
- [[product-strategy]]

## Transcript Highlights

**Lenny Rachitsky:** You lead work on Codex.

**Alexander Embiricos:** Codex is OpenAI's coding agent. We think of Codex as just the beginning of a software engineering teammate. It's a bit like this really smart intern that refuses to read Slack, doesn't check Datadog unless you ask it to.

**Lenny Rachitsky:** I remember Karpathy tweeted the gnarliest bugs that he runs into that he just spends hours trying to figure out nothing else has solved, he gives it to Codex, lets it run for an hour and it solves it.

**Alexander Embiricos:** Starting to see glimpses of the future where we're actually starting to have Codex be on call for its own training. Codex writes a lot of the code that helps manage its training run, the key infrastructure. So we have a Codex code review that's catching a lot of mistakes. It's actually caught some pretty interesting configuration mistakes. One of the most mind-blowing examples of acceleration, the Sora Android app, like a fully new app, we built it in 18 days and then 10 days later, so 28 days total, we went to the public.

**Lenny Rachitsky:** How do you think you win in this space?

**Alexander Embiricos:** One of our major goals with Codex is to get to proactivity. If we're going to build a super system, has to be able to do things. One of the learnings over the past year is that for models to do stuff, they're much more effective when they can use a computer. It turns out the best way for models to use computers is simply to write code. And so we're kind of getting to this idea where if you want to build any agent, maybe you should be building a coding agent.

**Lenny Rachitsky:** When you think about progress on Codex, I imagine you have a bunch of evals and there's all these public benchmarks.

**Alexander Embiricos:** A few of us are constantly on Reddit. There's praise up there and there's a lot of complaints. What we can do is as a product team just try to always think about how are we building a tool so that it feels like we're maximally accelerating people rather than building a tool that makes it more unclear what you should do as the human?

**Lenny Rachitsky:** Being at OpenAI, I can't not ask about how far you think we are from AGI.

**Alexander Embiricos:** The current underappreciated limiting factor is literally human typing speed or human multitasking speed.

**Lenny Rachitsky:** Today, my guest is Alexander Embiricos, product lead for Codex, OpenAI's incredibly popular and powerful coding agent. In the words of Nick Turley, head of ChatGPT and former podcast guest, "Alex is one of my all time favorite humans I've ever worked with, and bringing him and his company into OpenAI ended up being one of the best decisions we've ever made." Similarly, Kevin Weil, OpenAI's CPO, said, "Alex is simply the best."

**Lenny Rachitsky:** In our conversation, we chat about what it's truly like to build product at OpenAI, how Codex allowed the Sora team to ship the Sora app, which became the number one app in the app store in under one month. Also, the 20x growth Codex is seeing right now and what they did to make it so good at coding, why his team is now focused on making it easier to review code, not just write code, his AGI timelines, his thoughts on when AI agents will actually be really useful, and so much more. A huge thank you to Ed Bayes, Nick Turley, and Dennis Yang for suggesting topics for this conversation. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. And if you become an annual subscriber of my newsletter, you get a year free of 19 incredible products, including a year free of Devin, Lovable, Replit, Bolt, n8n, Linear, Superhuman, Descript, Wispr Flow, Gamma, Perplexity, Warp, Granola, Magic Patterns, Raycast, ChatPRD, Mobbin, PostHog, and Stripe Atlas. Head on over to lennysnewsletter.com and click Product Pass.

**Alexander Embiricos:** Thank you so much. I've been following for ages and I'm excited to be here.

**Lenny Rachitsky:** I'm even more excited. I really appreciate that. I want to start with your time at OpenAI. So you joined OpenAI about a year ago. Before that, you had your own startup for about five years. Before that, you were a product manager at Dropbox. I imagine OpenAI is very different from every other place you've worked. Let me just ask you this, what is most different about how OpenAI operates and what's something that you've learned there that you think you're going to take with you wherever you go, assuming you ever leave?

**Alexander Embiricos:** By far, I would say the speed and ambition of working at OpenAI are just dramatically more than what I can imagine. And I guess it's kind of an embarrassing thing to say because everyone who's a startup founder thinks like, "Oh yeah, my startup moves super fast and the talent bar is super high and we're super ambitious." But I have to say, working in OpenAI just made me reimagine what that even means.

**Lenny Rachitsky:** We hear this a lot about feels like every AI company is just like, "Oh my God, I can't believe how fast they're moving." Is there an example of just like, "Wow, that wouldn't have happened this quickly anywhere else"?

**Alexander Embiricos:** The most obvious thing that comes to mind is just the explosive growth of Codex itself. I think it's a while since we bumped our external number, but it's like the 10x-ing of Codex's scale was just super fast in a matter of months and it's well more since then. And once you've lived through that, or at least speaking for myself, having lived through that now, I feel like anytime I'm going to spend my time on building tech product, there's that speed and scale that I now need to meet.

**Alexander Embiricos:** If I think of what I was doing in my startup, it moved way slower and there's always this balance with startups of how much do you commit to an idea that you have versus find out that it's not working and then pivot. But I think one thing I've realized at OpenAI is the amount of impact that we can have and, in fact, need to have to do a good job is so high that I have to be way more ruthless with how I spend my time now.

**Lenny Rachitsky:** Before we get to Codex, is there a way that they've structured the org or, I don't know, the way that OpenAI operates that allows the team to move this quickly? Because everyone wants to move super fast. I imagine there's a structural approach to allowing this to happen.

**Alexander Embiricos:** I mean, so one thing is just the technology that we're building with has just transformed so many things from both how we build, but also what kinds of things we can enable for users. And we spend most of our time talking about the sort of improvements within the foundation models, but I believe that even if we had no more progress today with models, which is absolutely not the case, but even if we had no more progress, we are way behind on product. There's so much more product to build. So I think just the moment is ripe, if that makes sense.

**Alexander Embiricos:** But I think there's a lot of counterintuitive things that surprised me when I arrived as far as how things are structured. One example that comes to mind is when I was working on my startup and before that, when I was at Dropbox, it was very important, especially as a PM to always rally the ship and it was like make sure you're pointed in the right direction and then you can accelerate in that direction. But here, I think because we don't exactly know what capabilities will even come up soon and we don't know what's going to work technically, and then we also don't know what's going to land even if it works technically, it's much more important for us to be very humble and learn a lot more empirically and just try things quickly. And the org is set up in that way to be incredibly bottoms up.

**Alexander Embiricos:** This is, again, one of those things that, as you were saying, everyone wants to move fast. I think everyone likes to say that they're bottoms up, or at least a lot of people do, but OpenAI is truly, truly bottoms up. And that's been a learning experience for me that now it'll be interesting if I ever work at... I don't think it'll even make sense to work at a non-AI company in the future. I don't even know what that means. But if I were to imagine it or go back in time, I think I would run things totally new.

**Lenny Rachitsky:** What I'm hearing is this ready, fire, aim is the approach more than ready, aim, fire. And there's something, and as you process that, because that may not come across well, but I actually have heard this a lot at AI companies is because you don't know, and Nick Turley shared I think the same sentiment, because you don't know how people will use it it doesn't make sense to spend a lot of time making it perfect. It's better to just get it out there in a primordial way, see how people use it, and then go big on that use case.

**Alexander Embiricos:** Yeah. Okay, to use this analogy a little bit, I feel like there is an aim component, but the aim component is much fuzzier. It's kind of like, roughly what do we think can happen? Someone I've learned a ton from working here is a research lead, and he likes to say that at OpenAI, we can have really good conversations about something that's a year plus from now, and there's a lot of ambiguity in what will happen, but that's a right sort of timeline. And then we can have really good conversations about what's happening in low months or weeks. But there's this awkward middle ground, which was as you start approaching a year, but you're not at a year where it's very difficult to reason about, right?

**Alexander Embiricos:** And so as far as aiming, I think we want to know, "Okay, what are some of the futures that we're trying to build towards?" And a lot of the problems we're dealing with in AI, such as alignment are problems you need to be thinking out really far out into the future. So we're kind of aiming fuzzily there, but when it comes down to the more tactically like, "Oh yeah, what product will we build and therefore how will people use that product?" That's the place where we're much more like, "Let's find out empirically."

**Lenny Rachitsky:** That's a good way of putting it. Something else that when people hear this, people sometimes hear companies like yours saying, "Okay, we're going to be bottoms up. We're going to try a bunch of stuff. We're not going to have exactly a plan of where it's going in the next few months." The key is you all hire the best people in the world. And so that feels like a really key ingredient in order to be this successful at bottoms up work.

**Alexander Embiricos:** It just super resonates with me. I was just, again, surprised or even shocked when I arrived at the level of individual drive and autonomy that everyone here has. So I think the way that OpenAI runs, you can't read this or listen to a podcast and be like, "I'm just going to deploy this to my company." Maybe this is a harsh thing to say, but I think very few companies have the talent caliber to be able to do that. So it might need to be adjusted if you were going to implement this.

**Lenny Rachitsky:** Okay. So let's talk Codex. You lead work on Codex. How's Codex going? What numbers can you share? Is there anything you can share there? Also, just not everyone knows exactly what Codex is, explain what Codex is.

**Alexander Embiricos:** Totally, yeah. So I had the very lucky job of living in the future and leading products on Codex. And Codex is OpenAI's coding agent. So super concretely, that means it's an IDE extension, a VS code extension that you can install or a terminal tool that you can install. And when you do so, you can then basically pair with Codex to answer questions about code, write code, run tests, execute code, and do a bunch of the work in that thick middle section of the software development lifecycle, which is all about writing code that you're going to get into production.

**Alexander Embiricos:** More broadly, we think of Codex as what it currently is just the beginning of a software engineering teammate. So when we use a big word like teammate, some of the things we're imagining are that it's not only able to write code, but actually it participates early on in the ideation and planning phases of writing software and then further downstream in terms of validation, deploying and maintaining code.

