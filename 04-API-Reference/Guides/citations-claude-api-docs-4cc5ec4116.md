---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:14Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/citations"
title: "Citations - Claude API Docs"
---

Capabilities

# Citations

Copy page

Copy page

Claude is capable of providing detailed citations when answering questions about documents, helping you track and verify information sources in responses.

All [active models](/docs/en/about-claude/models/overview) support citations, with the exception of Haiku 3.

*Citations with Claude Sonnet 3.7*

Claude Sonnet 3.7 may be less likely to make citations compared to other Claude models without more explicit instructions from the user. When using citations with Claude Sonnet 3.7, we recommend including additional instructions in the `user` turn, like `"Use citations to back up your answer."` for example.

We've also observed that when the model is asked to structure its response, it is unlikely to use citations unless explicitly told to use citations within that format. For example, if the model is asked to use `<result>` tags in its response, you should add something like `"Always use citations in your answer, even within <result> tags."`

Please share your feedback and suggestions about the citations feature using this [form](https://forms.gle/9n9hSrKnKe3rpowH9).

Here's an example of how to use citations with the Messages API:

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "document",
            "source": {
              "type": "text",
              "media_type": "text/plain",
              "data": "The grass is green. The sky is blue."
            },
            "title": "My Document",
            "context": "This is a trustworthy document.",
            "citations": {"enabled": true}
          },
          {
            "type": "text",
            "text": "What color is the grass and sky?"
          }
        ]
      }
    ]
  }'
```

**Comparison with prompt-based approaches**

In comparison with prompt-based citations solutions, the citations feature has the following advantages:

- **Cost savings:** If your prompt-based approach asks Claude to output direct quotes, you may see cost savings due to the fact that `cited_text` does not count towards your output tokens.
- **Better citation reliability:** Because we parse citations into the respective response formats mentioned above and extract `cited_text`, citations are guaranteed to contain valid pointers to the provided documents.
- **Improved citation quality:** In our evals, we found the citations feature to be significantly more likely to cite the most relevant quotes from documents as compared to purely prompt-based approaches.

------------------------------------------------------------------------

## 

How citations work

Integrate citations with Claude in these steps:

1.  1

    Provide document(s) and enable citations

    - Include documents in any of the supported formats: [PDFs](#pdf-documents), [plain text](#plain-text-documents), or [custom content](#custom-content-documents) documents
    - Set `citations.enabled=true` on each of your documents. Currently, citations must be enabled on all or none of the documents within a request.
    - Note that only text citations are currently supported and image citations are not yet possible.

2.  2

    Documents get processed

    - Document contents are "chunked" in order to define the minimum granularity of possible citations. For example, sentence chunking would allow Claude to cite a single sentence or chain together multiple consecutive sentences to cite a paragraph (or longer)!
      - **For PDFs:** Text is extracted as described in [PDF Support](/docs/en/build-with-claude/pdf-support) and content is chunked into sentences. Citing images from PDFs is not currently supported.
      - **For plain text documents:** Content is chunked into sentences that can be cited from.
      - **For custom content documents:** Your provided content blocks are used as-is and no further chunking is done.

3.  3

    Claude provides cited response

    - Responses may now include multiple text blocks where each text block can contain a claim that Claude is making and a list of citations that support the claim.
    - Citations reference specific locations in source documents. The format of these citations are dependent on the type of document being cited from.
      - **For PDFs:** citations will include the page number range (1-indexed).
      - **For plain text documents:** Citations will include the character index range (0-indexed).
      - **For custom content documents:** Citations will include the content block index range (0-indexed) corresponding to the original content list provided.
    - Document indices are provided to indicate the reference source and are 0-indexed according to the list of all documents in your original request.

**Automatic chunking vs custom content**

By default, plain text and PDF documents are automatically chunked into sentences. If you need more control over citation granularity (e.g., for bullet points or transcripts), use custom content documents instead. See [Document Types](#document-types) for more details.

For example, if you want Claude to be able to cite specific sentences from your RAG chunks, you should put each RAG chunk into a plain text document. Otherwise, if you do not want any further chunking to be done, or if you want to customize any additional chunking, you can put RAG chunks into custom content document(s).

### 

Citable vs non-citable content

- Text found within a document's `source` content can be cited from.
- `title` and `context` are optional fields that will be passed to the model but not used towards cited content.
- `title` is limited in length so you may find the `context` field to be useful in storing any document metadata as text or stringified json.

### 

Citation indices

- Document indices are 0-indexed from the list of all document content blocks in the request (spanning across all messages).
- Character indices are 0-indexed with exclusive end indices.
- Page numbers are 1-indexed with exclusive end page numbers.
- Content block indices are 0-indexed with exclusive end indices from the `content` list provided in the custom content document.

### 

Token costs

- Enabling citations incurs a slight increase in input tokens due to system prompt additions and document chunking.
- However, the citations feature is very efficient with output tokens. Under the hood, the model is outputting citations in a standardized format that are then parsed into cited text and document location indices. The `cited_text` field is provided for convenience and does not count towards output tokens.
- When passed back in subsequent conversation turns, `cited_text` is also not counted towards input tokens.

### 

Feature compatibility

Citations works in conjunction with other API features including [prompt caching](/docs/en/build-with-claude/prompt-caching), [token counting](/docs/en/build-with-claude/token-counting) and [batch processing](/docs/en/build-with-claude/batch-processing).

**Citations and Structured Outputs are incompatible**

Citations cannot be used together with [Structured Outputs](/docs/en/build-with-claude/structured-outputs). If you enable citations on any user-provided document (Document blocks or RequestSearchResultBlock) and also include the `output_config.format` parameter (or the deprecated `output_format` parameter), the API will return a 400 error.

This is because citations require interleaving citation blocks with text output, which is incompatible with the strict JSON schema constraints of structured outputs.

#### 

Using Prompt Caching with Citations

Citations and prompt caching can be used together effectively.

The citation blocks generated in responses cannot be cached directly, but the source documents they reference can be cached. To optimize performance, apply `cache_control` to your top-level document content blocks.

Python

``` shiki
import anthropic

client = anthropic.Anthropic()

# Long document content (e.g., technical documentation)
long_document = "This is a very long document with thousands of words..." + " ... " * 1000  # Minimum cacheable length

response = client.messages.create(
    model="claude-opus-4-6",
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
                        "data": long_document
                    },
                    "citations": {"enabled": True},
                    "cache_control": {"type": "ephemeral"}  # Cache the document content
                },
                {
                    "type": "text",
                    "text": "What does this document say about API features?"
                }
            ]
        }
    ]
)
```

In this example:

- The document content is cached using `cache_control` on the document block
- Citations are enabled on the document
- Claude can generate responses with citations while benefiting from cached document content
- Subsequent requests using the same document will benefit from the cached content

## 

Document Types

### 

Choosing a document type

We support three document types for citations. Documents can be provided directly in the message (base64, text, or URL) or uploaded via the [Files API](/docs/en/build-with-claude/files) and referenced by `file_id`:

| Type | Best for | Chunking | Citation format |
|----|----|----|----|
| Plain text | Simple text documents, prose | Sentence | Character indices (0-indexed) |
| PDF | PDF files with text content | Sentence | Page numbers (1-indexed) |
| Custom content | Lists, transcripts, special formatting, more granular citations | No additional chunking | Block indices (0-indexed) |

.csv, .xlsx, .docx, .md, and .txt files are not supported as document blocks. Convert these to plain text and include directly in message content. See [Working with other file formats](/docs/en/build-with-claude/files#working-with-other-file-formats).

### 

Plain text documents

Plain text documents are automatically chunked into sentences. You can provide them inline or by reference with their `file_id`:

Inline text

Inline text

Files API

Files API

``` shiki
{
    "type": "document",
    "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": "Plain text content..."
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}
```

### Example plain text citation

### 

PDF documents

PDF documents can be provided as base64-encoded data or by `file_id`. PDF text is extracted and chunked into sentences. As image citations are not yet supported, PDFs that are scans of documents and do not contain extractable text will not be citable.

Base64

Base64

Files API

Files API

``` shiki
{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": base64_encoded_pdf_data
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}
```

### Example PDF citation

### 

Custom content documents

Custom content documents give you control over citation granularity. No additional chunking is done and chunks are provided to the model according to the content blocks provided.

``` shiki
{
    "type": "document",
    "source": {
        "type": "content",
        "content": [
            {"type": "text", "text": "First chunk"},
            {"type": "text", "text": "Second chunk"}
        ]
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}
```

### Example citation

------------------------------------------------------------------------

## 

Response Structure

When citations are enabled, responses include multiple text blocks with citations:

``` shiki
{
    "content": [
        {
            "type": "text",
            "text": "According to the document, "
        },
        {
            "type": "text",
            "text": "the grass is green",
            "citations": [{
                "type": "char_location",
                "cited_text": "The grass is green.",
                "document_index": 0,
                "document_title": "Example Document",
                "start_char_index": 0,
                "end_char_index": 20
            }]
        },
        {
            "type": "text",
            "text": " and "
        },
        {
            "type": "text",
            "text": "the sky is blue",
            "citations": [{
                "type": "char_location",
                "cited_text": "The sky is blue.",
                "document_index": 0,
                "document_title": "Example Document",
                "start_char_index": 20,
                "end_char_index": 36
            }]
        },
        {
            "type": "text",
            "text": ". Information from page 5 states that ",
        },
        {
            "type": "text",
            "text": "water is essential",
            "citations": [{
                "type": "page_location",
                "cited_text": "Water is essential for life.",
                "document_index": 1,
                "document_title": "PDF Document",
                "start_page_number": 5,
                "end_page_number": 6
            }]
        },
        {
            "type": "text",
            "text": ". The custom document mentions ",
        },
        {
            "type": "text",
            "text": "important findings",
            "citations": [{
                "type": "content_block_location",
                "cited_text": "These are important findings.",
                "document_index": 2,
                "document_title": "Custom Content Document",
                "start_block_index": 0,
                "end_block_index": 1
            }]
        }
    ]
}
```

### 

Streaming Support

For streaming responses, we've added a `citations_delta` type that contains a single citation to be added to the `citations` list on the current `text` content block.

### Example streaming events

Was this page helpful?

- 

- [How citations work](#how-citations-work)

- [Citable vs non-citable content](#citable-vs-non-citable-content)

- [Citation indices](#citation-indices)

- [Token costs](#token-costs)

- [Feature compatibility](#feature-compatibility)

- [Document Types](#document-types)

- [Choosing a document type](#choosing-a-document-type)

- [Plain text documents](#plain-text-documents)

- [PDF documents](#pdf-documents)

- [Custom content documents](#custom-content-documents)

- [Response Structure](#response-structure)

- [Streaming Support](#streaming-support)

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
