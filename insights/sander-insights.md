# Sander — Insights

*Extracted from podcast appearances.*

### Insight: AI guardrails do not work. If someone is determined enough to trick GPT-5, they'...
**Claim:** AI guardrails do not work. If someone is determined enough to trick GPT-5, they're going to deal with that guardrail. No problem. When these guardrail providers say, 'We catch everything,' that's a complete lie.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Sander states that AI guardrails are ineffective against determined attackers.

### Insight: You can patch a bug, but you can't patch a brain. If you find some bug in your s...
**Claim:** You can patch a bug, but you can't patch a brain. If you find some bug in your software and you go and patch it, you can be maybe 99.99% sure that bug is solved. Try to do that in your AI system. You can be 99.99% sure that the problem is still there.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Sander explains the fundamental difference between patching software bugs and securing AI systems.

### Insight: The only reason there hasn't been a massive attack yet is how early the adoption...
**Claim:** The only reason there hasn't been a massive attack yet is how early the adoption is, not because it's secured.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Lenny quotes Alex Komoroske on the current state of AI security.

### Insight: Not only do you have a God in the box, but that God is angry, that God is malici...
**Claim:** Not only do you have a God in the box, but that God is angry, that God is malicious, that God wants to hurt you. Can we control that malicious AI and make it useful to us and make sure nothing bad happens?
**Audience:** general | **Actionability:** 4/10 | **Confidence:** 0.8
**Source:** sander-schulhoff-20
**Context:** Sander describes the alignment problem with a metaphor.

### Insight: AI guardrails are, for the most part, a large language model that is trained or ...
**Claim:** AI guardrails are, for the most part, a large language model that is trained or prompted to look at inputs and outputs to an AI system and determine whether they are valid or malicious. They are terribly, terribly insecure and frankly, they don't work.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Sander explains what guardrails are and why they fail.

### Insight: Jailbreaking is like when it's just you and the model. Prompt injection occurs w...
**Claim:** Jailbreaking is like when it's just you and the model. Prompt injection occurs when somebody has built an application or sometimes an agent, and a malicious user tries to get the model to ignore the developer prompt.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Sander defines jailbreaking and prompt injection.

### Insight: Second-order prompt injection attacks can chain multiple agents to perform malic...
**Claim:** Second-order prompt injection attacks can chain multiple agents to perform malicious actions like CRUD on databases and sending external emails, as demonstrated in ServiceNow Assist AI.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Discussion of ServiceNow Assist AI vulnerability where a benign agent recruited more powerful agents to perform attacks.

### Insight: The only reason there hasn't been a massive attack yet is early adoption, not be...
**Claim:** The only reason there hasn't been a massive attack yet is early adoption, not because systems are secure; no meaningful mitigations exist.
**Audience:** founder | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Quote from Alex Komoroske about the lack of mitigation and the risk being due to low adoption.

### Insight: Prompt injection can cause real damage: e.g., MathGPT was tricked into writing m...
**Claim:** Prompt injection can cause real damage: e.g., MathGPT was tricked into writing malicious code that exfiltrated API keys by ignoring instructions.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Example of MathGPT where user input caused code execution and secret exfiltration.

### Insight: Jailbreaking can be achieved by separating malicious requests into smaller, seem...
**Claim:** Jailbreaking can be achieved by separating malicious requests into smaller, seemingly legitimate requests across different instances, as seen in the Claude Code cyber attack.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Description of how attackers bypassed Claude Code's defenses by splitting requests into separate instances.

### Insight: As agents gain control over the world (e.g., robots), prompt injection becomes m...
**Claim:** As agents gain control over the world (e.g., robots), prompt injection becomes more dangerous, potentially causing physical harm like a robot punching someone.
**Audience:** general | **Actionability:** 5/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Discussion of future risks with VLM-powered robots and existing jailbreaks of robotic systems.

### Insight: Current AI security industry focuses on monitoring, compliance, and automated re...
**Claim:** Current AI security industry focuses on monitoring, compliance, and automated red teaming/guardrails, but the latter two are less useful.
**Audience:** investor | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** sander-schulhoff-20
**Context:** Market map analysis of AI security industry, noting that automated red teaming and guardrails are not as effective.

### Insight: Guardrails are deployed as input and output filters to block malicious content, ...
**Claim:** Guardrails are deployed as input and output filters to block malicious content, but they can be bypassed.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Explanation of guardrail deployment pattern: one model watches inputs, another watches outputs.

### Insight: Guardrails are placed both in front of and behind the model to watch inputs and ...
**Claim:** Guardrails are placed both in front of and behind the model to watch inputs and outputs for malicious content.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Discussion of common deployment pattern with guardrails

### Insight: Adversarial robustness measures how well a system defends against attacks, often...
**Claim:** Adversarial robustness measures how well a system defends against attacks, often quantified by attack success rate (ASR).
**Framework:** Adversarial robustness
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Explanation of adversarial robustness and ASR

### Insight: Automated red teaming systems always find vulnerabilities in any model because a...
**Claim:** Automated red teaming systems always find vulnerabilities in any model because all current chatbots are based on transformers and are vulnerable to prompt injection and jailbreaking.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Critique of automated red teaming effectiveness

### Insight: The number of possible attacks against an LLM is effectively infinite (e.g., one...
**Claim:** The number of possible attacks against an LLM is effectively infinite (e.g., one followed by a million zeros for GPT-5), making claims of 99% effectiveness statistically insignificant.
**Audience:** investor | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Explanation of attack space size and limitations of guardrail metrics

### Insight: Adaptive attacks, especially human attackers, break all state-of-the-art defense...
**Claim:** Adaptive attacks, especially human attackers, break all state-of-the-art defenses within 10-30 attempts, while automated systems require orders of magnitude more attempts.
**Framework:** Adaptive evaluation
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Findings from a research paper with OpenAI, Google DeepMind, and Anthropic

### Insight: Guardrails do not dissuade determined attackers because if someone can trick GPT...
**Claim:** Guardrails do not dissuade determined attackers because if someone can trick GPT-5, they can also bypass the guardrail.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Discussion of whether guardrails deter attackers

### Insight: Some guardrail companies fabricate statistics and their models may not work on n...
**Claim:** Some guardrail companies fabricate statistics and their models may not work on non-English languages.
**Audience:** investor | **Actionability:** 6/10 | **Confidence:** 0.7
**Source:** sander-schulhoff-20
**Context:** Insider information about guardrail company practices

### Insight: If your AI system only acts on the user's own data and cannot take actions affec...
**Claim:** If your AI system only acts on the user's own data and cannot take actions affecting others, you may not need guardrails because the user can only harm themselves.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Discussion about when guardrails are unnecessary for simple chatbots that don't take actions or access external data.

### Insight: Any data the AI has access to, the user can make it leak; any actions it can tak...
**Claim:** Any data the AI has access to, the user can make it leak; any actions it can take, the user can make it take. Therefore, proper permissioning (classical cybersecurity) is essential.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Summarizing that AI security reduces to classical cybersecurity: lock down data and actions.

### Insight: Prompt-based defenses (e.g., instructing the model to ignore malicious instructi...
**Claim:** Prompt-based defenses (e.g., instructing the model to ignore malicious instructions) are the worst defenses and have been known to be ineffective since early 2023.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Critique of companies promoting prompt-based defenses as an alternative to guardrails.

### Insight: Automated red teaming always works on any transformer-based system, and guardrai...
**Claim:** Automated red teaming always works on any transformer-based system, and guardrails work too poorly to stop attacks.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Summary of the guardrails don't work rant.

### Insight: The smartest AI researchers at Frontier Labs cannot solve adversarial robustness...
**Claim:** The smartest AI researchers at Frontier Labs cannot solve adversarial robustness, so enterprises without AI researchers should not expect to solve it either.
**Audience:** founder | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Argument against trusting guardrail vendors.

### Insight: Frontier labs prioritize model capabilities over security because smarter models...
**Claim:** Frontier labs prioritize model capabilities over security because smarter models generate more revenue, while security investments don't directly increase sales.
**Audience:** investor | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Discussion of why AI companies don't apply more resources to adversarial robustness.

### Insight: The only reason there hasn't been a massive AI attack is low adoption, not becau...
**Claim:** The only reason there hasn't been a massive AI attack is low adoption, not because systems are secure.
**Audience:** general | **Actionability:** 4/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Lenny paraphrasing Alex Komoroski's point about early adoption masking insecurity.

### Insight: For read-only chatbots with no actions, don't spend time on guardrails or red te...
**Claim:** For read-only chatbots with no actions, don't spend time on guardrails or red teaming because they can't cause real damage and defenses are easily bypassed.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Discussion about when to invest in AI security vs. not

### Insight: The most valuable security work is at the intersection of classical cybersecurit...
**Claim:** The most valuable security work is at the intersection of classical cybersecurity and AI security; hire someone with both skill sets.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Advice on building security teams for AI systems

### Insight: For agentic systems that can take actions (e.g., read/send emails), prompt injec...
**Claim:** For agentic systems that can take actions (e.g., read/send emails), prompt injection is a serious threat; attackers can trick the AI into performing malicious actions via untrusted data.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Example of an email-reading/sending agent being tricked by a malicious email

### Insight: To secure an agentic system that executes code, containerize the code execution ...
**Claim:** To secure an agentic system that executes code, containerize the code execution (e.g., Docker) and sanitize outputs to prevent prompt injection from causing harm.
**Audience:** engineer | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Example of a math question system that runs code; solution to prompt injection

### Insight: Always log all inputs and outputs of AI systems for monitoring and improvement, ...
**Claim:** Always log all inputs and outputs of AI systems for monitoring and improvement, but this is not a security defense.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** General AI deployment practice recommendation

### Insight: Deploying multiple guardrails is impractical and ineffective; they don't dissuad...
**Claim:** Deploying multiple guardrails is impractical and ineffective; they don't dissuade attackers and consume too much product development time.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Discussion on guardrail effectiveness and practicality

### Insight: Treat any agentic system exposed to the internet as a potentially malicious AI (...
**Claim:** Treat any agentic system exposed to the internet as a potentially malicious AI ('angry god') and design controls to contain it.
**Framework:** Control
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Concept of controlling a malicious AI from the field of AI control

### Insight: Agentic AI systems are easier to attack and trick into doing bad things than eli...
**Claim:** Agentic AI systems are easier to attack and trick into doing bad things than eliciting CBRNE information.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Discussion of red teaming competitions and agent vulnerabilities.

### Insight: CAMEL is a framework that restricts agent permissions ahead of time based on the...
**Claim:** CAMEL is a framework that restricts agent permissions ahead of time based on the user's request, preventing prompt injection attacks when read and write permissions are not both needed.
**Framework:** CAMEL
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Explanation of CAMEL and how it blocks attacks by granting only necessary permissions.

### Insight: CAMEL cannot help when both read and write permissions are required for a legiti...
**Claim:** CAMEL cannot help when both read and write permissions are required for a legitimate task, as the agent then has enough permissions for an attack to occur.
**Framework:** CAMEL
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Example of reading and forwarding emails requiring both permissions.

### Insight: Education and awareness about prompt injection are crucial to prevent poor deplo...
**Claim:** Education and awareness about prompt injection are crucial to prevent poor deployment decisions and to build a team with AI security expertise.
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Discussion of education as a key mitigation strategy.

### Insight: There has been no meaningful progress in solving adversarial robustness, prompt ...
**Claim:** There has been no meaningful progress in solving adversarial robustness, prompt injection, or jailbreaking in the last few years.
**Audience:** founder | **Actionability:** 3/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Critique of current defenses and reporting methods.

### Insight: Companies should use adaptive evaluations (human evals) rather than static datas...
**Claim:** Companies should use adaptive evaluations (human evals) rather than static datasets to measure adversarial robustness.
**Audience:** engineer | **Actionability:** 7/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Discussion of how companies report robustness and the need for better evaluations.

### Insight: Adversarial training during pre-training (when the model is very small) could ma...
**Claim:** Adversarial training during pre-training (when the model is very small) could make models more robust, but resources have not been deployed to do this.
**Audience:** founder | **Actionability:** 2/10 | **Confidence:** 0.7
**Source:** sander-schulhoff-20
**Context:** Idea about training mechanisms to improve robustness.

### Insight: Solving indirect prompt injection against agents is much more difficult than pre...
**Claim:** Solving indirect prompt injection against agents is much more difficult than preventing CBRN elicitation because the model must sometimes perform actions like sending emails, making it hard to define the line not to cross.
**Audience:** engineer | **Actionability:** 6/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Discussion on difficulty of indirect prompt injection vs. CBRN elicitation

### Insight: Adversarial training deeper in the stack (when AI is very small) is promising fo...
**Claim:** Adversarial training deeper in the stack (when AI is very small) is promising for robustness, but resources have not been deployed to do that.
**Audience:** founder | **Actionability:** 4/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Discussion on adversarial training during early training stages

### Insight: Current guardrails and automated red teaming solutions are not effective; many a...
**Claim:** Current guardrails and automated red teaming solutions are not effective; many are open source and free, and the market will see a correction as companies realize they don't work.
**Audience:** investor | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Prediction about AI security market correction

### Insight: Companies should not rely on guardrails for security because they can lead to ov...
**Claim:** Companies should not rely on guardrails for security because they can lead to overconfidence, especially as agents and robotics powered by LLMs are deployed and can cause real damage.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Final takeaways on guardrails and upcoming dangers

### Insight: Researchers should stop publishing jailbreak papers because we already know mode...
**Claim:** Researchers should stop publishing jailbreak papers because we already know models can be broken, and such papers only provide easier attacks to malicious actors.
**Framework:** Do not write that jailbreak paper
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Advice against offensive adversarial security research

### Insight: Human-in-the-loop solutions are not a long-term fix because the market wants aut...
**Claim:** Human-in-the-loop solutions are not a long-term fix because the market wants autonomous AI agents that don't require human intervention for every action.
**Audience:** founder | **Actionability:** 3/10 | **Confidence:** 0.8
**Source:** sander-schulhoff-20
**Context:** Discussion on human-in-the-loop as a pseudo-solution

### Insight: Companies like Trustible (governance/compliance) and Repello (AI discovery) are ...
**Claim:** Companies like Trustible (governance/compliance) and Repello (AI discovery) are providing valuable services in AI security, especially for discovering shadow AI deployments.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.8
**Source:** sander-schulhoff-20
**Context:** Shout-out to companies doing good work in AI security

### Insight: Deploying guardrails on chatbots is not enough; as agents and robotics powered b...
**Claim:** Deploying guardrails on chatbots is not enough; as agents and robotics powered by LLMs are deployed, they can cause financial loss and eventually physical injury.
**Audience:** founder | **Actionability:** 7/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Discussion about the increasing danger of AI systems as they move from chatbots to agents and robotics.

### Insight: AI security is fundamentally different from classical security; you can patch a ...
**Claim:** AI security is fundamentally different from classical security; you can patch a bug but you can't patch a brain.
**Audience:** engineer | **Actionability:** 5/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Explaining why AI security requires a different approach than traditional cybersecurity.

### Insight: You need both an AI researcher and a classical security person on your team to u...
**Claim:** You need both an AI researcher and a classical security person on your team to understand the entirety of the AI security situation.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Advice on building a team to handle AI security effectively.

### Insight: Education is a crucial part of AI security; the industry needs to take it seriou...
**Claim:** Education is a crucial part of AI security; the industry needs to take it seriously before it gets dangerous.
**Audience:** general | **Actionability:** 6/10 | **Confidence:** 0.85
**Source:** sander-schulhoff-20
**Context:** Emphasizing the importance of education in AI security.

### Insight: Before deploying an AI system, think very long and hard about whether it is pote...
**Claim:** Before deploying an AI system, think very long and hard about whether it is potentially prompt injectable and consider using CaMeL or similar defenses, or decide not to deploy.
**Framework:** CaMeL
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** sander-schulhoff-20
**Context:** Actionable advice for engineers deploying AI systems.

### Insight: The most useful thing you can do is think very long and hard before deploying yo...
**Claim:** The most useful thing you can do is think very long and hard before deploying your AI system and consider if you shouldn't deploy it at all.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** sander-schulhoff-20
**Context:** Final advice on responsible AI deployment.
