---
episode_date: '2025-10-26'
guest: dhanji-r-prasanna
id: lenny-2025-10-26-dhanji-r-prasanna
key_insights:
- 'Dhanji R. Prasanna: We see a significant amount of games. We find engineering teams
  that are very, very AI forward are reporting about eight to 10 hours save per week.
  Whenever I hear a stat like this, I think an importa...'
podcast: lenny
tags:
- ai-ml
- saas
- leadership
- hiring
- marketplace
- startups
- pricing
- product-strategy
title: How Block is becoming the most AI-native enterprise in the world | Dhanji R.
  Prasanna
type: Episode
word_count: 15018
---

# How Block is becoming the most AI-native enterprise in the world | Dhanji R. Prasanna

Dhanji R. Prasanna is the chief technology officer at Block (formerly Square), where he’s managed more than 4,000 engineers over the past two years. Under his leadership, Block has become one of the most AI-native large companies in the world.

**Guest:** Dhanji R. Prasanna
**Date:** 2025-10-26
**YouTube:** https://www.youtube.com/watch?v=JMeXWVw0r3E
**Topics:** ai-ml, saas, leadership, hiring, marketplace, startups, pricing, product-strategy

## Key Topics Discussed

- [[ai-ml]]
- [[saas]]
- [[leadership]]
- [[hiring]]
- [[marketplace]]
- [[startups]]
- [[pricing]]
- [[product-strategy]]

## Transcript Highlights

**Lenny Rachitsky:** There's a lot of talk about productivity gains through AI. There's this camp of people that are so overhyped, nothing's working, nobody's actually adopting this at scale.

**Dhanji R. Prasanna:** We see a significant amount of games. We find engineering teams that are very, very AI forward are reporting about eight to 10 hours save per week. Whenever I hear a stat like this, I think an important element is this is the worst it will ever be. This is now the baseline. The truth is the value is changing every day, so you need to ride that wave along with it.

**Lenny Rachitsky:** There's a story I heard you share on a different podcast where there's an engineer who has Goose watching.

**Dhanji R. Prasanna:** You'll be talking to a colleague on Slack or an email, and they'll be discussing some feature that they think is useful to implement. Now a few hours later, he'll find that Goose has already tried to build that feature and opened a PR for it on Git.

**Lenny Rachitsky:** What level of engineer is most benefiting from these tools?

**Dhanji R. Prasanna:** What's been surprising and really amazing, the non-technical people using AI agents and programming tools to build things, the people that are able to embrace it to optimize for their particular workday and their particular set of tasks are really showing the most impact from these tools.

**Lenny Rachitsky:** How do you think things will look in a couple of years in terms of how engineers work that's different from today?

**Dhanji R. Prasanna:** All these LLMs are sitting idle overnight and on weekends, while humans aren't there. There's no need for that. They should be working all the time. They should be trying to build in anticipation of what we want.

**Lenny Rachitsky:** What's maybe the most counterintuitive lesson you've learned about building products or building teams?

**Dhanji R. Prasanna:** A lot of engineers think that code quality is important to building a successful product. The two have nothing to do with each other.

**Lenny Rachitsky:** Today my guest is Dhanji Prasanna. Dhanji is Chief Technology Officer at Block, where he oversees a team of over 3,500 people. With Dhanji's leadership, Block has become one of the most AI-native large companies in the world and has basically achieved what many eng and product leaders are trying to achieve within their companies.

**Lenny Rachitsky:** In our conversation, we chat about their internal open source agent called Goose, that by their measure is saving employees on average eight to 10 hours a week of work time, and that number is going up, how AI specifically making their teams more productive and the teams that are benefiting most. Interestingly, it's not the engineering team, what it took to shift the culture to be very AI-oriented, the very boring change they made internally that boosted productivity even more than any AI tool.

**Lenny Rachitsky:** Also, lessons from building Google Wave and Google Plus and Cash app and so much more. This episode is for anyone curious to see what a highly AI-forward technology-driven large company looks like and can act like. If you enjoy this podcast, don't forget to subscribe and follow it in your favorite podcasting app or YouTube. It helps tremendously.

**Dhanji R. Prasanna:** Thank you Lenny. It's a great pleasure to be here.

**Lenny Rachitsky:** I want to start with a letter that I hear you wrote to Jack Dorsey to convince him that he and that Block needed to take AI a lot more seriously. I think you called it your AI manifesto and it seems like it really worked. We're going to talk a lot about the changes that came as a result of that. So let me just ask, what did you say in this letter and what happened right after you sent that letter to him?

**Dhanji R. Prasanna:** So about two and a half years ago or so, Jack really felt like things needed to change. I think he had a sense that the industry was going in a different direction. So he got about 40 of the company's top executives into a room on a weekly basis, and they all used to sort of talk everything through that was going on and he added me to that group.

**Dhanji R. Prasanna:** So at some point, I observed that we were talking about lots of deep things, lots of relevant things, but no one was really paying attention to AI, and so that's when I wrote that letter. And to be honest, it's I think taken on a life of its own, but there wasn't much to the letter other than I think we should do this. I think we should do it centrally and it's important for us to be ahead of the game and be an AI native company because that's where the industry is heading.

**Lenny Rachitsky:** Let me just say it's important to note you were not CTO at this point. You were just a senior engineer kind of person?

**Dhanji R. Prasanna:** No, yeah, in fact, I was part-time at the time because I had just had a kid and I was coming back in and I was helping out one of the engineering teams and then Jack came over to Sydney and spent two days with me and both of us like long walks. So we walked all around Sydney and talked it through up and down, and then yeah, he offered me the job and I thought it was a great opportunity once in a lifetime, so I took it.

**Lenny Rachitsky:** It's like be careful what you're good at sort of situation. Okay. So what were some of the bigger changes that you made after Jack is on board and Block execs are on board of are, "Cool, this is completely right. We need to go much bigger and think much more deeply about how AI is changing, how we build and how we should build." Or some of the bigger changes that you made from a perspective of other companies listening to this, trying to think about what they should be doing?

**Dhanji R. Prasanna:** At the start, my main focus was to get block to think like a technology company. And for a long time we had had a little bit of, I'm going to call it identity drift, maybe. We were talking about ourselves as a financial services company. Some people called us FinTech, all of this stuff. But when I started working at what was then known as Square, we were always thought of as a technology company just like Google or Facebook or any of the others.

**Dhanji R. Prasanna:** And so I wanted to get us back to that. And so the first thing I did was to try and institute a number of programs that focused on that. So everything from getting the top ICs in the company together to talk to each other, to starting a whole bunch of special projects. So we got about two to five engineers per project. There were about eight or nine different projects and we had reinstituted, the company-wide hack week.

**Dhanji R. Prasanna:** And so all of this just kind of created a little bit of a spark of, "Hey, we're building technology again, we're trying to push the frontier again." And that's how it started, and then there were a whole number of steps after that where we went from a GM structure to a functional org structure, which was I think the key to making our transformation into being more of an AI-native company.

**Lenny Rachitsky:** Okay, talk more about that. What does that mean? What does that look like? Why is that so important?

**Dhanji R. Prasanna:** Absolutely. So when we were in our mature phase, so when Square was working quite well, it was a very large business, and then we had started Cash App and that also followed suit. We had spun them out almost as what we call a GM structure. So they were effectively run as a portfolio of independent companies and they had their own CEOs who all reported to Jack and it was still one single executive team, but they had separate engineering practices, they had separate design teams.

**Dhanji R. Prasanna:** They were kind of separate in almost every way except for some shared resources like our foundational resources like legal and some platforms and things like that. So I think that that was very useful for us for the stage of company that we were in, but when you really want to go deep in technology, when you really want to connect with these things that are industry changing events that are happening, you need a singular focus, and we changed the organization.

**Dhanji R. Prasanna:** So all engineers report into one single team now, all designers report into one single team and there's single head of engineering, single head of design, et cetera. And so that was the big transformation that we made, and that meant we could really drive forward AI, we could drive forward platform and just technical depth generally.

**Lenny Rachitsky:** For companies that are struggling with this potentially or trying to figure out how to do this, two things I'm hearing here is start to see yourself as a technology company. It doesn't necessarily apply to every company, but seems like an important element is like we're building technology, we're not a financial company, we're not a real estate company, we're not a technology company. And then two is organize the team such that say engineers report up to an engineering leader versus a GM who maybe doesn't understand engineering as well or doesn't take it as seriously as they should.

**Dhanji R. Prasanna:** Yeah, I think that's pretty much what we did. And not to lean too heavily on this, but this is what jobs did when he came back to Apple as well. He reorganized Apple to be functional, and it wasn't like we were following a playbook. We discovered this as we were investigating what it's going to take to make these teams more tech-focused and to bring our DNA back to our roots, which really was putting engineering and design first, which is what technology first means to me. So yeah, I would say to companies, find your DNA and really try to optimize for what that is in a very simple and clear way.

**Lenny Rachitsky:** Okay, so you made a bunch of changes, you had this manifesto, everyone's on board, you made a bunch of changes. Functional technology first, comparing the way that your say engineering team works today versus two or three years ago, what is most different?

