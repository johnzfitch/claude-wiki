---
title: "User Profiles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/user_profiles"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:12Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Fuser_profiles)

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

# User Profiles

##### [Create User Profile](/docs/en/api/http/beta/user_profiles/create)

POST/v1/user_profiles

##### [List User Profiles](/docs/en/api/http/beta/user_profiles/list)

GET/v1/user_profiles

##### [Get User Profile](/docs/en/api/http/beta/user_profiles/retrieve)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](/docs/en/api/http/beta/user_profiles/update)

POST/v1/user_profiles/{user_profile_id}

##### [Create Enrollment URL](/docs/en/api/http/beta/user_profiles/create_enrollment_url)

POST/v1/user_profiles/{user_profile_id}/enrollment_url

##### Models



BetaUserProfile object{ type: "user_profile", id, created_at, 8 more }



A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.



BetaUserProfileEnrollmentURL object{ type: "enrollment_url", expires_at, url }



A URL to give to the entity that a user profile represents, so that the entity can enroll for a trust grant.

type: "enrollment_url"



Object type. Always `enrollment_url`.



expires_at: string



When this enrollment URL expires, in RFC 3339 format.

formatdate-time

url: string



Enrollment URL to send to the end user. Valid until `expires_at`.



BetaUserProfileExternalUserDetails object{ account_status, country, email_hash, 4 more }



Details about the entity this profile represents, as the platform states them. Anthropic does not verify them. Every field is present, `null` until the platform supplies a value.



BetaUserProfileExternalUserDetailsParams object{ account_status, country, email_hash, 4 more }





BetaUserProfileTrustGrant object{ status }



The status of one trust grant on a user profile, listed in the profile's `trust_grants` map under the grant's name.



status: "active" or "pending" or "rejected"



Status of the trust grant.
