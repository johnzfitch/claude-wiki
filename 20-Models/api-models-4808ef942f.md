---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/models"
category: "20-Models"
fetched_at: "2026-09-26T06:39:16Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fmodels)

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



A beta version of this API exists and may have additional functionality. [View the beta version](/docs/en/api/http/beta/models).

1.  [API reference](/docs/en/api/http)

# Models

##### [List Models](/docs/en/api/http/models/list)

GET/v1/models

List available models.

##### [Get a Model](/docs/en/api/http/models/retrieve)

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

clear_thinking_20251015: [CapabilitySupport](/docs/en/api/http/models#capability_support) { supported } or null



Whether the clear_thinking_20251015 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



clear_tool_uses_20250919: [CapabilitySupport](/docs/en/api/http/models#capability_support) { supported } or null



Whether the clear_tool_uses_20250919 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



compact_20260112: [CapabilitySupport](/docs/en/api/http/models#capability_support) { supported } or null

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

ModelCapabilities object{ batch, citations, code_execution, 6 more }



Model capability information.



ModelInfo object{ type: "model", id, capabilities, 4 more }





type: "model"



Object type.

For Models, this is always `"model"`.

defaultmodel

id: string



Unique model identifier.



capabilities: [ModelCapabilities](/docs/en/api/http/models#model_capabilities) { batch, citations, code_execution, 6 more } or null



Object mapping capability names to their support details. Keys are always present for all known capabilities.



created_at: string



RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

display_name: string



A human-readable name for the model.

max_input_tokens: number or null



Maximum input context window size in tokens for this model.

max_tokens: number or null



Maximum value for the `max_tokens` parameter when using this model.



ThinkingCapability object{ supported, types }



Thinking capability details.

supported: boolean



Whether this capability is supported by the model.



types: [ThinkingTypes](/docs/en/api/http/models#thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [CapabilitySupport](/docs/en/api/http/models#capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.



enabled: [CapabilitySupport](/docs/en/api/http/models#capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.



ThinkingTypes object{ adaptive, enabled }



Supported thinking type configurations.



adaptive: [CapabilitySupport](/docs/en/api/http/models#capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.



enabled: [CapabilitySupport](/docs/en/api/http/models#capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.
