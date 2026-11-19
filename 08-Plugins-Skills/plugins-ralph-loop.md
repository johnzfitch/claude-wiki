---
title: "Ralph Loop | Claude by Anthropic"
source_url: "https://www.claude.com/plugins/ralph-loop"
category: "08-Plugins-Skills"
fetched_at: "2026-11-18T06:27:27Z"
tags: ["plugins"]
---

# Ralph Loop

Anthropic verified

Continuous self-referential AI loops for interactive iterative development, implementing the Ralph Wiggum technique. Run Claude in a while-true loop with the same prompt until task completion.

- 

  Install in
  Claude Code
- 

  Plugin source[View source](https://github.com/anthropics/claude-plugins-official/tree/e0ab6e51219eef74e417a0e1d89e5d53e5e763d4/plugins/ralph-loop)
- 

  Installs196,527

Ralph Loop enables iterative, self-referential AI development loops where Claude works on the same task repeatedly until completion. The plugin intercepts session exits via a stop hook and automatically re-feeds your prompt while preserving all file modifications and git history between iterations. This creates autonomous improvement cycles where Claude can refine its work based on test failures and previous attempts.

The technique is ideal for well-defined projects with clear success criteria, greenfield development with automated verification, and any task amenable to iterative refinement. Claude reads its own past work to inform improvements, creating a powerful feedback loop for autonomous problem-solving.

**How to use:** Start an iterative session with `/ralph-loop "your prompt here" --max-iterations 10 --completion-promise "DONE"`. The loop continues until Claude outputs the completion promise or reaches the iteration limit. Cancel anytime with `/cancel-ralph`. Write prompts with explicit completion criteria and success metrics for best results.

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

### [Context7](https://www.claude.com/marketplace/plugins/context7)

Anthropic verified

Upstash Context7 MCP server for up-to-date documentation lookup. Connects to Context7's hosted remote MCP server (https://mcp.context7.com/mcp) — no local Node.js or npx required — to pull version-specific documentation and code examples directly from source repositories into your LLM context. Authenticate with Context7 when prompted.

### [Code Simplifier](https://www.claude.com/marketplace/plugins/code-simplifier)

Anthropic verified

Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality

### [Playwright](https://www.claude.com/marketplace/plugins/playwright)

Anthropic verified

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click elements, and perform automated browser testing workflows.
