---
title: "Get Spend Limit Increase Request - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/spend_limits/increase_requests/retrieve"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:34:46Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/retrieve).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Spend Limits](https://platform.claude.com/docs/en/api/http/organization/spend_limits)
4.  [Increase Requests](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests)

# Get Spend Limit Increase Request

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

While `pending`, the response includes a live `spend_summary` for the requester at the request's period.

##### Path parameters

spend_limit_increase_request_id: string



ID of the spend limit increase request.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



SpendLimitIncreaseRequest object{ type: "spend_limit_increase_request", id, actor, 6 more }



Get Spend Limit Increase Request

cURL



```python
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
