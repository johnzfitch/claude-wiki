---
title: "Get RBAC Role - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/rbac_roles/retrieve"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:23Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/retrieve).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [RBAC Roles](https://platform.claude.com/docs/en/api/http/organization/rbac_roles)

# Get RBAC Role

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/rbac_roles/{rbac_role_id}

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

##### Path parameters

rbac_role_id: string



ID of the RBAC Role.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



RBACRole object{ type: "rbac_role", id, created_at, 3 more }



Get RBAC Role

cURL



```python
curl https://api.anthropic.com/v1/organizations/rbac_roles/$RBAC_ROLE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Project Editor",
  "source": {
    "type": "built_in"
  },
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Project Editor",
  "source": {
    "type": "built_in"
  },
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
