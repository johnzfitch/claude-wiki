---
title: "Dreams - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/dreams"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:33Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fdreams)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)

# Dreams

##### [Create a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/create)

POST/v1/dreams

Start an asynchronous job that uses past sessions to produce a reorganized version of a memory store and get back the dream to poll for the result.

##### [List Dreams](https://platform.claude.com/docs/en/api/http/beta/dreams/list)

GET/v1/dreams

List the dreams in the workspace, newest first.

##### [Get a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/retrieve)

GET/v1/dreams/{dream_id}

Get a dream by ID to check its status, output memory store, and token usage.

##### [Cancel a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/cancel)

POST/v1/dreams/{dream_id}/cancel

Stop a `pending` or `running` dream.

##### [Archive a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/archive)

POST/v1/dreams/{dream_id}/archive

Hide a `completed`, `failed`, or `canceled` dream from the default list of dreams.

##### Models



BetaDream object{ type: "dream", id, archived_at, 11 more }



An asynchronous job that reads a memory store and past sessions, then writes a reorganized version of that memory store.

By default the dream writes its result to a new memory store and doesn't change the input memory store. With `output_behavior` set to `update_existing`, it writes its result into the input memory store instead.

The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

See the [Dreams guide](../Other/managed-agents-dreams.md#how-it-works) for what a dream reads and produces.



BetaDreamError object{ type, message }



Failure detail for a Dream whose `status` is `failed`.



type: string



A code for why the dream failed, such as `timeout` or `internal_error`.

The [Dreams guide](../Other/managed-agents-dreams.md#errors) lists common error codes and when they occur.

message: string



A human-readable explanation of why the dream failed.



BetaDreamInput = [BetaDreamMemoryStoreInput](https://platform.claude.com/docs/en/api/http/beta/dreams#beta_dream_memory_store_input) or [BetaDreamSessionsInput](https://platform.claude.com/docs/en/api/http/beta/dreams#beta_dream_sessions_input)



A source that a dream reads, such as a memory store or a set of sessions.

One of the following:



BetaDreamMemoryStoreInput object{ type: "memory_store", memory_store_id }



The memory store that a dream reads, given as an entry in `inputs`.

With `output_behavior` set to `update_existing`, the dream writes its result into this memory store. Otherwise the dream doesn't change it.

type: "memory_store"





memory_store_id: string



The ID of the memory store for the dream to read (`memstore_...`).

The memory store must be in the same workspace as the dream and must not be archived.

minLength1



BetaDreamSessionsInput object{ type: "sessions", session_ids }



The sessions that a dream reads, given as an entry in `inputs`.

type: "sessions"





session_ids: array of string



The IDs of the sessions whose transcripts the dream reads (`sesn_...`).

Give 1 to 100 IDs, with no duplicates. Each session must be in the same workspace as the dream. Responses list the IDs in sorted order.

The [limits table in the Dreams guide](../Other/managed-agents-dreams.md#limits) lists all the limits on a dream.



BetaDreamMemoryStoreInput object{ type: "memory_store", memory_store_id }



The memory store that a dream reads, given as an entry in `inputs`.

With `output_behavior` set to `update_existing`, the dream writes its result into this memory store. Otherwise the dream doesn't change it.

type: "memory_store"





memory_store_id: string



The ID of the memory store for the dream to read (`memstore_...`).

The memory store must be in the same workspace as the dream and must not be archived.

minLength1



BetaDreamMemoryStoreOutput object{ type: "memory_store", memory_store_id }



The memory store that holds a dream's result, as an entry in `outputs`.

type: "memory_store"





memory_store_id: string



The ID of the memory store that the dream writes its result to (`memstore_...`).

With `output_behavior` set to `create_new`, this is a new memory store. With `update_existing`, it is the input memory store.



BetaDreamModelConfig object{ id, speed }



The model that runs a dream, from the request that created it.

The dream uses this model for all of its work. The response always gives the model as an object, even if the request gave only a model ID.



id: string



The ID of the model that runs the dream, as given in the request that created it.

minLength1

maxLength256



speed: optional "standard" or "fast"



How fast the model generates output for the dream. Always `standard`.

One of the following:

"standard"



"fast"





BetaDreamModelConfigParam object{ id, speed }



The object form of `model` in a request to create a dream.



id: string



The ID of the model to run the dream with.

The ID can be 1 to 256 characters long.

The [limits table in the Dreams guide](../Other/managed-agents-dreams.md#limits) lists the supported models.

minLength1

maxLength256



speed: optional "standard" or "fast" or null



How fast the model generates output for the dream. Defaults to `standard`.

Dreams accept only `standard`.

One of the following:

"standard"



"fast"





BetaDreamOutput object{ type: "memory_store", memory_store_id }



An entry in a dream's `outputs` that references the memory store holding its result.

type: "memory_store"





memory_store_id: string



The ID of the memory store that the dream writes its result to (`memstore_...`).

With `output_behavior` set to `create_new`, this is a new memory store. With `update_existing`, it is the input memory store.



BetaDreamSessionsInput object{ type: "sessions", session_ids }



The sessions that a dream reads, given as an entry in `inputs`.

type: "sessions"





session_ids: array of string



The IDs of the sessions whose transcripts the dream reads (`sesn_...`).

Give 1 to 100 IDs, with no duplicates. Each session must be in the same workspace as the dream. Responses list the IDs in sorted order.

The [limits table in the Dreams guide](../Other/managed-agents-dreams.md#limits) lists all the limits on a dream.



BetaDreamStatus = "pending" or "running" or "completed" or 2 more



Where a dream is in its lifecycle.

`completed`, `failed`, and `canceled` are final: once a dream has one of these statuses, its status doesn't change again.

See the [Dreams guide](../Other/managed-agents-dreams.md#lifecycle) for what each status means.

One of the following:



"pending"



The dream is waiting to start and hasn't read its inputs yet.

`outputs` is empty and every `usage` count is zero.



"running"



The dream is reading its inputs and writing its result.

`usage` updates while the dream has this status.

"completed"



The dream finished and its output memory store holds the complete result.



"failed"



The dream stopped with an error, which `error` describes.

If `outputs` references a memory store, that memory store keeps what the dream wrote before it stopped.



"canceled"



A cancel request stopped the dream before it reached `completed` or `failed`.

If `outputs` references a memory store, that memory store keeps what the dream wrote. `usage` can keep changing after the cancel.



BetaDreamUsage object{ cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }



The tokens that a dream has used so far.

The counts are zero while the dream is `pending` and update while it is `running`. They can keep changing after a cancel.

See the [Dreams guide](../Other/managed-agents-dreams.md#billing) for how dreams are billed. See the [prompt caching guide](../Guides/build-with-claude-prompt-caching.md#tracking-cache-performance) for how the input token counts add up.



cache_creation_input_tokens: number



The dream's input tokens that were written to the prompt cache, for both the 5-minute and 1-hour cache durations.

formatint32



cache_read_input_tokens: number



The dream's input tokens that were read from the prompt cache.

formatint32



input_tokens: number



The dream's input tokens that weren't read from or written to the prompt cache.

formatint32



output_tokens: number



The tokens that the model generated for the dream.

formatint32



BetaDreamingError = [BetaInvalidRequestError](http-beta.md#beta_invalid_request_error) or [BetaAuthenticationError](http-beta.md#beta_authentication_error) or [BetaBillingError](http-beta.md#beta_billing_error) or 7 more



One of the following:



BetaOutputBehavior = [BetaOutputBehaviorCreateNew](https://platform.claude.com/docs/en/api/http/beta/dreams#beta_output_behavior_create_new) or [BetaOutputBehaviorUpdateExisting](https://platform.claude.com/docs/en/api/http/beta/dreams#beta_output_behavior_update_existing)



Which memory store a dream writes its result to. Defaults to `create_new` when left out of a create request.

One of the following:



BetaOutputBehaviorCreateNew object{ type: "create_new" }



Write the result to a new memory store that starts as a copy of the input memory store. This is the default.

The new memory store is in the same workspace as the dream. The dream doesn't change the input memory store.

type: "create_new"





BetaOutputBehaviorUpdateExisting object{ type: "update_existing", memory_store_id }



Write the result into the input memory store instead of a new memory store.

The credential must be allowed to write memory stores, or the request returns a 403 error. While another `update_existing` dream on the same memory store hasn't fully stopped, the request returns a 409 error.

type: "update_existing"





memory_store_id: string



The ID of the memory store for the dream to write its result to (`memstore_...`). It must be the memory store in the `memory_store` entry of `inputs`.

minLength1



BetaOutputBehaviorCreateNew object{ type: "create_new" }



Write the result to a new memory store that starts as a copy of the input memory store. This is the default.

The new memory store is in the same workspace as the dream. The dream doesn't change the input memory store.

type: "create_new"





BetaOutputBehaviorUpdateExisting object{ type: "update_existing", memory_store_id }



Write the result into the input memory store instead of a new memory store.

The credential must be allowed to write memory stores, or the request returns a 403 error. While another `update_existing` dream on the same memory store hasn't fully stopped, the request returns a 409 error.

type: "update_existing"





memory_store_id: string



The ID of the memory store for the dream to write its result to (`memstore_...`). It must be the memory store in the `memory_store` entry of `inputs`.

minLength1



BetaTargetStoreHeldError object{ type: "conflict_error", message }



Returned with status 409 when a request to create a dream sets `output_behavior` to `update_existing` and another dream that writes into the same memory store hasn't fully stopped.

The other dream is `pending` or `running`, or it has just stopped and is still finishing its last writes. `message` gives the ID of the other dream when the server can identify it. If that dream has already reached `completed`, `failed`, or `canceled`, retry after a short wait. Otherwise, wait for the other dream to end or cancel it, then retry. The response sets the `x-should-retry` header to `false`.

type: "conflict_error"



message: optional string



A human-readable explanation of why the memory store can't be used yet, with the ID of the dream that is using it when the server can identify it.
