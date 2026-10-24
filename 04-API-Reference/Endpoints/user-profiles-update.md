---
title: "Update User Profile - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/user_profiles/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-21T06:29:39Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fuser_profiles%2Fupdate)

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

A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-user-profiles-update.md).

1.  [API reference](http.md)
2.  [User Profiles](https://platform.claude.com/docs/en/api/http/user_profiles)

# Update User Profile

Copy page



cURL

POST/v1/user_profiles/{user_profile_id}

Update User Profile

##### Path parameters

user_profile_id: string



The ID of the user profile to update (`uprof_...`).

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

##### Body



access_type: optional [UserProfileAccessType](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_access_type) or null



If present, replaces the stored access type. Omit to leave unchanged.

One of the following:

"application"



The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

"passthrough"



The user profile represents a company that the platform resells Claude access to.



external_user_details: optional [UserProfileExternalUserDetailsParams](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_external_user_details_params) { account_status, country, email_hash, 4 more }



Details about the entity this profile represents, as the platform states them. Each field sent replaces the stored value; omit a field to leave it unchanged. Once set, a value cannot be cleared and `null` is rejected. Not accepted under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers.

metadata: optional map\[string\]



Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.



name: optional string or null



If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

minLength1

maxLength255

##### Returns



UserProfile object{ type: "user_profile", id, access_type, 6 more }



A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

Update User Profile

cURL



```python
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "external_user_details": {
            "account_status": "suspended"
          }
        }'
```

Response 200



```python
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
      "tiers": {
        "a": {
          "status": "inactive"
        },
        "b": {
          "status": "inactive"
        },
        "c": {
          "status": "inactive"
        }
      }
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
```

##### Returns Examples

Response 200



```python
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
      "tiers": {
        "a": {
          "status": "inactive"
        },
        "b": {
          "status": "inactive"
        },
        "c": {
          "status": "inactive"
        }
      }
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
