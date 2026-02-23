---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:33:39Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/messages/batches"
title: "Batches - Claude API Reference"
---

Copy page

TypeScript

# Batches

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

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

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
