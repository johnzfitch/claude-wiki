---
title: "RBAC Roles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/rbac_roles"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:03Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# RBAC Roles

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List RBAC Roles](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/list)

GET/v1/organizations/rbac_roles

List RBAC Roles in the organization.

##### [Get RBAC Role](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{rbac_role_id}

Retrieve an RBAC Role by ID.

##### Models



BetaRBACRole object{ type: "rbac_role", id, created_at, 2 more }

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

#### RBAC Roles[Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions)

##### [List RBAC Role Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.
