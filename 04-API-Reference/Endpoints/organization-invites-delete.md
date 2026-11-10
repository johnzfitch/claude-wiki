---
title: "Delete Invite - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/invites/delete"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:26:43Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/invites/delete).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Invites](https://platform.claude.com/docs/en/api/http/organization/invites)

# Delete Invite

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/invites/{invite_id}

Delete a pending invite.

##### Path parameters

invite_id: string



ID of the Invite.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



type: "invite_deleted"



Deleted object type.

For Invites, this is always `"invite_deleted"`.

defaultinvite_deleted

id: string



ID of the Invite.

Delete Invite

cURL



```python
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
