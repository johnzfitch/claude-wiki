---
title: "Citations - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/citations"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:19Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcitations)

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

[Messages](../../01-Getting-Started/intro.md)Model capabilities

# Citations

Copy page



Ground Claude's responses in your source documents. Citations return the exact passages that support each claim, so you can verify answers and surface sources to your users.

Copy page



Citations

[ZDR](../Other/manage-claude-api-and-data-retention.md)

Eligible

excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Claude can provide detailed citations when answering questions about documents, helping you track and verify the sources behind each response.

All [active models](../../20-Models/about-claude-models-overview.md) support citations.



Share your feedback and suggestions about the citations feature using the [citations feedback form](https://forms.gle/9n9hSrKnKe3rpowH9).

The following example shows how to enable citations on a plain text document with the Messages API:

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

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "text",
                        "media_type": "text/plain",
                        "data": "The grass is green. The sky is blue.",
                    },
                    "title": "My Document",
                    "context": "This is a trustworthy document.",
                    "citations": {"enabled": True},
                },
                {"type": "text", "text": "What color is the grass and sky?"},
            ],
        }
    ],
)
print(response)
```



**Comparison with prompt-based approaches**

Compared to prompting Claude to cite sources, the citations feature offers the following advantages:

- **Cost savings:** If your prompt-based approach asks Claude to output direct quotes, you may see cost savings because `cited_text` does not count toward your output tokens.
- **Better citation reliability:** Because the API parses citations into the response formats described in the following sections and extracts `cited_text` directly, citations are guaranteed to contain valid pointers to the provided documents.
- **Improved citation quality:** In Anthropic's evaluations, the citations feature is significantly more likely to cite the most relevant quotes from documents than purely prompt-based approaches.

------------------------------------------------------------------------

## How citations work

Integrate citations with Claude in these steps:

1.  1

    ### Provide document(s) and enable citations

    - Include documents in any of the supported formats: [PDFs](#pdf-documents), [plain text](#plain-text-documents), or [custom content](#custom-content-documents) documents.
    - Set `citations.enabled=true` on each of your documents. Currently, citations must be enabled on all or none of the documents within a request.
    - Only text citations are currently supported. Image citations are not yet possible.

2.  2

    ### Documents get processed

    - Document contents are "chunked" to define the minimum granularity of possible citations. For example, sentence chunking lets Claude cite a single sentence or chain together multiple consecutive sentences to cite a paragraph or longer passage.
      - **For PDFs:** Text is extracted as described in [PDF support](build-with-claude-pdf-support.md) and content is chunked into sentences. Citing images from PDFs is not currently supported.
      - **For plain text documents:** Content is chunked into sentences that can be cited from.
      - **For custom content documents:** Your provided content blocks are used as-is and no further chunking is done.

3.  3

    ### Claude provides cited response

    - Responses may now include multiple text blocks where each text block can contain a claim that Claude is making and a list of citations that support the claim.
    - Citations reference specific locations in source documents. The format of these citations is dependent on the type of document being cited from.
      - **For PDFs:** Citations include the page number range (1-indexed).
      - **For plain text documents:** Citations include the character index range (0-indexed).
      - **For custom content documents:** Citations include the content block index range (0-indexed) corresponding to the original content list provided.
    - Document indices are provided to indicate the reference source and are 0-indexed according to the list of all documents in your original request.



**Automatic chunking vs custom content**

By default, plain text and PDF documents are automatically chunked into sentences. If you need more control over citation granularity (for example, for bullet points or transcripts), use custom content documents instead. See [Document types](#document-types) for more details.

For example, if you want Claude to be able to cite specific sentences from your RAG chunks, you should put each RAG chunk into a plain text document. Otherwise, if you do not want any further chunking to be done, or if you want to customize any additional chunking, you can put RAG chunks into custom content document(s).

### Citable versus non-citable content

- Text found within a document's `source` content can be cited from.
- `title` and `context` are optional fields that are passed to the model but not used toward cited content.
- `title` is limited in length, so the `context` field is useful for storing document metadata as text or stringified JSON.

### Citation indices

- Document indices are 0-indexed from the list of all document content blocks in the request (spanning across all messages).
- Character indices are 0-indexed with exclusive end indices.
- Page numbers are 1-indexed with exclusive end page numbers.
- Content block indices are 0-indexed with exclusive end indices from the `content` list provided in the custom content document.

### Token costs

- Enabling citations incurs a slight increase in input tokens because of system prompt additions and document chunking.
- However, the citations feature is very efficient with output tokens. Internally, the model outputs citations in a standardized format that are then parsed into cited text and document location indices. The `cited_text` field is provided for convenience and does not count toward output tokens.
- When passed back in subsequent conversation turns, `cited_text` is also not counted toward input tokens.

### Feature compatibility

Citations work in conjunction with other API features including [prompt caching](build-with-claude-prompt-caching.md), [token counting](build-with-claude-token-counting.md), and [batch processing](build-with-claude-batch-processing.md).



**Citations and structured outputs are incompatible**

Citations cannot be used together with [structured outputs](build-with-claude-structured-outputs.md). If you enable citations on any user-provided document (`document` blocks or `search_result` blocks) and also include the `output_config.format` parameter (or the deprecated `output_format` parameter), the API returns a 400 error.

This is because citations require interleaving citation blocks with text output, which is incompatible with the strict JSON schema constraints of structured outputs.

#### Using prompt caching with citations

Citations and prompt caching can be used together effectively.

The citation blocks generated in responses cannot be cached directly, but the source documents they reference can be cached. To optimize performance, apply `cache_control` to your top-level document content blocks.

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

# Long document content (for example, technical documentation)
long_document = (
    "This is a very long document with thousands of words..." + " ... " * 1000
)  # Minimum cacheable length

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "text",
                        "media_type": "text/plain",
                        "data": long_document,
                    },
                    "citations": {"enabled": True},
                    "cache_control": {
                        "type": "ephemeral"
                    },  # Cache the document content
                },
                {
                    "type": "text",
                    "text": "What does this document say about API features?",
                },
            ],
        }
    ],
)
print(response)
```

In this example:

- The document content is cached using `cache_control` on the document block.
- Citations are enabled on the document.
- Claude can generate responses with citations while benefiting from cached document content.
- Subsequent requests using the same document benefit from the cached content.

## Document types

### Choosing a document type

Three document types are supported for citations. Documents can be provided directly in the message (base64, text, or URL) or uploaded through the [Files API](build-with-claude-files.md) and referenced by `file_id`:

| Type           | Best for                                                        | Chunking               | Citation format               |
|:---------------|:----------------------------------------------------------------|:-----------------------|:------------------------------|
| Plain text     | Simple text documents, prose                                    | Sentence               | Character indices (0-indexed) |
| PDF            | PDF files with text content                                     | Sentence               | Page numbers (1-indexed)      |
| Custom content | Lists, transcripts, special formatting, more granular citations | No additional chunking | Block indices (0-indexed)     |



For file types that the `document` block doesn't support (for example, .docx and .xlsx), convert the files to plain text and include the content directly in message content. Files that are already plain text, such as .csv and .md files, can also be uploaded with an explicit `text/plain` content type. See [Working with other file formats](build-with-claude-files.md#working-with-other-file-formats).

### Plain text documents

Plain text documents are automatically chunked into sentences. You can provide them inline or by reference with their `file_id`:

Inline text

Files API

The intro example at the top of this page shows a complete plain text request in every SDK. The document block uses a `text` source:

```python
{
  "type": "document",
  "source": {
    "type": "text",
    "media_type": "text/plain",
    "data": "Plain text content..."
  },
  "title": "Document Title",
  "context": "Context about the document that will not be cited from",
  "citations": { "enabled": true }
}
```



### Example plain text citation

```python
{
  "type": "char_location",
  "cited_text": "The exact text being cited", // not counted toward output tokens
  "document_index": 0,
  "document_title": "Document Title",
  "start_char_index": 0, // 0-indexed
  "end_char_index": 50 // exclusive
}
```



### PDF documents

PDF documents can be provided as base64-encoded data, a URL, or by `file_id`. PDF text is extracted and chunked into sentences. As image citations are not yet supported, PDFs that are scans of documents and do not contain extractable text are not citable.

Base64

URL

Files API

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

pdf_base64 = base64.standard_b64encode(
    pathlib.Path("/path/to/document.pdf").read_bytes()
).decode()

response = client.messages.create(
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
                        "data": pdf_base64,
                    },
                    "title": "Document Title",
                    "context": "Context about the document that will not be cited from",
                    "citations": {"enabled": True},
                },
                {"type": "text", "text": "Summarize this document."},
            ],
        }
    ],
)
print(response)
```

### Example PDF citation

```python
{
  "type": "page_location",
  "cited_text": "The exact text being cited", // not counted toward output tokens
  "document_index": 0,
  "document_title": "Document Title",
  "start_page_number": 1, // 1-indexed
  "end_page_number": 2 // exclusive
}
```



### Custom content documents

Custom content documents give you control over citation granularity. No additional chunking is done and chunks are provided to the model according to the content blocks provided.

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

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "content",
                        "content": [
                            {"type": "text", "text": "First chunk"},
                            {"type": "text", "text": "Second chunk"},
                        ],
                    },
                    "title": "Document Title",
                    "context": "Context about the document that will not be cited from",
                    "citations": {"enabled": True},
                },
                {"type": "text", "text": "Summarize this document."},
            ],
        }
    ],
)
print(response)
```

### Example citation

```python
{
  "type": "content_block_location",
  "cited_text": "The exact text being cited", // not counted toward output tokens
  "document_index": 0,
  "document_title": "Document Title",
  "start_block_index": 0, // 0-indexed
  "end_block_index": 1 // exclusive
}
```



------------------------------------------------------------------------

## Response structure

When citations are enabled, responses include multiple text blocks with citations:

```python
{
  "content": [
    { "type": "text", "text": "According to the document, " },
    {
      "type": "text",
      "text": "the grass is green",
      "citations": [
        {
          "type": "char_location",
          "cited_text": "The grass is green.",
          "document_index": 0,
          "document_title": "Example Document",
          "start_char_index": 0,
          "end_char_index": 20
        }
      ]
    },
    { "type": "text", "text": " and " },
    {
      "type": "text",
      "text": "the sky is blue",
      "citations": [
        {
          "type": "char_location",
          "cited_text": "The sky is blue.",
          "document_index": 0,
          "document_title": "Example Document",
          "start_char_index": 20,
          "end_char_index": 36
        }
      ]
    },
    {
      "type": "text",
      "text": ". Information from page 5 states that "
    },
    {
      "type": "text",
      "text": "water is essential",
      "citations": [
        {
          "type": "page_location",
          "cited_text": "Water is essential for life.",
          "document_index": 1,
          "document_title": "PDF Document",
          "start_page_number": 5,
          "end_page_number": 6
        }
      ]
    },
    {
      "type": "text",
      "text": ". The custom document mentions "
    },
    {
      "type": "text",
      "text": "important findings",
      "citations": [
        {
          "type": "content_block_location",
          "cited_text": "These are important findings.",
          "document_index": 2,
          "document_title": "Custom Content Document",
          "start_block_index": 0,
          "end_block_index": 1
        }
      ]
    }
  ]
}
```



### Streaming support

For streaming responses, citations arrive as a `citations_delta` delta type inside `content_block_delta` events. Each delta contains a single citation to add to the `citations` list on the current `text` content block.

### Example streaming events

```python
event: message_start
data: {"type": "message_start", ...}

event: content_block_start
data: {"type": "content_block_start", "index": 0, ...}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0,
       "delta": {"type": "text_delta", "text": "According to..."}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0,
       "delta": {"type": "citations_delta",
                 "citation": {
                     "type": "char_location",
                     "cited_text": "...",
                     "document_index": 0,
                     ...
                 }}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: message_stop
data: {"type": "message_stop"}
```



## Next steps

[Streaming messages](build-with-claude-streaming.md)

Handle the `citations_delta` delta type alongside text deltas to render cited responses as they stream.

[Search results](build-with-claude-search-results.md)

Pass search results from your RAG pipeline as first-class content blocks with built-in citation support.



[PDF support](build-with-claude-pdf-support.md)

Learn how Claude extracts text from PDFs and how page-based citations map back to your source files.

[Files API](build-with-claude-files.md)

Upload documents once and reference them by `file_id` across multiple citation requests.

## Compatibility

Supported platforms  
- Claude API
- Claude Platform on AWS
- Amazon Bedrock
- Google Cloud
- Microsoft Foundry
