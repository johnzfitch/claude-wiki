---
title: "CLI, SDKs, and libraries - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/overview"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:37Z"
tags: ["api", "cli", "sdk"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


CLI, SDKs, and libraries

[Overview](/docs/en/cli-sdks-libraries/overview)

ant CLI

[Quickstart](/docs/en/cli-sdks-libraries/cli/quickstart)[Authentication options](/docs/en/cli-sdks-libraries/cli/authentication)[Using the CLI](/docs/en/cli-sdks-libraries/cli/using)[Scripting and automation](/docs/en/cli-sdks-libraries/cli/scripting)

Client SDKs

[Middleware](/docs/en/cli-sdks-libraries/middleware)[Python](/docs/en/cli-sdks-libraries/sdks/python)[TypeScript](/docs/en/cli-sdks-libraries/sdks/typescript)[C#](/docs/en/cli-sdks-libraries/sdks/csharp)[Go](/docs/en/cli-sdks-libraries/sdks/go)[Java](/docs/en/cli-sdks-libraries/sdks/java)[PHP](/docs/en/cli-sdks-libraries/sdks/php)[Ruby](/docs/en/cli-sdks-libraries/sdks/ruby)

Libraries and integrations

[Apple Foundation Models](/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)[OpenAI SDK compatibility](/docs/en/cli-sdks-libraries/libraries/openai-sdk)

[](/login)




CLI, SDKs, and libraries

Overview

CLI, SDKs, and libraries

# CLI, SDKs, and libraries




Official tools for building with the Claude API: the ant CLI, client SDKs in seven languages, and framework-specific libraries.




Anthropic provides three kinds of official tooling for building with the Claude API:

- **CLI:** The `ant` command-line tool for shell scripting and interactive use.
- **Client SDKs:** General-purpose Messages API clients for Python, TypeScript, C#, Go, Java, PHP, and Ruby. Each SDK provides idiomatic interfaces, type safety, and built-in support for streaming, retries, and error handling.
- **Libraries and integrations:** Packages and compatibility layers that expose Claude inside another framework's API surface rather than the Messages API directly.



For the full API specification, see the [API reference](/docs/en/api/overview).




CLI


ant CLI

Shell scripting, typed flags, response transforms




Client SDKs


Python

Sync and async clients, Pydantic models


TypeScript

Node.js, Deno, Bun, and browser support


C#

.NET Standard 2.0+, IChatClient integration


Go

Context-based cancellation, functional options


Java

Builder pattern, CompletableFuture async


PHP

Value objects, builder pattern


Ruby

Sorbet types, streaming helpers




Libraries and integrations

Libraries and integrations expose Claude through another framework's API surface. They are not general-purpose Messages API clients.


Apple Foundation Models

Swift package for Apple's `LanguageModelSession` API


OpenAI SDK compatibility

Use Claude through the OpenAI SDK surface




Building agents or using Claude Code?

The CLI, client SDKs, and libraries are for calling the Claude API yourself: you send each request and handle each response. Claude Code, the Claude Agent SDK, and Claude Managed Agents work at a higher level, providing the agent loop, tool execution, and runtime.


Claude Code



Agentic coding tool for delegating coding tasks to Claude


Claude Agent SDK



Build agents that run in a process you operate


Claude Managed Agents

Run agents in Anthropic's managed infrastructure
