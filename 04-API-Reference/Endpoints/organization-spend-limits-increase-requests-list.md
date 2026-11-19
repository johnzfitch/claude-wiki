---
title: "List Spend Limit Increase Requests - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/spend_limits/increase_requests/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:19Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Spend Limits](https://platform.claude.com/docs/en/api/http/organization/spend_limits)
4.  [Increase Requests](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests)

# List Spend Limit Increase Requests

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

status: optional array of [SpendLimitIncreaseRequestStatus](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests#spend_limit_increase_request_status)



Filter by status. Omit to return all.

One of the following:

"approved"



"denied"



"pending"



##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



data: array of [SpendLimitIncreaseRequest](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests#spend_limit_increase_request) { type: "spend_limit_increase_request", id, actor, 6 more }





type: "spend_limit_increase_request"



defaultspend_limit_increase_request

id: string





actor: [SpendLimitIncreaseRequestActor](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests#spend_limit_increase_request_actor)



Who submitted the increase request.

One of the following:



created_at: string



formatdate-time



period: [SpendLimitPeriod](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_period)

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

resolved_by: [SpendLimitIncreaseRequestResolvedBy](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests#spend_limit_increase_request_resolved_by) or null



Who approved or denied the increase request.

One of the following:



spend_summary: [SpendSummary](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_summary) { actor, amount, currency, 5 more } or null



Per-member effective-limit report row (`GET /spend_limits/effective`).



status: [SpendLimitIncreaseRequestStatus](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests#spend_limit_increase_request_status)

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
