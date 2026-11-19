---
title: "List RBAC Group Members - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rbac_groups/members/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:22Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [RBAC Groups](https://platform.claude.com/docs/en/api/http/organization/rbac_groups)
4.  [Members](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members)

# List RBAC Group Members

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/rbac_groups/{rbac_group_id}/members

List members of an RBAC Group.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Path parameters

rbac_group_id: string



ID of the RBAC Group.

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

data: array of [RBACGroupMember](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members#rbac_group_member) { type: "rbac_group_member", created_at, email, 2 more }

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

has_more: boolean



Indicates if there are more results in the requested page direction.

next_page: string or null



Token to provide in as `page` in the subsequent request to retrieve the next page of data.

List RBAC Group Members

cURL



```python
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID/members \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
