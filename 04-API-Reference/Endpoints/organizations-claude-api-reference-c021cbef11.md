---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:24:41Z"
source_url: "https://platform.claude.com/docs/en/api/admin/organizations"
title: "Organizations - Claude API Reference"
---
# Organizations

##### [Get Current Organization](/docs/en/api/admin/organizations/me)

GET/v1/organizations/me

##### ModelsExpand Collapse 

Organization = object { id, name, type }

id: string

ID of the Organization.

name: string

Name of the Organization.

type: "organization"

Object type.

For Organizations, this is always `"organization"`.
