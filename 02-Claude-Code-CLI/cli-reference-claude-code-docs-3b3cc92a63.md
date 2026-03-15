---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-15T04:10:54Z"
source_url: "https://code.claude.com/docs/en/cli-reference"
title: "CLI reference - Claude Code Docs"
---

# CLI reference


Complete reference for Claude Code command-line interface, including commands and flags.


## 

[​](#cli-commands)

CLI commands

You can start sessions, pipe content, resume conversations, and manage updates with these commands:

| Command | Description | Example |
|:---|:---|:---|
| `claude` | Start interactive session | `claude` |
| `claude "query"` | Start interactive session with initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Query via SDK, then exit | `claude -p "explain this function"` |
| `cat file | claude -p "query"` | Process piped content | `cat logs.txt | claude -p "explain"` |
| `claude -c` | Continue most recent conversation in current directory | `claude -c` |
| `claude -c -p "query"` | Continue via SDK | `claude -c -p "Check for type errors"` |
| `claude -r "<session>" "query"` | Resume session by ID or name | `claude -r "auth-refactor" "Finish this PR"` |
| `claude update` | Update to latest version | `claude update` |
| `claude auth login` | Sign in to your Anthropic account. Use `--email` to pre-fill your email address and `--sso` to force SSO authentication | `claude auth login --email `[`[email protected]`](/cdn-cgi/l/email-protection)` --sso` |
| `claude auth logout` | Log out from your Anthropic account | `claude auth logout` |
| `claude auth status` | Show authentication status as JSON. Use `--text` for human-readable output. Exits with code 0 if logged in, 1 if not | `claude auth status` |
| `claude agents` | List all configured [subagents](/docs/en/sub-agents), grouped by source | `claude agents` |
| `claude mcp` | Configure Model Context Protocol (MCP) servers | See the [Claude Code MCP documentation](/docs/en/mcp). |
| `claude remote-control` | Start a [Remote Control](/docs/en/remote-control) server to control Claude Code from Claude.ai or the Claude app. Runs in server mode (no local interactive session). See [Server mode flags](/docs/en/remote-control#server-mode) | `claude remote-control --name "My Project"` |

## 

[​](#cli-flags)

CLI flags

Customize Claude Code’s behavior with these command-line flags:

[TABLE]

### 

[​](#system-prompt-flags)

System prompt flags

Claude Code provides four flags for customizing the system prompt. All four work in both interactive and non-interactive modes.

| Flag | Behavior | Example |
|:---|:---|:---|
| `--system-prompt` | Replaces the entire default prompt | `claude --system-prompt "You are a Python expert"` |
| `--system-prompt-file` | Replaces with file contents | `claude --system-prompt-file ./prompts/review.txt` |
| `--append-system-prompt` | Appends to the default prompt | `claude --append-system-prompt "Always use TypeScript"` |
| `--append-system-prompt-file` | Appends file contents to the default prompt | `claude --append-system-prompt-file ./style-rules.txt` |

`--system-prompt` and `--system-prompt-file` are mutually exclusive. The append flags can be combined with either replacement flag. For most use cases, use an append flag. Appending preserves Claude Code’s built-in capabilities while adding your requirements. Use a replacement flag only when you need complete control over the system prompt.

## 

[​](#see-also)

See also

- [Chrome extension](/docs/en/chrome) - Browser automation and web testing
- [Interactive mode](/docs/en/interactive-mode) - Shortcuts, input modes, and interactive features
- [Quickstart guide](/docs/en/quickstart) - Getting started with Claude Code
- [Common workflows](/docs/en/common-workflows) - Advanced workflows and patterns
- [Settings](/docs/en/settings) - Configuration options
- [Agent SDK documentation](https://platform.claude.com/docs/en/agent-sdk/overview) - Programmatic usage and integrations
