---
title: "Feature availability - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/feature-availability"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-29T06:29:33Z"
tags: ["claude-code"]
---

## On this page

- [Availability by model provider](#availability-by-model-provider)
  - [Features available on every provider](#features-available-on-every-provider)
  - [Features that require a Claude subscription](#features-that-require-a-claude-subscription)
  - [CLI capabilities that vary by provider](#cli-capabilities-that-vary-by-provider)
  - [Admin and analytics](#admin-and-analytics)
  - [Summary by provider](#summary-by-provider)
- [Availability by subscription plan](#availability-by-subscription-plan)
- [Model availability](#model-availability)
- [Related resources](#related-resources)

Deployment

# Feature availability

Copy pageCopy page

Compare which Claude Code features are available across Anthropic subscription plans, the Anthropic Console, Amazon Bedrock, Claude Platform on AWS, Google Cloud’s Agent Platform, and Microsoft Foundry.

Copy pageCopy page

The Claude Code CLI and everything that runs locally work on every provider. For setup instructions per provider, see the [Enterprise deployment overview](third-party-integrations.md). To skip straight to what is missing on your provider, see the [summary by provider](#summary-by-provider) tabs. In the tables below, ✓ means available, ✗ means not available, and “See note” links to a footnote for partial support. A qualifier after ✓ narrows availability to that subset, and “Admin-enabled” means the feature is off until an organization admin turns it on.


[​](#availability-by-model-provider)

Availability by model provider

How you authenticate determines which features Claude Code can reach. For a single list of what is missing on your provider, see the [summary by provider](#summary-by-provider) tabs. To find your column in the tables:

- **Claude subscription**: you sign in with a claude.ai account on the Pro, Max, Team, or Enterprise plan
- **Anthropic Console**: you authenticate with an Anthropic API key or by [signing in to a Console account without one](../13-Enterprise-Admin/iam.md#sign-in-without-an-api-key)
- **Amazon Bedrock**: you use Claude models from the Amazon Bedrock model catalog and set `CLAUDE_CODE_USE_BEDROCK`. The [Mantle endpoint](amazon-bedrock.md#use-the-mantle-endpoint) (`CLAUDE_CODE_USE_MANTLE`) is covered by this column
- **Claude Platform on AWS**: you bought Claude through AWS Marketplace but call the Anthropic API, and set `CLAUDE_CODE_USE_ANTHROPIC_AWS`
- **Google Cloud’s Agent Platform**: Google-operated; you set `CLAUDE_CODE_USE_VERTEX`
- **Microsoft Foundry**: Anthropic-operated; you set `CLAUDE_CODE_USE_FOUNDRY`


[​](#features-available-on-every-provider)

Features available on every provider

These work on every provider:

- [CLI](../01-Getting-Started/quickstart.md) and [Agent SDK](../05-Agent-SDK/agent-sdk-overview.md)
- [VS Code](../03-IDE-Integrations/vs-code.md) and [JetBrains](../03-IDE-Integrations/jetbrains.md) extensions
- [Subagents](../09-Agents-Patterns/sub-agents.md), [hooks](../07-Hooks/hooks-guide.md), [commands](commands.md), and [skills](../08-Plugins-Skills/skills.md)
- [CLAUDE.md memory](memory.md), [plugins](../08-Plugins-Skills/plugins.md), and [MCP servers](../06-MCP-Tools/General/mcp.md)
- [Checkpoints](checkpointing.md), [sandboxing](sandboxing.md), and [Workflows](workflows.md)
- [OpenTelemetry metrics](../13-Enterprise-Admin/monitoring-usage.md) and the [managed settings file](../13-Enterprise-Admin/managed-settings.md#delivery-mechanisms)

These have provider-specific differences:

- **MCP servers**: [connectors from claude.ai](../06-MCP-Tools/General/mcp.md#use-mcp-servers-from-claude-ai) load only when your claude.ai subscription is the active authentication method. [Tool search](../06-MCP-Tools/General/mcp.md#configure-tool-search) is off by default when `ANTHROPIC_BASE_URL` points to a non-first-party host, and isn’t supported on Google Cloud’s Agent Platform models earlier than the Claude 4.5 generation or on Microsoft Foundry [deployments hosted on Azure](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md#hosting-options)
- **Subagents**: the built-in [Explore subagent](../09-Agents-Patterns/sub-agents.md#built-in-subagents) caps its inherited model at Opus on the Claude API, and inherits the main conversation’s model directly on any other provider, including Claude Platform on AWS
- **[Commands](commands.md#all-commands)**:
  - `/design-sync` and `/import` with its `claude import` subcommand form are unavailable on Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, and Claude Platform on AWS, and through a [Claude apps gateway](../13-Enterprise-Admin/claude-apps-gateway.md#availability-and-limitations)
  - `/voice` requires a claude.ai account
  - `/list-agents` and its alias `/peers` are available only in sessions where [cross-session messaging is enabled](cross-session-messaging.md#availability)


[​](#features-that-require-a-claude-subscription)

Features that require a Claude subscription

These require signing in with a claude.ai account and are not reachable with an Anthropic Console API key or from a third-party provider:

- [Cloud sessions](claude-code-on-the-web.md), Claude Code on mobile, and [Claude Code in Slack](../14-Connectors/slack.md)
- [Claude Code Desktop](../16-Mobile-Desktop/desktop.md)
- [Routines](web-scheduled-tasks.md) (`/schedule`)
- [Ultrareview](ultrareview.md)
- [Code Review](code-review.md): Team and Enterprise plans
- [Remote Control](remote-control.md)
- [Chrome extension](../03-IDE-Integrations/chrome.md)
- [Computer use](computer-use.md): Pro and Max plans
- [Artifacts](artifacts.md): Pro, Max, Team, and Enterprise plans
- [Voice dictation](voice-dictation.md)

Desktop is the partial exception: [gateway routing can be configured in the app or by an administrator](../13-Enterprise-Admin/llm-gateway-connect.md#desktop-app), Enterprise deployments can route Desktop to Google Cloud’s Agent Platform or a gateway provider via [managed settings](https://claude.com/docs/third-party/claude-desktop/configuration), and [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview) runs the Code tab on Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, or a self-hosted LLM gateway. For per-plan availability of these features, see [Availability by subscription plan](#availability-by-subscription-plan).


[​](#cli-capabilities-that-vary-by-provider)

CLI capabilities that vary by provider

These features work in the local CLI but depend on a server-side capability that not every provider exposes.

| Feature                                                        | Claude subscription                                                                                   | Anthropic Console             | Amazon Bedrock                | Claude Platform on AWS        | Google Cloud’s Agent Platform | Microsoft Foundry                                                                                                                        |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [Web search](tools-reference.md#websearch-tool-behavior) | ✓                                                                                                     | ✓                             | ✗                             | ✓                             | See note ^([1](#fn1))         | ✓ ([deployments hosted on Anthropic](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md#hosting-options)) |
| [Fast mode](fast-mode.md)                                | ✓ ([Owner-enabled](fast-mode.md#enable-fast-mode-for-your-organization) on Team and Enterprise) | ✓ (provisioned organizations) | ✗                             | ✗                             | ✗                             | ✗                                                                                                                                        |
| [Auto mode](auto-mode-config.md)                         | ✓                                                                                                     | ✓                             | See note ^([2](#fn2))         | ✓                             | See note ^([2](#fn2))         | See note ^([2](#fn2))                                                                                                                    |
| [Advisor](advisor.md)                                    | ✓                                                                                                     | ✓                             | ✗                             | ✗                             | ✗                             | ✗                                                                                                                                        |
| [Cross-session messaging](cross-session-messaging.md)    | ✓ ^([5](#fn5))                                                                                        | ✓ (same machine) ^([5](#fn5)) | ✓ (same machine) ^([5](#fn5)) | ✓ (same machine) ^([5](#fn5)) | ✓ (same machine) ^([5](#fn5)) | ✓ (same machine) ^([5](#fn5))                                                                                                            |
| [Channels](channels.md)                                  | ✓                                                                                                     | ✓                             | ✗                             | ✗                             | ✗                             | ✗                                                                                                                                        |
| [GitHub Actions](github-actions.md)                      | ✓                                                                                                     | ✓                             | ✓                             | ✗                             | ✓                             | ✓                                                                                                                                        |
| [GitLab CI/CD](gitlab-ci-cd.md)                          | ✓                                                                                                     | ✓                             | ✓                             | ✓                             | ✓                             | ✗                                                                                                                                        |


[​](#admin-and-analytics)

Admin and analytics

Organization-level controls and usage visibility.

| Feature                                                     | Claude subscription                                 | Anthropic Console       | Amazon Bedrock        | Claude Platform on AWS | Google Cloud’s Agent Platform | Microsoft Foundry     |
|-------------------------------------------------------------|-----------------------------------------------------|-------------------------|-----------------------|------------------------|-------------------------------|-----------------------|
| [Analytics dashboard and API](../13-Enterprise-Admin/analytics.md)           | ✓ (dashboard: Team and Enterprise; API: Enterprise) | ✓ ^([4](#fn4))          | ✗                     | ✗                      | ✗                             | ✗                     |
| [Server-managed settings](../13-Enterprise-Admin/server-managed-settings.md) | ✓ (Team and Enterprise)                             | ✓ (Team and Enterprise) | ✗                     | ✗                      | ✗                             | ✗                     |
| [Zero Data Retention](zero-data-retention.md)         | ✓ (qualified Enterprise accounts)                   | ✓ (qualified accounts)  | See note ^([3](#fn3)) | ✓ (qualified accounts) | See note ^([3](#fn3))         | See note ^([3](#fn3)) |

¹ On Google Cloud’s Agent Platform, web search is available for Claude 4 models and later.  
² On these providers, auto mode supports only Claude Sonnet 5 or later, Opus 4.7 or later, and the Fable models. See [Auto mode configuration](auto-mode-config.md). For the permission mode a session on these providers starts in, see [Which mode a session starts in](permission-modes.md#which-mode-a-session-starts-in). In v2.1.158 through v2.1.206, auto mode on these providers also required setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`; v2.1.207 removed the requirement.  
³ Subject to your agreement with the cloud provider.  
⁴ Dashboard and API only. [Contribution metrics](../13-Enterprise-Admin/analytics.md#enable-contribution-metrics) requires a claude.ai Team or Enterprise organization.  
⁵ Requires Claude Code v2.1.224 or later on macOS and Linux, including Linux inside WSL 2. On native Windows, requires Claude Code v2.1.234 or later. With API key authentication, messaging is same-machine only. On Amazon Bedrock, Claude Platform on AWS, Google Cloud’s Agent Platform, and Microsoft Foundry, messaging is same-machine only and requires Claude Code v2.1.248 or later. Claude can find your [cloud sessions](claude-code-on-the-web.md) and your sessions on other machines only from a session that is connected to [Remote Control](remote-control.md). To connect, you need a claude.ai sign-in and the other [Remote Control requirements](remote-control.md#requirements). See [Message sessions on other machines](cross-session-messaging.md#message-sessions-on-other-machines).

If you authenticate through an [LLM gateway](../13-Enterprise-Admin/llm-gateway.md), feature availability matches the underlying provider the gateway forwards to, except for the features Claude Code itself turns off. Whenever `ANTHROPIC_BASE_URL` points at a host other than `api.anthropic.com`, Claude Code turns off features such as [Remote Control](remote-control.md#requirements) and [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md#platform-availability), whatever the gateway forwards. Some Anthropic-only features such as the [Advisor](advisor.md) work only if the gateway forwards requests intact to the Anthropic API.For how the requests Claude Code sends differ between an Amazon Bedrock- or Agent Platform-format gateway, an `ANTHROPIC_BASE_URL` gateway, and a Claude apps gateway sign-in, see [client behavior by connection method](../13-Enterprise-Admin/llm-gateway-protocol.md#how-the-connection-method-changes-client-behavior).


[​](#summary-by-provider)

Summary by provider

Each tab lists what is unavailable or partially supported on that provider, with alternatives where one exists. Everything not listed works the same as on a Claude subscription, apart from the [provider-specific differences](#features-available-on-every-provider) noted above. On Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, and Claude Platform on AWS, error reporting and telemetry to Anthropic are off by default. See [default behaviors by API provider](../13-Enterprise-Admin/data-usage.md#default-behaviors-by-api-provider) for what traffic still reaches Anthropic and how to opt out.

- Amazon Bedrock

- Claude Platform on AWS

- Google Cloud's Agent Platform

- Microsoft Foundry

- Anthropic Console

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription), plus [web search](tools-reference.md#websearch-tool-behavior), [fast mode](fast-mode.md), [Advisor](advisor.md), [Channels](channels.md), the [analytics dashboard](../13-Enterprise-Admin/analytics.md), [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md), and the [`/design-sync` and `/import` commands](commands.md#all-commands).**Partial support:**

- [Desktop](../16-Mobile-Desktop/desktop.md): only via [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview)
- [Auto mode](auto-mode-config.md): Sonnet 5 or later, Opus 4.7 or later, and Fable models only
- [Cross-session messaging](cross-session-messaging.md): between your sessions on this machine only ^([5](#fn5))
- [Zero Data Retention](zero-data-retention.md): subject to your AWS agreement

**Alternatives:** for scheduling, use [`/loop`](scheduled-tasks.md) instead of `/schedule`. For cloud sessions, use [GitHub Actions](github-actions.md) or [GitLab CI/CD](gitlab-ci-cd.md). For web lookups, use the [WebFetch tool](tools-reference.md#webfetch-tool-behavior) with a specific URL.

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription), plus [fast mode](fast-mode.md), [Advisor](advisor.md), [Channels](channels.md), [GitHub Actions](github-actions.md), the [analytics dashboard](../13-Enterprise-Admin/analytics.md), [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md), and the [`/design-sync` and `/import` commands](commands.md#all-commands).**Available where Amazon Bedrock is not:** [web search](tools-reference.md#websearch-tool-behavior).**Partial support:**

- [Cross-session messaging](cross-session-messaging.md): between your sessions on this machine only ^([5](#fn5))

**Alternatives:** for scheduling, use [`/loop`](scheduled-tasks.md) instead of `/schedule`. For cloud sessions, use [GitLab CI/CD](gitlab-ci-cd.md).

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription), plus [fast mode](fast-mode.md), [Advisor](advisor.md), [Channels](channels.md), the [analytics dashboard](../13-Enterprise-Admin/analytics.md), [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md), and the [`/design-sync` and `/import` commands](commands.md#all-commands).**Partial support:**

- [Desktop](../16-Mobile-Desktop/desktop.md): via [managed settings](https://claude.com/docs/third-party/claude-desktop/configuration) or [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview)
- [Web search](tools-reference.md#websearch-tool-behavior): Claude 4 models and later
- [Auto mode](auto-mode-config.md): Sonnet 5 or later, Opus 4.7 or later, and Fable models only
- [Cross-session messaging](cross-session-messaging.md): between your sessions on this machine only ^([5](#fn5))
- [Zero Data Retention](zero-data-retention.md): subject to your Google Cloud agreement

**Alternatives:** for scheduling, use [`/loop`](scheduled-tasks.md) instead of `/schedule`. For cloud sessions, use [GitHub Actions](github-actions.md) or [GitLab CI/CD](gitlab-ci-cd.md).

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription), plus [fast mode](fast-mode.md), [Advisor](advisor.md), [Channels](channels.md), [GitLab CI/CD](gitlab-ci-cd.md), the [analytics dashboard](../13-Enterprise-Admin/analytics.md), [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md), and the [`/design-sync` and `/import` commands](commands.md#all-commands).**Partial support:**

- [Desktop](../16-Mobile-Desktop/desktop.md): only via [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview)
- [Web search](tools-reference.md#websearch-tool-behavior): [deployments hosted on Anthropic](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md#hosting-options) only
- [Auto mode](auto-mode-config.md): Sonnet 5 or later, Opus 4.7 or later, and Fable models only
- [Cross-session messaging](cross-session-messaging.md): between your sessions on this machine only ^([5](#fn5))
- [Zero Data Retention](zero-data-retention.md): subject to your Azure agreement

**Alternatives:** for scheduling, use [`/loop`](scheduled-tasks.md) instead of `/schedule`. For cloud sessions, use [GitHub Actions](github-actions.md).

**Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription).Everything in [CLI capabilities that vary by provider](#cli-capabilities-that-vary-by-provider) is available, except that [fast mode](fast-mode.md) requires [provisioned access](fast-mode.md#enable-fast-mode-for-your-organization). [Server-managed settings](../13-Enterprise-Admin/server-managed-settings.md) are also available when your API key belongs to a Team or Enterprise organization.


[​](#availability-by-subscription-plan)

Availability by subscription plan

If you authenticate through Amazon Bedrock, Google Cloud’s Agent Platform, Microsoft Foundry, or an Anthropic Console API key, this section does not apply to you. When you sign in with a claude.ai account, your plan determines which of the features below are available.

| Feature                                                                     | Pro | Max | Team          | Enterprise     |
|:----------------------------------------------------------------------------|:----|:----|:--------------|:---------------|
| [Cloud sessions](claude-code-on-the-web.md)                           | ✓   | ✓   | ✓             | ✓ ^([6](#fn6)) |
| [Routines](web-scheduled-tasks.md)                                               | ✓   | ✓   | ✓             | ✓              |
| [Remote Control](remote-control.md)                                   | ✓   | ✓   | Admin-enabled | Admin-enabled  |
| [Channels](channels.md)                                               | ✓   | ✓   | Admin-enabled | Admin-enabled  |
| [Computer use](computer-use.md)                                       | ✓   | ✓   | ✗             | ✗              |
| Dispatch ([Desktop](../16-Mobile-Desktop/desktop.md#sessions-from-dispatch))               | ✓   | ✓   | ✗             | ✗              |
| [Code Review](code-review.md)                                         | ✗   | ✗   | ✓             | ✓              |
| [Artifacts](artifacts.md)                                             | ✓   | ✓   | ✓             | Admin-enabled  |
| [Analytics dashboard and contribution metrics](../13-Enterprise-Admin/analytics.md)          | ✗   | ✗   | ✓             | ✓              |
| [Enterprise Analytics API](../13-Enterprise-Admin/analytics.md#access-data-programmatically) | ✗   | ✗   | ✗             | ✓              |
| [Server-managed settings](../13-Enterprise-Admin/server-managed-settings.md)                 | ✗   | ✗   | ✓             | ✓              |
| [SSO](../17-Billing-Plans/what-is-the-team-plan.md) | ✗   | ✗   | ✓             | ✓              |
| SCIM                                                                        | ✗   | ✗   | ✗             | ✓              |
| [Compliance API](../04-API-Reference/Endpoints/http-compliance.md)        | ✗   | ✗   | ✗             | ✓              |
| [Zero Data Retention](zero-data-retention.md)                         | ✗   | ✗   | ✗             | ✓ ^([7](#fn7)) |

⁶ On Enterprise, requires a premium seat or a Chat + Claude Code seat. See [Use Claude Code in the cloud](claude-code-on-the-web.md).  
⁷ Not included in the standard Enterprise plan. Requires separate enablement by Anthropic for qualified accounts. See [Zero Data Retention](zero-data-retention.md). For pricing and the full plan comparison, see [Team plans](../17-Billing-Plans/what-is-the-team-plan.md) and [Enterprise plans](../17-Billing-Plans/what-is-the-enterprise-plan.md).


[​](#model-availability)

Model availability

For which Claude models and context-window sizes are available per provider and region, see [Model configuration](model-config.md) and the [Models overview](../20-Models/about-claude-models-overview.md). Vision, PDF input, and extended thinking are model capabilities rather than Claude Code features and work on every provider that offers the model. [Prompt caching](prompt-caching.md) works the same way on most providers; on Amazon Bedrock, support varies by model.


[​](#related-resources)

Related resources

- [Enterprise deployment overview](third-party-integrations.md): compare authentication, billing, and regions across providers
- Provider setup guides: [Amazon Bedrock](amazon-bedrock.md), [Claude Platform on AWS](claude-platform-on-aws.md), [Google Cloud’s Agent Platform](google-vertex-ai.md), [Microsoft Foundry](microsoft-foundry.md)
- [Platforms and integrations](platforms.md): where Claude Code runs, including the CLI, Desktop, IDE extensions, web, mobile, and CI/CD
