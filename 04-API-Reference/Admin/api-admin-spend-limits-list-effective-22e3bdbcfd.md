---
title: "List Effective Spend Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-10T06:42:48Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fadmin%2Fspend_limits%2Flist_effective)





SearchCtrlK

Include beta APIs

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


Webhooks


Unwrap


Parse Unverified


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits


Set Spend Limit


Get Spend Limit


Delete Spend Limit


List Effective Spend Limits

Increase Requests

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


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Admin](/docs/en/api/http/admin)
3.  [Spend Limits](/docs/en/api/http/admin/spend_limits)

# List Effective Spend Limits

GET/v1/organizations/spend_limits/effective

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit for, with the `source` scope the spend limit was inherited from. Paginates by member, so a member's periods never split across pages.

##### Query parameters



limit: optional number



Maximum number of members per page. A member's period rows never split across pages, so a page may carry more rows than this. Defaults to `20`.

default20

maximum1000

minimum1

page: optional string



Opaque cursor from a previous response's `next_page` field.



period: optional array of "daily" or "monthly" or "weekly"



Restrict the report to these limit periods. Omit to return one row per period each member resolves a spend limit for.

maxItems3

One of the following:

"daily"



"monthly"



"weekly"





user_ids: optional array of string



Restrict the report to these members, by tagged user ID (`user_...`). At most 100 entries.

maxItems100

##### Returns



data: array of [SpendSummary](/docs/en/api/http/admin/spend_limits#spend_summary) { actor, amount, currency, 5 more }





actor: object{ deleted, email_address, name, 2 more }



A user within the organization. `name` and `email_address` are null when the underlying account is unavailable or has been deleted; `deleted` is true only for deleted accounts.

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



type: "user_actor"



Actor type. Always `user_actor`.

defaultuser_actor

user_id: string



Tagged ID of the user.

amount: string or null



Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

currency: string



ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.



period: "daily" or "monthly" or "weekly"



Period this row's effective limit and spend are reported for.

One of the following:

"daily"



"monthly"



"weekly"



period_to_date_spend: string



The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.



scope: object{ type, user_id }



Scope selecting a single member of the organization.



type: "user"



Scope type. Always `user` for this scope.

defaultuser

user_id: string



Tagged ID of the member the spend limit applies to.



source: object{ type, user_id } or object{ seat_tier, type } or object{ rbac_group_id, type } or 2 more



Scope selecting a single member of the organization.

One of the following:



User object{ type, user_id }



Scope selecting a single member of the organization.



type: "user"



Scope type. Always `user` for this scope.

defaultuser

user_id: string



Tagged ID of the member the spend limit applies to.



SeatTier object{ seat_tier, type }



seat_tier: string





type: "seat_tier"



defaultseat_tier



RbacGroup object{ rbac_group_id, type }



rbac_group_id: string





type: "rbac_group"



defaultrbac_group



OrganizationService object{ service, type }



service: string





type: "organization_service"



defaultorganization_service



Organization object{ type }





type: "organization"



defaultorganization

spend_limit_id: string



next_page: string or null



List Effective Spend Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

Response 200



```python
{
  "data": [
    {
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
