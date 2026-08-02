---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/models"
category: "20-Models"
fetched_at: "2026-08-02T05:40:21Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Models




cURL



A beta version of this API exists and may have additional functionality. [View the beta version](/docs/en/api/beta/models).

# Models

##### [List Models](/docs/en/api/models/list)

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 



CapabilitySupport object { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#capability_support.supported)

[](#capability_support)



ContextManagementCapability object { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management capability details.



clear_thinking_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.clear_thinking_20251015%20%2B%20(resource)%20models.supported)

[](#context_management_capability.clear_thinking_20251015)



clear_tool_uses_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.clear_tool_uses_20250919%20%2B%20(resource)%20models.supported)

[](#context_management_capability.clear_tool_uses_20250919)



compact_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.compact_20260112%20%2B%20(resource)%20models.supported)

[](#context_management_capability.compact_20260112)

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.supported)

[](#context_management_capability)



EffortCapability object { high, low, max, 3 more }



Effort (reasoning_effort) capability details.



high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports high effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.high%20%2B%20(resource)%20models.supported)

[](#effort_capability.high)



low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports low effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.low%20%2B%20(resource)%20models.supported)

[](#effort_capability.low)



max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports max effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.max%20%2B%20(resource)%20models.supported)

[](#effort_capability.max)



medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports medium effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.medium%20%2B%20(resource)%20models.supported)

[](#effort_capability.medium)

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.supported)



xhigh: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.xhigh%20%2B%20(resource)%20models.supported)

[](#effort_capability.xhigh)

[](#effort_capability)



ModelCapabilities object { batch, citations, code_execution, 6 more }



Model capability information.



batch: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports the Batch API.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.batch%20%2B%20(resource)%20models.supported)

[](#model_capabilities.batch)



citations: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports citation generation.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.citations%20%2B%20(resource)%20models.supported)

[](#model_capabilities.citations)



code_execution: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports code execution tools.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.code_execution%20%2B%20(resource)%20models.supported)

[](#model_capabilities.code_execution)



context_management: [ContextManagementCapability](/docs/en/api/models#context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management support and available strategies.



clear_thinking_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.clear_thinking_20251015%20%2B%20(resource)%20models.supported)

[](#model_capabilities.context_management%20%2B%20(resource)%20models.clear_thinking_20251015)



clear_tool_uses_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.clear_tool_uses_20250919%20%2B%20(resource)%20models.supported)

[](#model_capabilities.context_management%20%2B%20(resource)%20models.clear_tool_uses_20250919)



compact_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.compact_20260112%20%2B%20(resource)%20models.supported)

[](#model_capabilities.context_management%20%2B%20(resource)%20models.compact_20260112)

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.context_management%20%2B%20(resource)%20models.supported)

[](#model_capabilities.context_management)



effort: [EffortCapability](/docs/en/api/models#effort_capability) { high, low, max, 3 more }



Effort (reasoning_effort) support and available levels.



high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports high effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.high%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.high)



low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports low effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.low%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.low)



max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports max effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.max%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.max)



medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports medium effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.medium%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.medium)

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.effort%20%2B%20(resource)%20models.supported)



xhigh: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.xhigh%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.xhigh)

[](#model_capabilities.effort)



image_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model accepts image content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.image_input%20%2B%20(resource)%20models.supported)

[](#model_capabilities.image_input)



pdf_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model accepts PDF content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.pdf_input%20%2B%20(resource)%20models.supported)

[](#model_capabilities.pdf_input)



structured_outputs: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.structured_outputs%20%2B%20(resource)%20models.supported)

[](#model_capabilities.structured_outputs)



thinking: [ThinkingCapability](/docs/en/api/models#thinking_capability) { supported, types }



Thinking capability and supported type configurations.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.thinking%20%2B%20(resource)%20models.supported)



types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#thinking_types.adaptive%20%2B%20(resource)%20models.supported)

[](#thinking_capability.types%20%2B%20(resource)%20models.adaptive)



enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#thinking_types.enabled%20%2B%20(resource)%20models.supported)

[](#thinking_capability.types%20%2B%20(resource)%20models.enabled)

[](#model_capabilities.thinking%20%2B%20(resource)%20models.types)

[](#model_capabilities.thinking)

[](#model_capabilities)



ModelInfo object { id, capabilities, created_at, 4 more }



id: string



Unique model identifier.

[](#model_info.id)



capabilities: [ModelCapabilities](/docs/en/api/models#model_capabilities) { batch, citations, code_execution, 6 more }



Model capability information.



batch: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports the Batch API.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.batch%20%2B%20(resource)%20models.supported)

[](#model_info.capabilities%20%2B%20(resource)%20models.batch)



citations: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports citation generation.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.citations%20%2B%20(resource)%20models.supported)

[](#model_info.capabilities%20%2B%20(resource)%20models.citations)



code_execution: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports code execution tools.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.code_execution%20%2B%20(resource)%20models.supported)

[](#model_info.capabilities%20%2B%20(resource)%20models.code_execution)



context_management: [ContextManagementCapability](/docs/en/api/models#context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management support and available strategies.



clear_thinking_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.clear_thinking_20251015%20%2B%20(resource)%20models.supported)

[](#model_capabilities.context_management%20%2B%20(resource)%20models.clear_thinking_20251015)



clear_tool_uses_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.clear_tool_uses_20250919%20%2B%20(resource)%20models.supported)

[](#model_capabilities.context_management%20%2B%20(resource)%20models.clear_tool_uses_20250919)



compact_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#context_management_capability.compact_20260112%20%2B%20(resource)%20models.supported)

[](#model_capabilities.context_management%20%2B%20(resource)%20models.compact_20260112)

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.context_management%20%2B%20(resource)%20models.supported)

[](#model_info.capabilities%20%2B%20(resource)%20models.context_management)



effort: [EffortCapability](/docs/en/api/models#effort_capability) { high, low, max, 3 more }



Effort (reasoning_effort) support and available levels.



high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports high effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.high%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.high)



low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports low effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.low%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.low)



max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports max effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.max%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.max)



medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports medium effort level.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.medium%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.medium)

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.effort%20%2B%20(resource)%20models.supported)



xhigh: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#effort_capability.xhigh%20%2B%20(resource)%20models.supported)

[](#model_capabilities.effort%20%2B%20(resource)%20models.xhigh)

[](#model_info.capabilities%20%2B%20(resource)%20models.effort)



image_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model accepts image content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.image_input%20%2B%20(resource)%20models.supported)

[](#model_info.capabilities%20%2B%20(resource)%20models.image_input)



pdf_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model accepts PDF content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.pdf_input%20%2B%20(resource)%20models.supported)

[](#model_info.capabilities%20%2B%20(resource)%20models.pdf_input)



structured_outputs: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.structured_outputs%20%2B%20(resource)%20models.supported)

[](#model_info.capabilities%20%2B%20(resource)%20models.structured_outputs)



thinking: [ThinkingCapability](/docs/en/api/models#thinking_capability) { supported, types }



Thinking capability and supported type configurations.

supported: boolean



Whether this capability is supported by the model.

[](#model_capabilities.thinking%20%2B%20(resource)%20models.supported)



types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#thinking_types.adaptive%20%2B%20(resource)%20models.supported)

[](#thinking_capability.types%20%2B%20(resource)%20models.adaptive)



enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#thinking_types.enabled%20%2B%20(resource)%20models.supported)

[](#thinking_capability.types%20%2B%20(resource)%20models.enabled)

[](#model_capabilities.thinking%20%2B%20(resource)%20models.types)

[](#model_info.capabilities%20%2B%20(resource)%20models.thinking)

[](#model_info.capabilities)

created_at: string



RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

[](#model_info.created_at)

display_name: string



A human-readable name for the model.

[](#model_info.display_name)

max_input_tokens: number



Maximum input context window size in tokens for this model.

[](#model_info.max_input_tokens)

max_tokens: number



Maximum value for the `max_tokens` parameter when using this model.

[](#model_info.max_tokens)



type: "model"



Object type.

For Models, this is always `"model"`.

[](#model_info.type)

[](#model_info)



ThinkingCapability object { supported, types }



Thinking capability details.

supported: boolean



Whether this capability is supported by the model.

[](#thinking_capability.supported)



types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#thinking_types.adaptive%20%2B%20(resource)%20models.supported)

[](#thinking_capability.types%20%2B%20(resource)%20models.adaptive)



enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#thinking_types.enabled%20%2B%20(resource)%20models.supported)

[](#thinking_capability.types%20%2B%20(resource)%20models.enabled)

[](#thinking_capability.types)

[](#thinking_capability)



ThinkingTypes object { adaptive, enabled }



Supported thinking type configurations.



adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#thinking_types.adaptive%20%2B%20(resource)%20models.supported)

[](#thinking_types.adaptive)



enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#thinking_types.enabled%20%2B%20(resource)%20models.supported)

[](#thinking_types.enabled)
