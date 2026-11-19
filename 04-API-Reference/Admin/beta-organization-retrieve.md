---
title: "Get Current Organization - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:25:27Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Get Current Organization

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



BetaOrganization object{ type: "organization", id, name }





type: "organization"



Object type.

For Organizations, this is always `"organization"`.

defaultorganization



id: string



ID of the Organization.

formatuuid

name: string



Name of the Organization.

Get Current Organization

cURL



```python
curl https://api.anthropic.com/v1/organizations/me \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "12345678-1234-5678-1234-567812345678",
