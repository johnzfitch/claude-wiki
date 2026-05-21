---
title: "Api Admin Organizations Me 85Ca0A0Bba"
source_url: "https://platform.claude.com/docs/en/api/admin/organizations/me.md"
category: "Admin"
fetched_at: "2026-04-26T00:00:00Z"
tags: ["api"]
---

## Me

**get** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

### Returns

- `Organization = object { id, name, type }`

  - `id: string`

    ID of the Organization.

  - `name: string`

    Name of the Organization.

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    - `"organization"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/me \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```
