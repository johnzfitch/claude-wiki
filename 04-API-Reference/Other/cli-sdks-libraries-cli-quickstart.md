---
title: "CLI quickstart - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:36:12Z"
tags: ["api", "authentication", "cli"]
---

# CLI quickstart

Copy page



Install the ant command-line tool, authenticate, and send your first request to the Claude API.

Copy page



The `ant` CLI provides access to the Claude API from your terminal. Every API resource is exposed as a subcommand, with output formatting, response filtering, and YAML or JSON file input.

Compared to `curl`, `ant` builds request bodies from typed flags or piped YAML instead of hand-written JSON, and inlines file contents into string fields with an `@path` reference. It extracts response fields with a built-in `--transform` query, so you don’t need a separate tool such as `jq`, and it paginates list endpoints automatically.



For endpoint-specific parameters and response schemas, see the [API reference](../Endpoints/cli-messages-create.md). This page gets you to a working command. For everything else the CLI does, see [Using the CLI](cli-sdks-libraries-cli-using.md) and [CLI scripting and automation](cli-sdks-libraries-cli-scripting.md).

## Installation

Homebrew (macOS)

curl (Linux/WSL)

go install

Homebrew (macOS)

```python
brew install anthropics/tap/ant
```



curl (Linux/WSL)

For Linux environments, download the release binary directly.

```python
VERSION=2.6.0
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
case $(uname -m) in
  x86_64) ARCH=amd64 ;;
  aarch64) ARCH=arm64 ;;
esac
curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
  | sudo tar -xz -C /usr/local/bin ant
```



You can find all releases on the [GitHub releases page](https://github.com/anthropics/anthropic-cli/releases).

go install

You can also install the CLI from source using `go install`. Requires Go 1.25 or later.

```python
go install github.com/anthropics/anthropic-cli/v2/cmd/ant@latest
```



The binary is placed in `$(go env GOPATH)/bin`. Add it to your `PATH` if it isn’t already:

```python
export PATH="$PATH:$(go env GOPATH)/bin"
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

zsh

```python
ant @completion zsh > "${fpath[1]}/_ant"
# Restart your shell or run: autoload -U compinit && compinit
```



bash

```python
ant @completion bash > /etc/bash_completion.d/ant
```



fish

```python
ant @completion fish > ~/.config/fish/completions/ant.fish
```



PowerShell

```python
ant @completion powershell | Out-String | Invoke-Expression
# To persist across sessions:
# ant @completion powershell >> $PROFILE
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

Version control for API resources, scripting patterns, and use from Claude Code
