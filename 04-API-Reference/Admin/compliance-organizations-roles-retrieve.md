---
title: "Get Compliance Role - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:38Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Organizations](https://platform.claude.com/docs/en/api/http/compliance/organizations)
4.  [Roles](https://platform.claude.com/docs/en/api/http/compliance/organizations/roles)

# Get Compliance Role

Copy page



API version 2026-10-21

GET/v1/compliance/organizations/{org_uuid}/roles/{role_id}

Get Compliance Role

##### Path parameters

org_uuid: string



The organization UUID

role_id: string



The role ID (tagged ID, e.g., rbac_role_abc123)

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



##### Returns

id: string



Role identifier (tagged ID)



created_at: string or null



Role creation timestamp (RFC 3339)

formatdate-time

description: string



Role description

name: string



Role name



updated_at: string or null



Role last-updated timestamp (RFC 3339)

formatdate-time

Get Compliance Role

cURL



```python
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789Z"
