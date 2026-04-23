---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/models"
category: "20-Models"
fetched_at: "2026-03-20T10:35:25Z"
tags: ["api"]
---

# Models

##### [List Models](/docs/en/api/models/list)

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

CapabilitySupport = object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

ContextManagementCapability = object { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }

Context management capability details.

clear_thinking_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear_tool_uses_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

EffortCapability = object { high, low, max, 2 more }

Effort (reasoning_effort) capability details.

high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

ModelCapabilities = object { batch, citations, code_execution, 6 more }

Model capability information.

batch: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code_execution: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context_management: [ContextManagementCapability](/docs/en/api/models#context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }

Context management support and available strategies.

clear_thinking_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear_tool_uses_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: [EffortCapability](/docs/en/api/models#effort_capability) { high, low, max, 2 more }

Effort (reasoning_effort) support and available levels.

high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

image_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured_outputs: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: [ThinkingCapability](/docs/en/api/models#thinking_capability) { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

ModelInfo = object { id, capabilities, created_at, 4 more }

id: string

Unique model identifier.

capabilities: [ModelCapabilities](/docs/en/api/models#model_capabilities) { batch, citations, code_execution, 6 more }

Model capability information.

batch: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code_execution: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context_management: [ContextManagementCapability](/docs/en/api/models#context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }

Context management support and available strategies.

clear_thinking_20251015: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear_tool_uses_20250919: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact_20260112: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: [EffortCapability](/docs/en/api/models#effort_capability) { high, low, max, 2 more }

Effort (reasoning_effort) support and available levels.

high: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

image_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf_input: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured_outputs: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: [ThinkingCapability](/docs/en/api/models#thinking_capability) { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

created_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: string

A human-readable name for the model.

max_input_tokens: number

Maximum input context window size in tokens for this model.

max_tokens: number

Maximum value for the `max_tokens` parameter when using this model.

type: "model"

Object type.

For Models, this is always `"model"`.

ThinkingCapability = object { supported, types }

Thinking capability details.

supported: boolean

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

ThinkingTypes = object { adaptive, enabled }

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.
