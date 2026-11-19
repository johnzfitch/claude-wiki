---
title: "Code Review | Claude by Anthropic"
source_url: "https://www.claude.com/plugins/code-review"
category: "08-Plugins-Skills"
fetched_at: "2026-11-18T06:26:56Z"
tags: ["plugins"]
---

# Code Review

Anthropic verified

Automated code review for pull requests using multiple specialized agents with confidence-based scoring

- 

  Install in
  Claude Code
- 

  Plugin source[View source](https://github.com/anthropics/claude-plugins-official/tree/fd30cee3ecd5a8ee772733c5d20c0f2bae2da2f0/plugins/code-review)
- 

  Installs438,525

Automates pull request code review using multiple specialized agents working in parallel. Five independent reviewers analyze your changes from different angles: CLAUDE.md compliance checking, bug detection, git history context analysis, previous PR comment review, and code comment verification. Each finding is scored on a 0-100 confidence scale, and only high-confidence issues (default threshold: 80) are posted as comments, dramatically reducing false positives and review noise.

The plugin intelligently filters out PRs that don't need review—closed, draft, automated, or already-reviewed pull requests are automatically skipped. Comments include direct GitHub links with full SHA hashes and line number ranges for easy navigation to the exact code in question.

**How to use:** Run `/code-review` on any PR branch to launch the full automated review. The system will analyze your changes, score potential issues, and post actionable feedback directly to GitHub. You can customize the confidence threshold or focus areas (security, performance, accessibility) by editing the command configuration.

## Other plugins

### [Frontend Design](https://www.claude.com/marketplace/plugins/frontend-design)

Anthropic verified

Frontend design skill for UI/UX implementation

### [Superpowers](https://www.claude.com/marketplace/plugins/superpowers)

Anthropic verified

Core skills library for Claude Code: TDD, debugging, collaboration patterns, and proven techniques

### [Context7](https://www.claude.com/marketplace/plugins/context7)

Anthropic verified

Upstash Context7 MCP server for up-to-date documentation lookup. Connects to Context7's hosted remote MCP server (https://mcp.context7.com/mcp) — no local Node.js or npx required — to pull version-specific documentation and code examples directly from source repositories into your LLM context. Authenticate with Context7 when prompted.

### [Code Simplifier](https://www.claude.com/marketplace/plugins/code-simplifier)

Anthropic verified

Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality

### [Playwright](https://www.claude.com/marketplace/plugins/playwright)

Anthropic verified

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click elements, and perform automated browser testing workflows.

### [GitHub](https://www.claude.com/marketplace/plugins/github)

Anthropic verified

Official GitHub MCP server for repository management. Create issues, manage pull requests, review code, search repositories, and interact with GitHub's full API directly from Claude Code.
