---
title: "Memory Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:01Z"
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

Memory Versions


List memory versions


Retrieve a memory version


Redact a memory version


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

Memory versions




cURL

# Memory Versions

##### [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

##### [Retrieve a memory version](/docs/en/api/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

##### [Redact a memory version](/docs/en/api/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

##### ModelsExpand Collapse 



BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](/docs/en/api/beta/memory_stores/memory_versions#beta_managed_agents_session_actor) { session_id, type } or [BetaManagedAgentsAPIActor](/docs/en/api/beta/memory_stores/memory_versions#beta_managed_agents_api_actor) { api_key_id, type } or [BetaManagedAgentsUserActor](/docs/en/api/beta/memory_stores/memory_versions#beta_managed_agents_user_actor) { type, user_id }



Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

One of the following:



BetaManagedAgentsSessionActor object { session_id, type }



Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session_id: string



ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

[](#beta_managed_agents_session_actor.session_id)

type: "session_actor"



[](#beta_managed_agents_session_actor.type)

[](#beta_managed_agents_session_actor)



BetaManagedAgentsAPIActor object { api_key_id, type }



Attribution for a write made directly via the public API (outside of any session).

api_key_id: string



ID of the API key that performed the write. This identifies the key, not the secret.

[](#beta_managed_agents_api_actor.api_key_id)

type: "api_actor"



[](#beta_managed_agents_api_actor.type)

[](#beta_managed_agents_api_actor)



BetaManagedAgentsUserActor object { type, user_id }



Attribution for a write made by a human user through the Anthropic Console.

type: "user_actor"



[](#beta_managed_agents_user_actor.type)

user_id: string



ID of the user who performed the write (a `user_...` value).

[](#beta_managed_agents_user_actor.user_id)

[](#beta_managed_agents_user_actor)

[](#beta_managed_agents_actor)



BetaManagedAgentsAPIActor object { api_key_id, type }



Attribution for a write made directly via the public API (outside of any session).

api_key_id: string



ID of the API key that performed the write. This identifies the key, not the secret.

[](#beta_managed_agents_api_actor.api_key_id)

type: "api_actor"



[](#beta_managed_agents_api_actor.type)

[](#beta_managed_agents_api_actor)



BetaManagedAgentsMemoryVersion object { id, created_at, memory_id, 10 more }



A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

id: string



Unique identifier for this version (a `memver_...` value).

[](#beta_managed_agents_memory_version.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory_version.created_at)

memory_id: string



ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

[](#beta_managed_agents_memory_version.memory_id)

memory_store_id: string



ID of the memory store this version belongs to (a `memstore_...` value).

[](#beta_managed_agents_memory_version.memory_store_id)



operation: [BetaManagedAgentsMemoryVersionOperation](/docs/en/api/beta/memory_stores/memory_versions#beta_managed_agents_memory_version_operation)



The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

"created"



[](#beta_managed_agents_memory_version.operation%20%2B%20(resource)%20beta.memory_stores.memory_versions%5B0%5D)

"modified"



[](#beta_managed_agents_memory_version.operation%20%2B%20(resource)%20beta.memory_stores.memory_versions%5B1%5D)

"deleted"



[](#beta_managed_agents_memory_version.operation%20%2B%20(resource)%20beta.memory_stores.memory_versions%5B2%5D)

[](#beta_managed_agents_memory_version.operation)

type: "memory_version"



[](#beta_managed_agents_memory_version.type)

content: optional string



The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

[](#beta_managed_agents_memory_version.content)

content_sha256: optional string



Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

[](#beta_managed_agents_memory_version.content_sha256)

content_size_bytes: optional number



Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

[](#beta_managed_agents_memory_version.content_size_bytes)



created_by: optional [BetaManagedAgentsActor](/docs/en/api/beta/memory_stores/memory_versions#beta_managed_agents_actor)



Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

One of the following:



BetaManagedAgentsSessionActor object { session_id, type }



Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session_id: string



ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.session_id)

type: "session_actor"



[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.type)

[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions)



BetaManagedAgentsAPIActor object { api_key_id, type }



Attribution for a write made directly via the public API (outside of any session).

api_key_id: string



ID of the API key that performed the write. This identifies the key, not the secret.

[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.api_key_id)

type: "api_actor"



[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.type)

[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions)



BetaManagedAgentsUserActor object { type, user_id }



Attribution for a write made by a human user through the Anthropic Console.

type: "user_actor"



[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.type)

user_id: string



ID of the user who performed the write (a `user_...` value).

[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.user_id)

[](#beta_managed_agents_memory_version.created_by%20%2B%20(resource)%20beta.memory_stores.memory_versions)

[](#beta_managed_agents_memory_version.created_by)

path: optional string



The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

[](#beta_managed_agents_memory_version.path)

redacted_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory_version.redacted_at)



redacted_by: optional [BetaManagedAgentsActor](/docs/en/api/beta/memory_stores/memory_versions#beta_managed_agents_actor)



Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

One of the following:



BetaManagedAgentsSessionActor object { session_id, type }



Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session_id: string



ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.session_id)

type: "session_actor"



[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.type)

[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions)



BetaManagedAgentsAPIActor object { api_key_id, type }



Attribution for a write made directly via the public API (outside of any session).

api_key_id: string



ID of the API key that performed the write. This identifies the key, not the secret.

[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.api_key_id)

type: "api_actor"



[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.type)

[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions)



BetaManagedAgentsUserActor object { type, user_id }



Attribution for a write made by a human user through the Anthropic Console.

type: "user_actor"



[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.type)

user_id: string



ID of the user who performed the write (a `user_...` value).

[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions.user_id)

[](#beta_managed_agents_memory_version.redacted_by%20%2B%20(resource)%20beta.memory_stores.memory_versions)

[](#beta_managed_agents_memory_version.redacted_by)

[](#beta_managed_agents_memory_version)



BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"



The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

"created"



[](#beta_managed_agents_memory_version_operation%5B0%5D)

"modified"



[](#beta_managed_agents_memory_version_operation%5B1%5D)

"deleted"



[](#beta_managed_agents_memory_version_operation%5B2%5D)

[](#beta_managed_agents_memory_version_operation)



BetaManagedAgentsSessionActor object { session_id, type }



Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session_id: string



ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

[](#beta_managed_agents_session_actor.session_id)

type: "session_actor"



[](#beta_managed_agents_session_actor.type)

[](#beta_managed_agents_session_actor)



BetaManagedAgentsUserActor object { type, user_id }



Attribution for a write made by a human user through the Anthropic Console.

type: "user_actor"



[](#beta_managed_agents_user_actor.type)

user_id: string



ID of the user who performed the write (a `user_...` value).

[](#beta_managed_agents_user_actor.user_id)

[](#beta_managed_agents_user_actor)
