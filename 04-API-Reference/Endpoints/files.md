---
title: "Files - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/files"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-07T06:23:16Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-files.md).

1.  [API reference](http.md)

# Files

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Upload File](https://platform.claude.com/docs/en/api/http/files/upload)

POST/v1/files

##### [List Files](https://platform.claude.com/docs/en/api/http/files/list)

GET/v1/files

##### [Download File](https://platform.claude.com/docs/en/api/http/files/download)

GET/v1/files/{file_id}/content

##### [Get File Metadata](https://platform.claude.com/docs/en/api/http/files/retrieve_metadata)

GET/v1/files/{file_id}

##### [Delete File](https://platform.claude.com/docs/en/api/http/files/delete)

DELETE/v1/files/{file_id}

##### Models

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
