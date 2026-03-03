---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:00:24Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/files/download"
title: "Download File - Claude API Reference"
---

# Download File

beta.files.download(strfile_id, FileDownloadParams\*\*kwargs) -\> BinaryResponseContent

GET/v1/files/{file_id}/content

Download File

##### ParametersExpand Collapse 

file_id: str

ID of the File.

betas: Optional\[List\[[AnthropicBetaParam](/docs/en/api/beta#anthropic_beta)\]\]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal\["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 17 more\]

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

BinaryResponseContent

Download File

Python

``` shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.files.download(
    file_id="file_id",
)
print(response)
content = response.read()
