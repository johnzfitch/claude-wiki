---
title: "Rate Limits - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/rate_limits"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:27:10Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)

# Rate Limits

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

##### [Set Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits/update)

POST/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}

Set or clear rate-limit overrides for one rate-limit group in a workspace.

##### Models



WorkspaceRateLimit object{ type: "workspace_rate_limit", group, limits, 3 more }





WorkspaceRateLimitOrganizationSource object{ type: "organization" }





type: "organization"



Always `organization`: no workspace-level override is stored, so the organization's value applies.

defaultorganization



WorkspaceRateLimitType = "fast_itpmca" or "fast_otpm" or "input_tokens_per_minute" or 6 more

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

WorkspaceRateLimitUpdateValue object{ type, value }





type: [WorkspaceRateLimitType](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits#workspace_rate_limit_type)

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

WorkspaceRateLimitValue object{ type, org_limit, source, value }





WorkspaceRateLimitWorkspaceSource object{ type: "workspace" }





type: "workspace"



Always `workspace`: a workspace-level override is stored.
