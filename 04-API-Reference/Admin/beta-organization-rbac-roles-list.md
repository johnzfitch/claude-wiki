---
title: "List RBAC Roles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:40Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [RBAC Roles](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles)

# List RBAC Roles

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/rbac_roles

List RBAC Roles in the organization.

The RBAC Roles API is available to Claude Enterprise organizations only.

##### Query parameters



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

minimum1

maximum1000

page: optional string



Optionally set to the `next_page` token from the previous response.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



data: array of [BetaRBACRole](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles#beta_rbac_role) { type: "rbac_role", id, created_at, 2 more }





type: "rbac_role"



Object type.

For RBAC Roles, this is always `"rbac_role"`.

defaultrbac_role

id: string



ID of the RBAC Role.



created_at: string



RFC 3339 datetime string indicating when the RBAC Role was created.

formatdate-time

display_name: string



Name of the RBAC Role. For a role created by Anthropic, this name can differ from the label claude.ai shows, and Anthropic may change the name. To keep a lasting reference to a role, store its `id`.



updated_at: string



RFC 3339 datetime string indicating when the RBAC Role was last updated.

formatdate-time

has_more: boolean



Indicates whether there are more results beyond this page.

next_page: string or null



Opaque cursor for the next page. Pass as the `page` parameter on the next request.

List RBAC Roles

cURL



```python
curl https://api.anthropic.com/v1/organizations/rbac_roles \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Project Editor",
      "type": "rbac_role",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Project Editor",
      "type": "rbac_role",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
