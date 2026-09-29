---
title: "List API Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/api_keys/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-18T06:35:15Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fapi_keys%2Flist)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys


List API Keys


Retrieve API Key (Admin API)


Update API Key

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL



Looking for your API keys? You can view and create them in [Settings → API keys](../Other/usage-limits.md) in the Claude Console.

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)
4.  [API Keys](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys)

# List API Keys

GET/v1/organizations/api_keys

List API Keys

##### Query parameters

after_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

created_by_user_id: optional string



Filter by the ID of the User who created the object.



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

maximum1000

minimum1



status: optional "active" or "archived" or "expired" or "inactive"



Filter by API key status.

One of the following:

"active"



"archived"



"expired"



"inactive"



workspace_id: optional string



Filter by Workspace ID.

##### Returns



data: array of [BetaAPIKey](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys#beta_api_key) { type: "api_key", id, created_at, 8 more }





type: "api_key"



Object type.

For API Keys, this is always `"api_key"`.

defaultapi_key

id: string



ID of the API key.



created_at: string



RFC 3339 datetime string indicating when the API Key was created.

formatdate-time



created_by: [BetaAPIKeyCreatedBy](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys#beta_api_key_created_by) { type, id } or null



The ID and type of the actor that created the API key, or `null` when the creator is not recorded (legacy, workload-identity-federated, or system-created keys).

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

expires_at: string or null



RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

formatdate-time

name: string



Name of the API key.

partial_key_hint: string or null



Partially redacted hint for the API key.



principal: [BetaAPIKeyUserActor](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys#beta_api_key_user_actor) or [BetaAPIKeyServiceAccountActor](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys#beta_api_key_service_account_actor) or null



The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

One of the following:



BetaAPIKeyUserActor object{ type: "user_actor", user_id }

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

BetaAPIKeyServiceAccountActor object{ type: "service_account_actor", service_account_id }

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

scope: [BetaAPIKeyOrganizationScope](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys#beta_api_key_organization_scope) or [BetaAPIKeyWorkspaceScope](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys#beta_api_key_workspace_scope)



Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

One of the following:



BetaAPIKeyOrganizationScope object{ type: "organization" }





type: "organization"



Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

defaultorganization



BetaAPIKeyWorkspaceScope object{ type: "workspace", workspace_id }





type: "workspace"



Scope type. Always `"workspace"`: the API key belongs to one Workspace.

defaultworkspace

workspace_id: string



ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.



status: "active" or "archived" or "expired" or "inactive"



Status of the API key.

One of the following:

"active"



"archived"



"expired"



"inactive"





workspace_id: string or null⁠Deprecated



Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

Use \`scope\` instead. \`workspace_id\` is \`null\` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

first_id: string or null



First ID in the `data` list. Can be used as the `before_id` for the previous page.

has_more: boolean



Indicates if there are more results in the requested page direction.

last_id: string or null



Last ID in the `data` list. Can be used as the `after_id` for the next page.

List API Keys

cURL



```python
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "scope": {
        "type": "workspace",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "scope": {
        "type": "workspace",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
