---
title: "Create a Message - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/messages/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-23T06:27:23Z"
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

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmessages%2Fcreate)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


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

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)
3.  [Messages](http-beta-messages.md)

# Create a Message

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](../../01-Getting-Started/get-started.md)

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](http-beta.md#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string





"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 43 more

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

max_tokens: number



The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](../Guides/build-with-claude-prompt-caching.md#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](../../20-Models/about-claude-models-overview.md) for details.

minimum0



messages: array of [BetaMessageParam](http-beta-messages.md#beta_message_param) { content, role, clear_at, output_config }

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

See [input examples](../Guides/build-with-claude-working-with-messages.md).

Note that if you want to include a [system prompt](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.



content: string or array of [BetaContentBlockParam](http-beta-messages.md#beta_content_block_param)



One of the following:

string





array of [BetaContentBlockParam](http-beta-messages.md#beta_content_block_param)

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

content: [BetaCodeExecutionToolResultBlockParamContent](http-beta-messages.md#beta_code_execution_tool_result_block_param_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



cache_control: optional [BetaCacheControlEphemeral](http-beta-messages.md#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

cache_control: optional [BetaCacheControlEphemeral](http-beta-messages.md#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

BetaCompactionBlockParam object{ type: "compaction", cache_control, content, 2 more }



A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.



BetaRequestToolAdditionBlock object{ type: "tool_addition", tool, cache_control }



Mid-conversation directive to surface a declared tool.

`tool` references a tool (or MCP toolset) by name from the request's `tools`; it is offered to the model from this point in the conversation onward.



BetaRequestToolRemovalBlock object{ type: "tool_removal", tool, cache_control }



Mid-conversation directive to withdraw a tool.

`tool` references a tool (or MCP toolset) by name from the request's `tools`; it is no longer offered to the model from this point in the conversation onward.



BetaFallbackBlockParam object{ type: "fallback", from, to, trigger }



A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its original position. The block marks the boundary between content produced before and after a fallback hop, and the server relies on that boundary to validate the turn: when thinking runs flank the boundary, omitting the block merges them into one span the server cannot validate (the request is rejected), and moving it into the middle of a single run is likewise rejected; between non-thinking blocks the block's placement has no validation effect.

type: "fallback"





from: [BetaFallbackInfoParam](http-beta-messages.md#beta_fallback_info_param) { model }



Identifies one hop of a fallback transition.



model: [Model](https://platform.claude.com/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



to: [BetaFallbackInfoParam](http-beta-messages.md#beta_fallback_info_param) { model }



Identifies one hop of a fallback transition.



model: [Model](https://platform.claude.com/docs/en/api/http/messages#model)

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

output_config: optional [BetaSystemMessageOutputConfig](http-beta-messages.md#beta_system_message_output_config) { effort } or null



Per-message output configuration on a role:"system" input message.

Fields here apply per-turn; `format` remains top-level only. An empty `{}` is accepted on a message that carries content; a message with neither content nor output_config fields is rejected.



effort: optional "low" or "medium" or "high" or 2 more or null



All possible effort levels.

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

model: [Model](https://platform.claude.com/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



cache_control: optional [BetaCacheControlEphemeral](http-beta-messages.md#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

compaction: optional [BetaCompactionConfig](http-beta-messages.md#beta_compaction_config) { type: "summarize", instructions } or null



Compact the whole conversation and return a signed `compaction` block, alone, that a later request sends back first in `messages`, in place of the messages it summarizes. There is no trigger and no pause flag: sending the parameter compacts, and nothing is sampled after the block.

The summarization prompt is the server's own unless `instructions` are given, which then replace it for this request; a value that is empty or only whitespace counts as absent.

type: "summarize"





instructions: optional string or null



Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent.

maxLength16384



container: optional [BetaContainerParams](http-beta-messages.md#beta_container_params) or string or null

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

skills: optional array of [BetaSkillParams](http-beta-messages.md#beta_skill_params) { type, skill_id, version } or null

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

maxLength64

minLength1



version: optional string



Skill version or 'latest' for most recent version

maxLength64

minLength1

string





context_management: optional [BetaContextManagementConfig](http-beta-messages.md#beta_context_management_config) { edits } or null



Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



diagnostics: optional [BetaDiagnosticsParam](http-beta-messages.md#beta_diagnostics_param) { previous_message_id } or null



Request-level diagnostics. Currently carries the previous response id for prompt-cache divergence reporting.



previous_message_id: optional string or null



The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

maxLength256



fallback_credit_token: optional string or [BetaFallbackCreditTokenParam](http-beta-messages.md#beta_fallback_credit_token_param) or null

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

maxLength2048

minLength1

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

fallbacks: optional [BetaFallbacksParam](http-beta-messages.md#beta_fallbacks_param) or null



Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

One of the following:

inference_geo: optional string or null



Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



mcp_servers: optional array of [BetaRequestMCPServerURLDefinition](http-beta-messages.md#beta_request_mcp_server_url_definition) { type: "url", name, url, 2 more }

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

tool_configuration: optional [BetaRequestMCPServerToolConfiguration](http-beta-messages.md#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled } or null



allowed_tools: optional array of string or null



enabled: optional boolean or null





metadata: optional [BetaMetadata](http-beta-messages.md#beta_metadata) { user_id }



An object describing metadata about the request.



user_id: optional string or null



An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



output_config: optional [BetaOutputConfig](http-beta-messages.md#beta_output_config) { effort, format, task_budget }

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

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

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

Whether to incrementally stream the response using server-sent events.

See [streaming](../Guides/build-with-claude-streaming.md) for details.



system: optional string or array of [BetaTextBlockParam](http-beta-messages.md#beta_text_block_param)



System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#give-claude-a-role).

One of the following:

string





array of [BetaTextBlockParam](http-beta-messages.md#beta_text_block_param) { type: "text", text, cache_control, citations }



type: "text"





text: string



minLength1



cache_control: optional [BetaCacheControlEphemeral](http-beta-messages.md#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

citations: optional array of [BetaTextCitationParam](http-beta-messages.md#beta_text_citation_param) or null

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

maxLength500

minLength1

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

maxLength500

minLength1

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

maxLength500

minLength1

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

maxLength512

minLength1

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

thinking: optional [BetaThinkingConfigParam](http-beta-messages.md#beta_thinking_config_param)



Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](../Guides/build-with-claude-extended-thinking.md) for details.

One of the following:



tool_choice: optional [BetaToolChoice](http-beta-messages.md#beta_tool_choice)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



tools: optional array of [BetaToolUnion](http-beta-messages.md#beta_tool_union)

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

BetaMCPToolset object{ type: "mcp_toolset", mcp_server_name, cache_control, 2 more }



Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.



output_format: optional [BetaJSONOutputFormat](http-beta-messages.md#beta_json_output_format) { type: "json_schema", schema } or null⁠Deprecated



Deprecated: Use `output_config.format` instead. See [structured outputs](../Guides/build-with-claude-structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

type: "json_schema"



schema: map\[unknown\]



The JSON schema of the format



temperature: optional number⁠Deprecated



Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0



top_k: optional number⁠Deprecated



Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0



top_p: optional number⁠Deprecated



Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value \>= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

##### Returns



BetaMessage object{ type: "message", id, container, 10 more }





BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](http-beta-messages.md#beta_raw_message_start_event) or [BetaRawMessageDeltaEvent](http-beta-messages.md#beta_raw_message_delta_event) or [BetaRawMessageStopEvent](http-beta-messages.md#beta_raw_message_stop_event) or 3 more



One of the following:

Create a Message

cURL



```python
curl https://api.anthropic.com/v1/messages \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    --max-time 600 \
    -d '{
          "max_tokens": 1024,
          "messages": [
            {
              "content": "Hello, world",
              "role": "user"
            }
          ],
          "model": "claude-opus-5",
          "stream": false,
          "system": [
            {
              "text": "Today'\''s date is 2024-06-01.",
              "type": "text"
            }
          ],
          "temperature": 1,
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
          ],
          "top_k": 5,
          "top_p": 0.7
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
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
    "fallback_credit_token": "QW50aHJvcGljL0NsYXVkZQ==",
    "fallback_has_prefill_claim": true,
    "recommended_model": "claude-opus-4-8",
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
    "fallback_credit": {
      "status": {
        "type": "redeemed"
      }
    },
    "inference_geo": "global",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "model": "claude-fable-5-1",
        "output_tokens": 0,
        "type": "message"
      }
    ],
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
  },
  "input_transformations": [
    {
      "path": "path",
      "reason": "model_binding_mismatch",
      "type": "thinking_dropped"
    }
  ]
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
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
    "fallback_credit_token": "QW50aHJvcGljL0NsYXVkZQ==",
    "fallback_has_prefill_claim": true,
    "recommended_model": "claude-opus-4-8",
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
    "fallback_credit": {
      "status": {
        "type": "redeemed"
      }
    },
    "inference_geo": "global",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "model": "claude-fable-5-1",
        "output_tokens": 0,
        "type": "message"
      }
    ],
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
  },
  "input_transformations": [
    {
      "path": "path",
      "reason": "model_binding_mismatch",
