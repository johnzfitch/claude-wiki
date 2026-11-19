---
title: "Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rbac_groups/members"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:16Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [RBAC Groups](https://platform.claude.com/docs/en/api/http/organization/rbac_groups)

# Members

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List RBAC Group Members](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{rbac_group_id}/members

List members of an RBAC Group.

##### [Add RBAC Group Member](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members/add)

POST/v1/organizations/rbac_groups/{rbac_group_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Remove RBAC Group Member](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members/remove)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### Models



DeletedRBACGroupMember object{ type: "rbac_group_member_deleted", rbac_group_id, user_id }





type: "rbac_group_member_deleted"



Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

defaultrbac_group_member_deleted

rbac_group_id: string



ID of the RBAC Group.

user_id: string



ID of the User.



RBACGroupMember object{ type: "rbac_group_member", created_at, email, 2 more }





type: "rbac_group_member"



Object type.

For RBAC Group Members, this is always `"rbac_group_member"`.

defaultrbac_group_member



created_at: string



RFC 3339 timestamp of when the User was added to the RBAC Group.

formatdate-time

email: string



Email of the User.

rbac_group_id: string



ID of the RBAC Group.

user_id: string



ID of the User.
