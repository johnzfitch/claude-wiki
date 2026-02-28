---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:42:37Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/files"
title: "Files - Claude API Reference"
---
# Files

##### [Upload File](/docs/en/api/beta/files/upload)

beta.files.upload(FileUploadParams\*\*kwargs) -\> [FileMetadata](/docs/en/api/beta#file_metadata)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

beta.files.list(FileListParams\*\*kwargs) -\> SyncPage\[[FileMetadata](/docs/en/api/beta#file_metadata)\]

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

beta.files.download(strfile_id, FileDownloadParams\*\*kwargs) -\> BinaryResponseContent

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

beta.files.retrieve_metadata(strfile_id, FileRetrieveMetadataParams\*\*kwargs) -\> [FileMetadata](/docs/en/api/beta#file_metadata)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

beta.files.delete(strfile_id, FileDeleteParams\*\*kwargs) -\> [DeletedFile](/docs/en/api/beta#deleted_file)

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

class DeletedFile: …

id: str

ID of the deleted file.

type: Optional\[Literal\["file_deleted"\]\]

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

created_at: datetime

RFC 3339 datetime string representing when the file was created.

filename: str

Original filename of the uploaded file.

mime_type: str

MIME type of the file.

size_bytes: int

Size of the file in bytes.

type: Literal\["file"\]

Object type.

For files, this is always `"file"`.

downloadable: Optional\[bool\]

Whether the file can be downloaded.
