---
title: "List organization members' personal preferences - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/user_preferences/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-20T06:39:10Z"
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

[API reference](../Endpoints/overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Forganizations%2Fuser_preferences%2Flist)

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


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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


List organizations

Users

User Preferences


List organization members' personal preferences

Roles

Settings


Plugins

Groups

Apps


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Organizations](https://platform.claude.com/docs/en/api/http/compliance/organizations)
4.  [User Preferences](https://platform.claude.com/docs/en/api/http/compliance/organizations/user_preferences)

# List organization members' personal preferences

Copy page



GET/v1/compliance/organizations/{org_uuid}/user_preferences

List the personal preferences of an organization's current members.

Returns each member's "Instructions for Claude" and Cowork "Global instructions" text. Both are account-level settings: the same text is returned under every organization the member belongs to. Members are listed in the order they joined the organization, oldest first; use `limit` and `page` to paginate. A page may hold fewer than `limit` rows, or none at all, without being the last page: the server bounds the work it does per request. Follow `next_page` until it is `null`.

##### Path parameters

org_uuid: string



The organization's UUID

##### Query parameters



include_unset: optional boolean



When true, list every current member, with `null` for each value they have not set. By default only members with at least one value set are listed.

defaultfalse



limit: optional number



Maximum results (default: 20, max: 100)

default20

minimum1

maximum100

page: optional string



Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



user_ids: optional array of string



Restrict the list to these users (max 10 per request). An entry that does not name a current member of the organization matches nothing. Omit to list every eligible member. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

maxItems10

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



##### Returns



data: array of object{ conversation_preferences, cowork_global_instructions, user }



Current organization members in the order they joined the organization, oldest first. By default only members with at least one value set are listed; with `include_unset=true` every member is.

conversation_preferences: string or null



The member's "Instructions for Claude" text from their personal settings, with leading and trailing whitespace removed. `null` when the member has never set it or has cleared it.

cowork_global_instructions: string or null



The member's "Global instructions" text for Cowork, Claude's desktop agent, with leading and trailing whitespace removed. `null` when the member has never set it or has cleared it.



user: object{ id, email_address }



The organization member.

id: string



User identifier

email_address: string



User's current email address

has_more: boolean



Whether there is a further page to request. A page can hold fewer records than `limit`, or none, and still have more: the server bounds the work it does per request.

next_page: string or null



Token to retrieve the next page. Use this as the 'page' parameter in your next request; `null` on the last page.

List organization members' personal preferences

cURL



```python
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/user_preferences \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "conversation_preferences": "Always answer in British English.",
      "cowork_global_instructions": "Prefer short status updates.",
      "user": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "email_address": "jane.doe@example.com"
      }
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
      "conversation_preferences": "Always answer in British English.",
      "cowork_global_instructions": "Prefer short status updates.",
      "user": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "email_address": "jane.doe@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
