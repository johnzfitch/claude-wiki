---
title: "Agent SDK overview - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/agent-sdk/overview"
category: "05-Agent-SDK"
fetched_at: "2026-09-22T06:29:36Z"
tags: ["agents", "claude-code", "sdk"]
---

## On this page

- [Compare the Agent SDK to other Claude tools](#compare-the-agent-sdk-to-other-claude-tools)
- [Capabilities](#capabilities)
- [Get started](#get-started)
- [Changelog](#changelog)
- [Report bugs](#report-bugs)
- [Branding guidelines](#branding-guidelines)
- [License and terms](#license-and-terms)
- [Next steps](#next-steps)

Agent SDK

# Agent SDK overview

Copy pageCopy page

Build production AI agents with Claude Code as a library

Copy pageCopy page

An agent is an application that completes a task by planning its own steps and calling tools that read files, run commands, or edit code. The Agent SDK gives you the same tools, [agent loop](agent-sdk-agent-loop.md), and context management that power Claude Code, programmable in Python and TypeScript.


[​](#compare-the-agent-sdk-to-other-claude-tools)

Compare the Agent SDK to other Claude tools

The Agent SDK, the CLI, the Client SDK, and Managed Agents differ in who runs the agent, what comes built in, and how you reach it. Find the row that matches how you want to build and run yours.

| You want to                                                                                      | Use                                                                               | What you get                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Embed Claude Code’s agent in your own Python or TypeScript application, in a process you operate | **Agent SDK**                                                                     | A library that runs the Claude Code binary, with Claude Code’s [capabilities](#capabilities), such as built-in tools, permissions, sessions, and hooks.                                                                                                                                                                                                                                       |
| Do interactive development or run one-off tasks from a terminal                                  | [**Claude Code CLI**](../02-Claude-Code-CLI/code-home.md)                                          | The terminal interface, built for daily interactive use.                                                                                                                                                                                                                                                                                                                                      |
| Call the Claude API directly from your own code                                                  | [**Client SDK**](../04-API-Reference/Other/cli-sdks-libraries-overview.md) | Direct access to the Claude API from any of the client SDK languages. You write the tool loop yourself, or let the client SDK’s beta [tool runner](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-tool-runner.md) drive it.                                                                                                                                                       |
| Have Anthropic host the agent, configured through the Claude API                                 | [**Managed Agents**](../04-API-Reference/Other/managed-agents-overview.md) | A hosted agent harness that runs the agent loop, with sessions in an Anthropic-managed cloud sandbox or a [self-hosted sandbox](../04-API-Reference/Other/managed-agents-self-hosted-sandboxes.md) on your own infrastructure. Use it from the [SDK for your language](../04-API-Reference/Other/managed-agents-quickstart.md#install-the-sdk), the `ant` CLI, or the REST API. |

To drive the same agent loop from a language other than Python or TypeScript, [run the CLI as a subprocess](../02-Claude-Code-CLI/headless.md) with the `-p` flag and `--output-format json`.


[​](#capabilities)

Capabilities

These Claude Code capabilities are available in the SDK:

| Capability                   | What it does                                                                                 | Learn more                                                                                                                                                                                                                         |
|------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Built-in tools               | Read, write, edit files, run commands, and search the web                                    | [Tools reference](../02-Claude-Code-CLI/tools-reference.md)                                                                                                                                                                                        |
| Hooks                        | Run custom code at key points in the agent lifecycle                                         | [Hooks](agent-sdk-hooks.md)                                                                                                                                                                                                  |
| Subagents                    | Spawn specialized agents for focused subtasks                                                | [Subagents](agent-sdk-subagents.md)                                                                                                                                                                                          |
| MCP                          | Connect external tools and data sources via the Model Context Protocol                       | [MCP](agent-sdk-mcp.md)                                                                                                                                                                                                      |
| Permissions                  | Control which tools run automatically, which need approval                                   | [Permissions](agent-sdk-permissions.md)                                                                                                                                                                                      |
| Sessions                     | Maintain context across exchanges, resume or fork later                                      | [Sessions](agent-sdk-sessions.md)                                                                                                                                                                                            |
| Skills, commands, and memory | Load automatically from your project’s `.claude/` and from `~/.claude/`, same as Claude Code | [Skills](agent-sdk-skills.md), [Commands](agent-sdk-skills.md#commands-in-agent-sdk-sessions), [Memory](agent-sdk-modifying-system-prompts.md), [Configuration loading](agent-sdk-claude-code-features.md) |
| Plugins                      | Package skills, agents, hooks, and MCP servers, and load them by local path                  | [Plugins](agent-sdk-plugins.md)                                                                                                                                                                                              |


[​](#get-started)

Get started

Follow the [Quickstart](agent-sdk-quickstart.md) to install the SDK, set your API key, and build your first agent, one that finds and fixes bugs in existing code.

Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Use the API key authentication methods described in the [Quickstart](agent-sdk-quickstart.md) instead.


[​](#changelog)

Changelog

View the full changelog for SDK updates, bug fixes, and new features:

- **TypeScript SDK**: [view CHANGELOG.md](https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/CHANGELOG.md)
- **Python SDK**: [view CHANGELOG.md](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md)


[​](#report-bugs)

Report bugs

If you encounter bugs or issues with the Agent SDK:

- **TypeScript SDK**: [report issues on GitHub](https://github.com/anthropics/claude-agent-sdk-typescript/issues)
- **Python SDK**: [report issues on GitHub](https://github.com/anthropics/claude-agent-sdk-python/issues)


[​](#branding-guidelines)

Branding guidelines

For partners integrating the Claude Agent SDK, use of Claude branding is optional. When referencing Claude in your product: **Allowed:**

- “Claude Agent”, preferred for dropdown menus
- “Claude”, when within a menu already labeled “Agents”
- “{YourAgentName} Powered by Claude”, if you have an existing agent name

**Not permitted:**

- “Claude Code” or “Claude Code Agent”
- Claude Code-branded ASCII art or visual elements that mimic Claude Code

Your product should maintain its own branding and not appear to be Claude Code or any Anthropic product. For questions about branding compliance, contact the Anthropic [sales team](https://www.anthropic.com/contact-sales).


[​](#license-and-terms)

License and terms

Use of the Claude Agent SDK is governed by [Anthropic’s Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), including when you use it to power products and services that you make available to your own customers and end users, except to the extent a specific component or dependency is covered by a different license as indicated in that component’s LICENSE file.


[​](#next-steps)

Next steps

These resources cover deeper technical detail and example projects for building with the Agent SDK.

- [Quickstart](agent-sdk-quickstart.md): build your first agent that finds and fixes bugs
- [Migration guide](agent-sdk-migration-guide.md): migrate from the Claude Code SDK packages to the Agent SDK
- [Agent loop](agent-sdk-agent-loop.md): how Claude plans, calls tools, and decides when a task is done
- [Example agents](https://github.com/anthropics/claude-agent-sdk-demos): demo apps for local development
- [TypeScript SDK](agent-sdk-typescript.md): full TypeScript API reference and examples
- [Python SDK](agent-sdk-python.md): full Python API reference and examples
- [Agent harness design](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code): how the Claude Code team uses dynamic workflows to orchestrate many subagents at once
