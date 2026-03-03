---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:06:50Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/files"
title: "Files - Claude API Reference"
---

# Files

##### [Upload File](/docs/en/api/beta/files/upload)

[FileMetadata](/docs/en/api/beta#file_metadata) Beta.Files.Upload(FileUploadParamsparameters, CancellationTokencancellationToken = default)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

[FileListPageResponse](/docs/en/api/beta#FileListPageResponse) Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

[FileMetadata](/docs/en/api/beta#file_metadata) Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

[DeletedFile](/docs/en/api/beta#deleted_file) Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

class DeletedFile:

required string ID

ID of the deleted file.

Type Type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing when the file was created.

required string Filename

Original filename of the uploaded file.

required string MimeType

MIME type of the file.

required Long SizeBytes

Size of the file in bytes.

JsonElement Type "file"constant

Object type.

For files, this is always `"file"`.

Boolean Downloadable

Whether the file can be downloaded.
