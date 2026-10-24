---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/models"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-20T06:37:39Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fmodels)

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



A beta version of this API exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-models.md).

1.  [API reference](http.md)

# Models

Copy page



cURL

##### [List Models](https://platform.claude.com/docs/en/api/http/models/list)

GET/v1/models

List available models.

##### [Get a Model](https://platform.claude.com/docs/en/api/http/models/retrieve)

GET/v1/models/{model_id}

Get a specific model.

##### Models



CapabilitySupport object{ supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.



ContextManagementCapability object{ clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management capability details.



clear_thinking_20251015: [CapabilitySupport](https://platform.claude.com/docs/en/api/http/models#capability_support) { supported } or null



Whether the clear_thinking_20251015 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



clear_tool_uses_20250919: [CapabilitySupport](https://platform.claude.com/docs/en/api/http/models#capability_support) { supported } or null



Whether the clear_tool_uses_20250919 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



compact_20260112: [CapabilitySupport](https://platform.claude.com/docs/en/api/http/models#capability_support) { supported } or null



Whether the compact_20260112 strategy is supported.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



EffortCapability object{ high, low, max, 3 more }



Effort (reasoning_effort) capability details.



ModelCapabilities object{ batch, citations, code_execution, 7 more }



Model capability information.



ModelInfo object{ type: "model", id, capabilities, 8 more }





ModelLine = "haiku" or "sonnet" or "opus" or 2 more

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

ServerToolsCapability object{ code_execution, supported, web_search }



Web search and code execution tool support, with one entry per tool.



code_execution: [CapabilitySupport](https://platform.claude.com/docs/en/api/http/models#capability_support) { supported }



Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



web_search: [CapabilitySupport](https://platform.claude.com/docs/en/api/http/models#capability_support) { supported }



Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

supported: boolean



Whether this capability is supported by the model.



ThinkingCapability object{ supported, types }



Thinking capability details.

supported: boolean



Whether this capability is supported by the model.



types: [ThinkingTypes](https://platform.claude.com/docs/en/api/http/models#thinking_types) { adaptive, between_tools, disabled, enabled }



Supported thinking type configurations.



ThinkingTypes object{ adaptive, between_tools, disabled, enabled }



Which `thinking.type` values the model accepts on requests. Read each key on its own: for example, `enabled` can be false while `disabled` is true.
