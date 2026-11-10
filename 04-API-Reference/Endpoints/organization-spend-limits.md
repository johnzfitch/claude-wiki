---
title: "Spend Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/spend_limits"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:18Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Spend Limits

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### Models



SpendLimit object{ type: "spend_limit", id, amount, 6 more }



A configured spend limit: a cap on metered spend for one scope and period.



SpendLimitOrganizationScope object{ type: "organization" }





type: "organization"



defaultorganization

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

SpendLimitPeriod = "daily" or "monthly" or "weekly"



One of the following:

"daily"



"monthly"



"weekly"

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

SpendLimitScopedAPIKeyActor object{ type: "scoped_api_key_actor", scoped_api_key_id }



A scoped Admin API key acting on behalf of the organization.



type: "scoped_api_key_actor"



defaultscoped_api_key_actor

scoped_api_key_id: string



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

SpendLimitUsageTierScope object{ type: "usage_tier" }



Scope of the monthly spend cap Anthropic sets for a Claude Console organization from its usage tier, or a higher cap Anthropic granted the organization. Read-only; its `created_at` and `updated_at` are the organization's creation time, so `amount` can change while `updated_at` stays the same.



type: "usage_tier"



Scope type. Always `usage_tier` for this scope.

defaultusage_tier

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

SpendSummary object{ actor, amount, currency, 5 more }



Per-member effective-limit report row (`GET /spend_limits/effective`).

#### Spend Limits[Effective](https://platform.claude.com/docs/en/api/http/organization/spend_limits/effective)

##### [List Effective Spend Limits](https://platform.claude.com/docs/en/api/http/organization/spend_limits/effective/list)

GET/v1/organizations/spend_limits/effective

List each member's effective spend limit and period-to-date spend.

#### Spend Limits[Increase Requests](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests)

##### [List Spend Limit Increase Requests](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

List spend limit increase requests, most recent first.

##### [Get Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

##### [Approve Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approve a pending spend limit increase request.

##### [Deny Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

Deny a pending spend limit increase request.
