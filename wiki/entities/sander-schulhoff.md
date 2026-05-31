---
title: Sander Schulhoff
created: 2026-05-31
updated: 2026-05-31
type: entity
tags: [person, ai-security, prompt-engineering, red-teaming, hackaprompt, adversarial-robustness]
sources:
  - raw/transcripts/lenny/sander-schulhoff.md
  - raw/transcripts/lenny/sander-schulhoff-20.md
confidence: high
---

# Sander Schulhoff

OG prompt engineer and leading AI security researcher. Created the first comprehensive prompt engineering guide on the internet (two months before ChatGPT's release). Founder of HackAPrompt (the first and largest AI red-teaming competition). Led The Prompt Report — a 76-page study co-authored with OpenAI, Microsoft, Google, Princeton, and Stanford analyzing 1,500+ papers and 200 prompting techniques.

## Key Views

### 1. Prompt Engineering Is Not Dead — It's More Important Than Ever

"Studies have shown that using bad prompts can get you down to 0% on a problem, and good prompts can boost you up to 90%. People will always be saying 'it's dead' with the next model version, but then it comes out and it's not." Prompt engineering remains a critical skill even as models improve — better models amplify the value of good prompting.^[raw/transcripts/lenny/sander-schulhoff.md]

### 2. Self-Criticism: The Most Effective Prompting Technique

The technique: ask the LLM to check its own response, criticize it, and improve it. "Can you go and check your response?" This simple loop catches errors, improves reasoning, and produces significantly better outputs. It's the highest-leverage single technique in the Prompt Report's analysis of 200+ techniques.^[raw/transcripts/lenny/sander-schulhoff.md]

### 3. AI Guardrails Do Not Work — This Is Not a Solvable Problem

"Guardrails do not work. If someone is determined enough to trick GPT-5, they're going to deal with that guardrail. No problem." Unlike classical security (where you can patch a bug with high confidence), AI systems are fundamentally vulnerable to adversarial inputs. "You can patch a bug, but you can't patch a brain." The only reason we haven't seen massive AI attacks is early adoption, not security.^[raw/transcripts/lenny/sander-schulhoff-20.md]

### 4. Prompt Injection Is an Existential Security Problem for Agents

"If we can't even trust chatbots to be secure, how can we trust agents to go and manage our finances? If somebody goes up to a humanoid robot and gives it the middle finger, how can we be certain it's not going to punch that person in the face?" As AI systems gain more autonomy and ability to take actions in the real world, the prompt injection vulnerability becomes increasingly dangerous. This is a fundamental research problem without a clear solution.^[raw/transcripts/lenny/sander-schulhoff.md]

### 5. Red Teaming Is the Best Defense We Have

While we can't eliminate AI security vulnerabilities, continuous red teaming — systematically testing models for weaknesses — is the best available defense. Schulhoff partners with frontier labs to run red-teaming competitions that discover novel attack vectors before malicious actors do. The goal: surface vulnerabilities in controlled environments so labs can build better defenses.^[raw/transcripts/lenny/sander-schulhoff-20.md]

## Episode Appearances

- [[sander-schulhoff]] — *AI prompt engineering in 2025: What works and what doesn't*
- [[sander-schulhoff-20]] — *Why securing AI is harder than anyone expected*

## Related Concepts

- [[prompt-engineering]]
- [[ai-security]]
- [[red-teaming]]
- [[prompt-injection]]
- [[adversarial-robustness]]
