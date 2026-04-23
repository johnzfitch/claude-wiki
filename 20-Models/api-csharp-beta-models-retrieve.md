---
title: "Get a Model - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/models/retrieve"
category: "20-Models"
fetched_at: "2026-03-20T10:34:59Z"
tags: ["api"]
---

# Get a Model

[BetaModelInfo](/docs/en/api/beta#beta_model_info) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse 

ModelRetrieveParams parameters

required string modelID

Model identifier or alias.

IReadOnlyList\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\> betas

Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024_09_24

"prompt-caching-2024-07-31"PromptCaching2024_07_31

"computer-use-2024-10-22"ComputerUse2024_10_22

"computer-use-2025-01-24"ComputerUse2025_01_24

"pdfs-2024-09-25"Pdfs2024_09_25

"token-counting-2024-11-01"TokenCounting2024_11_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19

"output-128k-2025-02-19"Output128k2025_02_19

"files-api-2025-04-14"FilesApi2025_04_14

"mcp-client-2025-04-04"McpClient2025_04_04

"mcp-client-2025-11-20"McpClient2025_11_20

"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14

"code-execution-2025-05-22"CodeExecution2025_05_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11

"context-1m-2025-08-07"Context1m2025_08_07

"context-management-2025-06-27"ContextManagement2025_06_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26

"skills-2025-10-02"Skills2025_10_02

"fast-mode-2026-02-01"FastMode2026_02_01

##### ReturnsExpand Collapse 

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

Get a Model

C#

```python
ModelRetrieveParams parameters = new() { ModelID = "model_id" };

var betaModelInfo = await client.Beta.Models.Retrieve(parameters);

Console.WriteLine(betaModelInfo);
```

Response 200

```python
{
  "id": "claude-opus-4-6",
  "capabilities": {
    "batch": {
      "supported": true
    },
    "citations": {
      "supported": true
    },
    "code_execution": {
      "supported": true
    },
    "context_management": {
      "clear_thinking_20251015": {
        "supported": true
      },
      "clear_tool_uses_20250919": {
        "supported": true
      },
      "compact_20260112": {
        "supported": true
      },
      "supported": true
    },
    "effort": {
      "high": {
        "supported": true
      },
      "low": {
        "supported": true
      },
      "max": {
        "supported": true
      },
      "medium": {
        "supported": true
      },
      "supported": true
    },
    "image_input": {
      "supported": true
    },
    "pdf_input": {
      "supported": true
    },
    "structured_outputs": {
      "supported": true
    },
    "thinking": {
      "supported": true,
      "types": {
        "adaptive": {
          "supported": true
        },
        "enabled": {
          "supported": true
        }
      }
    }
  },
  "created_at": "2026-02-04T00:00:00Z",
  "display_name": "Claude Opus 4.6",
  "max_input_tokens": 0,
  "max_tokens": 0,
  "type": "model"
}
```

##### Returns Examples

Response 200

```python
{
  "id": "claude-opus-4-6",
  "capabilities": {
    "batch": {
      "supported": true
    },
    "citations": {
      "supported": true
    },
    "code_execution": {
      "supported": true
    },
    "context_management": {
      "clear_thinking_20251015": {
        "supported": true
      },
      "clear_tool_uses_20250919": {
        "supported": true
      },
      "compact_20260112": {
        "supported": true
      },
      "supported": true
    },
    "effort": {
      "high": {
        "supported": true
      },
      "low": {
        "supported": true
      },
      "max": {
        "supported": true
      },
      "medium": {
        "supported": true
      },
      "supported": true
    },
    "image_input": {
      "supported": true
    },
    "pdf_input": {
      "supported": true
    },
    "structured_outputs": {
      "supported": true
    },
    "thinking": {
      "supported": true,
      "types": {
        "adaptive": {
          "supported": true
        },
        "enabled": {
          "supported": true
        }
      }
    }
  },
  "created_at": "2026-02-04T00:00:00Z",
  "display_name": "Claude Opus 4.6",
