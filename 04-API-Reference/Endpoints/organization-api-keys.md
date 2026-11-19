---
title: "API Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/api_keys"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:16Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



Looking for your API keys? You can view and create them on the [API keys](../Other/playground.md) page in the Claude Console.



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# API Keys

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List API Keys](https://platform.claude.com/docs/en/api/http/organization/api_keys/list)

GET/v1/organizations/api_keys

##### [Retrieve API Key (Admin API)](https://platform.claude.com/docs/en/api/http/organization/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](../Other/playground.md) in the Claude Console.

##### [Update API Key](https://platform.claude.com/docs/en/api/http/organization/api_keys/update)

POST/v1/organizations/api_keys/{api_key_id}

##### Models



APIKey object{ type: "api_key", id, created_at, 7 more }





APIKeyCreatedBy object{ type, id }





type: "service_account" or "user"



Type of the actor that created the object.

One of the following:

"service_account"



"user"



id: string



ID of the actor that created the object.



APIKeyOrganizationScope object{ type: "organization" }





type: "organization"



Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

defaultorganization



APIKeyServiceAccountActor object{ type: "service_account_actor", service_account_id }





type: "service_account_actor"



Principal type. Always `"service_account_actor"` for a Service Account.

defaultservice_account_actor

service_account_id: string



ID of the Service Account the API key acts as.



APIKeyUserActor object{ type: "user_actor", user_id }





type: "user_actor"



Principal type. Always `"user_actor"` for a User.

defaultuser_actor

user_id: string



ID of the User the API key acts as.



APIKeyWorkspaceScope object{ type: "workspace", workspace_id }





type: "workspace"



Scope type. Always `"workspace"`: the API key belongs to one Workspace.

defaultworkspace

workspace_id: string



ID of the Workspace the API key belongs to, including when it is the organization's default Workspace.



OrgAPIKeyLimitExceededErrorDetails object{ error_code }



The organization has reached its limit of active API keys.

error_code: "org_api_key_limit_exceeded"





WorkspaceAPIKeyLimitExceededErrorDetails object{ error_code }



The workspace has reached its limit of active API keys.

error_code: "workspace_api_key_limit_exceeded"
