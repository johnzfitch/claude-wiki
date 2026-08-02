---
title: "User Profiles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/user_profiles"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:17Z"
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


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

User profiles




cURL

# User Profiles

##### [Create User Profile](/docs/en/api/beta/user_profiles/create)

POST/v1/user_profiles

##### [List User Profiles](/docs/en/api/beta/user_profiles/list)

GET/v1/user_profiles

##### [Get User Profile](/docs/en/api/beta/user_profiles/retrieve)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](/docs/en/api/beta/user_profiles/update)

POST/v1/user_profiles/{user_profile_id}

##### [Create Enrollment URL](/docs/en/api/beta/user_profiles/create_enrollment_url)

POST/v1/user_profiles/{user_profile_id}/enrollment_url

##### ModelsExpand Collapse 



BetaUserProfile object { id, created_at, metadata, 6 more }



id: string



Unique identifier for this user profile, prefixed `uprof_`.

[](#beta_user_profile.id)

created_at: string



A timestamp in RFC 3339 format

[](#beta_user_profile.created_at)

metadata: map\[string\]



Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

[](#beta_user_profile.metadata)



relationship: "external" or "resold" or "internal"



How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

One of the following:

"external"



[](#beta_user_profile.relationship%5B0%5D)

"resold"



[](#beta_user_profile.relationship%5B1%5D)

"internal"



[](#beta_user_profile.relationship%5B2%5D)

[](#beta_user_profile.relationship)



trust_grants: map\[[BetaUserProfileTrustGrant](/docs/en/api/beta/user_profiles#beta_user_profile_trust_grant) { status } \]



Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.



status: "active" or "pending" or "rejected"



Status of the trust grant.

One of the following:

"active"



[](#beta_user_profile_trust_grant.status%5B0%5D)

"pending"



[](#beta_user_profile_trust_grant.status%5B1%5D)

"rejected"



[](#beta_user_profile_trust_grant.status%5B2%5D)

[](#beta_user_profile_trust_grant.status)

[](#beta_user_profile.trust_grants)

type: "user_profile"



Object type. Always `user_profile`.

[](#beta_user_profile.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_user_profile.updated_at)

external_id: optional string



Platform's own identifier for this user. Not enforced unique.

[](#beta_user_profile.external_id)

name: optional string



Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

[](#beta_user_profile.name)

[](#beta_user_profile)



BetaUserProfileEnrollmentURL object { expires_at, type, url }



expires_at: string



A timestamp in RFC 3339 format

[](#beta_user_profile_enrollment_url.expires_at)

type: "enrollment_url"



Object type. Always `enrollment_url`.

[](#beta_user_profile_enrollment_url.type)

url: string



Enrollment URL to send to the end user. Valid until `expires_at`.

[](#beta_user_profile_enrollment_url.url)

[](#beta_user_profile_enrollment_url)



BetaUserProfileTrustGrant object { status }





status: "active" or "pending" or "rejected"



Status of the trust grant.

One of the following:

"active"



[](#beta_user_profile_trust_grant.status%5B0%5D)

"pending"



[](#beta_user_profile_trust_grant.status%5B1%5D)

"rejected"



[](#beta_user_profile_trust_grant.status%5B2%5D)

[](#beta_user_profile_trust_grant.status)

[](#beta_user_profile_trust_grant)
