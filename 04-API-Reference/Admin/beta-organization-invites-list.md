---
title: "List Invites - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/invites/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:24:50Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Invites](https://platform.claude.com/docs/en/api/http/beta/organization/invites)

# List Invites

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/invites

List the organization's invites.

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

Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

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



statuses: optional array of "accepted" or "expired" or "pending"



Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

One of the following:

"accepted"



"expired"



"pending"



##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



data: array of [BetaOrganizationInvite](https://platform.claude.com/docs/en/api/http/beta/organization/invites#beta_organization_invite) { type: "invite", id, accepted_at, 6 more }





type: "invite"



Object type.

For Invites, this is always `"invite"`.

defaultinvite

id: string



ID of the Invite.



accepted_at: string or null



RFC 3339 datetime string indicating when the Invite was accepted, or null.

formatdate-time

email: string



Email of the User being invited.



expires_at: string



RFC 3339 datetime string indicating when the Invite expires.

formatdate-time



invited_at: string



RFC 3339 datetime string indicating when the Invite was created.

formatdate-time

rbac_group_ids: array of string



RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

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



status: "accepted" or "deleted" or "expired" or "pending"



Status of the Invite.

One of the following:

"accepted"



"deleted"



"expired"



"pending"

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

List Invites

cURL



```python
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "accepted_at": "2019-12-27T18:11:19.117Z",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "rbac_group_ids": [
        "string"
      ],
      "role": "admin",
      "status": "pending",
      "type": "invite"
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
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "accepted_at": "2019-12-27T18:11:19.117Z",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
