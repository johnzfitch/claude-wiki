---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:04:51Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview"
title: "Prompt engineering overview - Claude API Docs"
---

Prompt engineering

# Prompt engineering overview

Copy page

Copy page

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/docs/en/build-with-claude/prompt-engineering/extended-thinking-tips).

## 

Before prompt engineering

This guide assumes that you have:

1.  A clear definition of the success criteria for your use case
2.  Some ways to empirically test against those criteria
3.  A first draft prompt you want to improve

If not, we highly suggest you spend time establishing that first. Check out [Define your success criteria](/docs/en/test-and-evaluate/define-success) and [Create strong empirical evaluations](/docs/en/test-and-evaluate/develop-tests) for tips and guidance.

[](/dashboard)

Prompt generator

Don't have a first draft prompt? Try the prompt generator in the Claude Console!

------------------------------------------------------------------------

## 

When to prompt engineer

This guide focuses on success criteria that are controllable through prompt engineering. Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model.

### Prompting vs. finetuning

------------------------------------------------------------------------

## 

How to prompt engineer

The prompt engineering pages in this section have been organized from most broadly effective techniques to more specialized techniques. When troubleshooting performance, we suggest you try these techniques in order, although the actual impact of each technique will depend on your use case.

1.  [Prompt generator](/docs/en/build-with-claude/prompt-engineering/prompt-generator)
2.  [Be clear and direct](/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct)
3.  [Use examples (multishot)](/docs/en/build-with-claude/prompt-engineering/multishot-prompting)
4.  [Let Claude think (chain of thought)](/docs/en/build-with-claude/prompt-engineering/chain-of-thought)
5.  [Use XML tags](/docs/en/build-with-claude/prompt-engineering/use-xml-tags)
6.  [Give Claude a role (system prompts)](/docs/en/build-with-claude/prompt-engineering/system-prompts)
7.  [Chain complex prompts](/docs/en/build-with-claude/prompt-engineering/chain-prompts)
8.  [Long context tips](/docs/en/build-with-claude/prompt-engineering/long-context-tips)

------------------------------------------------------------------------

## 

Prompt engineering tutorial

If you're an interactive learner, you can dive into our interactive tutorials instead!

[](https://github.com/anthropics/prompt-eng-interactive-tutorial)

GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

[](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)

Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

Was this page helpful?

- 

- [Before prompt engineering](#before-prompt-engineering)

- [When to prompt engineer](#when-to-prompt-engineer)

- [How to prompt engineer](#how-to-prompt-engineer)

- [Prompt engineering tutorial](#prompt-engineering-tutorial)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
