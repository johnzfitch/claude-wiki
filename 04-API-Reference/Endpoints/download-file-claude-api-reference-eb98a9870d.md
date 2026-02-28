---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:37:08Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/files/download"
title: "Download File - Claude API Reference"
---
# Download File

client.beta.files.download(stringfileID, FileDownloadParams { betas } params?, RequestOptionsoptions?): Response

GET/v1/files/{file_id}/content

Download File

##### ParametersExpand Collapse 

fileID: string

ID of the File.

params: FileDownloadParams { betas }

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

unnamed_schema_1 = Response

Download File

TypeScript

``` shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.files.download('file_id');

console.log(response);

const content = await response.blob();
console.log(content);
