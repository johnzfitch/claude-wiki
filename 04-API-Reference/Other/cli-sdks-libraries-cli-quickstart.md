---
title: "CLI quickstart - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:29Z"
tags: ["api", "authentication", "cli"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Fcli%2Fquickstart)

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

[CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)ant CLI

# CLI quickstart

Copy page



Install the ant command-line tool, authenticate, and send your first request to the Claude API.

Copy page



The `ant` CLI provides access to the Claude API from your terminal. Every API resource is exposed as a subcommand, with output formatting, response filtering, and YAML or JSON file input.

Compared to `curl`, `ant` builds request bodies from typed flags or piped YAML instead of hand-written JSON, and inlines file contents into string fields with an `@path` reference. It extracts response fields with a built-in `--transform` query, so you don't need a separate tool such as `jq`, and it paginates list endpoints automatically.



For endpoint-specific parameters and response schemas, see the [API reference](../Endpoints/cli-messages-create.md). This page gets you to a working command. For everything else the CLI does, see [Using the CLI](cli-sdks-libraries-cli-using.md) and [CLI scripting and automation](cli-sdks-libraries-cli-scripting.md).

## Installation

Homebrew (macOS)

curl (Linux/WSL)

Go

```python
brew install anthropics/tap/ant
```



Check the installation:

```python
ant --version
```



## Authentication

`ant auth login` opens a browser-based OAuth flow against the Claude Console and stores the resulting credentials locally, so you can call the API without creating or managing an API key.

CLI



```python
ant auth login
```



For other ways to authenticate (API key environment variable, headless hosts, multiple workspaces, named profiles, and Workload Identity Federation), see [CLI authentication options](cli-sdks-libraries-cli-authentication.md).

## Send your first request

With the binary installed and authenticated, call the [Messages API](../Endpoints/cli-messages-create.md):

```python
ant messages create \
  --model claude-opus-5-5 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}'
```



Output



```python
{
  "model": "claude-opus-5-5",
  "id": "msg_01YMmR5XodC5nTqMxLZMKaq6",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello! How are you doing today? Is there something I can help you with?"
    }
  ],
  "stop_reason": "end_turn",
  "usage": { "input_tokens": 27, "output_tokens": 20 /*, ... */ }
}
```

The response is the full API object, pretty-printed because stdout is a terminal.

## Shell completion

The CLI ships completion scripts for bash, zsh, fish, and PowerShell. Generate and install one for your shell:

zsh

bash

fish

PowerShell

```python
ant @completion zsh > "${fpath[1]}/_ant"
# Restart your shell or run: autoload -U compinit && compinit
```



## Next steps



[CLI authentication options](cli-sdks-libraries-cli-authentication.md)

API keys, headless hosts, multiple workspaces, and named profiles



[Using the CLI](cli-sdks-libraries-cli-using.md)

Command structure, output formats, GJSON transforms, and request bodies



[CLI scripting and automation](cli-sdks-libraries-cli-scripting.md)

Version-control API resources, scripting patterns, and use from Claude Code
