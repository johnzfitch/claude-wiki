---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:10:02Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/messages/batches"
title: "Batches - Claude API Reference"
---

Copy page

Go

# Batches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

client.Beta.Messages.Batches.New(ctx, params) (\*[BetaMessageBatch](/docs/en/api/beta#beta_message_batch), error)

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

client.Beta.Messages.Batches.Get(ctx, messageBatchID, query) (\*[BetaMessageBatch](/docs/en/api/beta#beta_message_batch), error)

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

client.Beta.Messages.Batches.List(ctx, params) (\*Page\[[BetaMessageBatch](/docs/en/api/beta#beta_message_batch)\], error)

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

client.Beta.Messages.Batches.Cancel(ctx, messageBatchID, body) (\*[BetaMessageBatch](/docs/en/api/beta#beta_message_batch), error)

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

client.Beta.Messages.Batches.Delete(ctx, messageBatchID, body) (\*[BetaDeletedMessageBatch](/docs/en/api/beta#beta_deleted_message_batch), error)

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

client.Beta.Messages.Batches.Results(ctx, messageBatchID, query) (\*[BetaMessageBatchIndividualResponse](/docs/en/api/beta#beta_message_batch_individual_response), error)

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

type BetaDeletedMessageBatch struct{…}

ID string

ID of the Message Batch.

Type MessageBatchDeleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

const MessageBatchDeletedMessageBatchDeleted MessageBatchDeleted = "message_batch_deleted"

type BetaMessageBatch struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

ArchivedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

CancelInitiatedAt Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

CreatedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

EndedAt Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

ExpiresAt Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

ProcessingStatus BetaMessageBatchProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

const BetaMessageBatchProcessingStatusInProgress BetaMessageBatchProcessingStatus = "in_progress"

const BetaMessageBatchProcessingStatusCanceling BetaMessageBatchProcessingStatus = "canceling"

const BetaMessageBatchProcessingStatusEnded BetaMessageBatchProcessingStatus = "ended"

RequestCounts [BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

Canceled int64

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

Errored int64

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

Expired int64

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

Processing int64

Number of requests in the Message Batch that are processing.

Succeeded int64

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

ResultsURL string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Type MessageBatch

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

const MessageBatchMessageBatch MessageBatch = "message_batch"

type BetaMessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type BetaMessageBatchErroredResult struct{…}

Error [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

Error [BetaErrorUnion](/docs/en/api/beta#beta_error)

Accepts one of the following:

type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid_request_error"

type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication_error"

type BetaBillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing_error"

type BetaPermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission_error"

type BetaNotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not_found_error"

type BetaRateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate_limit_error"

type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout_error"

type BetaAPIError struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api_error"

type BetaOverloadedError struct{…}

Message string

Type OverloadedError

Accepts one of the following:

const OverloadedErrorOverloadedError OverloadedError = "overloaded_error"

RequestID string

Type Error

Accepts one of the following:

const ErrorError Error = "error"

Type Errored

Accepts one of the following:

const ErroredErrored Errored = "errored"

type BetaMessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

type BetaMessageBatchIndividualResponse struct{…}

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

Result [BetaMessageBatchResultUnion](/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

type BetaMessageBatchSucceededResult struct{…}

Message [BetaMessage](/docs/en/api/beta#beta_message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [BetaContainer](/docs/en/api/beta#beta_container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

formatdate-time

Skills \[\][BetaSkill](/docs/en/api/beta#beta_skill)

Skills loaded in the container

SkillID string

Skill ID

maxLength64

minLength1

Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version

maxLength64

minLength1

Content \[\][BetaContentBlockUnion](/docs/en/api/beta#beta_content_block)

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

type BetaTextBlock struct{…}

Citations \[\][BetaTextCitationUnion](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type BetaToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

Caller BetaToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"

type BetaServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name BetaServerToolUseBlockName

Accepts one of the following:

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash_code_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text_editor_code_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool_search_tool_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

Caller BetaServerToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"

type BetaWebSearchToolResultBlock struct{…}

Content [BetaWebSearchToolResultBlockContentUnion](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

type BetaWebSearchToolResultError struct{…}

ErrorCode [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "invalid_tool_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "max_uses_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "too_many_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "query_too_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type BetaWebSearchToolResultBlockContentArray \[\][BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web_search_tool_result"

type BetaWebFetchToolResultBlock struct{…}

Content BetaWebFetchToolResultBlockContentUnion

Accepts one of the following:

type BetaWebFetchToolResultErrorBlock struct{…}

ErrorCode [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "invalid_tool_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_too_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_not_allowed"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_not_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "unsupported_content_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "too_many_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "max_uses_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

Accepts one of the following:

const WebFetchToolResultErrorWebFetchToolResultError WebFetchToolResultError = "web_fetch_tool_result_error"

type BetaWebFetchBlock struct{…}

Content [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

Citations [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)

Citation configuration for the document

Enabled bool

Source BetaDocumentBlockSourceUnion

Accepts one of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

Title string

The title of the document

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

Accepts one of the following:

const WebFetchResultWebFetchResult WebFetchResult = "web_fetch_result"

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

Accepts one of the following:

const WebFetchToolResultWebFetchToolResult WebFetchToolResult = "web_fetch_tool_result"

type BetaCodeExecutionToolResultBlock struct{…}

Content [BetaCodeExecutionToolResultBlockContentUnion](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

type BetaCodeExecutionToolResultError struct{…}

ErrorCode [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "invalid_tool_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "too_many_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

Accepts one of the following:

const CodeExecutionToolResultErrorCodeExecutionToolResultError CodeExecutionToolResultError = "code_execution_tool_result_error"

type BetaCodeExecutionResultBlock struct{…}

Content \[\][BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)

FileID string

Type CodeExecutionOutput

Accepts one of the following:

const CodeExecutionOutputCodeExecutionOutput CodeExecutionOutput = "code_execution_output"

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

Accepts one of the following:

const CodeExecutionResultCodeExecutionResult CodeExecutionResult = "code_execution_result"

ToolUseID string

Type CodeExecutionToolResult

Accepts one of the following:

const CodeExecutionToolResultCodeExecutionToolResult CodeExecutionToolResult = "code_execution_tool_result"

type BetaBashCodeExecutionToolResultBlock struct{…}

Content BetaBashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaBashCodeExecutionToolResultError struct{…}

ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too_many_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output_file_too_large"

Type BashCodeExecutionToolResultError

Accepts one of the following:

const BashCodeExecutionToolResultErrorBashCodeExecutionToolResultError BashCodeExecutionToolResultError = "bash_code_execution_tool_result_error"

type BetaBashCodeExecutionResultBlock struct{…}

Content \[\][BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

Accepts one of the following:

const BashCodeExecutionOutputBashCodeExecutionOutput BashCodeExecutionOutput = "bash_code_execution_output"

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

Accepts one of the following:

const BashCodeExecutionResultBashCodeExecutionResult BashCodeExecutionResult = "bash_code_execution_result"

ToolUseID string

Type BashCodeExecutionToolResult

Accepts one of the following:

const BashCodeExecutionToolResultBashCodeExecutionToolResult BashCodeExecutionToolResult = "bash_code_execution_tool_result"

type BetaTextEditorCodeExecutionToolResultBlock struct{…}

Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaTextEditorCodeExecutionToolResultError struct{…}

ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too_many_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorTextEditorCodeExecutionToolResultError TextEditorCodeExecutionToolResultError = "text_editor_code_execution_tool_result_error"

type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType BetaTextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

Accepts one of the following:

const TextEditorCodeExecutionViewResultTextEditorCodeExecutionViewResult TextEditorCodeExecutionViewResult = "text_editor_code_execution_view_result"

type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

Accepts one of the following:

const TextEditorCodeExecutionCreateResultTextEditorCodeExecutionCreateResult TextEditorCodeExecutionCreateResult = "text_editor_code_execution_create_result"

type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

Accepts one of the following:

const TextEditorCodeExecutionStrReplaceResultTextEditorCodeExecutionStrReplaceResult TextEditorCodeExecutionStrReplaceResult = "text_editor_code_execution_str_replace_result"

ToolUseID string

Type TextEditorCodeExecutionToolResult

Accepts one of the following:

const TextEditorCodeExecutionToolResultTextEditorCodeExecutionToolResult TextEditorCodeExecutionToolResult = "text_editor_code_execution_tool_result"

type BetaToolSearchToolResultBlock struct{…}

Content BetaToolSearchToolResultBlockContentUnion

Accepts one of the following:

type BetaToolSearchToolResultError struct{…}

ErrorCode BetaToolSearchToolResultErrorErrorCode

Accepts one of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid_tool_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too_many_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

Accepts one of the following:

const ToolSearchToolResultErrorToolSearchToolResultError ToolSearchToolResultError = "tool_search_tool_result_error"

type BetaToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)

ToolName string

Type ToolReference

Accepts one of the following:

const ToolReferenceToolReference ToolReference = "tool_reference"

Type ToolSearchToolSearchResult

Accepts one of the following:

const ToolSearchToolSearchResultToolSearchToolSearchResult ToolSearchToolSearchResult = "tool_search_tool_search_result"

ToolUseID string

Type ToolSearchToolResult

Accepts one of the following:

const ToolSearchToolResultToolSearchToolResult ToolSearchToolResult = "tool_search_tool_result"

type BetaMCPToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse

Accepts one of the following:

const MCPToolUseMCPToolUse MCPToolUse = "mcp_tool_use"

type BetaMCPToolResultBlock struct{…}

Content BetaMCPToolResultBlockContentUnion

Accepts one of the following:

string

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent \[\][BetaTextBlock](/docs/en/api/beta#beta_text_block)

Citations \[\][BetaTextCitationUnion](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

IsError bool

ToolUseID string

Type MCPToolResult

Accepts one of the following:

const MCPToolResultMCPToolResult MCPToolResult = "mcp_tool_result"

type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Accepts one of the following:

const ContainerUploadContainerUpload ContainerUpload = "container_upload"

type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

Type Compaction

Accepts one of the following:

const CompactionCompaction Compaction = "compaction"

ContextManagement [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)

Context management response.

Information about context management strategies applied during the request.

AppliedEdits \[\]BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

Accepts one of the following:

type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedToolUses int64

Number of tool uses that were cleared.

minimum0

Type ClearToolUses20250919

The type of context management edit applied.

Accepts one of the following:

const ClearToolUses20250919ClearToolUses20250919 ClearToolUses20250919 = "clear_tool_uses_20250919"

type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

minimum0

Type ClearThinking20251015

The type of context management edit applied.

Accepts one of the following:

const ClearThinking20251015ClearThinking20251015 ClearThinking20251015 = "clear_thinking_20251015"

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

const ModelClaudeOpus4_5_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaude3_7SonnetLatest Model = "claude-3-7-sonnet-latest"

High-performance model with early extended thinking

const ModelClaude3_7Sonnet20250219 Model = "claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

const ModelClaude3_5HaikuLatest Model = "claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

const ModelClaude3_5Haiku20241022 Model = "claude-3-5-haiku-20241022"

Our fastest model

const ModelClaudeHaiku4_5 Model = "claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeHaiku4_5_20251001 Model = "claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeSonnet4_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaude4Sonnet20250514 Model = "claude-4-sonnet-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4_5 Model = "claude-sonnet-4-5"

Our best model for real-world agents and coding

const ModelClaudeSonnet4_5_20250929 Model = "claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

const ModelClaudeOpus4_0 Model = "claude-opus-4-0"

Our most capable model

const ModelClaudeOpus4_20250514 Model = "claude-opus-4-20250514"

Our most capable model

const ModelClaude4Opus20250514 Model = "claude-4-opus-20250514"

Our most capable model

const ModelClaudeOpus4_1_20250805 Model = "claude-opus-4-1-20250805"

Our most capable model

const ModelClaude3OpusLatest Model = "claude-3-opus-latest"

Excels at writing and complex tasks

const ModelClaude_3_Opus_20240229 Model = "claude-3-opus-20240229"

Excels at writing and complex tasks

const ModelClaude_3_Haiku_20240307 Model = "claude-3-haiku-20240307"

Our previous most fast and cost-effective

string

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

const AssistantAssistant Assistant = "assistant"

StopReason [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

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

const BetaStopReasonEndTurn [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "end_turn"

const BetaStopReasonMaxTokens [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "max_tokens"

const BetaStopReasonStopSequence [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "stop_sequence"

const BetaStopReasonToolUse [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "tool_use"

const BetaStopReasonPauseTurn [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "pause_turn"

const BetaStopReasonCompaction [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "model_context_window_exceeded"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

const MessageMessage Message = "message"

Usage [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

minimum0

Iterations \[\]BetaUsageIterationUnion

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

Type Message

Usage for a sampling iteration

Accepts one of the following:

const MessageMessage Message = "message"

type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

Type Compaction

Usage for a compaction iteration

Accepts one of the following:

const CompactionCompaction Compaction = "compaction"

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

minimum0

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"

Type Succeeded

Accepts one of the following:

const SucceededSucceeded Succeeded = "succeeded"

type BetaMessageBatchErroredResult struct{…}

Error [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

Error [BetaErrorUnion](/docs/en/api/beta#beta_error)

Accepts one of the following:

type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid_request_error"

type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication_error"

type BetaBillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing_error"

type BetaPermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission_error"

type BetaNotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not_found_error"

type BetaRateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate_limit_error"

type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout_error"

type BetaAPIError struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api_error"

type BetaOverloadedError struct{…}

Message string

Type OverloadedError

Accepts one of the following:

const OverloadedErrorOverloadedError OverloadedError = "overloaded_error"

RequestID string

Type Error

Accepts one of the following:

const ErrorError Error = "error"

Type Errored

Accepts one of the following:

const ErroredErrored Errored = "errored"

type BetaMessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type BetaMessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

type BetaMessageBatchRequestCounts struct{…}

Canceled int64

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

Errored int64

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

Expired int64

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

Processing int64

Number of requests in the Message Batch that are processing.

Succeeded int64

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

type BetaMessageBatchResultUnion interface{…}

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

type BetaMessageBatchSucceededResult struct{…}

Message [BetaMessage](/docs/en/api/beta#beta_message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [BetaContainer](/docs/en/api/beta#beta_container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

formatdate-time

Skills \[\][BetaSkill](/docs/en/api/beta#beta_skill)

Skills loaded in the container

SkillID string

Skill ID

maxLength64

minLength1

Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version

maxLength64

minLength1

Content \[\][BetaContentBlockUnion](/docs/en/api/beta#beta_content_block)

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

type BetaTextBlock struct{…}

Citations \[\][BetaTextCitationUnion](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type BetaToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

Caller BetaToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"

type BetaServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name BetaServerToolUseBlockName

Accepts one of the following:

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash_code_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text_editor_code_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool_search_tool_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

Caller BetaServerToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"

type BetaWebSearchToolResultBlock struct{…}

Content [BetaWebSearchToolResultBlockContentUnion](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

type BetaWebSearchToolResultError struct{…}

ErrorCode [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "invalid_tool_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "max_uses_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "too_many_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "query_too_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type BetaWebSearchToolResultBlockContentArray \[\][BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web_search_tool_result"

type BetaWebFetchToolResultBlock struct{…}

Content BetaWebFetchToolResultBlockContentUnion

Accepts one of the following:

type BetaWebFetchToolResultErrorBlock struct{…}

ErrorCode [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "invalid_tool_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_too_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_not_allowed"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_not_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "unsupported_content_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "too_many_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "max_uses_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

Accepts one of the following:

const WebFetchToolResultErrorWebFetchToolResultError WebFetchToolResultError = "web_fetch_tool_result_error"

type BetaWebFetchBlock struct{…}

Content [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

Citations [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)

Citation configuration for the document

Enabled bool

Source BetaDocumentBlockSourceUnion

Accepts one of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

Title string

The title of the document

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

Accepts one of the following:

const WebFetchResultWebFetchResult WebFetchResult = "web_fetch_result"

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

Accepts one of the following:

const WebFetchToolResultWebFetchToolResult WebFetchToolResult = "web_fetch_tool_result"

type BetaCodeExecutionToolResultBlock struct{…}

Content [BetaCodeExecutionToolResultBlockContentUnion](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

type BetaCodeExecutionToolResultError struct{…}

ErrorCode [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "invalid_tool_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "too_many_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

Accepts one of the following:

const CodeExecutionToolResultErrorCodeExecutionToolResultError CodeExecutionToolResultError = "code_execution_tool_result_error"

type BetaCodeExecutionResultBlock struct{…}

Content \[\][BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)

FileID string

Type CodeExecutionOutput

Accepts one of the following:

const CodeExecutionOutputCodeExecutionOutput CodeExecutionOutput = "code_execution_output"

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

Accepts one of the following:

const CodeExecutionResultCodeExecutionResult CodeExecutionResult = "code_execution_result"

ToolUseID string

Type CodeExecutionToolResult

Accepts one of the following:

const CodeExecutionToolResultCodeExecutionToolResult CodeExecutionToolResult = "code_execution_tool_result"

type BetaBashCodeExecutionToolResultBlock struct{…}

Content BetaBashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaBashCodeExecutionToolResultError struct{…}

ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too_many_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output_file_too_large"

Type BashCodeExecutionToolResultError

Accepts one of the following:

const BashCodeExecutionToolResultErrorBashCodeExecutionToolResultError BashCodeExecutionToolResultError = "bash_code_execution_tool_result_error"

type BetaBashCodeExecutionResultBlock struct{…}

Content \[\][BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

Accepts one of the following:

const BashCodeExecutionOutputBashCodeExecutionOutput BashCodeExecutionOutput = "bash_code_execution_output"

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

Accepts one of the following:

const BashCodeExecutionResultBashCodeExecutionResult BashCodeExecutionResult = "bash_code_execution_result"

ToolUseID string

Type BashCodeExecutionToolResult

Accepts one of the following:

const BashCodeExecutionToolResultBashCodeExecutionToolResult BashCodeExecutionToolResult = "bash_code_execution_tool_result"

type BetaTextEditorCodeExecutionToolResultBlock struct{…}

Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaTextEditorCodeExecutionToolResultError struct{…}

ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too_many_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorTextEditorCodeExecutionToolResultError TextEditorCodeExecutionToolResultError = "text_editor_code_execution_tool_result_error"

type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType BetaTextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

Accepts one of the following:

const TextEditorCodeExecutionViewResultTextEditorCodeExecutionViewResult TextEditorCodeExecutionViewResult = "text_editor_code_execution_view_result"

type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

Accepts one of the following:

const TextEditorCodeExecutionCreateResultTextEditorCodeExecutionCreateResult TextEditorCodeExecutionCreateResult = "text_editor_code_execution_create_result"

type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

Accepts one of the following:

const TextEditorCodeExecutionStrReplaceResultTextEditorCodeExecutionStrReplaceResult TextEditorCodeExecutionStrReplaceResult = "text_editor_code_execution_str_replace_result"

ToolUseID string

Type TextEditorCodeExecutionToolResult

Accepts one of the following:

const TextEditorCodeExecutionToolResultTextEditorCodeExecutionToolResult TextEditorCodeExecutionToolResult = "text_editor_code_execution_tool_result"

type BetaToolSearchToolResultBlock struct{…}

Content BetaToolSearchToolResultBlockContentUnion

Accepts one of the following:

type BetaToolSearchToolResultError struct{…}

ErrorCode BetaToolSearchToolResultErrorErrorCode

Accepts one of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid_tool_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too_many_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

Accepts one of the following:

const ToolSearchToolResultErrorToolSearchToolResultError ToolSearchToolResultError = "tool_search_tool_result_error"

type BetaToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)

ToolName string

Type ToolReference

Accepts one of the following:

const ToolReferenceToolReference ToolReference = "tool_reference"

Type ToolSearchToolSearchResult

Accepts one of the following:

const ToolSearchToolSearchResultToolSearchToolSearchResult ToolSearchToolSearchResult = "tool_search_tool_search_result"

ToolUseID string

Type ToolSearchToolResult

Accepts one of the following:

const ToolSearchToolResultToolSearchToolResult ToolSearchToolResult = "tool_search_tool_result"

type BetaMCPToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse

Accepts one of the following:

const MCPToolUseMCPToolUse MCPToolUse = "mcp_tool_use"

type BetaMCPToolResultBlock struct{…}

Content BetaMCPToolResultBlockContentUnion

Accepts one of the following:

string

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent \[\][BetaTextBlock](/docs/en/api/beta#beta_text_block)

Citations \[\][BetaTextCitationUnion](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

IsError bool

ToolUseID string

Type MCPToolResult

Accepts one of the following:

const MCPToolResultMCPToolResult MCPToolResult = "mcp_tool_result"

type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Accepts one of the following:

const ContainerUploadContainerUpload ContainerUpload = "container_upload"

type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

Type Compaction

Accepts one of the following:

const CompactionCompaction Compaction = "compaction"

ContextManagement [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)

Context management response.

Information about context management strategies applied during the request.

AppliedEdits \[\]BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

Accepts one of the following:

type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedToolUses int64

Number of tool uses that were cleared.

minimum0

Type ClearToolUses20250919

The type of context management edit applied.

Accepts one of the following:

const ClearToolUses20250919ClearToolUses20250919 ClearToolUses20250919 = "clear_tool_uses_20250919"

type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

minimum0

Type ClearThinking20251015

The type of context management edit applied.

Accepts one of the following:

const ClearThinking20251015ClearThinking20251015 ClearThinking20251015 = "clear_thinking_20251015"

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

const ModelClaudeOpus4_5_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaude3_7SonnetLatest Model = "claude-3-7-sonnet-latest"

High-performance model with early extended thinking

const ModelClaude3_7Sonnet20250219 Model = "claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

const ModelClaude3_5HaikuLatest Model = "claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

const ModelClaude3_5Haiku20241022 Model = "claude-3-5-haiku-20241022"

Our fastest model

const ModelClaudeHaiku4_5 Model = "claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeHaiku4_5_20251001 Model = "claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeSonnet4_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaude4Sonnet20250514 Model = "claude-4-sonnet-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4_5 Model = "claude-sonnet-4-5"

Our best model for real-world agents and coding

const ModelClaudeSonnet4_5_20250929 Model = "claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

const ModelClaudeOpus4_0 Model = "claude-opus-4-0"

Our most capable model

const ModelClaudeOpus4_20250514 Model = "claude-opus-4-20250514"

Our most capable model

const ModelClaude4Opus20250514 Model = "claude-4-opus-20250514"

Our most capable model

const ModelClaudeOpus4_1_20250805 Model = "claude-opus-4-1-20250805"

Our most capable model

const ModelClaude3OpusLatest Model = "claude-3-opus-latest"

Excels at writing and complex tasks

const ModelClaude_3_Opus_20240229 Model = "claude-3-opus-20240229"

Excels at writing and complex tasks

const ModelClaude_3_Haiku_20240307 Model = "claude-3-haiku-20240307"

Our previous most fast and cost-effective

string

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

const AssistantAssistant Assistant = "assistant"

StopReason [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

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

const BetaStopReasonEndTurn [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "end_turn"

const BetaStopReasonMaxTokens [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "max_tokens"

const BetaStopReasonStopSequence [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "stop_sequence"

const BetaStopReasonToolUse [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "tool_use"

const BetaStopReasonPauseTurn [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "pause_turn"

const BetaStopReasonCompaction [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "model_context_window_exceeded"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

const MessageMessage Message = "message"

Usage [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

minimum0

Iterations \[\]BetaUsageIterationUnion

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

Type Message

Usage for a sampling iteration

Accepts one of the following:

const MessageMessage Message = "message"

type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

Type Compaction

Usage for a compaction iteration

Accepts one of the following:

const CompactionCompaction Compaction = "compaction"

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

minimum0

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"

Type Succeeded

Accepts one of the following:

const SucceededSucceeded Succeeded = "succeeded"

type BetaMessageBatchErroredResult struct{…}

Error [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

Error [BetaErrorUnion](/docs/en/api/beta#beta_error)

Accepts one of the following:

type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid_request_error"

type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication_error"

type BetaBillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing_error"

type BetaPermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission_error"

type BetaNotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not_found_error"

type BetaRateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate_limit_error"

type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout_error"

type BetaAPIError struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api_error"

type BetaOverloadedError struct{…}

Message string

Type OverloadedError

Accepts one of the following:

const OverloadedErrorOverloadedError OverloadedError = "overloaded_error"

RequestID string

Type Error

Accepts one of the following:

const ErrorError Error = "error"

Type Errored

Accepts one of the following:

const ErroredErrored Errored = "errored"

type BetaMessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type BetaMessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

type BetaMessageBatchSucceededResult struct{…}

Message [BetaMessage](/docs/en/api/beta#beta_message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [BetaContainer](/docs/en/api/beta#beta_container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

formatdate-time

Skills \[\][BetaSkill](/docs/en/api/beta#beta_skill)

Skills loaded in the container

SkillID string

Skill ID

maxLength64

minLength1

Type BetaSkillType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

const BetaSkillTypeAnthropic BetaSkillType = "anthropic"

const BetaSkillTypeCustom BetaSkillType = "custom"

Version string

Skill version or 'latest' for most recent version

maxLength64

minLength1

Content \[\][BetaContentBlockUnion](/docs/en/api/beta#beta_content_block)

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

type BetaTextBlock struct{…}

Citations \[\][BetaTextCitationUnion](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

type BetaThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type BetaRedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type BetaToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

Caller BetaToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"

type BetaServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name BetaServerToolUseBlockName

Accepts one of the following:

const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web_search"

const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web_fetch"

const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code_execution"

const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash_code_execution"

const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text_editor_code_execution"

const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool_search_tool_regex"

const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

Caller BetaServerToolUseBlockCallerUnionoptional

Tool invocation directly from the model.

Accepts one of the following:

type BetaDirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

Accepts one of the following:

const DirectDirect Direct = "direct"

type BetaServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"

type BetaWebSearchToolResultBlock struct{…}

Content [BetaWebSearchToolResultBlockContentUnion](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

type BetaWebSearchToolResultError struct{…}

ErrorCode [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

const BetaWebSearchToolResultErrorCodeInvalidToolInput [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "invalid_tool_input"

const BetaWebSearchToolResultErrorCodeUnavailable [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "unavailable"

const BetaWebSearchToolResultErrorCodeMaxUsesExceeded [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "max_uses_exceeded"

const BetaWebSearchToolResultErrorCodeTooManyRequests [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "too_many_requests"

const BetaWebSearchToolResultErrorCodeQueryTooLong [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "query_too_long"

const BetaWebSearchToolResultErrorCodeRequestTooLarge [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type BetaWebSearchToolResultBlockContentArray \[\][BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web_search_tool_result"

type BetaWebFetchToolResultBlock struct{…}

Content BetaWebFetchToolResultBlockContentUnion

Accepts one of the following:

type BetaWebFetchToolResultErrorBlock struct{…}

ErrorCode [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

const BetaWebFetchToolResultErrorCodeInvalidToolInput [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "invalid_tool_input"

const BetaWebFetchToolResultErrorCodeURLTooLong [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_too_long"

const BetaWebFetchToolResultErrorCodeURLNotAllowed [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_not_allowed"

const BetaWebFetchToolResultErrorCodeURLNotAccessible [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "url_not_accessible"

const BetaWebFetchToolResultErrorCodeUnsupportedContentType [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "unsupported_content_type"

const BetaWebFetchToolResultErrorCodeTooManyRequests [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "too_many_requests"

const BetaWebFetchToolResultErrorCodeMaxUsesExceeded [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "max_uses_exceeded"

const BetaWebFetchToolResultErrorCodeUnavailable [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

Accepts one of the following:

const WebFetchToolResultErrorWebFetchToolResultError WebFetchToolResultError = "web_fetch_tool_result_error"

type BetaWebFetchBlock struct{…}

Content [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

Citations [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)

Citation configuration for the document

Enabled bool

Source BetaDocumentBlockSourceUnion

Accepts one of the following:

type BetaBase64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaPlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

Title string

The title of the document

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

Accepts one of the following:

const WebFetchResultWebFetchResult WebFetchResult = "web_fetch_result"

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

Accepts one of the following:

const WebFetchToolResultWebFetchToolResult WebFetchToolResult = "web_fetch_tool_result"

type BetaCodeExecutionToolResultBlock struct{…}

Content [BetaCodeExecutionToolResultBlockContentUnion](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

type BetaCodeExecutionToolResultError struct{…}

ErrorCode [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "invalid_tool_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "too_many_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

Accepts one of the following:

const CodeExecutionToolResultErrorCodeExecutionToolResultError CodeExecutionToolResultError = "code_execution_tool_result_error"

type BetaCodeExecutionResultBlock struct{…}

Content \[\][BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)

FileID string

Type CodeExecutionOutput

Accepts one of the following:

const CodeExecutionOutputCodeExecutionOutput CodeExecutionOutput = "code_execution_output"

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

Accepts one of the following:

const CodeExecutionResultCodeExecutionResult CodeExecutionResult = "code_execution_result"

ToolUseID string

Type CodeExecutionToolResult

Accepts one of the following:

const CodeExecutionToolResultCodeExecutionToolResult CodeExecutionToolResult = "code_execution_tool_result"

type BetaBashCodeExecutionToolResultBlock struct{…}

Content BetaBashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaBashCodeExecutionToolResultError struct{…}

ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"

const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too_many_requests"

const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"

const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output_file_too_large"

Type BashCodeExecutionToolResultError

Accepts one of the following:

const BashCodeExecutionToolResultErrorBashCodeExecutionToolResultError BashCodeExecutionToolResultError = "bash_code_execution_tool_result_error"

type BetaBashCodeExecutionResultBlock struct{…}

Content \[\][BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

Accepts one of the following:

const BashCodeExecutionOutputBashCodeExecutionOutput BashCodeExecutionOutput = "bash_code_execution_output"

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

Accepts one of the following:

const BashCodeExecutionResultBashCodeExecutionResult BashCodeExecutionResult = "bash_code_execution_result"

ToolUseID string

Type BashCodeExecutionToolResult

Accepts one of the following:

const BashCodeExecutionToolResultBashCodeExecutionToolResult BashCodeExecutionToolResult = "bash_code_execution_tool_result"

type BetaTextEditorCodeExecutionToolResultBlock struct{…}

Content BetaTextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BetaTextEditorCodeExecutionToolResultError struct{…}

ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode

Accepts one of the following:

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too_many_requests"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorTextEditorCodeExecutionToolResultError TextEditorCodeExecutionToolResultError = "text_editor_code_execution_tool_result_error"

type BetaTextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType BetaTextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

Accepts one of the following:

const TextEditorCodeExecutionViewResultTextEditorCodeExecutionViewResult TextEditorCodeExecutionViewResult = "text_editor_code_execution_view_result"

type BetaTextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

Accepts one of the following:

const TextEditorCodeExecutionCreateResultTextEditorCodeExecutionCreateResult TextEditorCodeExecutionCreateResult = "text_editor_code_execution_create_result"

type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

Accepts one of the following:

const TextEditorCodeExecutionStrReplaceResultTextEditorCodeExecutionStrReplaceResult TextEditorCodeExecutionStrReplaceResult = "text_editor_code_execution_str_replace_result"

ToolUseID string

Type TextEditorCodeExecutionToolResult

Accepts one of the following:

const TextEditorCodeExecutionToolResultTextEditorCodeExecutionToolResult TextEditorCodeExecutionToolResult = "text_editor_code_execution_tool_result"

type BetaToolSearchToolResultBlock struct{…}

Content BetaToolSearchToolResultBlockContentUnion

Accepts one of the following:

type BetaToolSearchToolResultError struct{…}

ErrorCode BetaToolSearchToolResultErrorErrorCode

Accepts one of the following:

const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid_tool_input"

const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"

const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too_many_requests"

const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

Accepts one of the following:

const ToolSearchToolResultErrorToolSearchToolResultError ToolSearchToolResultError = "tool_search_tool_result_error"

type BetaToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)

ToolName string

Type ToolReference

Accepts one of the following:

const ToolReferenceToolReference ToolReference = "tool_reference"

Type ToolSearchToolSearchResult

Accepts one of the following:

const ToolSearchToolSearchResultToolSearchToolSearchResult ToolSearchToolSearchResult = "tool_search_tool_search_result"

ToolUseID string

Type ToolSearchToolResult

Accepts one of the following:

const ToolSearchToolResultToolSearchToolResult ToolSearchToolResult = "tool_search_tool_result"

type BetaMCPToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

The name of the MCP tool

ServerName string

The name of the MCP server

Type MCPToolUse

Accepts one of the following:

const MCPToolUseMCPToolUse MCPToolUse = "mcp_tool_use"

type BetaMCPToolResultBlock struct{…}

Content BetaMCPToolResultBlockContentUnion

Accepts one of the following:

string

type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent \[\][BetaTextBlock](/docs/en/api/beta#beta_text_block)

Citations \[\][BetaTextCitationUnion](/docs/en/api/beta#beta_text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type BetaCitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

IsError bool

ToolUseID string

Type MCPToolResult

Accepts one of the following:

const MCPToolResultMCPToolResult MCPToolResult = "mcp_tool_result"

type BetaContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Accepts one of the following:

const ContainerUploadContainerUpload ContainerUpload = "container_upload"

type BetaCompactionBlock struct{…}

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Content string

Summary of compacted content, or null if compaction failed

Type Compaction

Accepts one of the following:

const CompactionCompaction Compaction = "compaction"

ContextManagement [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)

Context management response.

Information about context management strategies applied during the request.

AppliedEdits \[\]BetaContextManagementResponseAppliedEditUnion

List of context management edits that were applied.

Accepts one of the following:

type BetaClearToolUses20250919EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedToolUses int64

Number of tool uses that were cleared.

minimum0

Type ClearToolUses20250919

The type of context management edit applied.

Accepts one of the following:

const ClearToolUses20250919ClearToolUses20250919 ClearToolUses20250919 = "clear_tool_uses_20250919"

type BetaClearThinking20251015EditResponse struct{…}

ClearedInputTokens int64

Number of input tokens cleared by this edit.

minimum0

ClearedThinkingTurns int64

Number of thinking turns that were cleared.

minimum0

Type ClearThinking20251015

The type of context management edit applied.

Accepts one of the following:

const ClearThinking20251015ClearThinking20251015 ClearThinking20251015 = "clear_thinking_20251015"

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

const ModelClaudeOpus4_5_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaude3_7SonnetLatest Model = "claude-3-7-sonnet-latest"

High-performance model with early extended thinking

const ModelClaude3_7Sonnet20250219 Model = "claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

const ModelClaude3_5HaikuLatest Model = "claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

const ModelClaude3_5Haiku20241022 Model = "claude-3-5-haiku-20241022"

Our fastest model

const ModelClaudeHaiku4_5 Model = "claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeHaiku4_5_20251001 Model = "claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeSonnet4_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaude4Sonnet20250514 Model = "claude-4-sonnet-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4_5 Model = "claude-sonnet-4-5"

Our best model for real-world agents and coding

const ModelClaudeSonnet4_5_20250929 Model = "claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

const ModelClaudeOpus4_0 Model = "claude-opus-4-0"

Our most capable model

const ModelClaudeOpus4_20250514 Model = "claude-opus-4-20250514"

Our most capable model

const ModelClaude4Opus20250514 Model = "claude-4-opus-20250514"

Our most capable model

const ModelClaudeOpus4_1_20250805 Model = "claude-opus-4-1-20250805"

Our most capable model

const ModelClaude3OpusLatest Model = "claude-3-opus-latest"

Excels at writing and complex tasks

const ModelClaude_3_Opus_20240229 Model = "claude-3-opus-20240229"

Excels at writing and complex tasks

const ModelClaude_3_Haiku_20240307 Model = "claude-3-haiku-20240307"

Our previous most fast and cost-effective

string

Role Assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

const AssistantAssistant Assistant = "assistant"

StopReason [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

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

const BetaStopReasonEndTurn [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "end_turn"

const BetaStopReasonMaxTokens [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "max_tokens"

const BetaStopReasonStopSequence [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "stop_sequence"

const BetaStopReasonToolUse [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "tool_use"

const BetaStopReasonPauseTurn [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "pause_turn"

const BetaStopReasonCompaction [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "compaction"

const BetaStopReasonRefusal [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "refusal"

const BetaStopReasonModelContextWindowExceeded [BetaStopReason](/docs/en/api/beta#beta_stop_reason) = "model_context_window_exceeded"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

const MessageMessage Message = "message"

Usage [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

minimum0

Iterations \[\]BetaUsageIterationUnion

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

type BetaMessageIterationUsage struct{…}

Token usage for a sampling iteration.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

Type Message

Usage for a sampling iteration

Accepts one of the following:

const MessageMessage Message = "message"

type BetaCompactionIterationUsage struct{…}

Token usage for a compaction iteration.

CacheCreation [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The number of input tokens read from the cache.

minimum0

InputTokens int64

The number of input tokens which were used.

minimum0

OutputTokens int64

The number of output tokens which were used.

minimum0

Type Compaction

Usage for a compaction iteration

Accepts one of the following:

const CompactionCompaction Compaction = "compaction"

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

minimum0

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier BetaUsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"

const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"

const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"

Type Succeeded

Accepts one of the following:

const SucceededSucceeded Succeeded = "succeeded"

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
