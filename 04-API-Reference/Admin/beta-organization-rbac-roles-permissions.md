---
title: "Permissions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/permissions"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:21Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [RBAC Roles](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles)

# Permissions

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List RBAC Role Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.

##### Models



BetaRBACAllConnectorsPermissionResource object{ type: "all_connectors" }





type: "all_connectors"



Kind of resource the permission applies to.

defaultall_connectors



BetaRBACConnectorPermissionResource object{ type: "connector", connector_id }





type: "connector"



Kind of resource the permission applies to.

defaultconnector

connector_id: string



ID of the connector the permission applies to.



BetaRBACConnectorScopePermissionResource object{ type: "connector_scope", connector_id, scope }





type: "connector_scope"



Kind of resource the permission applies to.

defaultconnector_scope

connector_id: string



ID of the connector the permission applies to.



scope: string



OAuth scope the permission names — the role may receive this scope when tokens are minted for the connector.

Subject to the same encoding rule as `tool_name`: a scope containing characters outside `[a-zA-Z0-9_-]` (or colliding with a reserved form) appears server-encoded in a stable `{prefix}_{32-hex}` form. OAuth scopes routinely contain `:` and `/`, so most appear encoded.



BetaRBACConnectorToolPermissionResource object{ type: "connector_tool", connector_id, tool_name }





type: "connector_tool"



Kind of resource the permission applies to.

defaultconnector_tool

connector_id: string



ID of the connector the permission applies to.



tool_name: string



Published name of the connector tool the permission applies to.

When the published name contains characters outside `[a-zA-Z0-9_-]` (or collides with a reserved form), it is server-encoded into a stable `{prefix}_{32-hex}` form — a shortened readable prefix of the name plus a hash — from which the published name is not recoverable.



BetaRBACOrganizationPermissionResource object{ type: "organization", organization_id }





type: "organization"



Kind of resource the permission applies to.

defaultorganization

organization_id: string



UUID of the organization the permission applies to.



BetaRBACRolePermission object{ type: "rbac_role_permission", action, resource }
