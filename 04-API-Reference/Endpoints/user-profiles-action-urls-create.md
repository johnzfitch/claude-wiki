---
title: "Create Action URL - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/user_profiles/action_urls/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-21T06:29:17Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fuser_profiles%2Faction_urls%2Fcreate)

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



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls/create).

1.  [API reference](http.md)
2.  [User Profiles](https://platform.claude.com/docs/en/api/http/user_profiles)
3.  [Action URLs](https://platform.claude.com/docs/en/api/http/user_profiles/action_urls)

# Create Action URL

Copy page



cURL

POST/v1/user_profiles/{user_profile_id}/action_urls

Create Action URL

##### Path parameters

user_profile_id: string



The ID of the user profile the action is for (`uprof_...`).

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

action: [UserProfileAction](https://platform.claude.com/docs/en/api/http/user_profiles/action_urls#user_profile_action)



The action that the person who opens the URL takes.

One of the following:



UserProfileEnrollEndUserAction object{ type: "enroll_end_user" }



The end-user that the profile represents enrolls in a program.

type: "enroll_end_user"



##### Returns



UserProfileActionURL object{ type: "user_profile_action_url", expires_at, url }

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

Create Action URL

cURL



```python
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID/action_urls \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "action": {
            "type": "enroll_end_user"
          }
        }'
```

Response 200



```python
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "user_profile_action_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

##### Returns Examples

Response 200



```python
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "user_profile_action_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
