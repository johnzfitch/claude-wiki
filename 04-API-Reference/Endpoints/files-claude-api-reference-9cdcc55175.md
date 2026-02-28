---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:36:48Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/files"
title: "Files - Claude API Reference"
---
# Files

##### [Upload File](/docs/en/api/beta/files/upload)

client.beta.files.upload(FileUploadParams { file, betas } params, RequestOptionsoptions?): [FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more }

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

client.beta.files.list(FileListParams { after_id, before_id, limit, betas } params?, RequestOptionsoptions?): Page\<[FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more } \>

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

client.beta.files.download(stringfileID, FileDownloadParams { betas } params?, RequestOptionsoptions?): Response

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

client.beta.files.retrieveMetadata(stringfileID, FileRetrieveMetadataParams { betas } params?, RequestOptionsoptions?): [FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more }

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

client.beta.files.delete(stringfileID, FileDeleteParams { betas } params?, RequestOptionsoptions?): [DeletedFile](/docs/en/api/beta#deleted_file) { id, type }

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

DeletedFile { id, type }

id: string

ID of the deleted file.

type?: "file_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

FileMetadata { id, created_at, filename, 4 more }

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

downloadable?: boolean

Whether the file can be downloaded.
