---
title: "Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/workspaces/rate_limits"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-06T06:26:53Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)

# Rate Limits

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

##### [Set Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/update)

POST/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}

Set or clear rate-limit overrides for one rate-limit group in a workspace.

##### Models



BetaWorkspaceRateLimit object{ type: "workspace_rate_limit", group, limits, 3 more }





BetaWorkspaceRateLimitOrganizationSource object{ type: "organization" }





type: "organization"



Always `organization`: no workspace-level override is stored, so the organization's value applies.

defaultorganization



BetaWorkspaceRateLimitType = "fast_itpmca" or "fast_otpm" or "input_tokens_per_minute" or 6 more

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

BetaWorkspaceRateLimitUpdateValue object{ type, value }



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



BetaWorkspaceRateLimitValue object{ type, org_limit, source, value }





BetaWorkspaceRateLimitWorkspaceSource object{ type: "workspace" }





type: "workspace"



Always `workspace`: a workspace-level override is stored.
