---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:41:48Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/messages/batches"
title: "Batches - Claude API Reference"
---

Copy page

Python

# Batches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

beta.messages.batches.create(BatchCreateParams\*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch)

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

beta.messages.batches.retrieve(strmessage_batch_id, BatchRetrieveParams\*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch)

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

beta.messages.batches.list(BatchListParams\*\*kwargs) -\> SyncPage\[[BetaMessageBatch](/docs/en/api/beta#beta_message_batch)\]

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

beta.messages.batches.cancel(strmessage_batch_id, BatchCancelParams\*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch)

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

beta.messages.batches.delete(strmessage_batch_id, BatchDeleteParams\*\*kwargs) -\> [BetaDeletedMessageBatch](/docs/en/api/beta#beta_deleted_message_batch)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

beta.messages.batches.results(strmessage_batch_id, BatchResultsParams\*\*kwargs) -\> [BetaMessageBatchIndividualResponse](/docs/en/api/beta#beta_message_batch_individual_response)

GET/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class BetaDeletedMessageBatch: …

id: str

ID of the Message Batch.

type: Literal\["message_batch_deleted"\]

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class BetaMessageBatch: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

archived_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel_initiated_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch was created.

ended_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

processing_status: Literal\["in_progress", "canceling", "ended"\]

Processing status of the Message Batch.

Accepts one of the following:

"in_progress"

"canceling"

"ended"

request_counts: [BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.

succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results_url: Optional\[str\]

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: Literal\["message_batch"\]

Object type.

For Message Batches, this is always `"message_batch"`.

class BetaMessageBatchCanceledResult: …

type: Literal\["canceled"\]

class BetaMessageBatchErroredResult: …

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

class BetaAuthenticationError: …

message: str

type: Literal\["authentication_error"\]

class BetaBillingError: …

message: str

type: Literal\["billing_error"\]

class BetaPermissionError: …

message: str

type: Literal\["permission_error"\]

class BetaNotFoundError: …

message: str

type: Literal\["not_found_error"\]

class BetaRateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

class BetaGatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

class BetaAPIError: …

message: str

type: Literal\["api_error"\]

class BetaOverloadedError: …

message: str

type: Literal\["overloaded_error"\]

request_id: Optional\[str\]

type: Literal\["error"\]

type: Literal\["errored"\]

class BetaMessageBatchExpiredResult: …

type: Literal\["expired"\]

class BetaMessageBatchIndividualResponse: …

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: str

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult: …

message: [BetaMessage](/docs/en/api/beta#beta_message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

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

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

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

type: Literal\["web_fetch_tool_result_error"\]

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web_search results.

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

encrypted_stdout: str

return_code: int

stderr: str

type: Literal\["encrypted_code_execution_result"\]

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

type: Literal\["tool_search_tool_search_result"\]

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

str

List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

cleared_tool_uses: int

Number of tool uses that were cleared.

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

cleared_thinking_turns: int

Number of thinking turns that were cleared.

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal\["claude-opus-4-6", "claude-sonnet-4-6", "claude-opus-4-5-20251101", 19 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Frontier intelligence at scale — built for coding, agents, and enterprise workflows
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

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

str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: Optional\[BetaStopReason\]

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

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

iterations: Optional\[BetaIterationsUsage\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

cache_read_input_tokens: int

The number of input tokens read from the cache.

input_tokens: int

The number of input tokens which were used.

output_tokens: int

The number of output tokens which were used.

type: Literal\["message"\]

Usage for a sampling iteration

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

cache_read_input_tokens: int

The number of input tokens read from the cache.

input_tokens: int

The number of input tokens which were used.

output_tokens: int

The number of output tokens which were used.

type: Literal\["compaction"\]

Usage for a compaction iteration

output_tokens: int

The number of output tokens which were used.

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

web_search_requests: int

The number of web search tool requests.

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: Optional\[Literal\["standard", "fast"\]\]

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: Literal\["succeeded"\]

class BetaMessageBatchErroredResult: …

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

class BetaAuthenticationError: …

message: str

type: Literal\["authentication_error"\]

class BetaBillingError: …

message: str

type: Literal\["billing_error"\]

class BetaPermissionError: …

message: str

type: Literal\["permission_error"\]

class BetaNotFoundError: …

message: str

type: Literal\["not_found_error"\]

class BetaRateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

class BetaGatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

class BetaAPIError: …

message: str

type: Literal\["api_error"\]

class BetaOverloadedError: …

message: str

type: Literal\["overloaded_error"\]

request_id: Optional\[str\]

type: Literal\["error"\]

type: Literal\["errored"\]

class BetaMessageBatchCanceledResult: …

type: Literal\["canceled"\]

class BetaMessageBatchExpiredResult: …

type: Literal\["expired"\]

class BetaMessageBatchRequestCounts: …

canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.

succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

[BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult: …

message: [BetaMessage](/docs/en/api/beta#beta_message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

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

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

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

type: Literal\["web_fetch_tool_result_error"\]

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web_search results.

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

encrypted_stdout: str

return_code: int

stderr: str

type: Literal\["encrypted_code_execution_result"\]

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

type: Literal\["tool_search_tool_search_result"\]

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

str

List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

cleared_tool_uses: int

Number of tool uses that were cleared.

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

cleared_thinking_turns: int

Number of thinking turns that were cleared.

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal\["claude-opus-4-6", "claude-sonnet-4-6", "claude-opus-4-5-20251101", 19 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Frontier intelligence at scale — built for coding, agents, and enterprise workflows
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

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

str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: Optional\[BetaStopReason\]

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

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

iterations: Optional\[BetaIterationsUsage\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

cache_read_input_tokens: int

The number of input tokens read from the cache.

input_tokens: int

The number of input tokens which were used.

output_tokens: int

The number of output tokens which were used.

type: Literal\["message"\]

Usage for a sampling iteration

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

cache_read_input_tokens: int

The number of input tokens read from the cache.

input_tokens: int

The number of input tokens which were used.

output_tokens: int

The number of output tokens which were used.

type: Literal\["compaction"\]

Usage for a compaction iteration

output_tokens: int

The number of output tokens which were used.

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

web_search_requests: int

The number of web search tool requests.

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: Optional\[Literal\["standard", "fast"\]\]

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: Literal\["succeeded"\]

class BetaMessageBatchErroredResult: …

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

class BetaAuthenticationError: …

message: str

type: Literal\["authentication_error"\]

class BetaBillingError: …

message: str

type: Literal\["billing_error"\]

class BetaPermissionError: …

message: str

type: Literal\["permission_error"\]

class BetaNotFoundError: …

message: str

type: Literal\["not_found_error"\]

class BetaRateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

class BetaGatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

class BetaAPIError: …

message: str

type: Literal\["api_error"\]

class BetaOverloadedError: …

message: str

type: Literal\["overloaded_error"\]

request_id: Optional\[str\]

type: Literal\["error"\]

type: Literal\["errored"\]

class BetaMessageBatchCanceledResult: …

type: Literal\["canceled"\]

class BetaMessageBatchExpiredResult: …

type: Literal\["expired"\]

class BetaMessageBatchSucceededResult: …

message: [BetaMessage](/docs/en/api/beta#beta_message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

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

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

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

type: Literal\["web_fetch_tool_result_error"\]

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class BetaServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web_search results.

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

encrypted_stdout: str

return_code: int

stderr: str

type: Literal\["encrypted_code_execution_result"\]

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

type: Literal\["tool_search_tool_search_result"\]

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

str

List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

cleared_tool_uses: int

Number of tool uses that were cleared.

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

cleared_thinking_turns: int

Number of thinking turns that were cleared.

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal\["claude-opus-4-6", "claude-sonnet-4-6", "claude-opus-4-5-20251101", 19 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Frontier intelligence at scale — built for coding, agents, and enterprise workflows
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

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

str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: Optional\[BetaStopReason\]

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

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

iterations: Optional\[BetaIterationsUsage\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

cache_read_input_tokens: int

The number of input tokens read from the cache.

input_tokens: int

The number of input tokens which were used.

output_tokens: int

The number of output tokens which were used.

type: Literal\["message"\]

Usage for a sampling iteration

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

cache_read_input_tokens: int

The number of input tokens read from the cache.

input_tokens: int

The number of input tokens which were used.

output_tokens: int

The number of output tokens which were used.

type: Literal\["compaction"\]

Usage for a compaction iteration

output_tokens: int

The number of output tokens which were used.

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

web_search_requests: int

The number of web search tool requests.

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

speed: Optional\[Literal\["standard", "fast"\]\]

The inference speed mode used for this request.

Accepts one of the following:

"standard"

"fast"

type: Literal\["succeeded"\]

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
