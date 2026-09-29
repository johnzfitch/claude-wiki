---
title: "Guides to common use cases - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/use-case-guides/overview"
category: "04-API-Reference/About"
fetched_at: "2026-09-26T06:38:10Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fabout-claude%2Fuse-case-guides%2Foverview)





SearchCtrlK

Use cases

[Overview](about-claude-use-case-guides-overview.md)[Ticket routing](about-claude-use-case-guides-ticket-routing.md)[Customer support agent](about-claude-use-case-guides-customer-support-chat.md)[Content moderation](about-claude-use-case-guides-content-moderation.md)[Legal summarization](about-claude-use-case-guides-legal-summarization.md)[Commerce agent](about-claude-use-case-guides-commerce-agents.md)

Prompt engineering

[Overview](../../10-Prompting-Guides/build-with-claude-prompt-engineering-overview.md)[Prompting best practices](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md)[Prompting Claude Fable 5.1](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md)[Prompting Claude Fable 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5.md)[Prompting Claude Opus 5.5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md)[Prompting Claude Opus 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md)[Prompting Claude Opus 4.8](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-4-8.md)[Prompting Claude Sonnet 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5.md)

Test and evaluate

[Define success and build evaluations](../Test-Evaluate/test-and-evaluate-develop-tests.md)[Reducing latency](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-reduce-latency.md)

Strengthen guardrails

[Reduce hallucinations](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-reduce-hallucinations.md)[Increase output consistency](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-increase-consistency.md)[Mitigate jailbreaks](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-mitigate-jailbreaks.md)[Reduce prompt leak](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-reduce-prompt-leak.md)

Reference

[Glossary](about-claude-glossary.md)[Additional resources](about-claude-additional-resources.md)

[Console](../Other/usage-limits.md)

Best practicesUse cases

# Guides to common use cases

Copy page



Explore production guides for building common Claude use cases: ticket routing, customer support agents, content moderation, legal summarization, and commerce agents.

Copy page



Claude is designed to excel in a variety of tasks. Explore these in-depth production guides to learn how to build common use cases with Claude.

[Ticket routing](about-claude-use-case-guides-ticket-routing.md)

Best practices for using Claude to classify and route customer support tickets at scale.



[Customer support agent](about-claude-use-case-guides-customer-support-chat.md)

Build intelligent, context-aware chatbots with Claude to enhance customer support interactions.



[Content moderation](about-claude-use-case-guides-content-moderation.md)

Techniques and best practices for using Claude to perform content filtering and general content moderation.



[Legal summarization](about-claude-use-case-guides-legal-summarization.md)

Summarize legal documents using Claude to extract key information and expedite research.



[Commerce agent](about-claude-use-case-guides-commerce-agents.md)

Build shopping and merchant agents from an open-source blueprint that runs on the Messages API, the Claude Agent SDK, and Claude Managed Agents.

## Choosing a build path

The three paths for building with Claude differ in how much control you keep and how much of the implementation you offload to Anthropic. The [Messages API](../Guides/build-with-claude-working-with-messages.md) gives you the most control: you write the agent loop and run your own tools and infrastructure. The [Claude Agent SDK](../../05-Agent-SDK/agent-sdk-overview.md) sits in between, providing the agent loop and tool execution in a process you operate. With [Claude Managed Agents](../Other/managed-agents-overview.md), you offload the most: Anthropic hosts the agent loop, tool execution, and runtime for you.
