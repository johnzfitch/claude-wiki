---
category: "04-API-Reference"
fetched_at: "2026-03-03T14:59:06Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/files/retrieve_metadata"
title: "Get File Metadata - Claude API Reference"
---

# Get File Metadata

client.beta.files.retrieveMetadata(stringfileID, FileRetrieveMetadataParams { betas } params?, RequestOptionsoptions?): [FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more }

GET/v1/files/{file_id}

Get File Metadata

##### ParametersExpand Collapse 

fileID: string

ID of the File.

params: FileRetrieveMetadataParams { betas }

betas?: Array\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\>

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" \| "prompt-caching-2024-07-31" \| "computer-use-2024-10-22" \| 17 more

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

Get File Metadata

TypeScript

``` shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const fileMetadata = await client.beta.files.retrieveMetadata('file_id');

console.log(fileMetadata.id);
```

Response 200

``` shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "x",
  "mime_type": "x",
  "size_bytes": 0,
  "type": "file",
  "downloadable": true
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
