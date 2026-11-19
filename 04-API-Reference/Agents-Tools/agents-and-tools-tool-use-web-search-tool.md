---
title: "Web search tool - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-13T06:35:21Z"
tags: ["api", "prompting", "search"]
---

# Web search tool

Copy page



Give Claude access to current web content with cited sources, optional dynamic filtering, and domain controls.

Copy page



Web search tool

[Models](#feature-availability)  
- All models

[APIs](#feature-availability)  
- Messages API
- Managed Agents

[Cloud platforms](#feature-availability)  
- Claude API
- Claude Platform on AWS
- Claude Models on Google CloudAnthropic managed
- Claude Models on Google CloudGoogle managed
- Microsoft Foundry

[Data handling](#feature-data-handling)  
ZDRZDR eligibleHIPAAHIPAA eligible

Usage differs by product

Messages API

Add a `web_search` tool to the request’s `tools`. Settings such as `max_uses`, domain lists and `user_location` go on that tool.

Managed Agents

On by default in the agent toolset, without `max_uses`, `citations` or `cache_control`.

The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. The response includes citations for sources drawn from search results.

With `web_search_20260209` and later versions, Claude can write and run code that filters the search results before they reach the context window (**dynamic filtering**), keeping only relevant information. Dynamic filtering is available with Claude 4.6 and later models and [Claude Mythos Preview](../../22-Safety-Policy/glasswing.md).

Three versions of the web search tool are available:

- `web_search_20250305`: basic web search
- `web_search_20260209`: adds [dynamic filtering](#dynamic-filtering)
- `web_search_20260318`: adds [response inclusion](#response-inclusion) control for agentic workflows

The examples on this page use `web_search_20250305` for basic search and `web_search_20260318` for dynamic filtering.



For [Claude Mythos Preview](../../22-Safety-Policy/glasswing.md), web search is supported on the Claude API, Claude Models on Google Cloud (Google managed), and Microsoft Foundry.

For web search’s Zero Data Retention eligibility and the related `allowed_callers` configuration, see [Server tools](agents-and-tools-tool-use-server-tools.md#zdr-and-allowed-callers).

For model support, see the [Tool reference](agents-and-tools-tool-use-tool-reference.md).

To check whether a model accepts web search before you send a request, read its `capabilities.server_tools.web_search.supported` value from the Models API. [Using the Models API](../../20-Models/about-claude-models-overview.md#using-the-models-api) describes the field.

## How web search works

When you add the web search tool to your API request:

1.  Claude determines when to search based on the prompt.
2.  The API runs the searches and provides Claude with the results. This process can repeat multiple times throughout a single request.
3.  At the end of its turn, Claude provides a final response with cited sources.

### When Claude searches

Claude searches when the request depends on information that is current, changing, or outside its training data:

- Recent events, news, or announcements
- Current prices, rates, scores, or statistics
- Information about specific organizations, people, or products that might have changed
- Explicit requests to search or look something up

Claude answers directly without searching when the request draws on stable knowledge:

- Established facts, math, science fundamentals, or coding concepts
- Creative writing or brainstorming
- Analysis of content already provided in the conversation
- Conversational turns and greetings

Triggering is steerable through your system prompt: you can encourage Claude to search more readily or to prefer answering directly. To enforce a limit, use [`max_uses`](#max-uses) to cap the number of searches in a turn.

### Dynamic filtering

With basic web search, every search result is loaded into Claude’s context window, and much of that content can be irrelevant to the request. With `web_search_20260209` or later, Claude instead writes and runs code that filters the results first, so only relevant content reaches the context window. This reduces token use on search-heavy requests.

Dynamic filtering runs web search from inside [code execution](agents-and-tools-tool-use-code-execution-tool.md): on `web_search_20260209` and later, the tool’s `allowed_callers` field defaults to `["code_execution_20260120"]`, and when dynamic filtering runs, the API provisions the code execution it needs for the request automatically. You don’t need to add the code execution tool to `tools` yourself. There are no additional charges for code execution calls made this way beyond the standard token costs.

To call web search directly, without dynamic filtering, set `allowed_callers: ["direct"]`. Models that don’t support programmatic tool calling require this setting. Without it, the API returns a 400 error that tells you to set it.



The web search tool (with and without dynamic filtering) is available on the Claude API, [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md), and [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md). On Microsoft Foundry, deployments [hosted on Azure](../Guides/build-with-claude-claude-in-microsoft-foundry.md#additional-features-not-supported-when-hosted-on-azure) support only the basic web search tool (`web_search_20250305`, without dynamic filtering). Deployments hosted on Anthropic support all versions. On Claude Models on Google Cloud (Google managed), only the basic web search tool (without dynamic filtering) is available.

The following examples use `web_search_20260318`:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.",
        }
    ],
    tools=[{"type": "web_search_20260318", "name": "web_search"}],
)
print(response)
```

## How to use web search



Web search is enabled for your organization unless an administrator has disabled it in the [Claude Console](../Other/playground.md), where they can also restrict which domains it searches. If it’s disabled, a Messages API request that includes the tool fails with a 400 `invalid_request_error` that says web search is not enabled, rather than an [error code](#errors) inside a search result.

For how your organization’s web search settings apply in Claude Managed Agents sessions, see [Restrict web search and web fetch domains](../Other/managed-agents-tools-web-restrictions.md).

Provide the web search tool in your API request:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=[{"role": "user", "content": "What's the weather in NYC?"}],
    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
)
print(response)
```

## Tool definition

The web search tool supports the following parameters:

JSON



```python
{
  "type": "web_search_20250305",
  "name": "web_search",

  // Optional: Limit the number of searches
  "max_uses": 5,

  // Optional: Only include results from these domains.
  // Use allowed_domains or blocked_domains, not both.
  "allowed_domains": ["example.com", "trusteddomain.org"],

  // Optional: Never include results from these domains
  "blocked_domains": ["untrustedsource.com"],

  // Optional: Localize search results
  "user_location": {
    "type": "approximate",
    "city": "San Francisco",
    "region": "California",
    "country": "US",
    "timezone": "America/Los_Angeles"
  }
}
```

All web search tool versions accept `allowed_callers`, which controls whether Claude calls web search directly or from code execution through [dynamic filtering](#dynamic-filtering). On `web_search_20260209` and later it defaults to `["code_execution_20260120"]` instead of `["direct"]`. See [ZDR and allowed_callers](agents-and-tools-tool-use-server-tools.md#zdr-and-allowed-callers) for how to configure it. `web_search_20260318` and later also accept [`response_inclusion`](#response-inclusion).

### Max uses

The `max_uses` parameter limits the number of searches in a single turn. Single-fact queries typically use 1–3 searches; comparative or multientity research can use 10 or more.

Failed searches count against the limit. If Claude calls web search directly more times than allowed, the `web_search_tool_result` is an error with the `max_uses_exceeded` error code. If Claude calls web search from code execution more times than allowed, the code execution run ends with an error.

A turn can span several requests. A request continues a turn when it resumes after [`pause_turn`](agents-and-tools-tool-use-server-tools.md#the-server-side-loop-and-pause-turn) or when its last message contains only `tool_result` blocks. Searches from earlier requests in that turn count against the limit, unless Claude ran them from code execution through [dynamic filtering](#dynamic-filtering).

### Domain filtering

Provide `allowed_domains` or `blocked_domains`, not both. If a request includes both, the API returns a 400 error. Entries are bare domains with an optional path, for example `example.com` or `example.com/blog`, without a scheme.

For the full domain filtering rules, see [Domain filtering](agents-and-tools-tool-use-server-tools.md#domain-filtering) in the Server tools guide.

On [Claude Managed Agents](../Other/managed-agents-overview.md), set these fields on the `web_search` entry of the agent toolset; see [Restrict web search and web fetch domains](../Other/managed-agents-tools-web-restrictions.md).

### Localization

The `user_location` parameter allows you to localize search results based on a user’s location. Provide at least one of `city`, `region`, `country`, or `timezone`.

- `type`: The type of location (must be `approximate`)
- `city`: The city name
- `region`: The region or state
- `country`: The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code (the API rejects an unsupported code with a 400 error)
- `timezone`: The [IANA time zone ID](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

On Claude Managed Agents, the `web_search` entry of the agent toolset also accepts `user_location`; see the [web tool settings](../Other/managed-agents-tools-web-restrictions.md#settings).

### Response inclusion



Requires `web_search_20260318` or later.

The `response_inclusion` parameter controls how search result blocks appear in the API response when a completed [code execution](agents-and-tools-tool-use-code-execution-tool.md) call in the same response consumed the result. Set `"response_inclusion": "excluded"` to drop those nested `server_tool_use` and result block pairs entirely from the response, for agentic workflows that don’t need the raw search content. Token usage is unaffected, because Claude reads the code’s output rather than these blocks. The default is `"full"`. The API always returns results from direct calls, or from code execution calls that paused before completing, in full so that you can send them back in the next request.

JSON



```python
{
  "tools": [
    {
      "type": "web_search_20260318",
      "name": "web_search",
      "response_inclusion": "excluded"
    }
  ]
}
```

## Response

Here’s an example response structure:

Output



```python
{
  "role": "assistant",
  "content": [
    // 1. Claude's decision to search
    {
      "type": "text",
      "text": "I'll search for when Claude Shannon was born."
    },
    // 2. The search query used
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "name": "web_search",
      "input": {
        "query": "claude shannon birth date"
      }
    },
    // 3. Search results
    {
      "type": "web_search_tool_result",
      "tool_use_id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "content": [
        {
          "type": "web_search_result",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_content": "EqgfCioIARgBIiQ3YTAwMjY1Mi1mZjM5LTQ1NGUtODgxNC1kNjNjNTk1ZWI3Y...",
          "page_age": "April 30, 2025"
        }
      ]
    },
    {
      "text": "Based on the search results, ",
      "type": "text"
    },
    // 4. Claude's response with citations
    {
      "text": "Claude Shannon was born on April 30, 1916, in Petoskey, Michigan",
      "type": "text",
      "citations": [
        {
          "type": "web_search_result_location",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_index": "Eo8BCioIAhgBIiQyYjQ0OWJmZi1lNm..",
          "cited_text": "Claude Elwood Shannon (April 30, 1916 – February 24, 2001) was an American mathematician, electrical engineer, computer scientist, cryptographer and i..."
        }
      ]
    }
  ],
  "id": "msg_a930390d3a",
  "usage": {
    "input_tokens": 6039,
    "output_tokens": 931,
    "server_tool_use": {
      "web_search_requests": 1
    }
  },
  "stop_reason": "end_turn"
}
```

This example shows a direct search. When a search runs through [dynamic filtering](#dynamic-filtering), the response also contains the result blocks of the [code execution tool](agents-and-tools-tool-use-code-execution-tool.md), and each nested `server_tool_use` and `web_search_tool_result` pair carries a `caller` field identifying the code execution call that made it.

### Search results

Search results include:

- `url`: The URL of the source page
- `title`: The title of the source page
- `page_age`: When the site was last updated
- `encrypted_content`: Encrypted content that you must pass back in multi-turn conversations

To continue a conversation that contains search results, send the assistant’s content blocks back exactly as you received them, including each result’s `encrypted_content`. The API decrypts that content in later requests to restore the search results in Claude’s context. If `encrypted_content` is missing or modified, the request fails with a 400 validation error.

### Citations

Citations are always enabled for web search, and each `web_search_result_location` includes:

- `url`: The URL of the cited source
- `title`: The title of the cited source
- `encrypted_index`: A reference that must be passed back for multi-turn conversations
- `cited_text`: Up to 150 characters of the cited content

The web search citation fields `cited_text`, `title`, and `url` do not count toward input or output token usage.



When displaying API outputs directly to end users, citations must be included to the original source. If you are making modifications to API outputs, including by reprocessing or combining them with your own material before displaying them to end users, display citations as appropriate based on consultation with your legal team.

### Errors

When the web search tool encounters an error (such as hitting rate limits), the Claude API still returns a 200 (success) response. The error is represented within the response body using the following structure:

Output



```python
{
  "type": "web_search_tool_result",
  "tool_use_id": "srvtoolu_a93jad",
  "content": {
    "type": "web_search_tool_result_error",
    "error_code": "max_uses_exceeded"
  }
}
```

On an error, `content` is a single error object rather than a list of result blocks. A search that succeeds but matches no results returns an empty `content` list, not an error.

These are the possible error codes:

- `too_many_requests`: Rate limit exceeded
- `invalid_tool_input`: Invalid search query parameter
- `max_uses_exceeded`: Maximum web search tool uses exceeded
- `query_too_long`: Query exceeds maximum length
- `request_too_large`: The search request is too large, typically because of a long domain filter list
- `unavailable`: An internal error occurred

### `pause_turn` stop reason

The API can pause a long-running search turn and return `stop_reason: "pause_turn"`. To continue, send the paused assistant message back unchanged in a new request.

If Claude calls web search and one of your client tools in the same group of parallel tool calls, the API returns `stop_reason: "tool_use"` instead and does not run the search yet. To continue, return the client tool results, and the API runs the search in the next request. See [Mixing server tools and client tools in one turn](agents-and-tools-tool-use-server-tools.md#mixing-server-tools-and-client-tools-in-one-turn).

For the server-side loop and `pause_turn` handling, see [The server-side loop and pause_turn](agents-and-tools-tool-use-server-tools.md#the-server-side-loop-and-pause-turn) in the Server tools guide.

## Prompt caching

To cache tool definitions across turns, see [Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md).

## Streaming

With streaming enabled, you receive search events as part of the stream. There is a pause while the search runs:

Output



```python
event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

// Claude's decision to search

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_search"}}

// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"latest quantum computing breakthroughs 2025\"}"}}

// Pause while search runs

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": [{"type": "web_search_result", "title": "Quantum Computing Breakthroughs in 2025", "url": "https://example.com"}]}}

// Claude's response with citations (omitted in this example)
```

## Batch requests

You can include the web search tool in the [Message Batches API](../Guides/build-with-claude-batch-processing.md). Web search tool calls through the Message Batches API are priced the same as those in regular Messages API requests.

To protect shared capacity, the Batches API throttles web search requests for each organization, so large batches with many searches might take longer to complete. You can see your organization’s web search rate limit on the [Rate limits](../Other/playground.md) page in the Claude Console. To request a higher limit, contact sales from that page.

## Usage and pricing

Web search usage is charged in addition to token usage:

```python
{
  "usage": {
    "input_tokens": 105,
    "output_tokens": 6039,
    "cache_read_input_tokens": 7123,
    "cache_creation_input_tokens": 7345,
    "server_tool_use": {
      "web_search_requests": 1
    }
  }
}
```



Web search is available on the Claude API for **\$10 USD per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations run during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. A web search that fails with an error is not billed.

## Next steps



[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)

Fetch and read content from specific URLs to augment Claude’s context with live web content.



[Server tools](agents-and-tools-tool-use-server-tools.md)

Work with tools that Anthropic runs: `server_tool_use` blocks, `pause_turn` continuation, and domain filtering.



[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Directory of Anthropic-provided tools and reference for optional tool definition properties.

## Availability

Web search tool

Cloud platform

Cloud platform: Claude API

Claude API

APIs  
- Messages API
- Managed Agents

Models  
- All models

Claude Platform on AWS

APIs  
- Messages API
- Managed Agents

Models  
- All models

Claude Models on Google Cloud (Anthropic managed)

API  
- Messages API

Models  
- All models

Claude Models on Google Cloud (Google managed)

API  
- Messages API

Models  
- All models

Note  
Only the basic web search tool (`web_search_20250305`), without dynamic filtering.

Microsoft Foundry (hosted on Azure)

API  
- Messages API

Models  
- All models

Note  
Only the basic web search tool (`web_search_20250305`), without dynamic filtering.

Microsoft Foundry (hosted on Anthropic)

API  
- Messages API

Models  
- All models

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages` with `web_search` tool

Zero data retentionEligible

Excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Real-time web search results returned in the API response. Dynamic filtering for web search is not eligible for ZDR or HIPAA.

HIPAAEligible

Dynamic filtering for web search is not eligible for ZDR or HIPAA.
