---
title: "Claude Code on the web | Claude by Anthropic"
source_url: "https://www.claude.com/blog/claude-code-on-the-web"
category: "02-Claude-Code-CLI"
fetched_at: "2026-11-18T06:26:42Z"
tags: ["claude-code", "security"]
---

# Claude Code on the web

- 

  Category[Product updates](https://www.claude.com/resources/product-updates)
- 

  ProductClaude Code
- 

  DateOctober 20, 2025
- 

  Reading time4 min
- 


Contents

1.  [Run coding tasks in parallel](#run-coding-tasks-in-parallel)
2.  [Flexible for every workflow](#flexible-for-every-workflow)
3.  [Security-first cloud execution](#security-first-cloud-execution)
4.  [Getting started](#getting-started)

***Update:** Cloud sessions (previously known as Claude Code on the web) are now generally available for Pro, Max, Ultra, and Team users, and for Enterprise users with premium seats or Chat + Claude Code seats. Read the [docs](claude-code-on-the-web.md) for the latest information, or our [field guide to cloud sessions](https://claude.dev/blog/claude-code-in-the-cloud/). September 23, 2026.*

Today, we're introducing Claude Code on the web, a new way to delegate coding tasks directly from your browser.

Now in beta as a research preview, you can assign multiple coding tasks to Claude that run on Anthropic-managed cloud infrastructure, perfect for tackling bug backlogs, routine fixes, or [parallel development work](https://claude.com/resources/articles/claude-code-desktop-redesign).

## Run coding tasks in parallel

Claude Code on the web lets you kick off coding sessions without opening your terminal. Connect your GitHub repositories, describe what you need, and Claude handles the implementation.

Each session runs in its own isolated environment with real-time progress tracking, and you can actively steer Claude to adjust course as it’s working through tasks.

With Claude Code running in the cloud, you can now **run multiple tasks in parallel** across different repositories from a single interface and **ship faster** with automatic PR creation and clear change summaries.

## Flexible for every workflow

The web interface complements your existing Claude Code workflow. Running tasks in the cloud is especially effective for:

- Answering questions about how projects work and how repositories are mapped
- Bugfixes and routine, well-defined tasks
- Backend changes, where Claude Code can use test-driven development to verify changes

You can also use Claude Code on mobile. As part of this research preview, we’re making Claude Code available on our iOS app so developers can explore coding with Claude on the go. It’s an early preview, and we hope to quickly refine the mobile experience based on your feedback.  

## Security-first cloud execution

Every Claude Code task runs in an isolated sandbox environment with network and filesystem restrictions. Git interactions are handled through a secure proxy service that ensures Claude can only access authorized repositories—helping keep your code and credentials protected throughout the entire workflow.

You can also add custom network configuration to choose what domains Claude Code can connect to from its sandbox. For example, you can allow Claude to download npm packages over the internet so that it can run tests and validate changes.

Read our [engineering blog](https://www.anthropic.com/engineering/claude-code-sandboxing) and [documentation](https://docs.claude.com/en/docs/claude-code/sandboxing) for a deep dive on Claude Code’s sandboxing approach.

## Getting started

Claude Code on the web is available now in research preview for Pro and Max users. Visit [claude.com/code](https://claude.ai/code) to connect your first repository and start delegating tasks.

Cloud-based sessions share rate limits with all other Claude Code usage. [Explore our documentation](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web) to learn more.

## Related articles

Explore more product news and best practices for teams building with Claude.


ArticleNov 17, 2026

### Linked billing on the Claude Platform

Claude Platform


ArticleNov 12, 2026

### Operate Claude Managed Agents inside your security perimeter

Introducing self-hosted Claude Managed Agents. Now you can run agents in your own environment, whether that’s in your own cloud or on-premise. You host the agents, credentials, and session history, and choose where requests to Claude are sent.

Claude PlatformClaude Managed Agents


ArticleNov 12, 2026

### Introducing Claude for Manufacturing

A new plugin with 17 skills and four connectors helps manufacturers draft quotes, quality reports, and supplier requests from the systems they already run.


ArticleNov 12, 2026

### Introducing Claude Meetings

Add Claude to your video call and get the work started while you talk
