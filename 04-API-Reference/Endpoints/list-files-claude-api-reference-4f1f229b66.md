---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:09:00Z"
source_url: "https://platform.claude.com/docs/en/api/java/beta/files/list"
title: "List Files - Claude API Reference"
---

Copy page

Java

# List Files

FileListPage beta().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/files

List Files

##### ParametersExpand Collapse 

FileListParams params

Optional\<String\> afterId

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Optional\<String\> beforeId

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

Optional\<Long\> limit

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

Optional\<List\<AnthropicBeta\>\> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")

PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")

COMPUTER_USE_2024_10_22("computer-use-2024-10-22")

COMPUTER_USE_2025_01_24("computer-use-2025-01-24")

PDFS_2024_09_25("pdfs-2024-09-25")

TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")

TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")

OUTPUT_128K_2025_02_19("output-128k-2025-02-19")

FILES_API_2025_04_14("files-api-2025-04-14")

MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")

MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")

DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")

INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")

CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")

EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")

CONTEXT_1M_2025_08_07("context-1m-2025-08-07")

CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")

MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")

SKILLS_2025_10_02("skills-2025-10-02")

##### ReturnsExpand Collapse 

class FileMetadata:

String id

Unique object identifier.

The format and length of IDs may change over time.

LocalDateTime createdAt

RFC 3339 datetime string representing when the file was created.

formatdate-time

String filename

Original filename of the uploaded file.

maxLength500

minLength1

String mimeType

MIME type of the file.

maxLength255

minLength1

long sizeBytes

Size of the file in bytes.

minimum0

JsonValue; type "file"constant"file"constant

Object type.

For files, this is always `"file"`.

Accepts one of the following:

FILE("file")

Optional\<Boolean\> downloadable

Whether the file can be downloaded.

List Files

Java

``` shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileListPage;
import com.anthropic.models.beta.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        FileListPage page = client.beta().files().list();
    }
}
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

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
