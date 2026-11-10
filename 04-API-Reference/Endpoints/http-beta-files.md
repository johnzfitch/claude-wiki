---
title: "Files - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/files"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:35:47Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# Files

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Upload File](platform-claude-com-http-beta-files-upload.md)

POST/v1/files

##### [List Files](platform-claude-com-http-beta-files-list.md)

GET/v1/files

##### [Download File](platform-claude-com-http-beta-files-download.md)

GET/v1/files/{file_id}/content

##### [Get File Metadata](platform-claude-com-http-beta-files-retrieve-metadata.md)

GET/v1/files/{file_id}

##### [Delete File](platform-claude-com-http-beta-files-delete.md)

DELETE/v1/files/{file_id}

##### Models



BetaDeletedFile object{ type: "file_deleted", id }

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

BetaFileMetadata object{ type: "file", id, created_at, 6 more }





BetaFileScope object{ type: "session", id }



type: "session"



The type of scope (e.g., `"session"`).

id: string



The ID of the scoping resource (e.g., the session ID).
