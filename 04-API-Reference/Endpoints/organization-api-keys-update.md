---
title: "Update API Key - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/api_keys/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:19Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



Looking for your API keys? You can view and create them on the [API keys](../Other/playground.md) page in the Claude Console.



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [API Keys](https://platform.claude.com/docs/en/api/http/organization/api_keys)

# Update API Key

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/api_keys/{api_key_id}

Update API Key

##### Path parameters

api_key_id: string



ID of the API key.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body



name: optional string or null



Name of the API key.

minLength1

maxLength500



status: optional "active" or "archived" or "inactive" or null



Status of the API key.

One of the following:

"active"



"archived"



"inactive"



##### Returns



APIKey object{ type: "api_key", id, created_at, 7 more }



Update API Key

cURL



```python
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

Response 200



```python
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "scope": {
    "type": "workspace",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  },
  "status": "active",
  "type": "api_key"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "scope": {
    "type": "workspace",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
