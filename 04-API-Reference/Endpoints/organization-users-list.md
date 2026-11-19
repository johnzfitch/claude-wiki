---
title: "List Users - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/users/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:59Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/users/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Users](https://platform.claude.com/docs/en/api/http/organization/users)

# List Users

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/users

List the organization's members.

##### Query parameters

after_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



email: optional string



Filter by user email.

formatemail



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

minimum1

maximum1000



roles: optional array of string



Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



data: array of [OrganizationUser](https://platform.claude.com/docs/en/api/http/organization/users#organization_user) { type: "user", id, added_at, 3 more }

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

role: [OrganizationRole](https://platform.claude.com/docs/en/api/http/organization#organization_role)

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

first_id: string or null



First ID in the `data` list. Can be used as the `before_id` for the previous page.

has_more: boolean



Indicates if there are more results in the requested page direction.

last_id: string or null



Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Users

cURL



```python
curl https://api.anthropic.com/v1/organizations/users \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "admin",
      "type": "user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
