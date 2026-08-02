---
title: "Memory Stores - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:34Z"
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

Memory stores




cURL

# Memory Stores

##### [Create a memory store](/docs/en/api/beta/memory_stores/create)

POST/v1/memory_stores

##### [List memory stores](/docs/en/api/beta/memory_stores/list)

GET/v1/memory_stores

##### [Retrieve a memory store](/docs/en/api/beta/memory_stores/retrieve)

GET/v1/memory_stores/{memory_store_id}

##### [Update a memory store](/docs/en/api/beta/memory_stores/update)

POST/v1/memory_stores/{memory_store_id}

##### [Delete a memory store](/docs/en/api/beta/memory_stores/delete)

DELETE/v1/memory_stores/{memory_store_id}

##### [Archive a memory store](/docs/en/api/beta/memory_stores/archive)

POST/v1/memory_stores/{memory_store_id}/archive

##### ModelsExpand Collapse 



BetaManagedAgentsDeletedMemoryStore object { id, type }



Confirmation that a `memory_store` was deleted.

id: string



ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

[](#beta_managed_agents_deleted_memory_store.id)

type: "memory_store_deleted"



[](#beta_managed_agents_deleted_memory_store.type)

[](#beta_managed_agents_deleted_memory_store)



BetaManagedAgentsMemoryStore object { id, created_at, name, 5 more }



A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

id: string



Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

[](#beta_managed_agents_memory_store.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory_store.created_at)

name: string



Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

[](#beta_managed_agents_memory_store.name)

type: "memory_store"



[](#beta_managed_agents_memory_store.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory_store.updated_at)

archived_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_memory_store.archived_at)

description: optional string



Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

[](#beta_managed_agents_memory_store.description)

metadata: optional map\[string\]



Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

[](#beta_managed_agents_memory_store.metadata)

[](#beta_managed_agents_memory_store)

#### Memory StoresMemories

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

#### Memory StoresMemory Versions

##### [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

##### [Retrieve a memory version](/docs/en/api/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

##### [Redact a memory version](/docs/en/api/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact
