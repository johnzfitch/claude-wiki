---
title: "Users - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/users"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:25:25Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Users

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Users](https://platform.claude.com/docs/en/api/http/beta/organization/users/list)

GET/v1/organizations/users

List the organization's members.

##### [Get User](https://platform.claude.com/docs/en/api/http/beta/organization/users/retrieve)

GET/v1/organizations/users/{user_id}

Retrieve a member of the organization by user ID.

##### [Update User](https://platform.claude.com/docs/en/api/http/beta/organization/users/update)

POST/v1/organizations/users/{user_id}

Update a member's organization role.

##### [Remove User](https://platform.claude.com/docs/en/api/http/beta/organization/users/remove)

DELETE/v1/organizations/users/{user_id}

Remove a member from the organization.

##### [Sign Out User](https://platform.claude.com/docs/en/api/http/beta/organization/users/sign_out)

POST/v1/organizations/users/{user_id}/sign_out

Requires `anthropic-beta: ``admin-user-sign-out-2026-10-08`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Sign a member out of Claude everywhere, without removing them from the organization. This ends their sign-in sessions and removes their trusted devices wherever they use Claude, including other organizations and individual plans. It also ends the OAuth tokens issued to them for this organization, so apps such as Claude Code must sign in again.

##### Models



BetaCannotSignOutManagedMemberErrorDetails object{ error_code }



The member has the `managed` role, and this API key or token cannot sign them out. The error message says which keys and tokens can.

error_code: "cannot_sign_out_managed_member"





BetaCannotSignOutMembershipAdminErrorDetails object{ error_code }



The member is a membership admin, and the person the API key or token belongs to is not allowed to sign out membership admins.

error_code: "cannot_sign_out_membership_admin"





BetaCannotSignOutOwnerErrorDetails object{ error_code }



The member is an owner or has owner permissions, and this API key or token cannot sign them out. In a Claude Enterprise organization, an API key with the `write:members` scope can.

error_code: "cannot_sign_out_owner"





BetaCannotSignOutPrimaryOwnerErrorDetails object{ error_code }



The member is the organization's primary owner, whom no API key or token can sign out.

error_code: "cannot_sign_out_primary_owner"





BetaCannotSignOutPrivilegedMemberErrorDetails object{ error_code }



This OAuth token cannot sign out a membership admin or a member whose roles grant owner, user management, or identity and access management.

error_code: "cannot_sign_out_privileged_member"





BetaCannotSignOutSelfErrorDetails object{ error_code }



The member is the user the API key or token belongs to.

error_code: "cannot_sign_out_self"



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
