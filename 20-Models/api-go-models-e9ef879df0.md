---
category: "20-Models"
fetched_at: "2026-03-20T10:35:08Z"
source_url: "https://platform.claude.com/docs/en/api/go/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/models/list)

client.Models.List(ctx, params) (\*Page\[[ModelInfo](/docs/en/api/models#model_info)\], error)

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

client.Models.Get(ctx, modelID, query) (\*[ModelInfo](/docs/en/api/models#model_info), error)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

type CapabilitySupport struct{…}

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

type ContextManagementCapability struct{…}

Context management capability details.

ClearThinking20251015 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

type EffortCapability struct{…}

Effort (reasoning_effort) capability details.

High [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

type ModelCapabilities struct{…}

Model capability information.

Batch [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports the Batch API.

Supported bool

Whether this capability is supported by the model.

Citations [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports citation generation.

Supported bool

Whether this capability is supported by the model.

CodeExecution [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports code execution tools.

Supported bool

Whether this capability is supported by the model.

ContextManagement [ContextManagementCapability](/docs/en/api/models#context_management_capability)

Context management support and available strategies.

ClearThinking20251015 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Effort [EffortCapability](/docs/en/api/models#effort_capability)

Effort (reasoning_effort) support and available levels.

High [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

ImageInput [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model accepts image content blocks.

Supported bool

Whether this capability is supported by the model.

PDFInput [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model accepts PDF content blocks.

Supported bool

Whether this capability is supported by the model.

StructuredOutputs [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports structured output / JSON mode / strict tool schemas.

Supported bool

Whether this capability is supported by the model.

Thinking [ThinkingCapability](/docs/en/api/models#thinking_capability)

Thinking capability and supported type configurations.

Supported bool

Whether this capability is supported by the model.

Types [ThinkingTypes](/docs/en/api/models#thinking_types)

Supported thinking type configurations.

Adaptive [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

type ModelInfo struct{…}

ID string

Unique model identifier.

Capabilities [ModelCapabilities](/docs/en/api/models#model_capabilities)

Model capability information.

Batch [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports the Batch API.

Supported bool

Whether this capability is supported by the model.

Citations [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports citation generation.

Supported bool

Whether this capability is supported by the model.

CodeExecution [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports code execution tools.

Supported bool

Whether this capability is supported by the model.

ContextManagement [ContextManagementCapability](/docs/en/api/models#context_management_capability)

Context management support and available strategies.

ClearThinking20251015 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [CapabilitySupport](/docs/en/api/models#capability_support)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Effort [EffortCapability](/docs/en/api/models#effort_capability)

Effort (reasoning_effort) support and available levels.

High [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

ImageInput [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model accepts image content blocks.

Supported bool

Whether this capability is supported by the model.

PDFInput [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model accepts PDF content blocks.

Supported bool

Whether this capability is supported by the model.

StructuredOutputs [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports structured output / JSON mode / strict tool schemas.

Supported bool

Whether this capability is supported by the model.

Thinking [ThinkingCapability](/docs/en/api/models#thinking_capability)

Thinking capability and supported type configurations.

Supported bool

Whether this capability is supported by the model.

Types [ThinkingTypes](/docs/en/api/models#thinking_types)

Supported thinking type configurations.

Adaptive [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [CapabilitySupport](/docs/en/api/models#capability_support)

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

type ThinkingCapability struct{…}

Thinking capability details.

Supported bool

Whether this capability is supported by the model.

Types [ThinkingTypes](/docs/en/api/models#thinking_types)

Supported thinking type configurations.

Adaptive [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

type ThinkingTypes struct{…}

Supported thinking type configurations.

Adaptive [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [CapabilitySupport](/docs/en/api/models#capability_support)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.
