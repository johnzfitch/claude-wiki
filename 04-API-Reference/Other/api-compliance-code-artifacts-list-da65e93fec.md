---
title: "List Code Artifacts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/code/artifacts/list"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:47Z"
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

Artifacts


List Code Artifacts


Download Code Artifact Version Content


Delete Code Artifact


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

List






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# List Code Artifacts

GET/v1/compliance/apps/code/artifacts

List Claude Code Artifacts owned by organizations under the parent organization.

Results are sorted by Artifact identifier. Pages may be short or empty while `next_page` is still set — continue until `next_page` is absent. Artifacts are sorted by identifier (not creation time): an Artifact published during an export may land before the cursor and be omitted, so for a point-in-time-complete export re-enumerate after publishing quiesces.

Artifacts owned by a since-deleted child organization are not returned.

##### Query ParametersExpand Collapse 

limit: optional number



Maximum results (default: 20, max: 100)

[](#list.limit)

organization_ids: optional array of string



Filter by organization IDs (accepts `org_...` or organization UUID, up to 500). Enumerate IDs via `GET /v1/compliance/organizations`.

[](#list.organization_ids)

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

[](#list.page)



updated_at: optional object { gt, gte, lt, lte }



gt: optional string



Return only Artifacts updated after this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

[](#list.updated_at.gt)

gte: optional string



Return only Artifacts updated at or after this time (RFC 3339 format). Time filters match an eventually-consistent index and Artifacts published before this field was recorded never match — omit the time filter for compliance-complete enumeration. For incremental export, apply a generous overlap margin between windows and dedupe by `id`: adjacent tiling silently misses items whose index update lagged their publish.

[](#list.updated_at.gte)

lt: optional string



Return only Artifacts updated before this time (RFC 3339 format). Multiple time operators are AND-ed to the tightest bound. See `updated_at.gte` for the completeness caveat.

[](#list.updated_at.lt)

lte: optional string



Return only Artifacts updated at or before this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

[](#list.updated_at.lte)

[](#list.updated_at)

user_ids: optional array of string



Filter by owner user IDs (up to 200). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

[](#list.user_ids)

##### Header ParametersExpand Collapse 

"x-api-key": optional string



[](#list.x-api-key)

##### ReturnsExpand Collapse 



data: array of object { id, organization_uuid, owner_user_id, 5 more }



Page of Artifacts

id: string



Artifact identifier (tagged ID)

[](#artifact_list_response.id)

organization_uuid: string



Organization UUID this Artifact belongs to

[](#artifact_list_response.organization_uuid)

owner_user_id: string



Artifact owner's user identifier (tagged ID). Always set, so attribution survives after the owner's account is deleted or the owner leaves every organization under the parent.

[](#artifact_list_response.owner_user_id)

published_version_id: string



Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read_mode widened.

[](#artifact_list_response.published_version_id)



read_mode: "org" or "owner" or "public" or "users"



Who can view this Artifact: only its owner, a named set of users, every member of its organization, or anyone on the internet (`public`)

One of the following:

"org"



[](#artifact_list_response.read_mode%5B0%5D)

"owner"



[](#artifact_list_response.read_mode%5B1%5D)

"public"



[](#artifact_list_response.read_mode%5B2%5D)

"users"



[](#artifact_list_response.read_mode%5B3%5D)

[](#artifact_list_response.read_mode)

updated_at: string



Artifact last update timestamp, or null for Artifacts published before this field was recorded

[](#artifact_list_response.updated_at)



user: object { id, email_address }



The user who owns a Code Artifact.

Fields that reference this type are null when the owner's account has been deleted or the owner is no longer a member of any organization under the parent organization.

id: string



User identifier (tagged ID)

[](#artifact_list_response.user.id)

email_address: string



User's email address

[](#artifact_list_response.user.email_address)

[](#artifact_list_response.user)



versions: array of object { id, created_at, name }



Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

id: string



Opaque version identifier

[](#artifact_list_response.versions.items.id)

created_at: string



When this version was published

[](#artifact_list_response.versions.items.created_at)

name: string



Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.

[](#artifact_list_response.versions.items.name)

[](#artifact_list_response.versions)

[](#list)

has_more: boolean



Whether `next_page` is set. May be true for a page whose next page is empty — continue until `next_page` is absent.

[](#list)

next_page: string



Token to retrieve the next page. Use this as the 'page' parameter in your next request

[](#list)

List Code Artifacts



```python
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "cart_01Tu9VwXyZaBcDeFgHiJkLmN",
      "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "owner_user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "published_version_id": "1741803761-9f3a",
      "read_mode": "org",
      "updated_at": "2025-03-14T09:05:17.456789Z",
      "user": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "email_address": "jane.doe@example.com"
      },
      "versions": [
        {
          "id": "1741803761-9f3a",
          "created_at": "2025-03-12T18:22:41.123456Z",
          "name": "Team dashboard"
        }
      ]
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "cart_01Tu9VwXyZaBcDeFgHiJkLmN",
      "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "owner_user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "published_version_id": "1741803761-9f3a",
      "read_mode": "org",
      "updated_at": "2025-03-14T09:05:17.456789Z",
      "user": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "email_address": "jane.doe@example.com"
      },
      "versions": [
        {
          "id": "1741803761-9f3a",
          "created_at": "2025-03-12T18:22:41.123456Z",
          "name": "Team dashboard"
        }
      ]
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
