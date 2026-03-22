---
category: "20-Models"
fetched_at: "2026-03-20T10:35:15Z"
source_url: "https://platform.claude.com/docs/en/api/java/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/models/list)

ModelListPage models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

[ModelInfo](/docs/en/api/models#model_info) models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class CapabilitySupport:

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

class ContextManagementCapability:

Context management capability details.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

class EffortCapability:

Effort (reasoning_effort) capability details.

[CapabilitySupport](/docs/en/api/models#capability_support) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

class ModelCapabilities:

Model capability information.

[CapabilitySupport](/docs/en/api/models#capability_support) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[ContextManagementCapability](/docs/en/api/models#context_management_capability) contextManagement

Context management support and available strategies.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[EffortCapability](/docs/en/api/models#effort_capability) effort

Effort (reasoning_effort) support and available levels.

[CapabilitySupport](/docs/en/api/models#capability_support) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[ThinkingCapability](/docs/en/api/models#thinking_capability) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[ThinkingTypes](/docs/en/api/models#thinking_types) types

Supported thinking type configurations.

[CapabilitySupport](/docs/en/api/models#capability_support) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

class ModelInfo:

String id

Unique model identifier.

Optional\<[ModelCapabilities](/docs/en/api/models#model_capabilities)\> capabilities

Model capability information.

[CapabilitySupport](/docs/en/api/models#capability_support) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[ContextManagementCapability](/docs/en/api/models#context_management_capability) contextManagement

Context management support and available strategies.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[CapabilitySupport](/docs/en/api/models#capability_support)\> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[EffortCapability](/docs/en/api/models#effort_capability) effort

Effort (reasoning_effort) support and available levels.

[CapabilitySupport](/docs/en/api/models#capability_support) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[ThinkingCapability](/docs/en/api/models#thinking_capability) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[ThinkingTypes](/docs/en/api/models#thinking_types) types

Supported thinking type configurations.

[CapabilitySupport](/docs/en/api/models#capability_support) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

String displayName

A human-readable name for the model.

Optional\<Long\> maxInputTokens

Maximum input context window size in tokens for this model.

Optional\<Long\> maxTokens

Maximum value for the `max_tokens` parameter when using this model.

JsonValue; type "model"constant

"model"constant

Object type.

For Models, this is always `"model"`.

class ThinkingCapability:

Thinking capability details.

boolean supported

Whether this capability is supported by the model.

[ThinkingTypes](/docs/en/api/models#thinking_types) types

Supported thinking type configurations.

[CapabilitySupport](/docs/en/api/models#capability_support) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

class ThinkingTypes:

Supported thinking type configurations.

[CapabilitySupport](/docs/en/api/models#capability_support) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](/docs/en/api/models#capability_support) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.
