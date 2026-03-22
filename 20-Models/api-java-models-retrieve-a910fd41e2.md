---
category: "20-Models"
fetched_at: "2026-03-20T10:35:17Z"
source_url: "https://platform.claude.com/docs/en/api/java/models/retrieve"
title: "Get a Model - Claude API Reference"
---

# Get a Model

[ModelInfo](/docs/en/api/models#model_info) models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse 

ModelRetrieveParams params

Optional\<String\> modelId

Model identifier or alias.

Optional\<List\<AnthropicBeta\>\> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")

PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")

COMPUTER_USE_2024_10_22("computer-use-2024-10-22")

COMPUTER_USE_2025_01_24("computer-use-2025-01-24")

PDFS_2024_09_25("pdfs-2024-09-25")

TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")

TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")

OUTPUT_128K_2025_02_19("output-128k-2025-02-19")

FILES_API_2025_04_14("files-api-2025-04-14")

MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")

MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")

DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")

INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")

CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")

EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")

CONTEXT_1M_2025_08_07("context-1m-2025-08-07")

CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")

MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")

SKILLS_2025_10_02("skills-2025-10-02")

FAST_MODE_2026_02_01("fast-mode-2026-02-01")

##### ReturnsExpand Collapse 

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

Get a Model

Java

```python
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.models.ModelInfo;
import com.anthropic.models.models.ModelRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ModelInfo modelInfo = client.models().retrieve("model_id");
    }
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
