---
title: "SDKs, CLI, and libraries - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/overview"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:36:34Z"
tags: ["agents", "api", "claude-code", "cli", "sdk"]
---

# SDKs, CLI, and libraries

Copy page



Official tools for building with the Claude API: client SDKs in seven languages, the ant CLI, and framework-specific libraries.

Copy page



Anthropic provides three kinds of official tooling for building with the Claude API:

- **CLI:** The `ant` command-line tool for shell scripting and interactive use.
- **Client SDKs:** General-purpose Messages API clients for Python, TypeScript, C#, Go, Java, PHP, and Ruby. Each SDK provides idiomatic interfaces, type safety, and built-in support for streaming, retries, error handling, and [OpenTelemetry tracing](manage-claude-opentelemetry-sdk.md).
- **Libraries and integrations:** Packages and compatibility layers that expose Claude inside another framework’s API surface rather than the Messages API directly.

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

Each major version of a client SDK sends one [API version](../Endpoints/versioning.md) by default, and a new major version comes with each new API version. To move to `2026-10-21`, see [Switch to 2026-10-21](../Endpoints/migration-2026-10-21.md#upgrade).

## Latest versions

| Tool | Latest version | Package |
|----|----|----|
| ant CLI | `2.6.0` | [`github.com/anthropics/anthropic-cli`](https://github.com/anthropics/anthropic-cli/releases) |
| Python | `2.5.0` | [`anthropic` on PyPI](https://pypi.org/project/anthropic/) |
| TypeScript | `1.5.0` | [`@anthropic-ai/sdk`](https://www.npmjs.com/package/@anthropic-ai/sdk) |
| C# | `13.5.0` | [`Anthropic`](https://www.nuget.org/packages/Anthropic) |
| Go | `2.6.0` | [`github.com/anthropics/anthropic-sdk-go/v2`](https://pkg.go.dev/github.com/anthropics/anthropic-sdk-go/v2) |
| Java | `3.5.0` | [`com.anthropic:anthropic-java`](https://central.sonatype.com/artifact/com.anthropic/anthropic-java) |
| PHP | `1.5.0` | [`anthropic-ai/sdk`](https://packagist.org/packages/anthropic-ai/sdk) |
| Ruby | `2.5.0` | [`anthropic` on RubyGems](https://rubygems.org/gems/anthropic) |

The same versions are available as JSON at `https://platform.claude.com/docs/sdk-versions.json`.

## Libraries and integrations

Libraries and integrations expose Claude through another framework’s API surface. They are not general-purpose Messages API clients.

[Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md)

Swift package for Apple’s `LanguageModelSession` API

[OpenAI SDK compatibility](cli-sdks-libraries-libraries-openai-sdk.md)

Use Claude through the OpenAI SDK surface

## Building agents or using Claude Code?

The CLI, client SDKs, and libraries are for calling the Claude API yourself: you send each request and handle each response. Claude Code, the Claude Agent SDK, and Claude Managed Agents work at a higher level, providing the agent loop, tool execution, and runtime.

[Claude Code](../../01-Getting-Started/overview.md)

Agentic coding tool for delegating coding tasks to Claude

[Claude Agent SDK](../../05-Agent-SDK/agent-sdk-overview.md)

Build agents that run in a process you operate

[Claude Managed Agents](managed-agents-overview.md)

Run agents in Anthropic’s managed infrastructure
