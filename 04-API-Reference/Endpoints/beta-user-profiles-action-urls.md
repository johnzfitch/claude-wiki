---
title: "Action URLs - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/user_profiles/action_urls"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-21T06:29:35Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fuser_profiles%2Faction_urls)

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


Create Action URL


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

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [User Profiles](platform-claude-com-http-beta-user-profiles.md)

# Action URLs

Copy page



cURL

##### [Create Action URL](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls/create)

POST/v1/user_profiles/{user_profile_id}/action_urls

##### Models



BetaUserProfileAction = [BetaUserProfileEnrollEndUserAction](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls#beta_user_profile_enroll_end_user_action)



The action that the person who opens the URL takes, discriminated by `type`.

One of the following:



BetaUserProfileEnrollEndUserAction object{ type: "enroll_end_user" }



The end-user that the profile represents enrolls in a program.

type: "enroll_end_user"





BetaUserProfileActionURL object{ type: "user_profile_action_url", expires_at, url }



A URL to give to the person who takes the requested action.

type: "user_profile_action_url"



Object type. Always `user_profile_action_url`.



expires_at: string



When the URL stops working, in RFC 3339 format.

formatdate-time

url: string



The URL to give to the person who takes the action. Anyone who holds it can open it until `expires_at`.



BetaUserProfileEnrollEndUserAction object{ type: "enroll_end_user" }



The end-user that the profile represents enrolls in a program.
