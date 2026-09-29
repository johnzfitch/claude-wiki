---
title: "Count tokens in a Message - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/messages/count_tokens"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:18Z"
tags: ["api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Fmessages%2Fcount_tokens)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)
3.  [Messages](/docs/en/api/http/beta/messages)

# Count tokens in a Message

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/http/beta#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string





"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more



One of the following:

"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"

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

"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"

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

"cache-diagnosis-2026-04-07"

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

"ce-user-management-2026-07-13"

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

"anthropic-user-profile-id": optional string



The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Body



messages: array of [BetaMessageParam](/docs/en/api/http/beta/messages#beta_message_param) { content, role, clear_at, output_config }



Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

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

Example with a partially-filled response from Claude:

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

See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.



content: string or array of [BetaContentBlockParam](/docs/en/api/http/beta/messages#beta_content_block_param)



One of the following:

string





array of [BetaContentBlockParam](/docs/en/api/http/beta/messages#beta_content_block_param)



One of the following:



BetaTextBlockParam object{ type: "text", text, cache_control, citations }





BetaImageBlockParam object{ type: "image", source, cache_control, transformations }





BetaRequestDocumentBlock object{ type: "document", source, cache_control, 3 more }





BetaSearchResultBlockParam object{ type: "search_result", content, source, 3 more }





BetaThinkingBlockParam object{ type: "thinking", signature, thinking }



type: "thinking"





signature: string



The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

thinking: string



The `thinking` text of this block as returned by the API.



BetaRedactedThinkingBlockParam object{ type: "redacted_thinking", data }



type: "redacted_thinking"



data: string



The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.



BetaToolUseBlockParam object{ type: "tool_use", id, input, 4 more }





BetaToolResultBlockParam object{ type: "tool_result", tool_use_id, cache_control, 3 more }





BetaServerToolUseBlockParam object{ type: "server_tool_use", id, input, 3 more }





BetaWebSearchToolResultBlockParam object{ type: "web_search_tool_result", content, tool_use_id, 2 more }





BetaWebFetchToolResultBlockParam object{ type: "web_fetch_tool_result", content, tool_use_id, 2 more }





BetaAdvisorToolResultBlockParam object{ type: "advisor_tool_result", content, tool_use_id, cache_control }





BetaCodeExecutionToolResultBlockParam object{ type: "code_execution_tool_result", content, tool_use_id, cache_control }



type: "code_execution_tool_result"





content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/http/beta/messages#beta_code_execution_tool_result_block_param_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/http/beta/messages#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



"1h"





BetaBashCodeExecutionToolResultBlockParam object{ type: "bash_code_execution_tool_result", content, tool_use_id, cache_control }





BetaTextEditorCodeExecutionToolResultBlockParam object{ type: "text_editor_code_execution_tool_result", content, tool_use_id, cache_control }





BetaToolSearchToolResultBlockParam object{ type: "tool_search_tool_result", content, tool_use_id, cache_control }





BetaMCPToolUseBlockParam object{ type: "mcp_tool_use", id, input, 3 more }





BetaRequestMCPToolResultBlockParam object{ type: "mcp_tool_result", tool_use_id, cache_control, 2 more }





BetaContainerUploadBlockParam object{ type: "container_upload", file_id, cache_control }



A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

type: "container_upload"



file_id: string





cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/http/beta/messages#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



"1h"





BetaCompactionBlockParam object{ type: "compaction", cache_control, content, 3 more }



A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.



BetaRequestToolAdditionBlock object{ type: "tool_addition", tool, cache_control }



Mid-conversation directive to make a tool available.

`tool` is a reference to a tool (or MCP toolset) declared in the request's `tools`. Under the `inline-tools-2026-09-15` beta it may instead be a reference to a tool defined earlier in `messages`, or a `tool_definition` object that carries an inline tool definition in `definition` (the same object a `tools` entry holds). An `mcp_toolset` definition also requires the `mcp-client-2026-09-15` beta. The tool is offered to the model from this point in the conversation onward.



BetaRequestToolRemovalBlock object{ type: "tool_removal", tool, cache_control }



Mid-conversation directive to withdraw a tool.

`tool` references a tool (or MCP toolset) by name: one declared in the request's `tools` or defined earlier in `messages`. It is no longer offered to the model from this point in the conversation onward.



BetaMCPToolListingBlockParam object{ type: "mcp_tool_listing", mcp_server_name, tools }



The tool listing an MCP server returned while an earlier response was produced, as that response carried it. Send the assistant message back unchanged, this block included, and the server uses this listing for the matching `mcp_toolset` instead of asking the MCP server again.

type: "mcp_tool_listing"





mcp_server_name: string



The name of the MCP server this listing came from, as `mcp_servers` declares it.

minLength1

maxLength255



tools: array of [BetaMCPToolParam](/docs/en/api/http/beta/messages#beta_mcp_tool_param) { input_schema, name, description }



The server's tools, exactly as the response listed them.

input_schema: map\[unknown\]



The tool's input schema as the MCP server lists it, verbatim.



name: string



The tool's name as the MCP server lists it (not prefixed with the server name).

minLength1

description: optional string or null



The tool's description as the MCP server lists it.



BetaFallbackBlockParam object{ type: "fallback", from, to, trigger }



A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its original position. The block marks the boundary between content produced before and after a fallback hop, and the server relies on that boundary to validate the turn: when thinking runs flank the boundary, omitting the block merges them into one span the server cannot validate (the request is rejected), and moving it into the middle of a single run is likewise rejected; between non-thinking blocks the block's placement has no validation effect.

type: "fallback"





from: [BetaFallbackInfoParam](/docs/en/api/http/beta/messages#beta_fallback_info_param) { model }



Identifies one hop of a fallback transition.



model: [Model](/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



to: [BetaFallbackInfoParam](/docs/en/api/http/beta/messages#beta_fallback_info_param) { model }



Identifies one hop of a fallback transition.



model: [Model](/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

trigger: optional unknown



The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



role: "user" or "assistant" or "system"



One of the following:

"user"



"assistant"



"system"





clear_at: optional "next_user_message" or "never" or null



How long this system message's text stays in front of the model. `"never"` (the default) renders it on every request that includes it. `"next_user_message"` renders it only for the user turn it follows: once a later `role: "user"` message exists in `messages` the message stays in the array (send it unchanged) but is no longer shown to the model. Only permitted on `role: "system"` messages.

One of the following:

"next_user_message"



"never"





output_config: optional [BetaSystemMessageOutputConfig](/docs/en/api/http/beta/messages#beta_system_message_output_config) { effort } or null



Per-message output configuration on a role:"system" input message.

Fields here apply per-turn; `format` remains top-level only. An empty `{}` is accepted on a message that carries content; a message with neither content nor output_config fields is rejected.

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

model: [Model](/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/http/beta/messages#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



"1h"





compaction: optional [BetaCompactionConfig](/docs/en/api/http/beta/messages#beta_compaction_config) { type: "summarize", instructions } or null

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

context_management: optional [BetaContextManagementConfig](/docs/en/api/http/beta/messages#beta_context_management_config) { edits } or null



Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



mcp_servers: optional array of [BetaRequestMCPServerURLDefinition](/docs/en/api/http/beta/messages#beta_request_mcp_server_url_definition) { type: "url", name, url, 2 more }

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

tool_configuration: optional [BetaRequestMCPServerToolConfiguration](/docs/en/api/http/beta/messages#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled } or null



allowed_tools: optional array of string or null



enabled: optional boolean or null





output_config: optional [BetaOutputConfig](/docs/en/api/http/beta/messages#beta_output_config) { effort, format, task_budget }



Configuration options for the model's output, such as the output format.



speed: optional "standard" or "fast" or null



The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

One of the following:

"standard"



"fast"





system: optional string or array of [BetaTextBlockParam](/docs/en/api/http/beta/messages#beta_text_block_param)



System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

One of the following:

string





array of [BetaTextBlockParam](/docs/en/api/http/beta/messages#beta_text_block_param) { type: "text", text, cache_control, citations }



type: "text"





text: string



minLength1



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/http/beta/messages#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



"1h"





citations: optional array of [BetaTextCitationParam](/docs/en/api/http/beta/messages#beta_text_citation_param) or null

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

thinking: optional [BetaThinkingConfigParam](/docs/en/api/http/beta/messages#beta_thinking_config_param)



Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

One of the following:



tool_choice: optional [BetaToolChoice](/docs/en/api/http/beta/messages#beta_tool_choice)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



tools: optional array of [BetaTool](/docs/en/api/http/beta/messages#beta_tool) or [BetaToolBash20241022](/docs/en/api/http/beta/messages#beta_tool_bash_20241022) or [BetaToolBash20250124](/docs/en/api/http/beta/messages#beta_tool_bash_20250124) or 25 more



Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)).

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

See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for more details.

One of the following:



BetaTool object{ type, input_schema, name, 7 more }





BetaToolBash20241022 object{ type: "bash_20241022", name, allowed_callers, 4 more }

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

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

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





BetaMemoryTool20250818 object{ type: "memory_20250818", name, allowed_callers, 4 more }





BetaToolComputerUse20250124 object{ type: "computer_20250124", display_height_px, display_width_px, 7 more }





BetaToolTextEditor20241022 object{ type: "text_editor_20241022", name, allowed_callers, 4 more }





BetaToolComputerUse20251124 object{ type: "computer_20251124", display_height_px, display_width_px, 8 more }

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





BetaToolSearchToolBm25_20251119 object{ type, name, allowed_callers, 3 more }





BetaToolSearchToolRegex20251119 object{ type, name, allowed_callers, 3 more }





BetaMCPToolset object{ type: "mcp_toolset", mcp_server_name, cache_control, 3 more }



Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.



output_format: optional [BetaJSONOutputFormat](/docs/en/api/http/beta/messages#beta_json_output_format) { type: "json_schema", schema } or null⁠Deprecated



Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

type: "json_schema"



schema: map\[unknown\]



The JSON schema of the format

##### Returns



BetaMessageTokensCount object{ context_management, input_tokens }





context_management: [BetaCountTokensContextManagementResponse](/docs/en/api/http/beta/messages#beta_count_tokens_context_management_response) { original_input_tokens } or null



Information about context management applied to the message.

original_input_tokens: number



The original token count before context management was applied

input_tokens: number



The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

cURL



```python
curl https://api.anthropic.com/v1/messages/count_tokens \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "messages": [
            {
              "content": "Hello, world",
              "role": "user"
            }
          ],
          "model": "claude-opus-5",
          "system": [
            {
              "text": "Today'\''s date is 2024-06-01.",
