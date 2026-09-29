---
title: "Week 26 · June 22–26, 2026 - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w26"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-04T06:29:54Z"
tags: ["claude-code"]
---

# Week 26 · June 22–26, 2026

Copy pageCopy page

Authenticate MCP servers from your shell with claude mcp login, get a response to shell mode command output with the ! prefix, and resume a conversation from before /clear with /rewind.

Copy pageCopy page

Releases [v2.1.185 → v2.1.193](changelog.md#2-1-185)2 features · June 22–26

Authenticate MCP servers from the CLIv2.1.186

New `claude mcp login <name>` and `claude mcp logout <name>` commands authenticate a configured MCP server from your shell instead of the interactive `/mcp` menu. `claude mcp login` runs the server’s OAuth flow directly, and `claude mcp logout` clears the stored credentials.

Run the OAuth flow for a configured server without opening a session:

terminal

```python
claude mcp login sentry
```

[Authenticate from the command line](../06-MCP-Tools/General/mcp.md#authenticate-from-the-command-line)

Shell mode responds to command outputv2.1.186

Commands you run with the `!` prefix now get a response from Claude once the output lands in the transcript, so you can run `! npm test` and get an explanation of the failures without a second prompt. The response costs the same as sending a normal prompt. To keep the earlier behavior, where the output is added to context without a response, set `respondToBashCommands` to `false` in `settings.json`.

Run a command and get a response to its output:

Claude Code

```python
> ! npm test
```

[Shell mode with the ! prefix](interactive-mode.md#shell-mode-with-prefix)

Other wins

`/rewind` can now resume a conversation from before `/clear` was run

New `sandbox.credentials` setting blocks sandboxed commands from reading credential files and secret environment variables

Org-configured model restrictions now apply to the model picker, `--model`, `/model`, and `ANTHROPIC_MODEL`, with a “restricted by your organization’s settings” message when a restricted model is selected

New `autoMode.classifyAllShell` setting routes all Bash and PowerShell commands through the auto-mode classifier, and denial reasons now show in the transcript, the denial toast, and `/permissions`

New `claude_code.assistant_response` OpenTelemetry log event carries the model’s response text; deployments that already log prompt content start receiving it on upgrade, so set `OTEL_LOG_ASSISTANT_RESPONSES=0` to keep prompts only

Background subagents now surface permission prompts in the main session instead of auto-denying; the dialog shows which agent is asking, and Esc denies only that tool

`/install-github-app` can now install only the GitHub App and skip the Actions workflow and secret steps

Hosts you allow in the sandbox network permission dialog are remembered for the rest of the session instead of re-prompting on every connection

Streaming responses use about 37% less CPU, and long-session memory growth from the terminal output cache is reduced

`/review <pr>` now uses the same review engine as `/code-review medium`

Bash mode `!` commands get live file path autocomplete

[Full changelog for v2.1.185–v2.1.193 →](changelog.md#2-1-185)
