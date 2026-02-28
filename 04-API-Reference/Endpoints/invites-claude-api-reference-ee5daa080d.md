---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:24:53Z"
source_url: "https://platform.claude.com/docs/en/api/admin/invites"
title: "Invites - Claude API Reference"
---
# Invites

##### [Create Invite](/docs/en/api/admin/invites/create)

POST/v1/organizations/invites

##### [Get Invite](/docs/en/api/admin/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

##### [List Invites](/docs/en/api/admin/invites/list)

GET/v1/organizations/invites

##### [Delete Invite](/docs/en/api/admin/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

##### ModelsExpand Collapse 

Invite = object { id, email, expires_at, 4 more }

id: string

ID of the Invite.

email: string

Email of the User being invited.

expires_at: string

RFC 3339 datetime string indicating when the Invite expires.

invited_at: string

RFC 3339 datetime string indicating when the Invite was created.

role: "user" or "developer" or "billing" or 3 more

Organization role of the User.

Accepts one of the following:

"user"

"developer"

"billing"

"admin"

"claude_code_user"

"managed"

status: "accepted" or "expired" or "deleted" or "pending"

Status of the Invite.

Accepts one of the following:

"accepted"

"expired"

"deleted"

"pending"

type: "invite"

Object type.

For Invites, this is always `"invite"`.
