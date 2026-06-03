# Colin Matthews — Insights

*Extracted from podcast appearances.*

## Insight 1: AI development tools come in three types: chatbots (e.g., Claude, ChatGPT), clou...
**Claim:** AI development tools come in three types: chatbots (e.g., Claude, ChatGPT), cloud development environments (e.g., Replit, Bolt, v0, Lovable), and local developer assistants (e.g., GitHub Copilot, Cursor, Windsurf, Zed).
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Choosing your tooling section, categorizing AI tools for prototyping.

## Insight 2: Chatbots like ChatGPT and Claude are best for simple, one-page prototypes like c...
**Claim:** Chatbots like ChatGPT and Claude are best for simple, one-page prototypes like calculators, flip cards, or data visualizations, but cannot host code or handle complex multi-page apps.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Chatbots section, describing their capabilities and limitations.

## Insight 3: Cloud development environments like v0, Bolt, Replit, and Lovable can build full...
**Claim:** Cloud development environments like v0, Bolt, Replit, and Lovable can build full-stack prototypes with multiple pages, handle backend infrastructure, and deploy code, but differ in hosting and features (e.g., v0 uses Next.js and Shadcn UI, Bolt runs server in browser, Replit excels at Python and internal tools, Lovable integrates with GitHub and Supabase).
**Audience:** operator | **Actionability:** 9/10 | **Confidence:** 0.9
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Cloud development environments section, comparing tools.

## Insight 4: To build a functional prototype quickly, use a cloud development environment lik...
**Claim:** To build a functional prototype quickly, use a cloud development environment like Replit or v0, and iterate by prompting for specific features (e.g., 'Add collision for the shot when it hits a tank').
**Audience:** operator | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Example of building a 2-D tank game in 10 minutes with iterative prompts.

## Insight 5: Lovable is best for building production-ready products due to its integrations w...
**Claim:** Lovable is best for building production-ready products due to its integrations with GitHub, Supabase, and AI providers, but lacks a code editor, making debugging difficult; users often start in Lovable and move to Cursor for fixes.
**Audience:** operator | **Actionability:** 7/10 | **Confidence:** 0.85
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Lovable section, describing its strengths and weaknesses.

## Insight 6: Bolt cannot natively support prototypes needing user identity, multi-user intera...
**Claim:** Bolt cannot natively support prototypes needing user identity, multi-user interactions, secure data operations, or persistent storage because server code runs in the browser; these can be added via external services like Supabase.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Bolt section, explaining its limitations.

## Insight 7: Replit excels at building internal admin tools (e.g., file conversion, job appli...
**Claim:** Replit excels at building internal admin tools (e.g., file conversion, job applicant tracking) and data-driven applications (e.g., image resizing, multi-page dashboards) with simple UIs, and is preferred when a fully functional backend or Python code is needed.
**Audience:** operator | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Replit section, describing its best use cases.

## Insight 8: Lovable lacks a code editor, making debugging difficult; users often start featu...
**Claim:** Lovable lacks a code editor, making debugging difficult; users often start features in Lovable but move to Cursor to resolve problems.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Comparison of AI development tools, specifically drawbacks of Lovable.

## Insight 9: Choose v0 for beautiful designs by default, Bolt for quick prototypes with flexi...
**Claim:** Choose v0 for beautiful designs by default, Bolt for quick prototypes with flexible designs, Replit for internal tools or products that store or transform data, and Lovable for building production apps that benefit from integrations.
**Audience:** general | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Summary of tool recommendations for different use cases.

## Insight 10: GitHub Copilot works best with very specific direction and does not perform as w...
**Claim:** GitHub Copilot works best with very specific direction and does not perform as well as Cursor at more general instructions; Copilot may re-create existing components while Cursor modifies existing files.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Comparison of GitHub Copilot and Cursor for local developer assistants.

## Insight 11: When prompting AI tools for subsequent changes, be hyperspecific to help the AI ...
**Claim:** When prompting AI tools for subsequent changes, be hyperspecific to help the AI pinpoint what should change.
**Audience:** general | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Building a price filter feature in Bolt for an Airbnb prototype.

## Insight 12: Reflection (forcing the AI to build a plan first before writing code) is the mos...
**Claim:** Reflection (forcing the AI to build a plan first before writing code) is the most important strategy for getting useful outputs from AI coding tools.
**Framework:** Reflection
**Audience:** general | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Section on solving prototyping problems without knowing how to code.

## Insight 13: AI prototyping tools can convert a design to a functional prototype in about 10 ...
**Claim:** AI prototyping tools can convert a design to a functional prototype in about 10 minutes, and build a prototype from scratch in less than five minutes.
**Audience:** operator | **Actionability:** 10/10 | **Confidence:** 0.9
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Examples of building an Airbnb prototype and a CRM prototype.

## Insight 14: Use prompt templates for common tasks: for converting Figma designs use Bolt, fo...
**Claim:** Use prompt templates for common tasks: for converting Figma designs use Bolt, for good UI defaults use v0, for data dashboards use Replit with Python/Streamlit, for hand-drawn mockups use v0, for PRD to prototype use Bolt, for personalized tools use Replit.
**Audience:** general | **Actionability:** 10/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Common use cases and prompt templates section.

## Insight 15: Reflection is the most important strategy for getting useful outputs from AI cod...
**Claim:** Reflection is the most important strategy for getting useful outputs from AI coding tools. Force the AI to build a plan first vs. going straight to code.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Discussion of reflection strategy for AI prototyping

## Insight 16: Batching: build the smallest iteration of something functional and then extend i...
**Claim:** Batching: build the smallest iteration of something functional and then extend it. Start with the data model first.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Discussion of batching strategy for AI prototyping

## Insight 17: Be specific with AI, just like with a junior engineer. Specify technologies, par...
**Claim:** Be specific with AI, just like with a junior engineer. Specify technologies, parts of product, files, or lines of code.
**Audience:** engineer | **Actionability:** 9/10 | **Confidence:** 0.95
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Discussion of being specific strategy for AI prototyping

## Insight 18: To avoid losing context, use reflection to determine what files need to change, ...
**Claim:** To avoid losing context, use reflection to determine what files need to change, batching to limit changes, and being specific to minimize incorrect results.
**Audience:** engineer | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Discussion of lost context and how to avoid it

## Insight 19: Most AI prototyping tools have a checkpoint system to roll back to prior version...
**Claim:** Most AI prototyping tools have a checkpoint system to roll back to prior versions when the AI rewrites sections.
**Audience:** general | **Actionability:** 8/10 | **Confidence:** 0.9
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Discussion of lost context and checkpoint systems

## Insight 20: Use cloud development environments: v0 for beautiful designs, Bolt for quick pro...
**Claim:** Use cloud development environments: v0 for beautiful designs, Bolt for quick prototypes, Replit for internal tools, Lovable for production apps.
**Audience:** founder | **Actionability:** 8/10 | **Confidence:** 0.85
**Source:** a-guide-to-ai-prototyping-for-product-managers
**Context:** Recommendation of specific AI prototyping tools
