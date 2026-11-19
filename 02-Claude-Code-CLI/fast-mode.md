---
title: "Speed up responses with fast mode - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/fast-mode"
category: "02-Claude-Code-CLI"
fetched_at: "2026-11-15T06:23:18Z"
last_modified: "Sat, 14 Nov 2026 19:07:38 GMT"
tags: ["claude-code", "search"]
---

## On this page

Back to top

- [Toggle fast mode](#toggle-fast-mode)
  - [Switch models while fast mode is on](#switch-models-while-fast-mode-is-on)
  - [Use fast mode in cloud sessions](#use-fast-mode-in-cloud-sessions)
- [Understand the cost tradeoff](#understand-the-cost-tradeoff)
  - [See where fast mode spend appears](#see-where-fast-mode-spend-appears)
- [Decide when to use fast mode](#decide-when-to-use-fast-mode)
  - [Fast mode vs effort level](#fast-mode-vs-effort-level)
- [Requirements](#requirements)
  - [Enable fast mode for your organization](#enable-fast-mode-for-your-organization)
  - [Use fast mode on Agent Platform](#use-fast-mode-on-agent-platform)
  - [Use fast mode behind proxies and LLM gateways](#use-fast-mode-behind-proxies-and-llm-gateways)
  - [Fast mode unavailable due to network connectivity issues](#fast-mode-unavailable-due-to-network-connectivity-issues)
  - [Fast mode is currently unavailable](#fast-mode-is-currently-unavailable)
  - [Fast mode has been disabled by your organization](#fast-mode-has-been-disabled-by-your-organization)
  - [Require per-session opt-in](#require-per-session-opt-in)
- [Handle rate limits](#handle-rate-limits)
- [Research preview](#research-preview)
- [See also](#see-also)

Model and responses

# Speed up responses with fast mode

Copy pageCopy page

Get faster Opus and Fable responses in Claude Code by toggling fast mode with `/fast`.

Copy pageCopy page

Fast mode for Claude Fable 5.2 and Claude Opus 5.5 is available. Fast mode for Claude Opus 5 and Claude Opus 4.8 is in [research preview](#research-preview).

Fast mode is a high-speed configuration for supported models, making the model up to 2.5x faster at a higher cost per token. Toggle it on with `/fast` when you need speed for interactive work such as rapid iteration or live debugging, and toggle it off when cost matters more than latency. Fast mode uses the same model with a different API configuration that prioritizes speed over cost efficiency, so quality and capabilities stay the same. On the Anthropic API, fast mode is supported on Fable 5.2, Opus 5.5, Opus 5, and Opus 4.8, but not on Sonnet, Haiku, or other models. For the models on Google Cloud’s Agent Platform, see [Use fast mode on Agent Platform](#use-fast-mode-on-agent-platform).

Fast mode for Opus 4.8 was deprecated on October 30, 2026, and will be removed on November 30, 2026. If Opus 4.8 is still your model with fast mode on after that date, the API rejects your requests. By that date, switch to Opus 5.5 or turn fast mode off in your session:

- **To keep fast mode**: use [`/model`](model-config.md#setting-your-model) to switch to [Opus 5.5](model-config.md#model-aliases), which requires Claude Code v2.1.280 or later. Fast mode stays on after the switch. If a new session still starts on Opus 4.8, see [A new session starts on a different model than you picked](model-config.md#a-new-session-starts-on-a-different-model-than-you-picked).
- **To stay on Opus 4.8 at standard speed**: run [`/fast off`](commands.md)

Opus 4.7 doesn’t support fast mode, so switching to it turns fast mode off. Fast mode for Opus 4.7 was deprecated on June 25, 2026, and removed on July 24, 2026. What to know:

- Use `/fast` to toggle on fast mode in the Claude Code CLI. The [VS Code extension](../03-IDE-Integrations/vs-code.md) offers a **Toggle fast mode** command when the selected model supports fast mode. On the Anthropic API, Claude Code saves that toggle to your [`fastMode` setting](#toggle-fast-mode).
- Anthropic’s fast mode pricing per MTok input/output: \$16/\$80 on Fable 5.2, \$8/\$40 on Opus 5.5, and \$10/\$50 on Opus 5 and Opus 4.8.
- Available to Claude Code users on subscription plans (Pro/Max/Ultra/Team/Enterprise), on Claude Console, and on Google Cloud’s Agent Platform [with conditions](#use-fast-mode-on-agent-platform). Team and Enterprise organizations need an Owner to enable it first, and Console organizations need access provisioned first to use it with Opus 5 or Opus 4.8. [Requirements](#requirements) describes both.
- For Claude Code users on subscription plans (Pro/Max/Ultra/Team/Enterprise), fast mode is available via usage credits only and not included in the subscription rate limits.

## [](#toggle-fast-mode)Toggle fast mode

On Agent Platform, `/fast` and the `fastMode` setting work differently, so follow [Use fast mode on Agent Platform](#use-fast-mode-on-agent-platform) instead. In the CLI, toggle fast mode in either of these ways:

- Run `/fast`, press Space to toggle on or off, then press Enter to confirm
- On a model that supports fast mode, set `"fastMode": true` in your [user settings file](settings.md). If you set it on any other model, you stay on that model with fast mode off. On Fable 5.2, that setting alone has no effect until you run `/fast` while using Fable 5.2.

By default on the Anthropic API, fast mode you turn on in an interactive session persists across sessions on a supported model. On Fable 5.2, fast mode persists only if you [turned it on while using Fable 5.2](#switch-models-while-fast-mode-is-on). You can configure fast mode to reset each session. See [require per-session opt-in](#require-per-session-opt-in) for details. Outside a [cloud session](#use-fast-mode-in-cloud-sessions), in [non-interactive mode](headless.md) with the `-p` flag, `/fast` works only in a session launched with fast mode in its [`--settings`](cli-reference.md#cli-flags) value, for example `claude -p --settings '{"fastMode": true}'`; the toggle then applies to that session only and isn’t saved as your default. The `-p` form requires Claude Code v2.1.205 or later. Elsewhere in non-interactive mode, the command reports that fast mode isn’t available. You can run `/fast` while Claude is working, and Claude Code toggles fast mode without waiting for the turn to end. Claude Code finishes the running turn at its original speed, so the speed change takes effect from your next turn. If your current model doesn’t support fast mode, turning it on also switches your model, and Claude Code uses the new model from its next request in that turn. For the best cost efficiency, enable fast mode at the start of a session rather than switching mid-conversation. See [understand the cost tradeoff](#understand-the-cost-tradeoff) for details. When you enable fast mode with `/fast`:

- On the Anthropic API, if your current model doesn’t support fast mode, Claude Code switches to Opus
- Fast mode on Fable 5.2 requires Claude Code v2.1.321 or later
- You’ll see a confirmation message: “Fast mode ON”
- A small `↯` icon appears next to the prompt while fast mode is active
- Run `/fast` again at any time to check whether fast mode is on or off

On the Anthropic API, Opus 5.5 is the fast mode default in Claude Code v2.1.280 and later. Before v2.1.280, fast mode defaulted to Opus 5 from v2.1.219. When you disable fast mode with `/fast` again, you remain on your current model. To switch to a different model, use `/model`.

### [](#switch-models-while-fast-mode-is-on)Switch models while fast mode is on

Fast mode follows your model switches:

- **Switch away**: when you switch to a model that doesn’t support fast mode, Claude Code turns fast mode off. This includes Opus 4.7; before v2.1.221, fast mode stayed on after a switch to Opus 4.7 and the API rejected the requests.
- **Switch back**: fast mode comes back on a supported Opus model when your saved preference is on. With [per-session opt-in](#require-per-session-opt-in), run `/fast` instead.
- **Switch to Fable 5.2**: fast mode turns off unless you turned it on while using Fable 5.2. To turn it on, run `/fast` on Fable 5.2. Unless you’ve set [per-session opt-in](#require-per-session-opt-in), that choice lasts across sessions on the Anthropic API until you turn fast mode off or turn it on with another model.

Whenever a model switch turns fast mode on or off, Claude Code shows a `Fast mode ON` or `Fast mode OFF` confirmation, and the `↯` icon appears while fast mode is on. This holds whether you switch with `/model`, with [`/config model=<model>`](settings.md), or from a device connected through [Remote Control](remote-control.md).

### [](#use-fast-mode-in-cloud-sessions)Use fast mode in cloud sessions

Fast mode works in [cloud sessions](claude-code-on-the-web.md) when it’s available on your account, whether the session runs on Anthropic-managed infrastructure or a [self-hosted runner](../13-Enterprise-Admin/self-hosted-environments.md) on the Anthropic API. Requires Claude Code v2.1.271 or later in the session’s environment. Type `/fast on` in the session to turn fast mode on. It stays on for that session only and isn’t saved as your default. The [requirements](#requirements) apply in cloud sessions too. In the browser at [claude.ai/code](https://claude.ai/code), you can also turn fast mode on and off from the model menu on the message box. The menu shows the switch when your plan includes fast mode and the selected model supports it.

## [](#understand-the-cost-tradeoff)Understand the cost tradeoff

Fast mode has higher per-token pricing than standard speed. These are Anthropic’s rates:

| Model     | Input (MTok) | Output (MTok) |
|-----------|--------------|---------------|
| Fable 5.2 | \$16         | \$80          |
| Opus 5.5  | \$8          | \$40          |
| Opus 5    | \$10         | \$50          |
| Opus 4.8  | \$10         | \$50          |

Fast mode pricing is flat across the full 1M token context window. For the standard rate to compare against, see the [Claude pricing reference](../17-Billing-Plans/about-claude-pricing.md). The first time you enable fast mode in a conversation, you pay the full fast mode uncached input token price for the entire conversation context. The deeper into a conversation you are, the more this costs, so the charge is smallest when you enable fast mode at the start. Fast mode and standard speed keep [separate caches](prompt-caching.md#turning-on-fast-mode), so each later switch reads part or all of the conversation uncached again.

### [](#see-where-fast-mode-spend-appears)See where fast mode spend appears

You see fast mode spend in a different place depending on how you signed in, so first run [`/status`](commands.md) to check. If it shows a `Login method` row such as `Claude Max account`, you signed in with a Claude subscription. If it shows an `API key` row instead, your requests bill to a Claude Console organization.

- **Pro, Max, and Ultra**: you pay for fast mode from your usage credits. Go to [**Settings \> Usage**](https://claude.ai/settings/usage) on claude.ai, where the **Usage credits** section shows how much you’ve spent in usage credits this month. That figure includes fast mode but doesn’t break it out separately.
- **Team and Enterprise**: your organization pays for your fast mode usage from its usage credits. To see your own usage-credits spend, run [`/usage`](../17-Billing-Plans/costs.md#check-your-usage-credits-spend). For where your organization sees that spend, see [Claude for Teams and Enterprise](../17-Billing-Plans/costs.md#claude-for-teams-and-enterprise).
- **Claude Console**: your organization pays for fast mode with the rest of its API usage. On the Console [Usage](../04-API-Reference/Other/playground.md) and [Cost](../04-API-Reference/Other/playground.md) pages, select **Speed** in the **Group by** menu to separate fast mode from standard-speed usage. You see that option only when the selected date range includes fast mode usage.

## [](#decide-when-to-use-fast-mode)Decide when to use fast mode

Fast mode is best for interactive work where response latency matters more than cost:

- Rapid iteration on code changes
- Live debugging sessions
- Time-sensitive work with tight deadlines

Standard mode is better for:

- Long autonomous tasks where speed matters less
- Batch processing or CI/CD pipelines
- Cost-sensitive workloads

### [](#fast-mode-vs-effort-level)Fast mode vs effort level

Fast mode and effort level both affect response speed, but differently:

| Setting | Effect |
|----|----|
| **Fast mode** | Same model quality, lower latency, higher cost |
| **Lower effort level** | Less thinking time, faster responses, potentially lower quality on complex tasks |

You can combine both: use fast mode with a lower [effort level](model-config.md#adjust-effort-level) for maximum speed on straightforward tasks.

## [](#requirements)Requirements

Fast mode requires all of the following:

- **Supported provider**: fast mode is available through the Anthropic Console API, for Claude subscription plans using usage credits, and on Google Cloud’s Agent Platform [with conditions](#use-fast-mode-on-agent-platform). It is not available on Amazon Bedrock, Microsoft Foundry, or Claude Platform on AWS, where `/fast` reports “Fast mode is not available on this provider”. Console organizations must also have [fast mode access provisioned](#enable-fast-mode-for-your-organization) to use it with Opus 5 or Opus 4.8.
- **Usage credits turned on for subscription plans**: on a Pro, Max, Ultra, Team, or Enterprise plan, your account must have [usage credits](../17-Billing-Plans/costs.md#add-usage-credits-to-your-subscription) turned on, which allows billing beyond your plan’s included usage. Until they’re on, `/fast` reports “Fast mode requires usage credits”. To turn them on, follow the step for your plan:
  - On Pro, Max, and Ultra, turn them on in the **Usage credits** section of [**Settings \> Usage**](https://claude.ai/settings/usage) on claude.ai, or run `/usage-credits` to open that page.
  - On Team and Enterprise, a member with billing access turns them on for the organization at [**Organization settings \> Usage**](https://claude.ai/admin-settings/usage), and a member without it runs `/usage-credits` to send the organization’s admins a request.

Fast mode usage draws directly from usage credits, even if you have remaining usage on your plan.

- **Paid Console organization**: Claude Console accounts don’t use usage credits, and your organization pays for fast mode per token with the rest of its API usage. On the Console’s free Evaluation plan, `/fast` shows “Fast mode unavailable during evaluation. Please purchase credits.” To clear it, purchase credits in your [Console billing settings](../04-API-Reference/Other/playground.md). Fast mode with Fable 5.2 or Opus 5.5 also depends on your organization’s [usage tier](../04-API-Reference/Endpoints/rate-limits.md).
- **Owner enablement for Team and Enterprise**: fast mode is disabled by default for Team and Enterprise organizations. An Owner must explicitly [enable fast mode](#enable-fast-mode-for-your-organization) before users can access it.

Four organization settings can block turning fast mode on with `/fast`:

- **Fast mode not enabled**: if fast mode hasn’t been enabled for your organization, turning fast mode on with `/fast` shows “Fast mode has been disabled by your organization.”
- **Fast mode turned off by managed settings**: if your organization deploys [managed settings](../13-Enterprise-Admin/managed-settings.md) that set [`fastMode: false`](settings-reference.md#fastmode), turning fast mode on with `/fast` shows the same “Fast mode has been disabled by your organization” message.
- **Per-session opt-in required**: managed settings that set [`fastModePerSessionOptIn: true`](#require-per-session-opt-in) refuse `/fast on` with the same message everywhere except an interactive terminal session.
- **Fast-mode model not allowed**: if your organization’s [`availableModels`](model-config.md#restrict-model-selection) allowlist excludes the model `/fast` switches to, turning it on is refused with “is not in your organization’s allowed models”. In a session already running on an allowed model that supports fast mode, `/fast` instead enables fast mode on your current model without switching models.

### [](#enable-fast-mode-for-your-organization)Enable fast mode for your organization

Where you enable fast mode depends on which product your organization uses:

- **Console** (API customers): an admin enables it in [Claude Code preferences](https://platform.claude.com/claude-code/preferences)
- **Claude AI** (Team and Enterprise): an Owner enables it at [**Organization settings \> Claude Code**](https://claude.ai/admin-settings/claude-code)

Console organizations that use Claude Opus 5 or Claude Opus 4.8 also need provisioned access, as described in [fast mode on the Claude API](../04-API-Reference/Guides/build-with-claude-fast-mode.md). Without that access, fast mode requests on those models hit the [fast mode rate limit](#handle-rate-limits) and fall back to standard speed until access is provisioned. Another option to disable fast mode entirely is to set `CLAUDE_CODE_DISABLE_FAST_MODE=1`. See [Environment variables](env-vars.md).

### [](#use-fast-mode-on-agent-platform)Use fast mode on Agent Platform

On [Google Cloud’s Agent Platform](google-vertex-ai.md), you can turn fast mode on for Fable 5.2, with `/fast` in an interactive session or with launch flags in [non-interactive mode](headless.md). Requires Claude Code v2.1.322 or later. Fast mode needs the [region](google-vertex-ai.md#region-configuration) for Fable 5.2 to be `global`, `us`, or `eu`. In another region, `/fast` reports `Fast mode needs Vertex region global, us or eu`, and `claude -p` runs at standard speed. Set the region in your shell before you start Claude Code, for example to `global`:

```python
export VERTEX_REGION_CLAUDE_FABLE_5_2=global
```

Then turn fast mode on:

- **In an interactive session**: run `/fast`. It switches you to Fable 5.2 from an Opus model or another model without fast mode on Agent Platform. Fast mode isn’t saved as your default.
- **In non-interactive mode**: pass Fable 5.2 as [`--model`](cli-reference.md#cli-flags) and fast mode in [`--settings`](cli-reference.md#cli-flags), for example `claude -p "Summarize this project" --model claude-fable-5-2 --settings '{"fastMode": true}'`

On Agent Platform, `"fastMode": true` in your user, project, local, or managed settings has no effect. If Agent Platform refuses fast mode, Claude Code falls back to standard speed. An interactive session then shows one of these terminal messages:

- `Using standard speed on Fable 5.2 · fast mode wasn't available`: run `/fast on` to try fast mode again
- `Fast mode paused: your cloud provider refused a fast request · trying again in 30m`: Agent Platform answered a fast mode request with a 403 or 404 error. To try sooner, run `/fast on`. Requires Claude Code v2.1.323 or later.

### [](#use-fast-mode-behind-proxies-and-llm-gateways)Use fast mode behind proxies and LLM gateways

Before offering fast mode on the Anthropic API, Claude Code checks your organization’s fast mode availability with a request directly to `api.anthropic.com`. The check doesn’t follow [`ANTHROPIC_BASE_URL`](../13-Enterprise-Admin/llm-gateway-connect.md#set-the-base-url-and-credential), so on a network that routes Claude traffic through an [LLM gateway](../13-Enterprise-Admin/llm-gateway.md) and blocks direct egress to `api.anthropic.com`, the check fails even though inference requests work. The check does use a configured [HTTP proxy](../13-Enterprise-Admin/network-config.md#proxy-configuration), so a network block fails the check only where `api.anthropic.com` is unreachable even through the proxy. If your organization has fast mode enabled and `/fast` says otherwise, find the message it shows among these cases.

#### [](#fast-mode-unavailable-due-to-network-connectivity-issues)Fast mode unavailable due to network connectivity issues

The availability check failed, for example because your network blocks `api.anthropic.com`, and requests run at standard speed. A check that succeeded in the past keeps working from its cached result, so a blocked check mostly affects new installations. To restore fast mode, allowlist direct egress to `api.anthropic.com`, or set `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS=1`, which treats a failed check as available and still honors a “disabled by your organization” response.

#### [](#fast-mode-is-currently-unavailable)Fast mode is currently unavailable

Behind a gateway, check for these configurations, in which Claude Code doesn’t send the availability check and has no earlier successful check cached:

- You point `ANTHROPIC_BASE_URL` at your gateway and set [`ANTHROPIC_API_KEY`](../13-Enterprise-Admin/llm-gateway-connect.md#set-the-base-url-and-credential) to a gateway-issued key that isn’t in the format of an Anthropic API key.
- You set [`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`](env-vars.md), so Claude Code skips the check.

To restore fast mode in either configuration, set `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS=1`.

#### [](#fast-mode-has-been-disabled-by-your-organization)Fast mode has been disabled by your organization

Behind a gateway, you can see this message even when your organization has fast mode enabled, in either of these configurations:

- You authenticate with [`ANTHROPIC_AUTH_TOKEN`](../13-Enterprise-Admin/llm-gateway-connect.md#set-the-base-url-and-credential) alone, with no claude.ai login, no API key, and no cached successful check. Claude Code then treats fast mode as disabled by your organization without sending the request.
- A proxy intercepts the check and answers with its own page, for example a TLS-inspecting proxy returning an HTTP 200 block page. Claude Code reads that page as a response saying your organization has fast mode disabled.

In both cases, set `CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK=1`, which skips the check entirely, rather than `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS`, which doesn’t apply to either.

The skip variables change only the client-side check. When your organization has fast mode disabled, the API rejects fast mode requests whether or not they’re set. Claude Code then retries the request at standard speed, turns fast mode off, and `/fast` reports that your organization has disabled fast mode.

### [](#require-per-session-opt-in)Require per-session opt-in

By default on the Anthropic API, fast mode a user turns on in an interactive session persists across sessions on a supported model. On Fable 5.2, fast mode persists only if the user [turned it on while using Fable 5.2](#switch-models-while-fast-mode-is-on). To make every session start with fast mode off, set `fastModePerSessionOptIn` to `true` in any [settings file](settings.md#where-settings-live). Users then enable it with `/fast` in each session. Owners on [Team](../17-Billing-Plans/pricing.md#team-&-enterprise) or [Enterprise](https://anthropic.com/contact-sales?utm_source=claude_code&utm_medium=docs&utm_content=fast_mode_enterprise) plans can deploy it organization-wide through [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md).

```python
{
  "fastModePerSessionOptIn": true
}
```

This is useful for controlling costs in organizations where users run multiple concurrent sessions. The user’s fast mode preference is still saved, so removing this setting restores the default persistent behavior. When managed settings set the key, `/fast on` works only in an interactive terminal session. Everywhere else, including [non-interactive mode](headless.md), the [VS Code extension](../03-IDE-Integrations/vs-code.md), and [cloud sessions](#use-fast-mode-in-cloud-sessions), it’s refused with a message that your organization has disabled fast mode.

## [](#handle-rate-limits)Handle rate limits

Fast mode has separate rate limits from standard speed; for Console organizations, the Claude Platform’s [rate limits](../04-API-Reference/Endpoints/rate-limits.md) page describes them. When you hit the fast mode rate limit:

1.  Fast mode automatically falls back to standard speed
2.  The `↯` icon turns gray to indicate cooldown
3.  You continue working at standard speed and pricing
4.  When the cooldown expires, fast mode automatically re-enables

To disable fast mode manually instead of waiting for cooldown, run `/fast` again. If you run out of usage credits mid-session, Claude Code retries each rejected fast mode request at standard speed and pricing, so you keep working, and there is no cooldown. How you see the rejection depends on the session type:

- In an interactive session, Claude Code shows a “Fast mode disabled · Out of usage credits” notification and turns fast mode off. Your saved fast mode preference doesn’t change; run `/fast` to turn fast mode back on.
- In [non-interactive mode](headless.md) with `--output-format stream-json`, and through the Agent SDK, Claude Code emits the same text on the message stream as a `system` message with subtype `notification`. The message arrives once per turn while you’re out of usage credits. Fast mode stays on.

## [](#research-preview)Research preview

Fast mode for Claude Opus 5 and Claude Opus 4.8 is a research preview feature, which means:

- The feature may change based on feedback
- Availability and pricing are subject to change
- The underlying API configuration may evolve

Report issues or feedback through your usual Anthropic support channels.

## [](#see-also)See also

- [Model configuration](model-config.md): switch models and adjust effort levels
- [Manage costs effectively](../17-Billing-Plans/costs.md): track token usage and reduce costs
- [Status line configuration](statusline.md): display model and context information
