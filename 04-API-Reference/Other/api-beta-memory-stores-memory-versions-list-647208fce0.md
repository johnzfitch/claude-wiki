---
title: "List memory versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:41Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmemory_stores%2Fmemory_versions%2Flist)

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
4.  [Memory Versions](/docs/en/api/http/beta/memory_stores/memory_versions)

# List memory versions

GET/v1/memory_stores/{memory_store_id}/memory_versions

List memory versions

##### Path parameters

memory_store_id: string



The ID of the memory store whose version history to list (`memstore_...`).

##### Query parameters

api_key_id: optional string



Return only versions written with the API key that has this ID.



"created_at\[gte\]": optional string



Return versions created at or after this time (inclusive).

formatdate-time



"created_at\[lte\]": optional string



Return versions created at or before this time (inclusive).

formatdate-time



limit: optional number



The maximum number of versions to return per page. Defaults to 20.

formatint32



memory_id: optional string



Return only versions of the memory with this ID (`mem_...`).

The filter still works after the memory is deleted. The results then include the version whose `operation` is `deleted`.



operation: optional [BetaManagedAgentsMemoryVersionOperation](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_memory_version_operation)



Return only versions that record this kind of change.

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

page: optional string



The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

service_account_id: optional string



Return only versions written by the service account with this ID (`svac_...`).

session_id: optional string



Return only versions written by the session with this ID.



view: optional [BetaManagedAgentsMemoryView](/docs/en/api/http/beta/memory_stores/memories#beta_managed_agents_memory_view)



Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

One of the following:

"basic"



Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

"full"



Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/http/beta#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string





"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more



One of the following:

"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"





"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



data: optional array of [BetaManagedAgentsMemoryVersion](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_memory_version) { type: "memory_version", id, created_at, 10 more }



One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

type: "memory_version"



id: string



Unique identifier for this version (a `memver_...` value).



created_at: string



When this version was written, in RFC 3339 format.

formatdate-time

memory_id: string



ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

memory_store_id: string



ID of the memory store this version belongs to (a `memstore_...` value).



operation: [BetaManagedAgentsMemoryVersionOperation](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_memory_version_operation)



The kind of mutation this version records: `created`, `modified`, or `deleted`.

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

content: optional string or null



The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content_sha256: optional string or null



Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.



content_size_bytes: optional number or null



Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

formatint32



created_by: optional [BetaManagedAgentsActor](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_actor)



Who performed this write: one of `session_actor`, `api_actor`, `user_actor`, or `service_account_actor`; `null` when no writer is recorded. Captured at write time and preserved through redaction. A `session_actor` is an agent writing through the store's mounted filesystem at `/mnt/memory/`. The API key that created that session is not recorded on agent writes, so attribution names who made the write, not who is ultimately responsible; look up session provenance via the [Sessions API](/docs/en/api/beta/sessions/retrieve).

One of the following:

path: optional string or null



The memory's path at the time of this write. `null` if and only if `redacted_at` is set.



redacted_at: optional string or null



When this version was redacted, in RFC 3339 format, or `null` if it has not been redacted. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are all `null`. See [Redact a memory version](/docs/en/api/beta/memory_stores/memory_versions/redact).

formatdate-time



redacted_by: optional [BetaManagedAgentsActor](/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_actor)



Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

One of the following:

next_page: optional string or null



Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

List memory versions

cURL



```python
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
