---
title: "Invites - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/invites"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:25:25Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Invites

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/create)

POST/v1/organizations/invites

Invite a user to join the organization by email.

##### [List Invites](https://platform.claude.com/docs/en/api/http/beta/organization/invites/list)

GET/v1/organizations/invites

List the organization's invites.

##### [Get Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

Retrieve an invite by ID.

##### [Delete Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

Delete a pending invite.

##### Models



BetaOrganizationInvite object{ type: "invite", id, accepted_at, 6 more }





InviteDeleteResponse object{ type: "invite_deleted", id }





type: "invite_deleted"



Deleted object type.

For Invites, this is always `"invite_deleted"`.

defaultinvite_deleted

id: string



ID of the Invite.
