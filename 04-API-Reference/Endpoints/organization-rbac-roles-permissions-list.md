---
title: "List RBAC Role Permissions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rbac_roles/permissions/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:34:45Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [RBAC Roles](https://platform.claude.com/docs/en/api/http/organization/rbac_roles)
4.  [Permissions](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions)

# List RBAC Role Permissions

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.

The RBAC Roles API is available to Claude Enterprise organizations only.

##### Path parameters

rbac_role_id: string



ID of the RBAC Role.

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

Read more about versioning and our version history [here](versioning.md).

##### Returns



data: array of [RBACRolePermission](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions#rbac_role_permission) { type: "rbac_role_permission", action, resource }





type: "rbac_role_permission"



Object type.

For RBAC Role Permissions, this is always `"rbac_role_permission"`.

defaultrbac_role_permission



action: string



Action the permission grants on the resource.

The vocabulary follows the resource: an `organization` grant carries a product-feature entitlement (for example `chat`), an admin-panel permission entitlement (`permission_*`), or a blanket capability-access mode — `capability_access_all` grants every product-feature entitlement except `inference_hooks_inspection`, which a role holds only through its own row, and `capability_access_all_ga` grants the subset of those for stable features as it stands at permission-check time; neither mode grants model-access entitlements. A consumer enumerating a role's per-feature grants should treat a blanket row as granting every product-feature entitlement it covers, or it will under-report the role's effective access. A `connector_tool` grant carries a tool-access action (`use` or `always_allow`); a `connector_scope` grant carries the scope action `grant` (the role may receive the named OAuth scope when tokens are minted for the connector); `connector` and `all_connectors` grants carry a tool-access action, the scope action, or an authentication-method action (`interactive` or `managed`).



resource: [RBACOrganizationPermissionResource](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions#rbac_organization_permission_resource) or [RBACConnectorToolPermissionResource](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions#rbac_connector_tool_permission_resource) or [RBACConnectorScopePermissionResource](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions#rbac_connector_scope_permission_resource) or 2 more



What the permission applies to.

A tagged union: `type` names the kind of resource and determines which identifier fields are present.

One of the following:



RBACOrganizationPermissionResource object{ type: "organization", organization_id }

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

RBACConnectorToolPermissionResource object{ type: "connector_tool", connector_id, tool_name }

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

RBACConnectorScopePermissionResource object{ type: "connector_scope", connector_id, scope }

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

RBACConnectorPermissionResource object{ type: "connector", connector_id }

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

RBACAllConnectorsPermissionResource object{ type: "all_connectors" }





type: "all_connectors"



Kind of resource the permission applies to.

defaultall_connectors

has_more: boolean



Indicates whether there are more results beyond this page.

next_page: string or null



Opaque cursor for the next page. Pass as the `page` parameter on the next request.

List RBAC Role Permissions

cURL



```python
curl https://api.anthropic.com/v1/organizations/rbac_roles/$RBAC_ROLE_ID/permissions \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
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
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
