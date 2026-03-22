---
category: "20-Models"
fetched_at: "2026-03-20T10:36:06Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

client.beta.models.list(ModelListParams { after_id, before_id, limit, betas } params?, RequestOptionsoptions?): Page\<[BetaModelInfo](/docs/en/api/beta#beta_model_info) { id, capabilities, created_at, 4 more } \>

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

client.beta.models.retrieve(stringmodelID, ModelRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaModelInfo](/docs/en/api/beta#beta_model_info) { id, capabilities, created_at, 4 more }

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

BetaCapabilitySupport { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

BetaContextManagementCapability { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }

Context management capability details.

clear_thinking_20251015: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear_tool_uses_20250919: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact_20260112: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

BetaEffortCapability { high, low, max, 2 more }

Effort (reasoning_effort) capability details.

high: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

BetaModelCapabilities { batch, citations, code_execution, 6 more }

Model capability information.

batch: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code_execution: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context_management: [BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }

Context management support and available strategies.

clear_thinking_20251015: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear_tool_uses_20250919: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact_20260112: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: [BetaEffortCapability](/docs/en/api/beta#beta_effort_capability) { high, low, max, 2 more }

Effort (reasoning_effort) support and available levels.

high: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

image_input: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf_input: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured_outputs: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: [BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability) { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

BetaModelInfo { id, capabilities, created_at, 4 more }

id: string

Unique model identifier.

capabilities: [BetaModelCapabilities](/docs/en/api/beta#beta_model_capabilities) { batch, citations, code_execution, 6 more } \| null

Model capability information.

batch: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code_execution: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context_management: [BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }

Context management support and available strategies.

clear_thinking_20251015: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear_tool_uses_20250919: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact_20260112: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported } \| null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: [BetaEffortCapability](/docs/en/api/beta#beta_effort_capability) { high, low, max, 2 more }

Effort (reasoning_effort) support and available levels.

high: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

image_input: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf_input: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured_outputs: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: [BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability) { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

created_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: string

A human-readable name for the model.

max_input_tokens: number \| null

Maximum input context window size in tokens for this model.

max_tokens: number \| null

Maximum value for the `max_tokens` parameter when using this model.

type: "model"

Object type.

For Models, this is always `"model"`.

BetaThinkingCapability { supported, types }

Thinking capability details.

supported: boolean

Whether this capability is supported by the model.

types: [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

BetaThinkingTypes { adaptive, enabled }

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.
