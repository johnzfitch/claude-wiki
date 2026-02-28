---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:31:21Z"
source_url: "https://platform.claude.com/docs/en/api/beta/files/list"
title: "List Files - Claude API Reference"
---
# List Files

GET/v1/files

List Files

##### Query ParametersExpand Collapse 

after_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

##### Header ParametersExpand Collapse 

"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 17 more

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

##### ReturnsExpand Collapse 

data: array of [FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more }

List of file metadata objects.

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

first_id: optional string

ID of the first file in this page of results.

has_more: optional boolean

Whether there are more results available.

last_id: optional string

ID of the last file in this page of results.

List Files

cURL

``` shiki
curl https://api.anthropic.com/v1/files?beta=true \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: files-api-2025-04-14' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200

``` shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "x",
      "mime_type": "x",
      "size_bytes": 0,
      "type": "file",
      "downloadable": true
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
