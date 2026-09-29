---
title: "PDF support - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/pdf-support"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:32Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fpdf-support)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode (research preview)](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Google Cloud](build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Working with files

# PDF support

Copy page



Process PDFs with Claude: extract text, analyze charts, and understand visual content from your documents.

Copy page



PDF support

[ZDR](../Other/manage-claude-api-and-data-retention.md)

Eligible

excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

You can ask Claude about any text, pictures, charts, and tables in PDFs you provide. Some sample use cases:

- Analyzing financial reports and understanding charts/tables
- Extracting key information from legal documents
- Assisting with document translation
- Converting document information into structured formats

## Before you begin

### Check PDF requirements

Claude works with any standard PDF. Ensure your request size meets these requirements:

| Requirement               | Limit                                                                   |
|---------------------------|-------------------------------------------------------------------------|
| Maximum request size      | 32 MB ([varies by platform](../Endpoints/overview.md#request-size-limits)) |
| Maximum pages per request | 600 (100 when the request's context window is under 1M tokens)          |
| Format                    | Standard PDF (no passwords/encryption)                                  |

Both limits are on the entire request payload, including any other content sent alongside PDFs. For large PDFs, consider uploading with the [Files API](build-with-claude-files.md) and referencing by `file_id` to keep request payloads small.



Dense PDFs (many small-font pages, complex tables, or heavy graphics) can fill the context window before reaching the page limit. Requests with large PDFs can also fail before reaching the page limit, even when using the Files API. Try splitting the document into sections; for large files, because each page is processed as an image, downsampling embedded images can also help.

Because PDF support relies on Claude's vision capabilities, it is subject to the same [limitations and considerations](build-with-claude-vision.md#limitations) as other vision tasks.

### Supported platforms and models

All [active models](../../20-Models/about-claude-models-overview.md) support PDF processing. For PDF support through Amazon Bedrock's Converse API, see [Amazon Bedrock PDF support](#amazon-bedrock-pdf-support).

### Amazon Bedrock PDF support

When using PDF support through the Converse API, part of [Claude on Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md), there are two distinct document processing modes:



**Important:** To access Claude's full visual PDF understanding capabilities in the Converse API, you must enable citations. Without citations enabled, the API falls back to basic text extraction only. Learn more about [working with citations](build-with-claude-citations.md).

#### Document processing modes

1.  **Converse Document Chat** (Original mode - Text extraction only)

    - Provides basic text extraction from PDFs
    - Cannot analyze images, charts, or visual layouts within PDFs
    - Uses approximately 1,000 tokens for a 3-page PDF
    - Automatically used when citations are not enabled

2.  **Claude PDF Chat** (New mode - Full visual understanding)

    - Provides complete visual analysis of PDFs
    - Can understand and analyze charts, graphs, images, and visual layouts
    - Processes each page as both text and image for comprehensive understanding
    - Uses approximately 7,000 tokens for a 3-page PDF
    - **Requires citations to be enabled** in the Converse API

#### Key limitations

- **Converse API:** Visual PDF analysis requires citations to be enabled. There is currently no option to use visual analysis without citations (unlike the InvokeModel API).
- **InvokeModel API:** Provides full control over PDF processing without forced citations.

#### Common issues

If Claude isn't seeing images or charts in your PDFs when using the Converse API, you likely need to enable the citations flag. Without it, Converse falls back to basic text extraction only.



This is a known constraint with the Converse API. For applications that require visual PDF analysis without citations, consider using the InvokeModel API instead.



Plain text files such as .txt, .csv, or .md can be used directly in document blocks: upload them to the Files API with MIME type `text/plain` and reference them by `file_id`. Binary formats such as .xlsx or .docx are not supported in document blocks and must be converted to text or PDF first. See [Working with other file formats](build-with-claude-files.md#working-with-other-file-formats).

## Process PDFs with Claude

### Send your first PDF request

Start with a simple example using the Messages API. You can provide PDFs to Claude in three ways:

1.  As a URL reference to a PDF hosted online
2.  As a base64-encoded PDF in `document` content blocks
3.  By a `file_id` from the [Files API](build-with-claude-files.md)



On Amazon Bedrock and Google Cloud, only base64-encoded sources are currently available. On Microsoft Foundry, the Files API is not supported for deployments hosted on Azure.

#### Option 1: URL-based PDF document

The simplest approach is to reference a PDF directly from a URL:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "url",
                        "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf",
                    },
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

The response returns Claude's analysis as text blocks in `content`, with token consumption in `usage`:

Output



```python
{
  "id": "msg_01Hfp8YuFjQ55VgWbpdHDehB",
  "type": "message",
  "role": "assistant",
  "model": "claude-opus-5-5",
  "content": [
    {
      "type": "text",
      "text": "This document is an addendum to the Claude 3 model card, reporting updated evaluation results. The key findings include..."
    }
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 45000,
    "output_tokens": 300
  }
}
```

#### Option 2: Base64-encoded PDF document

If you need to send PDFs from your local system or when a URL isn't available:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import base64
import httpx2

# First, load and encode the PDF
pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
pdf_data = base64.standard_b64encode(
    httpx2.get(pdf_url, follow_redirects=True).content
).decode("utf-8")

# Alternative: Load from a local file
# with open("document.pdf", "rb") as f:
#     pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

# Send to Claude using base64 encoding
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data,
                    },
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

#### Option 3: Files API

For PDFs you'll use repeatedly, or when you want to avoid encoding overhead, use the [Files API](build-with-claude-files.md):

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

# Upload the PDF file
with open("/path/to/document.pdf", "rb") as f:
    file_upload = client.files.upload(file=("document.pdf", f, "application/pdf"))

# Use the uploaded file in a message
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {"type": "file", "file_id": file_upload.id},
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

### How PDF support works

When you send a PDF to Claude, the following steps occur:

1.  1

    ### The system extracts the contents of the document.

    - The system converts each page of the document into an image.
    - The text from each page is extracted and provided alongside each page's image.

2.  2

    ### Claude analyzes both the text and images to better understand the document.

    - Documents are provided as a combination of text and images for analysis.
    - This allows users to ask for insights on visual elements of a PDF, such as charts, diagrams, and other non-textual content.

3.  3

    ### Claude responds, referencing the PDF's contents if relevant.

    Claude can reference both textual and visual content when it responds. You can further improve performance by integrating PDF support with:

    - [Use prompt caching](#use-prompt-caching): To improve performance for repeated analysis.
    - [Process document batches](#process-document-batches): For high-volume document processing.
    - [Tool use](../Agents-Tools/agents-and-tools-tool-use-overview.md): To extract specific information from documents for use as tool inputs.

### Estimate your costs

The token count of a PDF file depends on the total text extracted from the document and the number of pages:

- Text token costs: Each page typically uses 1,500–3,000 tokens per page depending on content density. Standard API pricing applies with no additional PDF fees.
- Image token costs: Because each page is converted into an image, the same [image-based cost calculations](build-with-claude-vision.md#evaluate-image-size) are applied.

You can use [token counting](build-with-claude-token-counting.md) to estimate costs for your specific PDFs.

## Optimize PDF processing

### Improve performance

Follow these best practices for optimal results:

- Place PDFs before text in your requests
- Use standard fonts
- Ensure text is clear and legible
- Rotate pages to proper upright orientation
- Use logical page numbers (from PDF viewer) in prompts
- Split large PDFs into chunks when needed
- Enable prompt caching for repeated analysis

### Scale your implementation

For high-volume processing, consider these approaches:

#### Use prompt caching

Cache PDFs with [prompt caching](build-with-claude-prompt-caching.md) to improve performance on repeated queries:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import base64
import httpx2

# First, load and encode the PDF
pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
pdf_data = base64.standard_b64encode(
    httpx2.get(pdf_url, follow_redirects=True).content
).decode("utf-8")

# Create a message with the cached document
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data,
                    },
                    "cache_control": {"type": "ephemeral"},
                },
                {
                    "type": "text",
                    "text": "Which model has the highest human preference win rates across each use-case?",
                },
            ],
        }
    ],
)

print(message.content)
```

#### Process document batches

Use the [Message Batches API](build-with-claude-batch-processing.md) to process many PDFs in one request:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import base64
import httpx2

# First, load and encode the PDF
pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
pdf_data = base64.standard_b64encode(
    httpx2.get(pdf_url, follow_redirects=True).content
).decode("utf-8")

# Create a batch of requests that use the document
client = anthropic.Anthropic()
message_batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-opus-5-5",
                "max_tokens": 1024,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "document",
                                "source": {
                                    "type": "base64",
                                    "media_type": "application/pdf",
                                    "data": pdf_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": "Which model has the highest human preference win rates across each use-case?",
                            },
                        ],
                    }
                ],
            },
        },
        {
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-opus-5-5",
                "max_tokens": 1024,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "document",
                                "source": {
                                    "type": "base64",
                                    "media_type": "application/pdf",
                                    "data": pdf_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": "Extract 5 key insights from this document.",
                            },
                        ],
                    }
                ],
            },
        },
    ]
)

print(message_batch)
```

Batches process asynchronously. To check progress and retrieve results once processing ends, see [Batch processing](build-with-claude-batch-processing.md).

## Next steps



[Vision](build-with-claude-vision.md)

Claude's vision capabilities allow it to understand and analyze images, opening up exciting possibilities for multimodal interaction.



[Try PDF examples](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision)

Explore practical examples of PDF processing in the Claude Cookbook recipe.



[View API reference](../Endpoints/messages-create.md)

See complete API documentation for PDF support.

## Compatibility

Supported platforms  
- Claude API
- Claude Platform on AWS
- Amazon Bedrock
- Google Cloud
- Microsoft Foundry
