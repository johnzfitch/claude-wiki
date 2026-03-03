---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:04:27Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/beta/files"
title: "Files - Claude API Reference"
---

# Files

##### [Upload File](/docs/en/api/beta/files/upload)

beta.files.upload(\*\*kwargs) -\> [FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more }

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

beta.files.list(\*\*kwargs) -\> Page\<[FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more } \>

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

beta.files.download(file_id, \*\*kwargs) -\> StringIO

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

beta.files.retrieve_metadata(file_id, \*\*kwargs) -\> [FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more }

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

beta.files.delete(file_id, \*\*kwargs) -\> [DeletedFile](/docs/en/api/beta#deleted_file) { id, type }

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

class DeletedFile { id, type }

id: String

ID of the deleted file.

type: :file_deleted

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata { id, created_at, filename, 4 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

created_at: Time

RFC 3339 datetime string representing when the file was created.

filename: String

Original filename of the uploaded file.

mime_type: String

MIME type of the file.

size_bytes: Integer

Size of the file in bytes.

type: :file

Object type.

For files, this is always `"file"`.

downloadable: bool

Whether the file can be downloaded.
