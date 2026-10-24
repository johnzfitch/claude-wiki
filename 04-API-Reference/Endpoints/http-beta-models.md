---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/models"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-20T06:38:31Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmodels)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# Models

Copy page



cURL

##### [List Models](platform-claude-com-http-beta-models-list.md)

GET/v1/models

List available models.

##### [Get a Model](platform-claude-com-http-beta-models-retrieve.md)

GET/v1/models/{model_id}

Get a specific model.

##### Models



BetaCapabilitySupport object{ supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.



BetaCompactionCapability object{ summarize, supported }



Compaction capability details: whether the model accepts the top-level `compaction` request parameter, with one entry per supported `compaction.type` value.



summarize: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported }



Whether the summarize compaction type is supported.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



BetaContextManagementCapability object{ clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management capability details.



clear_thinking_20251015: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported } or null



Whether the clear_thinking_20251015 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



clear_tool_uses_20250919: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported } or null



Whether the clear_tool_uses_20250919 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



compact_20260112: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported } or null



Whether the compact_20260112 strategy is supported.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



BetaEffortCapability object{ high, low, max, 3 more }



Effort (reasoning_effort) capability details.



BetaModelCapabilities object{ batch, citations, code_execution, 8 more }



Model capability information.



BetaModelInfo object{ type: "model", id, allowed_fallback_models, 9 more }





BetaModelLine = "haiku" or "sonnet" or "opus" or 2 more



A Claude model line, such as `opus` or `sonnet`. More lines may be added as new values.

One of the following:

"haiku"



"sonnet"



"opus"



"fable"



"mythos"





BetaServerToolsCapability object{ code_execution, supported, web_search }



Web search and code execution tool support, with one entry per tool.



code_execution: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported }



Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



web_search: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported }



Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

supported: boolean



Whether this capability is supported by the model.



BetaThinkingCapability object{ supported, types }



Thinking capability details.

supported: boolean



Whether this capability is supported by the model.



types: [BetaThinkingTypes](platform-claude-com-http-beta-models.md#beta_thinking_types) { adaptive, between_tools, disabled, enabled }



Supported thinking type configurations.



BetaThinkingTypes object{ adaptive, between_tools, disabled, enabled }



Which `thinking.type` values the model accepts on requests. Read each key on its own: for example, `enabled` can be false while `disabled` is true.
