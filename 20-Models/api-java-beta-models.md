---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/java/beta/models"
category: "20-Models"
fetched_at: "2026-03-20T10:35:11Z"
tags: ["api"]
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

ModelListPage beta().models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

[BetaModelInfo](/docs/en/api/beta#beta_model_info) beta().models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class BetaCapabilitySupport:

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

class BetaContextManagementCapability:

Context management capability details.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

class BetaEffortCapability:

Effort (reasoning_effort) capability details.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

class BetaModelCapabilities:

Model capability information.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability) contextManagement

Context management support and available strategies.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[BetaEffortCapability](/docs/en/api/beta#beta_effort_capability) effort

Effort (reasoning_effort) support and available levels.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) types

Supported thinking type configurations.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

class BetaModelInfo:

String id

Unique model identifier.

Optional\<[BetaModelCapabilities](/docs/en/api/beta#beta_model_capabilities)\> capabilities

Model capability information.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability) contextManagement

Context management support and available strategies.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional\<[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)\> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[BetaEffortCapability](/docs/en/api/beta#beta_effort_capability) effort

Effort (reasoning_effort) support and available levels.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) types

Supported thinking type configurations.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) enabled

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

class BetaThinkingCapability:

Thinking capability details.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) types

Supported thinking type configurations.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

class BetaThinkingTypes:

Supported thinking type configurations.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.
