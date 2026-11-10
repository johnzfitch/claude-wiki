---
title: "Get Spend Limit - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/spend_limits/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:23Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)

# Get Spend Limit

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/spend_limits/{spend_limit_id}

Retrieve a spend limit by ID.

##### Path parameters

spend_limit_id: string



ID of the Spend Limit.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



BetaSpendLimit object{ type: "spend_limit", id, amount, 6 more }



A configured spend limit: a cap on metered spend for one scope and period.

Get Spend Limit

cURL



```python
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
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
}
```

##### Returns Examples

Response 200



```python
{
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
