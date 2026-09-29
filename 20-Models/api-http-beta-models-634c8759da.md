---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/models"
category: "20-Models"
fetched_at: "2026-09-26T06:39:10Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Fmodels)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)

# Models

##### [List Models](/docs/en/api/http/beta/models/list)

GET/v1/models

List available models.

##### [Get a Model](/docs/en/api/http/beta/models/retrieve)

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

summarize: [BetaCapabilitySupport](/docs/en/api/http/beta/models#beta_capability_support) { supported }

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

clear_thinking_20251015: [BetaCapabilitySupport](/docs/en/api/http/beta/models#beta_capability_support) { supported } or null



Whether the clear_thinking_20251015 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



clear_tool_uses_20250919: [BetaCapabilitySupport](/docs/en/api/http/beta/models#beta_capability_support) { supported } or null



Whether the clear_tool_uses_20250919 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



compact_20260112: [BetaCapabilitySupport](/docs/en/api/http/beta/models#beta_capability_support) { supported } or null

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

types: [BetaThinkingTypes](/docs/en/api/http/beta/models#beta_thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](/docs/en/api/http/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](/docs/en/api/http/beta/models#beta_capability_support) { supported }

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

adaptive: [BetaCapabilitySupport](/docs/en/api/http/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](/docs/en/api/http/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.
