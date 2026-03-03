---
category: "04-API-Reference"
fetched_at: "2026-03-03T14:57:19Z"
source_url: "https://platform.claude.com/docs/en/api/beta"
title: "Beta - Claude API Reference"
---

# Beta

##### ModelsExpand Collapse 

AnthropicBeta = string or "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 17 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 17 more

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

BetaAPIError = object { message, type }

message: string

type: "api_error"

BetaAuthenticationError = object { message, type }

message: string

type: "authentication_error"

BetaBillingError = object { message, type }

message: string

type: "billing_error"

BetaError = [BetaInvalidRequestError](/docs/en/api/beta#beta_invalid_request_error) { message, type } or [BetaAuthenticationError](/docs/en/api/beta#beta_authentication_error) { message, type } or [BetaBillingError](/docs/en/api/beta#beta_billing_error) { message, type } or 6 more

Accepts one of the following:

BetaInvalidRequestError = object { message, type }

message: string

type: "invalid_request_error"

BetaAuthenticationError = object { message, type }

message: string

type: "authentication_error"

BetaBillingError = object { message, type }

message: string

type: "billing_error"

BetaPermissionError = object { message, type }

message: string

type: "permission_error"

BetaNotFoundError = object { message, type }

message: string

type: "not_found_error"

BetaRateLimitError = object { message, type }

message: string

type: "rate_limit_error"

BetaGatewayTimeoutError = object { message, type }

message: string

type: "timeout_error"

BetaAPIError = object { message, type }

message: string

type: "api_error"

BetaOverloadedError = object { message, type }

message: string

type: "overloaded_error"

BetaErrorResponse = object { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError = object { message, type }

message: string

type: "invalid_request_error"

BetaAuthenticationError = object { message, type }

message: string

type: "authentication_error"

BetaBillingError = object { message, type }

message: string

type: "billing_error"

BetaPermissionError = object { message, type }

message: string

type: "permission_error"

BetaNotFoundError = object { message, type }

message: string

type: "not_found_error"

BetaRateLimitError = object { message, type }

message: string

type: "rate_limit_error"

BetaGatewayTimeoutError = object { message, type }

message: string

type: "timeout_error"

BetaAPIError = object { message, type }

message: string

type: "api_error"

BetaOverloadedError = object { message, type }

message: string

type: "overloaded_error"

request_id: string

type: "error"

BetaGatewayTimeoutError = object { message, type }

message: string

type: "timeout_error"

BetaInvalidRequestError = object { message, type }

message: string

type: "invalid_request_error"

BetaNotFoundError = object { message, type }

message: string

type: "not_found_error"

BetaOverloadedError = object { message, type }

message: string

type: "overloaded_error"

BetaPermissionError = object { message, type }

message: string

type: "permission_error"

BetaRateLimitError = object { message, type }

message: string

type: "rate_limit_error"

#### BetaModels

##### [List Models](/docs/en/api/beta/models/list)

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

BetaModelInfo = object { id, created_at, display_name, type }

id: string

Unique model identifier.

created_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.

#### BetaMessages

##### [Create a Message](/docs/en/api/beta/messages/create)

POST/v1/messages

##### [Count tokens in a Message](/docs/en/api/beta/messages/count_tokens)

POST/v1/messages/count_tokens

##### ModelsExpand Collapse 

BetaAllThinkingTurns = object { type }

type: "all"

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaBashCodeExecutionOutputBlock = object { file_id, type }

file_id: string

type: "bash_code_execution_output"

BetaBashCodeExecutionOutputBlockParam = object { file_id, type }

file_id: string

type: "bash_code_execution_output"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

BetaBashCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaBashCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type } or [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaCacheControlEphemeral = object { type, ttl }

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCacheCreation = object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationConfig = object { enabled }

enabled: boolean

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationsConfigParam = object { enabled }

enabled: optional boolean

BetaCitationsDelta = object { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } or 2 more

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

type: "citations_delta"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaClearThinking20251015Edit = object { type, keep }

type: "clear_thinking_20251015"

keep: optional [BetaThinkingTurns](/docs/en/api/beta#beta_thinking_turns) { type, value } or [BetaAllThinkingTurns](/docs/en/api/beta#beta_all_thinking_turns) { type } or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

BetaThinkingTurns = object { type, value }

type: "thinking_turns"

value: number

BetaAllThinkingTurns = object { type }

type: "all"

UnionMember2 = "all"

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

BetaClearToolUses20250919Edit = object { type, clear_at_least, clear_tool_inputs, 3 more }

type: "clear_tool_uses_20250919"

clear_at_least: optional [BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input_tokens"

value: number

clear_tool_inputs: optional boolean or array of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

UnionMember0 = boolean

UnionMember1 = array of string

exclude_tools: optional array of string

Tool names whose uses are preserved from clearing

keep: optional [BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: "tool_uses"

value: number

trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value } or [BetaToolUsesTrigger](/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

BetaInputTokensTrigger = object { type, value }

type: "input_tokens"

value: number

BetaToolUsesTrigger = object { type, value }

type: "tool_uses"

value: number

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaCodeExecutionOutputBlock = object { file_id, type }

file_id: string

type: "code_execution_output"

BetaCodeExecutionOutputBlockParam = object { file_id, type }

file_id: string

type: "code_execution_output"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaCodeExecutionTool20250522 = object { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250522"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250825 = object { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250825"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20260120 = object { name, type, allowed_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20260120"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultError](/docs/en/api/beta#beta_code_execution_tool_result_error) { error_code, type } or [BetaCodeExecutionResultBlock](/docs/en/api/beta#beta_code_execution_result_block) { content, return_code, stderr, 2 more } or [BetaEncryptedCodeExecutionResultBlock](/docs/en/api/beta#beta_encrypted_code_execution_result_block) { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

BetaCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlockParam = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_code_execution_tool_result_error_param) { error_code, type } or [BetaCodeExecutionResultBlockParam](/docs/en/api/beta#beta_code_execution_result_block_param) { content, return_code, stderr, 2 more } or [BetaEncryptedCodeExecutionResultBlockParam](/docs/en/api/beta#beta_encrypted_code_execution_result_block_param) { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlockParam = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionToolResultErrorCode = "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

BetaCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCompact20260112Edit = object { type, instructions, pause_after_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact_20260112"

instructions: optional string

Additional instructions for summarization.

pause_after_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.

trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: "input_tokens"

value: number

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

BetaCompactionBlockParam = object { content, type, cache_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionContentBlockDelta = object { content, type }

content: string

type: "compaction_delta"

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

BetaContainer = object { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

BetaContainerParams = object { id, skills }

Container parameters with skills to be loaded.

id: optional string

Container id

skills: optional array of [BetaSkillParams](/docs/en/api/beta#beta_skill_params) { skill_id, type, version }

List of skills to load in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaContainerUploadBlockParam = object { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContentBlock = [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } or [BetaThinkingBlock](/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } or [BetaRedactedThinkingBlock](/docs/en/api/beta#beta_redacted_thinking_block) { data, type } or 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

BetaContentBlockParam = [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more } or 16 more

Regular text content.

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestDocumentBlock = object { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaSearchResultBlockParam = object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaThinkingBlockParam = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlockParam = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or 2 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or 2 more

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam = object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaRequestDocumentBlock = object { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaToolReferenceBlockParam = object { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error: optional boolean

BetaServerToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlockParam = object { content, tool_use_id, type, 2 more }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age: optional string

BetaWebSearchToolRequestError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

tool_use_id: string

type: "web_search_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlockParam = object { content, tool_use_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type } or [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlockParam = object { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web_fetch_result"

url: string

Fetched content URL

retrieved_at: optional string

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlockParam = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type } or [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } or [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam = object { error_code, type, error_message }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

error_message: optional string

BetaTextEditorCodeExecutionViewResultBlockParam = object { content, file_type, type, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

num_lines: optional number

start_line: optional number

total_lines: optional number

BetaTextEditorCodeExecutionCreateResultBlockParam = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

lines: optional array of string

new_lines: optional number

new_start: optional number

old_lines: optional number

old_start: optional number

tool_use_id: string

type: "text_editor_code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type } or [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlockParam = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control }

tool_name: string

type: "tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: string

server_name: string

The name of the MCP server

type: "mcp_tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestMCPToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "mcp_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

is_error: optional boolean

BetaContainerUploadBlockParam = object { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionBlockParam = object { content, type, cache_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaContentBlockSourceContent = [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control }

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContextManagementConfig = object { edits }

edits: optional array of [BetaClearToolUses20250919Edit](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit) { type, clear_at_least, clear_tool_inputs, 3 more } or [BetaClearThinking20251015Edit](/docs/en/api/beta#beta_clear_thinking_20251015_edit) { type, keep } or [BetaCompact20260112Edit](/docs/en/api/beta#beta_compact_20260112_edit) { type, instructions, pause_after_compaction, trigger }

List of context management edits to apply

Accepts one of the following:

BetaClearToolUses20250919Edit = object { type, clear_at_least, clear_tool_inputs, 3 more }

type: "clear_tool_uses_20250919"

clear_at_least: optional [BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input_tokens"

value: number

clear_tool_inputs: optional boolean or array of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

UnionMember0 = boolean

UnionMember1 = array of string

exclude_tools: optional array of string

Tool names whose uses are preserved from clearing

keep: optional [BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: "tool_uses"

value: number

trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value } or [BetaToolUsesTrigger](/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

BetaInputTokensTrigger = object { type, value }

type: "input_tokens"

value: number

BetaToolUsesTrigger = object { type, value }

type: "tool_uses"

value: number

BetaClearThinking20251015Edit = object { type, keep }

type: "clear_thinking_20251015"

keep: optional [BetaThinkingTurns](/docs/en/api/beta#beta_thinking_turns) { type, value } or [BetaAllThinkingTurns](/docs/en/api/beta#beta_all_thinking_turns) { type } or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

BetaThinkingTurns = object { type, value }

type: "thinking_turns"

value: number

BetaAllThinkingTurns = object { type }

type: "all"

UnionMember2 = "all"

BetaCompact20260112Edit = object { type, instructions, pause_after_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact_20260112"

instructions: optional string

Additional instructions for summarization.

pause_after_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.

trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: "input_tokens"

value: number

BetaContextManagementResponse = object { applied_edits }

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

BetaCountTokensContextManagementResponse = object { original_input_tokens }

original_input_tokens: number

The original token count before context management was applied

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaDocumentBlock = object { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

BetaEncryptedCodeExecutionResultBlockParam = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaInputJSONDelta = object { partial_json, type }

partial_json: string

type: "input_json_delta"

BetaInputTokensClearAtLeast = object { type, value }

type: "input_tokens"

value: number

BetaInputTokensTrigger = object { type, value }

type: "input_tokens"

value: number

BetaIterationsUsage = array of [BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } or [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

BetaJSONOutputFormat = object { schema, type }

schema: map\[unknown\]

The JSON schema of the format

type: "json_schema"

BetaMCPToolConfig = object { defer_loading, enabled }

Configuration for a specific tool in an MCP toolset.

defer_loading: optional boolean

enabled: optional boolean

BetaMCPToolDefaultConfig = object { defer_loading, enabled }

Default configuration for tools in an MCP toolset.

defer_loading: optional boolean

enabled: optional boolean

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: string

server_name: string

The name of the MCP server

type: "mcp_tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolset = object { mcp_server_name, type, cache_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: string

Name of the MCP server to configure tools for

type: "mcp_toolset"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs: optional map\[[BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config) { defer_loading, enabled } \]

Configuration overrides for specific tools, keyed by tool name

defer_loading: optional boolean

enabled: optional boolean

default_config: optional [BetaMCPToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) { defer_loading, enabled }

Default configuration applied to all tools from this server

defer_loading: optional boolean

enabled: optional boolean

BetaMemoryTool20250818 = object { name, type, allowed_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory_20250818"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818Command = [BetaMemoryTool20250818ViewCommand](/docs/en/api/beta#beta_memory_tool_20250818_view_command) { command, path, view_range } or [BetaMemoryTool20250818CreateCommand](/docs/en/api/beta#beta_memory_tool_20250818_create_command) { command, file_text, path } or [BetaMemoryTool20250818StrReplaceCommand](/docs/en/api/beta#beta_memory_tool_20250818_str_replace_command) { command, new_str, old_str, path } or 3 more

Accepts one of the following:

BetaMemoryTool20250818ViewCommand = object { command, path, view_range }

command: "view"

Command type identifier

path: string

Path to directory or file to view

view_range: optional array of number

Optional line range for viewing specific lines

BetaMemoryTool20250818CreateCommand = object { command, file_text, path }

command: "create"

Command type identifier

file_text: string

Content to write to the file

path: string

Path where the file should be created

BetaMemoryTool20250818StrReplaceCommand = object { command, new_str, old_str, path }

command: "str_replace"

Command type identifier

new_str: string

Text to replace with

old_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced

BetaMemoryTool20250818InsertCommand = object { command, insert_line, insert_text, path }

command: "insert"

Command type identifier

insert_line: number

Line number where text should be inserted

insert_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted

BetaMemoryTool20250818DeleteCommand = object { command, path }

command: "delete"

Command type identifier

path: string

Path to the file or directory to delete

BetaMemoryTool20250818RenameCommand = object { command, new_path, old_path }

command: "rename"

Command type identifier

new_path: string

New path for the file or directory

old_path: string

Current path of the file or directory

BetaMemoryTool20250818CreateCommand = object { command, file_text, path }

command: "create"

Command type identifier

file_text: string

Content to write to the file

path: string

Path where the file should be created

BetaMemoryTool20250818DeleteCommand = object { command, path }

command: "delete"

Command type identifier

path: string

Path to the file or directory to delete

BetaMemoryTool20250818InsertCommand = object { command, insert_line, insert_text, path }

command: "insert"

Command type identifier

insert_line: number

Line number where text should be inserted

insert_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted

BetaMemoryTool20250818RenameCommand = object { command, new_path, old_path }

command: "rename"

Command type identifier

new_path: string

New path for the file or directory

old_path: string

Current path of the file or directory

BetaMemoryTool20250818StrReplaceCommand = object { command, new_str, old_str, path }

command: "str_replace"

Command type identifier

new_str: string

Text to replace with

old_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced

BetaMemoryTool20250818ViewCommand = object { command, path, view_range }

command: "view"

Command type identifier

path: string

Path to directory or file to view

view_range: optional array of number

Optional line range for viewing specific lines

BetaMessage = object { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-opus-4-5-20251101" or 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

inference_geo: string

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

BetaMessageDeltaUsage = object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }

cache_creation_input_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The cumulative number of input tokens read from the cache.

input_tokens: number

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaMessageParam = object { content, role }

content: string or array of [BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestDocumentBlock = object { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaSearchResultBlockParam = object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaThinkingBlockParam = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlockParam = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or 2 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or 2 more

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam = object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaRequestDocumentBlock = object { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaToolReferenceBlockParam = object { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error: optional boolean

BetaServerToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlockParam = object { content, tool_use_id, type, 2 more }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age: optional string

BetaWebSearchToolRequestError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

tool_use_id: string

type: "web_search_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlockParam = object { content, tool_use_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type } or [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlockParam = object { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web_fetch_result"

url: string

Fetched content URL

retrieved_at: optional string

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlockParam = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type } or [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } or [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam = object { error_code, type, error_message }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

error_message: optional string

BetaTextEditorCodeExecutionViewResultBlockParam = object { content, file_type, type, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

num_lines: optional number

start_line: optional number

total_lines: optional number

BetaTextEditorCodeExecutionCreateResultBlockParam = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

lines: optional array of string

new_lines: optional number

new_start: optional number

old_lines: optional number

old_start: optional number

tool_use_id: string

type: "text_editor_code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type } or [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlockParam = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control }

tool_name: string

type: "tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: string

server_name: string

The name of the MCP server

type: "mcp_tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestMCPToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "mcp_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

is_error: optional boolean

BetaContainerUploadBlockParam = object { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionBlockParam = object { content, type, cache_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

role: "user" or "assistant"

Accepts one of the following:

"user"

"assistant"

BetaMessageTokensCount = object { context_management, input_tokens }

context_management: [BetaCountTokensContextManagementResponse](/docs/en/api/beta#beta_count_tokens_context_management_response) { original_input_tokens }

Information about context management applied to the message.

original_input_tokens: number

The original token count before context management was applied

input_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

BetaMetadata = object { user_id }

user_id: optional string

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

BetaOutputConfig = object { effort, format }

effort: optional "low" or "medium" or "high" or "max"

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format: optional [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: map\[unknown\]

The JSON schema of the format

type: "json_schema"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaRawContentBlockDelta = [BetaTextDelta](/docs/en/api/beta#beta_text_delta) { text, type } or [BetaInputJSONDelta](/docs/en/api/beta#beta_input_json_delta) { partial_json, type } or [BetaCitationsDelta](/docs/en/api/beta#beta_citations_delta) { citation, type } or 3 more

Accepts one of the following:

BetaTextDelta = object { text, type }

text: string

type: "text_delta"

BetaInputJSONDelta = object { partial_json, type }

partial_json: string

type: "input_json_delta"

BetaCitationsDelta = object { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } or 2 more

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

type: "citations_delta"

BetaThinkingDelta = object { thinking, type }

thinking: string

type: "thinking_delta"

BetaSignatureDelta = object { signature, type }

signature: string

type: "signature_delta"

BetaCompactionContentBlockDelta = object { content, type }

content: string

type: "compaction_delta"

BetaRawContentBlockDeltaEvent = object { delta, index, type }

delta: [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

BetaTextDelta = object { text, type }

text: string

type: "text_delta"

BetaInputJSONDelta = object { partial_json, type }

partial_json: string

type: "input_json_delta"

BetaCitationsDelta = object { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } or 2 more

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

type: "citations_delta"

BetaThinkingDelta = object { thinking, type }

thinking: string

type: "thinking_delta"

BetaSignatureDelta = object { signature, type }

signature: string

type: "signature_delta"

BetaCompactionContentBlockDelta = object { content, type }

content: string

type: "compaction_delta"

index: number

type: "content_block_delta"

BetaRawContentBlockStartEvent = object { content_block, index, type }

content_block: [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } or [BetaThinkingBlock](/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } or [BetaRedactedThinkingBlock](/docs/en/api/beta#beta_redacted_thinking_block) { data, type } or 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

index: number

type: "content_block_start"

BetaRawContentBlockStopEvent = object { index, type }

index: number

type: "content_block_stop"

BetaRawMessageDeltaEvent = object { context_management, delta, type, usage }

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Information about context management strategies applied during the request

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

delta: object { container, stop_reason, stop_sequence }

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string

type: "message_delta"

usage: [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The cumulative number of input tokens read from the cache.

input_tokens: number

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

BetaRawMessageStartEvent = object { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-opus-4-5-20251101" or 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

inference_geo: string

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "message_start"

BetaRawMessageStopEvent = object { type }

type: "message_stop"

BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](/docs/en/api/beta#beta_raw_message_start_event) { message, type } or [BetaRawMessageDeltaEvent](/docs/en/api/beta#beta_raw_message_delta_event) { context_management, delta, type, usage } or [BetaRawMessageStopEvent](/docs/en/api/beta#beta_raw_message_stop_event) { type } or 3 more

Accepts one of the following:

BetaRawMessageStartEvent = object { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-opus-4-5-20251101" or 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

inference_geo: string

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "message_start"

BetaRawMessageDeltaEvent = object { context_management, delta, type, usage }

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Information about context management strategies applied during the request

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

delta: object { container, stop_reason, stop_sequence }

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string

type: "message_delta"

usage: [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The cumulative number of input tokens read from the cache.

input_tokens: number

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

BetaRawMessageStopEvent = object { type }

type: "message_stop"

BetaRawContentBlockStartEvent = object { content_block, index, type }

content_block: [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } or [BetaThinkingBlock](/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } or [BetaRedactedThinkingBlock](/docs/en/api/beta#beta_redacted_thinking_block) { data, type } or 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

index: number

type: "content_block_start"

BetaRawContentBlockDeltaEvent = object { delta, index, type }

delta: [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

BetaTextDelta = object { text, type }

text: string

type: "text_delta"

BetaInputJSONDelta = object { partial_json, type }

partial_json: string

type: "input_json_delta"

BetaCitationsDelta = object { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } or 2 more

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

type: "citations_delta"

BetaThinkingDelta = object { thinking, type }

thinking: string

type: "thinking_delta"

BetaSignatureDelta = object { signature, type }

signature: string

type: "signature_delta"

BetaCompactionContentBlockDelta = object { content, type }

content: string

type: "compaction_delta"

index: number

type: "content_block_delta"

BetaRawContentBlockStopEvent = object { index, type }

index: number

type: "content_block_stop"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaRedactedThinkingBlockParam = object { data, type }

data: string

type: "redacted_thinking"

BetaRequestDocumentBlock = object { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaRequestMCPServerToolConfiguration = object { allowed_tools, enabled }

allowed_tools: optional array of string

enabled: optional boolean

BetaRequestMCPServerURLDefinition = object { name, type, url, 2 more }

name: string

type: "url"

url: string

authorization_token: optional string

tool_configuration: optional [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled }

allowed_tools: optional array of string

enabled: optional boolean

BetaRequestMCPToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "mcp_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

is_error: optional boolean

BetaSearchResultBlockParam = object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUsage = object { web_fetch_requests, web_search_requests }

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaSignatureDelta = object { signature, type }

signature: string

type: "signature_delta"

BetaSkill = object { skill_id, type, version }

A skill that was loaded in a container (response model).

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

BetaSkillParams = object { skill_id, type, version }

Specification for a skill to be loaded in a container (request model).

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version

BetaStopReason = "end_turn" or "max_tokens" or "stop_sequence" or 5 more

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaTextCitation = [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } or [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } or 2 more

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaTextCitationParam = [BetaCitationCharLocationParam](/docs/en/api/beta#beta_citation_char_location_param) { cited_text, document_index, document_title, 3 more } or [BetaCitationPageLocationParam](/docs/en/api/beta#beta_citation_page_location_param) { cited_text, document_index, document_title, 3 more } or [BetaCitationContentBlockLocationParam](/docs/en/api/beta#beta_citation_content_block_location_param) { cited_text, document_index, document_title, 3 more } or 2 more

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaTextDelta = object { text, type }

text: string

type: "text_delta"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionCreateResultBlockParam = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

lines: optional array of string

new_lines: optional number

new_start: optional number

old_lines: optional number

old_start: optional number

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } or [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam = object { error_code, type, error_message }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

error_message: optional string

BetaTextEditorCodeExecutionViewResultBlockParam = object { content, file_type, type, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

num_lines: optional number

start_line: optional number

total_lines: optional number

BetaTextEditorCodeExecutionCreateResultBlockParam = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

lines: optional array of string

new_lines: optional number

new_start: optional number

old_lines: optional number

old_start: optional number

tool_use_id: string

type: "text_editor_code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionToolResultErrorParam = object { error_code, type, error_message }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

error_message: optional string

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionViewResultBlockParam = object { content, file_type, type, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

num_lines: optional number

start_line: optional number

total_lines: optional number

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaThinkingBlockParam = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaThinkingConfigAdaptive = object { type }

type: "adaptive"

BetaThinkingConfigDisabled = object { type }

type: "disabled"

BetaThinkingConfigEnabled = object { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

BetaThinkingConfigParam = [BetaThinkingConfigEnabled](/docs/en/api/beta#beta_thinking_config_enabled) { budget_tokens, type } or [BetaThinkingConfigDisabled](/docs/en/api/beta#beta_thinking_config_disabled) { type } or [BetaThinkingConfigAdaptive](/docs/en/api/beta#beta_thinking_config_adaptive) { type }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

BetaThinkingConfigEnabled = object { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

BetaThinkingConfigDisabled = object { type }

type: "disabled"

BetaThinkingConfigAdaptive = object { type }

type: "adaptive"

BetaThinkingDelta = object { thinking, type }

thinking: string

type: "thinking_delta"

BetaThinkingTurns = object { type, value }

type: "thinking_turns"

value: number

BetaTool = object { input_schema, name, allowed_callers, 7 more }

input_schema: object { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map\[unknown\]

required: optional array of string

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

BetaToolBash20241022 = object { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolBash20250124 = object { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolChoice = [BetaToolChoiceAuto](/docs/en/api/beta#beta_tool_choice_auto) { type, disable_parallel_tool_use } or [BetaToolChoiceAny](/docs/en/api/beta#beta_tool_choice_any) { type, disable_parallel_tool_use } or [BetaToolChoiceTool](/docs/en/api/beta#beta_tool_choice_tool) { name, type, disable_parallel_tool_use } or [BetaToolChoiceNone](/docs/en/api/beta#beta_tool_choice_none) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

BetaToolChoiceAuto = object { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

BetaToolChoiceAny = object { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceTool = object { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceNone = object { type }

The model will not be allowed to use tools.

type: "none"

BetaToolChoiceAny = object { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceAuto = object { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

BetaToolChoiceNone = object { type }

The model will not be allowed to use tools.

type: "none"

BetaToolChoiceTool = object { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolComputerUse20241022 = object { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

display_width_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20250124 = object { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

display_width_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20251124 = object { display_height_px, display_width_px, name, 8 more }

display_height_px: number

The height of the display in pixels.

display_width_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer_20251124"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolReferenceBlock = object { tool_name, type }

tool_name: string

type: "tool_reference"

BetaToolReferenceBlockParam = object { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or 2 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or 2 more

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam = object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaRequestDocumentBlock = object { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaToolReferenceBlockParam = object { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error: optional boolean

BetaToolSearchToolBm25_20251119 = object { name, type, allowed_callers, 3 more }

name: "tool_search_tool_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolRegex20251119 = object { name, type, allowed_callers, 3 more }

name: "tool_search_tool_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaToolSearchToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type } or [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlockParam = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control }

tool_name: string

type: "tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

BetaToolSearchToolSearchResultBlockParam = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control }

tool_name: string

type: "tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

BetaToolTextEditor20241022 = object { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250124 = object { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250429 = object { name, type, allowed_callers, 4 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250429"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250728 = object { name, type, allowed_callers, 5 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250728"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

max_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolUnion = [BetaTool](/docs/en/api/beta#beta_tool) { input_schema, name, allowed_callers, 7 more } or [BetaToolBash20241022](/docs/en/api/beta#beta_tool_bash_20241022) { name, type, allowed_callers, 4 more } or [BetaToolBash20250124](/docs/en/api/beta#beta_tool_bash_20250124) { name, type, allowed_callers, 4 more } or 18 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

BetaTool = object { input_schema, name, allowed_callers, 7 more }

input_schema: object { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map\[unknown\]

required: optional array of string

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

BetaToolBash20241022 = object { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolBash20250124 = object { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250522 = object { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250522"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250825 = object { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250825"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20260120 = object { name, type, allowed_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20260120"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20241022 = object { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

display_width_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818 = object { name, type, allowed_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory_20250818"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20250124 = object { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

display_width_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20241022 = object { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20251124 = object { display_height_px, display_width_px, name, 8 more }

display_height_px: number

The height of the display in pixels.

display_width_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer_20251124"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250124 = object { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250429 = object { name, type, allowed_callers, 4 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250429"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250728 = object { name, type, allowed_callers, 5 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250728"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

max_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebSearchTool20250305 = object { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20250305"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user_location: optional [BetaUserLocation](/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebFetchTool20250910 = object { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20250910"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: optional array of string

List of domains to allow fetching from

blocked_domains: optional array of string

List of domains to block fetching from

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebSearchTool20260209 = object { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20260209"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user_location: optional [BetaUserLocation](/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebFetchTool20260209 = object { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20260209"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: optional array of string

List of domains to allow fetching from

blocked_domains: optional array of string

List of domains to block fetching from

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolBm25_20251119 = object { name, type, allowed_callers, 3 more }

name: "tool_search_tool_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolRegex20251119 = object { name, type, allowed_callers, 3 more }

name: "tool_search_tool_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMCPToolset = object { mcp_server_name, type, cache_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: string

Name of the MCP server to configure tools for

type: "mcp_toolset"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs: optional map\[[BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config) { defer_loading, enabled } \]

Configuration overrides for specific tools, keyed by tool name

defer_loading: optional boolean

enabled: optional boolean

default_config: optional [BetaMCPToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) { defer_loading, enabled }

Default configuration applied to all tools from this server

defer_loading: optional boolean

enabled: optional boolean

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaToolUsesKeep = object { type, value }

type: "tool_uses"

value: number

BetaToolUsesTrigger = object { type, value }

type: "tool_uses"

value: number

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

inference_geo: string

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

BetaUserLocation = object { type, city, country, 2 more }

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

BetaWebFetchBlockParam = object { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web_fetch_result"

url: string

Fetched content URL

retrieved_at: optional string

ISO 8601 timestamp when the content was retrieved

BetaWebFetchTool20250910 = object { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20250910"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: optional array of string

List of domains to allow fetching from

blocked_domains: optional array of string

List of domains to block fetching from

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebFetchTool20260209 = object { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20260209"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: optional array of string

List of domains to allow fetching from

blocked_domains: optional array of string

List of domains to block fetching from

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlockParam = object { content, tool_use_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type } or [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlockParam = object { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

BetaURLImageSource = object { type, url }

type: "url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

type: "image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

BetaURLPDFSource = object { type, url }

type: "url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

type: "document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web_fetch_result"

url: string

Fetched content URL

retrieved_at: optional string

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchToolResultErrorBlockParam = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchToolResultErrorCode = "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 5 more

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

BetaWebSearchResultBlock = object { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

BetaWebSearchResultBlockParam = object { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age: optional string

BetaWebSearchTool20250305 = object { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20250305"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user_location: optional [BetaUserLocation](/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebSearchTool20260209 = object { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20260209"

allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user_location: optional [BetaUserLocation](/docs/en/api/beta#beta_user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

BetaWebSearchToolRequestError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlockContent = [BetaWebSearchToolResultError](/docs/en/api/beta#beta_web_search_tool_result_error) { error_code, type } or array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

BetaWebSearchToolResultBlockParam = object { content, tool_use_id, type, 2 more }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age: optional string

BetaWebSearchToolRequestError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

tool_use_id: string

type: "web_search_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlockParamContent = array of [BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more } or [BetaWebSearchToolRequestError](/docs/en/api/beta#beta_web_search_tool_request_error) { error_code, type }

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age: optional string

BetaWebSearchToolRequestError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

BetaWebSearchToolResultErrorCode = "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

#### BetaMessagesBatches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

BetaDeletedMessageBatch = object { id, type }

id: string

ID of the Message Batch.

type: "message_batch_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

BetaMessageBatch = object { id, archived_at, cancel_initiated_at, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

archived_at: string

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel_initiated_at: string

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.

ended_at: string

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

processing_status: "in_progress" or "canceling" or "ended"

Processing status of the Message Batch.

Accepts one of the following:

"in_progress"

"canceling"

"ended"

request_counts: [BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts) { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results_url: string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: "message_batch"

Object type.

For Message Batches, this is always `"message_batch"`.

BetaMessageBatchCanceledResult = object { type }

type: "canceled"

BetaMessageBatchErroredResult = object { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError = object { message, type }

message: string

type: "invalid_request_error"

BetaAuthenticationError = object { message, type }

message: string

type: "authentication_error"

BetaBillingError = object { message, type }

message: string

type: "billing_error"

BetaPermissionError = object { message, type }

message: string

type: "permission_error"

BetaNotFoundError = object { message, type }

message: string

type: "not_found_error"

BetaRateLimitError = object { message, type }

message: string

type: "rate_limit_error"

BetaGatewayTimeoutError = object { message, type }

message: string

type: "timeout_error"

BetaAPIError = object { message, type }

message: string

type: "api_error"

BetaOverloadedError = object { message, type }

message: string

type: "overloaded_error"

request_id: string

type: "error"

type: "errored"

BetaMessageBatchExpiredResult = object { type }

type: "expired"

BetaMessageBatchIndividualResponse = object { custom_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

BetaMessageBatchSucceededResult = object { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-opus-4-5-20251101" or 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

inference_geo: string

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

BetaMessageBatchErroredResult = object { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError = object { message, type }

message: string

type: "invalid_request_error"

BetaAuthenticationError = object { message, type }

message: string

type: "authentication_error"

BetaBillingError = object { message, type }

message: string

type: "billing_error"

BetaPermissionError = object { message, type }

message: string

type: "permission_error"

BetaNotFoundError = object { message, type }

message: string

type: "not_found_error"

BetaRateLimitError = object { message, type }

message: string

type: "rate_limit_error"

BetaGatewayTimeoutError = object { message, type }

message: string

type: "timeout_error"

BetaAPIError = object { message, type }

message: string

type: "api_error"

BetaOverloadedError = object { message, type }

message: string

type: "overloaded_error"

request_id: string

type: "error"

type: "errored"

BetaMessageBatchCanceledResult = object { type }

type: "canceled"

BetaMessageBatchExpiredResult = object { type }

type: "expired"

BetaMessageBatchRequestCounts = object { canceled, errored, expired, 2 more }

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

BetaMessageBatchResult = [BetaMessageBatchSucceededResult](/docs/en/api/beta#beta_message_batch_succeeded_result) { message, type } or [BetaMessageBatchErroredResult](/docs/en/api/beta#beta_message_batch_errored_result) { error, type } or [BetaMessageBatchCanceledResult](/docs/en/api/beta#beta_message_batch_canceled_result) { type } or [BetaMessageBatchExpiredResult](/docs/en/api/beta#beta_message_batch_expired_result) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

BetaMessageBatchSucceededResult = object { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-opus-4-5-20251101" or 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

inference_geo: string

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

BetaMessageBatchErroredResult = object { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError = object { message, type }

message: string

type: "invalid_request_error"

BetaAuthenticationError = object { message, type }

message: string

type: "authentication_error"

BetaBillingError = object { message, type }

message: string

type: "billing_error"

BetaPermissionError = object { message, type }

message: string

type: "permission_error"

BetaNotFoundError = object { message, type }

message: string

type: "not_found_error"

BetaRateLimitError = object { message, type }

message: string

type: "rate_limit_error"

BetaGatewayTimeoutError = object { message, type }

message: string

type: "timeout_error"

BetaAPIError = object { message, type }

message: string

type: "api_error"

BetaOverloadedError = object { message, type }

message: string

type: "overloaded_error"

request_id: string

type: "error"

type: "errored"

BetaMessageBatchCanceledResult = object { type }

type: "canceled"

BetaMessageBatchExpiredResult = object { type }

type: "expired"

BetaMessageBatchSucceededResult = object { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

skills: array of [BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version }

Skills loaded in the container

skill_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

BetaTextBlock = object { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

BetaThinkingBlock = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

BetaRedactedThinkingBlock = object { data, type }

data: string

type: "redacted_thinking"

BetaToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaServerToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebSearchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

UnionMember1 = array of [BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaWebFetchToolResultBlock = object { content, tool_use_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } or [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

BetaWebFetchBlock = object { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved_at: string

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

BetaServerToolCaller20260120 = object { tool_id, type }

tool_id: string

type: "code_execution_20260120"

BetaCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

BetaCodeExecutionToolResultError = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

BetaCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

BetaEncryptedCodeExecutionResultBlock = object { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type }

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } or [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type }

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock = object { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string

type: "text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock = object { content, file_type, num_lines, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number

start_line: number

total_lines: number

type: "text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock = object { lines, new_lines, new_start, 3 more }

lines: array of string

new_lines: number

new_start: number

old_lines: number

old_start: number

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock = object { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } or [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError = object { error_code, error_message, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string

type: "tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type }

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

BetaMCPToolUseBlock = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

BetaMCPToolResultBlock = object { content, is_error, tool_use_id, type }

content: string or array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockContent = array of [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type }

citations: array of [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

file_id: string

start_char_index: number

type: "char_location"

BetaCitationPageLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

file_id: string

start_page_number: number

type: "page_location"

BetaCitationContentBlockLocation = object { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

file_id: string

start_block_index: number

type: "content_block_location"

BetaCitationsWebSearchResultLocation = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

url: string

BetaCitationSearchResultLocation = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

text: string

type: "text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

BetaContainerUploadBlock = object { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

BetaCompactionBlock = object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: array of [BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } or [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type }

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse = object { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_tool_uses: number

Number of tool uses that were cleared.

type: "clear_tool_uses_20250919"

The type of context management edit applied.

BetaClearThinking20251015EditResponse = object { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

cleared_thinking_turns: number

Number of thinking turns that were cleared.

type: "clear_thinking_20251015"

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-opus-4-5-20251101" or 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = string

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

inference_geo: string

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

BetaCompactionIterationUsage = object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output_tokens: number

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: "succeeded"

#### BetaFiles

##### [Upload File](/docs/en/api/beta/files/upload)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

DeletedFile = object { id, type }

id: string

ID of the deleted file.

type: optional "file_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

FileMetadata = object { id, created_at, filename, 4 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

created_at: string

RFC 3339 datetime string representing when the file was created.

filename: string

Original filename of the uploaded file.

mime_type: string

MIME type of the file.

size_bytes: number

Size of the file in bytes.

type: "file"

Object type.

For files, this is always `"file"`.

downloadable: optional boolean

Whether the file can be downloaded.

#### BetaSkills

##### [Create Skill](/docs/en/api/beta/skills/create)

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

DELETE/v1/skills/{skill_id}

#### BetaSkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}
