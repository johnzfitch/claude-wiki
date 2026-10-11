---
title: "Claude Code on the web | Claude by Anthropic"
source_url: "https://www.claude.com/blog/claude-code-on-the-web"
category: "02-Claude-Code-CLI"
fetched_at: "2026-10-10T06:27:28Z"
tags: ["claude-code", "security"]
---

# Claude Code on the web

- 

  Category[Announcements](https://www.claude.com/resources/product-announcements)
- 

  ProductClaude Code
- 

  DateOctober 20, 2025
- 

  Reading time4 min
- 


***Update:** Cloud sessions (previously known as Claude Code on the web) are now generally available for Pro, Max, and Team users, and for Enterprise users with premium seats or Chat + Claude Code seats. Read the [docs](claude-code-on-the-web.md) for the latest information. September 23, 2026.*

Today, we're introducing Claude Code on the web, a new way to delegate coding tasks directly from your browser.

Now in beta as a research preview, you can assign multiple coding tasks to Claude that run on Anthropic-managed cloud infrastructure, perfect for tackling bug backlogs, routine fixes, or parallel development work.

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

Claude Code on the web is available now in research preview for Pro and Max users. Visit [claude.com/code](http://claude.com/code) to connect your first repository and start delegating tasks.

Cloud-based sessions share rate limits with all other Claude Code usage. [Explore our documentation](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web) to learn more.

## Related articles

Explore more product news and best practices for teams building with Claude.


ArticleOct 8, 2026

### Build live dashboards and animate explainers with Claude 

Claude Dashboards and Claude Motion are now in beta. Docs, Slides, and Design are out of beta and on every Claude plan, including Free.

Claude appsClaude Design

2 more: Claude Cowork and Claude CodeClaude CoworkClaude Code


ArticleOct 7, 2026

### Claude Haiku 5.5

Introducing Claude Haiku 5.5: the cheapest, fastest, and most capable small model we’ve ever released.

(opens in new tab)[](https://www.claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides)

ArticleOct 6, 2026

### Claude now works with Google Docs, Sheets, and Slides

Teams that run on Google Workspace can now bring Claude into their files or work on their files directly from Claude, with our new add-on and Google Docs, Sheets, and Slides connectors (in beta).

Claude Enterprise


ArticleOct 6, 2026

### We’re expanding the Claude Startups program to help founders build
