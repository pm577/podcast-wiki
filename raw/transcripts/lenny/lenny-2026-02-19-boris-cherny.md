---
episode_date: '2026-02-19'
guest: boris-cherny
id: lenny-2026-02-19-boris-cherny
key_insights:
- 'Boris Cherny: 100% of my code is written by Claude Code. I have not edited a single
  line by hand since November. Every day, I ship 10, 20, 30 pull requests. So, at
  the moment I have, like, five agents running....'
podcast: lenny
tags:
- leadership
- saas
- startups
- pricing
- hiring
- marketplace
- retention
- ai-ml
title: Boris Cherny
type: Episode
word_count: 19629
---

# Boris Cherny

This is the world now." What's the next big shift to how software is written that either your team is already operating in or you think will head towards, covering engineering tradeoffs, product design, and AI product work.

**Guest:** Boris Cherny
**Date:** 2026-02-19
**Topics:** leadership, saas, startups, pricing, hiring, marketplace, retention, ai-ml

## Key Topics Discussed

- [[leadership]]
- [[saas]]
- [[startups]]
- [[pricing]]
- [[hiring]]
- [[marketplace]]
- [[retention]]
- [[ai-ml]]

## Transcript Highlights

**Boris Cherny:** 100% of my code is written by Claude Code. I have not edited a single line by hand since November. Every day, I ship 10, 20, 30 pull requests. So, at the moment I have, like, five agents running.

**Lenny Rachitsky:** While we're recording this?

**Boris Cherny:** Yeah. Yeah. Yeah.

**Lenny Rachitsky:** Do you miss writing code?

**Boris Cherny:** I have never enjoyed coding as much as I do today, because I don't have to deal with all the minutia. Productivity per engineer has increased 200%.

**Lenny Rachitsky:** There's always this question, "Should I learn to code?"

**Boris Cherny:** In a year or two, it's not going to matter. Coding is virtually solved. I imagine a world where everyone is able to program, anyone can just build software any time.

**Lenny Rachitsky:** What's a next big shift to how software is written?

**Boris Cherny:** Claude is starting to come up with ideas. It's looking for feedback, it's looking at bug reports, it's looking at telemetry for bug fixes, and things to ship. A little more like a coworker or something like that.

**Lenny Rachitsky:** A lot of people listening to this are product managers and they're probably sweating.

**Boris Cherny:** I think by the end of the year everyone is going to be a product manager, and everyone codes. The title software engineer is going to start to go away. It's just going to be replaced by builder, and it's going to be painful for a lot of people.

**Lenny Rachitsky:** Today my guest is Boris Cherny, head of Claude Code at Anthropic. It is hard to describe the impact that Claude Code has had on the world. Around the time this episode comes out will be the one year anniversary of Claude Code. And in that short time it has completely transformed the job of a software engineer, and it is now starting to transform the jobs of many other functions in tech, which we talk about.

**Lenny Rachitsky:** Claude Code itself is also a massive driver of Anthropic's overall growth over the past year. They just raised a round at over $350 billion. And as Boris mentions, the growth of Claude Code itself is still accelerating. Just in the past month, their daily active users has doubled. Boris is also just a really interesting, thoughtful, deep-thinking human, and during this conversation we discover we were born in the same city in Ukraine. That is so funny. I had no idea.

**Lenny Rachitsky:** A huge thank you to Ben Mann, Jenny Wen, and Mike Krieger for suggesting topics for this conversation. Don't forget to check out LennysProductPass.com for an incredible set of deals available exclusively to Lenny's newsletter subscribers. Let's get into it after a short word from our wonderful sponsors.

**Boris Cherny:** Yeah. Thanks for having me on.

**Lenny Rachitsky:** I want to start with a spicy question. About six months ago, I don't know if people even remember this, you actually left Anthropic. You joined Cursor. And then two weeks later you went back to Anthropic. What happened there? I don't think I've ever heard the actual story.

**Boris Cherny:** It was the fastest job change that I've ever had. I joined Cursor, because I'm a big fan of the product. And, honestly, I met the team and I was just really impressed. They're an awesome team. I still think they're awesome, and they're just building really cool stuff. And they saw where AI coding was going I think before a lot of people did.

**Boris Cherny:** So, the idea of building good product was just very exciting for me. I think as soon as I got there what I started to realize is what I really missed about Ant was the mission. And that's actually what originally drove me to Ant also, because before I joined Anthropic I was working in Big Tech, and then, at some point, I wanted to work at a lab to just help shape the future of this crazy thing that we're building in some way.

**Boris Cherny:** And the thing that drew me to Anthropic was the mission. And it's all about safety. And when you talk to people at Anthropic, just, like, find someone in the hallway, if you ask them why they're here, the answer is always going to be, "Safety." And so, this mission-driven [inaudible 00:05:14] just really, really resonated with me. And I just know, personally, it's something I need in order to be happy. And that's just a thing that I really missed, and I found that whatever the work might be, no matter how exciting, even if it's building a really cool product, it's just not really a substitute for that. So, for me, it was pretty obvious that I was missing that pretty quick.

**Lenny Rachitsky:** Okay. So, let me follow the thread of just coming back to Anthropic and the work you've done there. This podcast is going to come out around the year anniversary of launching Claude Code. So, I want to spend a little time just reflecting on the impact that you've had. There's this report that recently came out that I'm sure you saw by Semi-Analysis that showed that 4% of all GitHub commits are authored by Claude Code now. And they predicted it'll be a fifth of all code commits on GitHub by the end of the year.

**Lenny Rachitsky:** The way they put it is, "While we blinked, AI consumed all software development." The day that we're recording this Spotify just put out this headline that their best developers haven't written a line of code since December thanks to AI. More and more of the most advanced senior engineers, including you, are sharing the fact that you don't write code anymore, that it's all AI-generated, and many aren't even looking at code anymore is how far we've gotten.

**Lenny Rachitsky:** In large part, thanks to this little project that you started, and that your team has scaled over the past year. I'm curious just to hear your reflections on this past year, and the impact that your work has had.

**Boris Cherny:** These numbers are just totally crazy. Right? Like, 4% of all commits in the world is just way more than I imagined. And, like you said, it still feels like the starting point. These are also just public commits. So, we actually think if you look at private repositories it's quite a bit higher than that.

**Boris Cherny:** And I think the crazy thing for me isn't even the number that we're at right now, but the pace at which we're growing, because if you look at Claude Code's growth rate across any metric it's continuing to accelerate. So, it's not just going up, it's going up faster and faster.

**Boris Cherny:** When I first started Claude Code, it was just supposed to be a little hack. We broadly knew at Anthropic that we wanted to ship some kind of coding product. And for Anthropic for a long time, we were building the models in this way that fit our mental model of the way that we build safe AGI where the model starts by being really good at coding. Then it gets really good at tool use. Then it gets really good at computer use. Roughly, this is, like, the trajectory.

**Boris Cherny:** And we've been working on this for a long time. And when you look at the team that I started on, it was called Anthropic Labs team, and actually Mike Krieger and Ben Mann they just kicked this team off again for round two.

**Boris Cherny:** The team built some pretty cool stuff. So, we built Claude Code, we built MCP, we built the desktop app. So, you can see the seeds of this idea. It's coding, then it's tool use, then it's computer use.

**Boris Cherny:** And the reason this matters for Anthropic is because of safety. It's, again, just back to that AI is getting more and more powerful, it's getting more and more capable. The thing that's happened in the last year is that, at least, for engineers, the AI doesn't just write the code. It's not just a conversation partner, but it actually uses tools. It acts in the world.

**Boris Cherny:** And I think now with Cowork we're starting to see the transition for non-technical folks also. For a lot of people that use conversational AI, this might be the first time that they're using the thing that actually acts, it can actually use your Gmail, it can use your Slack. It can do all these things for you, and it's quite good at it. And it's only going to get better from here.

**Boris Cherny:** So, I think for Anthropic for a long time, there was this feeling that we wanted to build something, but it wasn't obvious what. And so, when I joined Ant, I spent one month hacking, and built a bunch of weird prototypes. Most of them didn't ship, and weren't even close to shipping. It was just understanding the boundaries of what the model can do.

