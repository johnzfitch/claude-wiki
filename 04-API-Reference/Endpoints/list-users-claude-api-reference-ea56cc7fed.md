---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:04Z"
source_url: "https://platform.claude.com/docs/en/api/admin/users/list"
title: "List Users - Claude API Reference"
---

# List Users

GET/v1/organizations/users

List Users

##### Query ParametersExpand Collapse 

after_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

email: optional string

Filter by user email.

limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

##### ReturnsExpand Collapse 

data: array of [User](/docs/en/api/admin#user) { id, added_at, email, 3 more }

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

first_id: string

First ID in the `data` list. Can be used as the `before_id` for the previous page.

has_more: boolean

Indicates if there are more results in the requested page direction.

last_id: string

Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Users

``` shiki
curl https://api.anthropic.com/v1/organizations/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
