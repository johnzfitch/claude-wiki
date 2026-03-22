---
category: "20-Models"
fetched_at: "2026-03-20T10:35:04Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

client.Beta.Models.List(ctx, params) (\*Page\[[BetaModelInfo](/docs/en/api/beta#beta_model_info)\], error)

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

client.Beta.Models.Get(ctx, modelID, query) (\*[BetaModelInfo](/docs/en/api/beta#beta_model_info), error)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

type BetaCapabilitySupport struct{…}

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

type BetaContextManagementCapability struct{…}

Context management capability details.

ClearThinking20251015 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

type BetaEffortCapability struct{…}

Effort (reasoning_effort) capability details.

High [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

type BetaModelCapabilities struct{…}

Model capability information.

Batch [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports the Batch API.

Supported bool

Whether this capability is supported by the model.

Citations [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports citation generation.

Supported bool

Whether this capability is supported by the model.

CodeExecution [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports code execution tools.

Supported bool

Whether this capability is supported by the model.

ContextManagement [BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability)

Context management support and available strategies.

ClearThinking20251015 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Effort [BetaEffortCapability](/docs/en/api/beta#beta_effort_capability)

Effort (reasoning_effort) support and available levels.

High [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

ImageInput [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model accepts image content blocks.

Supported bool

Whether this capability is supported by the model.

PDFInput [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model accepts PDF content blocks.

Supported bool

Whether this capability is supported by the model.

StructuredOutputs [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports structured output / JSON mode / strict tool schemas.

Supported bool

Whether this capability is supported by the model.

Thinking [BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability)

Thinking capability and supported type configurations.

Supported bool

Whether this capability is supported by the model.

Types [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types)

Supported thinking type configurations.

Adaptive [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

type BetaModelInfo struct{…}

ID string

Unique model identifier.

Capabilities [BetaModelCapabilities](/docs/en/api/beta#beta_model_capabilities)

Model capability information.

Batch [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports the Batch API.

Supported bool

Whether this capability is supported by the model.

Citations [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports citation generation.

Supported bool

Whether this capability is supported by the model.

CodeExecution [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports code execution tools.

Supported bool

Whether this capability is supported by the model.

ContextManagement [BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability)

Context management support and available strategies.

ClearThinking20251015 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Effort [BetaEffortCapability](/docs/en/api/beta#beta_effort_capability)

Effort (reasoning_effort) support and available levels.

High [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

ImageInput [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model accepts image content blocks.

Supported bool

Whether this capability is supported by the model.

PDFInput [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model accepts PDF content blocks.

Supported bool

Whether this capability is supported by the model.

StructuredOutputs [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports structured output / JSON mode / strict tool schemas.

Supported bool

Whether this capability is supported by the model.

Thinking [BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability)

Thinking capability and supported type configurations.

Supported bool

Whether this capability is supported by the model.

Types [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types)

Supported thinking type configurations.

Adaptive [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

CreatedAt Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

DisplayName string

A human-readable name for the model.

MaxInputTokens int64

Maximum input context window size in tokens for this model.

MaxTokens int64

Maximum value for the `max_tokens` parameter when using this model.

Type Model

Object type.

For Models, this is always `"model"`.

type BetaThinkingCapability struct{…}

Thinking capability details.

Supported bool

Whether this capability is supported by the model.

Types [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types)

Supported thinking type configurations.

Adaptive [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

type BetaThinkingTypes struct{…}

Supported thinking type configurations.

Adaptive [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.
