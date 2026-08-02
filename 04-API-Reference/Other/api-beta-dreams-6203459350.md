---
title: "Dreams - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/dreams"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:27Z"
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

Dreams




cURL

# Dreams

##### [Create a Dream](/docs/en/api/beta/dreams/create)

POST/v1/dreams

##### [List Dreams](/docs/en/api/beta/dreams/list)

GET/v1/dreams

##### [Get a Dream](/docs/en/api/beta/dreams/retrieve)

GET/v1/dreams/{dream_id}

##### [Cancel a Dream](/docs/en/api/beta/dreams/cancel)

POST/v1/dreams/{dream_id}/cancel

##### [Archive a Dream](/docs/en/api/beta/dreams/archive)

POST/v1/dreams/{dream_id}/archive

##### ModelsExpand Collapse 

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



BetaDreamError object { message, type }



Failure detail for a Dream whose `status` is `failed`.

message: string



[](#beta_dream_error.message)

type: string



[](#beta_dream_error.type)

[](#beta_dream_error)



BetaDreamInput = [BetaDreamMemoryStoreInput](/docs/en/api/beta/dreams#beta_dream_memory_store_input) { memory_store_id, type } or [BetaDreamSessionsInput](/docs/en/api/beta/dreams#beta_dream_sessions_input) { session_ids, type }



An input memory store the dream reads from. The dream never mutates this store.

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

[](#beta_dream_input)

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

BetaDreamMemoryStoreOutput object { memory_store_id, type }



An output memory store the dream writes consolidated memories into.

memory_store_id: string



[](#beta_dream_memory_store_output.memory_store_id)

type: "memory_store"



[](#beta_dream_memory_store_output.type)

[](#beta_dream_memory_store_output)



BetaDreamModelConfig object { id, speed }



Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

id: string



Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

[](#beta_dream_model_config.id)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#beta_dream_model_config.speed%5B0%5D)

"fast"



[](#beta_dream_model_config.speed%5B1%5D)

[](#beta_dream_model_config.speed)

[](#beta_dream_model_config)

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



BetaDreamOutput object { memory_store_id, type }



An output memory store the dream writes consolidated memories into.

memory_store_id: string



[](#beta_dream_output.memory_store_id)

type: "memory_store"



[](#beta_dream_output.type)

[](#beta_dream_output)

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



BetaDreamStatus = "pending" or "running" or "completed" or 2 more



Lifecycle status of a Dream.

One of the following:

"pending"



[](#beta_dream_status%5B0%5D)

"running"



[](#beta_dream_status%5B1%5D)

"completed"



[](#beta_dream_status%5B2%5D)

"failed"



[](#beta_dream_status%5B3%5D)

"canceled"



[](#beta_dream_status%5B4%5D)

[](#beta_dream_status)



BetaDreamUsage object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }



Cumulative token usage for the dream across every pipeline stage.

cache_creation_input_tokens: number



Total tokens used to create prompt-cache entries (sum of all TTL tiers).

[](#beta_dream_usage.cache_creation_input_tokens)

cache_read_input_tokens: number



Total tokens read from prompt cache.

[](#beta_dream_usage.cache_read_input_tokens)

input_tokens: number



Total uncached input tokens consumed across every pipeline stage.

[](#beta_dream_usage.input_tokens)

output_tokens: number



Total output tokens generated across every pipeline stage.

[](#beta_dream_usage.output_tokens)
