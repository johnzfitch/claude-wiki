---
title: "RBAC Roles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/rbac_roles"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:35:48Z"
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

BetaRBACRole object{ type: "rbac_role", id, created_at, 3 more }





BetaRBACRoleSource = [BetaRBACRoleSourceBuiltIn](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles#beta_rbac_role_source_built_in) or [BetaRBACRoleSourceCustom](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles#beta_rbac_role_source_custom)



One of the following:



BetaRBACRoleSourceBuiltIn object{ type: "built_in" }





type: "built_in"



Anthropic provisions the RBAC Role, and the organization's administrators cannot change or delete it.

defaultbuilt_in



BetaRBACRoleSourceCustom object{ type: "custom" }





type: "custom"



The organization's administrators can change and delete the RBAC Role.

defaultcustom



BetaRBACRoleSourceBuiltIn object{ type: "built_in" }





type: "built_in"



Anthropic provisions the RBAC Role, and the organization's administrators cannot change or delete it.

defaultbuilt_in



BetaRBACRoleSourceCustom object{ type: "custom" }





type: "custom"



The organization's administrators can change and delete the RBAC Role.

defaultcustom

#### RBAC Roles[Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions)

##### [List RBAC Role Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.
