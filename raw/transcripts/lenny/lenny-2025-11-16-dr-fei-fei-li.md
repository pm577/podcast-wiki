---
episode_date: '2025-11-16'
guest: dr-fei-fei-li
id: lenny-2025-11-16-dr-fei-fei-li
key_insights:
- 'Dr. Fei Fei Li: In the middle of 2015, middle of 2016, some tech companies avoid
  using the word AI because they were not sure if AI was a dirty word. 2017-ish was
  the beginning of companies calling themselves AI comp...'
podcast: lenny
tags:
- saas
- startups
- hiring
- marketplace
- ai-ml
- fundraising
title: The Godmother of AI on jobs, robots & why world models are next | Dr. Fei-Fei
  Li
type: Episode
word_count: 11651
---

# The Godmother of AI on jobs, robots & why world models are next | Dr. Fei-Fei Li

Jobs, robots & why world models are next, covering AI product work, product design, and consumer products.

**Guest:** Dr. Fei Fei Li
**Date:** 2025-11-16
**YouTube:** https://www.youtube.com/watch?v=Ctjiatnd6Xk
**Topics:** saas, startups, hiring, marketplace, ai-ml, fundraising

## Key Topics Discussed

- [[saas]]
- [[startups]]
- [[hiring]]
- [[marketplace]]
- [[ai-ml]]
- [[fundraising]]

## Transcript Highlights

**Lenny Rachitsky:** A lot of people call you the godmother of AI. The work you did actually was the spark that brought us out of AI winter.

**Dr. Fei Fei Li:** In the middle of 2015, middle of 2016, some tech companies avoid using the word AI because they were not sure if AI was a dirty word. 2017-ish was the beginning of companies calling themselves AI companies.

**Lenny Rachitsky:** There's this line, I think, this was when you were presenting to Congress. There's nothing artificial about AI. It's inspired by people. It's created by people, and most importantly, it impacts people.

**Dr. Fei Fei Li:** It's not like I think AI will have no impact on jobs or people. In fact, I believe that whatever AI does, currently or in the future, is up to us. It's up to the people. I do believe technology is a net positive for humanity, but I think every technology is a double-edged sword. If we're not doing the right thing as a society, as individuals, we can screw this up as well.

**Lenny Rachitsky:** You had this breakthrough insight of just, okay, we can train machines to think like humans, but it's just missing the data that humans have to learn as a child.

**Dr. Fei Fei Li:** I chose to look at artificial intelligence through the lens of visual intelligence because humans are deeply visual animals. We need to train machines with as much information as possible on images of objects, but objects are very, very difficult to learn. A single object can have infinite possibilities that is shown on an image. In order to train computers with tens and thousands of object concepts, you really need to show it millions of examples.

**Lenny Rachitsky:** Today, my guest is Dr. Fei-Fei Li, who's known as the godmother of AI. Fei-Fei has been responsible for and at the center of many of the biggest breakthroughs that sparked the AI revolution that we're currently living through. She spearheaded the creation of ImageNet, which was basically her realizing that AI needed a ton of clean-labeled data to get smarter, and that data set became the breakthrough that led to the current approach to building and scaling AI models. She was chief AI scientist at Google Cloud, which is where some of the biggest early technology breakthroughs emerged from. She was director at SAIL, Stanford's Artificial Intelligence Lab, where many of the biggest AI minds came out of. She's also co-creator of Stanford's Human-Centered AI Institute, which is playing a vital role in a direction that AI is taking. She's also been on the board of Twitter. She was named one of Time's 100 Most Influential People in AI. She's also United Nations advisory board. I could go on.

**Lenny Rachitsky:** In our conversation, Fei-Fei shares a brief history of how we got to today in the world of AI, including this mind-blowing reminder that 9 to 10 years ago, calling yourself an AI company was basically a death knell for your brand because no one believed that AI was actually going to work. Today, it's completely different. Every company is an AI company. We also chat about her take on how she sees AI impacting humanity in the future, how far current technologies will take us, why she's so passionate about building a world model and what exactly world models are, and most exciting of all, the launch of the world's first large world model, Marble, which just came out as this podcast comes out. Anyone can go play with this at marble.worldlabs.ai. It's insane. Definitely check it out. Fei-Fei is incredible and way too under the radar for the impact that she's had on the world, so I am really excited to have her on and to spread her wisdom with more people.

**Dr. Fei Fei Li:** I'm excited to be here, Lenny.

**Lenny Rachitsky:** I'm even more excited to have you here. It is such a treat to get to chat with you. There's so much that I want to talk about. You've been at the center of this AI explosion that we're seeing right now for so long. We're going to talk about a bunch of the history that I think a lot of people don't even know about how this whole thing started, but let me first read a quote from Wired about you just so people get a sense, and in the intro I'll share all of the other epic things you've done. But I think this is a good way to just set context. "Fei-Fei is one of a tiny group of scientists, a group perhaps small enough to fit around a kitchen table, who are responsible for AI's recent remarkable advances."

**Lenny Rachitsky:** A lot of people call you the godmother of AI, and unlike a lot of AI leaders, you're an AI optimist. You don't think AI is going to replace us. You don't think it's going to take all our jobs. You don't think it's going to kill us. So I thought it'd be fun to start there, just what's your perspective on how AI is going to impact humanity over time?

**Dr. Fei Fei Li:** Yeah, okay, so Lenny, let me be very clear. I'm not a utopian, so it's not like I think AI will have no impact on jobs or people. In fact, I'm a humanist. I believe that whatever AI does, currently or in the future, is up to us. It's up to the people. So I do believe technology is a net positive for humanity. If you look at the long course of civilization, I think we are, and fundamentally, we're an innovative species that we... If you look at from written record thousands of years ago to now, humans just kept innovating ourselves and innovating our tools, and with that, we make lives better, we make work better, we build civilization, and I do believe AI is part of that. So that's where the optimism comes from. But I think every technology is a double-edged sword, and if we're not doing the right thing as a species, as a society, as communities, as individuals, we can screw this up as well.

**Lenny Rachitsky:** There's this line, I think, this was when you were presenting to Congress, "There's nothing artificial about AI. It's inspired by people. It's created by people, and most importantly, it impacts people." I don't have a question there, but what a great line.

**Dr. Fei Fei Li:** Yeah, I feel pretty deeply. I started working AI two and a half decades ago, and I've been having students for the past two decades and almost every student who graduates, I remind them when they graduate from my lab that your field is called artificial intelligence, but there's nothing artificial about it.

**Lenny Rachitsky:** Coming back to the point you just made about how it's kind of up to us about where this all goes, what is it you think we need to get right? How do we set things on a path? I know this is a very difficult question to answer, but just what's your advice? What do you think we should be keeping in mind?

**Dr. Fei Fei Li:** Yeah, how many hours do we have?

**Lenny Rachitsky:** How do we align AI? There we go. Let's solve it.

**Dr. Fei Fei Li:** So I think people should be responsible individuals no matter what we do. This is what we teach our children, and this is what we need to do as grownups as well. No matter which part of the AI development or AI deployment or AI application you are participating in, and most likely many of us, especially as technologists, we're in multiple points. We should act like responsible individuals and care about this. Actually, care a lot about this. I think everybody today should care about AI because it is going to impact your individual life. It is going to impact your community, it's going to impact the society and the future generation. And caring about it as a responsible person is the first, but also the most important step.

**Lenny Rachitsky:** Okay, so let me actually take a step back and kind of go to the beginning of AI. Most people started hearing and caring about AI, as what it's called today, just like, I don't know, a few years ago when ChatGPT came out. Maybe it was like three years ago.

**Dr. Fei Fei Li:** Three years ago, almost one more month, three years ago.

**Lenny Rachitsky:** Wow, okay. And that was ChatGPT coming out. Is that the milestone you have in mind?

**Dr. Fei Fei Li:** Yes.

**Lenny Rachitsky:** Okay, cool. That's exactly how I saw it. But very few people know there was a long, long history of people working on, it was called machine learning back then and there's other terms, and now it's just everything's AI and there was kind of a long period of just a lot of people working on it. And then there's this what people refer to as the AI winter where people just gave up almost, most people did, and just, okay, this idea isn't going anywhere. And then the work you did actually was essentially the spark that brought us out of AI winter and is directly responsible for the world where now of just AI is all we talk about. As you just said, it's going to impact everything we do. So I thought it'd be really interesting to hear from you just the brief history of what the world was like before ImageNet and just the work you did to create ImageNet, why that was so important, and then just what happened after.

**Dr. Fei Fei Li:** It is, for me, hard to keep in mind that AI is so new for everybody when I lived my entire professional life in AI. There's a part of me that is just, it's so satisfying to see a personal curiosity that I started barely out of teenagehood and now has become a transformative force of our civilization. It generally is a civilizational level technology. So that journey is about 30 years or 20 something, 20 plus years, and it's just very satisfying. So where did it all start? Well, I'm not even the first generation AI researcher. The first generation really date back to the '50s and '60s, and Alan Turing was ahead of his time in the '40s by asking, daring humanity with the question, "Is there thinking machines?" And of course he has a specific way of testing this concept of thinking machine, which is a conversational chatbot, which to his standard we now have a thinking machine.

**Dr. Fei Fei Li:** But that was just a more anecdotal inspiration. The field really began in the '50s when computer scientists came together and look at how we can use computer programs and algorithms to build these programs that can do things that have been only capable by human cognition. And that was the beginning. And the founding fathers the Dartmouth workshop in the 1956, we have Professor John McCarthy who later came to Stanford who coined the term artificial intelligence. And between the '50s, '60s, '70s, and '80s, it was the early days of AI exploration and we had logic systems, we had expert systems, we also had early exploration of neural network. And then it came to around the late '80s, the '90s, and the very beginning of the 21st century. That stretch about 20 years is actually the beginning of machine learning, is the marriage between computer programming and statistical learning.

**Dr. Fei Fei Li:** And that marriage brought a very, very critical concept into AI, which is that purely rule-based program is not going to account for the vast amount of cognitive capabilities that we imagine computers can do. So we have to use machines to learn the patterns. Once the machines can learn the patterns, it has a hope to do more things. For example, if you give it three cats, the hope is not just for the machines to recognize these three cats. The hope is the machines can recognize the fourth cat, the fifth cat, the sixth cat, and all the other cats. And that's a learning ability that is fundamental to humans and remaining animals. And we, as a field, realized, "We need machine learning." So that was up till the beginning of the 21st century. I entered the field of AI literally in the year of 2000. That's when my PhD began at Caltech.

**Dr. Fei Fei Li:** And so I was one of the first generation machine learning researchers and we were already studying this concept of machine learning, especially neural network. I remember that was one of my first courses at Caltech is called neural network, but it was very painful. It was still smack in the middle of the so-called AI winter, meaning the public didn't look at this too much. There wasn't that much funding, but there was also a lot of ideas flowing around. And I think two things happened to myself that brought my own career so close to the birth of modern AI is that I chose to look at artificial intelligence through the lens of visual intelligence because humans are deeply visual animals. We can talk a little more later, but so much of our intelligence is built upon visual, perceptual, spatial understanding, not just language per se. I think they're complementary.

**Dr. Fei Fei Li:** So I choose to look at visual intelligence and my PhD and my early professor years, my students and I are very committed to a north star problem, which is solving the problem of object recognition because it's a building block for the perceptual world, right? We go around the world interpreting reasoning and interacting with it more or less at the object level. We don't interact with the world at the molecular level. We don't interact with the world as... We sometimes do, but we rarely, for example, if you want to lift a teapot, you don't say, "Okay, the teapot is made of a hundred pieces of porcelain and let me work on this a hundred pieces." You look at this as one object and interact with it. So object is really important. So I was among the first researchers to identify this as a north star problem, but I think what happened is that as a student of AI and a researcher of AI, I was working on all kinds of mathematical models including neural network, including Bayesian network, including many, many models.

**Dr. Fei Fei Li:** And there was one singular pain point is that these models don't have data to be trained on. And as a field, we were so focusing on these models, but it dawned on me that human learning as well as evolution is actually a big data learning process. Humans learn with so much experience constantly. In the evolution, if you look at time, animals evolve with just experiencing the world. So I think my students and I conjectured that a very critically-overlooked ingredient of bringing AI to life is big data. And then we began this ImageNet project in 2006, 2007. We were very ambitious. We want to get the entire internet's image data on objects. Now granted internet was a lot smaller than today, so I felt like that ambition was at least not too crazy. Now, it's totally delusional to think a couple of graduate student and a professor can do this.

**Dr. Fei Fei Li:** And that's what we did. We curated very carefully, 15 million images on the internet, created a taxonomy of 22,000 concepts, borrowing other researchers' work like linguists work on WordNet, and it's a particular way of dictionarying words. And we combine that into ImageNet and we open-sourced that to the research community. We held an annual ImageNet challenge to encourage everybody to participate in this. We continue to do our own research, but 2012 was the moment that many people think was the beginning of the deep learning or birth of modern AI because a group of Toronto researchers led by Professor Geoff Hinton, participated in ImageNet Challenge, used ImageNet big data and two GPUs from NVIDIA and created successfully the first neural network algorithm that can...

