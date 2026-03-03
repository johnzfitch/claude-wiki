---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:05Z"
source_url: "https://platform.claude.com/docs/en/api/admin/users/delete"
title: "Remove User - Claude API Reference"
---

# Remove User

DELETE/v1/organizations/users/{user_id}

Remove User

##### Path ParametersExpand Collapse 

user_id: string

ID of the User.

##### ReturnsExpand Collapse 

id: string

ID of the User.

type: "user_deleted"

Deleted object type.

For Users, this is always `"user_deleted"`.

Remove User

``` shiki
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
