---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/python/models"
category: "20-Models"
fetched_at: "2026-03-20T10:35:40Z"
tags: ["api"]
---

# Models

##### [List Models](/docs/en/api/models/list)

models.list(ModelListParams\*\*kwargs) -\> SyncPage\[[ModelInfo](/docs/en/api/models#model_info)\]

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

models.retrieve(strmodel_id, ModelRetrieveParams\*\*kwargs) -\> [ModelInfo](/docs/en/api/models#model_info)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class CapabilitySupport: …

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

class ContextManagementCapability: …

Context management capability details.

clear_thinking_20251015: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear_tool_uses_20250919: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact_20260112: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class EffortCapability: …

Effort (reasoning_effort) capability details.

high: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class ModelCapabilities: …

Model capability information.

batch: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code_execution: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context_management: [ContextManagementCapability](/docs/en/api/models#context_management_capability)

Context management support and available strategies.

clear_thinking_20251015: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear_tool_uses_20250919: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact_20260112: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [EffortCapability](/docs/en/api/models#effort_capability)

Effort (reasoning_effort) support and available levels.

high: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

image_input: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf_input: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured_outputs: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [ThinkingCapability](/docs/en/api/models#thinking_capability)

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types)

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class ModelInfo: …

id: str

Unique model identifier.

capabilities: Optional\[ModelCapabilities\]

Model capability information.

batch: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code_execution: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context_management: [ContextManagementCapability](/docs/en/api/models#context_management_capability)

Context management support and available strategies.

clear_thinking_20251015: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear_tool_uses_20250919: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact_20260112: Optional\[CapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [EffortCapability](/docs/en/api/models#effort_capability)

Effort (reasoning_effort) support and available levels.

high: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

image_input: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf_input: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured_outputs: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [ThinkingCapability](/docs/en/api/models#thinking_capability)

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types)

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

created_at: datetime

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: str

A human-readable name for the model.

max_input_tokens: Optional\[int\]

Maximum input context window size in tokens for this model.

max_tokens: Optional\[int\]

Maximum value for the `max_tokens` parameter when using this model.

type: Literal\["model"\]

Object type.

For Models, this is always `"model"`.

class ThinkingCapability: …

Thinking capability details.

supported: bool

Whether this capability is supported by the model.

types: [ThinkingTypes](/docs/en/api/models#thinking_types)

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class ThinkingTypes: …

Supported thinking type configurations.

adaptive: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.
