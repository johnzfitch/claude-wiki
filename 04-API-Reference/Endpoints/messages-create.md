---
title: "Create a Message - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/messages/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:18Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](http-beta-messages-create.md).

1.  [API reference](http.md)
2.  [Messages](https://platform.claude.com/docs/en/api/http/messages)

# Create a Message

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](../../01-Getting-Started/get-started.md)

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

"anthropic-user-profile-id": optional string



The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Body



max_tokens: number



The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](../Guides/build-with-claude-prompt-caching.md#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](../../20-Models/about-claude-models-overview.md) for details.

minimum0



messages: array of [MessageParam](https://platform.claude.com/docs/en/api/http/messages#message_param)



Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response. This is called prefill. On models that don't support prefill, creating a message that ends with a partial `assistant` response returns a 400 error. See [Prefill not supported](errors.md#prefill-not-supported).

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

See [input examples](../Guides/build-with-claude-working-with-messages.md).

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

Defaults to `5m`. See [prompt caching pricing](../Guides/build-with-claude-prompt-caching.md) for details.

One of the following:

"5m"



"1h"





container: optional [MessageCreateParamsContainer](https://platform.claude.com/docs/en/api/http/messages#message_create_params_container) or null



Container identifier for reuse across requests.

One of the following:



ContainerParams object{ id, skills }



Container parameters with skills to be loaded.

id: optional string or null



Container id



skills: optional array of [SkillParams](https://platform.claude.com/docs/en/api/http/messages#skill_params) { type, skill_id, version } or null



List of skills to load in the container

maxItems20



type: "anthropic" or "custom"



Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"



"custom"





skill_id: string



Skill ID

minLength1

maxLength64



version: optional string



Skill version or 'latest' for most recent version

minLength1

maxLength64

string





diagnostics: optional [DiagnosticsParam](https://platform.claude.com/docs/en/api/http/messages#diagnostics_param) { previous_message_id } or null



Request-level diagnostics. Supply `previous_message_id` to have the response include `diagnostics.cache_miss_reason` explaining any prompt-cache divergence from that prior request.



previous_message_id: optional string or null



The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

maxLength256

inference_geo: optional string or null



Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



metadata: optional [Metadata](https://platform.claude.com/docs/en/api/http/messages#metadata) { user_id }



An object describing metadata about the request.



user_id: optional string or null



An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

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

A schema to specify Claude's output format in responses. See [structured outputs](../Guides/build-with-claude-structured-outputs.md)

type: "json_schema"



schema: map\[unknown\]



The JSON schema of the format



service_tier: optional "auto" or "standard_only"



Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](service-tiers.md) for details.

One of the following:

"auto"



"standard_only"





speed: optional "standard" or "fast" or null



The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

Some models require the `fast-mode-2026-02-01` beta header for any `speed` value. See [fast mode](../Guides/build-with-claude-fast-mode.md) for which models.

One of the following:

"standard"



"fast"





stop_sequences: optional array of string



Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.



stream: optional boolean



Whether to incrementally stream the response using server-sent events. When `true`, SDKs return a raw event stream.

In the TypeScript, Python and Ruby SDKs, the recommended way to stream is `messages.stream()`. It sets `stream` for you and accumulates the events into the final message. See [Streaming with SDKs](../Guides/build-with-claude-streaming.md#streaming-with-sdks) for an example in each language.

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

Defaults to `5m`. See [prompt caching pricing](../Guides/build-with-claude-prompt-caching.md) for details.

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

Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](../Guides/build-with-claude-thinking.md#configuring-thinking) for each model's behavior.

One of the following:



tool_choice: optional [ToolChoice](https://platform.claude.com/docs/en/api/http/messages#tool_choice)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



tools: optional array of [ToolUnion](https://platform.claude.com/docs/en/api/http/messages#tool_union)

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

##### Returns



Message object{ type: "message", id, container, 8 more }





type: "message"



Object type.

For Messages, this is always `"message"`.

defaultmessage



id: string



Unique object identifier.

The format and length of IDs may change over time.



container: [Container](https://platform.claude.com/docs/en/api/http/messages#container) { id, expires_at, skills } or null



Information about the container used in this request.

This will be non-null if a container tool (e.g. code execution) was used.

id: string



Identifier for the container used in this request



expires_at: string



The time at which the container will expire.

formatdate-time



skills: array of [ContainerSkill](https://platform.claude.com/docs/en/api/http/messages#container_skill) { type, skill_id, version } or null



Skills loaded in the container



type: "anthropic" or "custom"



Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"



"custom"





skill_id: string



Skill ID

minLength1

maxLength64



version: string



The resolved version: a skill version ID for custom skills.

minLength1

maxLength64



content: array of [ContentBlock](https://platform.claude.com/docs/en/api/http/messages#content_block)



Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```python
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```python
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```python
[{"type": "text", "text": "B)"}]
```



One of the following:



TextBlock object{ type: "text", citations, text }





ThinkingBlock object{ type: "thinking", signature, thinking }





type: "thinking"



defaultthinking



signature: string



A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

See [extended thinking](../Guides/build-with-claude-extended-thinking.md) for details.

thinking: string



The text of Claude's thinking process for this block.



RedactedThinkingBlock object{ type: "redacted_thinking", data }





type: "redacted_thinking"



defaultredacted_thinking



data: string



The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

See [extended thinking](../Guides/build-with-claude-extended-thinking.md#redacted-thinking-blocks) for details.



ToolUseBlock object{ type: "tool_use", id, caller, 3 more }





ServerToolUseBlock object{ type: "server_tool_use", id, caller, 2 more }





WebSearchToolResultBlock object{ type: "web_search_tool_result", caller, content, tool_use_id }





WebFetchToolResultBlock object{ type: "web_fetch_tool_result", caller, content, tool_use_id }





CodeExecutionToolResultBlock object{ type: "code_execution_tool_result", content, tool_use_id }





type: "code_execution_tool_result"



defaultcode_execution_tool_result



content: [CodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_result_block_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



BashCodeExecutionToolResultBlock object{ type: "bash_code_execution_tool_result", content, tool_use_id }





TextEditorCodeExecutionToolResultBlock object{ type: "text_editor_code_execution_tool_result", content, tool_use_id }





ToolSearchToolResultBlock object{ type: "tool_search_tool_result", content, tool_use_id }





ContainerUploadBlock object{ type: "container_upload", file_id }



Response model for a file uploaded to the container.



type: "container_upload"



defaultcontainer_upload

file_id: string





diagnostics: [Diagnostics](https://platform.claude.com/docs/en/api/http/messages#diagnostics) { cache_miss_reason } or null



Request-level diagnostics. `null` when the request did not supply `diagnostics`, or when it did and no prompt-cache divergence was detected.



cache_miss_reason: [CacheMissReason](https://platform.claude.com/docs/en/api/http/messages#cache_miss_reason) or null



Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



model: [Model](https://platform.claude.com/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



role: "assistant"



Conversational role of the generated message.

This will always be `"assistant"`.

defaultassistant



stop_details: [RefusalStopDetails](https://platform.claude.com/docs/en/api/http/messages#refusal_stop_details) { type: "refusal", category, explanation } or null



Structured information about why model output stopped.

This is `null` when the `stop_reason` has no additional detail to report.



type: "refusal"



defaultrefusal



category: "cyber" or "bio" or "frontier_llm" or 2 more or null



The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"



The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

"bio"



The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

"frontier_llm"



The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

"reasoning_extraction"



The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](../Guides/build-with-claude-thinking-steering-and-cost.md).

"general_harms"



The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.



explanation: string or null



Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



stop_reason: [StopReason](https://platform.claude.com/docs/en/api/http/messages#stop_reason) or null



The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations
- `"model_context_window_exceeded"`: we exceeded the model's context window

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end_turn"



"max_tokens"



"stop_sequence"



"tool_use"



"pause_turn"



"refusal"



"model_context_window_exceeded"





stop_sequence: string or null



Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



usage: [Usage](https://platform.claude.com/docs/en/api/http/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }



Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



RawMessageStreamEvent = [RawMessageStartEvent](https://platform.claude.com/docs/en/api/http/messages#raw_message_start_event) or [RawMessageDeltaEvent](https://platform.claude.com/docs/en/api/http/messages#raw_message_delta_event) or [RawMessageStopEvent](https://platform.claude.com/docs/en/api/http/messages#raw_message_stop_event) or 3 more



One of the following:

Create a Message

cURL



```python
curl https://api.anthropic.com/v1/messages \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    --max-time 600 \
    -d '{
          "max_tokens": 1024,
          "messages": [
            {
              "content": "Hello, world",
              "role": "user"
            }
          ],
          "model": "claude-opus-5-5",
          "stream": false,
          "system": [
            {
              "text": "Today'\''s date is 2024-06-01.",
              "type": "text"
            }
          ],
          "thinking": {
            "type": "adaptive"
          },
          "tools": [
            {
              "input_schema": {
                "type": "object",
                "properties": {
                  "location": "bar",
                  "unit": "bar"
                },
                "required": [
                  "location"
                ]
              },
              "name": "name"
            }
          ]
        }'
```

Response 200



```python
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "container_011CpZohnwH4vuy7gazohgSP",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "The grass is green. The sky is blue.",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 0,
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-5-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "global",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  }
}
```

##### Returns Examples

Response 200



```python
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "container_011CpZohnwH4vuy7gazohgSP",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "The grass is green. The sky is blue.",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 0,
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-5-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
