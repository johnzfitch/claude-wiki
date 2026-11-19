---
title: "Get Current Organization - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/retrieve"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:57Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](../Admin/http-beta-organization-retrieve.md).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

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

Read more about versioning and our version history [here](versioning.md).

##### Returns



OrganizationInfo object{ type: "organization", id, name }

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
