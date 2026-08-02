---
title: "Web fetch tool - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-08-02T05:39:56Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

Thinking

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Compaction](/docs/en/build-with-claude/compaction)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics (beta)](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

MCP tunnels

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[](/login)




Messages

Web fetch tool

Messages/Tools

# Web fetch tool




Fetch and read content from specific URLs to augment Claude's context with live web content.






For how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

The web fetch tool allows Claude to retrieve full content from specified web pages and PDF documents.

The latest web fetch tool version (`web_fetch_20260318`) supports **dynamic filtering** with Claude Fable 5, Claude Opus 4.8, Claude Mythos 5, [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, and Claude Sonnet 4.6. Claude can write and execute code to filter fetched content before it reaches the context window, keeping only relevant information and discarding the rest. This reduces token consumption while maintaining response quality. `web_fetch_20260318` also adds [response inclusion](#response-inclusion) control for agentic workflows. The previous versions (`web_fetch_20260309` for dynamic filtering and [cache bypass](#cache-bypass), `web_fetch_20260209` for dynamic filtering only, `web_fetch_20250910` for basic fetch) remain available.

Web fetch (with and without dynamic filtering) is available on the Claude API, [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry). On Microsoft Foundry, web fetch requires a [Hosted on Anthropic deployment](/docs/en/build-with-claude/claude-in-microsoft-foundry#additional-features-not-supported-when-hosted-on-azure). It is not currently available on Amazon Bedrock or Google Cloud.



For [Claude Mythos Preview](https://anthropic.com/glasswing), web fetch is available on the Claude API and Microsoft Foundry. It is not currently available for Mythos Preview on Amazon Bedrock or Google Cloud.



Use the [feedback form](https://forms.gle/NhWcgmkcvPCMmPE86) to provide feedback on the quality of the model responses, the API itself, or the quality of the documentation.

For Zero Data Retention eligibility and the `allowed_callers` workaround, see [Server tools](/docs/en/agents-and-tools/tool-use/server-tools#zdr-and-allowed-callers).



Enabling the web fetch tool in environments where Claude processes untrusted input alongside sensitive data poses data exfiltration risks. Only use this tool in trusted environments or when handling non-sensitive data.

To minimize exfiltration risks, Claude is not allowed to dynamically construct URLs. Claude can only fetch URLs that have been explicitly provided by the user or that come from previous web search or web fetch results. However, there is still residual risk that you should carefully consider when using this tool.

If data exfiltration is a concern, consider:

- Disabling the web fetch tool entirely
- Using the `max_uses` parameter to limit the number of requests
- Using the `allowed_domains` parameter to restrict to known safe domains

For model support, see the [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference).




How web fetch works

Web fetch is a [server tool](/docs/en/agents-and-tools/tool-use/server-tools): the API fetches the content during the request and inserts the results into the conversation. You don't run anything or return a `tool_result`. The exception is when Claude calls web fetch and one of your client tools in the same group of parallel tool calls: the API returns the response with `stop_reason: "tool_use"` before that fetch has run, then runs the fetch when you send back the client `tool_result` blocks. See [Mixing server tools and client tools in one turn](/docs/en/agents-and-tools/tool-use/server-tools#mixing-server-tools-and-client-tools-in-one-turn).

When you add the web fetch tool to your API request:

1.  Claude determines when to fetch content based on the prompt and available URLs.
2.  The API retrieves the full text content from the specified URL.
3.  For PDFs, the API returns the content as base64-encoded data and processes it like a directly attached PDF document.
4.  Claude analyzes the fetched content and provides a response with optional citations.



The web fetch tool currently does not support websites dynamically rendered with JavaScript.




When Claude fetches

Claude fetches when the request points at a specific page or document:

- A URL is provided in the conversation (or a previous tool result)
- The user names a specific resource (a particular article, README, pricing page, or documentation section) without a URL, and the [web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool) is also enabled so Claude can locate it first (see [Combined search and fetch](#combined-search-and-fetch))

Claude does **not** fetch for general-knowledge or open-ended questions that don't reference a specific page. "Summarize this article: `<url>`" triggers a fetch. "What are best practices for REST API design?" is answered directly.




Dynamic filtering

Fetching full web pages and PDFs can quickly consume tokens, especially when only specific information is needed from large documents. With `web_fetch_20260209` or later, Claude can write and execute code to filter the fetched content before loading it into context.

This dynamic filtering is particularly useful for:

- Extracting specific sections from long documents
- Processing structured data from web pages
- Filtering relevant information from PDFs
- Reducing token costs when working with large documents



Dynamic filtering runs on the [code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool), which the API enables automatically for the request. You don't need to add the code execution tool to the `tools` array.

To enable dynamic filtering, use `web_fetch_20260209` or any later version. The following examples use `web_fetch_20260318`:

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
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Fetch the content at https://example.com/research-paper and extract the key findings.",
        }
    ],
    tools=[{"type": "web_fetch_20260318", "name": "web_fetch"}],
)
print(response)
```




How to use web fetch

Provide the web fetch tool in your API request:

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
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Please analyze the content at https://example.com/article",
        }
    ],
    tools=[{"type": "web_fetch_20250910", "name": "web_fetch", "max_uses": 5}],
)
print(response)
```




Tool definition

The web fetch tool supports the following parameters:

JSON



```python
{
  "type": "web_fetch_20250910",
  "name": "web_fetch",

  // Optional: Limit the number of fetches per request
  "max_uses": 10,

  // Optional: Only fetch from these domains
  "allowed_domains": ["example.com", "docs.example.com"],

  // Optional: Never fetch from these domains (cannot be combined with allowed_domains)
  "blocked_domains": ["private.example.com"],

  // Optional: Enable citations for fetched content
  "citations": {
    "enabled": true
  },

  // Optional: Maximum content length in tokens
  "max_content_tokens": 100000
}
```

Later tool versions add two more optional parameters: `use_cache` requires `web_fetch_20260309` or later (see [Cache bypass](#cache-bypass)), and `response_inclusion` requires `web_fetch_20260318` or later (see [Response inclusion](#response-inclusion)).




Max uses

The `max_uses` parameter limits the number of web fetches performed. Failed fetches count against the limit. If Claude attempts more fetches than allowed, the `web_fetch_tool_result` is an error with the `max_uses_exceeded` error code. There is currently no default limit.




Domain filtering

For domain filtering with `allowed_domains` and `blocked_domains`, see [Server tools](/docs/en/agents-and-tools/tool-use/server-tools#domain-filtering).




Content limits

The `max_content_tokens` parameter limits the amount of content included in the context. If the fetched content exceeds this limit, the tool truncates it. This helps control token usage when fetching large documents. The limit applies to text content, not to binary content such as PDFs.



The `max_content_tokens` parameter limit is approximate. The actual number of input tokens used can vary by a small amount.




Cache bypass



Requires `web_fetch_20260309` or later (including `web_fetch_20260318`).

The `use_cache` parameter controls whether cached content may be returned. Set `"use_cache": false` to bypass the cache and fetch fresh content. The default is `true`. Only disable caching when the user explicitly requests fresh content or when fetching rapidly changing sources, because bypassing the cache increases latency.

```python
{
  "tools": [
    {
      "type": "web_fetch_20260309",
      "name": "web_fetch",
      "use_cache": false
    }
  ]
}
```






Response inclusion



Requires `web_fetch_20260318` or later.

The `response_inclusion` parameter controls how fetch result blocks appear in the API response when the result was consumed by a completed [code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool) call in the same turn. Set `"response_inclusion": "excluded"` to drop those nested `server_tool_use` and result block pairs entirely from the response, reducing output token costs for agentic workflows that don't need to echo raw page content back to the client. The default is `"full"`. Results from direct calls, or from code execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

```python
{
  "tools": [
    {
      "type": "web_fetch_20260318",
      "name": "web_fetch",
      "response_inclusion": "excluded"
    }
  ]
}
```






Citations

Unlike web search where citations are always enabled, citations are optional for web fetch and disabled by default. Set `"citations": {"enabled": true}` to enable Claude to cite specific passages from fetched documents.



When displaying API outputs directly to end users, include citations to the original source. If you are making modifications to API outputs, including by reprocessing and/or combining them with your own material before displaying them to end users, display citations as appropriate based on consultation with your legal team.




Response

Here's an example response structure:

Output



```python
{
  "role": "assistant",
  "content": [
    // 1. Claude's decision to fetch
    {
      "type": "text",
      "text": "I'll fetch the content from the article to analyze it."
    },
    // 2. The fetch request
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01234567890abcdef",
      "name": "web_fetch",
      "input": {
        "url": "https://example.com/article"
      }
    },
    // 3. Fetch results
    {
      "type": "web_fetch_tool_result",
      "tool_use_id": "srvtoolu_01234567890abcdef",
      "content": {
        "type": "web_fetch_result",
        "url": "https://example.com/article",
        "content": {
          "type": "document",
          "source": {
            "type": "text",
            "media_type": "text/plain",
            "data": "Full text content of the article..."
          },
          "title": "Article Title",
          "citations": { "enabled": true }
        },
        "retrieved_at": "2025-08-25T10:30:00Z"
      }
    },
    // 4. Claude's analysis with citations (if enabled)
    {
      "text": "Based on the article, ",
      "type": "text"
    },
    {
      "text": "the main argument presented is that artificial intelligence will transform healthcare",
      "type": "text",
      "citations": [
        {
          "type": "char_location",
          "document_index": 0,
          "document_title": "Article Title",
          "start_char_index": 1234,
          "end_char_index": 1456,
          "cited_text": "Artificial intelligence is poised to revolutionize healthcare delivery..."
        }
      ]
    }
  ],
  "id": "msg_a930390d3a",
  "usage": {
    "input_tokens": 25039,
    "output_tokens": 931,
    "server_tool_use": {
      "web_fetch_requests": 1
    }
  },
  "stop_reason": "end_turn"
}
```




Fetch results

Fetch results include:

- `url`: The URL that was fetched
- `content`: A document block containing the fetched content
- `retrieved_at`: Timestamp when the content was retrieved



The web fetch tool caches results to improve performance and reduce redundant requests. The content returned may not always reflect the latest version available at the URL. The cache behavior is managed automatically and may change over time to optimize for different content types and usage patterns. To fetch fresh content, set `"use_cache": false` (see [Cache bypass](#cache-bypass)).

For PDF documents, content is returned as base64-encoded data:

Output



```python
{
  "type": "web_fetch_tool_result",
  "tool_use_id": "srvtoolu_02",
  "content": {
    "type": "web_fetch_result",
    "url": "https://example.com/paper.pdf",
    "content": {
      "type": "document",
      "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBvYmo..."
      },
      "citations": { "enabled": true }
    },
    "retrieved_at": "2025-08-25T10:30:02Z"
  }
}
```




Errors

When the web fetch tool encounters an error, the Claude API returns a 200 (success) response with the error represented in the response body. Claude sees the error result and continues the turn. For example:

Output



```python
{
  "type": "web_fetch_tool_result",
  "tool_use_id": "srvtoolu_a93jad",
  "content": {
    "type": "web_fetch_tool_result_error",
    "error_code": "url_not_accessible"
  }
}
```

These are the possible error codes:

- `invalid_tool_input`: Invalid tool input, such as a malformed URL or a non-HTTP(S) scheme
- `url_too_long`: URL exceeds maximum length (250 characters)
- `url_not_allowed`: URL blocked by domain filtering rules (including your organization's settings) or by Anthropic-side restrictions, such as private addresses and `robots.txt`
- `url_not_in_prior_context`: URL did not appear earlier in the conversation (see [URL validation](#url-validation))
- `url_not_accessible`: Failed to fetch content (HTTP error)
- `too_many_requests`: Rate limit exceeded
- `unsupported_content_type`: Content type not supported (only text, HTML, and PDF)
- `max_uses_exceeded`: Maximum web fetch tool uses exceeded
- `unavailable`: An internal error occurred




URL validation

For security reasons, the web fetch tool can only fetch URLs that have previously appeared in the conversation context. This includes:

- URLs in user messages
- URLs in client-side tool results
- URLs from previous web search or web fetch results

The tool cannot fetch arbitrary URLs that Claude generates or URLs from container-based server tools (such as Code Execution and Bash).




Combined search and fetch

When both the web search and web fetch tools are enabled, and the user names a specific page or document without providing a URL (for example, "read the README from the anthropics/anthropic-sdk-python repository"), Claude uses web search to locate it, then fetches the result. The following example asks for a search and an analysis in one request:

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
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Find recent articles about quantum computing and analyze the most relevant one in detail",
        }
    ],
    tools=[
        {"type": "web_search_20250305", "name": "web_search", "max_uses": 3},
        {
            "type": "web_fetch_20250910",
            "name": "web_fetch",
            "max_uses": 5,
            "citations": {"enabled": True},
        },
    ],
)
print(response)
```

In this workflow, Claude:

1.  Uses web search to find relevant articles.
2.  Selects the most promising results.
3.  Uses web fetch to retrieve full content.
4.  Provides detailed analysis with citations.




Prompt caching

For caching tool definitions across turns, see [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).




Streaming

With streaming enabled, fetch events are part of the stream with a pause during content retrieval:

Output



```python
event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

// Claude's decision to fetch

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_fetch"}}

// Fetch URL streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"url\":\"https://example.com/article\"}"}}

// Pause while fetch executes

// Fetch results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_fetch_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"type": "web_fetch_result", "url": "https://example.com/article", "content": {"type": "document", "source": {"type": "text", "media_type": "text/plain", "data": "Article content..."}}}}}

// Claude's response continues...
```




Batch requests

You can include the web fetch tool in the [Messages Batches API](/docs/en/build-with-claude/batch-processing). Web fetch tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.




Usage and pricing

Web fetch usage has **no additional charges** beyond standard token costs:

```python
{
  "usage": {
    "input_tokens": 25039,
    "output_tokens": 931,
    "cache_read_input_tokens": 0,
    "cache_creation_input_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 1
    }
  }
}
```



The web fetch tool is available on the Claude API at **no additional cost**. You only pay standard token costs for the fetched content that becomes part of your conversation context.

To protect against inadvertently fetching large content that would consume excessive tokens, use the `max_content_tokens` parameter to set appropriate limits based on your use case and budget considerations.

Example token usage for typical content:

- Average web page (10 kB): ~2,500 tokens
- Large documentation page (100 kB): ~25,000 tokens
- Research paper PDF (500 kB): ~125,000 tokens




Next steps




Code execution tool

Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions.


Server tools

Work with Anthropic-executed tools: server_tool_use blocks, pause_turn continuation, and domain filtering.




Tool reference

Directory of Anthropic-provided tools and reference for optional tool definition properties.
