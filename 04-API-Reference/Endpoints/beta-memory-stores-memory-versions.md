---
title: "Memory Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:37Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmemory_stores%2Fmemory_versions)

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

# Memory Versions

##### [List memory versions](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

##### [Retrieve a memory version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

##### [Redact a memory version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

##### Models



BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_session_actor) or [BetaManagedAgentsAPIActor](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_api_actor) or [BetaManagedAgentsUserActor](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_user_actor) or [BetaManagedAgentsServiceAccountActor](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_service_account_actor)

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

ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](beta-sessions-retrieve.md) for further provenance.

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
