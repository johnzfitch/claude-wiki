---
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-26T03:19:52Z"
source_url: "https://code.claude.com/docs/en/cli-reference"
title: "CLI reference - Claude Code Docs"
---

# CLI reference


Complete reference for Claude Code command-line interface, including commands and flags.


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
| `claude install [version]` | Install or reinstall the native binary. Accepts a version like `2.1.118`, or `stable` or `latest`. See [Install a specific version](/docs/en/setup#install-a-specific-version) | `claude install stable` |
| `claude auth login` | Sign in to your Anthropic account. Use `--email` to pre-fill your email address, `--sso` to force SSO authentication, and `--console` to sign in with Anthropic Console for API usage billing instead of a Claude subscription | `claude auth login --console` |
| `claude auth logout` | Log out from your Anthropic account | `claude auth logout` |
| `claude auth status` | Show authentication status as JSON. Use `--text` for human-readable output. Exits with code 0 if logged in, 1 if not | `claude auth status` |
| `claude agents` | List all configured [subagents](/docs/en/sub-agents), grouped by source | `claude agents` |
| `claude auto-mode defaults` | Print the built-in [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) classifier rules as JSON. Use `claude auto-mode config` to see your effective config with settings applied | `claude auto-mode defaults > rules.json` |
| `claude mcp` | Configure Model Context Protocol (MCP) servers | See the [Claude Code MCP documentation](/docs/en/mcp). |
| `claude plugin` | Manage Claude Code [plugins](/docs/en/plugins). Alias: `claude plugins`. See [plugin reference](/docs/en/plugins-reference#cli-commands-reference) for subcommands | `claude plugin install code-review@claude-plugins-official` |
| `claude remote-control` | Start a [Remote Control](/docs/en/remote-control) server to control Claude Code from Claude.ai or the Claude app. Runs in server mode (no local interactive session). See [Server mode flags](/docs/en/remote-control#start-a-remote-control-session) | `claude remote-control --name "My Project"` |
| `claude setup-token` | Generate a long-lived OAuth token for CI and scripts. Prints the token to the terminal without saving it. Requires a Claude subscription. See [Generate a long-lived token](/docs/en/authentication#generate-a-long-lived-token) | `claude setup-token` |

If you mistype a subcommand, Claude Code suggests the closest match and exits without starting a session. For example, `claude udpate` prints `Did you mean claude update?`.


[​](#cli-flags)

CLI flags

Customize Claude Code’s behavior with these command-line flags. `claude --help` does not list every flag, so a flag’s absence from `--help` does not mean it is unavailable.

[TABLE]


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


[​](#see-also)

See also

- [Chrome extension](/docs/en/chrome) - Browser automation and web testing
- [Interactive mode](/docs/en/interactive-mode) - Shortcuts, input modes, and interactive features
- [Quickstart guide](/docs/en/quickstart) - Getting started with Claude Code
- [Common workflows](/docs/en/common-workflows) - Advanced workflows and patterns
- [Settings](/docs/en/settings) - Configuration options
- [Agent SDK documentation](/docs/en/agent-sdk/overview) - Programmatic usage and integrations
