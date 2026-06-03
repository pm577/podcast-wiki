---
episode_date: '2026-01-18'
guest: zevi-arnovitz
id: lenny-2026-01-18-zevi-arnovitz
key_insights:
- 'Zevi Arnovitz: I have zero technical background, did music in high school ... when
  Sonnet 3.5 came out. I remember watching a YouTube video building apps using Bolt
  or Lovable. It basically felt like someone came up...'
podcast: lenny
tags:
- pricing
- saas
- startups
- ai-ml
- marketplace
- hiring
title: The non-technical PM’s guide to building with Cursor | Zevi Arnovitz (Meta)
type: Episode
word_count: 15000
---

# The non-technical PM’s guide to building with Cursor | Zevi Arnovitz (Meta)

The complete AI workflow that lets non-technical people build real products in Cursor.

**Guest:** Zevi Arnovitz
**Date:** 2026-01-18
**YouTube:** https://www.youtube.com/watch?v=1em64iUFt3U
**Topics:** pricing, saas, startups, ai-ml, marketplace, hiring

## Key Topics Discussed

- [[pricing]]
- [[saas]]
- [[startups]]
- [[ai-ml]]
- [[marketplace]]
- [[hiring]]

## Transcript Highlights

**Lenny Rachitsky:** You are a product manager shipping product without knowing how to write code, barely knowing how to review code.

**Zevi Arnovitz:** I have zero technical background, did music in high school ... when Sonnet 3.5 came out. I remember watching a YouTube video building apps using Bolt or Lovable. It basically felt like someone came up to me and said, "You have superpowers now."

**Lenny Rachitsky:** These days, you're using Cursor with Claude Code.

**Zevi Arnovitz:** If you're non-technical like me, code is terrifying, but AI just makes it so much possible. In the next coming years, I think everyone's going to become a builder. Titles are going to collapse and responsibilities are going to collapse.

**Lenny Rachitsky:** The main challenge people have is reviewing the code that AI has written.

**Zevi Arnovitz:** It's very difficult for me to catch mistakes. What I'll do is basically /review. This tells Claude to start reviewing its own code, but what's even cooler is I have Codex as well as Cursor open. I will have each of them review the code.

**Lenny Rachitsky:** This comes back to this quote. I think everyone's always hearing. It's not that you will be replaced by AI. You'll be replaced by someone who's better at using AI than you.

**Zevi Arnovitz:** It's the best time to be a junior, contrary to what a lot of people are saying, how there's no more junior roles out there. Yeah, that's true, but also when else in history could you get out of school and just build a startup on your own?

**Lenny Rachitsky:** Today, my guest is Zevi Arnovitz. Zevi is a PM at Meta. Prior to that, he was a PM at Wix, and this is a truly remarkable conversation that every non-technical product person needs to hear. Zevi is super young and has no technical background, but as a smart, young, ambitious person, has learned how to use Cursor and Claude Code to build significant and real products completely on his own, and he's created his own very clever and effective workflow that everyone listening can copy.

**Lenny Rachitsky:** To make that copying even easier, at the top of the show notes of this episode, you can download all of the prompts and /commands and start doing all of this yourself. Zevi shows you how to work with cursor to quickly add your ideas to Linear to explore your idea with AI, how to develop your plan, how to then build the thing, and then have different LLMs review your code and update your documentation, and then use all of this as a learning opportunity to develop your own sense of how things work.

**Lenny Rachitsky:** I haven't stopped thinking about this conversation since we had it, and everyone needs to pay attention to what AI is unlocking for non-technical people. A huge thank you to Tal Raviv for encouraging me to meet Zevi. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube.

**Zevi Arnovitz:** Thanks for having me, Lenny. I'm a huge fan of the show and tons of people that I've admired most and learned the most from. I've been on here, so it's a crazy moment for me. I'm really excited for this.

**Lenny Rachitsky:** I really appreciate that. I want to start by reading actually a note I got about you from Tal Raviv, who is a previous podcast guest, many times newsletter collaborator. One of the most AI forward product managers that I know I've learned a ton from him. So here's what he said about you when he introduced us.

**Lenny Rachitsky:** Zevi is the most hands-on vibe coding PM I know, and I've personally learned so much from him. His engineers at Meta ask him to teach them how to do what he does. Every time we get coffee, I repeatedly get this feeling of everyone needs to be hearing this.

**Zevi Arnovitz:** That's so nice.

**Lenny Rachitsky:** And so that's the goal. That's the goal of this conversation is to help more people hear what you figured out. We're going to get very hands-on. We're going to do a lot of show versus tell, showing people what you've figured out about how to be a PM, a non-technical PM building stuff. I want to give people a little bit of background on you because I think this is going to inspire a lot of listeners to feel like they can also do what we're about to show you. This is going to look very advanced, but just give people a little bit of sense of just your background.

**Zevi Arnovitz:** I'm very non-technical. I have zero technical background. Did music in high school. A lot of Israelis do technology units in the Army. I was not in a tech unit. And basically a year ago, I was traveling with my wife for three months in Asia and we were in Japan and that was around when Sonnet 3.5 came out. And I remember watching a YouTube video. I think it was either Greg Isenberg or Riley Brown and they were basically building apps using, it was either Bolt or Lovable, just using AI.

**Zevi Arnovitz:** And it was like a crazy moment for me because I was watching this and it basically felt like someone came up to me and said, "Hey Zevi, there's this cool new technology you should check out. You should really give it a try. Oh, and by the way, you have superpowers now." And the second I got home from Japan, I didn't even unpack my bags, ran to my computer, opened Bolt, opened an account, and for the past year I've been building.

**Zevi Arnovitz:** And the last thing I'll say on that is we talked about this a bit before we started recording, but I was prepping with Claude for the episode and I was trying to clarify what my goal is for this episode. And Claude said, "If people walk away thinking how amazing you are, you failed. And if people walk away and open their computer and start building, you've succeeded." So I really hope that we can inspire some people to do the same.

**Lenny Rachitsky:** I love that so much. I feel like that should be the goal for my podcast. If you're like, "I love that guest." It's less of a win. If it's just like, "Oh, I'm so inspired to do the thing that they figured out, that is the real win." I love, Claude is the best.

**Zevi Arnovitz:** I agree.

**Lenny Rachitsky:** Okay. So let's dive in and give people, let's start with kind of a high level overview of how you operate and you use AI in your job. What are the core tools and just what's kind of like the frame of reference for the workflow that you figured out and how you operate?

**Zevi Arnovitz:** This all started where I was a project's power user. I love projects, GPT projects.

**Lenny Rachitsky:** ChatGPT projects?

**Zevi Arnovitz:** Yeah, exactly. GPT projects and Claude projects, which are basically a shared folder of chats which share both custom instructions and shared knowledge base. And I think it was around when GPT started using memory where I thought it was interesting, but it really annoyed me because I do a bunch of different things. I'm a terrible runner, I'm a PM, I was a student, psychology student, so I had all these different facets of life. And what happened was the memory feature was mixing stuff up.

**Zevi Arnovitz:** So like I talked to GPT about running and it would say, "Oh yeah, after this 5K, you're going to crush all your next product reviews." And it's like, okay, I understand that you have that in your memory, but it's just not relevant. And projects basically allows you to compartmentalize and have things within the right context. So tracking back to the story I told when we came back from Japan, I started building this app.

**Zevi Arnovitz:** The first thing I noticed was that these products were built in a way where, and when I say these products, I mean Bolt and Lovable, were built in a way where they were super eager to write code. So their system prompt was you're a coding agent. So when you'd write something, they'd straight away start coding. So at the beginning of a project, this was super fun and exciting because they just go and start building your app.

**Zevi Arnovitz:** But later on when things got more complex, this created much more problems because planning is really important when you're implementing something technical and let's say you're implementing payments or something that's going to be a change to your database. If the coding agent is just like, "All right, I got it." And just starts writing code, this always results in terrible things, some really gnarly bugs that I had.

**Zevi Arnovitz:** And to mitigate this, what I did was I created sort of a CTO. So again, I'm not technical. I have been in product for a while, but I know zero stuff about code. So basically what I did was I created a CTO with the custom prompt of it being the complete technical owner of the project. So I told it, "I own the problem. I own how we want the users to feel. You're the complete owner of how this is going to be built. I want you to challenge me. I don't want you to be a people pleaser."

**Zevi Arnovitz:** All these things that kind of mitigate the regular ChatGPT-isms. I always think about this where for some reason, the easiest way for me to think about AI is to imagine it as people. And I think ChatGPT would probably be the worst CTO because it's such a people pleaser and it's so sycophantic where ... Just a short story I had a few weeks ago, I was trying to learn about Bun JavaScript, which was acquired by Anthropic and I was trying to understand what they do.

