---
title: "List User Profiles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/user_profiles/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-21T06:29:08Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fuser_profiles%2Flist)





SearchCtrlK

Include beta APIs

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


Organization


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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations

Webhooks


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


Compliance API

Activities

Organizations

Groups

Apps


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-user-profiles-list.md).

1.  [API reference](http.md)
2.  [User Profiles](https://platform.claude.com/docs/en/api/http/user_profiles)

# List User Profiles

Copy page



cURL

GET/v1/user_profiles

List User Profiles

##### Query parameters



limit: optional number



The maximum number of user profiles to return, from 1 to 100. Defaults to 20.

formatint32



order: optional [UserProfileListOrder](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_list_order)



The sort direction, applied to the field that `order_by` selects. Defaults to `desc`.

One of the following:

"asc"



Oldest first when `order_by` is `created_at`, or names in ascending order when `order_by` is `name`.

"desc"



Newest first when `order_by` is `created_at`, or names in descending order when `order_by` is `name`. This is the default.



order_by: optional [UserProfileListOrderBy](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_list_order_by)



The field to sort user profiles by, in the direction that `order` sets. Defaults to `created_at`.

One of the following:

"created_at"



Sort by when each user profile was created. This is the default.

"name"



Sort by `name`, ignoring the case of ASCII letters. Profiles without a name come last in either direction.



page: optional string



The cursor for the page to return, taken from `next_page` in a previous response.

Leave it out to get the first page.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



data: array of [UserProfile](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile) { type: "user_profile", id, access_type, 6 more }



User profiles on this page.

type: "user_profile"



Object type. Always `user_profile`.

id: string



Unique identifier for this user profile, prefixed `uprof_`.



access_type: [UserProfileAccessType](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_access_type)



How the platform uses the API for this entity: `application` (default) or `passthrough`. Absent under the legacy `user-profiles-2026-03-24` beta header.

One of the following:

"application"



The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

"passthrough"



The user profile represents a company that the platform resells Claude access to.



created_at: string



When this user profile was created, in RFC 3339 format.

formatdate-time



external_user_details: [UserProfileExternalUserDetails](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_external_user_details) { account_status, country, email_hash, 4 more }



Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Every field is present, `null` until the platform supplies a value. Absent under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which serve `reference_id` as the top-level `external_id` and, under `user-profiles-2026-08-18`, `onboarded_at` as `external_user_onboarded_at`.

metadata: map\[string\]



Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

name: string or null



Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name. `null` until the platform supplies one.



programs: [UserProfilePrograms](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_programs) { cyber, efs }



The profile's standing in each Anthropic program, such as the Cyber Verification Program. Present when the request sends no user-profiles beta header; absent under the `user-profiles-2026-09-04` and earlier beta headers, which serve `trust_grants` instead.



updated_at: string



When this user profile was last modified, in RFC 3339 format. It normally also updates shortly after Anthropic gives the profile an approval or withdraws one. Other changes to the statuses that Anthropic reports do not always update it, so read the status itself rather than watching this timestamp.

formatdate-time

next_page: string or null



Cursor for the next page, or `null` when there are no more results.

List User Profiles

cURL



```python
curl https://api.anthropic.com/v1/user_profiles \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "access_type": "application",
      "created_at": "2026-03-15T10:00:00Z",
      "external_user_details": {
        "account_status": "active",
        "country": "US",
        "email_hash": null,
        "entity_type": "business",
        "name_hash": null,
        "onboarded_at": "2024-11-02T08:15:00Z",
        "reference_id": "user_12345"
      },
      "metadata": {},
      "name": "Example User",
      "programs": {
        "cyber": {
          "requirements": {
            "data_retention": true,
            "human_review": true
          },
          "status": "active",
          "tiers": {}
        },
        "efs": {
          "features": {
            "data_retention_exemption": {
              "status": "inactive"
            },
            "cmek": {
              "status": "active"
            },
            "storage": {
              "status": "inactive"
            }
          },
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "access_type": "application",
      "created_at": "2026-03-15T10:00:00Z",
      "external_user_details": {
        "account_status": "active",
        "country": "US",
        "email_hash": null,
        "entity_type": "business",
        "name_hash": null,
        "onboarded_at": "2024-11-02T08:15:00Z",
        "reference_id": "user_12345"
      },
      "metadata": {},
      "name": "Example User",
      "programs": {
        "cyber": {
          "requirements": {
            "data_retention": true,
            "human_review": true
          },
          "status": "active",
          "tiers": {}
        },
        "efs": {
          "features": {
            "data_retention_exemption": {
              "status": "inactive"
            },
            "cmek": {
              "status": "active"
            },
            "storage": {
              "status": "inactive"
            }
          },
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
