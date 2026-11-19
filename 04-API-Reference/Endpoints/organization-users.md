---
title: "Users - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/users"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:25Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/users).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Users

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Users](https://platform.claude.com/docs/en/api/http/organization/users/list)

GET/v1/organizations/users

List the organization's members.

##### [Get User](https://platform.claude.com/docs/en/api/http/organization/users/retrieve)

GET/v1/organizations/users/{user_id}

Retrieve a member of the organization by user ID.

##### [Update User](https://platform.claude.com/docs/en/api/http/organization/users/update)

POST/v1/organizations/users/{user_id}

Update a member's organization role.

##### [Remove User](https://platform.claude.com/docs/en/api/http/organization/users/remove)

DELETE/v1/organizations/users/{user_id}

Remove a member from the organization.

##### Models



CannotRemoveLastMemberErrorDetails object{ error_code }



The user is the organization's only member. Add another member before removing this one.

error_code: "cannot_remove_last_member"





OrganizationUser object{ type: "user", id, added_at, 3 more }

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



UserRemoveResponse object{ type: "user_deleted", id }





type: "user_deleted"



Deleted object type.

For Users, this is always `"user_deleted"`.

defaultuser_deleted

id: string



ID of the User.
