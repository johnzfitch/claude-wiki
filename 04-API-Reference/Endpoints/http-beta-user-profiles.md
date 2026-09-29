---
title: "User Profiles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/user_profiles"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:39:12Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Fuser_profiles)

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

# User Profiles

##### [Create User Profile](http-beta-user-profiles-create.md)

POST/v1/user_profiles

##### [List User Profiles](http-beta-user-profiles-list.md)

GET/v1/user_profiles

##### [Get User Profile](http-beta-user-profiles-retrieve.md)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](http-beta-user-profiles-update.md)

POST/v1/user_profiles/{user_profile_id}

##### [Create Enrollment URL](http-beta-user-profiles-create-enrollment-url.md)

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
