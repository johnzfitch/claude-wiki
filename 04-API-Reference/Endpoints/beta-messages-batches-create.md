---
title: "Create a Message Batch - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/messages/batches/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:33:19Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Messages](platform-claude-com-http-beta-messages.md)
4.  [Batches](https://platform.claude.com/docs/en/api/http/beta/messages/batches)

# Create a Message Batch

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](../Guides/build-with-claude-batch-processing.md)

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](platform-claude-com-http-beta.md#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"output-128k-2025-02-19"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"



"ce-plugins-2026-09-01"



"spend-limit-reads-2026-09-26"



"telemetry-destinations-2026-08-11"



"webhooks-2026-10-07"



"admin-user-sign-out-2026-10-08"



"message-threads-2026-08-12"



"analytics-usage-cost-2026-08-24"



"experimental-claude-tag-2026-10-21"





"message-batches-2024-09-24"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"prompt-caching-2024-07-31"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"pdfs-2024-09-25"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"token-counting-2024-11-01"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"token-efficient-tools-2025-02-19"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"files-api-2025-04-14"⁠Deprecated



Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14



"extended-cache-ttl-2025-04-11"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"skills-2025-10-02"⁠Deprecated



Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02



"cache-diagnosis-2026-04-07"⁠Deprecated



This value is no longer needed. Remove it from your requests.



"ce-user-management-2026-07-13"⁠Deprecated



This value is no longer needed. Remove it from your requests.

"anthropic-user-profile-id": optional string



The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Body



requests: array of object{ custom_id, params }



List of requests for prompt completion. Each is an individual request to create a Message.

minItems1

maxItems100000



custom_id: string



Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

minLength1

maxLength64

pattern^\[a-zA-Z0-9\_-\]{1,64}\$



params: object{ max_tokens, messages, model, 21 more }



Messages API creation parameters for the individual request.

See the [Messages API reference](messages.md) for full documentation on available parameters.



max_tokens: number



The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](../Guides/build-with-claude-prompt-caching.md#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](../../20-Models/about-claude-models-overview.md) for details.

minimum0



messages: array of [BetaMessageParam](platform-claude-com-http-beta-messages.md#beta_message_param)

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

BetaUserMessageParam object{ content, role }





content: [BetaMessageContentParam](platform-claude-com-http-beta-messages.md#beta_message_content_param)



One of the following:

role: "user"





BetaAssistantMessageParam object{ content, role }





content: [BetaMessageContentParam](platform-claude-com-http-beta-messages.md#beta_message_content_param)



One of the following:

role: "assistant"





BetaSystemMessageParam object{ role, clear_at, content, output_config }





model: [Model](https://platform.claude.com/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



cache_control: optional [BetaCacheControlEphemeral](platform-claude-com-http-beta-messages.md#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

compaction: optional [BetaCompactionConfig](platform-claude-com-http-beta-messages.md#beta_compaction_config) { type: "summarize", instructions } or null

⁠





Compaction configuration.

When set on `POST /v1/messages`, the request is a compaction request: the conversation in `messages` is summarized and the response holds only the resulting `compaction` block (`stop_reason` `"compaction"`), which later requests send first in `messages` in place of the messages it summarizes. `POST /v1/messages/count_tokens` accepts this parameter and ignores it: the count it returns is for the conversation in `messages` as sent. Cannot be combined with `context_management`.

type: "summarize"





instructions: optional string or null



Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent.

maxLength16384



container: optional [BetaContainerParams](platform-claude-com-http-beta-messages.md#beta_container_params) or string or null



Container identifier for reuse across requests.

One of the following:



BetaContainerParams object{ id, skills }



Container parameters with skills to be loaded.

id: optional string or null



Container id



skills: optional array of [BetaSkillParams](platform-claude-com-http-beta-messages.md#beta_skill_params) { type, skill_id, version } or null

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

context_management: optional [BetaContextManagementConfig](platform-claude-com-http-beta-messages.md#beta_context_management_config) { edits } or null

⁠





Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



diagnostics: optional [BetaDiagnosticsParam](platform-claude-com-http-beta-messages.md#beta_diagnostics_param) { previous_message_id } or null



Request-level diagnostics. Supply `previous_message_id` to have the response include `diagnostics.cache_miss_reason` explaining any prompt-cache divergence from that prior request.



previous_message_id: optional string or null



The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

maxLength256



fallback_credit_token: optional string or [BetaFallbackCreditTokenParam](platform-claude-com-http-beta-messages.md#beta_fallback_credit_token_param) or null

⁠





The `fallback_credit_token` from a prior refusal's `stop_details`.

When a preceding request was refused and returned a `fallback_credit_token`, pass that code here on the retry to have the retry's cache-creation tokens for the prefix that was warm on the refused model billed at the cache-read rate. Must be redeemed by the same organization and workspace, with the same request body (optionally extended by one appended `assistant` message whose content is the partial text — with any trailing whitespace stripped from the final text block — and paired server-tool blocks streamed before the refusal; the appended-assistant form is not available for requests with `output_format` set or forced `tool_choice`), on an eligible fallback model, on the same platform, and within 5 minutes of the refusal; a mismatch is a 400. A token minted mid-server-tool-loop whose partial content was continuable may only be redeemed with the appended-assistant form — if an exact-body retry is rejected with a 400 saying the token must be redeemed by continuing the partial response, retry with the appended-assistant form instead.

When the appended-assistant form is used on a model that otherwise disallows assistant-turn prefill, this token also authorizes that one prefill.

One of the following:

string





BetaFallbackCreditTokenParam object{ token, mode }



Object form of `fallback_credit_token`: the token plus a redemption mode.

Requires `anthropic-beta: fallback-credit-2026-07-01`; without that header the field accepts the bare string only. The bare string and the mode-less object are equivalent (both select `strict`), so wrapping an existing token changes nothing by itself.



token: string



The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

minLength1

maxLength2048



mode: optional "strict" or "best_effort"



How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

One of the following:

"strict"



"best_effort"





fallbacks: optional [BetaFallbacksParam](platform-claude-com-http-beta-messages.md#beta_fallbacks_param) or null

⁠





Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. Some models don't support fallbacks; on those models, a list of fallback models returns a 400 error. See [Server-side fallback](../Guides/build-with-claude-refusals-and-fallback.md#server-side-fallback). The string "default" requests the requested model's server-defined default fallback configuration. On a model that doesn't support fallbacks, the request runs on the requested model alone, so a declined request stays declined.

One of the following:

inference_geo: optional string or null



Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



mcp_servers: optional array of [BetaRequestMCPServerURLDefinition](platform-claude-com-http-beta-messages.md#beta_request_mcp_server_url_definition) { type: "url", name, url, 2 more }

⁠





MCP servers to be utilized in this request

maxItems20

type: "url"



name: string



url: string



authorization_token: optional string or null





tool_configuration: optional [BetaRequestMCPServerToolConfiguration](platform-claude-com-http-beta-messages.md#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled } or null



allowed_tools: optional array of string or null



enabled: optional boolean or null





metadata: optional [BetaMetadata](platform-claude-com-http-beta-messages.md#beta_metadata) { user_id }



An object describing metadata about the request.



user_id: optional string or null



An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



output_config: optional [BetaOutputConfig](platform-claude-com-http-beta-messages.md#beta_output_config) { effort, format, task_budget }



Configuration options for the model's output, such as the output format.

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

system: optional string or array of [BetaTextBlockParam](platform-claude-com-http-beta-messages.md#beta_text_block_param)



System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#give-claude-a-role).

One of the following:

string





array of [BetaTextBlockParam](platform-claude-com-http-beta-messages.md#beta_text_block_param) { type: "text", text, cache_control, citations }



type: "text"





text: string



minLength1



cache_control: optional [BetaCacheControlEphemeral](platform-claude-com-http-beta-messages.md#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

citations: optional array of [BetaTextCitationParam](platform-claude-com-http-beta-messages.md#beta_text_citation_param) or null



One of the following:



BetaCitationCharLocationParam object{ type: "char_location", cited_text, document_index, 3 more }

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

BetaCitationPageLocationParam object{ type: "page_location", cited_text, document_index, 3 more }

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

BetaCitationContentBlockLocationParam object{ type: "content_block_location", cited_text, document_index, 3 more }

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

BetaCitationWebSearchResultLocationParam object{ type: "web_search_result_location", cited_text, encrypted_index, 2 more }

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

BetaCitationSearchResultLocationParam object{ type: "search_result_location", cited_text, end_block_index, 4 more }

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

thinking: optional [BetaThinkingConfigParam](platform-claude-com-http-beta-messages.md#beta_thinking_config_param)



Configuration for Claude's thinking.

With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit.

Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](../Guides/build-with-claude-thinking.md#configuring-thinking) for each model's behavior.

One of the following:



thread: optional [BetaMessageThreadParam](platform-claude-com-http-beta-messages.md#beta_message_thread_param) or null

⁠





Server-held conversation state (a Thread). `{"type": "create"}` asks the server to hold this conversation's state under the response's `id`; `{"type": "continue", "previous_message_id": ...}` resumes from a previous response so only the new turn's messages are sent. The response shape is unchanged.

One of the following:



BetaThreadCreateParams object{ type: "create" }



Start holding conversation state under this response's `id`.

type: "create"





BetaThreadContinueParams object{ type: "continue", previous_message_id }



Resume from the response named by `previous_message_id`.

type: "continue"



previous_message_id: string



The `id` of the previous response in this Thread.



tool_choice: optional [BetaToolChoice](platform-claude-com-http-beta-messages.md#beta_tool_choice)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



tools: optional array of [BetaToolUnion](platform-claude-com-http-beta-messages.md#beta_tool_union)

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

BetaTool object{ type, input_schema, name, 7 more }





BetaToolBash20241022 object{ type: "bash_20241022", name, allowed_callers, 4 more }

⁠







BetaToolBash20250124 object{ type: "bash_20250124", name, allowed_callers, 4 more }





BetaCodeExecutionTool20250522 object{ type: "code_execution_20250522", name, allowed_callers, 3 more }





BetaCodeExecutionTool20250825 object{ type: "code_execution_20250825", name, allowed_callers, 3 more }





BetaCodeExecutionTool20260120 object{ type: "code_execution_20260120", name, allowed_callers, 3 more }



A `tools` entry for the code execution tool, version `code_execution_20260120`. It adds REPL state persistence to version `code_execution_20250825`.

REPL state persistence applies with programmatic tool calling. With it, the Python interpreter state, such as variable bindings, persists across requests that reuse the container.

See the [code execution tool guide](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#tool-versions) to learn what each tool version adds.



BetaCodeExecutionTool20260521 object{ type: "code_execution_20260521", name, allowed_callers, 3 more }



Code execution tool with REPL state persistence.



BetaBrowserToolset20260801 object{ type: "browser_toolset_20260801", cache_control, configs }



The browser toolset: a single `tools[]` entry (carrying no `name`) that declares the browser tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema.



BetaToolComputerUse20241022 object{ type: "computer_20241022", display_height_px, display_width_px, 7 more }

⁠







BetaMemoryTool20250818 object{ type: "memory_20250818", name, allowed_callers, 4 more }





BetaToolComputerUse20250124 object{ type: "computer_20250124", display_height_px, display_width_px, 7 more }

⁠







BetaToolTextEditor20241022 object{ type: "text_editor_20241022", name, allowed_callers, 4 more }

⁠







BetaToolComputerUse20251124 object{ type: "computer_20251124", display_height_px, display_width_px, 8 more }

⁠







BetaComputerToolset20260801 object{ type: "computer_toolset_20260801", cache_control, configs }



The computer toolset: a single `tools[]` entry (carrying no `name`) that declares the computer tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema. Every member is enabled by default, zoom included. The single-tool options `display_number` and `enable_zoom` are not fields of a toolset entry — it carries only `type`, `configs`, and `cache_control`; zoom is controlled via `configs.zoom.enabled`.



BetaToolTextEditor20250124 object{ type: "text_editor_20250124", name, allowed_callers, 4 more }





BetaToolTextEditor20250429 object{ type: "text_editor_20250429", name, allowed_callers, 4 more }





BetaToolTextEditor20250728 object{ type: "text_editor_20250728", name, allowed_callers, 5 more }





BetaWebSearchTool20250305 object{ type: "web_search_20250305", name, allowed_callers, 7 more }





BetaWebFetchTool20250910 object{ type: "web_fetch_20250910", name, allowed_callers, 9 more }





BetaWebSearchTool20260209 object{ type: "web_search_20260209", name, allowed_callers, 7 more }





BetaWebFetchTool20260209 object{ type: "web_fetch_20260209", name, allowed_callers, 9 more }





BetaWebFetchTool20260309 object{ type: "web_fetch_20260309", name, allowed_callers, 10 more }



Web fetch tool with use_cache parameter for bypassing cached content.



BetaWebSearchTool20260318 object{ type: "web_search_20260318", name, allowed_callers, 8 more }





BetaWebFetchTool20260318 object{ type: "web_fetch_20260318", name, allowed_callers, 11 more }





BetaAdvisorTool20260301 object{ type: "advisor_20260301", model, name, 7 more }

⁠







BetaToolSearchToolBm25_20251119 object{ type, name, allowed_callers, 3 more }





BetaToolSearchToolRegex20251119 object{ type, name, allowed_callers, 3 more }





BetaMCPToolset object{ type: "mcp_toolset", mcp_server_name, cache_control, 3 more }

⁠





Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.



output_format: optional [BetaJSONOutputFormat](platform-claude-com-http-beta-messages.md#beta_json_output_format) { type: "json_schema", schema } or null

⁠Deprecated





Deprecated: Use `output_config.format` instead. See [structured outputs](../Guides/build-with-claude-structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

type: "json_schema"



schema: map\[unknown\]



The JSON schema of the format

##### Returns



BetaMessageBatch object{ type: "message_batch", id, archived_at, 7 more }



Create a Message Batch

cURL



```python
curl https://api.anthropic.com/v1/messages/batches \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "requests": [
            {
              "custom_id": "my-custom-id-1",
              "params": {
                "max_tokens": 1024,
                "messages": [
                  {
                    "content": "Hello, world",
                    "role": "user"
                  }
                ],
                "model": "claude-opus-5-5"
              }
            }
          ]
        }'
```

Response 200



```python
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
