---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:48:30Z"
source_url: "https://platform.claude.com/docs/en/api/java/beta/files"
title: "Files - Claude API Reference"
---
# Files

##### [Upload File](/docs/en/api/beta/files/upload)

[FileMetadata](/docs/en/api/beta#file_metadata) beta().files().upload(FileUploadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

FileListPage beta().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

HttpResponse beta().files().download(FileDownloadParamsparams = FileDownloadParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

[FileMetadata](/docs/en/api/beta#file_metadata) beta().files().retrieveMetadata(FileRetrieveMetadataParamsparams = FileRetrieveMetadataParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

[DeletedFile](/docs/en/api/beta#deleted_file) beta().files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

class DeletedFile:

String id

ID of the deleted file.

Optional\<Type\> type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata:

String id

Unique object identifier.

The format and length of IDs may change over time.

LocalDateTime createdAt

RFC 3339 datetime string representing when the file was created.

String filename

Original filename of the uploaded file.

String mimeType

MIME type of the file.

long sizeBytes

Size of the file in bytes.

JsonValue; type "file"constant

"file"constant

Object type.

For files, this is always `"file"`.

Optional\<Boolean\> downloadable

Whether the file can be downloaded.
