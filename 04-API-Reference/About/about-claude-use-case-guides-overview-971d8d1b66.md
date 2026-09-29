---
title: "Guides to common use cases - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/use-case-guides/overview"
category: "04-API-Reference/About"
fetched_at: "2026-09-26T06:38:10Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fabout-claude%2Fuse-case-guides%2Foverview)





SearchCtrlK

Use cases

[Overview](/docs/en/about-claude/use-case-guides/overview)[Ticket routing](/docs/en/about-claude/use-case-guides/ticket-routing)[Customer support agent](/docs/en/about-claude/use-case-guides/customer-support-chat)[Content moderation](/docs/en/about-claude/use-case-guides/content-moderation)[Legal summarization](/docs/en/about-claude/use-case-guides/legal-summarization)[Commerce agent](/docs/en/about-claude/use-case-guides/commerce-agents)

Prompt engineering

[Overview](/docs/en/build-with-claude/prompt-engineering/overview)[Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)[Prompting Claude Fable 5.1](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)[Prompting Claude Fable 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)[Prompting Claude Opus 5.5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)[Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)[Prompting Claude Opus 4.8](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)[Prompting Claude Sonnet 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)

Test and evaluate

[Define success and build evaluations](/docs/en/test-and-evaluate/develop-tests)[Reducing latency](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)

Strengthen guardrails

[Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)[Increase output consistency](/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)[Mitigate jailbreaks](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)[Reduce prompt leak](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)

Reference

[Glossary](/docs/en/about-claude/glossary)[Additional resources](/docs/en/about-claude/additional-resources)

[Console](/)

Best practicesUse cases

# Guides to common use cases

Copy page



Explore production guides for building common Claude use cases: ticket routing, customer support agents, content moderation, legal summarization, and commerce agents.

Copy page



Claude is designed to excel in a variety of tasks. Explore these in-depth production guides to learn how to build common use cases with Claude.

[Ticket routing](/docs/en/about-claude/use-case-guides/ticket-routing)

Best practices for using Claude to classify and route customer support tickets at scale.



[Customer support agent](/docs/en/about-claude/use-case-guides/customer-support-chat)

Build intelligent, context-aware chatbots with Claude to enhance customer support interactions.



[Content moderation](/docs/en/about-claude/use-case-guides/content-moderation)

Techniques and best practices for using Claude to perform content filtering and general content moderation.



[Legal summarization](/docs/en/about-claude/use-case-guides/legal-summarization)

Summarize legal documents using Claude to extract key information and expedite research.



[Commerce agent](/docs/en/about-claude/use-case-guides/commerce-agents)

Build shopping and merchant agents from an open-source blueprint that runs on the Messages API, the Claude Agent SDK, and Claude Managed Agents.

## Choosing a build path

The three paths for building with Claude differ in how much control you keep and how much of the implementation you offload to Anthropic. The [Messages API](/docs/en/build-with-claude/working-with-messages) gives you the most control: you write the agent loop and run your own tools and infrastructure. The [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) sits in between, providing the agent loop and tool execution in a process you operate. With [Claude Managed Agents](/docs/en/managed-agents/overview), you offload the most: Anthropic hosts the agent loop, tool execution, and runtime for you.
