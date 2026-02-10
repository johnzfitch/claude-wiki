---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:17Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/pdf-support"
title: "PDF support - Claude API Docs"
---

Capabilities

# PDF support

Copy page

Process PDFs with Claude. Extract text, analyze charts, and understand visual content from your documents.

Copy page

You can now ask Claude about any text, pictures, charts, and tables in PDFs you provide. Some sample use cases:

- Analyzing financial reports and understanding charts/tables
- Extracting key information from legal documents
- Translation assistance for documents
- Converting document information into structured formats

## 

Before you begin

### 

Check PDF requirements

Claude works with any standard PDF. However, you should ensure your request size meets these requirements when using PDF support:

| Requirement               | Limit                                  |
|---------------------------|----------------------------------------|
| Maximum request size      | 32MB                                   |
| Maximum pages per request | 100                                    |
| Format                    | Standard PDF (no passwords/encryption) |

Please note that both limits are on the entire request payload, including any other content sent alongside PDFs.

Since PDF support relies on Claude's vision capabilities, it is subject to the same [limitations and considerations](/docs/en/build-with-claude/vision#limitations) as other vision tasks.

### 

Supported platforms and models

PDF support is currently supported via direct API access and Google Vertex AI. All [active models](/docs/en/about-claude/models/overview) support PDF processing.

PDF support is now available on Amazon Bedrock with the following considerations:

### 

Amazon Bedrock PDF Support

When using PDF support through Amazon Bedrock's Converse API, there are two distinct document processing modes:

**Important**: To access Claude's full visual PDF understanding capabilities in the Converse API, you must enable citations. Without citations enabled, the API falls back to basic text extraction only. Learn more about [working with citations](/docs/en/build-with-claude/citations).

#### 

Document Processing Modes

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

#### 

Key Limitations

- **Converse API**: Visual PDF analysis requires citations to be enabled. There is currently no option to use visual analysis without citations (unlike the InvokeModel API).
- **InvokeModel API**: Provides full control over PDF processing without forced citations.

#### 

Common Issues

If customers report that Claude isn't seeing images or charts in their PDFs when using the Converse API, they likely need to enable the citations flag. Without it, Converse falls back to basic text extraction only.

This is a known constraint with the Converse API that we're working to address. For applications that require visual PDF analysis without citations, consider using the InvokeModel API instead.

For non-PDF files like .csv, .xlsx, .docx, .md, or .txt files, see [Working with other file formats](/docs/en/build-with-claude/files#working-with-other-file-formats).

------------------------------------------------------------------------

## 

Process PDFs with Claude

### 

Send your first PDF request

Let's start with a simple example using the Messages API. You can provide PDFs to Claude in three ways:

1.  As a URL reference to a PDF hosted online
2.  As a base64-encoded PDF in `document` content blocks
3.  By a `file_id` from the [Files API](/docs/en/build-with-claude/files)

#### 

Option 1: URL-based PDF document

The simplest approach is to reference a PDF directly from a URL:

Shell

``` shiki
 curl https://api.anthropic.com/v1/messages \
   -H "content-type: application/json" \
   -H "x-api-key: $ANTHROPIC_API_KEY" \
   -H "anthropic-version: 2023-06-01" \
   -d '{
     "model": "claude-opus-4-6",
     "max_tokens": 1024,
     "messages": [{
         "role": "user",
         "content": [{
             "type": "document",
             "source": {
                 "type": "url",
                 "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
             }
         },
         {
             "type": "text",
             "text": "What are the key findings in this document?"
         }]
     }]
 }'
```

#### 

Option 2: Base64-encoded PDF document

If you need to send PDFs from your local system or when a URL isn't available:

Shell

``` shiki
# Method 1: Fetch and encode a remote PDF
curl -s "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf" | base64 | tr -d '\n' > pdf_base64.txt

# Method 2: Encode a local PDF file
# base64 document.pdf | tr -d '\n' > pdf_base64.txt

# Create a JSON request file using the pdf_base64.txt content
jq -n --rawfile PDF_BASE64 pdf_base64.txt '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [{
        "role": "user",
        "content": [{
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": $PDF_BASE64
            }
        },
        {
            "type": "text",
            "text": "What are the key findings in this document?"
        }]
    }]
}' > request.json

# Send the API request using the JSON file
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d @request.json
```

#### 

Option 3: Files API

For PDFs you'll use repeatedly, or when you want to avoid encoding overhead, use the [Files API](/docs/en/build-with-claude/files):

Shell

``` shiki
# First, upload your PDF to the Files API
curl -X POST https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "file=@document.pdf"

# Then use the returned file_id in your message
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -d '{
    "model": "claude-opus-4-6", 
    "max_tokens": 1024,
    "messages": [{
      "role": "user",
      "content": [{
        "type": "document",
        "source": {
          "type": "file",
          "file_id": "file_abc123"
        }
      },
      {
        "type": "text",
        "text": "What are the key findings in this document?"
      }]
    }]
  }'
```

### 

How PDF support works

When you send a PDF to Claude, the following steps occur:

1.  1

    The system extracts the contents of the document.

    - The system converts each page of the document into an image.
    - The text from each page is extracted and provided alongside each page's image.

2.  2

    Claude analyzes both the text and images to better understand the document.

    - Documents are provided as a combination of text and images for analysis.
    - This allows users to ask for insights on visual elements of a PDF, such as charts, diagrams, and other non-textual content.

3.  3

    Claude responds, referencing the PDF's contents if relevant.

    Claude can reference both textual and visual content when it responds. You can further improve performance by integrating PDF support with:

    - **Prompt caching**: To improve performance for repeated analysis.
    - **Batch processing**: For high-volume document processing.
    - **Tool use**: To extract specific information from documents for use as tool inputs.

### 

Estimate your costs

The token count of a PDF file depends on the total text extracted from the document as well as the number of pages:

- Text token costs: Each page typically uses 1,500-3,000 tokens per page depending on content density. Standard API pricing applies with no additional PDF fees.
- Image token costs: Since each page is converted into an image, the same [image-based cost calculations](/docs/en/build-with-claude/vision#evaluate-image-size) are applied.

You can use [token counting](/docs/en/build-with-claude/token-counting) to estimate costs for your specific PDFs.

------------------------------------------------------------------------

## 

Optimize PDF processing

### 

Improve performance

Follow these best practices for optimal results:

- Place PDFs before text in your requests
- Use standard fonts
- Ensure text is clear and legible
- Rotate pages to proper upright orientation
- Use logical page numbers (from PDF viewer) in prompts
- Split large PDFs into chunks when needed
- Enable prompt caching for repeated analysis

### 

Scale your implementation

For high-volume processing, consider these approaches:

#### 

Use prompt caching

Cache PDFs to improve performance on repeated queries:

Shell

``` shiki
# Create a JSON request file using the pdf_base64.txt content
jq -n --rawfile PDF_BASE64 pdf_base64.txt '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [{
        "role": "user",
        "content": [{
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": $PDF_BASE64
            },
            "cache_control": {
              "type": "ephemeral"
            }
        },
        {
            "type": "text",
            "text": "Which model has the highest human preference win rates across each use-case?"
        }]
    }]
}' > request.json

# Then make the API call using the JSON file
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d @request.json
```

#### 

Process document batches

Use the Message Batches API for high-volume workflows:

Shell

``` shiki
# Create a JSON request file using the pdf_base64.txt content
jq -n --rawfile PDF_BASE64 pdf_base64.txt '
{
  "requests": [
      {
          "custom_id": "my-first-request",
          "params": {
              "model": "claude-opus-4-6",
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
                                "data": $PDF_BASE64
                            }
                        },
                        {
                            "type": "text",
                            "text": "Which model has the highest human preference win rates across each use-case?"
                        }
                    ]
                }
              ]
          }
      },
      {
          "custom_id": "my-second-request",
          "params": {
              "model": "claude-opus-4-6",
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
                                "data": $PDF_BASE64
                            }
                        },
                        {
                            "type": "text",
                            "text": "Extract 5 key insights from this document."
                        }
                    ]
                }
              ]
          }
      }
  ]
}
' > request.json

# Then make the API call using the JSON file
curl https://api.anthropic.com/v1/messages/batches \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d @request.json
```

## 

Next steps

[](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision)

Try PDF examples

Explore practical examples of PDF processing in our cookbook recipe.

[](/docs/en/api/messages)

View API reference

See complete API documentation for PDF support.

Was this page helpful?

- 

- [Before you begin](#before-you-begin)

- [Check PDF requirements](#check-pdf-requirements)

- [Supported platforms and models](#supported-platforms-and-models)

- [Amazon Bedrock PDF Support](#amazon-bedrock-pdf-support)

- [Process PDFs with Claude](#process-pdfs-with-claude)

- [Send your first PDF request](#send-your-first-pdf-request)

- [How PDF support works](#how-pdf-support-works)

- [Estimate your costs](#estimate-your-costs)

- [Optimize PDF processing](#optimize-pdf-processing)

- [Improve performance](#improve-performance)

- [Scale your implementation](#scale-your-implementation)

- [Next steps](#next-steps)

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
