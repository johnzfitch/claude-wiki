---
title: "Memory Stores - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:38Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmemory_stores)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)

# Memory Stores

##### [Create a memory store](/docs/en/api/http/beta/memory_stores/create)

POST/v1/memory_stores

##### [List memory stores](/docs/en/api/http/beta/memory_stores/list)

GET/v1/memory_stores

##### [Retrieve a memory store](/docs/en/api/http/beta/memory_stores/retrieve)

GET/v1/memory_stores/{memory_store_id}

##### [Update a memory store](/docs/en/api/http/beta/memory_stores/update)

POST/v1/memory_stores/{memory_store_id}

##### [Delete a memory store](/docs/en/api/http/beta/memory_stores/delete)

DELETE/v1/memory_stores/{memory_store_id}

##### [Archive a memory store](/docs/en/api/http/beta/memory_stores/archive)

POST/v1/memory_stores/{memory_store_id}/archive

##### Models



BetaManagedAgentsDeletedMemoryStore object{ type: "memory_store_deleted", id }



Confirmation that a `memory_store` was deleted.

type: "memory_store_deleted"



id: string



ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.



BetaManagedAgentsMemoryStore object{ type: "memory_store", id, created_at, 5 more }



A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

type: "memory_store"



id: string



Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.



created_at: string



Timestamp when the store was created.

formatdate-time

name: string



Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.



updated_at: string



Timestamp when the store's `name`, `description`, or `metadata` was last modified. Memory writes inside the store do not advance this.

formatdate-time



archived_at: optional string or null



Timestamp when the store was archived, or `null` if active. Set once and never cleared; archiving is one-way. Archived stores are read-only and cannot be attached to new sessions.

formatdate-time

description: optional string



Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

metadata: optional map\[string\]



Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory Stores[Memories](/docs/en/api/http/beta/memory_stores/memories)

##### [Create a memory](/docs/en/api/http/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

##### [List memories](/docs/en/api/http/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

##### [Retrieve a memory](/docs/en/api/http/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Update a memory](/docs/en/api/http/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Delete a memory](/docs/en/api/http/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

#### Memory Stores[Memory Versions](/docs/en/api/http/beta/memory_stores/memory_versions)

##### [List memory versions](/docs/en/api/http/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

##### [Retrieve a memory version](/docs/en/api/http/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

##### [Redact a memory version](/docs/en/api/http/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact
