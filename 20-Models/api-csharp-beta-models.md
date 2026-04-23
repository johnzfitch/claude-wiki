---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/models"
category: "20-Models"
fetched_at: "2026-03-20T10:34:56Z"
tags: ["api"]
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

[ModelListPageResponse](/docs/en/api/beta#ModelListPageResponse) Beta.Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

[BetaModelInfo](/docs/en/api/beta#beta_model_info) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class BetaCapabilitySupport:

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

class BetaContextManagementCapability:

Context management capability details.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

class BetaEffortCapability:

Effort (reasoning_effort) capability details.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

class BetaModelCapabilities:

Model capability information.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability) ContextManagement

Context management support and available strategies.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaEffortCapability](/docs/en/api/beta#beta_effort_capability) Effort

Effort (reasoning_effort) support and available levels.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) Types

Supported thinking type configurations.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

class BetaModelInfo:

required string ID

Unique model identifier.

required [BetaModelCapabilities](/docs/en/api/beta#beta_model_capabilities)? Capabilities

Model capability information.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaContextManagementCapability](/docs/en/api/beta#beta_context_management_capability) ContextManagement

Context management support and available strategies.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaEffortCapability](/docs/en/api/beta#beta_effort_capability) Effort

Effort (reasoning_effort) support and available levels.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingCapability](/docs/en/api/beta#beta_thinking_capability) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) Types

Supported thinking type configurations.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Enabled

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

class BetaThinkingCapability:

Thinking capability details.

required Boolean Supported

Whether this capability is supported by the model.

required [BetaThinkingTypes](/docs/en/api/beta#beta_thinking_types) Types

Supported thinking type configurations.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

class BetaThinkingTypes:

Supported thinking type configurations.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.

required [BetaCapabilitySupport](/docs/en/api/beta#beta_capability_support) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.
