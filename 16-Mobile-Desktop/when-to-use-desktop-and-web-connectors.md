---
title: "When to use desktop and web connectors | Claude Help Center"
source_url: "https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors"
category: "16-Mobile-Desktop"
fetched_at: "2026-09-30T06:31:06Z"
tags: ["connectors", "desktop", "plugins"]
---

# When to use desktop and web connectors


Claude can connect to your tools in two ways: through the web (remote connectors) or through the Claude Desktop app (desktop extensions). Most connectors are remote—they're the default choice and work everywhere you use Claude.

## Use a remote connector when

- The tool is a cloud service you sign into (Slack, Notion, Linear, GitHub, your company's SaaS)

- You want the connector available everywhere—web, mobile, Cowork, Desktop, and Claude Code

- You're connecting something from the **[Connectors Directory](https://claude.ai/directory)**

Remote connectors work across all Claude surfaces. Once connected, they're available everywhere without extra setup.

## Use a desktop extension when

- The tool runs on your computer—local files, a database on localhost, a desktop application

- The tool needs OS-level access (filesystem, clipboard, local processes)

- There's no cloud version to connect to

Desktop extensions run locally and are only available in Claude Desktop and Claude Code—not on web or mobile.

## Plugins work with both

A plugin can bundle either remote or local MCP servers (or both). Adding a plugin that references a remote MCP makes it available everywhere. One that references a local MCP works in Cowork and Claude Code, not in chat.

## Quick guide

[TABLE]

## Get started

- Browse and add remote connectors: **[Settings → Connectors](https://claude.ai/settings/connectors)** or the **[Connectors Directory](https://claude.ai/directory)**

- Install a desktop extension: Open Claude Desktop → Settings → Extensions

- Building your own? See the **[connector building docs](https://claude.com/docs/connectors/building)** for remote connectors or the **[MCPB guide](https://claude.com/docs/connectors/building/mcpb)** for local ones.
