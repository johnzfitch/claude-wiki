---
title: "Delete File - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/files/delete"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:26:52Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-files-delete.md).

1.  [API reference](http.md)
2.  [Files](https://platform.claude.com/docs/en/api/http/files)

# Delete File

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/files/{file_id}

Delete File

##### Path parameters

file_id: string



ID of the File.

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

DeletedFile object{ type: "file_deleted", id }





type: optional "file_deleted"



Deleted object type.

For file deletion, this is always `"file_deleted"`.

defaultfile_deleted

id: string



ID of the deleted file.

Delete File

cURL



```python
curl https://api.anthropic.com/v1/files/$FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
