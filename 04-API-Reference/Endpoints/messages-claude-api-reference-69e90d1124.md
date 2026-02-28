---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:33:13Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/messages"
title: "Messages - Claude API Reference"
---
# Messages

##### [Create a Message](/docs/en/api/messages/create)

client.messages.create(MessageCreateParamsbody, RequestOptionsoptions?): [Message](/docs/en/api/messages#message) { id, container, content, 6 more } \| Stream\<[RawMessageStreamEvent](/docs/en/api/messages#raw_message_stream_event)\>

POST/v1/messages

##### [Count tokens in a Message](/docs/en/api/messages/count_tokens)

client.messages.countTokens(MessageCountTokensParams { messages, model, cache_control, 5 more } body, RequestOptionsoptions?): [MessageTokensCount](/docs/en/api/messages#message_tokens_count) { input_tokens }

POST/v1/messages/count_tokens

##### ModelsExpand Collapse 

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

BashCodeExecutionOutputBlock { file_id, type }

file_id: string

type: "bash_code_execution_output"

BashCodeExecutionOutputBlockParam { file_id, type }

file_id: string

type: "bash_code_execution_output"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

BashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

BashCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BashCodeExecutionToolResultErrorParam](/docs/en/api/messages#bash_code_execution_tool_result_error_param) { error_code, type } \| [BashCodeExecutionResultBlockParam](/docs/en/api/messages#bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionToolResultErrorCode = "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

BashCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

CacheControlEphemeral { type, ttl }

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

CacheCreation { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsConfig { enabled }

enabled: boolean

CitationsConfigParam { enabled }

enabled?: boolean

CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

type: "citations_delta"

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CodeExecutionOutputBlock { file_id, type }

file_id: string

type: "code_execution_output"

CodeExecutionOutputBlockParam { file_id, type }

file_id: string

type: "code_execution_output"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

CodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

CodeExecutionTool20250522 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250522"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionTool20250825 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250825"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionTool20260120 { name, type, allowed_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20260120"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

CodeExecutionToolResultBlockContent = [CodeExecutionToolResultError](/docs/en/api/messages#code_execution_tool_result_error) { error_code, type } \| [CodeExecutionResultBlock](/docs/en/api/messages#code_execution_result_block) { content, return_code, stderr, 2 more } \| [EncryptedCodeExecutionResultBlock](/docs/en/api/messages#encrypted_code_execution_result_block) { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

CodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultErrorParam { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlockParam { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

CodeExecutionToolResultBlockParamContent = [CodeExecutionToolResultErrorParam](/docs/en/api/messages#code_execution_tool_result_error_param) { error_code, type } \| [CodeExecutionResultBlockParam](/docs/en/api/messages#code_execution_result_block_param) { content, return_code, stderr, 2 more } \| [EncryptedCodeExecutionResultBlockParam](/docs/en/api/messages#encrypted_code_execution_result_block_param) { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultErrorParam { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlockParam { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionToolResultErrorCode = "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

CodeExecutionToolResultErrorParam { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Container { id, expires_at }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

ContainerUploadBlockParam { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ContentBlock = [TextBlock](/docs/en/api/messages#text_block) { citations, text, type } \| [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type } \| [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type } \| 9 more

Response model for a file uploaded to the container.

Accepts one of the following:

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

ContentBlockParam = [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \| 13 more

Regular text content.

Accepts one of the following:

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

ThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

ToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

ToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| 2 more\>

Accepts one of the following:

string

Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| 2 more\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

ToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ServerToolUseBlockParam { id, input, name, 3 more }

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

WebSearchToolResultBlockParam { content, tool_use_id, type, 2 more }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age?: string \| null

WebSearchToolRequestError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

WebFetchToolResultBlockParam { content, tool_use_id, type, 2 more }

content: [WebFetchToolResultErrorBlockParam](/docs/en/api/messages#web_fetch_tool_result_error_block_param) { error_code, type } \| [WebFetchBlockParam](/docs/en/api/messages#web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

WebFetchToolResultErrorBlockParam { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlockParam { content, type, url, retrieved_at }

content: [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

type: "web_fetch_result"

url: string

Fetched content URL

retrieved_at?: string \| null

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

CodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultErrorParam { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlockParam { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BashCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BashCodeExecutionToolResultErrorParam](/docs/en/api/messages#bash_code_execution_tool_result_error_param) { error_code, type } \| [BashCodeExecutionResultBlockParam](/docs/en/api/messages#bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

TextEditorCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [TextEditorCodeExecutionToolResultErrorParam](/docs/en/api/messages#text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } \| [TextEditorCodeExecutionViewResultBlockParam](/docs/en/api/messages#text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } \| [TextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/messages#text_editor_code_execution_create_result_block_param) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

error_message?: string \| null

TextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

num_lines?: number \| null

start_line?: number \| null

total_lines?: number \| null

TextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

lines?: Array\<string\> \| null

new_lines?: number \| null

new_start?: number \| null

old_lines?: number \| null

old_start?: number \| null

tool_use_id: string

type: "text_editor_code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ToolSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [ToolSearchToolResultErrorParam](/docs/en/api/messages#tool_search_tool_result_error_param) { error_code, type } \| [ToolSearchToolSearchResultBlockParam](/docs/en/api/messages#tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultErrorParam { error_code, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\<[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param) { tool_name, type, cache_control } \>

tool_name: string

type: "tool_reference"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

tool_use_id: string

type: "tool_search_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ContainerUploadBlockParam { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ContentBlockSourceContent = [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control }

Accepts one of the following:

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

DocumentBlock { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

EncryptedCodeExecutionResultBlockParam { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

InputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

JSONOutputFormat { schema, type }

schema: Record\<string, unknown\>

The JSON schema of the format

type: "json_schema"

MemoryTool20250818 { name, type, allowed_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory_20250818"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

Message { id, container, content, 6 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](/docs/en/api/messages#container) { id, expires_at } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-sonnet-4-6" \| "claude-opus-4-5-20251101" \| 19 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

MessageCountTokensTool = [Tool](/docs/en/api/messages#tool) { input_schema, name, allowed_callers, 7 more } \| [ToolBash20250124](/docs/en/api/messages#tool_bash_20250124) { name, type, allowed_callers, 4 more } \| [CodeExecutionTool20250522](/docs/en/api/messages#code_execution_tool_20250522) { name, type, allowed_callers, 3 more } \| 12 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

Tool { input_schema, name, allowed_callers, 7 more }

input_schema: InputSchema { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties?: Record\<string, unknown\> \| null

required?: Array\<string\> \| null

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolBash20250124 { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionTool20250522 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250522"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionTool20250825 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250825"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionTool20260120 { name, type, allowed_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20260120"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

MemoryTool20250818 { name, type, allowed_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory_20250818"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250124 { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250429 { name, type, allowed_callers, 4 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250429"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250728 { name, type, allowed_callers, 5 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250728"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

WebSearchTool20250305 { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20250305"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more } \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string \| null

The city of the user.

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string \| null

The region of the user.

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

WebFetchTool20250910 { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20250910"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

List of domains to allow fetching from

blocked_domains?: Array\<string\> \| null

List of domains to block fetching from

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens?: number \| null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

WebSearchTool20260209 { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20260209"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more } \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string \| null

The city of the user.

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string \| null

The region of the user.

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

WebFetchTool20260209 { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20260209"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

List of domains to allow fetching from

blocked_domains?: Array\<string\> \| null

List of domains to block fetching from

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens?: number \| null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolSearchToolBm25_20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_bm25_20251119" \| "tool_search_tool_bm25"

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolSearchToolRegex20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_regex_20251119" \| "tool_search_tool_regex"

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

MessageDeltaUsage { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

input_tokens: number \| null

The cumulative number of input tokens which were used.

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

MessageParam { content, role }

content: string \| Array\<[ContentBlockParam](/docs/en/api/messages#content_block_param)\>

Accepts one of the following:

string

Array\<[ContentBlockParam](/docs/en/api/messages#content_block_param)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

ThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

ToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

ToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| 2 more\>

Accepts one of the following:

string

Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| 2 more\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

ToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ServerToolUseBlockParam { id, input, name, 3 more }

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

WebSearchToolResultBlockParam { content, tool_use_id, type, 2 more }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age?: string \| null

WebSearchToolRequestError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

WebFetchToolResultBlockParam { content, tool_use_id, type, 2 more }

content: [WebFetchToolResultErrorBlockParam](/docs/en/api/messages#web_fetch_tool_result_error_block_param) { error_code, type } \| [WebFetchBlockParam](/docs/en/api/messages#web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

WebFetchToolResultErrorBlockParam { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlockParam { content, type, url, retrieved_at }

content: [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

type: "web_fetch_result"

url: string

Fetched content URL

retrieved_at?: string \| null

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

CodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultErrorParam { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlockParam { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BashCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BashCodeExecutionToolResultErrorParam](/docs/en/api/messages#bash_code_execution_tool_result_error_param) { error_code, type } \| [BashCodeExecutionResultBlockParam](/docs/en/api/messages#bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

TextEditorCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [TextEditorCodeExecutionToolResultErrorParam](/docs/en/api/messages#text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } \| [TextEditorCodeExecutionViewResultBlockParam](/docs/en/api/messages#text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } \| [TextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/messages#text_editor_code_execution_create_result_block_param) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

error_message?: string \| null

TextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

num_lines?: number \| null

start_line?: number \| null

total_lines?: number \| null

TextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

lines?: Array\<string\> \| null

new_lines?: number \| null

new_start?: number \| null

old_lines?: number \| null

old_start?: number \| null

tool_use_id: string

type: "text_editor_code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ToolSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [ToolSearchToolResultErrorParam](/docs/en/api/messages#tool_search_tool_result_error_param) { error_code, type } \| [ToolSearchToolSearchResultBlockParam](/docs/en/api/messages#tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultErrorParam { error_code, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\<[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param) { tool_name, type, cache_control } \>

tool_name: string

type: "tool_reference"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

tool_use_id: string

type: "tool_search_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ContainerUploadBlockParam { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

MessageTokensCount { input_tokens }

input_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

Metadata { user_id }

user_id?: string \| null

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

Model = "claude-opus-4-6" \| "claude-sonnet-4-6" \| "claude-opus-4-5-20251101" \| 19 more \| (string & {})

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-sonnet-4-6" \| "claude-opus-4-5-20251101" \| 19 more

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

(string & {})

OutputConfig { effort, format }

effort?: "low" \| "medium" \| "high" \| "max" \| null

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format?: [JSONOutputFormat](/docs/en/api/messages#json_output_format) { schema, type } \| null

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: Record\<string, unknown\>

The JSON schema of the format

type: "json_schema"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

RawContentBlockDelta = [TextDelta](/docs/en/api/messages#text_delta) { text, type } \| [InputJSONDelta](/docs/en/api/messages#input_json_delta) { partial_json, type } \| [CitationsDelta](/docs/en/api/messages#citations_delta) { citation, type } \| 2 more

Accepts one of the following:

TextDelta { text, type }

text: string

type: "text_delta"

InputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

type: "citations_delta"

ThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

SignatureDelta { signature, type }

signature: string

type: "signature_delta"

RawContentBlockDeltaEvent { delta, index, type }

delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

TextDelta { text, type }

text: string

type: "text_delta"

InputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

type: "citations_delta"

ThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

SignatureDelta { signature, type }

signature: string

type: "signature_delta"

index: number

type: "content_block_delta"

RawContentBlockStartEvent { content_block, index, type }

content_block: [TextBlock](/docs/en/api/messages#text_block) { citations, text, type } \| [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type } \| [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type } \| 9 more

Response model for a file uploaded to the container.

Accepts one of the following:

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

index: number

type: "content_block_start"

RawContentBlockStopEvent { index, type }

index: number

type: "content_block_stop"

RawMessageDeltaEvent { delta, type, usage }

delta: Delta { container, stop_reason, stop_sequence }

container: [Container](/docs/en/api/messages#container) { id, expires_at } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

type: "message_delta"

usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

input_tokens: number \| null

The cumulative number of input tokens which were used.

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

RawMessageStartEvent { message, type }

message: [Message](/docs/en/api/messages#message) { id, container, content, 6 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](/docs/en/api/messages#container) { id, expires_at } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-sonnet-4-6" \| "claude-opus-4-5-20251101" \| 19 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "message_start"

RawMessageStopEvent { type }

type: "message_stop"

RawMessageStreamEvent = [RawMessageStartEvent](/docs/en/api/messages#raw_message_start_event) { message, type } \| [RawMessageDeltaEvent](/docs/en/api/messages#raw_message_delta_event) { delta, type, usage } \| [RawMessageStopEvent](/docs/en/api/messages#raw_message_stop_event) { type } \| 3 more

Accepts one of the following:

RawMessageStartEvent { message, type }

message: [Message](/docs/en/api/messages#message) { id, container, content, 6 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](/docs/en/api/messages#container) { id, expires_at } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-sonnet-4-6" \| "claude-opus-4-5-20251101" \| 19 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "message_start"

RawMessageDeltaEvent { delta, type, usage }

delta: Delta { container, stop_reason, stop_sequence }

container: [Container](/docs/en/api/messages#container) { id, expires_at } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

type: "message_delta"

usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

input_tokens: number \| null

The cumulative number of input tokens which were used.

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

RawMessageStopEvent { type }

type: "message_stop"

RawContentBlockStartEvent { content_block, index, type }

content_block: [TextBlock](/docs/en/api/messages#text_block) { citations, text, type } \| [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type } \| [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type } \| 9 more

Response model for a file uploaded to the container.

Accepts one of the following:

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

index: number

type: "content_block_start"

RawContentBlockDeltaEvent { delta, index, type }

delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

TextDelta { text, type }

text: string

type: "text_delta"

InputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

type: "citations_delta"

ThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

SignatureDelta { signature, type }

signature: string

type: "signature_delta"

index: number

type: "content_block_delta"

RawContentBlockStopEvent { index, type }

index: number

type: "content_block_stop"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

RedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

ServerToolUsage { web_fetch_requests, web_search_requests }

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

ServerToolUseBlockParam { id, input, name, 3 more }

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

SignatureDelta { signature, type }

signature: string

type: "signature_delta"

StopReason = "end_turn" \| "max_tokens" \| "stop_sequence" \| 3 more

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

TextCitation = [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

TextCitationParam = [CitationCharLocationParam](/docs/en/api/messages#citation_char_location_param) { cited_text, document_index, document_title, 3 more } \| [CitationPageLocationParam](/docs/en/api/messages#citation_page_location_param) { cited_text, document_index, document_title, 3 more } \| [CitationContentBlockLocationParam](/docs/en/api/messages#citation_content_block_location_param) { cited_text, document_index, document_title, 3 more } \| 2 more

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

TextDelta { text, type }

text: string

type: "text_delta"

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

TextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

lines?: Array\<string\> \| null

new_lines?: number \| null

new_start?: number \| null

old_lines?: number \| null

old_start?: number \| null

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [TextEditorCodeExecutionToolResultErrorParam](/docs/en/api/messages#text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } \| [TextEditorCodeExecutionViewResultBlockParam](/docs/en/api/messages#text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } \| [TextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/messages#text_editor_code_execution_create_result_block_param) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

error_message?: string \| null

TextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

num_lines?: number \| null

start_line?: number \| null

total_lines?: number \| null

TextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

lines?: Array\<string\> \| null

new_lines?: number \| null

new_start?: number \| null

old_lines?: number \| null

old_start?: number \| null

tool_use_id: string

type: "text_editor_code_execution_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionToolResultErrorCode = "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

TextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

error_message?: string \| null

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: string

file_type: "text" \| "image" \| "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

num_lines?: number \| null

start_line?: number \| null

total_lines?: number \| null

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

ThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

ThinkingConfigAdaptive { type }

type: "adaptive"

ThinkingConfigDisabled { type }

type: "disabled"

ThinkingConfigEnabled { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

ThinkingConfigParam = [ThinkingConfigEnabled](/docs/en/api/messages#thinking_config_enabled) { budget_tokens, type } \| [ThinkingConfigDisabled](/docs/en/api/messages#thinking_config_disabled) { type } \| [ThinkingConfigAdaptive](/docs/en/api/messages#thinking_config_adaptive) { type }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

ThinkingConfigEnabled { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

ThinkingConfigDisabled { type }

type: "disabled"

ThinkingConfigAdaptive { type }

type: "adaptive"

ThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Tool { input_schema, name, allowed_callers, 7 more }

input_schema: InputSchema { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties?: Record\<string, unknown\> \| null

required?: Array\<string\> \| null

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolBash20250124 { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolChoice = [ToolChoiceAuto](/docs/en/api/messages#tool_choice_auto) { type, disable_parallel_tool_use } \| [ToolChoiceAny](/docs/en/api/messages#tool_choice_any) { type, disable_parallel_tool_use } \| [ToolChoiceTool](/docs/en/api/messages#tool_choice_tool) { name, type, disable_parallel_tool_use } \| [ToolChoiceNone](/docs/en/api/messages#tool_choice_none) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

ToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

ToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolChoiceNone { type }

The model will not be allowed to use tools.

type: "none"

ToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

ToolChoiceNone { type }

The model will not be allowed to use tools.

type: "none"

ToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolReferenceBlock { tool_name, type }

tool_name: string

type: "tool_reference"

ToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| 2 more\>

Accepts one of the following:

string

Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| 2 more\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

source: string

title: string

type: "search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

ToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolSearchToolBm25_20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_bm25_20251119" \| "tool_search_tool_bm25"

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolSearchToolRegex20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_regex_20251119" \| "tool_search_tool_regex"

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ToolSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [ToolSearchToolResultErrorParam](/docs/en/api/messages#tool_search_tool_result_error_param) { error_code, type } \| [ToolSearchToolSearchResultBlockParam](/docs/en/api/messages#tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultErrorParam { error_code, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\<[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param) { tool_name, type, cache_control } \>

tool_name: string

type: "tool_reference"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

tool_use_id: string

type: "tool_search_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolResultErrorCode = "invalid_tool_input" \| "unavailable" \| "too_many_requests" \| "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

ToolSearchToolResultErrorParam { error_code, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

ToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\<[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param) { tool_name, type, cache_control } \>

tool_name: string

type: "tool_reference"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250124 { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250429 { name, type, allowed_callers, 4 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250429"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250728 { name, type, allowed_callers, 5 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250728"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolUnion = [Tool](/docs/en/api/messages#tool) { input_schema, name, allowed_callers, 7 more } \| [ToolBash20250124](/docs/en/api/messages#tool_bash_20250124) { name, type, allowed_callers, 4 more } \| [CodeExecutionTool20250522](/docs/en/api/messages#code_execution_tool_20250522) { name, type, allowed_callers, 3 more } \| 12 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

Tool { input_schema, name, allowed_callers, 7 more }

input_schema: InputSchema { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties?: Record\<string, unknown\> \| null

required?: Array\<string\> \| null

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolBash20250124 { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionTool20250522 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250522"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionTool20250825 { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20250825"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

CodeExecutionTool20260120 { name, type, allowed_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code_execution_20260120"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

MemoryTool20250818 { name, type, allowed_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory_20250818"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250124 { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250124"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250429 { name, type, allowed_callers, 4 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250429"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolTextEditor20250728 { name, type, allowed_callers, 5 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text_editor_20250728"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

WebSearchTool20250305 { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20250305"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more } \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string \| null

The city of the user.

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string \| null

The region of the user.

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

WebFetchTool20250910 { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20250910"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

List of domains to allow fetching from

blocked_domains?: Array\<string\> \| null

List of domains to block fetching from

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens?: number \| null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

WebSearchTool20260209 { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20260209"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more } \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string \| null

The city of the user.

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string \| null

The region of the user.

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

WebFetchTool20260209 { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20260209"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

List of domains to allow fetching from

blocked_domains?: Array\<string\> \| null

List of domains to block fetching from

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens?: number \| null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolSearchToolBm25_20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_bm25_20251119" \| "tool_search_tool_bm25"

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolSearchToolRegex20251119 { name, type, allowed_callers, 3 more }

name: "tool_search_tool_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool_search_tool_regex_20251119" \| "tool_search_tool_regex"

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ToolUseBlockParam { id, input, name, 3 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

URLImageSource { type, url }

type: "url"

url: string

URLPDFSource { type, url }

type: "url"

url: string

Usage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

UserLocation { type, city, country, 2 more }

type: "approximate"

city?: string \| null

The city of the user.

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string \| null

The region of the user.

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

WebFetchBlockParam { content, type, url, retrieved_at }

content: [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

type: "web_fetch_result"

url: string

Fetched content URL

retrieved_at?: string \| null

ISO 8601 timestamp when the content was retrieved

WebFetchTool20250910 { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20250910"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

List of domains to allow fetching from

blocked_domains?: Array\<string\> \| null

List of domains to block fetching from

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens?: number \| null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

WebFetchTool20260209 { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_fetch_20260209"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

List of domains to allow fetching from

blocked_domains?: Array\<string\> \| null

List of domains to block fetching from

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

Citations configuration for fetched documents. Citations are disabled by default.

enabled?: boolean

defer_loading?: boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens?: number \| null

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

WebFetchToolResultBlockParam { content, tool_use_id, type, 2 more }

content: [WebFetchToolResultErrorBlockParam](/docs/en/api/messages#web_fetch_tool_result_error_block_param) { error_code, type } \| [WebFetchBlockParam](/docs/en/api/messages#web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

WebFetchToolResultErrorBlockParam { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlockParam { content, type, url, retrieved_at }

content: [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

URLImageSource { type, url }

type: "url"

url: string

type: "image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

URLPDFSource { type, url }

type: "url"

url: string

type: "document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

type: "web_fetch_result"

url: string

Fetched content URL

retrieved_at?: string \| null

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchToolResultErrorBlockParam { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchToolResultErrorCode = "invalid_tool_input" \| "url_too_long" \| "url_not_allowed" \| 5 more

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

WebSearchResultBlock { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

WebSearchResultBlockParam { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age?: string \| null

WebSearchTool20250305 { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20250305"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more } \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string \| null

The city of the user.

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string \| null

The region of the user.

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

WebSearchTool20260209 { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web_search_20260209"

allowed_callers?: Array\<"direct" \| "code_execution_20250825" \| "code_execution_20260120"\>

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

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

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more } \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city?: string \| null

The city of the user.

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region?: string \| null

The region of the user.

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

WebSearchToolRequestError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebSearchToolResultBlockContent = [WebSearchToolResultError](/docs/en/api/messages#web_search_tool_result_error) { error_code, type } \| Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

WebSearchToolResultBlockParam { content, tool_use_id, type, 2 more }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age?: string \| null

WebSearchToolRequestError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller?: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

WebSearchToolResultBlockParamContent = Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \> \| [WebSearchToolRequestError](/docs/en/api/messages#web_search_tool_request_error) { error_code, type }

Accepts one of the following:

Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

url: string

page_age?: string \| null

WebSearchToolRequestError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

WebSearchToolResultErrorCode = "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

client.messages.batches.create(BatchCreateParams { requests } body, RequestOptionsoptions?): [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

client.messages.batches.retrieve(stringmessageBatchID, RequestOptionsoptions?): [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

client.messages.batches.list(BatchListParams { after_id, before_id, limit } query?, RequestOptionsoptions?): Page\<[MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more } \>

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

client.messages.batches.cancel(stringmessageBatchID, RequestOptionsoptions?): [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

client.messages.batches.delete(stringmessageBatchID, RequestOptionsoptions?): [DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch) { id, type }

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

client.messages.batches.results(stringmessageBatchID, RequestOptionsoptions?): [MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response) { custom_id, result } \| Stream\<[MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response) { custom_id, result } \>

GET/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

DeletedMessageBatch { id, type }

id: string

ID of the Message Batch.

type: "message_batch_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

MessageBatch { id, archived_at, cancel_initiated_at, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

archived_at: string \| null

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel_initiated_at: string \| null

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.

ended_at: string \| null

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

processing_status: "in_progress" \| "canceling" \| "ended"

Processing status of the Message Batch.

Accepts one of the following:

"in_progress"

"canceling"

"ended"

request_counts: [MessageBatchRequestCounts](/docs/en/api/messages#message_batch_request_counts) { canceled, errored, expired, 2 more }

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

MessageBatchCanceledResult { type }

type: "canceled"

MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

InvalidRequestError { message, type }

message: string

type: "invalid_request_error"

AuthenticationError { message, type }

message: string

type: "authentication_error"

BillingError { message, type }

message: string

type: "billing_error"

PermissionError { message, type }

message: string

type: "permission_error"

NotFoundError { message, type }

message: string

type: "not_found_error"

RateLimitError { message, type }

message: string

type: "rate_limit_error"

GatewayTimeoutError { message, type }

message: string

type: "timeout_error"

APIErrorObject { message, type }

message: string

type: "api_error"

OverloadedError { message, type }

message: string

type: "overloaded_error"

request_id: string \| null

type: "error"

type: "errored"

MessageBatchExpiredResult { type }

type: "expired"

MessageBatchIndividualResponse { custom_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [MessageBatchResult](/docs/en/api/messages#message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, container, content, 6 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](/docs/en/api/messages#container) { id, expires_at } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-sonnet-4-6" \| "claude-opus-4-5-20251101" \| 19 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

InvalidRequestError { message, type }

message: string

type: "invalid_request_error"

AuthenticationError { message, type }

message: string

type: "authentication_error"

BillingError { message, type }

message: string

type: "billing_error"

PermissionError { message, type }

message: string

type: "permission_error"

NotFoundError { message, type }

message: string

type: "not_found_error"

RateLimitError { message, type }

message: string

type: "rate_limit_error"

GatewayTimeoutError { message, type }

message: string

type: "timeout_error"

APIErrorObject { message, type }

message: string

type: "api_error"

OverloadedError { message, type }

message: string

type: "overloaded_error"

request_id: string \| null

type: "error"

type: "errored"

MessageBatchCanceledResult { type }

type: "canceled"

MessageBatchExpiredResult { type }

type: "expired"

MessageBatchRequestCounts { canceled, errored, expired, 2 more }

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

MessageBatchResult = [MessageBatchSucceededResult](/docs/en/api/messages#message_batch_succeeded_result) { message, type } \| [MessageBatchErroredResult](/docs/en/api/messages#message_batch_errored_result) { error, type } \| [MessageBatchCanceledResult](/docs/en/api/messages#message_batch_canceled_result) { type } \| [MessageBatchExpiredResult](/docs/en/api/messages#message_batch_expired_result) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, container, content, 6 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](/docs/en/api/messages#container) { id, expires_at } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-sonnet-4-6" \| "claude-opus-4-5-20251101" \| 19 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

InvalidRequestError { message, type }

message: string

type: "invalid_request_error"

AuthenticationError { message, type }

message: string

type: "authentication_error"

BillingError { message, type }

message: string

type: "billing_error"

PermissionError { message, type }

message: string

type: "permission_error"

NotFoundError { message, type }

message: string

type: "not_found_error"

RateLimitError { message, type }

message: string

type: "rate_limit_error"

GatewayTimeoutError { message, type }

message: string

type: "timeout_error"

APIErrorObject { message, type }

message: string

type: "api_error"

OverloadedError { message, type }

message: string

type: "overloaded_error"

request_id: string \| null

type: "error"

type: "errored"

MessageBatchCanceledResult { type }

type: "canceled"

MessageBatchExpiredResult { type }

type: "expired"

MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, container, content, 6 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](/docs/en/api/messages#container) { id, expires_at } \| null

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires_at: string

The time at which the container will expire.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

text: string

type: "text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

ToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

input: Record\<string, unknown\>

name: string

type: "tool_use"

ServerToolUseBlock { id, caller, input, 2 more }

id: string

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

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

WebSearchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

WebFetchToolResultBlock { caller, content, tool_use_id, type }

caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

DirectCaller { type }

Tool invocation directly from the model.

type: "direct"

ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

ServerToolCaller20260120 { tool_id, type }

tool_id: string

type: "code_execution_20260120"

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

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

WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled } \| null

Citation configuration for the document

enabled: boolean

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

type: "base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

type: "text"

title: string \| null

The title of the document

type: "document"

retrieved_at: string \| null

ISO 8601 timestamp when the content was retrieved

type: "web_fetch_result"

url: string

Fetched content URL

tool_use_id: string

type: "web_fetch_tool_result"

CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \>

file_id: string

type: "code_execution_output"

encrypted_stdout: string

return_code: number

stderr: string

type: "encrypted_code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \>

file_id: string

type: "bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: string \| null

type: "text_editor_code_execution_tool_result_error"

TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\<string\> \| null

new_lines: number \| null

new_start: number \| null

old_lines: number \| null

old_start: number \| null

type: "text_editor_code_execution_str_replace_result"

tool_use_id: string

type: "text_editor_code_execution_tool_result"

ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: string \| null

type: "tool_search_tool_result_error"

ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \>

tool_name: string

type: "tool_reference"

type: "tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: string

type: "container_upload"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-sonnet-4-6" \| "claude-opus-4-5-20251101" \| 19 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

output_tokens: number

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } \| null

The number of server tool requests.

web_fetch_requests: number

The number of web fetch tool requests.

web_search_requests: number

The number of web search tool requests.

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.
