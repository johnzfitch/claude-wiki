---
title: "Upload File - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/files/upload"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:26:53Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-files-upload.md).

1.  [API reference](http.md)
2.  [Files](https://platform.claude.com/docs/en/api/http/files)

# Upload File

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/files

Upload File

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

##### Body (form-data)



file: file



The file to upload. Only the final path component of the part's `filename` is kept; an absent or empty `filename` is replaced with `unnamed` plus the extension for the file's stored `mime_type`, when known.

formatbinary



expires_in_seconds: optional number



Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

minimum3600

maximum7776000

##### Returns



FileMetadata object{ type: "file", id, created_at, 5 more }





type: "file"



Object type.

For files, this is always `"file"`.



id: string



Unique object identifier.

The format and length of IDs may change over time.



created_at: string



RFC 3339 datetime string representing when the file was created.

formatdate-time



filename: string



Original filename of the uploaded file.

minLength1

maxLength500



mime_type: string



MIME type of the file.

minLength1

maxLength255



size_bytes: number



Size of the file in bytes.

minimum0



downloadable: optional boolean



Whether the file can be downloaded.

defaultfalse



expires_at: optional string or null



RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

formatdate-time

Upload File

cURL



```python
curl https://api.anthropic.com/v1/files \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -F 'file=@/path/to/file'
```

Response 200



```python
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z"
