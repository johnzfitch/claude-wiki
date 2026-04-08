---
source_url: "https://code.claude.com/docs/en/remote-control.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
---

# Continue local sessions from any device with Remote Control

Continue a local Claude Code session from your phone, tablet, or any browser using Remote Control. Works with claude.ai/code and the Claude mobile app.

> Remote Control is available on all plans. On Team and Enterprise, it is off by default until an admin enables the Remote Control toggle in Claude Code admin settings.

Remote Control connects claude.ai/code or the Claude app for iOS and Android to a Claude Code session running on your machine. Start a task at your desk, then pick it up from your phone or a browser on another computer.

When you start a Remote Control session on your machine, Claude keeps running locally the entire time, so nothing moves to the cloud.

- **Use your full local environment remotely**: your filesystem, MCP servers, tools, and project configuration all stay available
- **Work from both surfaces at once**: the conversation stays in sync across all connected devices
- **Survive interruptions**: if your laptop sleeps or your network drops, the session reconnects automatically

> Remote Control requires Claude Code v2.1.51 or later.

## Requirements

- **Subscription**: Pro, Max, Team, or Enterprise plans. API keys not supported.
- **Authentication**: run `claude` and use `/login` to sign in through claude.ai
- **Workspace trust**: run `claude` in your project directory at least once

## Start a Remote Control session

### Server mode

```bash
claude remote-control
```

Available flags:

| Flag                                            | Description                                          |
| ----------------------------------------------- | ---------------------------------------------------- |
| `--name "My Project"`                           | Custom session title                                 |
| `--remote-control-session-name-prefix <prefix>` | Prefix for auto-generated names                      |
| `--spawn <mode>`                                | `same-dir` (default) or `worktree` for isolation     |
| `--capacity <N>`                                | Max concurrent sessions (default 32)                 |
| `--verbose`                                     | Show detailed logs                                   |
| `--sandbox` / `--no-sandbox`                    | Enable/disable sandboxing                            |

### Interactive session

```bash
claude --remote-control
```

### From an existing session

```
/remote-control
```

### Connect from another device

- Open the session URL in any browser
- Scan the QR code (press spacebar to show)
- Find the session in claude.ai/code session list

### Enable for all sessions

Run `/config` and set **Enable Remote Control for all sessions** to `true`.

## Connection and security

Your local Claude Code session makes outbound HTTPS requests only and never opens inbound ports. All traffic travels through the Anthropic API over TLS. The connection uses multiple short-lived credentials, each scoped to a single purpose.

## Remote Control vs Claude Code on the web

Remote Control executes on your machine (local MCP servers, tools, and config stay available). Claude Code on the web executes in Anthropic-managed cloud infrastructure.

Use Remote Control for continuing local work from another device. Use Claude Code on the web for tasks without local setup or running multiple tasks in parallel.

## Limitations

- **One remote session per interactive process**: use server mode with `--spawn` for multiple
- **Terminal must stay open**: closing the terminal ends the session
- **Extended network outage**: ~10 minutes without network causes timeout
- **Ultraplan disconnects Remote Control**: both features occupy claude.ai/code interface

## Troubleshooting

- **"Remote Control requires a claude.ai subscription"**: Run `claude auth login`
- **"Requires a full-scope login token"**: Run `claude auth login` instead of using `setup-token`
- **"Unable to determine your organization"**: Run `claude auth login` to refresh
- **"Not yet enabled for your account"**: Unset `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or third-party provider env vars
- **"Disabled by your organization's policy"**: Admin must enable in claude.ai admin settings
- **"Remote credentials fetch failed"**: Re-run with `--verbose` to diagnose

## See Also

- [Claude Code on the web](/en/claude-code-on-the-web)
- [Ultraplan](/en/ultraplan)
- [Channels](/en/channels)
- [Dispatch](/en/desktop#sessions-from-dispatch)
