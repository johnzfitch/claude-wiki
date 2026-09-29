---
title: "List Spend Limit Increase Requests - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-27T06:27:04Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fspend_limits%2Fincrease_requests%2Flist)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


Set Spend Limit


Get Spend Limit


Delete Spend Limit


List Effective Spend Limits

Increase Requests


List Spend Limit Increase Requests


Get Spend Limit Increase Request


Approve Spend Limit Increase Request


Deny Spend Limit Increase Request

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

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)
4.  [Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)
5.  [Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests)

# List Spend Limit Increase Requests

GET/v1/organizations/spend_limit_increase_requests

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester. Requests whose requester is no longer a member are excluded.

##### Query parameters

actor_ids: optional array of string



Filter by requester, as `user_...` tagged IDs.



limit: optional number



default20

minimum1

maximum1000

page: optional string



Opaque cursor from a previous response's `next_page`.



status: optional array of "approved" or "denied" or "pending"



Filter by status. Omit to return all.

One of the following:

"approved"



"denied"



"pending"



##### Returns



data: array of [BetaSpendLimitIncreaseRequest](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests#beta_spend_limit_increase_request) { type: "spend_limit_increase_request", id, actor, 6 more }





type: "spend_limit_increase_request"



defaultspend_limit_increase_request

id: string





actor: object{ type: "user_actor", deleted, email_address, 2 more }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.



type: "user_actor"



Actor type. Always `user_actor`.

defaultuser_actor



deleted: boolean



True only when the underlying account has been deleted.

defaultfalse

email_address: string or null



The user's email address. Null when the account is unavailable or has been deleted.

name: string or null



The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

user_id: string



Tagged ID of the user.



created_at: string



formatdate-time



period: "daily" or "monthly" or "weekly"



One of the following:

"daily"



"monthly"



"weekly"





resolved_at: string or null



formatdate-time



resolved_by: UserActor or ScopedAPIKeyActor or null



One of the following:



UserActor object{ type: "user_actor", deleted, email_address, 2 more }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.



type: "user_actor"



Actor type. Always `user_actor`.

defaultuser_actor



deleted: boolean



True only when the underlying account has been deleted.

defaultfalse

email_address: string or null



The user's email address. Null when the account is unavailable or has been deleted.

name: string or null



The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

user_id: string



Tagged ID of the user.



ScopedAPIKeyActor object{ type: "scoped_api_key_actor", scoped_api_key_id }



A scoped Admin API key acting on behalf of the organization.



type: "scoped_api_key_actor"



defaultscoped_api_key_actor

scoped_api_key_id: string





spend_summary: [BetaSpendSummary](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_summary) { actor, amount, currency, 5 more } or null



Per-member effective-limit report row (`GET /spend_limits/effective`).



status: "approved" or "denied" or "pending"



One of the following:

"approved"



"denied"



"pending"



next_page: string or null



List Spend Limit Increase Requests

cURL



```python
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "monthly",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "period_to_date_spend": "12050.5",
        "scope": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "source": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "approved",
      "type": "spend_limit_increase_request"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "monthly",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "period_to_date_spend": "12050.5",
        "scope": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "source": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "approved",
      "type": "spend_limit_increase_request"
