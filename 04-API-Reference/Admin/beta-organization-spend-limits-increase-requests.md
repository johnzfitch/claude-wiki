---
title: "Increase Requests - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:05Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)

# Increase Requests

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Spend Limit Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

List spend limit increase requests, most recent first.

##### [Get Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

##### [Approve Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approve a pending spend limit increase request.

##### [Deny Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

Deny a pending spend limit increase request.

##### Models



BetaSpendLimitIncreaseRequest object{ type: "spend_limit_increase_request", id, actor, 6 more }





BetaSpendLimitIncreaseRequestActor = [BetaSpendLimitUserActor](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_user_actor) or [BetaSpendLimitScopedAPIKeyActor](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_scoped_api_key_actor)



Who submitted the increase request.

One of the following:



BetaSpendLimitIncreaseRequestResolvedBy = [BetaSpendLimitUserActor](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_user_actor) or [BetaSpendLimitScopedAPIKeyActor](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits#beta_spend_limit_scoped_api_key_actor)



Who approved or denied the increase request.

One of the following:



BetaSpendLimitIncreaseRequestStatus = "approved" or "denied" or "pending"



One of the following:

"approved"



"denied"



"pending"





IncreaseRequestApproveResponse object{ type: "spend_limit_increase_request", id, actor, 7 more }
