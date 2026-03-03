---
category: "04-API-Reference"
fetched_at: "2026-03-03T14:57:47Z"
source_url: "https://platform.claude.com/docs/en/api/beta/files"
title: "Files - Claude API Reference"
---

# Files

##### [Upload File](/docs/en/api/beta/files/upload)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

DeletedFile = object { id, type }

id: string

ID of the deleted file.

type: optional "file_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

FileMetadata = object { id, created_at, filename, 4 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

created_at: string

RFC 3339 datetime string representing when the file was created.

filename: string

Original filename of the uploaded file.

mime_type: string

MIME type of the file.

size_bytes: number

Size of the file in bytes.

type: "file"

Object type.

For files, this is always `"file"`.

downloadable: optional boolean

Whether the file can be downloaded.
