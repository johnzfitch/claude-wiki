---
title: "Memories - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memories"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:30Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmemory_stores%2Fmemories)

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


Create a memory store


List memory stores


Retrieve a memory store


Update a memory store


Delete a memory store


Archive a memory store

Memories


Create a memory


List memories


Retrieve a memory


Update a memory


Delete a memory

Memory Versions

Dreams


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
3.  [Memory Stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores)

# Memories

##### [Create a memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

##### [List memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

##### [Retrieve a memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Update a memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Delete a memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### Models



BetaManagedAgentsConflictError object{ type: "conflict_error", message }



type: "conflict_error"



message: optional string





BetaManagedAgentsContentSha256Precondition object{ type: "content_sha256", content_sha256 }



Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: "content_sha256"



content_sha256: optional string



Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.



BetaManagedAgentsDeletedMemory object{ type: "memory_deleted", id }



Tombstone returned by [Delete a memory](beta-memory-stores-memories-delete.md). Deleting a memory does not erase its version history: its versions remain listable via [List memory versions](beta-memory-stores-memory-versions-list.md) while they are retained (each version is kept for at least the version retention period after it was written, unless the store itself is deleted).

type: "memory_deleted"



id: string



ID of the deleted memory (a `mem_...` value).



BetaManagedAgentsError = [BetaInvalidRequestError](http-beta.md#beta_invalid_request_error) or [BetaAuthenticationError](http-beta.md#beta_authentication_error) or [BetaBillingError](http-beta.md#beta_billing_error) or 9 more



One of the following:



BetaManagedAgentsMemory object{ type: "memory", id, content_sha256, 7 more }



A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.



BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories#beta_managed_agents_memory) or [BetaManagedAgentsMemoryPrefix](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories#beta_managed_agents_memory_prefix)



One item in a [List memories](beta-memory-stores-memories-list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

One of the following:



BetaManagedAgentsMemory object{ type: "memory", id, content_sha256, 7 more }



A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.



BetaManagedAgentsMemoryPrefix object{ type: "memory_prefix", path }



A rolled-up directory marker returned by [List memories](beta-memory-stores-memories-list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

type: "memory_prefix"



path: string



The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.



BetaManagedAgentsMemoryPathConflictError object{ type: "memory_path_conflict_error", conflicting_memory_id, conflicting_path, message }



The error returned with HTTP status 409 when a create or rename targets a path that another memory uses, or a path that overlaps another memory's path.

Two paths overlap when one is an ancestor of the other, such as `/notes` and `/notes/todo.md`. To free the path, rename or delete the memory that `conflicting_memory_id` references, then retry. To change that memory instead of creating a new one, update it.

type: "memory_path_conflict_error"





conflicting_memory_id: optional string



The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified.

Retry the request when it is empty.

conflicting_path: optional string



The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it.

message: optional string



A human-readable explanation of the conflict. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead.



BetaManagedAgentsMemoryPreconditionFailedError object{ type: "memory_precondition_failed_error", message }



The error returned with HTTP status 409 when a request's precondition doesn't hold for the memory's current state, such as `precondition` on an update or `expected_content_sha256` on a delete.

The error doesn't include the memory's current state. Retrieve the memory to see its current content and `content_sha256` before you retry.

See the [memory guide](../Other/managed-agents-memory.md#safe-content-edits-optimistic-concurrency) to learn more about safe content edits with content hash preconditions.

type: "memory_precondition_failed_error"



message: optional string



A human-readable explanation of why the precondition failed.



BetaManagedAgentsMemoryPrefix object{ type: "memory_prefix", path }



A rolled-up directory marker returned by [List memories](beta-memory-stores-memories-list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

type: "memory_prefix"



path: string



The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.



BetaManagedAgentsMemoryView = "basic" or "full"



Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

One of the following:

"basic"



Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

"full"



Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.



BetaManagedAgentsPrecondition object{ type: "content_sha256", content_sha256 }



Optional condition that must hold for an update to apply. When omitted, the update is unconditional. Asserts the current state of the memory being updated. When an update changes `path`, the precondition still refers to the memory's current content, not the destination path. Currently the only supported variant is `content_sha256`.

type: "content_sha256"



content_sha256: optional string



Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.
