---
title: "Increase Requests - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/spend_limits/increase_requests"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:34:46Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Spend Limits](https://platform.claude.com/docs/en/api/http/organization/spend_limits)

# Increase Requests

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

##### Models



SpendLimitIncreaseRequest object{ type: "spend_limit_increase_request", id, actor, 6 more }





SpendLimitIncreaseRequestActor = [SpendLimitUserActor](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_user_actor) or [SpendLimitScopedAPIKeyActor](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_scoped_api_key_actor)



Who submitted the increase request.

One of the following:



SpendLimitIncreaseRequestResolvedBy = [SpendLimitUserActor](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_user_actor) or [SpendLimitScopedAPIKeyActor](https://platform.claude.com/docs/en/api/http/organization/spend_limits#spend_limit_scoped_api_key_actor)



Who approved or denied the increase request.

One of the following:



SpendLimitIncreaseRequestStatus = "approved" or "denied" or "pending"

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
