---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/models"
category: "20-Models"
fetched_at: "2026-08-02T05:40:07Z"
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

# Models

##### [List Models](/docs/en/api/beta/models/list)

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 



BetaCapabilitySupport object { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_capability_support.supported)

[](#beta_capability_support)



BetaContextManagementCapability object { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management capability details.



clear_thinking_20251015: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.clear_thinking_20251015%20%2B%20(resource)%20beta.models.supported)

[](#beta_context_management_capability.clear_thinking_20251015)



clear_tool_uses_20250919: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.clear_tool_uses_20250919%20%2B%20(resource)%20beta.models.supported)

[](#beta_context_management_capability.clear_tool_uses_20250919)



compact_20260112: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.compact_20260112%20%2B%20(resource)%20beta.models.supported)

[](#beta_context_management_capability.compact_20260112)

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.supported)

[](#beta_context_management_capability)



BetaEffortCapability object { high, low, max, 3 more }



Effort (reasoning_effort) capability details.



high: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports high effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.high%20%2B%20(resource)%20beta.models.supported)

[](#beta_effort_capability.high)



low: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports low effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.low%20%2B%20(resource)%20beta.models.supported)

[](#beta_effort_capability.low)



max: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports max effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.max%20%2B%20(resource)%20beta.models.supported)

[](#beta_effort_capability.max)



medium: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports medium effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.medium%20%2B%20(resource)%20beta.models.supported)

[](#beta_effort_capability.medium)

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.supported)



xhigh: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.xhigh%20%2B%20(resource)%20beta.models.supported)

[](#beta_effort_capability.xhigh)

[](#beta_effort_capability)



BetaModelCapabilities object { batch, citations, code_execution, 6 more }



Model capability information.



batch: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports the Batch API.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.batch%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.batch)



citations: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports citation generation.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.citations%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.citations)



code_execution: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports code execution tools.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.code_execution%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.code_execution)



context_management: [BetaContextManagementCapability](/docs/en/api/beta/models#beta_context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management support and available strategies.



clear_thinking_20251015: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.clear_thinking_20251015%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.clear_thinking_20251015)



clear_tool_uses_20250919: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.clear_tool_uses_20250919%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.clear_tool_uses_20250919)



compact_20260112: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.compact_20260112%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.compact_20260112)

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management)



effort: [BetaEffortCapability](/docs/en/api/beta/models#beta_effort_capability) { high, low, max, 3 more }



Effort (reasoning_effort) support and available levels.



high: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports high effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.high%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.high)



low: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports low effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.low%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.low)



max: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports max effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.max%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.max)



medium: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports medium effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.medium%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.medium)

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.supported)



xhigh: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.xhigh%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.xhigh)

[](#beta_model_capabilities.effort)



image_input: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model accepts image content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.image_input%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.image_input)



pdf_input: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model accepts PDF content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.pdf_input%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.pdf_input)



structured_outputs: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.structured_outputs%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.structured_outputs)



thinking: [BetaThinkingCapability](/docs/en/api/beta/models#beta_thinking_capability) { supported, types }



Thinking capability and supported type configurations.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.thinking%20%2B%20(resource)%20beta.models.supported)



types: [BetaThinkingTypes](/docs/en/api/beta/models#beta_thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.adaptive%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_capability.types%20%2B%20(resource)%20beta.models.adaptive)



enabled: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.enabled%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_capability.types%20%2B%20(resource)%20beta.models.enabled)

[](#beta_model_capabilities.thinking%20%2B%20(resource)%20beta.models.types)

[](#beta_model_capabilities.thinking)

[](#beta_model_capabilities)



BetaModelInfo object { id, allowed_fallback_models, capabilities, 5 more }



id: string



Unique model identifier.

[](#beta_model_info.id)

allowed_fallback_models: array of string



Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

[](#beta_model_info.allowed_fallback_models)



capabilities: [BetaModelCapabilities](/docs/en/api/beta/models#beta_model_capabilities) { batch, citations, code_execution, 6 more }



Model capability information.



batch: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports the Batch API.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.batch%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.batch)



citations: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports citation generation.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.citations%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.citations)



code_execution: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports code execution tools.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.code_execution%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.code_execution)



context_management: [BetaContextManagementCapability](/docs/en/api/beta/models#beta_context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management support and available strategies.



clear_thinking_20251015: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.clear_thinking_20251015%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.clear_thinking_20251015)



clear_tool_uses_20250919: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.clear_tool_uses_20250919%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.clear_tool_uses_20250919)



compact_20260112: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.compact_20260112%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.compact_20260112)

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.context_management)



effort: [BetaEffortCapability](/docs/en/api/beta/models#beta_effort_capability) { high, low, max, 3 more }



Effort (reasoning_effort) support and available levels.



high: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports high effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.high%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.high)



low: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports low effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.low%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.low)



max: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports max effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.max%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.max)



medium: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports medium effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.medium%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.medium)

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.supported)



xhigh: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.xhigh%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.xhigh)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.effort)



image_input: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model accepts image content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.image_input%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.image_input)



pdf_input: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model accepts PDF content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.pdf_input%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.pdf_input)



structured_outputs: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.structured_outputs%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.structured_outputs)



thinking: [BetaThinkingCapability](/docs/en/api/beta/models#beta_thinking_capability) { supported, types }



Thinking capability and supported type configurations.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.thinking%20%2B%20(resource)%20beta.models.supported)



types: [BetaThinkingTypes](/docs/en/api/beta/models#beta_thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.adaptive%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_capability.types%20%2B%20(resource)%20beta.models.adaptive)



enabled: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.enabled%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_capability.types%20%2B%20(resource)%20beta.models.enabled)

[](#beta_model_capabilities.thinking%20%2B%20(resource)%20beta.models.types)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.thinking)

[](#beta_model_info.capabilities)

created_at: string



RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

[](#beta_model_info.created_at)

display_name: string



A human-readable name for the model.

[](#beta_model_info.display_name)

max_input_tokens: number



Maximum input context window size in tokens for this model.

[](#beta_model_info.max_input_tokens)

max_tokens: number



Maximum value for the `max_tokens` parameter when using this model.

[](#beta_model_info.max_tokens)



type: "model"



Object type.

For Models, this is always `"model"`.

[](#beta_model_info.type)

[](#beta_model_info)



BetaThinkingCapability object { supported, types }



Thinking capability details.

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_capability.supported)



types: [BetaThinkingTypes](/docs/en/api/beta/models#beta_thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.adaptive%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_capability.types%20%2B%20(resource)%20beta.models.adaptive)



enabled: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.enabled%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_capability.types%20%2B%20(resource)%20beta.models.enabled)

[](#beta_thinking_capability.types)

[](#beta_thinking_capability)



BetaThinkingTypes object { adaptive, enabled }



Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.adaptive%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_types.adaptive)



enabled: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.enabled%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_types.enabled)
