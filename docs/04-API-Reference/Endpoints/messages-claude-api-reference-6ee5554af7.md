---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:07:13Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/messages"
title: "Messages - Claude API Reference"
---

Copy page

TypeScript

# Messages

##### [Create a Message](/docs/en/api/beta/messages/create)

client.beta.messages.create(MessageCreateParamsparams, RequestOptionsoptions?): [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more } \| Stream\<[BetaRawMessageStreamEvent](/docs/en/api/beta#beta_raw_message_stream_event)\>

post/v1/messages

##### [Count tokens in a Message](/docs/en/api/beta/messages/count_tokens)

client.beta.messages.countTokens(MessageCountTokensParams { messages, model, context_management, 8 more } params, RequestOptionsoptions?): [BetaMessageTokensCount](/docs/en/api/beta#beta_message_tokens_count) { context_management, input_tokens }

post/v1/messages/count_tokens

##### ModelsExpand Collapse 

BetaAllThinkingTurns { type }

type: "all"

Accepts one of the following:

"all"

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaBashCodeExecutionOutputBlock { file_id, type }

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

BetaBashCodeExecutionOutputBlockParam { file_id, type }

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

BetaBashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaBashCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type } \| [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionToolResultErrorParam { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaCacheControlEphemeral { type, ttl }

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCacheCreation { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationConfig { enabled }

enabled: boolean

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationsConfigParam { enabled }

enabled?: boolean

BetaCitationsDelta { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

type: "citations_delta"

Accepts one of the following:

"citations_delta"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaClearThinking20251015Edit { type, keep }

type: "clear_thinking_20251015"

Accepts one of the following:

"clear_thinking_20251015"

keep?: [BetaThinkingTurns](/docs/en/api/beta#beta_thinking_turns) { type, value } \| [BetaAllThinkingTurns](/docs/en/api/beta#beta_all_thinking_turns) { type } \| "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

BetaThinkingTurns { type, value }

type: "thinking_turns"

Accepts one of the following:

"thinking_turns"

value: number

BetaAllThinkingTurns { type }

type: "all"

Accepts one of the following:

"all"

"all"

"all"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

BetaClearToolUses20250919Edit { type, clear_at_least, clear_tool_inputs, 3 more }

type: "clear_tool_uses_20250919"

Accepts one of the following:

"clear_tool_uses_20250919"

clear_at_least?: [BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value } \| null

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

clear_tool_inputs?: boolean \| Array\<string\> \| null

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

boolean

Array\<string\>

exclude_tools?: Array\<string\> \| null

Tool names whose uses are preserved from clearing

keep?: [BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: "tool_uses"

Accepts one of the following:

"tool_uses"

value: number

trigger?: [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value } \| [BetaToolUsesTrigger](/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

BetaInputTokensTrigger { type, value }

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

BetaToolUsesTrigger { type, value }

type: "tool_uses"

Accepts one of the following:

"tool_uses"

value: number

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaCodeExecutionOutputBlock { file_id, type }

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

BetaCodeExecutionOutputBlockParam { file_id, type }

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

BetaCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

BetaCodeExecutionTool20250522 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: "code_execution_20250522"

Accepts one of the following:

"code_execution_20250522"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250825 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultError](/docs/en/api/beta#beta_code_execution_tool_result_error) { error_code, type } \| [BetaCodeExecutionResultBlock](/docs/en/api/beta#beta_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

BetaCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_code_execution_tool_result_error_param) { error_code, type } \| [BetaCodeExecutionResultBlockParam](/docs/en/api/beta#beta_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionToolResultErrorCode = "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

BetaCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCompact20260112Edit { type, instructions, pause_after_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact_20260112"

Accepts one of the following:

"compact_20260112"

instructions?: string \| null

Additional instructions for summarization.

pause_after_compaction?: boolean

Whether to pause after compaction and return the compaction block to the user.

trigger?: [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value } \| null

When to trigger compaction. Defaults to 150000 input tokens.

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

BetaCompactionBlockParam { content, type, cache_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: string \| null

Summary of previously compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionContentBlockDelta { content, type }

content: string \| null

type: "compaction_delta"

Accepts one of the following:

"compaction_delta"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

BetaContainer { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

BetaContainerParams { id, skills }

Container parameters with skills to be loaded.

id?: string \| null

Container id

skills?: Array\<[BetaSkillParams](/docs/en/api/beta#beta_skill_params) { skill_id, type, version } \> \| null

List of skills to load in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version?: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaContainerUploadBlockParam { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContentBlock = [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \| [BetaThinkingBlock](/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } \| [BetaRedactedThinkingBlock](/docs/en/api/beta#beta_redacted_thinking_block) { data, type } \| 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

BetaContentBlockParam = [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more } \| 16 more

Regular text content.

Accepts one of the following:

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestDocumentBlock { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled?: boolean

BetaThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

Accepts one of the following:

"tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } \| 2 more\>

Accepts one of the following:

string

Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } \| 2 more\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled?: boolean

BetaRequestDocumentBlock { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

BetaToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error?: boolean

BetaServerToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

BetaWebSearchToolRequestError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaWebFetchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type } \| [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlockParam { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

retrieved_at?: string \| null

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type } \| [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } \| [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message?: string \| null

BetaTextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines?: number \| null

start_line?: number \| null

total_lines?: number \| null

BetaTextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines?: Array\<string\> \| null

new_lines?: number \| null

new_start?: number \| null

old_lines?: number \| null

old_start?: number \| null

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type } \| [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestMCPToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

Accepts one of the following:

string

Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

is_error?: boolean

BetaContainerUploadBlockParam { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionBlockParam { content, type, cache_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: string \| null

Summary of previously compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaContentBlockSourceContent = [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control }

Accepts one of the following:

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContextManagementConfig { edits }

edits?: Array\<[BetaClearToolUses20250919Edit](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit) { type, clear_at_least, clear_tool_inputs, 3 more } \| [BetaClearThinking20251015Edit](/docs/en/api/beta#beta_clear_thinking_20251015_edit) { type, keep } \| [BetaCompact20260112Edit](/docs/en/api/beta#beta_compact_20260112_edit) { type, instructions, pause_after_compaction, trigger } \>

List of context management edits to apply

Accepts one of the following:

BetaClearToolUses20250919Edit { type, clear_at_least, clear_tool_inputs, 3 more }

type: "clear_tool_uses_20250919"

Accepts one of the following:

"clear_tool_uses_20250919"

clear_at_least?: [BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value } \| null

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

clear_tool_inputs?: boolean \| Array\<string\> \| null

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

boolean

Array\<string\>

exclude_tools?: Array\<string\> \| null

Tool names whose uses are preserved from clearing

keep?: [BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: "tool_uses"

Accepts one of the following:

"tool_uses"

value: number

trigger?: [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value } \| [BetaToolUsesTrigger](/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

BetaInputTokensTrigger { type, value }

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

BetaToolUsesTrigger { type, value }

type: "tool_uses"

Accepts one of the following:

"tool_uses"

value: number

BetaClearThinking20251015Edit { type, keep }

type: "clear_thinking_20251015"

Accepts one of the following:

"clear_thinking_20251015"

keep?: [BetaThinkingTurns](/docs/en/api/beta#beta_thinking_turns) { type, value } \| [BetaAllThinkingTurns](/docs/en/api/beta#beta_all_thinking_turns) { type } \| "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

BetaThinkingTurns { type, value }

type: "thinking_turns"

Accepts one of the following:

"thinking_turns"

value: number

BetaAllThinkingTurns { type }

type: "all"

Accepts one of the following:

"all"

"all"

"all"

BetaCompact20260112Edit { type, instructions, pause_after_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact_20260112"

Accepts one of the following:

"compact_20260112"

instructions?: string \| null

Additional instructions for summarization.

pause_after_compaction?: boolean

Whether to pause after compaction and return the compaction block to the user.

trigger?: [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value } \| null

When to trigger compaction. Defaults to 150000 input tokens.

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

BetaContextManagementResponse { applied_edits }

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

BetaCountTokensContextManagementResponse { original_input_tokens }

original_input_tokens: number

The original token count before context management was applied

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaDocumentBlock { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaInputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

Accepts one of the following:

"input_json_delta"

BetaInputTokensClearAtLeast { type, value }

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

BetaInputTokensTrigger { type, value }

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

BetaJSONOutputFormat { schema, type }

schema: Record\<string, unknown\>

The JSON schema of the format

type: "json_schema"

Accepts one of the following:

"json_schema"

BetaMCPToolConfig { defer_loading, enabled }

Configuration for a specific tool in an MCP toolset.

defer_loading?: boolean

enabled?: boolean

BetaMCPToolDefaultConfig { defer_loading, enabled }

Default configuration for tools in an MCP toolset.

defer_loading?: boolean

enabled?: boolean

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolset { mcp_server_name, type, cache_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: string

Name of the MCP server to configure tools for

maxLength255

minLength1

type: "mcp_toolset"

Accepts one of the following:

"mcp_toolset"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs?: Record\<string, [BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config) { defer_loading, enabled } \> \| null

Configuration overrides for specific tools, keyed by tool name

defer_loading?: boolean

enabled?: boolean

default_config?: [BetaMCPToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) { defer_loading, enabled }

Default configuration applied to all tools from this server

defer_loading?: boolean

enabled?: boolean

BetaMemoryTool20250818 { name, type, allowed_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"memory"

type: "memory_20250818"

Accepts one of the following:

"memory_20250818"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818Command = [BetaMemoryTool20250818ViewCommand](/docs/en/api/beta#beta_memory_tool_20250818_view_command) { command, path, view_range } \| [BetaMemoryTool20250818CreateCommand](/docs/en/api/beta#beta_memory_tool_20250818_create_command) { command, file_text, path } \| [BetaMemoryTool20250818StrReplaceCommand](/docs/en/api/beta#beta_memory_tool_20250818_str_replace_command) { command, new_str, old_str, path } \| 3 more

Accepts one of the following:

BetaMemoryTool20250818ViewCommand { command, path, view_range }

command: "view"

Command type identifier

Accepts one of the following:

"view"

path: string

Path to directory or file to view

view_range?: Array\<number\>

Optional line range for viewing specific lines

BetaMemoryTool20250818CreateCommand { command, file_text, path }

command: "create"

Command type identifier

Accepts one of the following:

"create"

file_text: string

Content to write to the file

path: string

Path where the file should be created

BetaMemoryTool20250818StrReplaceCommand { command, new_str, old_str, path }

command: "str_replace"

Command type identifier

Accepts one of the following:

"str_replace"

new_str: string

Text to replace with

old_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced

BetaMemoryTool20250818InsertCommand { command, insert_line, insert_text, path }

command: "insert"

Command type identifier

Accepts one of the following:

"insert"

insert_line: number

Line number where text should be inserted

minimum1

insert_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted

BetaMemoryTool20250818DeleteCommand { command, path }

command: "delete"

Command type identifier

Accepts one of the following:

"delete"

path: string

Path to the file or directory to delete

BetaMemoryTool20250818RenameCommand { command, new_path, old_path }

command: "rename"

Command type identifier

Accepts one of the following:

"rename"

new_path: string

New path for the file or directory

old_path: string

Current path of the file or directory

BetaMemoryTool20250818CreateCommand { command, file_text, path }

command: "create"

Command type identifier

Accepts one of the following:

"create"

file_text: string

Content to write to the file

path: string

Path where the file should be created

BetaMemoryTool20250818DeleteCommand { command, path }

command: "delete"

Command type identifier

Accepts one of the following:

"delete"

path: string

Path to the file or directory to delete

BetaMemoryTool20250818InsertCommand { command, insert_line, insert_text, path }

command: "insert"

Command type identifier

Accepts one of the following:

"insert"

insert_line: number

Line number where text should be inserted

minimum1

insert_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted

BetaMemoryTool20250818RenameCommand { command, new_path, old_path }

command: "rename"

Command type identifier

Accepts one of the following:

"rename"

new_path: string

New path for the file or directory

old_path: string

Current path of the file or directory

BetaMemoryTool20250818StrReplaceCommand { command, new_str, old_str, path }

command: "str_replace"

Command type identifier

Accepts one of the following:

"str_replace"

new_str: string

Text to replace with

old_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced

BetaMemoryTool20250818ViewCommand { command, path, view_range }

command: "view"

Command type identifier

Accepts one of the following:

"view"

path: string

Path to directory or file to view

view_range?: Array\<number\>

Optional line range for viewing specific lines

BetaMessage { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\>

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

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits } \| null

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason) \| null

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

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

BetaMessageDeltaUsage { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: number \| null

The cumulative number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaMessageParam { content, role }

content: string \| Array\<[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\>

Accepts one of the following:

string

Array\<[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestDocumentBlock { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled?: boolean

BetaThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

Accepts one of the following:

"tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } \| 2 more\>

Accepts one of the following:

string

Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } \| 2 more\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled?: boolean

BetaRequestDocumentBlock { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

BetaToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error?: boolean

BetaServerToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

BetaWebSearchToolRequestError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaWebFetchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type } \| [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlockParam { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

retrieved_at?: string \| null

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type } \| [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } \| [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message?: string \| null

BetaTextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines?: number \| null

start_line?: number \| null

total_lines?: number \| null

BetaTextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines?: Array\<string\> \| null

new_lines?: number \| null

new_start?: number \| null

old_lines?: number \| null

old_start?: number \| null

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type } \| [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestMCPToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

Accepts one of the following:

string

Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

is_error?: boolean

BetaContainerUploadBlockParam { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionBlockParam { content, type, cache_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: string \| null

Summary of previously compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

role: "user" \| "assistant"

Accepts one of the following:

"user"

"assistant"

BetaMessageTokensCount { context_management, input_tokens }

context_management: [BetaCountTokensContextManagementResponse](/docs/en/api/beta#beta_count_tokens_context_management_response) { original_input_tokens } \| null

Information about context management applied to the message.

original_input_tokens: number

The original token count before context management was applied

input_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

BetaMetadata { user_id }

user_id?: string \| null

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

BetaOutputConfig { effort, format }

effort?: "low" \| "medium" \| "high" \| "max" \| null

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format?: [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format) { schema, type } \| null

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: Record\<string, unknown\>

The JSON schema of the format

type: "json_schema"

Accepts one of the following:

"json_schema"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaRawContentBlockDelta = [BetaTextDelta](/docs/en/api/beta#beta_text_delta) { text, type } \| [BetaInputJSONDelta](/docs/en/api/beta#beta_input_json_delta) { partial_json, type } \| [BetaCitationsDelta](/docs/en/api/beta#beta_citations_delta) { citation, type } \| 3 more

Accepts one of the following:

BetaTextDelta { text, type }

text: string

type: "text_delta"

Accepts one of the following:

"text_delta"

BetaInputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

Accepts one of the following:

"input_json_delta"

BetaCitationsDelta { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

type: "citations_delta"

Accepts one of the following:

"citations_delta"

BetaThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Accepts one of the following:

"thinking_delta"

BetaSignatureDelta { signature, type }

signature: string

type: "signature_delta"

Accepts one of the following:

"signature_delta"

BetaCompactionContentBlockDelta { content, type }

content: string \| null

type: "compaction_delta"

Accepts one of the following:

"compaction_delta"

BetaRawContentBlockDeltaEvent { delta, index, type }

delta: [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

BetaTextDelta { text, type }

text: string

type: "text_delta"

Accepts one of the following:

"text_delta"

BetaInputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

Accepts one of the following:

"input_json_delta"

BetaCitationsDelta { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

type: "citations_delta"

Accepts one of the following:

"citations_delta"

BetaThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Accepts one of the following:

"thinking_delta"

BetaSignatureDelta { signature, type }

signature: string

type: "signature_delta"

Accepts one of the following:

"signature_delta"

BetaCompactionContentBlockDelta { content, type }

content: string \| null

type: "compaction_delta"

Accepts one of the following:

"compaction_delta"

index: number

type: "content_block_delta"

Accepts one of the following:

"content_block_delta"

BetaRawContentBlockStartEvent { content_block, index, type }

content_block: [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \| [BetaThinkingBlock](/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } \| [BetaRedactedThinkingBlock](/docs/en/api/beta#beta_redacted_thinking_block) { data, type } \| 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

index: number

type: "content_block_start"

Accepts one of the following:

"content_block_start"

BetaRawContentBlockStopEvent { index, type }

index: number

type: "content_block_stop"

Accepts one of the following:

"content_block_stop"

BetaRawMessageDeltaEvent { context_management, delta, type, usage }

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits } \| null

Information about context management strategies applied during the request

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

delta: Delta { container, stop_reason, stop_sequence }

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason) \| null

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string \| null

type: "message_delta"

Accepts one of the following:

"message_delta"

usage: [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: number \| null

The cumulative number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

BetaRawMessageStartEvent { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\>

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

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits } \| null

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason) \| null

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

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "message_start"

Accepts one of the following:

"message_start"

BetaRawMessageStopEvent { type }

type: "message_stop"

Accepts one of the following:

"message_stop"

BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](/docs/en/api/beta#beta_raw_message_start_event) { message, type } \| [BetaRawMessageDeltaEvent](/docs/en/api/beta#beta_raw_message_delta_event) { context_management, delta, type, usage } \| [BetaRawMessageStopEvent](/docs/en/api/beta#beta_raw_message_stop_event) { type } \| 3 more

Accepts one of the following:

BetaRawMessageStartEvent { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\>

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

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits } \| null

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason) \| null

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

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "message_start"

Accepts one of the following:

"message_start"

BetaRawMessageDeltaEvent { context_management, delta, type, usage }

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits } \| null

Information about context management strategies applied during the request

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

delta: Delta { container, stop_reason, stop_sequence }

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason) \| null

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: string \| null

type: "message_delta"

Accepts one of the following:

"message_delta"

usage: [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: number \| null

The cumulative number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

BetaRawMessageStopEvent { type }

type: "message_stop"

Accepts one of the following:

"message_stop"

BetaRawContentBlockStartEvent { content_block, index, type }

content_block: [BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \| [BetaThinkingBlock](/docs/en/api/beta#beta_thinking_block) { signature, thinking, type } \| [BetaRedactedThinkingBlock](/docs/en/api/beta#beta_redacted_thinking_block) { data, type } \| 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

index: number

type: "content_block_start"

Accepts one of the following:

"content_block_start"

BetaRawContentBlockDeltaEvent { delta, index, type }

delta: [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

BetaTextDelta { text, type }

text: string

type: "text_delta"

Accepts one of the following:

"text_delta"

BetaInputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

Accepts one of the following:

"input_json_delta"

BetaCitationsDelta { citation, type }

citation: [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

type: "citations_delta"

Accepts one of the following:

"citations_delta"

BetaThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Accepts one of the following:

"thinking_delta"

BetaSignatureDelta { signature, type }

signature: string

type: "signature_delta"

Accepts one of the following:

"signature_delta"

BetaCompactionContentBlockDelta { content, type }

content: string \| null

type: "compaction_delta"

Accepts one of the following:

"compaction_delta"

index: number

type: "content_block_delta"

Accepts one of the following:

"content_block_delta"

BetaRawContentBlockStopEvent { index, type }

index: number

type: "content_block_stop"

Accepts one of the following:

"content_block_stop"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaRedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaRequestDocumentBlock { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

BetaRequestMCPServerToolConfiguration { allowed_tools, enabled }

allowed_tools?: Array\<string\> \| null

enabled?: boolean \| null

BetaRequestMCPServerURLDefinition { name, type, url, 2 more }

name: string

type: "url"

Accepts one of the following:

"url"

url: string

authorization_token?: string \| null

tool_configuration?: [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled } \| null

allowed_tools?: Array\<string\> \| null

enabled?: boolean \| null

BetaRequestMCPToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

Accepts one of the following:

string

Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

is_error?: boolean

BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled?: boolean

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUsage { web_fetch_requests, web_search_requests }

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaSignatureDelta { signature, type }

signature: string

type: "signature_delta"

Accepts one of the following:

"signature_delta"

BetaSkill { skill_id, type, version }

A skill that was loaded in a container (response model).

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

BetaSkillParams { skill_id, type, version }

Specification for a skill to be loaded in a container (request model).

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version?: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

BetaStopReason = "end_turn" \| "max_tokens" \| "stop_sequence" \| 5 more

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaTextCitation = [BetaCitationCharLocation](/docs/en/api/beta#beta_citation_char_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationPageLocation](/docs/en/api/beta#beta_citation_page_location) { cited_text, document_index, document_title, 4 more } \| [BetaCitationContentBlockLocation](/docs/en/api/beta#beta_citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaTextCitationParam = [BetaCitationCharLocationParam](/docs/en/api/beta#beta_citation_char_location_param) { cited_text, document_index, document_title, 3 more } \| [BetaCitationPageLocationParam](/docs/en/api/beta#beta_citation_page_location_param) { cited_text, document_index, document_title, 3 more } \| [BetaCitationContentBlockLocationParam](/docs/en/api/beta#beta_citation_content_block_location_param) { cited_text, document_index, document_title, 3 more } \| 2 more

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaTextDelta { text, type }

text: string

type: "text_delta"

Accepts one of the following:

"text_delta"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines?: Array\<string\> \| null

new_lines?: number \| null

new_start?: number \| null

old_lines?: number \| null

old_start?: number \| null

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } \| [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message?: string \| null

BetaTextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines?: number \| null

start_line?: number \| null

total_lines?: number \| null

BetaTextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines?: Array\<string\> \| null

new_lines?: number \| null

new_start?: number \| null

old_lines?: number \| null

old_start?: number \| null

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message?: string \| null

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines?: number \| null

start_line?: number \| null

total_lines?: number \| null

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaThinkingConfigAdaptive { type }

type: "adaptive"

Accepts one of the following:

"adaptive"

BetaThinkingConfigDisabled { type }

type: "disabled"

Accepts one of the following:

"disabled"

BetaThinkingConfigEnabled { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

Accepts one of the following:

"enabled"

BetaThinkingConfigParam = [BetaThinkingConfigEnabled](/docs/en/api/beta#beta_thinking_config_enabled) { budget_tokens, type } \| [BetaThinkingConfigDisabled](/docs/en/api/beta#beta_thinking_config_disabled) { type } \| [BetaThinkingConfigAdaptive](/docs/en/api/beta#beta_thinking_config_adaptive) { type }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

BetaThinkingConfigEnabled { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

Accepts one of the following:

"enabled"

BetaThinkingConfigDisabled { type }

type: "disabled"

Accepts one of the following:

"disabled"

BetaThinkingConfigAdaptive { type }

type: "adaptive"

Accepts one of the following:

"adaptive"

BetaThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Accepts one of the following:

"thinking_delta"

BetaThinkingTurns { type, value }

type: "thinking_turns"

Accepts one of the following:

"thinking_turns"

value: number

BetaTool { input_schema, name, allowed_callers, 7 more }

input_schema: InputSchema { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

Accepts one of the following:

"object"

properties?: Record\<string, unknown\> \| null

required?: Array\<string\> \| null

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description?: string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming?: boolean \| null

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

type?: "custom" \| null

Accepts one of the following:

"custom"

BetaToolBash20241022 { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20241022"

Accepts one of the following:

"bash_20241022"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolBash20250124 { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20250124"

Accepts one of the following:

"bash_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolChoice = [BetaToolChoiceAuto](/docs/en/api/beta#beta_tool_choice_auto) { type, disable_parallel_tool_use } \| [BetaToolChoiceAny](/docs/en/api/beta#beta_tool_choice_any) { type, disable_parallel_tool_use } \| [BetaToolChoiceTool](/docs/en/api/beta#beta_tool_choice_tool) { name, type, disable_parallel_tool_use } \| [BetaToolChoiceNone](/docs/en/api/beta#beta_tool_choice_none) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

BetaToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

Accepts one of the following:

"auto"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

BetaToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

Accepts one of the following:

"any"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

Accepts one of the following:

"tool"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceNone { type }

The model will not be allowed to use tools.

type: "none"

Accepts one of the following:

"none"

BetaToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

Accepts one of the following:

"any"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

Accepts one of the following:

"auto"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

BetaToolChoiceNone { type }

The model will not be allowed to use tools.

type: "none"

Accepts one of the following:

"none"

BetaToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

Accepts one of the following:

"tool"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolComputerUse20241022 { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20241022"

Accepts one of the following:

"computer_20241022"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number?: number \| null

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20250124 { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20250124"

Accepts one of the following:

"computer_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number?: number \| null

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20251124 { display_height_px, display_width_px, name, 8 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20251124"

Accepts one of the following:

"computer_20251124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number?: number \| null

The X11 display number (e.g. 0, 1) for the display.

minimum0

enable_zoom?: boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolReferenceBlock { tool_name, type }

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

BetaToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

Accepts one of the following:

"tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } \| 2 more\>

Accepts one of the following:

string

Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } \| 2 more\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled?: boolean

BetaRequestDocumentBlock { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

BetaToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error?: boolean

BetaToolSearchToolBm25_20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_bm25"

type: "tool_search_tool_bm25_20251119" \| "tool_search_tool_bm25"

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolRegex20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_regex"

type: "tool_search_tool_regex_20251119" \| "tool_search_tool_regex"

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaToolSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type } \| [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolResultErrorParam { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

BetaToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

BetaToolTextEditor20241022 { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20241022"

Accepts one of the following:

"text_editor_20241022"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250124 { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20250124"

Accepts one of the following:

"text_editor_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250429 { name, type, allowed_callers, 4 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250429"

Accepts one of the following:

"text_editor_20250429"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250728 { name, type, allowed_callers, 5 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250728"

Accepts one of the following:

"text_editor_20250728"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

max_characters?: number \| null

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolUnion = [BetaTool](/docs/en/api/beta#beta_tool) { input_schema, name, allowed_callers, 7 more } \| [BetaToolBash20241022](/docs/en/api/beta#beta_tool_bash_20241022) { name, type, allowed_callers, 4 more } \| [BetaToolBash20250124](/docs/en/api/beta#beta_tool_bash_20250124) { name, type, allowed_callers, 4 more } \| 15 more

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

Accepts one of the following:

BetaTool { input_schema, name, allowed_callers, 7 more }

input_schema: InputSchema { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

Accepts one of the following:

"object"

properties?: Record\<string, unknown\> \| null

required?: Array\<string\> \| null

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description?: string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming?: boolean \| null

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

type?: "custom" \| null

Accepts one of the following:

"custom"

BetaToolBash20241022 { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20241022"

Accepts one of the following:

"bash_20241022"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolBash20250124 { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20250124"

Accepts one of the following:

"bash_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250522 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: "code_execution_20250522"

Accepts one of the following:

"code_execution_20250522"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250825 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20241022 { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20241022"

Accepts one of the following:

"computer_20241022"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number?: number \| null

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818 { name, type, allowed_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"memory"

type: "memory_20250818"

Accepts one of the following:

"memory_20250818"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20250124 { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20250124"

Accepts one of the following:

"computer_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number?: number \| null

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20241022 { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20241022"

Accepts one of the following:

"text_editor_20241022"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20251124 { display_height_px, display_width_px, name, 8 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20251124"

Accepts one of the following:

"computer_20251124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number?: number \| null

The X11 display number (e.g. 0, 1) for the display.

minimum0

enable_zoom?: boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250124 { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20250124"

Accepts one of the following:

"text_editor_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250429 { name, type, allowed_callers, 4 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250429"

Accepts one of the following:

"text_editor_20250429"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250728 { name, type, allowed_callers, 5 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250728"

Accepts one of the following:

"text_editor_20250728"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples?: Array\<Record\<string, unknown\>\>

max_characters?: number \| null

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaWebSearchTool20250305 { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: "web_search_20250305"

Accepts one of the following:

"web_search_20250305"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: UserLocation \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

Accepts one of the following:

"approximate"

city?: string \| null

The city of the user.

maxLength255

minLength1

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region?: string \| null

The region of the user.

maxLength255

minLength1

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

BetaWebFetchTool20250910 { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_fetch"

type: "web_fetch_20250910"

Accepts one of the following:

"web_fetch_20250910"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains?: Array\<string\> \| null

List of domains to allow fetching from

blocked_domains?: Array\<string\> \| null

List of domains to block fetching from

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens?: number \| null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolBm25_20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_bm25"

type: "tool_search_tool_bm25_20251119" \| "tool_search_tool_bm25"

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolRegex20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_regex"

type: "tool_search_tool_regex_20251119" \| "tool_search_tool_regex"

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaMCPToolset { mcp_server_name, type, cache_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: string

Name of the MCP server to configure tools for

maxLength255

minLength1

type: "mcp_toolset"

Accepts one of the following:

"mcp_toolset"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs?: Record\<string, [BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config) { defer_loading, enabled } \> \| null

Configuration overrides for specific tools, keyed by tool name

defer_loading?: boolean

enabled?: boolean

default_config?: [BetaMCPToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) { defer_loading, enabled }

Default configuration applied to all tools from this server

defer_loading?: boolean

enabled?: boolean

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaToolUsesKeep { type, value }

type: "tool_uses"

Accepts one of the following:

"tool_uses"

value: number

BetaToolUsesTrigger { type, value }

type: "tool_uses"

Accepts one of the following:

"tool_uses"

value: number

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

BetaWebFetchBlockParam { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

retrieved_at?: string \| null

ISO 8601 timestamp when the content was retrieved

BetaWebFetchTool20250910 { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_fetch"

type: "web_fetch_20250910"

Accepts one of the following:

"web_fetch_20250910"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains?: Array\<string\> \| null

List of domains to allow fetching from

blocked_domains?: Array\<string\> \| null

List of domains to block fetching from

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens?: number \| null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict?: boolean

When true, guarantees schema validation on tool names and inputs

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaWebFetchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type } \| [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlockParam { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource { content, type }

content: string \| Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

string

Array\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

BetaTextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\> \| null

Accepts one of the following:

BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

retrieved_at?: string \| null

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchToolResultErrorBlockParam { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchToolResultErrorCode = "invalid_tool_input" \| "url_too_long" \| "url_not_allowed" \| 5 more

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

BetaWebSearchResultBlock { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

BetaWebSearchResultBlockParam { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

BetaWebSearchTool20250305 { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: "web_search_20250305"

Accepts one of the following:

"web_search_20250305"

allowed_callers?: Array\<"direct" \| "code_execution_20250825"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: UserLocation \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

Accepts one of the following:

"approximate"

city?: string \| null

The city of the user.

maxLength255

minLength1

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region?: string \| null

The region of the user.

maxLength255

minLength1

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

BetaWebSearchToolRequestError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebSearchToolResultBlockContent = [BetaWebSearchToolResultError](/docs/en/api/beta#beta_web_search_tool_result_error) { error_code, type } \| Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

BetaWebSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

BetaWebSearchToolRequestError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

cache_control?: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaWebSearchToolResultBlockParamContent = Array\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more } \> \| [BetaWebSearchToolRequestError](/docs/en/api/beta#beta_web_search_tool_request_error) { error_code, type }

Accepts one of the following:

Array\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

BetaWebSearchToolRequestError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

BetaWebSearchToolResultErrorCode = "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

client.beta.messages.batches.create(BatchCreateParams { requests, betas } params, RequestOptionsoptions?): [BetaMessageBatch](/docs/en/api/beta#beta_message_batch) { id, archived_at, cancel_initiated_at, 7 more }

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

client.beta.messages.batches.retrieve(stringmessageBatchID, BatchRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatch](/docs/en/api/beta#beta_message_batch) { id, archived_at, cancel_initiated_at, 7 more }

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

client.beta.messages.batches.list(BatchListParams { after_id, before_id, limit, betas } params?, RequestOptionsoptions?): Page\<[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) { id, archived_at, cancel_initiated_at, 7 more } \>

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

client.beta.messages.batches.cancel(stringmessageBatchID, BatchCancelParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatch](/docs/en/api/beta#beta_message_batch) { id, archived_at, cancel_initiated_at, 7 more }

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

client.beta.messages.batches.delete(stringmessageBatchID, BatchDeleteParams { betas } params?, RequestOptionsoptions?): [BetaDeletedMessageBatch](/docs/en/api/beta#beta_deleted_message_batch) { id, type }

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

client.beta.messages.batches.results(stringmessageBatchID, BatchResultsParams { betas } params?, RequestOptionsoptions?): [BetaMessageBatchIndividualResponse](/docs/en/api/beta#beta_message_batch_individual_response) { custom_id, result } \| Stream\<[BetaMessageBatchIndividualResponse](/docs/en/api/beta#beta_message_batch_individual_response) { custom_id, result } \>

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

BetaDeletedMessageBatch { id, type }

id: string

ID of the Message Batch.

type: "message_batch_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

"message_batch_deleted"

BetaMessageBatch { id, archived_at, cancel_initiated_at, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

archived_at: string \| null

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel_initiated_at: string \| null

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended_at: string \| null

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processing_status: "in_progress" \| "canceling" \| "ended"

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

results_url: string \| null

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: "message_batch"

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

"message_batch"

BetaMessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError { message, type }

message: string

type: "invalid_request_error"

Accepts one of the following:

"invalid_request_error"

BetaAuthenticationError { message, type }

message: string

type: "authentication_error"

Accepts one of the following:

"authentication_error"

BetaBillingError { message, type }

message: string

type: "billing_error"

Accepts one of the following:

"billing_error"

BetaPermissionError { message, type }

message: string

type: "permission_error"

Accepts one of the following:

"permission_error"

BetaNotFoundError { message, type }

message: string

type: "not_found_error"

Accepts one of the following:

"not_found_error"

BetaRateLimitError { message, type }

message: string

type: "rate_limit_error"

Accepts one of the following:

"rate_limit_error"

BetaGatewayTimeoutError { message, type }

message: string

type: "timeout_error"

Accepts one of the following:

"timeout_error"

BetaAPIError { message, type }

message: string

type: "api_error"

Accepts one of the following:

"api_error"

BetaOverloadedError { message, type }

message: string

type: "overloaded_error"

Accepts one of the following:

"overloaded_error"

request_id: string \| null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

BetaMessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

BetaMessageBatchIndividualResponse { custom_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\>

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

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits } \| null

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason) \| null

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

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

Accepts one of the following:

"succeeded"

BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError { message, type }

message: string

type: "invalid_request_error"

Accepts one of the following:

"invalid_request_error"

BetaAuthenticationError { message, type }

message: string

type: "authentication_error"

Accepts one of the following:

"authentication_error"

BetaBillingError { message, type }

message: string

type: "billing_error"

Accepts one of the following:

"billing_error"

BetaPermissionError { message, type }

message: string

type: "permission_error"

Accepts one of the following:

"permission_error"

BetaNotFoundError { message, type }

message: string

type: "not_found_error"

Accepts one of the following:

"not_found_error"

BetaRateLimitError { message, type }

message: string

type: "rate_limit_error"

Accepts one of the following:

"rate_limit_error"

BetaGatewayTimeoutError { message, type }

message: string

type: "timeout_error"

Accepts one of the following:

"timeout_error"

BetaAPIError { message, type }

message: string

type: "api_error"

Accepts one of the following:

"api_error"

BetaOverloadedError { message, type }

message: string

type: "overloaded_error"

Accepts one of the following:

"overloaded_error"

request_id: string \| null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

BetaMessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

BetaMessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

BetaMessageBatchRequestCounts { canceled, errored, expired, 2 more }

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

BetaMessageBatchResult = [BetaMessageBatchSucceededResult](/docs/en/api/beta#beta_message_batch_succeeded_result) { message, type } \| [BetaMessageBatchErroredResult](/docs/en/api/beta#beta_message_batch_errored_result) { error, type } \| [BetaMessageBatchCanceledResult](/docs/en/api/beta#beta_message_batch_canceled_result) { type } \| [BetaMessageBatchExpiredResult](/docs/en/api/beta#beta_message_batch_expired_result) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\>

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

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits } \| null

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason) \| null

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

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

Accepts one of the following:

"succeeded"

BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

BetaInvalidRequestError { message, type }

message: string

type: "invalid_request_error"

Accepts one of the following:

"invalid_request_error"

BetaAuthenticationError { message, type }

message: string

type: "authentication_error"

Accepts one of the following:

"authentication_error"

BetaBillingError { message, type }

message: string

type: "billing_error"

Accepts one of the following:

"billing_error"

BetaPermissionError { message, type }

message: string

type: "permission_error"

Accepts one of the following:

"permission_error"

BetaNotFoundError { message, type }

message: string

type: "not_found_error"

Accepts one of the following:

"not_found_error"

BetaRateLimitError { message, type }

message: string

type: "rate_limit_error"

Accepts one of the following:

"rate_limit_error"

BetaGatewayTimeoutError { message, type }

message: string

type: "timeout_error"

Accepts one of the following:

"timeout_error"

BetaAPIError { message, type }

message: string

type: "api_error"

Accepts one of the following:

"api_error"

BetaOverloadedError { message, type }

message: string

type: "overloaded_error"

Accepts one of the following:

"overloaded_error"

request_id: string \| null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

BetaMessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

BetaMessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

formatdate-time

skills: Array\<[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \> \| null

Skills loaded in the container

skill_id: string

Skill ID

maxLength64

minLength1

type: "anthropic" \| "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\>

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

BetaTextBlock { citations, text, type }

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

BetaThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaServerToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search" \| "web_fetch" \| "code_execution" \| 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

caller?: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

Array\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

BetaWebFetchToolResultErrorBlock { error_code, type }

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

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

BetaBase64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

title: string \| null

The title of the document

type: "document"

Accepts one of the following:

"document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: number \| null

start_line: number \| null

total_lines: number \| null

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultError { error_code, error_message, type }

error_code: "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

BetaMCPToolUseBlock { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

The name of the MCP tool

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: string \| Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

Accepts one of the following:

string

Array\<[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \>

citations: Array\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

is_error: boolean

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: string \| null

Summary of compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits } \| null

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\<[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \>

List of context management edits that were applied.

Accepts one of the following:

BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: number

Number of tool uses that were cleared.

minimum0

type: "clear_tool_uses_20250919"

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: number

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: number

Number of thinking turns that were cleared.

minimum0

type: "clear_thinking_20251015"

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

"claude-opus-4-6"

Most intelligent model for building agents and coding

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason) \| null

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

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

iterations: Array\<[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \> \| null

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "message"

Usage for a sampling iteration

Accepts one of the following:

"message"

BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number

The number of input tokens read from the cache.

minimum0

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

type: "compaction"

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

minimum0

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

Accepts one of the following:

"succeeded"

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
