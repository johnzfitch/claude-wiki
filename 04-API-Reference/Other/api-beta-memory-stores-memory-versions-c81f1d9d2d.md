---
title: "Memory Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:37Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmemory_stores%2Fmemory_versions)

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


List memory versions


Retrieve a memory version


Redact a memory version

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
3.  [Memory Stores](/docs/en/api/http/beta/memory_stores)

# Memory Versions

##### [List memory versions](/docs/en/api/http/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

##### [Retrieve a memory version](/docs/en/api/http/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

##### [Redact a memory version](/docs/en/api/http/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

##### Models



BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_session_actor) or [BetaManagedAgentsAPIActor](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_api_actor) or [BetaManagedAgentsUserActor](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_user_actor) or [BetaManagedAgentsServiceAccountActor](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_service_account_actor)



Identifies who performed an operation. Recorded when the operation happens and not updated afterwards, so the ID may refer to a user, service account, API key, or session that has since been deleted.

One of the following:



BetaManagedAgentsAPIActor object{ type: "api_actor", api_key_id }



A direct caller of the public API, identified by the API key that authenticated the request.

type: "api_actor"





api_key_id: string



ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

minLength1



BetaManagedAgentsMemoryVersion object{ type: "memory_version", id, created_at, 10 more }



A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.



BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"



The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

One of the following:

"created"



The memory was created. The first version in any memory's lineage.

"modified"



The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

"deleted"



The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.



BetaManagedAgentsServiceAccountActor object{ type: "service_account_actor", service_account_id }



A workload authenticated as a service account, for example via Workload Identity Federation.

type: "service_account_actor"





service_account_id: string



ID of the service account (a `svac_...` value).

minLength1



BetaManagedAgentsSessionActor object{ type: "session_actor", session_id }



An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

type: "session_actor"





session_id: string



ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/beta/sessions/retrieve) for further provenance.

minLength1



BetaManagedAgentsUserActor object{ type: "user_actor", user_id }



A human user, for example acting through the Anthropic Console.

type: "user_actor"





user_id: string



ID of the user (a `user_...` value).
