---
title: "Token counting - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/token-counting"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-05T06:36:54Z"
tags: ["api"]
---

# Token counting

Copy page



Count the tokens in a message before you send it to Claude. Use token counts to manage rate limits and costs, make model routing decisions, and fit prompts to a target length.

Copy page



Token counting

Feature of  
[Messages API](build-with-claude-working-with-messages.md)

[APIs](#feature-availability)  
Messages APIAvailableManaged AgentsNot available

[Cloud platforms](#availability-feature-support)  
All platforms

[Data handling](#feature-data-handling)  
ZDR eligibleHIPAA eligible

Token counting lets you determine the number of tokens in a message before you send it to Claude. This helps you make informed decisions about your prompts and usage. With token counting, you can:

- Proactively manage rate limits and costs
- Make smart model routing decisions
- Optimize prompts to a specific length

------------------------------------------------------------------------

## How to count message tokens

The [token counting](../Endpoints/platform-claude-com-messages-count-tokens.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](../Agents-Tools/agents-and-tools-tool-use-overview.md), [images](build-with-claude-vision.md), and [PDFs](build-with-claude-pdf-support.md). The response contains the total number of [input tokens](../Endpoints/platform-claude-com-messages-count-tokens.md#message_tokens_count.input_tokens)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return..

#### [Count tokens in a Message](../Endpoints/platform-claude-com-messages-count-tokens.md)

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

##### Headers `anthropic-version` `anthropic-user-profile-id` `anthropic-workspace-id`



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"anthropic-user-profile-id": optional string



The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Body `messages` `model` `cache_control` `output_config` `speed` `system` +3 more



messages: array of [MessageParam](https://platform.claude.com/docs/en/api/http/messages#message_param)



Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response. This is called prefill. On models that don't support prefill, creating a message that ends with a partial `assistant` response returns a 400 error. See [Prefill not supported](../Endpoints/errors.md#prefill-not-supported).

Example with a single `user` message:

```python
[{"role": "user", "content": "Hello, Claude"}]
```



Example with multiple conversational turns:

```python
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```



Example with a partially-filled response from Claude, for models that support prefill:

```python
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]
```



Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

```python
{"role": "user", "content": "Hello, Claude"}
```



```python
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```



See [input examples](build-with-claude-working-with-messages.md).

Note that if you want to include a [system prompt](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#give-claude-a-role), you can use the top-level `system` parameter.

There is a limit of 100,000 messages in a single request.

One of the following:



UserMessageParam object{ content, role }





content: [MessageContentParam](https://platform.claude.com/docs/en/api/http/messages#message_content_param)



One of the following:

role: "user"





AssistantMessageParam object{ content, role }





content: [MessageContentParam](https://platform.claude.com/docs/en/api/http/messages#message_content_param)



One of the following:

role: "assistant"





SystemMessageParam object{ content, role }





model: [Model](https://platform.claude.com/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-haiku-5-5"



Fastest model for high-volume, real-time tasks

"claude-sonnet-5-5"



Efficient model for coding and agents

"claude-fable-5-1"



Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

"claude-opus-5-5"



Powerful intelligence for coding, knowledge work, and long-running agents

"claude-mythos-5-1"



Our most capable model for cybersecurity and biology research, available through trusted access programs

"claude-sonnet-5"



Efficient model for coding and agents

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"



Most capable model for cybersecurity and biology research

"claude-opus-5"



Powerful intelligence for long-running agents and coding

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

"claude-sonnet-4-6"



Best combination of speed and intelligence

"claude-haiku-4-5"



"claude-haiku-4-5-20251001"



"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding



"claude-mythos-preview"⁠Deprecated



New class of intelligence, strongest in coding and cybersecurity

Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.



"claude-sonnet-4-5"⁠Deprecated



High-performance model for agents and coding

Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.



"claude-sonnet-4-5-20250929"⁠Deprecated



High-performance model for agents and coding

Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

string





cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/http/messages#cache_control_ephemeral) { type: "ephemeral", ttl } or null



Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

type: "ephemeral"





ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude-prompt-caching.md) for details.

One of the following:

"5m"



"1h"





output_config: optional [OutputConfig](https://platform.claude.com/docs/en/api/http/messages#output_config) { effort, format }



Configuration options for the model's output, such as the output format.



effort: optional "low" or "medium" or "high" or 2 more or null



How much effort the model should put into its response. Higher effort levels may result in more thorough analysis but take longer.

Valid values are `low`, `medium`, `high`, `xhigh`, or `max`.

One of the following:

"low"



"medium"



"high"



"xhigh"



"max"





format: optional [JSONOutputFormat](https://platform.claude.com/docs/en/api/http/messages#json_output_format) { type: "json_schema", schema } or null



A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude-structured-outputs.md)

type: "json_schema"



schema: map\[unknown\]



The JSON schema of the format



speed: optional "standard" or "fast" or null



The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

Some models require the `fast-mode-2026-02-01` beta header for any `speed` value. See [fast mode](build-with-claude-fast-mode.md) for which models.

One of the following:

"standard"



"fast"





system: optional string or array of [TextBlockParam](https://platform.claude.com/docs/en/api/http/messages#text_block_param)



System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#give-claude-a-role).

One of the following:

string





array of [TextBlockParam](https://platform.claude.com/docs/en/api/http/messages#text_block_param) { type: "text", text, cache_control, citations }



type: "text"





text: string



minLength1



cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/http/messages#cache_control_ephemeral) { type: "ephemeral", ttl } or null



Create a cache control breakpoint at this content block.

type: "ephemeral"





ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude-prompt-caching.md) for details.

One of the following:

"5m"



"1h"





citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/http/messages#text_citation_param) or null



One of the following:



CitationCharLocationParam object{ type: "char_location", cited_text, document_index, 3 more }



type: "char_location"



cited_text: string





document_index: number



minimum0



document_title: string or null



minLength1

maxLength500

end_char_index: number





start_char_index: number



minimum0



CitationPageLocationParam object{ type: "page_location", cited_text, document_index, 3 more }



type: "page_location"



cited_text: string





document_index: number



minimum0



document_title: string or null



minLength1

maxLength500

end_page_number: number





start_page_number: number



minimum1



CitationContentBlockLocationParam object{ type: "content_block_location", cited_text, document_index, 3 more }



type: "content_block_location"





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



document_index: number



minimum0



document_title: string or null



minLength1

maxLength500



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



start_block_index: number



0-based index of the first cited block in the source's `content` array.

minimum0



CitationWebSearchResultLocationParam object{ type: "web_search_result_location", cited_text, encrypted_index, 2 more }



type: "web_search_result_location"



cited_text: string



encrypted_index: string





title: string or null



minLength1

maxLength512



url: string



minLength1



CitationSearchResultLocationParam object{ type: "search_result_location", cited_text, end_block_index, 4 more }



type: "search_result_location"





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string





start_block_index: number



0-based index of the first cited block in the source's `content` array.

minimum0

title: string or null





thinking: optional [ThinkingConfigParam](https://platform.claude.com/docs/en/api/http/messages#thinking_config_param)



Configuration for Claude's thinking.

With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit.

Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](build-with-claude-thinking.md#configuring-thinking) for each model's behavior.

One of the following:



tool_choice: optional [ToolChoice](https://platform.claude.com/docs/en/api/http/messages#tool_choice)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



tools: optional array of [MessageCountTokensTool](https://platform.claude.com/docs/en/api/http/messages#message_count_tokens_tool)



Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md), see their individual documentation as each has its own behavior (e.g., the [web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)).

Each tool definition includes:

- `name`: Name of the tool.
- `description`: Optional, but strongly-recommended description of the tool.
- `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

For example, if you defined `tools` as:

```python
[
  {
    "name": "get_stock_price",
    "description": "Get the current stock price for a given ticker symbol.",
    "input_schema": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
        }
      },
      "required": ["ticker"]
    }
  }
]
```



And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

```python
[
  {
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
  }
]
```



You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

```python
[
  {
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
  }
]
```



Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

See our [guide](../Agents-Tools/agents-and-tools-tool-use-overview.md) for more details.

One of the following:



Tool object{ type, input_schema, name, 7 more }





ToolBash20250124 object{ type: "bash_20250124", name, allowed_callers, 4 more }





CodeExecutionTool20250522 object{ type: "code_execution_20250522", name, allowed_callers, 3 more }





CodeExecutionTool20250825 object{ type: "code_execution_20250825", name, allowed_callers, 3 more }





CodeExecutionTool20260120 object{ type: "code_execution_20260120", name, allowed_callers, 3 more }



A `tools` entry for the code execution tool, version `code_execution_20260120`. It adds REPL state persistence to version `code_execution_20250825`.

REPL state persistence applies with programmatic tool calling. With it, the Python interpreter state, such as variable bindings, persists across requests that reuse the container.

See the [code execution tool guide](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#tool-versions) to learn what each tool version adds.



CodeExecutionTool20260521 object{ type: "code_execution_20260521", name, allowed_callers, 3 more }



Code execution tool with REPL state persistence.



BrowserToolset20260801 object{ type: "browser_toolset_20260801", cache_control, configs }



The browser toolset: a single `tools[]` entry (carrying no `name`) that declares the browser tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema.



MemoryTool20250818 object{ type: "memory_20250818", name, allowed_callers, 4 more }





ComputerToolset20260801 object{ type: "computer_toolset_20260801", cache_control, configs }



The computer toolset: a single `tools[]` entry (carrying no `name`) that declares the computer tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema. Every member is enabled by default, zoom included. The single-tool options `display_number` and `enable_zoom` are not fields of a toolset entry — it carries only `type`, `configs`, and `cache_control`; zoom is controlled via `configs.zoom.enabled`.



ToolTextEditor20250124 object{ type: "text_editor_20250124", name, allowed_callers, 4 more }





ToolTextEditor20250429 object{ type: "text_editor_20250429", name, allowed_callers, 4 more }





ToolTextEditor20250728 object{ type: "text_editor_20250728", name, allowed_callers, 5 more }





WebSearchTool20250305 object{ type: "web_search_20250305", name, allowed_callers, 7 more }





WebFetchTool20250910 object{ type: "web_fetch_20250910", name, allowed_callers, 9 more }





WebSearchTool20260209 object{ type: "web_search_20260209", name, allowed_callers, 7 more }





WebFetchTool20260209 object{ type: "web_fetch_20260209", name, allowed_callers, 9 more }





WebFetchTool20260309 object{ type: "web_fetch_20260309", name, allowed_callers, 10 more }



Web fetch tool with use_cache parameter for bypassing cached content.



WebSearchTool20260318 object{ type: "web_search_20260318", name, allowed_callers, 8 more }





WebFetchTool20260318 object{ type: "web_fetch_20260318", name, allowed_callers, 11 more }





ToolSearchToolBm25_20251119 object{ type, name, allowed_callers, 3 more }





ToolSearchToolRegex20251119 object{ type, name, allowed_callers, 3 more }



##### Returns `input_tokens`



MessageTokensCount object{ input_tokens }



input_tokens: number



The total number of tokens across the provided list of messages, system prompt, and tools.

This endpoint returns an `invalid_request_error` for a few inputs that the Messages API accepts:

- [Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md) such as web search, web fetch, code execution, and tool search (every server tool except the [advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md))
- The [MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)
- `image` or `document` blocks with a `url` or `file` source

Send images and PDFs as base64 to count them. For requests that use server tools or MCP servers, the Messages API response reports the tokens used in its [`usage`](../Endpoints/messages-create.md#message.usage)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. object.



The token count is an **estimate**. In some cases, the actual number of input tokens used when creating a message might differ by a small amount.

Token counts might include tokens added automatically by Anthropic for system optimizations. **You are not billed for system-added tokens**. Billing reflects only your content.

### Supported models

All [active models](../../20-Models/about-claude-models-overview.md) support token counting.



Claude 4.7 and later models and Claude Mythos Preview use a newer tokenizer. The same input text produces approximately 30 percent more tokens than on earlier models. The exact increase depends on the content and workload shape. Recount prompts against the model you plan to use rather than reusing counts measured against earlier models.

### Count tokens in basic messages

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

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    system="You are a scientist",
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(response.json())
```

Output



```python
{ "input_tokens": 14 }
```

### Count tokens in messages with tools



Token counting supports client tools and the [advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md). Requests that include other [server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md) return an error. For the advisor tool, the count covers the executor’s first sampling call only.

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

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"],
            },
        }
    ],
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
)

print(response.json())
```

Output



```python
{ "input_tokens": 403 }
```

### Count tokens in messages with images

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
import base64
import httpx2

image_url = "https://platform.claude.com/docs/images/vision-example.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx2.get(image_url).content).decode("utf-8")

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                    },
                },
                {"type": "text", "text": "Describe this image"},
            ],
        }
    ],
)
print(response.json())
```

Output



```python
{ "input_tokens": 1028 }
```

An embedded image block that sets [`"oversized_image": "error"`](build-with-claude-vision-coordinates.md#oversized-image-error) is rejected at count time exactly as the Messages API would reject it.

### Count tokens in messages with thinking



See [Thinking and the context window](build-with-claude-thinking.md#thinking-and-the-context-window) for more details.

- Thinking blocks from **previous** assistant turns count toward your input tokens on models that [keep all prior turns](build-with-claude-thinking.md#thinking-block-preservation-by-model); on models that keep only the last turn, the API strips them and they do **not** count.
- **Current** assistant turn thinking **does** count toward your input tokens.

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

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    thinking={"type": "adaptive"},
    messages=[
        {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "thinking",
                    "thinking": "This is a nice number theory question. Let's think about it step by step...",
                    "signature": "EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV...",
                },
                {
                    "type": "text",
                    "text": "Yes, there are infinitely many prime numbers p such that p mod 4 = 3...",
                },
            ],
        },
        {"role": "user", "content": "Can you write a formal proof?"},
    ],
)

print(response.json())
```

Output



```python
{ "input_tokens": 88 }
```

### Count tokens in messages with PDFs



Token counting supports base64-encoded PDFs with the same [PDF requirements](build-with-claude-pdf-support.md#check-pdf-requirements) as the Messages API. This endpoint doesn’t support `url` or `file` document sources.

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
import base64
import anthropic

client = anthropic.Anthropic()

with open("/path/to/document.pdf", "rb") as pdf_file:
    pdf_base64 = base64.standard_b64encode(pdf_file.read()).decode("utf-8")

response = client.messages.count_tokens(
    model="claude-opus-5-5",
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
                },
                {"type": "text", "text": "Please summarize this document."},
            ],
        }
    ],
)

print(response.json())
```

Output



```python
{ "input_tokens": 2188 }
```

------------------------------------------------------------------------

## Token counts on Claude Fable and Claude Mythos models

Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, and Claude Mythos 5 share the tokenizer introduced with Claude Opus 4.7. A prompt counts the same on all four, and roughly 30 percent higher than on models before Claude Opus 4.7 (the exact increase depends on the content). The token counting endpoint counts under the tokenizer of the `model` you pass. To measure the difference for your workload, count the same request twice, once with your current model and once with the model you plan to move to, and compare the two `input_tokens` values.



**Billing and migration:** Usage and billing on these models reflect this tokenizer’s counts. When migrating from a model before Claude Opus 4.7, don’t reuse token counts measured on the older model to estimate costs or context window fit. Count your prompts with the `model` ID you plan to use (for example, `"claude-fable-5-1"`).

------------------------------------------------------------------------

## Pricing and rate limits

Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](../Endpoints/rate-limits.md#rate-limits). If you need higher limits, use **Request tier increase** on the [Rate limits](../Other/playground.md) page in the Claude Console.

| Usage tier | Requests per minute (RPM) |
|------------|---------------------------|
| Start      | 5,000                     |
| Build      | 10,000                    |
| Scale      | 20,000                    |



Token counting and message creation have separate and independent rate limits. Usage of one does not count against the limits of the other.

------------------------------------------------------------------------

## FAQ

### Does token counting use prompt caching?

No, token counting provides an estimate without using caching logic. Although you may provide `cache_control` blocks in your token counting request, prompt caching only occurs during actual message creation.

------------------------------------------------------------------------

## Next steps



[Count message tokens](../Endpoints/platform-claude-com-messages-count-tokens.md)

Read the full API reference for the token counting endpoint.



[Context windows](build-with-claude-context-windows.md)

Use token counts to keep prompts within a model’s context window.



[Rate limits](../Endpoints/rate-limits.md)

Check token counts before you send a request to stay within your usage tier.



[Prompt caching](build-with-claude-prompt-caching.md)

Reduce cost and latency on repeated prompts by caching prompt prefixes.

## Availability

Token counting is available on every model and eligible for zero data retention and HIPAA readiness.

### API support

[Messages API](build-with-claude-working-with-messages.md)

StatusAvailable

Models

- [All models](../../20-Models/about-claude-models-overview.md)

[Managed Agents](../Other/managed-agents-overview.md)

StatusNot available

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages/count_tokens`

Zero data retentionEligible

Excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Count tokens before sending requests.

HIPAAEligible
