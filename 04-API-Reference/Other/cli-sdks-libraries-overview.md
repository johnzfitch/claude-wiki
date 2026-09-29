---
title: "CLI, SDKs, and libraries - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/overview"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:40Z"
tags: ["agents", "api", "claude-code", "cli", "sdk"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Foverview)





SearchCtrlK

CLI, SDKs, and libraries

[Overview](cli-sdks-libraries-overview.md)

ant CLI

[Quickstart](cli-sdks-libraries-cli-quickstart.md)[Authentication options](cli-sdks-libraries-cli-authentication.md)[Using the CLI](cli-sdks-libraries-cli-using.md)[Scripting and automation](cli-sdks-libraries-cli-scripting.md)[Manage resources as code](cli-sdks-libraries-cli-apply.md)[Connect to a Managed Agents session](cli-sdks-libraries-cli-sessions-connect.md)

Client SDKs

[Middleware](cli-sdks-libraries-middleware.md)[Python](cli-sdks-libraries-sdks-python.md)[TypeScript](cli-sdks-libraries-sdks-typescript.md)[C#](cli-sdks-libraries-sdks-csharp.md)[Go](cli-sdks-libraries-sdks-go.md)[Java](cli-sdks-libraries-sdks-java.md)[PHP](cli-sdks-libraries-sdks-php.md)[Ruby](cli-sdks-libraries-sdks-ruby.md)

Libraries and integrations

[Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md)[OpenAI SDK compatibility](cli-sdks-libraries-libraries-openai-sdk.md)

[Console](usage-limits.md)

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

For the full API specification, see the [API reference](../Endpoints/overview.md).

## CLI

[ant CLI](cli-sdks-libraries-cli-quickstart.md)

Shell scripting, typed flags, response transforms

## Client SDKs

[Python](cli-sdks-libraries-sdks-python.md)

Sync and async clients, Pydantic models

[TypeScript](cli-sdks-libraries-sdks-typescript.md)

Node.js, Deno, Bun, and browser support

[C#](cli-sdks-libraries-sdks-csharp.md)

.NET Standard 2.0+, IChatClient integration

[Go](cli-sdks-libraries-sdks-go.md)

Context-based cancellation, functional options

[Java](cli-sdks-libraries-sdks-java.md)

Builder pattern, CompletableFuture async

[PHP](cli-sdks-libraries-sdks-php.md)

Value objects, builder pattern

[Ruby](cli-sdks-libraries-sdks-ruby.md)

Sorbet types, streaming helpers

## Libraries and integrations

Libraries and integrations expose Claude through another framework's API surface. They are not general-purpose Messages API clients.

[Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md)

Swift package for Apple's `LanguageModelSession` API

[OpenAI SDK compatibility](cli-sdks-libraries-libraries-openai-sdk.md)

Use Claude through the OpenAI SDK surface

## Building agents or using Claude Code?

The CLI, client SDKs, and libraries are for calling the Claude API yourself: you send each request and handle each response. Claude Code, the Claude Agent SDK, and Claude Managed Agents work at a higher level, providing the agent loop, tool execution, and runtime.

[Claude Code](../../02-Claude-Code-CLI/code-home.md)

Agentic coding tool for delegating coding tasks to Claude

[Claude Agent SDK](../../05-Agent-SDK/agent-sdk-overview.md)

Build agents that run in a process you operate

[Claude Managed Agents](managed-agents-overview.md)

Run agents in Anthropic's managed infrastructure
