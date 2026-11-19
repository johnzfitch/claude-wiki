---
title: "List Effective Spend Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/spend_limits/effective/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:18Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/effective/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Spend Limits](https://platform.claude.com/docs/en/api/http/organization/spend_limits)
4.  [Effective](https://platform.claude.com/docs/en/api/http/organization/spend_limits/effective)

# List Effective Spend Limits

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/spend_limits/effective

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit for, with the `source` scope the spend limit was inherited from. Paginates by member, so a member's periods never split across pages. Supported for Claude Enterprise organizations only, not for Claude Console organizations.

##### Query parameters



limit: optional number



Maximum number of members per page. A member's period rows never split across pages, so a page may carry more rows than this. Defaults to `20`.

default20

minimum1

maximum1000

page: optional string



Opaque cursor from a previous response's `next_page` field.



period: optional array of [SpendLimitPeriod](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_period)

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

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



data: array of [SpendSummary](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_summary) { actor, amount, currency, 5 more }





actor: [SpendLimitUserActor](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_user_actor) or [SpendLimitScopedAPIKeyActor](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_scoped_api_key_actor)



One of the following:



SpendLimitUserActor object{ type: "user_actor", deleted, email_address, 2 more }

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

SpendLimitScopedAPIKeyActor object{ type: "scoped_api_key_actor", scoped_api_key_id }



A scoped Admin API key acting on behalf of the organization.



type: "scoped_api_key_actor"



defaultscoped_api_key_actor

scoped_api_key_id: string



amount: string or null



Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

currency: string



ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.



period: [SpendLimitPeriod](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_period)

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

scope: [SpendLimitUserScope](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_user_scope) or [SpendLimitSeatTierScope](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_seat_tier_scope) or [SpendLimitRBACGroupScope](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_rbac_group_scope) or 4 more



One of the following:



SpendLimitUserScope object{ type: "user", user_id }

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

SpendLimitSeatTierScope object{ type: "seat_tier", seat_tier }





type: "seat_tier"



defaultseat_tier

seat_tier: string





SpendLimitRBACGroupScope object{ type: "rbac_group", rbac_group_id }





type: "rbac_group"



defaultrbac_group

rbac_group_id: string





SpendLimitOrganizationServiceScope object{ type: "organization_service", service }





type: "organization_service"



defaultorganization_service

service: string





SpendLimitOrganizationScope object{ type: "organization" }





type: "organization"



defaultorganization



SpendLimitWorkspaceScope object{ type: "workspace", workspace_id }



Scope selecting one workspace of a Claude Console organization.



type: "workspace"



Scope type. Always `workspace` for this scope.

defaultworkspace

workspace_id: string



Tagged ID of the workspace the spend limit applies to.



SpendLimitUsageTierScope object{ type: "usage_tier" }



Scope of the monthly spend cap Anthropic sets for a Claude Console organization from its usage tier, or a higher cap Anthropic granted the organization. Read-only; its `created_at` and `updated_at` are the organization's creation time, so `amount` can change while `updated_at` stays the same.



type: "usage_tier"



Scope type. Always `usage_tier` for this scope.

defaultusage_tier



source: [SpendLimitUserScope](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_user_scope) or [SpendLimitSeatTierScope](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_seat_tier_scope) or [SpendLimitRBACGroupScope](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_rbac_group_scope) or 4 more



One of the following:



SpendLimitUserScope object{ type: "user", user_id }

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

SpendLimitSeatTierScope object{ type: "seat_tier", seat_tier }





type: "seat_tier"



defaultseat_tier

seat_tier: string





SpendLimitRBACGroupScope object{ type: "rbac_group", rbac_group_id }





type: "rbac_group"



defaultrbac_group

rbac_group_id: string





SpendLimitOrganizationServiceScope object{ type: "organization_service", service }





type: "organization_service"



defaultorganization_service

service: string





SpendLimitOrganizationScope object{ type: "organization" }





type: "organization"



defaultorganization



SpendLimitWorkspaceScope object{ type: "workspace", workspace_id }



Scope selecting one workspace of a Claude Console organization.



type: "workspace"



Scope type. Always `workspace` for this scope.

defaultworkspace

workspace_id: string



Tagged ID of the workspace the spend limit applies to.



SpendLimitUsageTierScope object{ type: "usage_tier" }



Scope of the monthly spend cap Anthropic sets for a Claude Console organization from its usage tier, or a higher cap Anthropic granted the organization. Read-only; its `created_at` and `updated_at` are the organization's creation time, so `amount` can change while `updated_at` stays the same.



type: "usage_tier"



Scope type. Always `usage_tier` for this scope.

defaultusage_tier

spend_limit_id: string



next_page: string or null



List Effective Spend Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "amount": "50000",
      "currency": "USD",
      "period": "daily",
      "period_to_date_spend": "12050.5",
      "scope": {
        "type": "user",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "source": {
        "type": "user",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
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
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "amount": "50000",
      "currency": "USD",
      "period": "daily",
      "period_to_date_spend": "12050.5",
      "scope": {
        "type": "user",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "source": {
        "type": "user",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "spend_limit_id": "spend_limit_id"
