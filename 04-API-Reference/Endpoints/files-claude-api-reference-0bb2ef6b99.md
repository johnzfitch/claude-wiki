---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:58:27Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/files"
title: "Files - Claude API Reference"
---
# Files

##### [Upload File](/docs/en/api/beta/files/upload)

client.Beta.Files.Upload(ctx, params) (\*[FileMetadata](/docs/en/api/beta#file_metadata), error)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

client.Beta.Files.List(ctx, params) (\*Page\[[FileMetadata](/docs/en/api/beta#file_metadata)\], error)

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

client.Beta.Files.Download(ctx, fileID, query) (\*Response, error)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

client.Beta.Files.GetMetadata(ctx, fileID, query) (\*[FileMetadata](/docs/en/api/beta#file_metadata), error)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

client.Beta.Files.Delete(ctx, fileID, body) (\*[DeletedFile](/docs/en/api/beta#deleted_file), error)

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

type DeletedFile struct{…}

ID string

ID of the deleted file.

Type DeletedFileType

optional

Deleted object type.

For file deletion, this is always `"file_deleted"`.

type FileMetadata struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

CreatedAt Time

RFC 3339 datetime string representing when the file was created.

Filename string

Original filename of the uploaded file.

MimeType string

MIME type of the file.

SizeBytes int64

Size of the file in bytes.

Type File

Object type.

For files, this is always `"file"`.

Downloadable bool

optional

Whether the file can be downloaded.
