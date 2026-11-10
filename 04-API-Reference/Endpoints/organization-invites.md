---
title: "Invites - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/invites"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:26:43Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/invites).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Invites

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Invite](https://platform.claude.com/docs/en/api/http/organization/invites/create)

POST/v1/organizations/invites

Invite a user to join the organization by email.

##### [List Invites](https://platform.claude.com/docs/en/api/http/organization/invites/list)

GET/v1/organizations/invites

List the organization's invites.

##### [Get Invite](https://platform.claude.com/docs/en/api/http/organization/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

Retrieve an invite by ID.

##### [Delete Invite](https://platform.claude.com/docs/en/api/http/organization/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

Delete a pending invite.

##### Models



OrganizationInvite object{ type: "invite", id, accepted_at, 6 more }

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
