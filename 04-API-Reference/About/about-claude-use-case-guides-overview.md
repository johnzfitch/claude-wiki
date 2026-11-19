---
title: "Guides to common use cases - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/use-case-guides/overview"
category: "04-API-Reference/About"
fetched_at: "2026-11-13T06:32:58Z"
tags: ["api"]
---

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
