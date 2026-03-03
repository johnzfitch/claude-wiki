---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:00Z"
source_url: "https://platform.claude.com/docs/en/api/admin/organizations/me"
title: "Get Current Organization - Claude API Reference"
---

# Get Current Organization

GET/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

##### ReturnsExpand Collapse 

Organization = object { id, name, type }

id: string

ID of the Organization.

name: string

Name of the Organization.

type: "organization"

Object type.

For Organizations, this is always `"organization"`.

Get Current Organization

``` shiki
curl https://api.anthropic.com/v1/organizations/me \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
