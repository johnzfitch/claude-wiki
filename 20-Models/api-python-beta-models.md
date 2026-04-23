---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/python/beta/models"
category: "20-Models"
fetched_at: "2026-03-20T10:35:35Z"
tags: ["api"]
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

beta.models.list(ModelListParams\*\*kwargs) -\> SyncPage\[[BetaModelInfo](/docs/en/api/beta#beta_model_info)\]

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

beta.models.retrieve(strmodel_id, ModelRetrieveParams\*\*kwargs) -\> [BetaModelInfo](/docs/en/api/beta#beta_model_info)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class BetaCapabilitySupport: …

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

class BetaContextManagementCapability: …

Context management capability details.

clear_thinking_20251015: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear_tool_uses_20250919: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact_20260112: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class BetaEffortCapability: …

Effort (reasoning_effort) capability details.

high: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class BetaModelCapabilities: …

Model capability information.

batch: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code_execution: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context_management: [BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability)

Context management support and available strategies.

clear_thinking_20251015: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear_tool_uses_20250919: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact_20260112: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [BetaEffortCapability](/docs/en/api/beta#beta_effort_capability)

Effort (reasoning_effort) support and available levels.

high: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

image_input: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf_input: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured_outputs: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability)

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types)

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class BetaModelInfo: …

id: str

Unique model identifier.

capabilities: Optional\[BetaModelCapabilities\]

Model capability information.

batch: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code_execution: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context_management: [BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability)

Context management support and available strategies.

clear_thinking_20251015: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear_tool_uses_20250919: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact_20260112: Optional\[BetaCapabilitySupport\]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [BetaEffortCapability](/docs/en/api/beta#beta_effort_capability)

Effort (reasoning_effort) support and available levels.

high: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

image_input: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf_input: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured_outputs: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability)

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types)

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

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

class BetaThinkingCapability: …

Thinking capability details.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types)

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class BetaThinkingTypes: …

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.
