---
title: "Approve Spend Limit Increase Request - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests/approve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:41Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)
5.  [Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests)

# Approve Spend Limit Increase Request

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and transitions the request to `approved`. `period` defaults to the period the member was blocked on. Anthropic emails the requester unless `suppress_notification` is set.

##### Path parameters

spend_limit_increase_request_id: string



ID of the spend limit increase request.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Body

amount: string



New per-user spend limit as a non-negative integer decimal string (minor units).



period: optional [BetaSpendLimitPeriod](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_period) or null



One of the following:

"daily"



"monthly"



"weekly"



suppress_notification: optional boolean



##### Returns



type: "spend_limit_increase_request"



defaultspend_limit_increase_request

id: string





actor: [BetaSpendLimitIncreaseRequestActor](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests#beta_spend_limit_increase_request_actor)



Who submitted the increase request.

One of the following:



created_at: string



formatdate-time



period: [BetaSpendLimitPeriod](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_period)

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

resolved_by: [BetaSpendLimitIncreaseRequestResolvedBy](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests#beta_spend_limit_increase_request_resolved_by) or null



Who approved or denied the increase request.

One of the following:



spend_limit: [BetaSpendLimit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit) { type: "spend_limit", id, amount, 6 more } or null



A configured spend limit: a cap on metered spend for one scope and period.



spend_summary: [BetaSpendSummary](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_summary) { actor, amount, currency, 5 more } or null



Per-member effective-limit report row (`GET /spend_limits/effective`).



status: [BetaSpendLimitIncreaseRequestStatus](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests#beta_spend_limit_increase_request_status)



One of the following:

"approved"



"denied"



"pending"



Approve Spend Limit Increase Request

cURL



```python
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "amount": "50000",
          "period": "monthly"
        }'
```

Response 200



```python
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "is_enabled": true,
    "period": "daily",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
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
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "is_enabled": true,
    "period": "daily",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
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
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
