---
title: "Create RBAC Group - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rbac_groups/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:34:43Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/create).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [RBAC Groups](https://platform.claude.com/docs/en/api/http/organization/rbac_groups)

# Create RBAC Group

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/rbac_groups

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body



name: string



Name of the RBAC Group. Not uniqueness-enforced.

minLength1

maxLength255

##### Returns



RBACGroup object{ type: "rbac_group", id, created_at, 4 more }





type: "rbac_group"



Object type.

For RBAC Groups, this is always `"rbac_group"`.

defaultrbac_group

id: string



ID of the RBAC Group.



created_at: string



RFC 3339 timestamp of when the RBAC Group was created.

formatdate-time

name: string



Name of the RBAC Group. Not uniqueness-enforced.

role_ids: array of string or null



RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.



source_type: "direct" or "scim"



How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

One of the following:

"direct"



"scim"





updated_at: string



RFC 3339 timestamp of when the RBAC Group was last updated.

formatdate-time

Create RBAC Group

cURL



```python
curl https://api.anthropic.com/v1/organizations/rbac_groups \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "name": "Engineering"
        }'
```

Response 200



```python
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
