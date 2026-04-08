---
source_url: "https://code.claude.com/docs/en/channels-reference.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
---

# Channels reference

Build an MCP server that pushes webhooks, alerts, and chat messages into a Claude Code session. Reference for the channel contract: capability declaration, notification events, reply tools, sender gating, and permission relay.

> Channels are in research preview and require Claude Code v2.1.80 or later. They require claude.ai login. Console and API key authentication is not supported. Team and Enterprise organizations must explicitly enable them.

A channel is an MCP server that pushes events into a Claude Code session so Claude can react to things happening outside the terminal.

You can build a one-way or two-way channel. One-way channels forward alerts, webhooks, or monitoring events for Claude to act on. Two-way channels also expose a reply tool so Claude can send messages back. A channel with a trusted sender path can also opt in to relay permission prompts so you can approve or deny tool use remotely.

## Overview

A channel is an MCP server that runs on the same machine as Claude Code. Claude Code spawns it as a subprocess and communicates over stdio.

- **Chat platforms** (Telegram, Discord): your plugin runs locally and polls the platform's API for new messages
- **Webhooks** (CI, monitoring): your server listens on a local HTTP port. External systems POST to that port

## What you need

The only hard requirement is the `@modelcontextprotocol/sdk` package and a Node.js-compatible runtime (Bun, Node, or Deno).

Your server needs to:

1. Declare the `claude/channel` capability so Claude Code registers a notification listener
2. Emit `notifications/claude/channel` events when something happens
3. Connect over stdio transport

## Example: build a webhook receiver

```ts
#!/usr/bin/env bun
import { Server } from '@modelcontextprotocol/sdk/server/index.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'

const mcp = new Server(
  { name: 'webhook', version: '0.0.1' },
  {
    capabilities: { experimental: { 'claude/channel': {} } },
    instructions: 'Events from the webhook channel arrive as <channel source="webhook" ...>. Read them and act, no reply expected.',
  },
)

await mcp.connect(new StdioServerTransport())

Bun.serve({
  port: 8788,
  hostname: '127.0.0.1',
  async fetch(req) {
    const body = await req.text()
    await mcp.notification({
      method: 'notifications/claude/channel',
      params: {
        content: body,
        meta: { path: new URL(req.url).pathname, method: req.method },
      },
    })
    return new Response('ok')
  },
})
```

Register in `.mcp.json`:

```json
{
  "mcpServers": {
    "webhook": { "command": "bun", "args": ["./webhook.ts"] }
  }
}
```

Test with the development flag:

```bash
claude --dangerously-load-development-channels server:webhook
```

Then from another terminal:

```bash
curl -X POST localhost:8788 -d "build failed on main: https://ci.example.com/run/1234"
```

## Server options

| Field                                                    | Type     | Description                                                     |
| :------------------------------------------------------- | :------- | :-------------------------------------------------------------- |
| `capabilities.experimental['claude/channel']`            | `object` | Required. Always `{}`. Registers the notification listener.     |
| `capabilities.experimental['claude/channel/permission']` | `object` | Optional. Declares channel can receive permission relay requests.|
| `capabilities.tools`                                     | `object` | Two-way only. Standard MCP tool capability.                     |
| `instructions`                                           | `string` | Added to Claude's system prompt.                                |

## Notification format

| Field     | Type                     | Description                                            |
| :-------- | :----------------------- | :----------------------------------------------------- |
| `content` | `string`                 | The event body, delivered as body of `<channel>` tag.  |
| `meta`    | `Record<string, string>` | Optional. Each entry becomes a tag attribute.          |

## Expose a reply tool

For two-way channels, expose a standard MCP tool:

1. Add `tools: {}` to capabilities
2. Register `ListToolsRequestSchema` and `CallToolRequestSchema` handlers
3. Update `instructions` to tell Claude when to call the tool

## Gate inbound messages

Check the sender against an allowlist before calling `mcp.notification()`:

```ts
const allowed = new Set(loadAllowlist())
if (!allowed.has(message.from.id)) {
  return  // drop silently
}
await mcp.notification({ ... })
```

Gate on the **sender's identity**, not the chat or room identity.

## Relay permission prompts

> Permission relay requires Claude Code v2.1.81 or later.

When Claude calls a tool that needs approval, a two-way channel can receive the same prompt and relay it remotely.

### Permission request fields

| Field           | Description                                              |
| --------------- | -------------------------------------------------------- |
| `request_id`    | Five lowercase letters (a-z without l)                   |
| `tool_name`     | Name of the tool Claude wants to use                     |
| `description`   | Human-readable summary of what the tool call does        |
| `input_preview` | Tool arguments as JSON, truncated to 200 characters      |

The verdict sends `notifications/claude/channel/permission` with `request_id` and `behavior` set to `'allow'` or `'deny'`.

### Add relay to a chat bridge

1. Declare `claude/channel/permission: {}` capability
2. Handle `notifications/claude/channel/permission_request` notifications
3. Check inbound for `yes <id>` / `no <id>` verdict pattern

## Package as a plugin

Wrap in a plugin and publish to a marketplace. Users install with `/plugin install`, then enable per session with `--channels plugin:<name>@<marketplace>`.

## See Also

- [Channels](/en/channels) — Install and use Telegram, Discord, iMessage, or fakechat
- [Working channel implementations](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins)
- [MCP](/en/mcp) — The underlying protocol
- [Plugins](/en/plugins) — Package your channel for installation
