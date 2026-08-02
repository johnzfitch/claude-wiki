---
title: "Create a Dream - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/dreams/create"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:53Z"
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

Create




cURL

# Create a Dream

POST/v1/dreams

Create a Dream

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

[](#create.betas)

##### Body ParametersJSONExpand Collapse 



inputs: array of [BetaDreamInput](/docs/en/api/beta/dreams#beta_dream_input)



One of the following:



BetaDreamMemoryStoreInput object { memory_store_id, type }



An input memory store the dream reads from. The dream never mutates this store.

memory_store_id: string



[](#beta_dream_memory_store_input.memory_store_id)

type: "memory_store"



[](#beta_dream_memory_store_input.type)

[](#beta_dream_memory_store_input)



BetaDreamSessionsInput object { session_ids, type }



Input session transcripts the dream reads.

session_ids: array of string



[](#beta_dream_sessions_input.session_ids)

type: "sessions"



[](#beta_dream_sessions_input.type)

[](#beta_dream_sessions_input)

[](#create.inputs)



model: string or [BetaDreamModelConfigParam](/docs/en/api/beta/dreams#beta_dream_model_config_param) { id, speed }



Model identifier and configuration applied to every pipeline stage.

One of the following:

string



[](#create.model%5B0%5D)



BetaDreamModelConfigParam object { id, speed }



Model identifier and configuration applied to every pipeline stage.

id: string



Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

[](#beta_dream_model_config_param.id)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_dream_model_config_param.speed%5B0%5D)

"fast"



[](#beta_dream_model_config_param.speed%5B1%5D)

[](#beta_dream_model_config_param.speed)

[](#beta_dream_model_config_param)

[](#create.model)

instructions: optional string



[](#create.instructions)

##### ReturnsExpand Collapse 



BetaDream object { id, archived_at, created_at, 10 more }



An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

id: string



[](#beta_dream.id)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_dream.archived_at)

created_at: string



A timestamp in RFC 3339 format

[](#beta_dream.created_at)

ended_at: string



A timestamp in RFC 3339 format

[](#beta_dream.ended_at)



error: [BetaDreamError](/docs/en/api/beta/dreams#beta_dream_error) { message, type }



Failure detail for a Dream whose `status` is `failed`.

message: string



[](#beta_dream.error%20%2B%20(resource)%20beta.dreams.message)

type: string



[](#beta_dream.error%20%2B%20(resource)%20beta.dreams.type)

[](#beta_dream.error)



inputs: array of [BetaDreamInput](/docs/en/api/beta/dreams#beta_dream_input)



One of the following:



BetaDreamMemoryStoreInput object { memory_store_id, type }



An input memory store the dream reads from. The dream never mutates this store.

memory_store_id: string



[](#beta_dream_memory_store_input.memory_store_id)

type: "memory_store"



[](#beta_dream_memory_store_input.type)

[](#beta_dream_memory_store_input)



BetaDreamSessionsInput object { session_ids, type }



Input session transcripts the dream reads.

session_ids: array of string



[](#beta_dream_sessions_input.session_ids)

type: "sessions"



[](#beta_dream_sessions_input.type)

[](#beta_dream_sessions_input)

[](#beta_dream.inputs)

instructions: string



[](#beta_dream.instructions)



model: [BetaDreamModelConfig](/docs/en/api/beta/dreams#beta_dream_model_config) { id, speed }



Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

id: string



Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

[](#beta_dream.model%20%2B%20(resource)%20beta.dreams.id)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_dream.model%20%2B%20(resource)%20beta.dreams.speed%5B0%5D)

"fast"



[](#beta_dream.model%20%2B%20(resource)%20beta.dreams.speed%5B1%5D)

[](#beta_dream.model%20%2B%20(resource)%20beta.dreams.speed)

[](#beta_dream.model)



outputs: array of [BetaDreamOutput](/docs/en/api/beta/dreams#beta_dream_output) { memory_store_id, type }



memory_store_id: string



[](#beta_dream_output.memory_store_id)

type: "memory_store"



[](#beta_dream_output.type)

[](#beta_dream.outputs)

session_id: string



[](#beta_dream.session_id)



status: [BetaDreamStatus](/docs/en/api/beta/dreams#beta_dream_status)



Lifecycle status of a Dream.

One of the following:

"pending"



[](#beta_dream.status%20%2B%20(resource)%20beta.dreams%5B0%5D)

"running"



[](#beta_dream.status%20%2B%20(resource)%20beta.dreams%5B1%5D)

"completed"



[](#beta_dream.status%20%2B%20(resource)%20beta.dreams%5B2%5D)

"failed"



[](#beta_dream.status%20%2B%20(resource)%20beta.dreams%5B3%5D)

"canceled"



[](#beta_dream.status%20%2B%20(resource)%20beta.dreams%5B4%5D)

[](#beta_dream.status)

type: "dream"



[](#beta_dream.type)



usage: [BetaDreamUsage](/docs/en/api/beta/dreams#beta_dream_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }



Cumulative token usage for the dream across every pipeline stage.

cache_creation_input_tokens: number



Total tokens used to create prompt-cache entries (sum of all TTL tiers).

[](#beta_dream.usage%20%2B%20(resource)%20beta.dreams.cache_creation_input_tokens)

cache_read_input_tokens: number



Total tokens read from prompt cache.

[](#beta_dream.usage%20%2B%20(resource)%20beta.dreams.cache_read_input_tokens)

input_tokens: number



Total uncached input tokens consumed across every pipeline stage.

[](#beta_dream.usage%20%2B%20(resource)%20beta.dreams.input_tokens)

output_tokens: number



Total output tokens generated across every pipeline stage.

[](#beta_dream.usage%20%2B%20(resource)%20beta.dreams.output_tokens)

[](#beta_dream.usage)

[](#beta_dream)

Create a Dream

cURL



```python
curl https://api.anthropic.com/v1/dreams \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "inputs": [
            {
              "memory_store_id": "x",
              "type": "memory_store"
            }
          ],
          "model": "string"
        }'
```

Response 200



```python
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
