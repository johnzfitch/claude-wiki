---
title: "List Code Artifacts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/code/artifacts/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:39:05Z"
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

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fcode%2Fartifacts%2Flist)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


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

Artifacts


List Code Artifacts


Download Code Artifact Version Content


Delete Code Artifact


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Code](https://platform.claude.com/docs/en/api/http/compliance/code)
4.  [Artifacts](https://platform.claude.com/docs/en/api/http/compliance/code/artifacts)

# List Code Artifacts

GET/v1/compliance/apps/code/artifacts

List Claude Code Artifacts owned by organizations under the parent organization.

Results are sorted by Artifact identifier. Pages may be short or empty while `next_page` is still set — continue until `next_page` is absent. Artifacts are sorted by identifier (not creation time): an Artifact published during an export may land before the cursor and be omitted, so for a point-in-time-complete export re-enumerate after publishing quiesces.

Artifacts owned by a since-deleted child organization are not returned.

##### Query parameters



limit: optional number



Maximum results (default: 20, max: 100)

default20

minimum1

maximum100



organization_ids: optional array of string



Filter by organization IDs (accepts `org_...` or organization UUID, up to 500). Enumerate IDs via `GET /v1/compliance/organizations`.

maxItems500

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



updated_at: optional object{ gt, gte, lt, lte }





gt: optional string



Return only Artifacts updated after this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

formatdate-time



gte: optional string



Return only Artifacts updated at or after this time (RFC 3339 format). Time filters match an eventually-consistent index and Artifacts published before this field was recorded never match — omit the time filter for compliance-complete enumeration. For incremental export, apply a generous overlap margin between windows and dedupe by `id`: adjacent tiling silently misses items whose index update lagged their publish.

formatdate-time



lt: optional string



Return only Artifacts updated before this time (RFC 3339 format). Multiple time operators are AND-ed to the tightest bound. See `updated_at.gte` for the completeness caveat.

formatdate-time



lte: optional string



Return only Artifacts updated at or before this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

formatdate-time



user_ids: optional array of string



Filter by owner user IDs (up to 200). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

maxItems200

##### Headers

"x-api-key": optional string



##### Returns



data: array of object{ id, organization_uuid, owner_user_id, 5 more }



Page of Artifacts

id: string



Artifact identifier (tagged ID)

organization_uuid: string



Organization UUID this Artifact belongs to

owner_user_id: string or null



Artifact owner's user identifier (tagged ID), or null for Artifacts published by an agent session rather than a user account. When set, it survives after the owner's account is deleted or the owner leaves every organization under the parent.

published_version_id: string or null



Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read_mode widened.



read_mode: "org" or "owner" or "public" or "users"



Who can view this Artifact: only its owner, a named set of users, every member of its organization, or anyone on the internet (`public`)

One of the following:

"org"



"owner"



"public"



"users"





updated_at: string or null



Artifact last update timestamp, or null for Artifacts published before this field was recorded

formatdate-time



user: object{ id, email_address } or null



Artifact owner with email, or null if the Artifact was published by an agent session, the owner's account has been deleted, or the owner is no longer a member of an organization the key may read

id: string



User identifier (tagged ID)

email_address: string



User's email address



versions: array of object{ id, created_at, name }



Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

id: string



Opaque version identifier



created_at: string or null



When this version was published

formatdate-time

name: string



Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.

has_more: boolean



Whether `next_page` is set. May be true for a page whose next page is empty — continue until `next_page` is absent.

next_page: string or null



Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Code Artifacts

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts \
    -H 'anthropic-version: 2023-06-01' \
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
