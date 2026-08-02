---
title: "Memories - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memories"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:38Z"
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


Create a memory store


List memory stores


Retrieve a memory store


Update a memory store


Delete a memory store


Archive a memory store

Memories


Create a memory


List memories


Retrieve a memory


Update a memory


Delete a memory

Memory Versions


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

Memories




cURL

# Memories

##### [Create a memory](/docs/en/api/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

##### [List memories](/docs/en/api/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

##### [Retrieve a memory](/docs/en/api/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Update a memory](/docs/en/api/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### ModelsExpand Collapse 



BetaManagedAgentsConflictError object { type, message }



type: "conflict_error"



[](#beta_managed_agents_conflict_error.type)

message: optional string



[](#beta_managed_agents_conflict_error.message)

[](#beta_managed_agents_conflict_error)



BetaManagedAgentsContentSha256Precondition object { type, content_sha256 }



Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: "content_sha256"



[](#beta_managed_agents_content_sha256_precondition.type)

content_sha256: optional string



Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

[](#beta_managed_agents_content_sha256_precondition.content_sha256)

[](#beta_managed_agents_content_sha256_precondition)



BetaManagedAgentsDeletedMemory object { id, type }



Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

id: string



ID of the deleted memory (a `mem_...` value).

[](#beta_managed_agents_deleted_memory.id)

type: "memory_deleted"



[](#beta_managed_agents_deleted_memory.type)

[](#beta_managed_agents_deleted_memory)



BetaManagedAgentsError = [BetaInvalidRequestError](/docs/en/api/beta#beta_invalid_request_error) { message, type } or [BetaAuthenticationError](/docs/en/api/beta#beta_authentication_error) { message, type } or [BetaBillingError](/docs/en/api/beta#beta_billing_error) { message, type } or 9 more



One of the following:



BetaInvalidRequestError object { message, type }



message: string



[](#beta_invalid_request_error.message)

type: "invalid_request_error"



[](#beta_invalid_request_error.type)

[](#beta_invalid_request_error)



BetaAuthenticationError object { message, type }



message: string



[](#beta_authentication_error.message)

type: "authentication_error"



[](#beta_authentication_error.type)

[](#beta_authentication_error)



BetaBillingError object { message, type }



message: string



[](#beta_billing_error.message)

type: "billing_error"



[](#beta_billing_error.type)

[](#beta_billing_error)



BetaPermissionError object { message, type }



message: string



[](#beta_permission_error.message)

type: "permission_error"



[](#beta_permission_error.type)

[](#beta_permission_error)



BetaNotFoundError object { message, type }



message: string



[](#beta_not_found_error.message)

type: "not_found_error"



[](#beta_not_found_error.type)

[](#beta_not_found_error)



BetaRateLimitError object { message, type }



message: string



[](#beta_rate_limit_error.message)

type: "rate_limit_error"



[](#beta_rate_limit_error.type)

[](#beta_rate_limit_error)



BetaGatewayTimeoutError object { message, type }



message: string



[](#beta_gateway_timeout_error.message)

type: "timeout_error"



[](#beta_gateway_timeout_error.type)

[](#beta_gateway_timeout_error)



BetaAPIError object { message, type }



message: string



[](#beta_api_error.message)

type: "api_error"



[](#beta_api_error.type)

[](#beta_api_error)



BetaOverloadedError object { message, type }



message: string



[](#beta_overloaded_error.message)

type: "overloaded_error"



[](#beta_overloaded_error.type)

[](#beta_overloaded_error)



BetaManagedAgentsMemoryPreconditionFailedError object { type, message }



type: "memory_precondition_failed_error"



[](#beta_managed_agents_memory_precondition_failed_error.type)

message: optional string



[](#beta_managed_agents_memory_precondition_failed_error.message)

[](#beta_managed_agents_memory_precondition_failed_error)



BetaManagedAgentsMemoryPathConflictError object { type, conflicting_memory_id, conflicting_path, message }



type: "memory_path_conflict_error"



[](#beta_managed_agents_memory_path_conflict_error.type)

conflicting_memory_id: optional string



[](#beta_managed_agents_memory_path_conflict_error.conflicting_memory_id)

conflicting_path: optional string



[](#beta_managed_agents_memory_path_conflict_error.conflicting_path)

message: optional string



[](#beta_managed_agents_memory_path_conflict_error.message)

[](#beta_managed_agents_memory_path_conflict_error)



BetaManagedAgentsConflictError object { type, message }



type: "conflict_error"



[](#beta_managed_agents_conflict_error.type)

message: optional string



[](#beta_managed_agents_conflict_error.message)

[](#beta_managed_agents_conflict_error)

[](#beta_managed_agents_error)



BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more }



A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: string



Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

[](#beta_managed_agents_memory.id)

content_sha256: string



Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

[](#beta_managed_agents_memory.content_sha256)

content_size_bytes: number



Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

[](#beta_managed_agents_memory.content_size_bytes)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory.created_at)

memory_store_id: string



ID of the memory store this memory belongs to (a `memstore_...` value).

[](#beta_managed_agents_memory.memory_store_id)

memory_version_id: string



ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

[](#beta_managed_agents_memory.memory_version_id)

path: string



Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

[](#beta_managed_agents_memory.path)

type: "memory"



[](#beta_managed_agents_memory.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory.updated_at)

content: optional string



The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

[](#beta_managed_agents_memory.content)

[](#beta_managed_agents_memory)



BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](/docs/en/api/beta/memory_stores/memories#beta_managed_agents_memory) { id, content_sha256, content_size_bytes, 7 more } or [BetaManagedAgentsMemoryPrefix](/docs/en/api/beta/memory_stores/memories#beta_managed_agents_memory_prefix) { path, type }



One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

One of the following:



BetaManagedAgentsMemory object { id, content_sha256, content_size_bytes, 7 more }



A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: string



Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

[](#beta_managed_agents_memory.id)

content_sha256: string



Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

[](#beta_managed_agents_memory.content_sha256)

content_size_bytes: number



Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

[](#beta_managed_agents_memory.content_size_bytes)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory.created_at)

memory_store_id: string



ID of the memory store this memory belongs to (a `memstore_...` value).

[](#beta_managed_agents_memory.memory_store_id)

memory_version_id: string



ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

[](#beta_managed_agents_memory.memory_version_id)

path: string



Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

[](#beta_managed_agents_memory.path)

type: "memory"



[](#beta_managed_agents_memory.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory.updated_at)

content: optional string



The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

[](#beta_managed_agents_memory.content)

[](#beta_managed_agents_memory)



BetaManagedAgentsMemoryPrefix object { path, type }



A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: string



The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

[](#beta_managed_agents_memory_prefix.path)

type: "memory_prefix"



[](#beta_managed_agents_memory_prefix.type)

[](#beta_managed_agents_memory_prefix)

[](#beta_managed_agents_memory_list_item)



BetaManagedAgentsMemoryPathConflictError object { type, conflicting_memory_id, conflicting_path, message }



type: "memory_path_conflict_error"



[](#beta_managed_agents_memory_path_conflict_error.type)

conflicting_memory_id: optional string



[](#beta_managed_agents_memory_path_conflict_error.conflicting_memory_id)

conflicting_path: optional string



[](#beta_managed_agents_memory_path_conflict_error.conflicting_path)

message: optional string



[](#beta_managed_agents_memory_path_conflict_error.message)

[](#beta_managed_agents_memory_path_conflict_error)



BetaManagedAgentsMemoryPreconditionFailedError object { type, message }



type: "memory_precondition_failed_error"



[](#beta_managed_agents_memory_precondition_failed_error.type)

message: optional string



[](#beta_managed_agents_memory_precondition_failed_error.message)

[](#beta_managed_agents_memory_precondition_failed_error)



BetaManagedAgentsMemoryPrefix object { path, type }



A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: string



The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

[](#beta_managed_agents_memory_prefix.path)

type: "memory_prefix"



[](#beta_managed_agents_memory_prefix.type)

[](#beta_managed_agents_memory_prefix)



BetaManagedAgentsMemoryView = "basic" or "full"



Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

One of the following:

"basic"



[](#beta_managed_agents_memory_view%5B0%5D)

"full"



[](#beta_managed_agents_memory_view%5B1%5D)

[](#beta_managed_agents_memory_view)



BetaManagedAgentsPrecondition object { type, content_sha256 }



Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: "content_sha256"



[](#beta_managed_agents_precondition.type)

content_sha256: optional string



Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

[](#beta_managed_agents_precondition.content_sha256)

[](#beta_managed_agents_precondition)
