---
category: "20-Models"
fetched_at: "2026-03-20T10:35:10Z"
source_url: "https://platform.claude.com/docs/en/api/go/models/retrieve"
title: "Get a Model - Claude API Reference"
---

# Get a Model

client.Models.Get(ctx, modelID, query) (\*[ModelInfo](/docs/en/api/models#model_info), error)

GET/v1/models/{model_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse 

modelID string

Model identifier or alias.

query ModelGetParams

Betas param.Field\[\[\]AnthropicBeta\]

optional

Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"

##### ReturnsExpand Collapse 

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

Get a Model

Go

```python
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  modelInfo, err := client.Models.Get(
    context.TODO(),
    "model_id",
    anthropic.ModelGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", modelInfo.ID)
}
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
