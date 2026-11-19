---
title: "Run Claude Code through a gateway - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/gateways"
category: "13-Enterprise-Admin"
fetched_at: "2026-11-13T06:33:35Z"
last_modified: "Fri, 13 Nov 2026 06:21:52 GMT"
tags: ["claude-code", "enterprise"]
---

## On this page

Back to top

- [How a gateway works](#how-a-gateway-works)
- [Choose a gateway](#choose-a-gateway)
  - [Claude apps gateway](#claude-apps-gateway)
  - [Other gateways](#other-gateways)
- [Subscriptions and gateways](#subscriptions-and-gateways)
- [Configure separately from the gateway](#configure-separately-from-the-gateway)
- [Next steps](#next-steps)

Gateways

# Run Claude Code through a gateway

Copy pageCopy page

Route Claude Code through a self-hosted gateway for centralized credentials, usage tracking, and cost controls. Covers the architecture, Anthropic’s Claude apps gateway, and using other gateway products.

Copy pageCopy page

A gateway is a proxy your organization runs between Claude Code and a model provider. Claude Code sends API traffic to the gateway instead of directly to the provider, and the gateway forwards it using a credential your organization holds. Developers authenticate to the gateway rather than holding provider credentials, so authentication, usage tracking, budgets, and audit logging happen in one place you control. Claude Code includes a self-hosted gateway, [Claude apps gateway](claude-apps-gateway.md), in the `claude` binary, so you don’t have to adopt a separate gateway product to run one. If your organization already runs an [LLM gateway](llm-gateway.md), Claude Code works with that too. This page covers:

- [How a gateway sits between Claude Code and your provider](#how-a-gateway-works)
- [Choosing between Claude apps gateway and a gateway you already run](#choose-a-gateway)
- [How gateways interact with claude.ai subscriptions](#subscriptions-and-gateways)
- [What’s configured separately from the gateway](#configure-separately-from-the-gateway)


[​](#how-a-gateway-works)

How a gateway works

Each developer’s Claude Code sends its requests to the gateway’s address and authenticates with a gateway-issued credential. The gateway authenticates the developer, applies whatever access and budget rules you configure, and forwards the request to your provider with the organization’s credential. The provider can be Anthropic’s API or a [cloud provider](../02-Claude-Code-CLI/third-party-integrations.md) such as Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry; the gateway’s configuration decides. With Claude apps gateway, or another gateway that exposes a single Anthropic-format endpoint, changing provider doesn’t require touching developer machines.

Two kinds of credential are involved:

- **Developer credential**: each developer holds their own, issued by the gateway. It authenticates them to the gateway and identifies them in usage tracking
- **Provider credential**: the gateway holds one credential for your provider account, shared by all forwarded traffic


[​](#choose-a-gateway)

Choose a gateway

Claude Code works with Anthropic’s own gateway or with a gateway your organization already runs.


[​](#claude-apps-gateway)

Claude apps gateway

Claude apps gateway is Anthropic’s self-hosted gateway, included in the `claude` binary. It routes to Amazon Bedrock, Claude Platform on AWS, Google Cloud, Microsoft Foundry, or the Anthropic API as the upstream. Developers sign in with your corporate identity provider through `/login`, the gateway enforces model access and [managed settings](managed-settings.md) by IdP group, and it emits [OpenTelemetry Protocol (OTLP)](monitoring-usage.md) usage metrics to your own observability stack. Because it is built and tested alongside each Claude Code release, it forwards the `anthropic-beta` values and request fields Claude Code sends. A gateway maintained separately needs its [forwarding rules updated](llm-gateway-protocol.md#forward-as-open-lists) as those change with each release; Claude apps gateway releases with the CLI, so there is no list to keep current. See [Availability and limitations](claude-apps-gateway.md#availability-and-limitations) for the small set of features that behave differently on a gateway session. The gateway sign-in is a browser SSO step, and there is no service-token flow, so a CI pipeline with no developer to approve the sign-in can’t authenticate through it; configure those against your provider directly. Agent SDK sessions and `claude -p` runs on a machine where a developer has signed in use that machine’s gateway session and are governed by its policies. See [CI pipelines and remote machines](claude-apps-gateway.md#ci-pipelines-and-remote-machines). See [Claude apps gateway](claude-apps-gateway.md) to deploy it.


[​](#other-gateways)

Other gateways

If your organization already runs an LLM gateway or API gateway, you can use it instead. Anthropic doesn’t endorse, maintain, or audit other gateway products, and doesn’t support routing Claude Code to non-Claude models through any gateway. See [Other LLM gateways](llm-gateway.md) for the admin rollout checklist, what a gateway must implement, and how to point Claude Code at it.


[​](#subscriptions-and-gateways)

Subscriptions and gateways

When developers connect through a gateway with a gateway credential, usage is billed to your organization’s provider account at API rates, and their claude.ai subscriptions aren’t used or charged. Every request forwarded under that credential is charged to the account behind the gateway’s provider credential. The exception is setting only `ANTHROPIC_BASE_URL`, with no gateway credential. Requests still route through the gateway, but a saved claude.ai login stays the active credential, so the subscription’s usage limits and billing apply. [Other LLM gateways](llm-gateway.md#subscriptions-and-gateways) covers that configuration and what the gateway has to forward for it to work.


[​](#configure-separately-from-the-gateway)

Configure separately from the gateway

A gateway routes model API requests. A few things you might expect it to handle are configured elsewhere:

- **Which model answers**: pick the model with the `/model` command or [model environment variables](../02-Claude-Code-CLI/model-config.md#setting-your-model). The gateway decides where requests go, not which model the developer selects. Claude apps gateway can bound the choice with a per-group `availableModels` allowlist, but the developer still picks within it.
- **Other network traffic**: Claude Code itself sends version checks and downloads directly to Anthropic, separate from the gateway path. Your network still needs egress to the [required domains](network-config.md), or set [`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`](../02-Claude-Code-CLI/env-vars.md) to turn off the optional streams.
- **Client telemetry**: Claude Code disables its Anthropic-bound client analytics when a session signs in to a Claude apps gateway. To keep pre-sign-in startup analytics off as well, deliver [`DISABLE_TELEMETRY`](managed-settings.md#turn-telemetry-off-for-your-organization) in the [client-side managed settings](claude-apps-gateway-config.md#client-side-managed-settings) on each device.
- **Client telemetry on other gateways**: whether Claude Code sends the optional client telemetry stream depends on your provider, and the [telemetry defaults table](data-usage.md#default-behaviors-by-api-provider) covers each case.
- **Telemetry destinations**: where Claude Code sends a gateway session’s telemetry depends on how the session signed in, and [What’s enforced on developers](claude-apps-gateway.md#whats-enforced-on-developers) says where each kind of session’s exports go.
- **Corporate HTTP proxies**: Claude Code sends its requests, including those to the gateway, through the proxy in `HTTPS_PROXY`. If your network requires a proxy, [configure it](network-config.md). If the proxy applies to a Claude apps gateway you host, [sign-in](claude-apps-gateway.md#prerequisites) needs the proxy’s hostname to resolve to private addresses, or the gateway host in `NO_PROXY`.


[​](#next-steps)

Next steps

The next page depends on who runs the gateway. Anthropic’s gateway runs from the `claude` binary and has its own setup guide; a gateway your organization already runs has a compatibility guide to follow and an admin rollout checklist.

- [Claude apps gateway](claude-apps-gateway.md) to deploy Anthropic’s self-hosted gateway with SSO sign-in and OTLP telemetry
- [Other LLM gateways](llm-gateway.md) for what a gateway your organization already runs must implement, and how to point Claude Code at it
- [Set up Claude Code for your organization](admin-setup.md) for the wider rollout decisions a gateway is one part of
