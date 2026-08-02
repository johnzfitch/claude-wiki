---
title: "List Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/models/list"
category: "20-Models"
fetched_at: "2026-08-02T05:39:46Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

List




cURL

# List Models

GET/v1/models

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

##### Query ParametersExpand Collapse 

after_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

[](#list.after_id)

before_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

[](#list.before_id)



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

[](#list.limit)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string



[](#anthropic_beta%5B0%5D)



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more



One of the following:

"message-batches-2024-09-24"



[](#anthropic_beta%5B1%5D%5B0%5D)

"prompt-caching-2024-07-31"



[](#anthropic_beta%5B1%5D%5B1%5D)

"computer-use-2024-10-22"



[](#anthropic_beta%5B1%5D%5B2%5D)

"computer-use-2025-01-24"



[](#anthropic_beta%5B1%5D%5B3%5D)

"pdfs-2024-09-25"



[](#anthropic_beta%5B1%5D%5B4%5D)

"token-counting-2024-11-01"



[](#anthropic_beta%5B1%5D%5B5%5D)

"token-efficient-tools-2025-02-19"



[](#anthropic_beta%5B1%5D%5B6%5D)

"output-128k-2025-02-19"



[](#anthropic_beta%5B1%5D%5B7%5D)

"files-api-2025-04-14"



[](#anthropic_beta%5B1%5D%5B8%5D)

"mcp-client-2025-04-04"



[](#anthropic_beta%5B1%5D%5B9%5D)

"mcp-client-2025-11-20"



[](#anthropic_beta%5B1%5D%5B10%5D)

"dev-full-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B11%5D)

"interleaved-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B12%5D)

"code-execution-2025-05-22"



[](#anthropic_beta%5B1%5D%5B13%5D)

"extended-cache-ttl-2025-04-11"



[](#anthropic_beta%5B1%5D%5B14%5D)

"context-1m-2025-08-07"



[](#anthropic_beta%5B1%5D%5B15%5D)

"context-management-2025-06-27"



[](#anthropic_beta%5B1%5D%5B16%5D)

"model-context-window-exceeded-2025-08-26"



[](#anthropic_beta%5B1%5D%5B17%5D)

"skills-2025-10-02"



[](#anthropic_beta%5B1%5D%5B18%5D)

"fast-mode-2026-02-01"



[](#anthropic_beta%5B1%5D%5B19%5D)

"output-300k-2026-03-24"



[](#anthropic_beta%5B1%5D%5B20%5D)

"user-profiles-2026-03-24"



[](#anthropic_beta%5B1%5D%5B21%5D)

"advisor-tool-2026-03-01"



[](#anthropic_beta%5B1%5D%5B22%5D)

"managed-agents-2026-04-01"



[](#anthropic_beta%5B1%5D%5B23%5D)

"cache-diagnosis-2026-04-07"



[](#anthropic_beta%5B1%5D%5B24%5D)

"dreaming-2026-04-21"



[](#anthropic_beta%5B1%5D%5B25%5D)

"thinking-token-count-2026-05-13"



[](#anthropic_beta%5B1%5D%5B26%5D)

"server-side-fallback-2026-06-01"



[](#anthropic_beta%5B1%5D%5B27%5D)

"server-side-fallback-2026-07-01"



[](#anthropic_beta%5B1%5D%5B28%5D)

"fallback-credit-2026-06-01"



[](#anthropic_beta%5B1%5D%5B29%5D)

"fallback-credit-2026-07-01"



[](#anthropic_beta%5B1%5D%5B30%5D)

"agent-memory-2026-07-22"



[](#anthropic_beta%5B1%5D%5B31%5D)

[](#anthropic_beta%5B1%5D)

[](#list.betas)

##### ReturnsExpand Collapse 



data: array of [BetaModelInfo](/docs/en/api/beta/models#beta_model_info) { id, allowed_fallback_models, capabilities, 5 more }



id: string



Unique model identifier.

[](#beta_model_info.id)

allowed_fallback_models: array of string



Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

[](#beta_model_info.allowed_fallback_models)



capabilities: [BetaModelCapabilities](/docs/en/api/beta/models#beta_model_capabilities) { batch, citations, code_execution, 6 more }



Model capability information.



batch: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports the Batch API.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.batch%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.batch)



citations: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports citation generation.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.citations%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.citations)



code_execution: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports code execution tools.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.code_execution%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.code_execution)



context_management: [BetaContextManagementCapability](/docs/en/api/beta/models#beta_context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management support and available strategies.



clear_thinking_20251015: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.clear_thinking_20251015%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.clear_thinking_20251015)



clear_tool_uses_20250919: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.clear_tool_uses_20250919%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.clear_tool_uses_20250919)



compact_20260112: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_context_management_capability.compact_20260112%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.compact_20260112)

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.context_management%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.context_management)



effort: [BetaEffortCapability](/docs/en/api/beta/models#beta_effort_capability) { high, low, max, 3 more }



Effort (reasoning_effort) support and available levels.



high: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports high effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.high%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.high)



low: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports low effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.low%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.low)



max: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports max effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.max%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.max)



medium: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports medium effort level.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.medium%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.medium)

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.supported)



xhigh: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.

[](#beta_effort_capability.xhigh%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_capabilities.effort%20%2B%20(resource)%20beta.models.xhigh)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.effort)



image_input: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model accepts image content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.image_input%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.image_input)



pdf_input: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model accepts PDF content blocks.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.pdf_input%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.pdf_input)



structured_outputs: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.structured_outputs%20%2B%20(resource)%20beta.models.supported)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.structured_outputs)



thinking: [BetaThinkingCapability](/docs/en/api/beta/models#beta_thinking_capability) { supported, types }



Thinking capability and supported type configurations.

supported: boolean



Whether this capability is supported by the model.

[](#beta_model_capabilities.thinking%20%2B%20(resource)%20beta.models.supported)



types: [BetaThinkingTypes](/docs/en/api/beta/models#beta_thinking_types) { adaptive, enabled }



Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.adaptive%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_capability.types%20%2B%20(resource)%20beta.models.adaptive)



enabled: [BetaCapabilitySupport](/docs/en/api/beta/models#beta_capability_support) { supported }



Whether the model supports thinking with type 'enabled'.

supported: boolean



Whether this capability is supported by the model.

[](#beta_thinking_types.enabled%20%2B%20(resource)%20beta.models.supported)

[](#beta_thinking_capability.types%20%2B%20(resource)%20beta.models.enabled)

[](#beta_model_capabilities.thinking%20%2B%20(resource)%20beta.models.types)

[](#beta_model_info.capabilities%20%2B%20(resource)%20beta.models.thinking)

[](#beta_model_info.capabilities)

created_at: string



RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

[](#beta_model_info.created_at)

display_name: string



A human-readable name for the model.

[](#beta_model_info.display_name)

max_input_tokens: number



Maximum input context window size in tokens for this model.

[](#beta_model_info.max_input_tokens)

max_tokens: number



Maximum value for the `max_tokens` parameter when using this model.

[](#beta_model_info.max_tokens)



type: "model"



Object type.

For Models, this is always `"model"`.

[](#beta_model_info.type)

[](#list)

first_id: string



First ID in the `data` list. Can be used as the `before_id` for the previous page.

[](#list)

has_more: boolean



Indicates if there are more results in the requested page direction.

[](#list)

last_id: string



Last ID in the `data` list. Can be used as the `after_id` for the next page.

[](#list)

List Models

cURL



```python
curl https://api.anthropic.com/v1/models \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "claude-opus-4-6",
      "allowed_fallback_models": [
        "string"
      ],
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
          "supported": true,
          "xhigh": {
            "supported": true
          }
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "claude-opus-4-6",
      "allowed_fallback_models": [
        "string"
      ],
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
          "supported": true,
          "xhigh": {
            "supported": true
          }
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
