---
title: "Move Claude Code CLI users | Claude Help Center"
source_url: "https://support.claude.com/en/articles/18466061"
category: "02-Claude-Code-CLI"
fetched_at: "2026-11-18T06:28:11Z"
tags: ["claude-code", "cli"]
---

# Move Claude Code CLI users


If your developers use the Claude Code CLI, set it up separately from the desktop app. The desktop app takes its provider settings from its Claude Desktop on 3P configuration, **[not from `ANTHROPIC_BASE_URL` or `settings.json`](../13-Enterprise-Admin/llm-gateway-connect.md)**, and **[passes them to the Code sessions it starts](https://claude.com/docs/third-party/claude-desktop/code)**. The CLI reads environment variables, settings files, and **[Claude Code managed settings](../13-Enterprise-Admin/managed-settings.md)**, which use **[a separate policy key](../13-Enterprise-Admin/admin-setup.md)**.

This guide is for admins of organizations on Claude Enterprise plans.

This article is part of **[Move from Claude Enterprise to Claude Desktop on a cloud provider](https://support.claude.com/en/articles/18426225)**, which defines the terms wave, overlap period, and cutoff date.

**[The CLI and everything that runs locally work on every provider](feature-availability.md)**. After the move, developers sign in differently, your policies reach their computers differently, and some features aren't available.

## Connect the CLI to your provider

Set the provider variables for **[Amazon Bedrock](amazon-bedrock.md)**, **[Google Cloud](google-vertex-ai.md)**, **[Microsoft Foundry](microsoft-foundry.md)**, or an **[LLM gateway](../13-Enterprise-Admin/llm-gateway-connect.md)**. Developers **[don't need a claude.ai browser login](authentication.md)**. With a gateway, set both the base URL and a gateway credential. With only the base URL, **[a saved claude.ai login stays the active credential](../13-Enterprise-Admin/llm-gateway.md)**, so its limits and billing still apply. Before a team rollout, **[pin your model versions](third-party-integrations.md)**.

## Deliver policy to each device

**[Server-managed settings don't apply](../13-Enterprise-Admin/server-managed-settings.md)** when a third-party provider or a custom base URL is set. Move those policies to **[managed settings on the device](../13-Enterprise-Admin/managed-settings.md)**. You can deliver them as a `managed-settings.json` file, the `com.anthropic.claudecode` macOS profile, or the `HKLM\SOFTWARE\Policies\ClaudeCode` registry key. They take priority over user and project settings, apart from a few security-sensitive keys where a stricter value from a lower level still counts.

- **Limit which providers a computer can use:** Set **[`allowedProviders`](third-party-integrations.md)** (Claude Code v2.1.285 or later). During the overlap period, **[a list such as `["anthropic", "bedrock"]`](authentication.md)** lets developers use either one. After the move, list only the new provider. Keep "anthropic" on computers where users stay signed in to claude.ai in Claude Desktop, because their Cowork sessions are refused without it. For a gateway reached through `ANTHROPIC_BASE_URL`, list `"customEndpoint"` and put the gateway URL in the `env` block of the same managed source.

- **Remove old login settings:** With gateway credentials, **[remove `forceLoginMethod` and `forceLoginOrgUUID`](../13-Enterprise-Admin/llm-gateway-rollout.md)**, because either key blocks gateway credentials at startup. On a cloud provider, those keys **[block a session only while certain credentials are still on the computer](authentication.md)**: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, an `apiKeyHelper` credential, or an API key saved by an earlier Claude Console login.

Developers can run `/status` to see the active provider and where their settings come from. For telemetry, network hosts, and updates, see **[Data usage](../13-Enterprise-Admin/data-usage.md)**, **[Enterprise network configuration](../13-Enterprise-Admin/network-config.md)**, and **[Advanced setup](../01-Getting-Started/setup.md)**.

## Track cost and usage

On Bedrock, Google Cloud, and Foundry, usage is **[billed per token to your cloud account](../17-Billing-Plans/costs.md)**, and cost controls are in your cloud billing console. Through a gateway, usage is **[billed per token to whoever owns the credential the gateway forwards](../13-Enterprise-Admin/llm-gateway.md)**. The claude.ai analytics dashboards and the Claude Code Analytics API don't cover this usage. For reporting by user, use **[OpenTelemetry](../13-Enterprise-Admin/monitoring-usage.md)** or an LLM gateway.

## What carries over for developers

[TABLE]

## What to watch for during the overlap period

- **Server-managed settings take priority in sessions that still authenticate with claude.ai.** By default, Claude Code **[uses them and skips the managed settings on the device](../13-Enterprise-Admin/server-managed-settings.md)**, with a few exceptions such as the `env` block and `allowedProviders`. If some developers stay on claude.ai, **[use server-managed settings for them and a file or OS policy for everyone else](../13-Enterprise-Admin/admin-setup.md)**.

- **A saved claude.ai login stays on the computer.** Cloud provider credentials **[take precedence](authentication.md)** over it, and `/logout` **[is unavailable](amazon-bedrock.md)** once a cloud provider is active. If you want the login removed, have developers log out before you deploy the provider settings. Logging out also **[removes saved MCP server logins and plugin secrets](troubleshoot-install.md)**, so they'll need to authorize those again. With a gateway credential, `/logout` stays available, and you can **[run it to clear the saved login](../13-Enterprise-Admin/llm-gateway-connect.md)**.

- **CLI policy can override part of your desktop policy.** By default, if a computer has Claude Code managed settings, a desktop Code session **[ignores the managed policy values that the desktop app supplies](https://claude.com/docs/third-party/claude-desktop/code)**. To use both, see `parentSettingsBehavior` in **[Deploy managed settings](../13-Enterprise-Admin/managed-settings.md)**.

## Checklist for developers

**Before the move**

- Update Claude Code to the version your admins specify.

- Pull any cloud sessions you need into the terminal with `claude --teleport`. First make sure the session's branch is pushed to the remote, and clean your working tree.

- List the claude.ai connectors you use, so they can be added as MCP servers.

- Copy any skill you rely on out of `~/.claude/skills/synced/`, and list the synced plugins you'll need to reinstall.

**On the day you move**

1.  Sign in to your cloud provider the way your admins describe, for example with `aws sso login`, `gcloud auth application-default login`, or `az login`.

2.  Start `claude` and run `/status`. Check the provider, the model, and the settings source.

3.  Reopen a recent session with `claude --resume` and confirm that it responds.

4.  Tell your admins about any tool or connector that's missing.
