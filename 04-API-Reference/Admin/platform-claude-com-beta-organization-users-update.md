---
title: "Update User - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/users/update"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-06T06:33:33Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Users](https://platform.claude.com/docs/en/api/http/beta/organization/users)

# Update User

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/users/{user_id}

Update a member's organization role.

##### Path parameters

user_id: string



ID of the User.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Body



role: "billing" or "claude_code_user" or "developer" or 2 more



New role for the User.

The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`; changing a User's role to `managed` requires the `write:rbac_groups` scope in addition to `write:members`.

One of the following:

"billing"



"claude_code_user"



"developer"



"managed"



"user"



##### Returns



BetaOrganizationUser object{ type: "user", id, added_at, 3 more }





type: "user"



Object type.

For Users, this is always `"user"`.

defaultuser

id: string



ID of the User.



added_at: string



RFC 3339 datetime string indicating when the User joined the Organization.

formatdate-time

email: string



Email of the User.

name: string



Name of the User.



role: [BetaOrganizationRole](platform-claude-com-http-beta-organization.md#beta_organization_role)



Organization role of the User.

One of the following:

"admin"



"billing"



"claude_code_user"



"developer"



"managed"



"membership_admin"



"owner"



"primary_owner"



"user"



Update User

cURL



```python
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "role": "user"
        }'
```

Response 200



```python
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
