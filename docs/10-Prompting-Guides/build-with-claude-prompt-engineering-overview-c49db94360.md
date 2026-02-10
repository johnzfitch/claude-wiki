---
category: "10-Prompting-Guides"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview"
---


Prompt engineering
Prompt engineering overview
Copy page

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models here.

Before prompt engineering

This guide assumes that you have:

A clear definition of the success criteria for your use case
Some ways to empirically test against those criteria
A first draft prompt you want to improve

If not, we highly suggest you spend time establishing that first. Check out Define your success criteria and Create strong empirical evaluations for tips and guidance.

Prompt generator

Don't have a first draft prompt? Try the prompt generator in the Claude Console!

When to prompt engineer

This guide focuses on success criteria that are controllable through prompt engineering. Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model.

Prompting vs. finetuning
How to prompt engineer

The prompt engineering pages in this section have been organized from most broadly effective techniques to more specialized techniques. When troubleshooting performance, we suggest you try these techniques in order, although the actual impact of each technique will depend on your use case.

Prompt generator
Be clear and direct
Use examples (multishot)
Let Claude think (chain of thought)
Use XML tags
Give Claude a role (system prompts)
Prefill Claude's response
Chain complex prompts
Long context tips
Prompt engineering tutorial

If you're an interactive learner, you can dive into our interactive tutorials instead!

GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

Was this page helpful?