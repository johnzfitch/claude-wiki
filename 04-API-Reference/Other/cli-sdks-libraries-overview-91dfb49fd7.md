---
title: "CLI, SDKs, and libraries - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/overview"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:40Z"
tags: ["agents", "api", "claude-code", "cli", "sdk"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Foverview)





SearchCtrlK

CLI, SDKs, and libraries

[Overview](/docs/en/cli-sdks-libraries/overview)

ant CLI

[Quickstart](/docs/en/cli-sdks-libraries/cli/quickstart)[Authentication options](/docs/en/cli-sdks-libraries/cli/authentication)[Using the CLI](/docs/en/cli-sdks-libraries/cli/using)[Scripting and automation](/docs/en/cli-sdks-libraries/cli/scripting)[Manage resources as code](/docs/en/cli-sdks-libraries/cli/apply)[Connect to a Managed Agents session](/docs/en/cli-sdks-libraries/cli/sessions-connect)

Client SDKs

[Middleware](/docs/en/cli-sdks-libraries/middleware)[Python](/docs/en/cli-sdks-libraries/sdks/python)[TypeScript](/docs/en/cli-sdks-libraries/sdks/typescript)[C#](/docs/en/cli-sdks-libraries/sdks/csharp)[Go](/docs/en/cli-sdks-libraries/sdks/go)[Java](/docs/en/cli-sdks-libraries/sdks/java)[PHP](/docs/en/cli-sdks-libraries/sdks/php)[Ruby](/docs/en/cli-sdks-libraries/sdks/ruby)

Libraries and integrations

[Apple Foundation Models](/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)[OpenAI SDK compatibility](/docs/en/cli-sdks-libraries/libraries/openai-sdk)

[Console](/)

CLI, SDKs, and libraries

# CLI, SDKs, and libraries

Copy page



Official tools for building with the Claude API: the ant CLI, client SDKs in seven languages, and framework-specific libraries.

Copy page



Anthropic provides three kinds of official tooling for building with the Claude API:

- **CLI:** The `ant` command-line tool for shell scripting and interactive use.
- **Client SDKs:** General-purpose Messages API clients for Python, TypeScript, C#, Go, Java, PHP, and Ruby. Each SDK provides idiomatic interfaces, type safety, and built-in support for streaming, retries, and error handling.
- **Libraries and integrations:** Packages and compatibility layers that expose Claude inside another framework's API surface rather than the Messages API directly.



For the full API specification, see the [API reference](/docs/en/api/overview).

## CLI

[ant CLI](/docs/en/cli-sdks-libraries/cli/quickstart)

Shell scripting, typed flags, response transforms

## Client SDKs

[Python](/docs/en/cli-sdks-libraries/sdks/python)

Sync and async clients, Pydantic models

[TypeScript](/docs/en/cli-sdks-libraries/sdks/typescript)

Node.js, Deno, Bun, and browser support

[C#](/docs/en/cli-sdks-libraries/sdks/csharp)

.NET Standard 2.0+, IChatClient integration

[Go](/docs/en/cli-sdks-libraries/sdks/go)

Context-based cancellation, functional options

[Java](/docs/en/cli-sdks-libraries/sdks/java)

Builder pattern, CompletableFuture async

[PHP](/docs/en/cli-sdks-libraries/sdks/php)

Value objects, builder pattern

[Ruby](/docs/en/cli-sdks-libraries/sdks/ruby)

Sorbet types, streaming helpers

## Libraries and integrations

Libraries and integrations expose Claude through another framework's API surface. They are not general-purpose Messages API clients.

[Apple Foundation Models](/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)

Swift package for Apple's `LanguageModelSession` API

[OpenAI SDK compatibility](/docs/en/cli-sdks-libraries/libraries/openai-sdk)

Use Claude through the OpenAI SDK surface

## Building agents or using Claude Code?

The CLI, client SDKs, and libraries are for calling the Claude API yourself: you send each request and handle each response. Claude Code, the Claude Agent SDK, and Claude Managed Agents work at a higher level, providing the agent loop, tool execution, and runtime.

[Claude Code](https://code.claude.com/docs/en/overview)

Agentic coding tool for delegating coding tasks to Claude

[Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)

Build agents that run in a process you operate

[Claude Managed Agents](/docs/en/managed-agents/overview)

Run agents in Anthropic's managed infrastructure
