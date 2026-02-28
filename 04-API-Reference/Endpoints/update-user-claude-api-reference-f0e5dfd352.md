---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:25:43Z"
source_url: "https://platform.claude.com/docs/en/api/admin/users/update"
title: "Update User - Claude API Reference"
---
# Update User

POST/v1/organizations/users/{user_id}

Update User

##### Path ParametersExpand Collapse 

user_id: string

ID of the User.

##### Body ParametersJSONExpand Collapse 

role: "user" or "developer" or "billing" or 2 more

New role for the User. Cannot be "admin".

Accepts one of the following:

"user"

"developer"

"billing"

"claude_code_user"

"managed"

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

Update User

``` shiki
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
