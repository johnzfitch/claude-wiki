---
title: "Search results - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/search-results"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:26Z"
tags: ["api", "search"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fsearch-results)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)Model capabilities

# Search results

Copy page



Enable natural citations for RAG applications by providing search results with source attribution

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

Search result content blocks let Claude cite your own content the same way it cites web search results: each citation carries the source and title you provided. Use them in RAG (Retrieval-Augmented Generation) applications where Claude needs to attribute answers to your documents.

All [active models](/docs/en/models/overview) support search results with citations, with the exception of Claude Haiku 3. No beta header is required: search results are part of the standard Messages API.

## How it works

Search results can be provided in two ways:

1.  **From tool calls:** Your custom tools return search results, enabling dynamic RAG applications
2.  **As top-level content:** You provide search results directly in user messages for pre-fetched or cached content

In both cases, Claude cites the search results automatically when citations are enabled. No special prompting is needed: ask your question, and citations appear on the text blocks that draw on your content.

### Search result schema

Search results use the following structure:

```python
{
  "type": "search_result",
  "source": "https://example.com/article", // Required: Source URL or identifier
  "title": "Article Title", // Required: Title of the result
  "content": [
    // Required: Array of text blocks
    {
      "type": "text",
      "text": "The actual content of the search result..."
    }
  ],
  "citations": {
    // Optional: Citation configuration
    "enabled": true // Enable/disable citations for this result
  }
}
```



### Required fields

| Field     | Type   | Description                                                                                                      |
|-----------|--------|------------------------------------------------------------------------------------------------------------------|
| `type`    | string | Must be `"search_result"`                                                                                        |
| `source`  | string | The source of the content. Any stable string works: a URL, or an internal identifier such as `kb://article-1234` |
| `title`   | string | A descriptive title for the search result                                                                        |
| `content` | array  | An array of text blocks containing the actual content                                                            |

### Optional fields

| Field           | Type   | Description                                                                                                                                                                                                                                                 |
|-----------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `citations`     | object | Citation configuration with `enabled` Boolean field. Citations are disabled by default; every example on this page sets `"enabled": true` explicitly. All search results in a request must use the same setting (see [Citation control](#citation-control)) |
| `cache_control` | object | Cache control settings (for example, `{"type": "ephemeral"}`)                                                                                                                                                                                               |

Each item in the `content` array must be a text block with:

- `type`: Must be `"text"`
- `text`: The actual text content (non-empty string)

Search results hold text only. Images and other media are not supported inside the `content` array.

## Method 1: Search results from tool calls

Returning search results from your custom tools enables dynamic RAG applications: tools fetch content at runtime, and Claude cites it in the response. The following example forces the tool call with [`tool_choice`](/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use), so the retrieval step runs every time.

### Example: Knowledge base tool

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
from anthropic.types import (
    MessageParam,
    TextBlockParam,
    SearchResultBlockParam,
    ToolResultBlockParam,
)

client = Anthropic()

# Define a knowledge base search tool
knowledge_base_tool = {
    "name": "search_knowledge_base",
    "description": "Search the company knowledge base for information",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string", "description": "The search query"}},
        "required": ["query"],
    },
}


# Function to handle the tool call
def search_knowledge_base(query):
    # Your search logic here
    # Returns search results in the correct format
    return [
        SearchResultBlockParam(
            type="search_result",
            source="https://docs.company.com/product-guide",
            title="Product Configuration Guide",
            content=[
                TextBlockParam(
                    type="text",
                    text="To configure the product, navigate to Settings > Configuration. The default timeout is 30 seconds, but can be adjusted between 10-120 seconds based on your needs.",
                )
            ],
            citations={"enabled": True},
        ),
        SearchResultBlockParam(
            type="search_result",
            source="https://docs.company.com/troubleshooting",
            title="Troubleshooting Guide",
            content=[
                TextBlockParam(
                    type="text",
                    text="If you encounter timeout errors, first check the configuration settings. Common causes include network latency and incorrect timeout values.",
                )
            ],
            citations={"enabled": True},
        ),
    ]


# Build up the conversation in a list, starting with the user's question
messages = [
    MessageParam(role="user", content="How do I configure the timeout settings?")
]

# Create a message with the tool
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    tools=[knowledge_base_tool],
    tool_choice={"type": "tool", "name": "search_knowledge_base"},
    messages=messages,
)

# When Claude calls the tool, provide the search results.
# The tool_use block is not always first: iterate to find it.
tool_use = next((block for block in response.content if block.type == "tool_use"), None)
if tool_use is not None:
    tool_result = search_knowledge_base(tool_use.input["query"])

    # Append Claude's turn, then the tool result, to the running conversation
    messages.append(MessageParam(role="assistant", content=response.content))
    messages.append(
        MessageParam(
            role="user",
            content=[
                ToolResultBlockParam(
                    type="tool_result",
                    tool_use_id=tool_use.id,
                    content=tool_result,  # Search results go here
                )
            ],
        )
    )

    # Send the tool result back
    final_response = client.messages.create(
        model="claude-opus-5",
        max_tokens=1024,
        messages=messages,
    )
    print(final_response)
```

## Method 2: Search results as top-level content

You can also provide search results directly in user messages. This is useful for:

- Pre-fetched content from your search infrastructure
- Cached search results from previous queries
- Content from external search services
- Testing and development

### Example: Direct search results

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
from anthropic.types import MessageParam, TextBlockParam, SearchResultBlockParam

client = Anthropic()

# Provide search results directly in the user message
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        MessageParam(
            role="user",
            content=[
                SearchResultBlockParam(
                    type="search_result",
                    source="https://docs.company.com/api-reference",
                    title="API Reference - Authentication",
                    content=[
                        TextBlockParam(
                            type="text",
                            text="All API requests must include an API key in the Authorization header. Keys can be generated from the dashboard. Rate limits: 1000 requests per hour for standard tier, 10000 for premium.",
                        )
                    ],
                    citations={"enabled": True},
                ),
                SearchResultBlockParam(
                    type="search_result",
                    source="https://docs.company.com/quickstart",
                    title="Getting Started Guide",
                    content=[
                        TextBlockParam(
                            type="text",
                            text="To get started: 1) Sign up for an account, 2) Generate an API key from the dashboard, 3) Install our SDK using pip install company-sdk, 4) Initialize the client with your API key.",
                        )
                    ],
                    citations={"enabled": True},
                ),
                TextBlockParam(
                    type="text",
                    text="Based on these search results, how do I authenticate API requests and what are the rate limits?",
                ),
            ],
        )
    ],
)

print(response)
```

## Claude's response with citations

Regardless of how search results are provided, Claude automatically includes citations when using information from them:

```python
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "All API requests must include an API key in the Authorization header. Keys can be generated from the dashboard.",
      "citations": [
        {
          "type": "search_result_location",
          "cited_text": "All API requests must include an API key in the Authorization header. Keys can be generated from the dashboard. Rate limits: 1000 requests per hour for standard tier, 10000 for premium.",
          "source": "https://docs.company.com/api-reference",
          "title": "API Reference - Authentication",
          "search_result_index": 0,
          "start_block_index": 0,
          "end_block_index": 1
        }
      ]
    },
    {
      "type": "text",
      "text": "\n\nTo set this up from scratch, you'll need to "
    },
    {
      "type": "text",
      "text": "sign up for an account, generate an API key from the dashboard, install the SDK using `pip install company-sdk`, and initialize the client with your API key.",
      "citations": [
        {
          "type": "search_result_location",
          "cited_text": "To get started: 1) Sign up for an account, 2) Generate an API key from the dashboard, 3) Install our SDK using pip install company-sdk, 4) Initialize the client with your API key.",
          "source": "https://docs.company.com/quickstart",
          "title": "Getting Started Guide",
          "search_result_index": 1,
          "start_block_index": 0,
          "end_block_index": 1
        }
      ]
    }
  ]
}
```



### Citation fields

Each citation includes:

| Field                 | Type           | Description                                                                                                                                                               |
|-----------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`                | string         | Always `"search_result_location"` for search result citations                                                                                                             |
| `source`              | string         | The source from the original search result                                                                                                                                |
| `title`               | string or null | The title from the original search result                                                                                                                                 |
| `cited_text`          | string         | The full text of the cited block(s), concatenated. Equals the contents of `content[start_block_index:end_block_index]` joined together. Not counted toward output tokens. |
| `search_result_index` | integer        | 0-based index of the cited search result among all `search_result` blocks in the request, in the order they appear (across all messages and tool results).                |
| `start_block_index`   | integer        | 0-based index of the first cited block in the search result's `content` array.                                                                                            |
| `end_block_index`     | integer        | Exclusive end index of the cited block range in the search result's `content` array. Always greater than `start_block_index`.                                             |

The block indices identify a slice of the search result's `content` array, and `cited_text` is the full text of that slice. The text block is the minimal citable unit: Claude cites whole blocks, not substrings within a block. To get finer-grained citations, split your search result content into smaller blocks (see [Multiple content blocks](#multiple-content-blocks)).

## Multiple content blocks

Search results can contain multiple text blocks in the `content` array:

```python
{
  "type": "search_result",
  "source": "https://docs.company.com/api-guide",
  "title": "API Documentation",
  "content": [
    {
      "type": "text",
      "text": "Authentication: All API requests require an API key."
    },
    {
      "type": "text",
      "text": "Rate Limits: The API allows 1000 requests per hour per key."
    },
    {
      "type": "text",
      "text": "Error Handling: The API returns standard HTTP status codes."
    }
  ],
  "citations": { "enabled": true }
}
```



A citation referencing the rate limits block looks like:

```python
{
  "type": "search_result_location",
  "cited_text": "Rate Limits: The API allows 1000 requests per hour per key.",
  "source": "https://docs.company.com/api-guide",
  "title": "API Documentation",
  "search_result_index": 0,
  "start_block_index": 1,
  "end_block_index": 2
}
```



When this search result is cited, `start_block_index` and `end_block_index` identify which of these blocks the citation covers, and `cited_text` contains exactly those blocks' text. Splitting content into smaller, focused blocks gives Claude finer citation boundaries; combining content into one block means every citation returns the full text. This is the same model used by [custom content documents](/docs/en/build-with-claude/citations#custom-content-documents) in the Citations feature.

## Advanced usage

### Combining both methods

You can mix both methods in the same conversation. Claude cites from either source, and `search_result_index` counts all `search_result` blocks in request order, regardless of source.

The following example replays a complete conversation. The first user message carries a pre-fetched search result, the assistant turn calls a knowledge base tool, and the tool result returns a second search result. Claude's answer cites both sources:

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
from anthropic.types import (
    MessageParam,
    SearchResultBlockParam,
    TextBlockParam,
    ToolResultBlockParam,
    ToolUseBlockParam,
)

client = Anthropic()

knowledge_base_tool = {
    "name": "search_knowledge_base",
    "description": "Search the company knowledge base for information",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string", "description": "The search query"}},
        "required": ["query"],
    },
}

# Replay a conversation that provides search results both ways: the first
# user message carries a pre-fetched result, the tool result returns another
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[knowledge_base_tool],
    messages=[
        MessageParam(
            role="user",
            content=[
                SearchResultBlockParam(
                    type="search_result",
                    source="https://docs.company.com/overview",
                    title="Product Overview",
                    content=[
                        TextBlockParam(
                            type="text",
                            text="Acme Dashboard is a monitoring tool for distributed systems. It supports real-time alerting and custom metric dashboards.",
                        )
                    ],
                    citations={"enabled": True},
                ),
                TextBlockParam(
                    type="text",
                    text="What does Acme Dashboard do, and what plans is it available on?",
                ),
            ],
        ),
        MessageParam(
            role="assistant",
            content=[
                TextBlockParam(
                    type="text", text="Let me check the pricing information."
                ),
                ToolUseBlockParam(
                    type="tool_use",
                    id="toolu_01A09q90qw90lq917835lq9",
                    name="search_knowledge_base",
                    input={"query": "Acme Dashboard pricing plans"},
                ),
            ],
        ),
        MessageParam(
            role="user",
            content=[
                ToolResultBlockParam(
                    type="tool_result",
                    tool_use_id="toolu_01A09q90qw90lq917835lq9",
                    content=[
                        SearchResultBlockParam(
                            type="search_result",
                            source="https://docs.company.com/pricing",
                            title="Pricing Plans",
                            content=[
                                TextBlockParam(
                                    type="text",
                                    text="Acme Dashboard is available on the Starter plan at $10 per user per month and the Enterprise plan with custom pricing.",
                                )
                            ],
                            citations={"enabled": True},
                        )
                    ],
                )
            ],
        ),
    ],
)

print(response)
```

The response cites both sources. The pre-fetched result is `search_result_index: 0` and the tool-returned result is `search_result_index: 1`, matching the order the `search_result` blocks appear in the conversation:

```python
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Here's what I found about Acme Dashboard:\n\n**What it does:** "
    },
    {
      "type": "text",
      "text": "Acme Dashboard is a monitoring tool for distributed systems. It supports real-time alerting and custom metric dashboards.",
      "citations": [
        {
          "type": "search_result_location",
          "cited_text": "Acme Dashboard is a monitoring tool for distributed systems. It supports real-time alerting and custom metric dashboards.",
          "source": "https://docs.company.com/overview",
          "title": "Product Overview",
          "search_result_index": 0,
          "start_block_index": 0,
          "end_block_index": 1
        }
      ]
    },
    {
      "type": "text",
      "text": "\n\n**Available plans:** "
    },
    {
      "type": "text",
      "text": "Acme Dashboard is available on the Starter plan at $10 per user per month and the Enterprise plan with custom pricing.",
      "citations": [
        {
          "type": "search_result_location",
          "cited_text": "Acme Dashboard is available on the Starter plan at $10 per user per month and the Enterprise plan with custom pricing.",
          "source": "https://docs.company.com/pricing",
          "title": "Pricing Plans",
          "search_result_index": 1,
          "start_block_index": 0,
          "end_block_index": 1
        }
      ]
    }
  ]
}
```



### Mixing with other content types

In user messages, `search_result` blocks can sit alongside any other content block. The Method 2 example pairs search results with a `text` question, and image or document blocks can join them the same way.

Tool results are stricter: if any block in a `tool_result` content array is a `search_result`, all of its blocks must be `search_result`. Mixing search results with other block types in the same tool result returns a validation error. To return supporting text alongside tool-sourced search results, include it as a text block inside one of the search results' `content` arrays, where it also becomes citable.

### Cache control

Add `cache_control` on the search result block to cache it for reuse across requests. It sits alongside `citations` on the same block:

```python
{
  "type": "search_result",
  "source": "https://docs.company.com/guide",
  "title": "User Guide",
  "content": [{ "type": "text", "text": "..." }],
  "citations": { "enabled": true },
  "cache_control": { "type": "ephemeral" }
}
```



See [Prompt caching](/docs/en/build-with-claude/prompt-caching) for minimum cacheable lengths and other requirements.

### Citation control

By default, citations are disabled for search results. You can enable citations by explicitly setting the `citations` configuration:

```python
{
  "type": "search_result",
  "source": "https://docs.company.com/guide",
  "title": "User Guide",
  "content": [{ "type": "text", "text": "Important documentation..." }],
  "citations": {
    "enabled": true // Enable citations for this result
  }
}
```



When `citations.enabled` is set to `true`, Claude attaches citation references to the text blocks that draw on the search result.



Citations are all-or-nothing: either all search results in a request must have citations enabled, or all must have them disabled. Mixing search results with different citation settings results in an error.

## Best practices

### For tool-based search (Method 1)

- **Dynamic content:** Use for real-time searches and dynamic RAG applications
- **Error handling:** Return appropriate messages when searches fail
- **Result limits:** Return only the most relevant results to avoid context overflow

### For top-level search (Method 2)

- **Pre-fetched content:** Use when you already have search results
- **Batch processing:** Ideal for processing multiple search results at once
- **Testing:** Great for testing citation behavior with known content

### General best practices

1.  **Structure results effectively:**

    - Use clear, permanent source URLs
    - Provide descriptive titles
    - Break long content into logical text blocks to give Claude finer citation boundaries

2.  **Maintain consistency:**

    - Use consistent source formats across your application
    - Ensure titles accurately reflect content
    - Keep formatting consistent

3.  **Handle errors gracefully:** when a search fails or returns nothing, return a plain text block describing the outcome (for example, `{"type": "text", "text": "No results found."}`) instead of raising an error: Claude explains the empty result to the user, and the conversation continues.

## Limitations

- Search result content blocks are available on Claude API, Amazon Bedrock, and Google Cloud.
- Only text content is supported within search results (no images or other media).
- `search_result` blocks can only appear in user messages (including inside tool results). Assistant messages with search results are rejected.
- When the [web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool) is enabled in the same request, citations must be enabled on all `search_result` blocks.

## Next steps



[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)

Detect and handle refusal stop reasons in streaming responses, and retry refused requests on a fallback model.



[Citations](/docs/en/build-with-claude/citations)

Ground Claude's responses in your source documents. Citations return the exact passages that support each claim, so you can verify answers and surface sources to your users.



[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)

Give Claude access to current web content with cited sources, optional dynamic filtering, and domain controls.



[Messages API reference](/docs/en/api/messages/create)

See the complete Messages API documentation, including content block types.



[Prompt caching](/docs/en/build-with-claude/prompt-caching)

Cache search results with `cache_control` to reduce cost and latency on repeated requests.
