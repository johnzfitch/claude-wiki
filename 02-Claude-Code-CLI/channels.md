---
source_url: "https://code.claude.com/docs/en/channels.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
---

# Push events into a running session with channels

Use channels to push messages, alerts, and webhooks into your Claude Code session from an MCP server. Forward CI results, chat messages, and monitoring events so Claude can react while you're away.

> Channels are in research preview and require Claude Code v2.1.80 or later. They require claude.ai login. Console and API key authentication is not supported. Team and Enterprise organizations must explicitly enable them.

A channel is an MCP server that pushes events into your running Claude Code session, so Claude can react to things that happen while you're not at the terminal. Channels can be two-way: Claude reads the event and replies back through the same channel, like a chat bridge. Events only arrive while the session is open, so for an always-on setup you run Claude in a background process or persistent terminal.

You install a channel as a plugin and configure it with your own credentials. Telegram, Discord, and iMessage are included in the research preview.

## Supported channels

Each supported channel is a plugin that requires [Bun](https://bun.sh).

### Telegram

1. **Create a Telegram bot**: Open BotFather in Telegram and send `/newbot`. Copy the token.
2. **Install the plugin**: `/plugin install telegram@claude-plugins-official`
3. **Configure your token**: `/telegram:configure <token>`
4. **Restart with channels enabled**: `claude --channels plugin:telegram@claude-plugins-official`
5. **Pair your account**: Send any message to your bot, get the pairing code, run `/telegram:access pair <code>`, then `/telegram:access policy allowlist`

### Discord

1. **Create a Discord bot**: Go to Discord Developer Portal, create application, enable Message Content Intent
2. **Invite the bot**: OAuth2 > URL Generator, select `bot` scope with View Channels, Send Messages, Read Message History permissions
3. **Install the plugin**: `/plugin install discord@claude-plugins-official`
4. **Configure your token**: `/discord:configure <token>`
5. **Restart with channels enabled**: `claude --channels plugin:discord@claude-plugins-official`
6. **Pair your account**: DM your bot, get pairing code, run `/discord:access pair <code>`

### iMessage

The iMessage channel reads your Messages database directly and sends replies through AppleScript. Requires macOS.

1. **Grant Full Disk Access** for your terminal
2. **Install the plugin**: `/plugin install imessage@claude-plugins-official`
3. **Restart with channels enabled**: `claude --channels plugin:imessage@claude-plugins-official`
4. **Text yourself**: Self-chat bypasses access control
5. **Allow other senders**: `/imessage:access allow +15551234567`

You can also build your own channel — see the Channels reference.

## Quickstart with fakechat

Fakechat is a demo channel that runs a chat UI on localhost:

1. Install: `/plugin install fakechat@claude-plugins-official`
2. Restart: `claude --channels plugin:fakechat@claude-plugins-official`
3. Open http://localhost:8787 and type a message

## Security

Every approved channel plugin maintains a sender allowlist: only IDs you've added can push messages, and everyone else is silently dropped.

Telegram and Discord bootstrap the list by pairing. iMessage detects the user's own addresses automatically.

Being in `.mcp.json` isn't enough to push messages: a server also has to be named in `--channels`.

The allowlist also gates permission relay if the channel declares it. Anyone who can reply through the channel can approve or deny tool use in your session.

## Enterprise controls

On Team and Enterprise plans, channels are off by default. Admins control availability through two managed settings:

| Setting                 | Purpose                                                    | When not configured            |
| :---------------------- | :--------------------------------------------------------- | :----------------------------- |
| `channelsEnabled`       | Master switch. Must be `true` for any channel to deliver.  | Channels blocked               |
| `allowedChannelPlugins` | Which plugins can register once channels are enabled.      | Anthropic default list applies |

Pro and Max users without an organization skip these checks entirely.

### Enable channels for your organization

Admins can enable channels from **claude.ai → Admin settings → Claude Code → Channels**, or by setting `channelsEnabled` to `true` in managed settings.

### Restrict which channel plugins can run

```json
{
  "channelsEnabled": true,
  "allowedChannelPlugins": [
    { "marketplace": "claude-plugins-official", "plugin": "telegram" },
    { "marketplace": "claude-plugins-official", "plugin": "discord" },
    { "marketplace": "acme-corp-plugins", "plugin": "internal-alerts" }
  ]
}
```

## How channels compare

| Feature                | What it does                                                    | Good for                                              |
| :--------------------- | :-------------------------------------------------------------- | :---------------------------------------------------- |
| Claude Code on the web | Runs tasks in a fresh cloud sandbox                             | Delegating self-contained async work                  |
| Claude in Slack        | Spawns a web session from an `@Claude` mention                  | Starting tasks from team conversation                 |
| Standard MCP server    | Claude queries it during a task; nothing is pushed              | Giving Claude on-demand access to a system            |
| Remote Control         | You drive your local session from claude.ai or mobile           | Steering in-progress work from another device         |
| **Channels**           | Push events from non-Claude sources into your running session   | Reacting to CI failures, chat messages, webhooks      |

## See Also

- [Channels reference](/en/channels-reference) — Build your own channel
- [Remote Control](/en/remote-control)
- [Scheduled tasks](/en/scheduled-tasks)
