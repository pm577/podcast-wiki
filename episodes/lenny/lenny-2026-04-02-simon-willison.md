---
episode_date: '2026-04-02'
guest: simon-willison
id: lenny-2026-04-02-simon-willison
key_insights:
- 'Simon Willison: A lot of people woke up in January and February and started realizing,
  "Oh wow, I can churn out 10,000 lines of code in a day." It used to be you''d ask
  ChatGPT for some code and it would spit out some...'
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
title: 'An AI state of the union: We’ve passed the inflection point, dark factories
  are coming, and automation timelines | Simon Willison'
type: Episode
word_count: 21276
---

# An AI state of the union: We’ve passed the inflection point, dark factories are coming, and automation timelines | Simon Willison

We’ve passed the inflection point, dark factories are coming, and automation timelines, covering engineering tradeoffs, AI product work, and product design.

**Guest:** Simon Willison
**Date:** 2026-04-02
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

**Simon Willison:** A lot of people woke up in January and February and started realizing, "Oh wow, I can churn out 10,000 lines of code in a day." It used to be you'd ask ChatGPT for some code and it would spit out some code, and you have to run it and test it. The coding agents, they take that step for you, and an open question for me is how many other knowledge work fields are actually prone to these agent loops?

**Lenny Rachitsky:** Now that we have this power, people almost underestimate what they do with it.

**Simon Willison:** Today probably 95% of the code that I produce I didn't type it myself. I write so much of my code on my phone, it's wild. I can get good work done walking the dog along the beach. My New Year's resolution. Every previous year, I've always told myself this year I'm going to focus more, I'm going to take on less things. This year my ambition was take on more stuff and be more ambitious.

**Lenny Rachitsky:** Such an interesting contradiction. AI's supposed to make us more productive. It feels like the people that are most AI-pilled are working harder than they've ever worked.

**Simon Willison:** Using coding agents well is taking every inch of my 25 years of experience as a software engineer. I can fire up four agents in parallel and have them work on four different problems. By 11: 00 AM, I am wiped out.

**Lenny Rachitsky:** You have this prediction that we're going to have a massive disaster. At some point, you call it the challenger disaster of AI.

**Simon Willison:** Lots of people knew that those little O-rings were unreliable, but every single time you get away with launching a space shuttle without the O-rings failing, you institutionally feel more confident in what you're doing. We've been using these systems in increasingly unsafe ways, this is going to catch up with us. My prediction is that we're going to see a challenger disaster.

**Lenny Rachitsky:** Today, my guest is Simon Willison. Simon, in my opinion, is one of the most important and useful voices right now on how AI is changing the way that we build software and how professional work is changing broadly. What I love about Simon is that he doesn't just pontificate in the clouds, he's been what you'd call a 10X engineer for over 20 years. He co-created Django, the web framework that powers Instagram, Pinterest, Spotify, and thousands of other platforms, he coined the term prompt injection, popularized the ideas of AI slop and agentic engineering, and amongst his 100+ open source projects he created Datasette, a data analysis tool that has become a staple of investigative journalism.

**Lenny Rachitsky:** What makes Simon rare is that very few engineers have made the leap from the old way of building to the new way as fully and visibly as he has. As he's leaned into this new way of building, he's been sharing everything he's learning in real-time through his incredible blog, simonwillison.net. Simon does not do a lot of podcasts, and this conversation opened my mind up in a bunch of new ways. I am so excited for you to get to learn from Simon.

**Simon Willison:** Hey, Lenny, it's really great to be here.

**Lenny Rachitsky:** I'm so excited to have you here. I've been such a fan of yours from afar for so long, I've learned so much from your blog. Even though every guest I have in this podcast is my favorite guest, you're my favorite kind of guest, because you're on the ground building with the latest tools, using it for real, you're very good at articulating what you experience, so we're going to get a lot of ROI out of your brain from this time that we have together.

**Simon Willison:** Absolutely.

**Lenny Rachitsky:** What I want to start with is essentially an AI State of the Union. You've written about this November inflection.

**Simon Willison:** Yes.

**Lenny Rachitsky:** So what I'm thinking as we start, just give us a brief history lesson of just what happened in November and where are we today? What's possible now?

**Simon Willison:** Well, let's talk about all of 2025 very briefly. 2025 was the year that especially Anthropic and OpenAI realized that code is the application, like having these things generate code. I think partly because Anthropic came up with Claude Code back in February of 2025, and it took off like crazy, and a bunch of people started signing up for $200 a month accounts. So, suddenly, wow, it turns out people are willing to pay a lot of money for this stuff for that specific field. Both Anthropic and OpenAI spent the whole of 2025 focusing all of their training efforts on coding. If you look at what they were doing, it was all the reinforcement learning stuff. The reasoning trick, the thing where the models say they're thinking, that was new in late 2024. OpenAI's o1 was the first model to exhibit that, and now all of the models do it. So, that was the other big trend of last year was these reasoning models.

**Simon Willison:** Turns out reasoning is great for code. It can reason through code and figure out the root of bugs and all of that. So the end result of this, the end result of these two labs throwing everything they had at making their models better at code is in November we had what I call the inflection point where GPT 5.1 and Claude Opus 4.5 came along. They were incrementally better than the previous models, but in a way that crossed a threshold, where previously if you had these coding agents you could get them to write you some code and most of the time it would mostly work, but you had to pay very close attention to it. Suddenly we went from that to almost all of the time it does what you told it to do, which makes all of the difference in the world.

**Simon Willison:** Now, you can spin up a coding agent and say, "Hey, build me a Mac application that does this thing." You'll get something back, which still leads some back and forth, but it won't just be a buggy pile of rubbish that doesn't do anything. That was fascinating, because all of the software engineers who took time off over the holidays and started tinkering with this stuff got this moment of realization where it's like, "Oh, wow, this stuff actually works now. I could tell it to build code, and if I describe that code well enough, it'll follow the instructions and it'll build the thing that I asked it to build."

**Simon Willison:** I think the reverberations of that are still shaking us. To software engineering, a lot of people woke up in January and February and started realizing, "Oh wow, this technology, which I'd been kind of paying attention to, suddenly it's got really, really good." And what does that mean? I can churn out 10,000 lines of code in a day and most of it works. Is that good? How do we get from most of it works to all of it works? There are so many new questions that we're facing, which I think makes us a bellwether for other information workers.

**Simon Willison:** Code is easier than almost every other problem that you pose these agents, because code is obviously right or wrong. It produces code, you run the code, either it works or it doesn't work. There might be a few subtle hidden bugs, but generally you can tell if the thing actually works. If it writes you an essay or if it prepares a lawsuit for you, it's so much harder to derive if it's actually done a good job to figure out if it got things right or wrong, but it's kind of happening to us.

**Simon Willison:** So software engineers, it came for us first and we're figuring out, okay, what do our careers look like? How do we work as teams when part of what we did that used to take look most of the time doesn't take most of the time anymore, what's that look like? It's going to be very interesting seeing how this rolls out to other information work in the future.

**Simon Willison:** I write so much of my code on my phone, it's wild. I can get good work done walking the dog along the beach, which is delightful.

**Lenny Rachitsky:** Yeah, I had Boris Cherny on the podcast and he's doing the same thing, and I was just like, "Is that even coding anymore?" He's like, "Yeah, it's just another level of abstraction, just like engineering has always gone." Talk about maybe just what else is there around just what is possible now with AI in terms of building that people may not fully recognize? And what's the next leap? Is there anything beyond this?

**Simon Willison:** Let's talk about the two, there's the vibe coding side of things and then there's the ... and I like Andrej Karpathy's original definition of vibe coding, which is when you don't even look at code and you basically just go on the vibes. You say, build me something that does X, and it builds it and you play with it. If it looks good, then great, and if it doesn't quite do it, you keep on going back and forth with it. But it's very hands-off, you're not looking at code, it's ... so he originally said, "This is great for having fun and prototyping," and it then exploded way out of that.

**Simon Willison:** I think today vibe coding is effectively it's ... the definition I use is it's when you're not looking at the code, you don't care about code and maybe you don't understand the code. Non-programmers can now tell Claude what to build and it can build them a little app, and I love that. I absolutely love that we're democratizing the art of getting a computer to do stuff for you, of automating tedious things in your life by knocking out these little tools. Of course, the problem is that there is a limit on how much you can do with that responsibly. I like to tell people, if you're vibe coding something for yourself where the only person who gets hurt if it has bugs is you, go wild. That's completely fine. The moment you're vibe coding code for other people to use where your bugs might actually harm somebody else, that's when you need to take a step back and say, hang on a second, this is not a responsible way of using these tools.

**Simon Willison:** The challenge is that understanding what's responsible and what isn't is in itself a expert level skill, so knowing that once you start dealing with scraping other people's websites, maybe you'll damage their websites by hitting them too hard. There are so many ways that you can cause damage if you don't know what you're doing. But I love that liberation and I love that people can come to meetings with a prototype that they knocked up of that idea that illustrates the idea. I think those things are wonderful.

**Simon Willison:** The ongoing debate has been what do we call it when a professional software engineer uses these tools to write real code that's production-ready that they've reviewed and they've checked all of the details of? A lot of people call that vibe coding as well. I think that devalues vibe coding as a term, 'cause it's useful to say, "I vibe coded this," as in I haven't even looked at how it works, it's not production-ready, but it's kind of a cool prototype. The moment vibe coding mean everything that touches AI, it effectively ends up needing programming, because we're all moving in a direction where our code is mediated through AI at some point.

**Simon Willison:** So, what do we call it for professionals? I've gone with agentic engineering, because I think the thing to emphasize is these coding agents, right? If you're asking ChatGPT to knock out some code, that's a different thing from if you're running Codex and having it write the code, debug the code, test the code, all of that. I think that agentic engineering is such a deep and fascinating discipline, because the art of getting really good results out of this, the art of having them help you build software you could deploy to a million people, that's never going to be easy, that's never going to be trivial. That's always going to require a great deal of depth of experience in how software works and how these agents work, and I love that.

**Simon Willison:** I'm kind of writing a book about it now that I'm publishing a chapter at a time on my blog. The best form of writing, because I don't have an editor or any pressure from a publisher, is just when I feel like writing another chapter I can do that, but there's so much to discuss. But yeah, so I think right now the frontier is how do we build professional software using coding agents? How do we build software that is ... I don't just want to build software that's good, I want us to build software that is better than we were building before. If the agents let us move a bit faster, but we're still churning out the same quality of software, that's less interesting to me than if the software we're producing has less bugs, more features, it's higher quality, it's better software, because we're harnessing these tools.

**Simon Willison:** The really interesting future is something which some people have been calling the dark factory pattern or software factories. This is the idea where right now if you're a professional using these tools, the way you do it is you tell them what to build and then you look at the code and you review that code really carefully and make sure it's doing the right thing. What does it look like if you're not reviewing the code, if you're not looking at that code, but you're also not vibe coding, you're not throwing everything to the wind and seeing what happened? You're applying professional practices and quality expectations to code that you're not directly reviewing.

