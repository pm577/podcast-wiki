---
episode_date: '2026-04-23'
guest: cat-wu
id: lenny-2026-04-23-cat-wu
key_insights:
- 'Cat Wu: I think it is very hard to be the right amount of AGI-pilled. It''s very
  easy to build the product for the super AGI strong model. The hard thing is figuring
  out for the current model, how do you elici...'
podcast: lenny
tags:
- saas
- startups
- ai-ml
- marketplace
- leadership
- hiring
- retention
- product-strategy
title: How Anthropic’s product team moves faster than anyone else | Cat Wu (Head of
  Product, Claude Code)
type: Episode
word_count: 16271
---

# How Anthropic’s product team moves faster than anyone else | Cat Wu (Head of Product, Claude Code)

How Anthropic’s product team moves faster than anyone else, covering team leadership, AI product work, and product design.

**Guest:** Cat Wu
**Date:** 2026-04-23
**Topics:** saas, startups, ai-ml, marketplace, leadership, hiring, retention, product-strategy

## Key Topics Discussed

- [[saas]]
- [[startups]]
- [[ai-ml]]
- [[marketplace]]
- [[leadership]]
- [[hiring]]
- [[retention]]
- [[product-strategy]]

## Transcript Highlights

**Cat Wu:** I think it is very hard to be the right amount of AGI-pilled. It's very easy to build the product for the super AGI strong model. The hard thing is figuring out for the current model, how do you elicit the maximum capability?

**Lenny Rachitsky:** I've never seen anything like the pace folks at Anthropic are shipping at.

**Cat Wu:** We want to remove every single barrier to shipping things. The timelines for a lot of our product features have gone down from six month to one month and sometimes to even one day.

**Lenny Rachitsky:** You're interviewing hundreds of PMs and you just keep feeling like they're approaching it very incorrectly.

**Cat Wu:** The PM role is changing a lot. It's changing really quickly. The thing that is extremely important for building AI-native products is iterating so quickly, figuring out a way for you to actually launch features every single week.

**Lenny Rachitsky:** What do you think are the emerging skills PMs need to develop?

**Cat Wu:** It comes back to product taste. As code becomes much cheaper to write, the thing that becomes more valuable is deciding what to write.

**Cat Wu:** Thanks for having me.

**Lenny Rachitsky:** I have so many questions. I'm so excited to have you on this podcast. I want to start with giving people an understanding of your role alongside Boris. Everybody knows Boris. His episode is the number one most popular episode on this podcast, no pressure. He created Claude Code. He leads the eng team, ships a bazillion PRs a day from his phone, just like... I don't even know what the number is anymore. I think people don't give you enough credit for the success that Claude Code has had and Cowork and all the things you all are building. Help us understand your role on the team, how you work with Boris, how you split responsibilities. Just like what does the PMO look like on the Claude Code team?

**Cat Wu:** I feel very lucky to work with Boris. He's been an amazing thought partner. He's our tech lead. He's very much the product visionary, and he is great at setting, "This is what the product needs to be in three months, six months from now. This is what the AGI-pilled version of the product is," and a lot of my role is figuring out, okay, what is the path from where we are today to that vision three to six months from now? And I spend more of my time on the cross-functional, so making sure that our marketing team, sales team, finance, capacity, et cetera, are bought in on the plan and that we're all rowing the same direction and that once the feature is ready, that there aren't any blockers to shipping it.

**Cat Wu:** I think in many ways it works well because we kind of mind meld, but it is actually remarkably blurry of a line. I think we're 80% mind meld, and then there's this 20% of things that maybe I care a lot more about than Boris, so I'll drive those and 20% work he cares a lot more than me and he just drives those.

**Cat Wu:** I think before AI, technology shifts were a lot slower, so you could plan on these six to 12 month time horizons, and because you were shipping features at a bit of a slower rate, there was a lot more emphasis on coordinating with all the other partner teams to make sure that their shipping features that unblock your features because code at that time was very expensive to make. I think now with AI and with how much that has accelerated engineering and with how quickly the model capabilities are improving, the timelines for a lot of our product features have gone down from six month to one month and sometimes to one week or even one day. And with that, we actually need to make sure that products ship quite quickly.

**Cat Wu:** And what that means is as a PM, there should be less emphasis on making sure that you're aligning your multi-quarter roadmaps with your partner teams and more emphasis on, okay, how can we figure out the fastest way to get something out the door? How can we figure out how to make a concept corner of our product suite where we can just... An engineer has an idea or a PM has an idea, and by the end of the week, we are able to get into our user's hands. I think the PMs who do the best on AI-native products are the ones who can figure out, how can I shorten the time from having this idea to actually getting the product in the hands of users and help define what are the most important tasks that need to work out of the box for my product?

**Lenny Rachitsky:** So what I love about this is what you're saying is just like people haven't grasped how fast they need to move and how much of the job now is helping the team move fast. What helps do that? What do you do, what does your PM team do to help them move this fast other than have access to the most advanced models?

**Cat Wu:** I think the first thing is to set clear goals. Because LLMs are so general, that actually creates a lot of ambiguity in who we're building for, what problems we're trying to solve, what the top use cases are. And so I think a great PM is able to say, "Okay, our key user is professional developers. The main problem that we want to solve for this feature is maybe there's too many permission prompts and people are feeling fatigue, and the use case is we want professional developers at enterprises to safely get to zero permission prompts." And that actually sets a pretty clear goal because it rules out a lot of potential approaches for reducing permission prompts so that people can get a lot more done with one prompt.

**Cat Wu:** And then I think the second thing that's very important is figuring out some repeatable process for getting these features shipped. So for Claude Code, what we do is we actually ship almost all of our features in research preview. We clearly brand this when we ship something so that users know that this is an early product, this is just an idea, this is just something that we're trying to get feedback on and iterating on, and that this might not be supported forever. And what this does is it reduces our commitment for shipping something. We can just get something out in a week or two.

**Cat Wu:** And then the third thing that a PM should do is help create the framework for the team so that they know when to pull in cross-functional partners and what those cross-functional partners' expectations are. So for example, we have a really tight process between engineering, marketing, and docs. So when engineers have a feature that they feel is ready and that we've dogfooded internally, they post it in our evergreen launch room, and then Sarah, who leads our docs, and Alex who leads PMM, Antaric and Lydia on DevRel just jump in and can turn around the marketing announcement for it the very next day. And because we have this really tight process, it lowers the friction for any engineer to ship something, and PM is the role that should be setting this up.

**Lenny Rachitsky:** How do PRDs fit into this and the fact that you said that goals are a really important part, just like being aligned on what does success look like? Who is this for? Who's this now for? Are you writing PRDs, is it just a couple bullet points? How's that evolved in the world of a PM?

**Cat Wu:** So there's two things that we do. One is we have very rigorous metrics and we do metrics readouts with the entire team every week. The goal of this is to make sure that everyone deeply understands all the facets of our business, what our key goals are, how they're trending, and what drives them. The second thing that we do is we have this list of team principles, and this includes who our key users are, why those are our key users, and the reason that we articulate all of this is so that everybody on the team feels like they understand how our business works, they understand what's important to us and what we're willing to trade off, and it lets people make decisions by themselves without feeling like they're blocked on PM or any other stakeholder.

**Lenny Rachitsky:** I love how so much of this is like, okay, we still need PMs in the future, and there's so much talk of why do we need PMs? We're just going to ship and build. We need engineers.

**Cat Wu:** Oh, we actually do PRDs sometimes. So I think for features that are particularly ambiguous, it does help to write out just a one-pager on what the goals are, what the delightful use cases are, what the failure modes currently are that we need to fix. And there are occasionally some projects, especially things that require heavy infrastructure that do take many months, and for those situations, we do write PRDs still.

**Lenny Rachitsky:** I want to drill a little bit further into just how you're able to move so fast. I've never seen anything like the pace folks at Anthropic are shipping at. Someone made this calendar of launches across Anthropic, and it was literally every day there was a major feature or product. So one question people had online is you guys just launched this, not launched, but built this incredible model Mythos that is still in preview because it's so powerful, people are a little afraid of what it can do. Have you guys been using this? Is this part of the reason you've been able to move so fast?

**Cat Wu:** We've been moving pretty fast for several quarters now, so I think it's not fully Mythos. Mythos is an incredibly powerful model. We do use the models internally, and I think this has increased our rate of shipping a little bit, but I don't think it explains the bulk of the increase. I think a lot of it is the process and the expectation on the team. So we're very low on process. We want to remove every single barrier to shipping things. We want to make sure every single person on the team feels empowered to take their idea from just an idea to out in the world in less than a week, sometimes even in a day.

**Lenny Rachitsky:** Cool. Oh, man. What an advantage to have the best model and also be building product. That's so cool.

**Cat Wu:** We are very lucky to be able to work with the frontier models.

**Lenny Rachitsky:** Oh my God, what an awesome advantage, just build a thing and then use it and then accelerate faster. It's so interesting. There's a couple of these other side things, I want to just go on these sidequest on this conversation. There's so much happening with Anthropic, and I just am so curious to get your insight. One is a week ago or so, the whole source code of Claude Code leaked. Somebody got it out there. I think it was a mistake someone made. Is there anything you comment there, just like what happened? What went wrong? What should people know?

**Cat Wu:** So we immediately looked into this when we saw it. We realized that this was the result of human error. There was a human working with Claude to write PR. This was just an update to how we release our packages and it actually went through two layers of human review, and so this was a result of human error and we've hardened our processes to make sure that it doesn't happen in the future.

**Lenny Rachitsky:** Is this person still at Anthropic? Are they doing all right?

**Cat Wu:** Yes, yes. It's a process failure, and the most important thing is to just learn from it and to add more safeguards so that doesn't happen again, and so that's what we've been focused on and most of those have shifted.

**Lenny Rachitsky:** Okay. Another question I had is OpenClaw. So recently there's been this move to keep people from using Claude's subscription with their OpenClaws. People got really upset. They're confused why this is happening. It feels like there's harm caused to the open source community. What do people need to understand about what went into this decision?

