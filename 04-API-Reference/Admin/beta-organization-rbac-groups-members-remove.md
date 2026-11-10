---
title: "Remove RBAC Group Member - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/remove"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-03T06:23:33Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [RBAC Groups](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups)
5.  [Members](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members)

# Remove RBAC Group Member

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Path parameters

rbac_group_id: string



ID of the RBAC Group.

user_id: string



ID of the User.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns

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

Remove RBAC Group Member

cURL



```python
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
}
```

##### Returns Examples

Response 200



```python
{
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
