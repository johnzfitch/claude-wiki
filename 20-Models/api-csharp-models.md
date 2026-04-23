---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/csharp/models"
category: "20-Models"
fetched_at: "2026-03-20T10:35:00Z"
tags: ["api"]
---

# Models

##### [List Models](/docs/en/api/models/list)

[ModelListPageResponse](/docs/en/api/models#ModelListPageResponse) Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

[ModelInfo](/docs/en/api/models#model_info) Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class CapabilitySupport:

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

class ContextManagementCapability:

Context management capability details.

required [CapabilitySupport](/docs/en/api/models#capability_support)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

class EffortCapability:

Effort (reasoning_effort) capability details.

required [CapabilitySupport](/docs/en/api/models#capability_support) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

class ModelCapabilities:

Model capability information.

required [CapabilitySupport](/docs/en/api/models#capability_support) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.

required [ContextManagementCapability](/docs/en/api/models#context_management_capability) ContextManagement

Context management support and available strategies.

required [CapabilitySupport](/docs/en/api/models#capability_support)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [EffortCapability](/docs/en/api/models#effort_capability) Effort

Effort (reasoning_effort) support and available levels.

required [CapabilitySupport](/docs/en/api/models#capability_support) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.

required [ThinkingCapability](/docs/en/api/models#thinking_capability) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.

required [ThinkingTypes](/docs/en/api/models#thinking_types) Types

Supported thinking type configurations.

required [CapabilitySupport](/docs/en/api/models#capability_support) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

class ModelInfo:

required string ID

Unique model identifier.

required [ModelCapabilities](/docs/en/api/models#model_capabilities)? Capabilities

Model capability information.

required [CapabilitySupport](/docs/en/api/models#capability_support) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.

required [ContextManagementCapability](/docs/en/api/models#context_management_capability) ContextManagement

Context management support and available strategies.

required [CapabilitySupport](/docs/en/api/models#capability_support)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [EffortCapability](/docs/en/api/models#effort_capability) Effort

Effort (reasoning_effort) support and available levels.

required [CapabilitySupport](/docs/en/api/models#capability_support) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.

required [ThinkingCapability](/docs/en/api/models#thinking_capability) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.

required [ThinkingTypes](/docs/en/api/models#thinking_types) Types

Supported thinking type configurations.

required [CapabilitySupport](/docs/en/api/models#capability_support) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

required string DisplayName

A human-readable name for the model.

required Long? MaxInputTokens

Maximum input context window size in tokens for this model.

required Long? MaxTokens

Maximum value for the `max_tokens` parameter when using this model.

JsonElement Type "model"constant

Object type.

For Models, this is always `"model"`.

class ThinkingCapability:

Thinking capability details.

required Boolean Supported

Whether this capability is supported by the model.

required [ThinkingTypes](/docs/en/api/models#thinking_types) Types

Supported thinking type configurations.

required [CapabilitySupport](/docs/en/api/models#capability_support) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

class ThinkingTypes:

Supported thinking type configurations.

required [CapabilitySupport](/docs/en/api/models#capability_support) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [CapabilitySupport](/docs/en/api/models#capability_support) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.
