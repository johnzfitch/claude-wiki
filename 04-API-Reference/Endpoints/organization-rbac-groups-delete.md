---
title: "Delete RBAC Group - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rbac_groups/delete"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:15Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/delete).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [RBAC Groups](https://platform.claude.com/docs/en/api/http/organization/rbac_groups)

# Delete RBAC Group

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/rbac_groups/{rbac_group_id}

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Path parameters

rbac_group_id: string



ID of the RBAC Group.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



DeletedRBACGroup object{ type: "rbac_group_deleted", id }





type: "rbac_group_deleted"



Deleted object type.

For RBAC Groups, this is always `"rbac_group_deleted"`.

defaultrbac_group_deleted

id: string



ID of the RBAC Group.

Delete RBAC Group

cURL



```python
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
