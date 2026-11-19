---
title: "Context7 | Claude by Anthropic"
source_url: "https://www.claude.com/plugins/context7"
category: "08-Plugins-Skills"
fetched_at: "2026-11-18T06:26:44Z"
tags: ["plugins"]
---

# Context7

Anthropic verified

Upstash Context7 MCP server for up-to-date documentation lookup. Connects to Context7's hosted remote MCP server (https://mcp.context7.com/mcp) — no local Node.js or npx required — to pull version-specific documentation and code examples directly from source repositories into your LLM context. Authenticate with Context7 when prompted.

- 

  Install in
  Claude Code
- 

  Plugin source[View source](https://github.com/anthropics/claude-plugins-official/tree/fd30cee3ecd5a8ee772733c5d20c0f2bae2da2f0/external_plugins/context7)
- 

  Installs417,801

Context7 is an MCP server that delivers up-to-date, version-specific documentation and code examples directly into your prompts. It solves a common problem with LLMs: outdated training data leading to hallucinated APIs and deprecated code patterns. Instead of relying on stale information, Context7 pulls current documentation straight from source repositories.

The plugin provides two main tools: **resolve-library-id** for matching library names to Context7-compatible identifiers, and **query-docs** for retrieving documentation for specific libraries. You can even target specific versions by mentioning them in your prompt.

**How to use:** Simply add "use context7" to any prompt where you need current documentation. For example: "Create a Next.js middleware that checks for a valid JWT in cookies. use context7" or "Configure a Cloudflare Worker script to cache JSON API responses. use context7". You can also specify exact libraries with "use library /supabase/supabase for API and docs".

## Other plugins

### [Frontend Design](https://www.claude.com/marketplace/plugins/frontend-design)

Anthropic verified

Frontend design skill for UI/UX implementation

### [Superpowers](https://www.claude.com/marketplace/plugins/superpowers)

Anthropic verified

Core skills library for Claude Code: TDD, debugging, collaboration patterns, and proven techniques

### [Code Review](https://www.claude.com/marketplace/plugins/code-review)

Anthropic verified

Automated code review for pull requests using multiple specialized agents with confidence-based scoring

### [Code Simplifier](https://www.claude.com/marketplace/plugins/code-simplifier)

Anthropic verified

Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality

### [Playwright](https://www.claude.com/marketplace/plugins/playwright)

Anthropic verified

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click elements, and perform automated browser testing workflows.

### [GitHub](https://www.claude.com/marketplace/plugins/github)

Anthropic verified

Official GitHub MCP server for repository management. Create issues, manage pull requests, review code, search repositories, and interact with GitHub's full API directly from Claude Code.
