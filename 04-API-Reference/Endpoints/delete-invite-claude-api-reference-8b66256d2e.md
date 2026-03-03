---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:03Z"
source_url: "https://platform.claude.com/docs/en/api/admin/invites/delete"
title: "Delete Invite - Claude API Reference"
---

# Delete Invite

DELETE/v1/organizations/invites/{invite_id}

Delete Invite

##### Path ParametersExpand Collapse 

invite_id: string

ID of the Invite.

##### ReturnsExpand Collapse 

id: string

ID of the Invite.

type: "invite_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

Delete Invite

``` shiki
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
