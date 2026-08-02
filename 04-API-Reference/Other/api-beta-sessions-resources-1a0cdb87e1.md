---
title: "Resources - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/resources"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:13Z"
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


Create Session


List Sessions


Get Session


Update Session


Delete Session


Archive Session

Events

Resources


Add Session Resource


List Session Resources


Get Session Resource


Update Session Resource


Delete Session Resource

Threads

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

Resources




cURL

# Resources

##### [Add Session Resource](/docs/en/api/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

##### [List Session Resources](/docs/en/api/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

##### [Get Session Resource](/docs/en/api/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

##### [Update Session Resource](/docs/en/api/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

##### [Delete Session Resource](/docs/en/api/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

##### ModelsExpand Collapse 



BetaManagedAgentsDeleteSessionResource object { id, type }



Confirmation of resource deletion.

id: string



[](#beta_managed_agents_delete_session_resource.id)

type: "session_resource_deleted"



[](#beta_managed_agents_delete_session_resource.type)

[](#beta_managed_agents_delete_session_resource)



BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }



id: string



[](#beta_managed_agents_file_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.created_at)

file_id: string



[](#beta_managed_agents_file_resource.file_id)

mount_path: string



[](#beta_managed_agents_file_resource.mount_path)

type: "file"



[](#beta_managed_agents_file_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.updated_at)

[](#beta_managed_agents_file_resource)



BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }



id: string



[](#beta_managed_agents_github_repository_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.created_at)

mount_path: string



[](#beta_managed_agents_github_repository_resource.mount_path)

type: "github_repository"



[](#beta_managed_agents_github_repository_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.updated_at)

url: string



[](#beta_managed_agents_github_repository_resource.url)



checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta/sessions#beta_managed_agents_branch_checkout) { name, type } or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta/sessions#beta_managed_agents_commit_checkout) { sha, type }



One of the following:



BetaManagedAgentsBranchCheckout object { name, type }



name: string



Branch name to check out.

[](#beta_managed_agents_branch_checkout.name)

type: "branch"



[](#beta_managed_agents_branch_checkout.type)

[](#beta_managed_agents_branch_checkout)



BetaManagedAgentsCommitCheckout object { sha, type }



sha: string



Full commit SHA to check out.

[](#beta_managed_agents_commit_checkout.sha)

type: "commit"



[](#beta_managed_agents_commit_checkout.type)

[](#beta_managed_agents_commit_checkout)

[](#beta_managed_agents_github_repository_resource.checkout)

[](#beta_managed_agents_github_repository_resource)



BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }



A memory store attached to an agent session.

memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

[](#beta_managed_agents_memory_store_resource.memory_store_id)

type: "memory_store"



[](#beta_managed_agents_memory_store_resource.type)



access: optional "read_write" or "read_only"



Access mode for an attached memory store.

One of the following:

"read_write"



[](#beta_managed_agents_memory_store_resource.access%5B0%5D)

"read_only"



[](#beta_managed_agents_memory_store_resource.access%5B1%5D)

[](#beta_managed_agents_memory_store_resource.access)

description: optional string



Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

[](#beta_managed_agents_memory_store_resource.description)

instructions: optional string



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[](#beta_managed_agents_memory_store_resource.instructions)

mount_path: optional string



Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

[](#beta_managed_agents_memory_store_resource.mount_path)

name: optional string



Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

[](#beta_managed_agents_memory_store_resource.name)

[](#beta_managed_agents_memory_store_resource)



BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_github_repository_resource) { id, created_at, mount_path, 4 more } or [BetaManagedAgentsFileResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_file_resource) { id, created_at, file_id, 3 more } or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_memory_store_resource) { memory_store_id, type, access, 4 more }



A memory store attached to an agent session.

One of the following:



BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }



id: string



[](#beta_managed_agents_github_repository_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.created_at)

mount_path: string



[](#beta_managed_agents_github_repository_resource.mount_path)

type: "github_repository"



[](#beta_managed_agents_github_repository_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.updated_at)

url: string



[](#beta_managed_agents_github_repository_resource.url)



checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta/sessions#beta_managed_agents_branch_checkout) { name, type } or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta/sessions#beta_managed_agents_commit_checkout) { sha, type }



One of the following:



BetaManagedAgentsBranchCheckout object { name, type }



name: string



Branch name to check out.

[](#beta_managed_agents_branch_checkout.name)

type: "branch"



[](#beta_managed_agents_branch_checkout.type)

[](#beta_managed_agents_branch_checkout)



BetaManagedAgentsCommitCheckout object { sha, type }



sha: string



Full commit SHA to check out.

[](#beta_managed_agents_commit_checkout.sha)

type: "commit"



[](#beta_managed_agents_commit_checkout.type)

[](#beta_managed_agents_commit_checkout)

[](#beta_managed_agents_github_repository_resource.checkout)

[](#beta_managed_agents_github_repository_resource)



BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }



id: string



[](#beta_managed_agents_file_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.created_at)

file_id: string



[](#beta_managed_agents_file_resource.file_id)

mount_path: string



[](#beta_managed_agents_file_resource.mount_path)

type: "file"



[](#beta_managed_agents_file_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.updated_at)

[](#beta_managed_agents_file_resource)



BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }



A memory store attached to an agent session.

memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

[](#beta_managed_agents_memory_store_resource.memory_store_id)

type: "memory_store"



[](#beta_managed_agents_memory_store_resource.type)



access: optional "read_write" or "read_only"



Access mode for an attached memory store.

One of the following:

"read_write"



[](#beta_managed_agents_memory_store_resource.access%5B0%5D)

"read_only"



[](#beta_managed_agents_memory_store_resource.access%5B1%5D)

[](#beta_managed_agents_memory_store_resource.access)

description: optional string



Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

[](#beta_managed_agents_memory_store_resource.description)

instructions: optional string



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[](#beta_managed_agents_memory_store_resource.instructions)

mount_path: optional string



Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

[](#beta_managed_agents_memory_store_resource.mount_path)

name: optional string



Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

[](#beta_managed_agents_memory_store_resource.name)

[](#beta_managed_agents_memory_store_resource)

[](#beta_managed_agents_session_resource)



ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_github_repository_resource) { id, created_at, mount_path, 4 more } or [BetaManagedAgentsFileResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_file_resource) { id, created_at, file_id, 3 more } or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_memory_store_resource) { memory_store_id, type, access, 4 more }



The requested session resource.

One of the following:



BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }



id: string



[](#beta_managed_agents_github_repository_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.created_at)

mount_path: string



[](#beta_managed_agents_github_repository_resource.mount_path)

type: "github_repository"



[](#beta_managed_agents_github_repository_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.updated_at)

url: string



[](#beta_managed_agents_github_repository_resource.url)



checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta/sessions#beta_managed_agents_branch_checkout) { name, type } or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta/sessions#beta_managed_agents_commit_checkout) { sha, type }



One of the following:



BetaManagedAgentsBranchCheckout object { name, type }



name: string



Branch name to check out.

[](#beta_managed_agents_branch_checkout.name)

type: "branch"



[](#beta_managed_agents_branch_checkout.type)

[](#beta_managed_agents_branch_checkout)



BetaManagedAgentsCommitCheckout object { sha, type }



sha: string



Full commit SHA to check out.

[](#beta_managed_agents_commit_checkout.sha)

type: "commit"



[](#beta_managed_agents_commit_checkout.type)

[](#beta_managed_agents_commit_checkout)

[](#beta_managed_agents_github_repository_resource.checkout)

[](#beta_managed_agents_github_repository_resource)



BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }



id: string



[](#beta_managed_agents_file_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.created_at)

file_id: string



[](#beta_managed_agents_file_resource.file_id)

mount_path: string



[](#beta_managed_agents_file_resource.mount_path)

type: "file"



[](#beta_managed_agents_file_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.updated_at)

[](#beta_managed_agents_file_resource)



BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }



A memory store attached to an agent session.

memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

[](#beta_managed_agents_memory_store_resource.memory_store_id)

type: "memory_store"



[](#beta_managed_agents_memory_store_resource.type)



access: optional "read_write" or "read_only"



Access mode for an attached memory store.

One of the following:

"read_write"



[](#beta_managed_agents_memory_store_resource.access%5B0%5D)

"read_only"



[](#beta_managed_agents_memory_store_resource.access%5B1%5D)

[](#beta_managed_agents_memory_store_resource.access)

description: optional string



Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

[](#beta_managed_agents_memory_store_resource.description)

instructions: optional string



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[](#beta_managed_agents_memory_store_resource.instructions)

mount_path: optional string



Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

[](#beta_managed_agents_memory_store_resource.mount_path)

name: optional string



Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

[](#beta_managed_agents_memory_store_resource.name)

[](#beta_managed_agents_memory_store_resource)

[](#resource_retrieve_response)



ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_github_repository_resource) { id, created_at, mount_path, 4 more } or [BetaManagedAgentsFileResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_file_resource) { id, created_at, file_id, 3 more } or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/beta/sessions/resources#beta_managed_agents_memory_store_resource) { memory_store_id, type, access, 4 more }



The updated session resource.

One of the following:



BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more }



id: string



[](#beta_managed_agents_github_repository_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.created_at)

mount_path: string



[](#beta_managed_agents_github_repository_resource.mount_path)

type: "github_repository"



[](#beta_managed_agents_github_repository_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_github_repository_resource.updated_at)

url: string



[](#beta_managed_agents_github_repository_resource.url)



checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta/sessions#beta_managed_agents_branch_checkout) { name, type } or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta/sessions#beta_managed_agents_commit_checkout) { sha, type }



One of the following:



BetaManagedAgentsBranchCheckout object { name, type }



name: string



Branch name to check out.

[](#beta_managed_agents_branch_checkout.name)

type: "branch"



[](#beta_managed_agents_branch_checkout.type)

[](#beta_managed_agents_branch_checkout)



BetaManagedAgentsCommitCheckout object { sha, type }



sha: string



Full commit SHA to check out.

[](#beta_managed_agents_commit_checkout.sha)

type: "commit"



[](#beta_managed_agents_commit_checkout.type)

[](#beta_managed_agents_commit_checkout)

[](#beta_managed_agents_github_repository_resource.checkout)

[](#beta_managed_agents_github_repository_resource)



BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more }



id: string



[](#beta_managed_agents_file_resource.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.created_at)

file_id: string



[](#beta_managed_agents_file_resource.file_id)

mount_path: string



[](#beta_managed_agents_file_resource.mount_path)

type: "file"



[](#beta_managed_agents_file_resource.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_file_resource.updated_at)

[](#beta_managed_agents_file_resource)



BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more }



A memory store attached to an agent session.

memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

[](#beta_managed_agents_memory_store_resource.memory_store_id)

type: "memory_store"



[](#beta_managed_agents_memory_store_resource.type)



access: optional "read_write" or "read_only"



Access mode for an attached memory store.

One of the following:

"read_write"



[](#beta_managed_agents_memory_store_resource.access%5B0%5D)

"read_only"



[](#beta_managed_agents_memory_store_resource.access%5B1%5D)

[](#beta_managed_agents_memory_store_resource.access)

description: optional string



Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

[](#beta_managed_agents_memory_store_resource.description)

instructions: optional string



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[](#beta_managed_agents_memory_store_resource.instructions)

mount_path: optional string



Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

[](#beta_managed_agents_memory_store_resource.mount_path)

name: optional string



Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

[](#beta_managed_agents_memory_store_resource.name)

[](#beta_managed_agents_memory_store_resource)
