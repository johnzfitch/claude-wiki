---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:03Z"
source_url: "https://platform.claude.com/docs/en/api/admin/users"
title: "Users - Claude API Reference"
---

# Users

##### [Get User](/docs/en/api/admin/users/retrieve)

GET/v1/organizations/users/{user_id}

##### [List Users](/docs/en/api/admin/users/list)

GET/v1/organizations/users

##### [Update User](/docs/en/api/admin/users/update)

POST/v1/organizations/users/{user_id}

##### [Remove User](/docs/en/api/admin/users/delete)

DELETE/v1/organizations/users/{user_id}

##### ModelsExpand Collapse 

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
