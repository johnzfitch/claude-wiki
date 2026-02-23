---
category: "02-Claude-Code-CLI"
fetched_at: "2026-02-23T00:45:39Z"
source_url: "https://code.claude.com/docs/en/fast-mode"
title: "Speed up responses with fast mode - Claude Code Docs"
---

[Skip to main content](#content-area)

[Claude Code Docs home page](/docs)

English

Search...

⌘K

Ask AI

- [Claude Developer Platform](https://platform.claude.com/)
- [Claude Code on the Web](https://claude.ai/code)
- [](https://claude.ai/code)
  Claude Code on the Web

Search...

Navigation

Configuration

Speed up responses with fast mode

[Getting started](/docs/en/overview)

[Build with Claude Code](/docs/en/sub-agents)

[Deployment](/docs/en/third-party-integrations)

[Administration](/docs/en/setup)

[Configuration](/docs/en/settings)

[Reference](/docs/en/cli-reference)

[Resources](/docs/en/legal-and-compliance)

##### Configuration

- [](/docs/en/settings)
  Settings
- [](/docs/en/permissions)
  Permissions
- [](/docs/en/sandboxing)
  Sandboxing
- [](/docs/en/terminal-config)
  Terminal configuration
- [](/docs/en/model-config)
  Model configuration
- [](/docs/en/fast-mode)
  Speed up responses with fast mode
- [](/docs/en/memory)
  Memory management
- [](/docs/en/statusline)
  Customize status line
- [](/docs/en/keybindings)
  Customize keyboard shortcuts

On this page

- [Toggle fast mode](#toggle-fast-mode)
- [Understand the cost tradeoff](#understand-the-cost-tradeoff)
- [Decide when to use fast mode](#decide-when-to-use-fast-mode)
- [Fast mode vs effort level](#fast-mode-vs-effort-level)
- [Requirements](#requirements)
- [Enable fast mode for your organization](#enable-fast-mode-for-your-organization)
- [Handle rate limits](#handle-rate-limits)
- [Research preview](#research-preview)
- [See also](#see-also)

Configuration

# Speed up responses with fast mode

Copy page

Get faster Opus 4.6 responses in Claude Code by toggling fast mode.

Copy page

Fast mode is in [research preview](#research-preview). The feature, pricing, and availability may change based on feedback.

Fast mode is a high-speed configuration for Claude Opus 4.6, making the model 2.5x faster at a higher cost per token. Toggle it on with `/fast` when you need speed for interactive work like rapid iteration or live debugging, and toggle it off when cost matters more than latency. Fast mode is not a different model. It uses the same Opus 4.6 with a different API configuration that prioritizes speed over cost efficiency. You get identical quality and capabilities, just faster responses. What to know:

- Use `/fast` to toggle on fast mode in Claude Code CLI. Also available via `/fast` in Claude Code VS Code Extension.
- Fast mode for Opus 4.6 pricing starts at \$30/150 MTok. Fast mode is available at a 50% discount for all plans until 11:59pm PT on February 16.
- Available to all Claude Code users on subscription plans (Pro/Max/Team/Enterprise) and Claude Console.
- For Claude Code users on subscription plans (Pro/Max/Team/Enterprise), fast mode is available via extra usage only and not included in the subscription rate limits.

This page covers how to [toggle fast mode](#toggle-fast-mode), its [cost tradeoff](#understand-the-cost-tradeoff), [when to use it](#decide-when-to-use-fast-mode), [requirements](#requirements), and [rate limit behavior](#handle-rate-limits).

## 

[​](#toggle-fast-mode)

Toggle fast mode

Toggle fast mode in either of these ways:

- Type `/fast` and press Tab to toggle on or off
- Set `"fastMode": true` in your [user settings file](/docs/en/settings)

Fast mode persists across sessions. For the best cost efficiency, enable fast mode at the start of a session rather than switching mid-conversation. See [understand the cost tradeoff](#understand-the-cost-tradeoff) for details. When you enable fast mode:

- If you’re on a different model, Claude Code automatically switches to Opus 4.6
- You’ll see a confirmation message: “Fast mode ON”
- A small `↯` icon appears next to the prompt while fast mode is active
- Run `/fast` again at any time to check whether fast mode is on or off

When you disable fast mode with `/fast` again, you remain on Opus 4.6. The model does not revert to your previous model. To switch to a different model, use `/model`.

## 

[​](#understand-the-cost-tradeoff)

Understand the cost tradeoff

Fast mode has higher per-token pricing than standard Opus 4.6:

| Mode                           | Input (MTok) | Output (MTok) |
|--------------------------------|--------------|---------------|
| Fast mode on Opus 4.6 (\<200K) | \$30         | \$150         |
| Fast mode on Opus 4.6 (\>200K) | \$60         | \$225         |

Fast mode is compatible with the 1M token extended context window. When you switch into fast mode mid-conversation, you pay the full fast mode uncached input token price for the entire conversation context. This costs more than if you had enabled fast mode from the start.

## 

[​](#decide-when-to-use-fast-mode)

Decide when to use fast mode

Fast mode is best for interactive work where response latency matters more than cost:

- Rapid iteration on code changes
- Live debugging sessions
- Time-sensitive work with tight deadlines

Standard mode is better for:

- Long autonomous tasks where speed matters less
- Batch processing or CI/CD pipelines
- Cost-sensitive workloads

### 

[​](#fast-mode-vs-effort-level)

Fast mode vs effort level

Fast mode and effort level both affect response speed, but differently:

| Setting | Effect |
|----|----|
| **Fast mode** | Same model quality, lower latency, higher cost |
| **Lower effort level** | Less thinking time, faster responses, potentially lower quality on complex tasks |

You can combine both: use fast mode with a lower [effort level](/docs/en/model-config#adjust-effort-level) for maximum speed on straightforward tasks.

## 

[​](#requirements)

Requirements

Fast mode requires all of the following:

- **Not available on third-party cloud providers**: fast mode is not available on Amazon Bedrock, Google Vertex AI, or Microsoft Azure Foundry. Fast mode is available through the Anthropic Console API and for Claude subscription plans using extra usage.
- **Extra usage enabled**: your account must have extra usage enabled, which allows billing beyond your plan’s included usage. For individual accounts, enable this in your [Console billing settings](https://platform.claude.com/settings/organization/billing). For Teams and Enterprise, an admin must enable extra usage for the organization.

Fast mode usage is billed directly to extra usage, even if you have remaining usage on your plan. This means fast mode tokens do not count against your plan’s included usage and are charged at the fast mode rate from the first token.

- **Admin enablement for Teams and Enterprise**: fast mode is disabled by default for Teams and Enterprise organizations. An admin must explicitly [enable fast mode](#enable-fast-mode-for-your-organization) before users can access it.

If your admin has not enabled fast mode for your organization, the `/fast` command will show “Fast mode has been disabled by your organization.”

### 

[​](#enable-fast-mode-for-your-organization)

Enable fast mode for your organization

Admins can enable fast mode in:

- **Console** (API customers): [Claude Code preferences](https://platform.claude.com/claude-code/preferences)
- **Claude AI** (Teams and Enterprise): [Admin Settings \> Claude Code](https://claude.ai/admin-settings/claude-code)

## 

[​](#handle-rate-limits)

Handle rate limits

Fast mode has separate rate limits from standard Opus 4.6. When you hit the fast mode rate limit or run out of extra usage credits:

1.  Fast mode automatically falls back to standard Opus 4.6
2.  The `↯` icon turns gray to indicate cooldown
3.  You continue working at standard speed and pricing
4.  When the cooldown expires, fast mode automatically re-enables

To disable fast mode manually instead of waiting for cooldown, run `/fast` again.

## 

[​](#research-preview)

Research preview

Fast mode is a research preview feature. This means:

- The feature may change based on feedback
- Availability and pricing are subject to change
- The underlying API configuration may evolve

Report issues or feedback through your usual Anthropic support channels.

## 

[​](#see-also)

See also

- [Model configuration](/docs/en/model-config): switch models and adjust effort levels
- [Manage costs effectively](/docs/en/costs): track token usage and reduce costs
- [Status line configuration](/docs/en/statusline): display model and context information

Was this page helpful?

Yes

No

[Model configuration](/docs/en/model-config)[Memory management](/docs/en/memory)

[Claude Code Docs home page](/docs)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)

Assistant

Responses are generated using AI and may contain mistakes.
