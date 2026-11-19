---
title: "RBAC Roles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rbac_roles"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:22Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# RBAC Roles

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List RBAC Roles](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/list)

GET/v1/organizations/rbac_roles

List RBAC Roles in the organization.

##### [Get RBAC Role](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{rbac_role_id}

Retrieve an RBAC Role by ID.

##### Models



RBACRole object{ type: "rbac_role", id, created_at, 3 more }





RBACRoleSource = [RBACRoleSourceBuiltIn](https://platform.claude.com/docs/en/api/http/organization/rbac_roles#rbac_role_source_built_in) or [RBACRoleSourceCustom](https://platform.claude.com/docs/en/api/http/organization/rbac_roles#rbac_role_source_custom)



One of the following:



RBACRoleSourceBuiltIn object{ type: "built_in" }





type: "built_in"



Anthropic provisions the RBAC Role, and the organization's administrators cannot change or delete it.

defaultbuilt_in



RBACRoleSourceCustom object{ type: "custom" }





type: "custom"



The organization's administrators can change and delete the RBAC Role.

defaultcustom



RBACRoleSourceBuiltIn object{ type: "built_in" }





type: "built_in"



Anthropic provisions the RBAC Role, and the organization's administrators cannot change or delete it.

defaultbuilt_in



RBACRoleSourceCustom object{ type: "custom" }





type: "custom"



The organization's administrators can change and delete the RBAC Role.

defaultcustom

#### RBAC Roles[Permissions](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions)

##### [List RBAC Role Permissions](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.
