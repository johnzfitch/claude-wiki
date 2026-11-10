---
title: "Set Workspace Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/rate_limits/update"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-06T06:33:36Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)
5.  [Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits)

# Set Workspace Rate Limits

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}

Set or clear rate-limit overrides for one rate-limit group in a workspace.

Only the limiter types named in `limits` change: an integer `value` sets that type's override and `null` clears it. Types not named keep their current value. A value above the organization's own limit is stored, but the organization limit still applies, so the lower of the two is enforced.

Returns the targeted group's entry with this request applied, in the shape `GET /v1/organizations/workspaces/{workspace_id}/rate_limits` returns. Changes take effect within about an hour.

##### Path parameters

workspace_id: string



The ID of the workspace.

rate_limit_id: string



The `id` of the organization's rate-limit entry to set overrides for.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Body



limits: array of [BetaWorkspaceRateLimitUpdateValue](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits#beta_workspace_rate_limit_update_value) { type, value }



Limits to set or clear. Unspecified limit types are unchanged.

minItems1

maxItems16



type: [BetaWorkspaceRateLimitType](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits#beta_workspace_rate_limit_type)



Rate limiter type.

One of the following:

"fast_itpmca"



"fast_otpm"



"input_tokens_per_minute"



"input_tokens_per_minute_cache_aware"



"output_tokens_per_minute"



"requests_per_minute"



"tokens_per_day"



"tokens_per_minute"



"tool_uses_per_second"





value: number or null



New limit value. Set to null to clear the workspace override and fall back to the organization limit.

minimum0

maximum9007199254740991

##### Returns



BetaWorkspaceRateLimit object{ type: "workspace_rate_limit", group, limits, 3 more }



Set Workspace Rate Limits

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits/$RATE_LIMIT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "limits": [
            {
              "type": "fast_itpmca",
              "value": 0
            }
          ]
        }'
```

Response 200



```python
{
  "group": {
    "id": "id",
    "display_name": "display_name",
    "type": "model_group"
  },
  "limits": [
    {
      "org_limit": 0,
      "source": {
        "type": "workspace"
      },
      "type": "type",
      "value": 0
    }
  ],
  "models": [
    "string"
  ],
  "rate_limit_id": "rate_limit_id",
  "type": "workspace_rate_limit",
  "workspace_id": "workspace_id"
}
```

##### Returns Examples

Response 200



```python
{
  "group": {
    "id": "id",
    "display_name": "display_name",
    "type": "model_group"
  },
  "limits": [
    {
      "org_limit": 0,
      "source": {
        "type": "workspace"
      },
      "type": "type",
      "value": 0
    }
  ],
  "models": [
    "string"
  ],
  "rate_limit_id": "rate_limit_id",
  "type": "workspace_rate_limit",
  "workspace_id": "workspace_id"
