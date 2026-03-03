---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:04:20Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/beta/messages/batches"
title: "Batches - Claude API Reference"
---

# Batches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

beta.messages.batches.create(\*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch) { id, archived_at, cancel_initiated_at, 7 more }

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

beta.messages.batches.retrieve(message_batch_id, \*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch) { id, archived_at, cancel_initiated_at, 7 more }

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

beta.messages.batches.list(\*\*kwargs) -\> Page\<[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) { id, archived_at, cancel_initiated_at, 7 more } \>

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

beta.messages.batches.cancel(message_batch_id, \*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch) { id, archived_at, cancel_initiated_at, 7 more }

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

beta.messages.batches.delete(message_batch_id, \*\*kwargs) -\> [BetaDeletedMessageBatch](/docs/en/api/beta#beta_deleted_message_batch) { id, type }

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

beta.messages.batches.results(message_batch_id, \*\*kwargs) -\> [BetaMessageBatchIndividualResponse](/docs/en/api/beta#beta_message_batch_individual_response) { custom_id, result }

GET/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class BetaDeletedMessageBatch { id, type }

id: String

ID of the Message Batch.

type: :message_batch_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class BetaMessageBatch { id, archived_at, cancel_initiated_at, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

archived_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel_initiated_at: Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

ended_at: Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

processing_status: :in_progress \| :canceling \| :ended

Processing status of the Message Batch.

Accepts one of the following:

:in_progress

:canceling

:ended

request_counts: [BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts) { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.

succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results_url: String

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: :message_batch

Object type.

For Message Batches, this is always `"message_batch"`.

class BetaMessageBatchCanceledResult { type }

type: :canceled

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid_request_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication_error

class BetaBillingError { message, type }

message: String

type: :billing_error

class BetaPermissionError { message, type }

message: String

type: :permission_error

class BetaNotFoundError { message, type }

message: String

type: :not_found_error

class BetaRateLimitError { message, type }

message: String

type: :rate_limit_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout_error

class BetaAPIError { message, type }

message: String

type: :api_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded_error

request_id: String

type: :error

type: :errored

class BetaMessageBatchExpiredResult { type }

type: :expired

class BetaMessageBatchIndividualResponse { custom_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires_at: Time

The time at which the container will expire.

skills: Array\[[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \]

Skills loaded in the container

skill_id: String

Skill ID

type: :anthropic \| :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

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

class BetaTextBlock { citations, text, type }

citations: Array\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

class BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search \| :web_fetch \| :code_execution \| 4 more

Accepts one of the following:

:web_search

:web_fetch

:code_execution

:bash_code_execution

:text_editor_code_execution

:tool_search_tool_regex

:tool_search_tool_bm25

type: :server_tool_use

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaWebSearchToolResultBlock { content, tool_use_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Array\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaWebFetchToolResultBlock { content, tool_use_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:url_too_long

:url_not_allowed

:url_not_accessible

:unsupported_content_type

:too_many_requests

:max_uses_exceeded

:unavailable

type: :web_fetch_tool_result_error

class BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

type: :web_fetch_result

url: String

Fetched content URL

tool_use_id: String

type: :web_fetch_tool_result

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

class BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

encrypted_stdout: String

return_code: Integer

stderr: String

type: :encrypted_code_execution_result

tool_use_id: String

type: :code_execution_tool_result

class BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

class BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

error_message: String

type: :text_editor_code_execution_tool_result_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: String

file_type: :text \| :image \| :pdf

Accepts one of the following:

:text

:image

:pdf

num_lines: Integer

start_line: Integer

total_lines: Integer

type: :text_editor_code_execution_view_result

class BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

type: :text_editor_code_execution_str_replace_result

tool_use_id: String

type: :text_editor_code_execution_tool_result

class BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error_code, error_message, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| :execution_time_exceeded

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

error_message: String

type: :tool_search_tool_result_error

class BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \]

tool_name: String

type: :tool_reference

type: :tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

The name of the MCP tool

server_name: String

The name of the MCP server

type: :mcp_tool_use

class BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: String \| Array\[[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \]

Accepts one of the following:

String

Array\[[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \]

citations: Array\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

class BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

is_error: bool

tool_use_id: String

type: :mcp_tool_result

class BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: String

type: :container_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\[[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: Integer

Number of input tokens cleared by this edit.

cleared_tool_uses: Integer

Number of tool uses that were cleared.

type: :clear_tool_uses_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: Integer

Number of input tokens cleared by this edit.

cleared_thinking_turns: Integer

Number of thinking turns that were cleared.

type: :clear_thinking_20251015

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-sonnet-4-6" \| :"claude-opus-4-5-20251101" \| 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

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

:end_turn

:max_tokens

:stop_sequence

:tool_use

:pause_turn

:compaction

:refusal

:model_context_window_exceeded

stop_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

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

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

input_tokens: Integer

The number of input tokens which were used.

output_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

input_tokens: Integer

The number of input tokens which were used.

output_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output_tokens: Integer

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: Integer

The number of web fetch tool requests.

web_search_requests: Integer

The number of web search tool requests.

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard \| :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

type: :succeeded

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid_request_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication_error

class BetaBillingError { message, type }

message: String

type: :billing_error

class BetaPermissionError { message, type }

message: String

type: :permission_error

class BetaNotFoundError { message, type }

message: String

type: :not_found_error

class BetaRateLimitError { message, type }

message: String

type: :rate_limit_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout_error

class BetaAPIError { message, type }

message: String

type: :api_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded_error

request_id: String

type: :error

type: :errored

class BetaMessageBatchCanceledResult { type }

type: :canceled

class BetaMessageBatchExpiredResult { type }

type: :expired

class BetaMessageBatchRequestCounts { canceled, errored, expired, 2 more }

canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.

succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

BetaMessageBatchResult = [BetaMessageBatchSucceededResult](/docs/en/api/beta#beta_message_batch_succeeded_result) { message, type } \| [BetaMessageBatchErroredResult](/docs/en/api/beta#beta_message_batch_errored_result) { error, type } \| [BetaMessageBatchCanceledResult](/docs/en/api/beta#beta_message_batch_canceled_result) { type } \| [BetaMessageBatchExpiredResult](/docs/en/api/beta#beta_message_batch_expired_result) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires_at: Time

The time at which the container will expire.

skills: Array\[[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \]

Skills loaded in the container

skill_id: String

Skill ID

type: :anthropic \| :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

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

class BetaTextBlock { citations, text, type }

citations: Array\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

class BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search \| :web_fetch \| :code_execution \| 4 more

Accepts one of the following:

:web_search

:web_fetch

:code_execution

:bash_code_execution

:text_editor_code_execution

:tool_search_tool_regex

:tool_search_tool_bm25

type: :server_tool_use

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaWebSearchToolResultBlock { content, tool_use_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Array\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaWebFetchToolResultBlock { content, tool_use_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:url_too_long

:url_not_allowed

:url_not_accessible

:unsupported_content_type

:too_many_requests

:max_uses_exceeded

:unavailable

type: :web_fetch_tool_result_error

class BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

type: :web_fetch_result

url: String

Fetched content URL

tool_use_id: String

type: :web_fetch_tool_result

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

class BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

encrypted_stdout: String

return_code: Integer

stderr: String

type: :encrypted_code_execution_result

tool_use_id: String

type: :code_execution_tool_result

class BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

class BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

error_message: String

type: :text_editor_code_execution_tool_result_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: String

file_type: :text \| :image \| :pdf

Accepts one of the following:

:text

:image

:pdf

num_lines: Integer

start_line: Integer

total_lines: Integer

type: :text_editor_code_execution_view_result

class BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

type: :text_editor_code_execution_str_replace_result

tool_use_id: String

type: :text_editor_code_execution_tool_result

class BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error_code, error_message, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| :execution_time_exceeded

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

error_message: String

type: :tool_search_tool_result_error

class BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \]

tool_name: String

type: :tool_reference

type: :tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

The name of the MCP tool

server_name: String

The name of the MCP server

type: :mcp_tool_use

class BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: String \| Array\[[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \]

Accepts one of the following:

String

Array\[[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \]

citations: Array\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

class BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

is_error: bool

tool_use_id: String

type: :mcp_tool_result

class BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: String

type: :container_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\[[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: Integer

Number of input tokens cleared by this edit.

cleared_tool_uses: Integer

Number of tool uses that were cleared.

type: :clear_tool_uses_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: Integer

Number of input tokens cleared by this edit.

cleared_thinking_turns: Integer

Number of thinking turns that were cleared.

type: :clear_thinking_20251015

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-sonnet-4-6" \| :"claude-opus-4-5-20251101" \| 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

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

:end_turn

:max_tokens

:stop_sequence

:tool_use

:pause_turn

:compaction

:refusal

:model_context_window_exceeded

stop_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

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

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

input_tokens: Integer

The number of input tokens which were used.

output_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

input_tokens: Integer

The number of input tokens which were used.

output_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output_tokens: Integer

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: Integer

The number of web fetch tool requests.

web_search_requests: Integer

The number of web search tool requests.

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard \| :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

type: :succeeded

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response) { error, request_id, type }

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid_request_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication_error

class BetaBillingError { message, type }

message: String

type: :billing_error

class BetaPermissionError { message, type }

message: String

type: :permission_error

class BetaNotFoundError { message, type }

message: String

type: :not_found_error

class BetaRateLimitError { message, type }

message: String

type: :rate_limit_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout_error

class BetaAPIError { message, type }

message: String

type: :api_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded_error

request_id: String

type: :error

type: :errored

class BetaMessageBatchCanceledResult { type }

type: :canceled

class BetaMessageBatchExpiredResult { type }

type: :expired

class BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires_at: Time

The time at which the container will expire.

skills: Array\[[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \]

Skills loaded in the container

skill_id: String

Skill ID

type: :anthropic \| :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

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

class BetaTextBlock { citations, text, type }

citations: Array\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

class BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search \| :web_fetch \| :code_execution \| 4 more

Accepts one of the following:

:web_search

:web_fetch

:code_execution

:bash_code_execution

:text_editor_code_execution

:tool_search_tool_regex

:tool_search_tool_bm25

type: :server_tool_use

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaWebSearchToolResultBlock { content, tool_use_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Array\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaWebFetchToolResultBlock { content, tool_use_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:url_too_long

:url_not_allowed

:url_not_accessible

:unsupported_content_type

:too_many_requests

:max_uses_exceeded

:unavailable

type: :web_fetch_tool_result_error

class BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

type: :web_fetch_result

url: String

Fetched content URL

tool_use_id: String

type: :web_fetch_tool_result

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type } \| [BetaServerToolCaller20260120](/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class BetaServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

class BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

encrypted_stdout: String

return_code: Integer

stderr: String

type: :encrypted_code_execution_result

tool_use_id: String

type: :code_execution_tool_result

class BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

class BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

error_message: String

type: :text_editor_code_execution_tool_result_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: String

file_type: :text \| :image \| :pdf

Accepts one of the following:

:text

:image

:pdf

num_lines: Integer

start_line: Integer

total_lines: Integer

type: :text_editor_code_execution_view_result

class BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

type: :text_editor_code_execution_str_replace_result

tool_use_id: String

type: :text_editor_code_execution_tool_result

class BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error_code, error_message, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| :execution_time_exceeded

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

error_message: String

type: :tool_search_tool_result_error

class BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \]

tool_name: String

type: :tool_reference

type: :tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

The name of the MCP tool

server_name: String

The name of the MCP server

type: :mcp_tool_use

class BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: String \| Array\[[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \]

Accepts one of the following:

String

Array\[[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \]

citations: Array\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

class BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

is_error: bool

tool_use_id: String

type: :mcp_tool_result

class BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: String

type: :container_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\[[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: Integer

Number of input tokens cleared by this edit.

cleared_tool_uses: Integer

Number of tool uses that were cleared.

type: :clear_tool_uses_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: Integer

Number of input tokens cleared by this edit.

cleared_thinking_turns: Integer

Number of thinking turns that were cleared.

type: :clear_thinking_20251015

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-sonnet-4-6" \| :"claude-opus-4-5-20251101" \| 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

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

:end_turn

:max_tokens

:stop_sequence

:tool_use

:pause_turn

:compaction

:refusal

:model_context_window_exceeded

stop_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

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

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](/docs/en/api/beta#beta_iterations_usage) { , }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

input_tokens: Integer

The number of input tokens which were used.

output_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

input_tokens: Integer

The number of input tokens which were used.

output_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output_tokens: Integer

The number of output tokens which were used.

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: Integer

The number of web fetch tool requests.

web_search_requests: Integer

The number of web search tool requests.

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard \| :fast

The inference speed mode used for this request.
