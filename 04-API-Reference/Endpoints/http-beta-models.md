---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/models"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:39:10Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Fmodels)

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


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


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

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)

# Models

##### [List Models](http-beta-models-list.md)

GET/v1/models

List available models.

##### [Get a Model](http-beta-models-retrieve.md)

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

summarize: [BetaCapabilitySupport](http-beta-models.md#beta_capability_support) { supported }

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

clear_thinking_20251015: [BetaCapabilitySupport](http-beta-models.md#beta_capability_support) { supported } or null



Whether the clear_thinking_20251015 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



clear_tool_uses_20250919: [BetaCapabilitySupport](http-beta-models.md#beta_capability_support) { supported } or null



Whether the clear_tool_uses_20250919 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



compact_20260112: [BetaCapabilitySupport](http-beta-models.md#beta_capability_support) { supported } or null

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

BetaModelCapabilities object{ batch, citations, code_execution, 7 more }



Model capability information.



BetaModelInfo object{ type: "model", id, allowed_fallback_models, 5 more }





BetaThinkingCapability object{ supported, types }



Thinking capability details.

supported: boolean



Whether this capability is supported by the model.



types: [BetaThinkingTypes](http-beta-models.md#beta_thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](http-beta-models.md#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](http-beta-models.md#beta_capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.



BetaThinkingTypes object{ adaptive, enabled }



Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](http-beta-models.md#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](http-beta-models.md#beta_capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.
