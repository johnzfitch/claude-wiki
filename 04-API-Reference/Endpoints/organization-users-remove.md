---
title: "Remove User - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/users/remove"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:26:46Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/users/remove).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Users](https://platform.claude.com/docs/en/api/http/organization/users)

# Remove User

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/users/{user_id}

Remove a member from the organization.

##### Path parameters

user_id: string



ID of the User.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



type: "user_deleted"



Deleted object type.

For Users, this is always `"user_deleted"`.

defaultuser_deleted

id: string



ID of the User.

Remove User

cURL



```python
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "type": "user_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
