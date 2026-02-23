---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:54:53Z"
source_url: "https://platform.claude.com/docs/en/api/go/messages"
title: "Messages - Claude API Reference"
---

Copy page

Go

# Messages

##### [Create a Message](/docs/en/api/messages/create)

client.Messages.New(ctx, body) (\*[Message](/docs/en/api/messages#message), error)

POST/v1/messages

##### [Count tokens in a Message](/docs/en/api/messages/count_tokens)

client.Messages.CountTokens(ctx, body) (\*[MessageTokensCount](/docs/en/api/messages#message_tokens_count), error)

POST/v1/messages/count_tokens

##### ModelsExpand Collapse 

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type BashCodeExecutionOutputBlock struct{…}

FileID string

Type BashCodeExecutionOutput

type BashCodeExecutionOutputBlockParamResp struct{…}

FileID string

Type BashCodeExecutionOutput

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

type BashCodeExecutionResultBlockParamResp struct{…}

Content \[\][BashCodeExecutionOutputBlockParamResp](/docs/en/api/messages#bash_code_execution_output_block_param)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type BashCodeExecutionToolResultBlockParamResp struct{…}

Content BashCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type BashCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlockParamResp struct{…}

Content \[\][BashCodeExecutionOutputBlockParamResp](/docs/en/api/messages#bash_code_execution_output_block_param)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionToolResultErrorCode string

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

type BashCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type CacheControlEphemeral struct{…}

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type CacheCreation struct{…}

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsConfig struct{…}

Enabled bool

type CitationsConfigParamResp struct{…}

Enabled bool

optional

type CitationsDelta struct{…}

Citation CitationsDeltaCitationUnion

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Type CitationsDelta

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CodeExecutionOutputBlock struct{…}

FileID string

Type CodeExecutionOutput

type CodeExecutionOutputBlockParamResp struct{…}

FileID string

Type CodeExecutionOutput

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type CodeExecutionResultBlockParamResp struct{…}

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type CodeExecutionTool20250522 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20250522AllowedCallerDirect CodeExecutionTool20250522AllowedCaller = "direct"

const CodeExecutionTool20250522AllowedCallerCodeExecution20250825 CodeExecutionTool20250522AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20250522AllowedCallerCodeExecution20260120 CodeExecutionTool20250522AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250825 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20250825AllowedCallerDirect CodeExecutionTool20250825AllowedCaller = "direct"

const CodeExecutionTool20250825AllowedCallerCodeExecution20250825 CodeExecutionTool20250825AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20250825AllowedCallerCodeExecution20260120 CodeExecutionTool20250825AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20260120AllowedCallerDirect CodeExecutionTool20260120AllowedCaller = "direct"

const CodeExecutionTool20260120AllowedCallerCodeExecution20250825 CodeExecutionTool20260120AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20260120AllowedCallerCodeExecution20260120 CodeExecutionTool20260120AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type CodeExecutionToolResultBlockContentUnion interface{…}

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

type CodeExecutionToolResultBlockParamResp struct{…}

Content [CodeExecutionToolResultBlockParamContentUnionResp](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlockParamResp struct{…}

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type CodeExecutionToolResultBlockParamContentUnionResp interface{…}

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlockParamResp struct{…}

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionToolResultErrorCode string

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

type CodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type Container struct{…}

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

type ContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ContentBlockUnion interface{…}

Response model for a file uploaded to the container.

Accepts one of the following:

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

type ContentBlockParamUnionResp interface{…}

Regular text content.

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

type ToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ToolUseBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type ToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Content \[\]ToolResultBlockParamContentUnionResp

optional

Accepts one of the following:

\[\]ToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

type ToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool_result content.

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

IsError bool

optional

type ServerToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name ServerToolUseBlockParamName

Accepts one of the following:

const ServerToolUseBlockParamNameWebSearch ServerToolUseBlockParamName = "web_search"

const ServerToolUseBlockParamNameWebFetch ServerToolUseBlockParamName = "web_fetch"

const ServerToolUseBlockParamNameCodeExecution ServerToolUseBlockParamName = "code_execution"

const ServerToolUseBlockParamNameBashCodeExecution ServerToolUseBlockParamName = "bash_code_execution"

const ServerToolUseBlockParamNameTextEditorCodeExecution ServerToolUseBlockParamName = "text_editor_code_execution"

const ServerToolUseBlockParamNameToolSearchToolRegex ServerToolUseBlockParamName = "tool_search_tool_regex"

const ServerToolUseBlockParamNameToolSearchToolBm25 ServerToolUseBlockParamName = "tool_search_tool_bm25"

Type ServerToolUse

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ServerToolUseBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebSearchToolResultBlockParamResp struct{…}

Content [WebSearchToolResultBlockParamContentUnionResp](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge string

optional

type WebSearchToolRequestError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebSearchToolResultBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebFetchToolResultBlockParamResp struct{…}

Content WebFetchToolResultBlockParamContentUnionResp

Accepts one of the following:

type WebFetchToolResultErrorBlockParamResp struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlockParamResp struct{…}

Content [DocumentBlockParamResp](/docs/en/api/messages#document_block_param)

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt string

optional

ISO 8601 timestamp when the content was retrieved

ToolUseID string

Type WebFetchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebFetchToolResultBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type CodeExecutionToolResultBlockParamResp struct{…}

Content [CodeExecutionToolResultBlockParamContentUnionResp](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlockParamResp struct{…}

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type BashCodeExecutionToolResultBlockParamResp struct{…}

Content BashCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type BashCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlockParamResp struct{…}

Content \[\][BashCodeExecutionOutputBlockParamResp](/docs/en/api/messages#bash_code_execution_output_block_param)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type TextEditorCodeExecutionToolResultBlockParamResp struct{…}

Content TextEditorCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextEditorCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage string

optional

type TextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockParamFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"

const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"

const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64

optional

StartLine int64

optional

TotalLines int64

optional

type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines \[\]string

optional

NewLines int64

optional

NewStart int64

optional

OldLines int64

optional

OldStart int64

optional

ToolUseID string

Type TextEditorCodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ToolSearchToolResultBlockParamResp struct{…}

Content ToolSearchToolResultBlockParamContentUnionResp

Accepts one of the following:

type ToolSearchToolResultErrorParamResp struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlockParamResp struct{…}

ToolReferences \[\][ToolReferenceBlockParamResp](/docs/en/api/messages#tool_reference_block_param)

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type ContentBlockSourceContentItemUnion interface{…}

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type DocumentBlock struct{…}

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

type EncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta

type JSONOutputFormat struct{…}

Schema map\[string, any\]

The JSON schema of the format

Type JSONSchema

type MemoryTool20250818 struct{…}

Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818

AllowedCallers \[\]string

optional

Accepts one of the following:

const MemoryTool20250818AllowedCallerDirect MemoryTool20250818AllowedCaller = "direct"

const MemoryTool20250818AllowedCallerCodeExecution20250825 MemoryTool20250818AllowedCaller = "code_execution_20250825"

const MemoryTool20250818AllowedCallerCodeExecution20260120 MemoryTool20250818AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type Message struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [Container](/docs/en/api/messages#container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

Content \[\][ContentBlockUnion](/docs/en/api/messages#content_block)

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

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

StopReason [StopReason](/docs/en/api/messages#stop_reason)

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

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](/docs/en/api/messages#usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](/docs/en/api/messages#cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

type MessageCountTokensToolUnion interface{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

type Tool struct{…}

InputSchema ToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Properties map\[string, any\]

optional

Required \[\]string

optional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolAllowedCallerDirect ToolAllowedCaller = "direct"

const ToolAllowedCallerCodeExecution20250825 ToolAllowedCaller = "code_execution_20250825"

const ToolAllowedCallerCodeExecution20260120 ToolAllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Description string

optional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming bool

optional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

Type ToolType

optional

type ToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolBash20250124AllowedCallerDirect ToolBash20250124AllowedCaller = "direct"

const ToolBash20250124AllowedCallerCodeExecution20250825 ToolBash20250124AllowedCaller = "code_execution_20250825"

const ToolBash20250124AllowedCallerCodeExecution20260120 ToolBash20250124AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250522 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20250522AllowedCallerDirect CodeExecutionTool20250522AllowedCaller = "direct"

const CodeExecutionTool20250522AllowedCallerCodeExecution20250825 CodeExecutionTool20250522AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20250522AllowedCallerCodeExecution20260120 CodeExecutionTool20250522AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250825 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20250825AllowedCallerDirect CodeExecutionTool20250825AllowedCaller = "direct"

const CodeExecutionTool20250825AllowedCallerCodeExecution20250825 CodeExecutionTool20250825AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20250825AllowedCallerCodeExecution20260120 CodeExecutionTool20250825AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20260120AllowedCallerDirect CodeExecutionTool20260120AllowedCaller = "direct"

const CodeExecutionTool20260120AllowedCallerCodeExecution20250825 CodeExecutionTool20260120AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20260120AllowedCallerCodeExecution20260120 CodeExecutionTool20260120AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type MemoryTool20250818 struct{…}

Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818

AllowedCallers \[\]string

optional

Accepts one of the following:

const MemoryTool20250818AllowedCallerDirect MemoryTool20250818AllowedCaller = "direct"

const MemoryTool20250818AllowedCallerCodeExecution20250825 MemoryTool20250818AllowedCaller = "code_execution_20250825"

const MemoryTool20250818AllowedCallerCodeExecution20260120 MemoryTool20250818AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250124AllowedCallerDirect ToolTextEditor20250124AllowedCaller = "direct"

const ToolTextEditor20250124AllowedCallerCodeExecution20250825 ToolTextEditor20250124AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250124AllowedCallerCodeExecution20260120 ToolTextEditor20250124AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250429AllowedCallerDirect ToolTextEditor20250429AllowedCaller = "direct"

const ToolTextEditor20250429AllowedCallerCodeExecution20250825 ToolTextEditor20250429AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250429AllowedCallerCodeExecution20260120 ToolTextEditor20250429AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250728AllowedCallerDirect ToolTextEditor20250728AllowedCaller = "direct"

const ToolTextEditor20250728AllowedCallerCodeExecution20250825 ToolTextEditor20250728AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250728AllowedCallerCodeExecution20260120 ToolTextEditor20250728AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

MaxCharacters int64

optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebSearchTool20250305AllowedCallerDirect WebSearchTool20250305AllowedCaller = "direct"

const WebSearchTool20250305AllowedCallerCodeExecution20250825 WebSearchTool20250305AllowedCaller = "code_execution_20250825"

const WebSearchTool20250305AllowedCallerCodeExecution20260120 WebSearchTool20250305AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]string

optional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](/docs/en/api/messages#user_location)

optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchTool20250910 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebFetchTool20250910AllowedCallerDirect WebFetchTool20250910AllowedCaller = "direct"

const WebFetchTool20250910AllowedCallerCodeExecution20250825 WebFetchTool20250910AllowedCaller = "code_execution_20250825"

const WebFetchTool20250910AllowedCallerCodeExecution20260120 WebFetchTool20250910AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

List of domains to allow fetching from

BlockedDomains \[\]string

optional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled bool

optional

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64

optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20260209 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebSearchTool20260209AllowedCallerDirect WebSearchTool20260209AllowedCaller = "direct"

const WebSearchTool20260209AllowedCallerCodeExecution20250825 WebSearchTool20260209AllowedCaller = "code_execution_20250825"

const WebSearchTool20260209AllowedCallerCodeExecution20260120 WebSearchTool20260209AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]string

optional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](/docs/en/api/messages#user_location)

optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchTool20260209 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebFetchTool20260209AllowedCallerDirect WebFetchTool20260209AllowedCaller = "direct"

const WebFetchTool20260209AllowedCallerCodeExecution20250825 WebFetchTool20260209AllowedCaller = "code_execution_20250825"

const WebFetchTool20260209AllowedCallerCodeExecution20260120 WebFetchTool20260209AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

List of domains to allow fetching from

BlockedDomains \[\]string

optional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled bool

optional

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64

optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolBm25_20251119 struct{…}

Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolBm25_20251119Type

Accepts one of the following:

const ToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"

const ToolSearchToolBm25_20251119TypeToolSearchToolBm25 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolSearchToolBm25_20251119AllowedCallerDirect ToolSearchToolBm25_20251119AllowedCaller = "direct"

const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"

const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolRegex20251119 struct{…}

Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolRegex20251119Type

Accepts one of the following:

const ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 ToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"

const ToolSearchToolRegex20251119TypeToolSearchToolRegex ToolSearchToolRegex20251119Type = "tool_search_tool_regex"

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolSearchToolRegex20251119AllowedCallerDirect ToolSearchToolRegex20251119AllowedCaller = "direct"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type MessageDeltaUsage struct{…}

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

InputTokens int64

The cumulative number of input tokens which were used.

OutputTokens int64

The cumulative number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

type MessageParamResp struct{…}

Content \[\][ContentBlockParamUnionResp](/docs/en/api/messages#content_block_param)

Accepts one of the following:

\[\][ContentBlockParamUnionResp](/docs/en/api/messages#content_block_param)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

type ToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ToolUseBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type ToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Content \[\]ToolResultBlockParamContentUnionResp

optional

Accepts one of the following:

\[\]ToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

type ToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool_result content.

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

IsError bool

optional

type ServerToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name ServerToolUseBlockParamName

Accepts one of the following:

const ServerToolUseBlockParamNameWebSearch ServerToolUseBlockParamName = "web_search"

const ServerToolUseBlockParamNameWebFetch ServerToolUseBlockParamName = "web_fetch"

const ServerToolUseBlockParamNameCodeExecution ServerToolUseBlockParamName = "code_execution"

const ServerToolUseBlockParamNameBashCodeExecution ServerToolUseBlockParamName = "bash_code_execution"

const ServerToolUseBlockParamNameTextEditorCodeExecution ServerToolUseBlockParamName = "text_editor_code_execution"

const ServerToolUseBlockParamNameToolSearchToolRegex ServerToolUseBlockParamName = "tool_search_tool_regex"

const ServerToolUseBlockParamNameToolSearchToolBm25 ServerToolUseBlockParamName = "tool_search_tool_bm25"

Type ServerToolUse

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ServerToolUseBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebSearchToolResultBlockParamResp struct{…}

Content [WebSearchToolResultBlockParamContentUnionResp](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge string

optional

type WebSearchToolRequestError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebSearchToolResultBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebFetchToolResultBlockParamResp struct{…}

Content WebFetchToolResultBlockParamContentUnionResp

Accepts one of the following:

type WebFetchToolResultErrorBlockParamResp struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlockParamResp struct{…}

Content [DocumentBlockParamResp](/docs/en/api/messages#document_block_param)

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt string

optional

ISO 8601 timestamp when the content was retrieved

ToolUseID string

Type WebFetchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebFetchToolResultBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type CodeExecutionToolResultBlockParamResp struct{…}

Content [CodeExecutionToolResultBlockParamContentUnionResp](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlockParamResp struct{…}

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type BashCodeExecutionToolResultBlockParamResp struct{…}

Content BashCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type BashCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlockParamResp struct{…}

Content \[\][BashCodeExecutionOutputBlockParamResp](/docs/en/api/messages#bash_code_execution_output_block_param)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type TextEditorCodeExecutionToolResultBlockParamResp struct{…}

Content TextEditorCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextEditorCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage string

optional

type TextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockParamFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"

const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"

const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64

optional

StartLine int64

optional

TotalLines int64

optional

type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines \[\]string

optional

NewLines int64

optional

NewStart int64

optional

OldLines int64

optional

OldStart int64

optional

ToolUseID string

Type TextEditorCodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ToolSearchToolResultBlockParamResp struct{…}

Content ToolSearchToolResultBlockParamContentUnionResp

Accepts one of the following:

type ToolSearchToolResultErrorParamResp struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlockParamResp struct{…}

ToolReferences \[\][ToolReferenceBlockParamResp](/docs/en/api/messages#tool_reference_block_param)

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Role MessageParamRole

Accepts one of the following:

const MessageParamRoleUser MessageParamRole = "user"

const MessageParamRoleAssistant MessageParamRole = "assistant"

type MessageTokensCount struct{…}

InputTokens int64

The total number of tokens across the provided list of messages, system prompt, and tools.

type Metadata struct{…}

UserID string

optional

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

type Model interface{…}

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

type OutputConfig struct{…}

Effort OutputConfigEffort

optional

All possible effort levels.

Accepts one of the following:

const OutputConfigEffortLow OutputConfigEffort = "low"

const OutputConfigEffortMedium OutputConfigEffort = "medium"

const OutputConfigEffortHigh OutputConfigEffort = "high"

const OutputConfigEffortMax OutputConfigEffort = "max"

Format [JSONOutputFormat](/docs/en/api/messages#json_output_format)

optional

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

Schema map\[string, any\]

The JSON schema of the format

Type JSONSchema

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type RawContentBlockDeltaUnion interface{…}

Accepts one of the following:

type TextDelta struct{…}

Text string

Type TextDelta

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta

type CitationsDelta struct{…}

Citation CitationsDeltaCitationUnion

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Type CitationsDelta

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

type ContentBlockDeltaEvent struct{…}

Delta [RawContentBlockDeltaUnion](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

type TextDelta struct{…}

Text string

Type TextDelta

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta

type CitationsDelta struct{…}

Citation CitationsDeltaCitationUnion

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Type CitationsDelta

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Index int64

Type ContentBlockDelta

type ContentBlockStartEvent struct{…}

ContentBlock ContentBlockStartEventContentBlockUnion

Response model for a file uploaded to the container.

Accepts one of the following:

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Index int64

Type ContentBlockStart

type ContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop

type MessageDeltaEvent struct{…}

Delta MessageDeltaEventDelta

Container [Container](/docs/en/api/messages#container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

StopReason [StopReason](/docs/en/api/messages#stop_reason)

Accepts one of the following:

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

StopSequence string

Type MessageDelta

Usage [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

InputTokens int64

The cumulative number of input tokens which were used.

OutputTokens int64

The cumulative number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

type MessageStartEvent struct{…}

Message [Message](/docs/en/api/messages#message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [Container](/docs/en/api/messages#container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

Content \[\][ContentBlockUnion](/docs/en/api/messages#content_block)

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

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

StopReason [StopReason](/docs/en/api/messages#stop_reason)

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

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](/docs/en/api/messages#usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](/docs/en/api/messages#cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type MessageStart

type MessageStopEvent struct{…}

Type MessageStop

type MessageStreamEventUnion interface{…}

Accepts one of the following:

type MessageStartEvent struct{…}

Message [Message](/docs/en/api/messages#message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [Container](/docs/en/api/messages#container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

Content \[\][ContentBlockUnion](/docs/en/api/messages#content_block)

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

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

StopReason [StopReason](/docs/en/api/messages#stop_reason)

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

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](/docs/en/api/messages#usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](/docs/en/api/messages#cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type MessageStart

type MessageDeltaEvent struct{…}

Delta MessageDeltaEventDelta

Container [Container](/docs/en/api/messages#container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

StopReason [StopReason](/docs/en/api/messages#stop_reason)

Accepts one of the following:

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

StopSequence string

Type MessageDelta

Usage [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

InputTokens int64

The cumulative number of input tokens which were used.

OutputTokens int64

The cumulative number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

type MessageStopEvent struct{…}

Type MessageStop

type ContentBlockStartEvent struct{…}

ContentBlock ContentBlockStartEventContentBlockUnion

Response model for a file uploaded to the container.

Accepts one of the following:

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

Index int64

Type ContentBlockStart

type ContentBlockDeltaEvent struct{…}

Delta [RawContentBlockDeltaUnion](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

type TextDelta struct{…}

Text string

Type TextDelta

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta

type CitationsDelta struct{…}

Citation CitationsDeltaCitationUnion

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Type CitationsDelta

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Index int64

Type ContentBlockDelta

type ContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type ServerToolUsage struct{…}

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type ServerToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name ServerToolUseBlockParamName

Accepts one of the following:

const ServerToolUseBlockParamNameWebSearch ServerToolUseBlockParamName = "web_search"

const ServerToolUseBlockParamNameWebFetch ServerToolUseBlockParamName = "web_fetch"

const ServerToolUseBlockParamNameCodeExecution ServerToolUseBlockParamName = "code_execution"

const ServerToolUseBlockParamNameBashCodeExecution ServerToolUseBlockParamName = "bash_code_execution"

const ServerToolUseBlockParamNameTextEditorCodeExecution ServerToolUseBlockParamName = "text_editor_code_execution"

const ServerToolUseBlockParamNameToolSearchToolRegex ServerToolUseBlockParamName = "tool_search_tool_regex"

const ServerToolUseBlockParamNameToolSearchToolBm25 ServerToolUseBlockParamName = "tool_search_tool_bm25"

Type ServerToolUse

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ServerToolUseBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

type StopReason string

Accepts one of the following:

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type TextCitationUnion interface{…}

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type TextCitationParamUnionResp interface{…}

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type TextDelta struct{…}

Text string

Type TextDelta

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines \[\]string

optional

NewLines int64

optional

NewStart int64

optional

OldLines int64

optional

OldStart int64

optional

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlockParamResp struct{…}

Content TextEditorCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextEditorCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage string

optional

type TextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockParamFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"

const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"

const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64

optional

StartLine int64

optional

TotalLines int64

optional

type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines \[\]string

optional

NewLines int64

optional

NewStart int64

optional

OldLines int64

optional

OldStart int64

optional

ToolUseID string

Type TextEditorCodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionToolResultErrorCode string

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

type TextEditorCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage string

optional

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockParamFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"

const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"

const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64

optional

StartLine int64

optional

TotalLines int64

optional

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

type ThinkingConfigAdaptive struct{…}

Type Adaptive

type ThinkingConfigDisabled struct{…}

Type Disabled

type ThinkingConfigEnabled struct{…}

BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

Type Enabled

type ThinkingConfigParamUnionResp interface{…}

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

type ThinkingConfigEnabled struct{…}

BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

Type Enabled

type ThinkingConfigDisabled struct{…}

Type Disabled

type ThinkingConfigAdaptive struct{…}

Type Adaptive

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

type Tool struct{…}

InputSchema ToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Properties map\[string, any\]

optional

Required \[\]string

optional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolAllowedCallerDirect ToolAllowedCaller = "direct"

const ToolAllowedCallerCodeExecution20250825 ToolAllowedCaller = "code_execution_20250825"

const ToolAllowedCallerCodeExecution20260120 ToolAllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Description string

optional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming bool

optional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

Type ToolType

optional

type ToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolBash20250124AllowedCallerDirect ToolBash20250124AllowedCaller = "direct"

const ToolBash20250124AllowedCallerCodeExecution20250825 ToolBash20250124AllowedCaller = "code_execution_20250825"

const ToolBash20250124AllowedCallerCodeExecution20260120 ToolBash20250124AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolChoiceUnion interface{…}

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

type ToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto

DisableParallelToolUse bool

optional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

type ToolChoiceAny struct{…}

The model will use any available tools.

Type Any

DisableParallelToolUse bool

optional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type ToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool

DisableParallelToolUse bool

optional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type ToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None

type ToolChoiceAny struct{…}

The model will use any available tools.

Type Any

DisableParallelToolUse bool

optional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type ToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto

DisableParallelToolUse bool

optional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

type ToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None

type ToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool

DisableParallelToolUse bool

optional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type ToolReferenceBlock struct{…}

ToolName string

Type ToolReference

type ToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool_result content.

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Content \[\]ToolResultBlockParamContentUnionResp

optional

Accepts one of the following:

\[\]ToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

type ToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool_result content.

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

IsError bool

optional

type ToolSearchToolBm25_20251119 struct{…}

Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolBm25_20251119Type

Accepts one of the following:

const ToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"

const ToolSearchToolBm25_20251119TypeToolSearchToolBm25 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolSearchToolBm25_20251119AllowedCallerDirect ToolSearchToolBm25_20251119AllowedCaller = "direct"

const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"

const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolRegex20251119 struct{…}

Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolRegex20251119Type

Accepts one of the following:

const ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 ToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"

const ToolSearchToolRegex20251119TypeToolSearchToolRegex ToolSearchToolRegex20251119Type = "tool_search_tool_regex"

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolSearchToolRegex20251119AllowedCallerDirect ToolSearchToolRegex20251119AllowedCaller = "direct"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ToolSearchToolResultBlockParamResp struct{…}

Content ToolSearchToolResultBlockParamContentUnionResp

Accepts one of the following:

type ToolSearchToolResultErrorParamResp struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlockParamResp struct{…}

ToolReferences \[\][ToolReferenceBlockParamResp](/docs/en/api/messages#tool_reference_block_param)

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolResultErrorCode string

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

type ToolSearchToolResultErrorParamResp struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

type ToolSearchToolSearchResultBlockParamResp struct{…}

ToolReferences \[\][ToolReferenceBlockParamResp](/docs/en/api/messages#tool_reference_block_param)

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

type ToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250124AllowedCallerDirect ToolTextEditor20250124AllowedCaller = "direct"

const ToolTextEditor20250124AllowedCallerCodeExecution20250825 ToolTextEditor20250124AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250124AllowedCallerCodeExecution20260120 ToolTextEditor20250124AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250429AllowedCallerDirect ToolTextEditor20250429AllowedCaller = "direct"

const ToolTextEditor20250429AllowedCallerCodeExecution20250825 ToolTextEditor20250429AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250429AllowedCallerCodeExecution20260120 ToolTextEditor20250429AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250728AllowedCallerDirect ToolTextEditor20250728AllowedCaller = "direct"

const ToolTextEditor20250728AllowedCallerCodeExecution20250825 ToolTextEditor20250728AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250728AllowedCallerCodeExecution20260120 ToolTextEditor20250728AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

MaxCharacters int64

optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolUnion interface{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

type Tool struct{…}

InputSchema ToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Properties map\[string, any\]

optional

Required \[\]string

optional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolAllowedCallerDirect ToolAllowedCaller = "direct"

const ToolAllowedCallerCodeExecution20250825 ToolAllowedCaller = "code_execution_20250825"

const ToolAllowedCallerCodeExecution20260120 ToolAllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Description string

optional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming bool

optional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

Type ToolType

optional

type ToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolBash20250124AllowedCallerDirect ToolBash20250124AllowedCaller = "direct"

const ToolBash20250124AllowedCallerCodeExecution20250825 ToolBash20250124AllowedCaller = "code_execution_20250825"

const ToolBash20250124AllowedCallerCodeExecution20260120 ToolBash20250124AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250522 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20250522AllowedCallerDirect CodeExecutionTool20250522AllowedCaller = "direct"

const CodeExecutionTool20250522AllowedCallerCodeExecution20250825 CodeExecutionTool20250522AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20250522AllowedCallerCodeExecution20260120 CodeExecutionTool20250522AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250825 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20250825AllowedCallerDirect CodeExecutionTool20250825AllowedCaller = "direct"

const CodeExecutionTool20250825AllowedCallerCodeExecution20250825 CodeExecutionTool20250825AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20250825AllowedCallerCodeExecution20260120 CodeExecutionTool20250825AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20260120AllowedCallerDirect CodeExecutionTool20260120AllowedCaller = "direct"

const CodeExecutionTool20260120AllowedCallerCodeExecution20250825 CodeExecutionTool20260120AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20260120AllowedCallerCodeExecution20260120 CodeExecutionTool20260120AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type MemoryTool20250818 struct{…}

Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818

AllowedCallers \[\]string

optional

Accepts one of the following:

const MemoryTool20250818AllowedCallerDirect MemoryTool20250818AllowedCaller = "direct"

const MemoryTool20250818AllowedCallerCodeExecution20250825 MemoryTool20250818AllowedCaller = "code_execution_20250825"

const MemoryTool20250818AllowedCallerCodeExecution20260120 MemoryTool20250818AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250124AllowedCallerDirect ToolTextEditor20250124AllowedCaller = "direct"

const ToolTextEditor20250124AllowedCallerCodeExecution20250825 ToolTextEditor20250124AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250124AllowedCallerCodeExecution20260120 ToolTextEditor20250124AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250429AllowedCallerDirect ToolTextEditor20250429AllowedCaller = "direct"

const ToolTextEditor20250429AllowedCallerCodeExecution20250825 ToolTextEditor20250429AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250429AllowedCallerCodeExecution20260120 ToolTextEditor20250429AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250728AllowedCallerDirect ToolTextEditor20250728AllowedCaller = "direct"

const ToolTextEditor20250728AllowedCallerCodeExecution20250825 ToolTextEditor20250728AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250728AllowedCallerCodeExecution20260120 ToolTextEditor20250728AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

MaxCharacters int64

optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebSearchTool20250305AllowedCallerDirect WebSearchTool20250305AllowedCaller = "direct"

const WebSearchTool20250305AllowedCallerCodeExecution20250825 WebSearchTool20250305AllowedCaller = "code_execution_20250825"

const WebSearchTool20250305AllowedCallerCodeExecution20260120 WebSearchTool20250305AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]string

optional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](/docs/en/api/messages#user_location)

optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchTool20250910 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebFetchTool20250910AllowedCallerDirect WebFetchTool20250910AllowedCaller = "direct"

const WebFetchTool20250910AllowedCallerCodeExecution20250825 WebFetchTool20250910AllowedCaller = "code_execution_20250825"

const WebFetchTool20250910AllowedCallerCodeExecution20260120 WebFetchTool20250910AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

List of domains to allow fetching from

BlockedDomains \[\]string

optional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled bool

optional

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64

optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20260209 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebSearchTool20260209AllowedCallerDirect WebSearchTool20260209AllowedCaller = "direct"

const WebSearchTool20260209AllowedCallerCodeExecution20250825 WebSearchTool20260209AllowedCaller = "code_execution_20250825"

const WebSearchTool20260209AllowedCallerCodeExecution20260120 WebSearchTool20260209AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]string

optional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](/docs/en/api/messages#user_location)

optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchTool20260209 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebFetchTool20260209AllowedCallerDirect WebFetchTool20260209AllowedCaller = "direct"

const WebFetchTool20260209AllowedCallerCodeExecution20250825 WebFetchTool20260209AllowedCaller = "code_execution_20250825"

const WebFetchTool20260209AllowedCallerCodeExecution20260120 WebFetchTool20260209AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

List of domains to allow fetching from

BlockedDomains \[\]string

optional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled bool

optional

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64

optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolBm25_20251119 struct{…}

Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolBm25_20251119Type

Accepts one of the following:

const ToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"

const ToolSearchToolBm25_20251119TypeToolSearchToolBm25 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolSearchToolBm25_20251119AllowedCallerDirect ToolSearchToolBm25_20251119AllowedCaller = "direct"

const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"

const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolRegex20251119 struct{…}

Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolRegex20251119Type

Accepts one of the following:

const ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 ToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"

const ToolSearchToolRegex20251119TypeToolSearchToolRegex ToolSearchToolRegex20251119Type = "tool_search_tool_regex"

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolSearchToolRegex20251119AllowedCallerDirect ToolSearchToolRegex20251119AllowedCaller = "direct"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ToolUseBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type URLImageSource struct{…}

Type URL

URL string

type URLPDFSource struct{…}

Type URL

URL string

type Usage struct{…}

CacheCreation [CacheCreation](/docs/en/api/messages#cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

type UserLocation struct{…}

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

type WebFetchBlockParamResp struct{…}

Content [DocumentBlockParamResp](/docs/en/api/messages#document_block_param)

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt string

optional

ISO 8601 timestamp when the content was retrieved

type WebFetchTool20250910 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebFetchTool20250910AllowedCallerDirect WebFetchTool20250910AllowedCaller = "direct"

const WebFetchTool20250910AllowedCallerCodeExecution20250825 WebFetchTool20250910AllowedCaller = "code_execution_20250825"

const WebFetchTool20250910AllowedCallerCodeExecution20260120 WebFetchTool20250910AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

List of domains to allow fetching from

BlockedDomains \[\]string

optional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled bool

optional

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64

optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type WebFetchTool20260209 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebFetchTool20260209AllowedCallerDirect WebFetchTool20260209AllowedCaller = "direct"

const WebFetchTool20260209AllowedCallerCodeExecution20250825 WebFetchTool20260209AllowedCaller = "code_execution_20250825"

const WebFetchTool20260209AllowedCallerCodeExecution20260120 WebFetchTool20260209AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

List of domains to allow fetching from

BlockedDomains \[\]string

optional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled bool

optional

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64

optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type WebFetchToolResultBlockParamResp struct{…}

Content WebFetchToolResultBlockParamContentUnionResp

Accepts one of the following:

type WebFetchToolResultErrorBlockParamResp struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlockParamResp struct{…}

Content [DocumentBlockParamResp](/docs/en/api/messages#document_block_param)

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

type ImageBlockParamResp struct{…}

Source ImageBlockParamSourceUnionResp

Accepts one of the following:

type Base64ImageSource struct{…}

Data string

MediaType Base64ImageSourceMediaType

Accepts one of the following:

const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"

const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"

const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"

const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"

Type Base64

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt string

optional

ISO 8601 timestamp when the content was retrieved

ToolUseID string

Type WebFetchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebFetchToolResultBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchToolResultErrorBlockParamResp struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchToolResultErrorCode string

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

type WebSearchResultBlock struct{…}

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

type WebSearchResultBlockParamResp struct{…}

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge string

optional

type WebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebSearchTool20250305AllowedCallerDirect WebSearchTool20250305AllowedCaller = "direct"

const WebSearchTool20250305AllowedCallerCodeExecution20250825 WebSearchTool20250305AllowedCaller = "code_execution_20250825"

const WebSearchTool20250305AllowedCallerCodeExecution20260120 WebSearchTool20250305AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]string

optional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](/docs/en/api/messages#user_location)

optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebSearchTool20260209 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebSearchTool20260209AllowedCallerDirect WebSearchTool20260209AllowedCaller = "direct"

const WebSearchTool20260209AllowedCallerCodeExecution20250825 WebSearchTool20260209AllowedCaller = "code_execution_20250825"

const WebSearchTool20260209AllowedCallerCodeExecution20260120 WebSearchTool20260209AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]string

optional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](/docs/en/api/messages#user_location)

optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebSearchToolRequestError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebSearchToolResultBlockContentUnion interface{…}

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

type WebSearchToolResultBlockParamResp struct{…}

Content [WebSearchToolResultBlockParamContentUnionResp](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge string

optional

type WebSearchToolRequestError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebSearchToolResultBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebSearchToolResultBlockParamContentUnionResp interface{…}

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge string

optional

type WebSearchToolRequestError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultErrorCode string

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

client.Messages.Batches.New(ctx, body) (\*[MessageBatch](/docs/en/api/messages#message_batch), error)

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

client.Messages.Batches.Get(ctx, messageBatchID) (\*[MessageBatch](/docs/en/api/messages#message_batch), error)

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

client.Messages.Batches.List(ctx, query) (\*Page\[[MessageBatch](/docs/en/api/messages#message_batch)\], error)

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

client.Messages.Batches.Cancel(ctx, messageBatchID) (\*[MessageBatch](/docs/en/api/messages#message_batch), error)

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

client.Messages.Batches.Delete(ctx, messageBatchID) (\*[DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch), error)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

client.Messages.Batches.Results(ctx, messageBatchID) (\*[MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response), error)

GET/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

type DeletedMessageBatch struct{…}

ID string

ID of the Message Batch.

Type MessageBatchDeleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

type MessageBatch struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

ArchivedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

CancelInitiatedAt Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

CreatedAt Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

EndedAt Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

ExpiresAt Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus MessageBatchProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

const MessageBatchProcessingStatusInProgress MessageBatchProcessingStatus = "in_progress"

const MessageBatchProcessingStatusCanceling MessageBatchProcessingStatus = "canceling"

const MessageBatchProcessingStatusEnded MessageBatchProcessingStatus = "ended"

RequestCounts [MessageBatchRequestCounts](/docs/en/api/messages#message_batch_request_counts)

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

type MessageBatchCanceledResult struct{…}

Type Canceled

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](/docs/en/api/$shared#error_response)

Error [ErrorObjectUnion](/docs/en/api/$shared#error_object)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

type AuthenticationError struct{…}

Message string

Type AuthenticationError

type BillingError struct{…}

Message string

Type BillingError

type PermissionError struct{…}

Message string

Type PermissionError

type NotFoundError struct{…}

Message string

Type NotFoundError

type RateLimitError struct{…}

Message string

Type RateLimitError

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

type APIErrorObject struct{…}

Message string

Type APIError

type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored

type MessageBatchExpiredResult struct{…}

Type Expired

type MessageBatchIndividualResponse struct{…}

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

Result [MessageBatchResultUnion](/docs/en/api/messages#message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

type MessageBatchSucceededResult struct{…}

Message [Message](/docs/en/api/messages#message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [Container](/docs/en/api/messages#container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

Content \[\][ContentBlockUnion](/docs/en/api/messages#content_block)

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

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

StopReason [StopReason](/docs/en/api/messages#stop_reason)

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

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](/docs/en/api/messages#usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](/docs/en/api/messages#cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](/docs/en/api/$shared#error_response)

Error [ErrorObjectUnion](/docs/en/api/$shared#error_object)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

type AuthenticationError struct{…}

Message string

Type AuthenticationError

type BillingError struct{…}

Message string

Type BillingError

type PermissionError struct{…}

Message string

Type PermissionError

type NotFoundError struct{…}

Message string

Type NotFoundError

type RateLimitError struct{…}

Message string

Type RateLimitError

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

type APIErrorObject struct{…}

Message string

Type APIError

type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored

type MessageBatchCanceledResult struct{…}

Type Canceled

type MessageBatchExpiredResult struct{…}

Type Expired

type MessageBatchRequestCounts struct{…}

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

type MessageBatchResultUnion interface{…}

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

type MessageBatchSucceededResult struct{…}

Message [Message](/docs/en/api/messages#message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [Container](/docs/en/api/messages#container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

Content \[\][ContentBlockUnion](/docs/en/api/messages#content_block)

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

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

StopReason [StopReason](/docs/en/api/messages#stop_reason)

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

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](/docs/en/api/messages#usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](/docs/en/api/messages#cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](/docs/en/api/$shared#error_response)

Error [ErrorObjectUnion](/docs/en/api/$shared#error_object)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

type AuthenticationError struct{…}

Message string

Type AuthenticationError

type BillingError struct{…}

Message string

Type BillingError

type PermissionError struct{…}

Message string

Type PermissionError

type NotFoundError struct{…}

Message string

Type NotFoundError

type RateLimitError struct{…}

Message string

Type RateLimitError

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

type APIErrorObject struct{…}

Message string

Type APIError

type OverloadedError struct{…}

Message string

Type OverloadedError

RequestID string

Type Error

Type Errored

type MessageBatchCanceledResult struct{…}

Type Canceled

type MessageBatchExpiredResult struct{…}

Type Expired

type MessageBatchSucceededResult struct{…}

Message [Message](/docs/en/api/messages#message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

Container [Container](/docs/en/api/messages#container)

Information about the container used in the request (for the code execution tool)

ID string

Identifier for the container used in this request

ExpiresAt Time

The time at which the container will expire.

Content \[\][ContentBlockUnion](/docs/en/api/messages#content_block)

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

type TextBlock struct{…}

Citations \[\][TextCitationUnion](/docs/en/api/messages#text_citation)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Text string

Type Text

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

type ToolUseBlock struct{…}

ID string

Caller ToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name string

Type ToolUse

type ServerToolUseBlock struct{…}

ID string

Caller ServerToolUseBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Input map\[string, any\]

Name ServerToolUseBlockName

Accepts one of the following:

const ServerToolUseBlockNameWebSearch ServerToolUseBlockName = "web_search"

const ServerToolUseBlockNameWebFetch ServerToolUseBlockName = "web_fetch"

const ServerToolUseBlockNameCodeExecution ServerToolUseBlockName = "code_execution"

const ServerToolUseBlockNameBashCodeExecution ServerToolUseBlockName = "bash_code_execution"

const ServerToolUseBlockNameTextEditorCodeExecution ServerToolUseBlockName = "text_editor_code_execution"

const ServerToolUseBlockNameToolSearchToolRegex ServerToolUseBlockName = "tool_search_tool_regex"

const ServerToolUseBlockNameToolSearchToolBm25 ServerToolUseBlockName = "tool_search_tool_bm25"

Type ServerToolUse

type WebSearchToolResultBlock struct{…}

Caller WebSearchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

URL string

ToolUseID string

Type WebSearchToolResult

type WebFetchToolResultBlock struct{…}

Caller WebFetchToolResultBlockCallerUnion

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

Content WebFetchToolResultBlockContentUnion

Accepts one of the following:

type WebFetchToolResultErrorBlock struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlock struct{…}

Content [DocumentBlock](/docs/en/api/messages#document_block)

Citations [CitationsConfig](/docs/en/api/messages#citations_config)

Citation configuration for the document

Enabled bool

Source DocumentBlockSourceUnion

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

Title string

The title of the document

Type Document

RetrievedAt string

ISO 8601 timestamp when the content was retrieved

Type WebFetchResult

URL string

Fetched content URL

ToolUseID string

Type WebFetchToolResult

type CodeExecutionToolResultBlock struct{…}

Content [CodeExecutionToolResultBlockContentUnion](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultError struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlock struct{…}

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlock struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

type BashCodeExecutionToolResultBlock struct{…}

Content BashCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type BashCodeExecutionToolResultError struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlock struct{…}

Content \[\][BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

type TextEditorCodeExecutionToolResultBlock struct{…}

Content TextEditorCodeExecutionToolResultBlockContentUnion

Accepts one of the following:

type TextEditorCodeExecutionToolResultError struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

ErrorMessage string

Type TextEditorCodeExecutionToolResultError

type TextEditorCodeExecutionViewResultBlock struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockFileTypeText TextEditorCodeExecutionViewResultBlockFileType = "text"

const TextEditorCodeExecutionViewResultBlockFileTypeImage TextEditorCodeExecutionViewResultBlockFileType = "image"

const TextEditorCodeExecutionViewResultBlockFileTypePDF TextEditorCodeExecutionViewResultBlockFileType = "pdf"

NumLines int64

StartLine int64

TotalLines int64

Type TextEditorCodeExecutionViewResult

type TextEditorCodeExecutionCreateResultBlock struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlock struct{…}

Lines \[\]string

NewLines int64

NewStart int64

OldLines int64

OldStart int64

Type TextEditorCodeExecutionStrReplaceResult

ToolUseID string

Type TextEditorCodeExecutionToolResult

type ToolSearchToolResultBlock struct{…}

Content ToolSearchToolResultBlockContentUnion

Accepts one of the following:

type ToolSearchToolResultError struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

ErrorMessage string

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlock struct{…}

ToolReferences \[\][ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)

ToolName string

Type ToolReference

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

type ContainerUploadBlock struct{…}

Response model for a file uploaded to the container.

FileID string

Type ContainerUpload

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

const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

StopReason [StopReason](/docs/en/api/messages#stop_reason)

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

const StopReasonEndTurn [StopReason](/docs/en/api/messages#stop_reason) = "end_turn"

const StopReasonMaxTokens [StopReason](/docs/en/api/messages#stop_reason) = "max_tokens"

const StopReasonStopSequence [StopReason](/docs/en/api/messages#stop_reason) = "stop_sequence"

const StopReasonToolUse [StopReason](/docs/en/api/messages#stop_reason) = "tool_use"

const StopReasonPauseTurn [StopReason](/docs/en/api/messages#stop_reason) = "pause_turn"

const StopReasonRefusal [StopReason](/docs/en/api/messages#stop_reason) = "refusal"

StopSequence string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

Type Message

Object type.

For Messages, this is always `"message"`.

Usage [Usage](/docs/en/api/messages#usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreation [CacheCreation](/docs/en/api/messages#cache_creation)

Breakdown of cached tokens by TTL

Ephemeral1hInputTokens int64

The number of input tokens used to create the 1 hour cache entry.

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

CacheCreationInputTokens int64

The number of input tokens used to create the cache entry.

CacheReadInputTokens int64

The number of input tokens read from the cache.

InferenceGeo string

The geographic region where inference was performed for this request.

InputTokens int64

The number of input tokens which were used.

OutputTokens int64

The number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebFetchRequests int64

The number of web fetch tool requests.

WebSearchRequests int64

The number of web search tool requests.

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

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
