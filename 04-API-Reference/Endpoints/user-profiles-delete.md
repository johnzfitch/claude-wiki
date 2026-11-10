---
title: "Delete User Profile - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/user_profiles/delete"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:26:55Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/user_profiles/delete).

1.  [API reference](http.md)
2.  [User Profiles](https://platform.claude.com/docs/en/api/http/user_profiles)

# Delete User Profile

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/user_profiles/{user_profile_id}

Delete User Profile

##### Path parameters

user_profile_id: string



The ID of the user profile to delete (`uprof_...`).

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



DeletedUserProfile object{ type: "user_profile_deleted", id }



type: "user_profile_deleted"



Object type. Always `user_profile_deleted`.

id: string



Identifier of the deleted user profile, prefixed `uprof_`.

Delete User Profile

cURL



```python
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "type": "user_profile_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "type": "user_profile_deleted"
