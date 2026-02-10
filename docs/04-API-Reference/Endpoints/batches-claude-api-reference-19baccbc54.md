---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:08:53Z"
source_url: "https://platform.claude.com/docs/en/api/java/beta/messages/batches"
title: "Batches - Claude API Reference"
---

Copy page

Java

# Batches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) beta().messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

BatchListPage beta().messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) beta().messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

[BetaDeletedMessageBatch](/docs/en/api/beta#beta_deleted_message_batch) beta().messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

[BetaMessageBatchIndividualResponse](/docs/en/api/beta#beta_message_batch_individual_response) beta().messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class BetaDeletedMessageBatch:

String id

ID of the Message Batch.

JsonValue; type "message_batch_deleted"constant"message_batch_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

MESSAGE_BATCH_DELETED("message_batch_deleted")

class BetaMessageBatch:

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<LocalDateTime\> archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

Optional\<LocalDateTime\> cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

Optional\<LocalDateTime\> endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

LocalDateTime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

ProcessingStatus processingStatus

Processing status of the Message Batch.

Accepts one of the following:

IN_PROGRESS("in_progress")

CANCELING("canceling")

ENDED("ended")

[BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.

long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

Optional\<String\> resultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

JsonValue; type "message_batch"constant"message_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

MESSAGE_BATCH("message_batch")

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchErroredResult:

[BetaErrorResponse](/docs/en/api/beta#beta_error_response) error

[BetaError](/docs/en/api/beta#beta_error) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant"invalid_request_error"constant

Accepts one of the following:

INVALID_REQUEST_ERROR("invalid_request_error")

class BetaAuthenticationError:

String message

JsonValue; type "authentication_error"constant"authentication_error"constant

Accepts one of the following:

AUTHENTICATION_ERROR("authentication_error")

class BetaBillingError:

String message

JsonValue; type "billing_error"constant"billing_error"constant

Accepts one of the following:

BILLING_ERROR("billing_error")

class BetaPermissionError:

String message

JsonValue; type "permission_error"constant"permission_error"constant

Accepts one of the following:

PERMISSION_ERROR("permission_error")

class BetaNotFoundError:

String message

JsonValue; type "not_found_error"constant"not_found_error"constant

Accepts one of the following:

NOT_FOUND_ERROR("not_found_error")

class BetaRateLimitError:

String message

JsonValue; type "rate_limit_error"constant"rate_limit_error"constant

Accepts one of the following:

RATE_LIMIT_ERROR("rate_limit_error")

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant"timeout_error"constant

Accepts one of the following:

TIMEOUT_ERROR("timeout_error")

class BetaApiError:

String message

JsonValue; type "api_error"constant"api_error"constant

Accepts one of the following:

API_ERROR("api_error")

class BetaOverloadedError:

String message

JsonValue; type "overloaded_error"constant"overloaded_error"constant

Accepts one of the following:

OVERLOADED_ERROR("overloaded_error")

Optional\<String\> requestId

JsonValue; type "error"constant"error"constant

Accepts one of the following:

ERROR("error")

JsonValue; type "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

String customId

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult:

[BetaMessage](/docs/en/api/beta#beta_message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[BetaContainer](/docs/en/api/beta#beta_container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

formatdate-time

Optional\<List\<[BetaSkill](/docs/en/api/beta#beta_skill)\>\> skills

Skills loaded in the container

String skillId

Skill ID

maxLength64

minLength1

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

maxLength64

minLength1

List\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> content

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

class BetaTextBlock:

Optional\<List\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

WEB_SEARCH("web_search")

WEB_FETCH("web_fetch")

CODE_EXECUTION("code_execution")

BASH_CODE_EXECUTION("bash_code_execution")

TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant"web_search_tool_result_error"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")

List\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant"web_search_tool_result"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT("web_search_tool_result")

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant"web_fetch_tool_result_error"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")

class BetaWebFetchBlock:

[BetaDocumentBlock](/docs/en/api/beta#beta_document_block) content

Optional\<[BetaCitationConfig](/docs/en/api/beta#beta_citation_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<String\> title

The title of the document

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant"web_fetch_result"constant

Accepts one of the following:

WEB_FETCH_RESULT("web_fetch_result")

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant"web_fetch_tool_result"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) content

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCodeExecutionResultBlock:

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant"code_execution_output"constant

Accepts one of the following:

CODE_EXECUTION_OUTPUT("code_execution_output")

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant"code_execution_result"constant

Accepts one of the following:

CODE_EXECUTION_RESULT("code_execution_result")

String toolUseId

JsonValue; type "code_execution_tool_result"constant"code_execution_tool_result"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant"bash_code_execution_tool_result_error"constant

Accepts one of the following:

BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")

class BetaBashCodeExecutionResultBlock:

List\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant"bash_code_execution_output"constant

Accepts one of the following:

BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant"bash_code_execution_result"constant

Accepts one of the following:

BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant"bash_code_execution_tool_result"constant

Accepts one of the following:

BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant"text_editor_code_execution_tool_result_error"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant"text_editor_code_execution_view_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant"text_editor_code_execution_create_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant"text_editor_code_execution_str_replace_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant"text_editor_code_execution_tool_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant"tool_search_tool_result_error"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")

class BetaToolSearchToolSearchResultBlock:

List\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

JsonValue; type "tool_search_tool_search_result"constant"tool_search_tool_search_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")

String toolUseId

JsonValue; type "tool_search_tool_result"constant"tool_search_tool_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant"mcp_tool_use"constant

Accepts one of the following:

MCP_TOOL_USE("mcp_tool_use")

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

Optional\<List\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

boolean isError

String toolUseId

JsonValue; type "mcp_tool_result"constant"mcp_tool_result"constant

Accepts one of the following:

MCP_TOOL_RESULT("mcp_tool_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant"container_upload"constant

Accepts one of the following:

CONTAINER_UPLOAD("container_upload")

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Optional\<String\> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Accepts one of the following:

COMPACTION("compaction")

Optional\<[BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)\> contextManagement

Context management response.

Information about context management strategies applied during the request.

List\<AppliedEdit\> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

minimum0

long clearedToolUses

Number of tool uses that were cleared.

minimum0

JsonValue; type "clear_tool_uses_20250919"constant"clear_tool_uses_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR_TOOL_USES_20250919("clear_tool_uses_20250919")

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

minimum0

long clearedThinkingTurns

Number of thinking turns that were cleared.

minimum0

JsonValue; type "clear_thinking_20251015"constant"clear_thinking_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR_THINKING_20251015("clear_thinking_20251015")

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE_OPUS_4_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE_HAIKU_4_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE_SONNET_4_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE_SONNET_4_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE_OPUS_4_0("claude-opus-4-0")

Our most capable model

CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

Optional\<[BetaStopReason](/docs/en/api/beta#beta_stop_reason)\> stopReason

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

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

[BetaUsage](/docs/en/api/beta#beta_usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

minimum0

Optional\<List\<Iteration\>\> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

long cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

long inputTokens

The number of input tokens which were used.

minimum0

long outputTokens

The number of output tokens which were used.

minimum0

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

Accepts one of the following:

MESSAGE("message")

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

long cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

long inputTokens

The number of input tokens which were used.

minimum0

long outputTokens

The number of output tokens which were used.

minimum0

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

Accepts one of the following:

COMPACTION("compaction")

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

minimum0

long webSearchRequests

The number of web search tool requests.

minimum0

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

JsonValue; type "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

class BetaMessageBatchErroredResult:

[BetaErrorResponse](/docs/en/api/beta#beta_error_response) error

[BetaError](/docs/en/api/beta#beta_error) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant"invalid_request_error"constant

Accepts one of the following:

INVALID_REQUEST_ERROR("invalid_request_error")

class BetaAuthenticationError:

String message

JsonValue; type "authentication_error"constant"authentication_error"constant

Accepts one of the following:

AUTHENTICATION_ERROR("authentication_error")

class BetaBillingError:

String message

JsonValue; type "billing_error"constant"billing_error"constant

Accepts one of the following:

BILLING_ERROR("billing_error")

class BetaPermissionError:

String message

JsonValue; type "permission_error"constant"permission_error"constant

Accepts one of the following:

PERMISSION_ERROR("permission_error")

class BetaNotFoundError:

String message

JsonValue; type "not_found_error"constant"not_found_error"constant

Accepts one of the following:

NOT_FOUND_ERROR("not_found_error")

class BetaRateLimitError:

String message

JsonValue; type "rate_limit_error"constant"rate_limit_error"constant

Accepts one of the following:

RATE_LIMIT_ERROR("rate_limit_error")

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant"timeout_error"constant

Accepts one of the following:

TIMEOUT_ERROR("timeout_error")

class BetaApiError:

String message

JsonValue; type "api_error"constant"api_error"constant

Accepts one of the following:

API_ERROR("api_error")

class BetaOverloadedError:

String message

JsonValue; type "overloaded_error"constant"overloaded_error"constant

Accepts one of the following:

OVERLOADED_ERROR("overloaded_error")

Optional\<String\> requestId

JsonValue; type "error"constant"error"constant

Accepts one of the following:

ERROR("error")

JsonValue; type "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchRequestCounts:

long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.

long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

class BetaMessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class BetaMessageBatchSucceededResult:

[BetaMessage](/docs/en/api/beta#beta_message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[BetaContainer](/docs/en/api/beta#beta_container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

formatdate-time

Optional\<List\<[BetaSkill](/docs/en/api/beta#beta_skill)\>\> skills

Skills loaded in the container

String skillId

Skill ID

maxLength64

minLength1

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

maxLength64

minLength1

List\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> content

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

class BetaTextBlock:

Optional\<List\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

WEB_SEARCH("web_search")

WEB_FETCH("web_fetch")

CODE_EXECUTION("code_execution")

BASH_CODE_EXECUTION("bash_code_execution")

TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant"web_search_tool_result_error"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")

List\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant"web_search_tool_result"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT("web_search_tool_result")

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant"web_fetch_tool_result_error"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")

class BetaWebFetchBlock:

[BetaDocumentBlock](/docs/en/api/beta#beta_document_block) content

Optional\<[BetaCitationConfig](/docs/en/api/beta#beta_citation_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<String\> title

The title of the document

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant"web_fetch_result"constant

Accepts one of the following:

WEB_FETCH_RESULT("web_fetch_result")

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant"web_fetch_tool_result"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) content

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCodeExecutionResultBlock:

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant"code_execution_output"constant

Accepts one of the following:

CODE_EXECUTION_OUTPUT("code_execution_output")

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant"code_execution_result"constant

Accepts one of the following:

CODE_EXECUTION_RESULT("code_execution_result")

String toolUseId

JsonValue; type "code_execution_tool_result"constant"code_execution_tool_result"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant"bash_code_execution_tool_result_error"constant

Accepts one of the following:

BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")

class BetaBashCodeExecutionResultBlock:

List\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant"bash_code_execution_output"constant

Accepts one of the following:

BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant"bash_code_execution_result"constant

Accepts one of the following:

BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant"bash_code_execution_tool_result"constant

Accepts one of the following:

BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant"text_editor_code_execution_tool_result_error"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant"text_editor_code_execution_view_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant"text_editor_code_execution_create_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant"text_editor_code_execution_str_replace_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant"text_editor_code_execution_tool_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant"tool_search_tool_result_error"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")

class BetaToolSearchToolSearchResultBlock:

List\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

JsonValue; type "tool_search_tool_search_result"constant"tool_search_tool_search_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")

String toolUseId

JsonValue; type "tool_search_tool_result"constant"tool_search_tool_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant"mcp_tool_use"constant

Accepts one of the following:

MCP_TOOL_USE("mcp_tool_use")

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

Optional\<List\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

boolean isError

String toolUseId

JsonValue; type "mcp_tool_result"constant"mcp_tool_result"constant

Accepts one of the following:

MCP_TOOL_RESULT("mcp_tool_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant"container_upload"constant

Accepts one of the following:

CONTAINER_UPLOAD("container_upload")

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Optional\<String\> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Accepts one of the following:

COMPACTION("compaction")

Optional\<[BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)\> contextManagement

Context management response.

Information about context management strategies applied during the request.

List\<AppliedEdit\> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

minimum0

long clearedToolUses

Number of tool uses that were cleared.

minimum0

JsonValue; type "clear_tool_uses_20250919"constant"clear_tool_uses_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR_TOOL_USES_20250919("clear_tool_uses_20250919")

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

minimum0

long clearedThinkingTurns

Number of thinking turns that were cleared.

minimum0

JsonValue; type "clear_thinking_20251015"constant"clear_thinking_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR_THINKING_20251015("clear_thinking_20251015")

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE_OPUS_4_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE_HAIKU_4_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE_SONNET_4_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE_SONNET_4_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE_OPUS_4_0("claude-opus-4-0")

Our most capable model

CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

Optional\<[BetaStopReason](/docs/en/api/beta#beta_stop_reason)\> stopReason

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

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

[BetaUsage](/docs/en/api/beta#beta_usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

minimum0

Optional\<List\<Iteration\>\> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

long cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

long inputTokens

The number of input tokens which were used.

minimum0

long outputTokens

The number of output tokens which were used.

minimum0

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

Accepts one of the following:

MESSAGE("message")

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

long cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

long inputTokens

The number of input tokens which were used.

minimum0

long outputTokens

The number of output tokens which were used.

minimum0

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

Accepts one of the following:

COMPACTION("compaction")

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

minimum0

long webSearchRequests

The number of web search tool requests.

minimum0

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

JsonValue; type "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

class BetaMessageBatchErroredResult:

[BetaErrorResponse](/docs/en/api/beta#beta_error_response) error

[BetaError](/docs/en/api/beta#beta_error) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant"invalid_request_error"constant

Accepts one of the following:

INVALID_REQUEST_ERROR("invalid_request_error")

class BetaAuthenticationError:

String message

JsonValue; type "authentication_error"constant"authentication_error"constant

Accepts one of the following:

AUTHENTICATION_ERROR("authentication_error")

class BetaBillingError:

String message

JsonValue; type "billing_error"constant"billing_error"constant

Accepts one of the following:

BILLING_ERROR("billing_error")

class BetaPermissionError:

String message

JsonValue; type "permission_error"constant"permission_error"constant

Accepts one of the following:

PERMISSION_ERROR("permission_error")

class BetaNotFoundError:

String message

JsonValue; type "not_found_error"constant"not_found_error"constant

Accepts one of the following:

NOT_FOUND_ERROR("not_found_error")

class BetaRateLimitError:

String message

JsonValue; type "rate_limit_error"constant"rate_limit_error"constant

Accepts one of the following:

RATE_LIMIT_ERROR("rate_limit_error")

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant"timeout_error"constant

Accepts one of the following:

TIMEOUT_ERROR("timeout_error")

class BetaApiError:

String message

JsonValue; type "api_error"constant"api_error"constant

Accepts one of the following:

API_ERROR("api_error")

class BetaOverloadedError:

String message

JsonValue; type "overloaded_error"constant"overloaded_error"constant

Accepts one of the following:

OVERLOADED_ERROR("overloaded_error")

Optional\<String\> requestId

JsonValue; type "error"constant"error"constant

Accepts one of the following:

ERROR("error")

JsonValue; type "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchSucceededResult:

[BetaMessage](/docs/en/api/beta#beta_message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[BetaContainer](/docs/en/api/beta#beta_container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

formatdate-time

Optional\<List\<[BetaSkill](/docs/en/api/beta#beta_skill)\>\> skills

Skills loaded in the container

String skillId

Skill ID

maxLength64

minLength1

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

maxLength64

minLength1

List\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> content

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

class BetaTextBlock:

Optional\<List\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

WEB_SEARCH("web_search")

WEB_FETCH("web_fetch")

CODE_EXECUTION("code_execution")

BASH_CODE_EXECUTION("bash_code_execution")

TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant"web_search_tool_result_error"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")

List\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant"web_search_tool_result"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT("web_search_tool_result")

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant"web_fetch_tool_result_error"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")

class BetaWebFetchBlock:

[BetaDocumentBlock](/docs/en/api/beta#beta_document_block) content

Optional\<[BetaCitationConfig](/docs/en/api/beta#beta_citation_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<String\> title

The title of the document

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant"web_fetch_result"constant

Accepts one of the following:

WEB_FETCH_RESULT("web_fetch_result")

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant"web_fetch_tool_result"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) content

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCodeExecutionResultBlock:

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant"code_execution_output"constant

Accepts one of the following:

CODE_EXECUTION_OUTPUT("code_execution_output")

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant"code_execution_result"constant

Accepts one of the following:

CODE_EXECUTION_RESULT("code_execution_result")

String toolUseId

JsonValue; type "code_execution_tool_result"constant"code_execution_tool_result"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant"bash_code_execution_tool_result_error"constant

Accepts one of the following:

BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")

class BetaBashCodeExecutionResultBlock:

List\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant"bash_code_execution_output"constant

Accepts one of the following:

BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant"bash_code_execution_result"constant

Accepts one of the following:

BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant"bash_code_execution_tool_result"constant

Accepts one of the following:

BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant"text_editor_code_execution_tool_result_error"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant"text_editor_code_execution_view_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant"text_editor_code_execution_create_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant"text_editor_code_execution_str_replace_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant"text_editor_code_execution_tool_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant"tool_search_tool_result_error"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")

class BetaToolSearchToolSearchResultBlock:

List\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

JsonValue; type "tool_search_tool_search_result"constant"tool_search_tool_search_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")

String toolUseId

JsonValue; type "tool_search_tool_result"constant"tool_search_tool_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant"mcp_tool_use"constant

Accepts one of the following:

MCP_TOOL_USE("mcp_tool_use")

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

Optional\<List\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

boolean isError

String toolUseId

JsonValue; type "mcp_tool_result"constant"mcp_tool_result"constant

Accepts one of the following:

MCP_TOOL_RESULT("mcp_tool_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant"container_upload"constant

Accepts one of the following:

CONTAINER_UPLOAD("container_upload")

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Optional\<String\> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Accepts one of the following:

COMPACTION("compaction")

Optional\<[BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)\> contextManagement

Context management response.

Information about context management strategies applied during the request.

List\<AppliedEdit\> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

minimum0

long clearedToolUses

Number of tool uses that were cleared.

minimum0

JsonValue; type "clear_tool_uses_20250919"constant"clear_tool_uses_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR_TOOL_USES_20250919("clear_tool_uses_20250919")

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

minimum0

long clearedThinkingTurns

Number of thinking turns that were cleared.

minimum0

JsonValue; type "clear_thinking_20251015"constant"clear_thinking_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR_THINKING_20251015("clear_thinking_20251015")

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE_OPUS_4_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE_HAIKU_4_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE_SONNET_4_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE_SONNET_4_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE_OPUS_4_0("claude-opus-4-0")

Our most capable model

CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

Optional\<[BetaStopReason](/docs/en/api/beta#beta_stop_reason)\> stopReason

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

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

[BetaUsage](/docs/en/api/beta#beta_usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

minimum0

Optional\<List\<Iteration\>\> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

long cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

long inputTokens

The number of input tokens which were used.

minimum0

long outputTokens

The number of output tokens which were used.

minimum0

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

Accepts one of the following:

MESSAGE("message")

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

minimum0

long cacheReadInputTokens

The number of input tokens read from the cache.

minimum0

long inputTokens

The number of input tokens which were used.

minimum0

long outputTokens

The number of output tokens which were used.

minimum0

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

Accepts one of the following:

COMPACTION("compaction")

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

minimum0

long webSearchRequests

The number of web search tool requests.

minimum0

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

JsonValue; type "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

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
