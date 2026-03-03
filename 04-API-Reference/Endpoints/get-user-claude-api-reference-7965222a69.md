---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:04Z"
source_url: "https://platform.claude.com/docs/en/api/admin/users/retrieve"
title: "Get User - Claude API Reference"
---

# Get User

GET/v1/organizations/users/{user_id}

Get User

##### Path ParametersExpand Collapse 

user_id: string

ID of the User.

##### ReturnsExpand Collapse 

User = object { id, added_at, email, 3 more }

id: string

ID of the User.

added_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

email: string

Email of the User.

name: string

Name of the User.

role: "user" or "developer" or "billing" or 3 more

Organization role of the User.

Accepts one of the following:

"user"

"developer"

"billing"

"admin"

"claude_code_user"

"managed"

type: "user"

Object type.

For Users, this is always `"user"`.

Get User

``` shiki
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
