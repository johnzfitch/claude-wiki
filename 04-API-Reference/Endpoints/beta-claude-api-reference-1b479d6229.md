---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:06:21Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta"
title: "Beta - Claude API Reference"
---

# Beta

##### ModelsExpand Collapse 

class BetaApiError:

required string Message

JsonElement Type "api_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing_error"constant

class BetaError: A class that can be one of several variants.union

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid_request_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not_found_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate_limit_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout_error"constant

class BetaApiError:

required string Message

JsonElement Type "api_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded_error"constant

class BetaErrorResponse:

required [BetaError](/docs/en/api/beta#beta_error) Error

Accepts one of the following:

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid_request_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not_found_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate_limit_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout_error"constant

class BetaApiError:

required string Message

JsonElement Type "api_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded_error"constant

required string? RequestID

JsonElement Type "error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout_error"constant

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid_request_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not_found_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate_limit_error"constant

#### BetaModels

##### [List Models](/docs/en/api/beta/models/list)

[ModelListPageResponse](/docs/en/api/beta#ModelListPageResponse) Beta.Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

[BetaModelInfo](/docs/en/api/beta#beta_model_info) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class BetaModelInfo:

required string ID

Unique model identifier.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

required string DisplayName

A human-readable name for the model.

JsonElement Type "model"constant

Object type.

For Models, this is always `"model"`.

#### BetaMessages

##### [Create a Message](/docs/en/api/beta/messages/create)

[BetaMessage](/docs/en/api/beta#beta_message) Beta.Messages.Create(MessageCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages

##### [Count tokens in a Message](/docs/en/api/beta/messages/count_tokens)

[BetaMessageTokensCount](/docs/en/api/beta#beta_message_tokens_count) Beta.Messages.CountTokens(MessageCountTokensParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/count_tokens

##### ModelsExpand Collapse 

class BetaAllThinkingTurns:

JsonElement Type "all"constant

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaBashCodeExecutionOutputBlock:

required string FileID

JsonElement Type "bash_code_execution_output"constant

class BetaBashCodeExecutionOutputBlockParam:

required string FileID

JsonElement Type "bash_code_execution_output"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaCacheControlEphemeral:

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaCacheCreation:

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationConfig:

required Boolean Enabled

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationsConfigParam:

Boolean Enabled

class BetaCitationsDelta:

required Citation Citation

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

JsonElement Type "citations_delta"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaClearThinking20251015Edit:

JsonElement Type "clear_thinking_20251015"constant

Keep Keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonElement Type "thinking_turns"constant

required Long Value

class BetaAllThinkingTurns:

JsonElement Type "all"constant

class All:

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

class BetaClearToolUses20250919Edit:

JsonElement Type "clear_tool_uses_20250919"constant

[BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least)? ClearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonElement Type "input_tokens"constant

required Long Value

ClearToolInputs? ClearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

Boolean

IReadOnlyList\<string\>

IReadOnlyList\<string\>? ExcludeTools

Tool names whose uses are preserved from clearing

[BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) Keep

Number of tool uses to retain in the conversation

JsonElement Type "tool_uses"constant

required Long Value

Trigger Trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonElement Type "input_tokens"constant

required Long Value

class BetaToolUsesTrigger:

JsonElement Type "tool_uses"constant

required Long Value

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaCodeExecutionOutputBlock:

required string FileID

JsonElement Type "code_execution_output"constant

class BetaCodeExecutionOutputBlockParam:

required string FileID

JsonElement Type "code_execution_output"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaCodeExecutionTool20250522:

JsonElement Name "code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code_execution_20250522"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonElement Name "code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code_execution_20250825"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonElement Name "code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code_execution_20260120"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaCodeExecutionToolResultBlockContent: A class that can be one of several variants.union

Code execution result with encrypted stdout for PFC + web_search results.

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaCodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union

Code execution result with encrypted stdout for PFC + web_search results.

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

enum BetaCodeExecutionToolResultErrorCode:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonElement Type "compact_20260112"constant

string? Instructions

Additional instructions for summarization.

Boolean PauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

[BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger)? Trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonElement Type "input_tokens"constant

required Long Value

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

required string? Content

Summary of previously compacted content, or null if compaction failed

JsonElement Type "compaction"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaCompactionContentBlockDelta:

required string? Content

JsonElement Type "compaction_delta"constant

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

class BetaContainer:

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

class BetaContainerParams:

Container parameters with skills to be loaded.

string? ID

Container id

IReadOnlyList\<[BetaSkillParams](/docs/en/api/beta#beta_skill_params)\>? Skills

List of skills to load in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

string Version

Skill version or 'latest' for most recent version

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container_upload"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaContentBlock: A class that can be one of several variants.union

Response model for a file uploaded to the container.

class BetaTextBlock:

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

class BetaContentBlockParam: A class that can be one of several variants.union

Regular text content.

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

class BetaSearchResultBlockParam:

required IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Source

required string Title

JsonElement Type "search_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) Citations

Boolean Enabled

class BetaThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList\<Block\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaSearchResultBlockParam:

required IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Source

required string Title

JsonElement Type "search_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) Citations

Boolean Enabled

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

required string ToolName

JsonElement Type "tool_reference"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean IsError

class BetaServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlockParam:

required [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content) Content

Accepts one of the following:

IReadOnlyList\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

required string EncryptedContent

required string Title

JsonElement Type "web_search_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaBashCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaTextEditorCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

JsonElement Type "text_editor_code_execution_tool_result_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text_editor_code_execution_view_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text_editor_code_execution_str_replace_result"constant

IReadOnlyList\<string\>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaToolSearchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaMcpToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaRequestMcpToolResultBlockParam:

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

Boolean IsError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container_upload"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

required string? Content

Summary of previously compacted content, or null if compaction failed

JsonElement Type "compaction"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaContentBlockSourceContent: A class that can be one of several variants.union

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaContextManagementConfig:

IReadOnlyList\<Edit\> Edits

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit:

JsonElement Type "clear_tool_uses_20250919"constant

[BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least)? ClearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonElement Type "input_tokens"constant

required Long Value

ClearToolInputs? ClearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

Boolean

IReadOnlyList\<string\>

IReadOnlyList\<string\>? ExcludeTools

Tool names whose uses are preserved from clearing

[BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) Keep

Number of tool uses to retain in the conversation

JsonElement Type "tool_uses"constant

required Long Value

Trigger Trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonElement Type "input_tokens"constant

required Long Value

class BetaToolUsesTrigger:

JsonElement Type "tool_uses"constant

required Long Value

class BetaClearThinking20251015Edit:

JsonElement Type "clear_thinking_20251015"constant

Keep Keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonElement Type "thinking_turns"constant

required Long Value

class BetaAllThinkingTurns:

JsonElement Type "all"constant

class All:

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonElement Type "compact_20260112"constant

string? Instructions

Additional instructions for summarization.

Boolean PauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

[BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger)? Trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonElement Type "input_tokens"constant

required Long Value

class BetaContextManagementResponse:

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

class BetaCountTokensContextManagementResponse:

required Long OriginalInputTokens

The original token count before context management was applied

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaDocumentBlock:

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaInputJsonDelta:

required string PartialJson

JsonElement Type "input_json_delta"constant

class BetaInputTokensClearAtLeast:

JsonElement Type "input_tokens"constant

required Long Value

class BetaInputTokensTrigger:

JsonElement Type "input_tokens"constant

required Long Value

class BetaJsonOutputFormat:

required IReadOnlyDictionary\<string, JsonElement\> Schema

The JSON schema of the format

JsonElement Type "json_schema"constant

class BetaMcpToolConfig:

Configuration for a specific tool in an MCP toolset.

Boolean DeferLoading

Boolean Enabled

class BetaMcpToolDefaultConfig:

Default configuration for tools in an MCP toolset.

Boolean DeferLoading

Boolean Enabled

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

required string McpServerName

Name of the MCP server to configure tools for

JsonElement Type "mcp_toolset"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyDictionary\<string, [BetaMcpToolConfig](/docs/en/api/beta#beta_mcp_tool_config)\>? Configs

Configuration overrides for specific tools, keyed by tool name

Boolean DeferLoading

Boolean Enabled

[BetaMcpToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) DefaultConfig

Default configuration applied to all tools from this server

Boolean DeferLoading

Boolean Enabled

class BetaMemoryTool20250818:

JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory_20250818"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818Command: A class that can be one of several variants.union

class BetaMemoryTool20250818ViewCommand:

JsonElement Command "view"constant

Command type identifier

required string Path

Path to directory or file to view

IReadOnlyList\<Long\> ViewRange

Optional line range for viewing specific lines

class BetaMemoryTool20250818CreateCommand:

JsonElement Command "create"constant

Command type identifier

required string FileText

Content to write to the file

required string Path

Path where the file should be created

class BetaMemoryTool20250818StrReplaceCommand:

JsonElement Command "str_replace"constant

Command type identifier

required string NewStr

Text to replace with

required string OldStr

Text to search for and replace

required string Path

Path to the file where text should be replaced

class BetaMemoryTool20250818InsertCommand:

JsonElement Command "insert"constant

Command type identifier

required Long InsertLine

Line number where text should be inserted

required string InsertText

Text to insert at the specified line

required string Path

Path to the file where text should be inserted

class BetaMemoryTool20250818DeleteCommand:

JsonElement Command "delete"constant

Command type identifier

required string Path

Path to the file or directory to delete

class BetaMemoryTool20250818RenameCommand:

JsonElement Command "rename"constant

Command type identifier

required string NewPath

New path for the file or directory

required string OldPath

Current path of the file or directory

class BetaMemoryTool20250818CreateCommand:

JsonElement Command "create"constant

Command type identifier

required string FileText

Content to write to the file

required string Path

Path where the file should be created

class BetaMemoryTool20250818DeleteCommand:

JsonElement Command "delete"constant

Command type identifier

required string Path

Path to the file or directory to delete

class BetaMemoryTool20250818InsertCommand:

JsonElement Command "insert"constant

Command type identifier

required Long InsertLine

Line number where text should be inserted

required string InsertText

Text to insert at the specified line

required string Path

Path to the file where text should be inserted

class BetaMemoryTool20250818RenameCommand:

JsonElement Command "rename"constant

Command type identifier

required string NewPath

New path for the file or directory

required string OldPath

Current path of the file or directory

class BetaMemoryTool20250818StrReplaceCommand:

JsonElement Command "str_replace"constant

Command type identifier

required string NewStr

Text to replace with

required string OldStr

Text to search for and replace

required string Path

Path to the file where text should be replaced

class BetaMemoryTool20250818ViewCommand:

JsonElement Command "view"constant

Command type identifier

required string Path

Path to directory or file to view

IReadOnlyList\<Long\> ViewRange

Optional line range for viewing specific lines

class BetaMessage:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](/docs/en/api/beta#beta_container)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> Content

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

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

required [Model](/docs/en/api/messages#model) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4_6

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude_3_Opus_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude_3_Haiku_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaStopReason](/docs/en/api/beta#beta_stop_reason)? StopReason

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

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](/docs/en/api/beta#beta_usage) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaMessageDeltaUsage:

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The cumulative number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaMessageParam:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

class BetaSearchResultBlockParam:

required IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Source

required string Title

JsonElement Type "search_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) Citations

Boolean Enabled

class BetaThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList\<Block\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaSearchResultBlockParam:

required IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Source

required string Title

JsonElement Type "search_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) Citations

Boolean Enabled

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

required string ToolName

JsonElement Type "tool_reference"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean IsError

class BetaServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlockParam:

required [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content) Content

Accepts one of the following:

IReadOnlyList\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

required string EncryptedContent

required string Title

JsonElement Type "web_search_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaBashCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaTextEditorCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

JsonElement Type "text_editor_code_execution_tool_result_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text_editor_code_execution_view_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text_editor_code_execution_str_replace_result"constant

IReadOnlyList\<string\>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaToolSearchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaMcpToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaRequestMcpToolResultBlockParam:

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

Boolean IsError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container_upload"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

required string? Content

Summary of previously compacted content, or null if compaction failed

JsonElement Type "compaction"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

required Role Role

Accepts one of the following:

"user"User

"assistant"Assistant

class BetaMessageTokensCount:

required [BetaCountTokensContextManagementResponse](/docs/en/api/beta#beta_count_tokens_context_management_response)? ContextManagement

Information about context management applied to the message.

required Long OriginalInputTokens

The original token count before context management was applied

required Long InputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

class BetaMetadata:

string? UserID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

class BetaOutputConfig:

Effort? Effort

All possible effort levels.

Accepts one of the following:

"low"Low

"medium"Medium

"high"High

"max"Max

[BetaJsonOutputFormat](/docs/en/api/beta#beta_json_output_format)? Format

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

required IReadOnlyDictionary\<string, JsonElement\> Schema

The JSON schema of the format

JsonElement Type "json_schema"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaRawContentBlockDelta: A class that can be one of several variants.union

class BetaTextDelta:

required string Text

JsonElement Type "text_delta"constant

class BetaInputJsonDelta:

required string PartialJson

JsonElement Type "input_json_delta"constant

class BetaCitationsDelta:

required Citation Citation

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

JsonElement Type "citations_delta"constant

class BetaThinkingDelta:

required string Thinking

JsonElement Type "thinking_delta"constant

class BetaSignatureDelta:

required string Signature

JsonElement Type "signature_delta"constant

class BetaCompactionContentBlockDelta:

required string? Content

JsonElement Type "compaction_delta"constant

class BetaRawContentBlockDeltaEvent:

required [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta) Delta

Accepts one of the following:

class BetaTextDelta:

required string Text

JsonElement Type "text_delta"constant

class BetaInputJsonDelta:

required string PartialJson

JsonElement Type "input_json_delta"constant

class BetaCitationsDelta:

required Citation Citation

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

JsonElement Type "citations_delta"constant

class BetaThinkingDelta:

required string Thinking

JsonElement Type "thinking_delta"constant

class BetaSignatureDelta:

required string Signature

JsonElement Type "signature_delta"constant

class BetaCompactionContentBlockDelta:

required string? Content

JsonElement Type "compaction_delta"constant

required Long Index

JsonElement Type "content_block_delta"constant

class BetaRawContentBlockStartEvent:

required ContentBlock ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock:

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required Long Index

JsonElement Type "content_block_start"constant

class BetaRawContentBlockStopEvent:

required Long Index

JsonElement Type "content_block_stop"constant

class BetaRawMessageDeltaEvent:

required [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)? ContextManagement

Information about context management strategies applied during the request

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

required Delta Delta

required [BetaContainer](/docs/en/api/beta#beta_container)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required [BetaStopReason](/docs/en/api/beta#beta_stop_reason)? StopReason

Accepts one of the following:

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

required string? StopSequence

JsonElement Type "message_delta"constant

required [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The cumulative number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class BetaRawMessageStartEvent:

required [BetaMessage](/docs/en/api/beta#beta_message) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](/docs/en/api/beta#beta_container)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> Content

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

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

required [Model](/docs/en/api/messages#model) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4_6

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude_3_Opus_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude_3_Haiku_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaStopReason](/docs/en/api/beta#beta_stop_reason)? StopReason

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

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](/docs/en/api/beta#beta_usage) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "message_start"constant

class BetaRawMessageStopEvent:

JsonElement Type "message_stop"constant

class BetaRawMessageStreamEvent: A class that can be one of several variants.union

class BetaRawMessageStartEvent:

required [BetaMessage](/docs/en/api/beta#beta_message) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](/docs/en/api/beta#beta_container)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> Content

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

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

required [Model](/docs/en/api/messages#model) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4_6

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude_3_Opus_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude_3_Haiku_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaStopReason](/docs/en/api/beta#beta_stop_reason)? StopReason

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

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](/docs/en/api/beta#beta_usage) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "message_start"constant

class BetaRawMessageDeltaEvent:

required [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)? ContextManagement

Information about context management strategies applied during the request

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

required Delta Delta

required [BetaContainer](/docs/en/api/beta#beta_container)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required [BetaStopReason](/docs/en/api/beta#beta_stop_reason)? StopReason

Accepts one of the following:

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

required string? StopSequence

JsonElement Type "message_delta"constant

required [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required Long? CacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The cumulative number of input tokens read from the cache.

required Long? InputTokens

The cumulative number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The cumulative number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class BetaRawMessageStopEvent:

JsonElement Type "message_stop"constant

class BetaRawContentBlockStartEvent:

required ContentBlock ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock:

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required Long Index

JsonElement Type "content_block_start"constant

class BetaRawContentBlockDeltaEvent:

required [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta) Delta

Accepts one of the following:

class BetaTextDelta:

required string Text

JsonElement Type "text_delta"constant

class BetaInputJsonDelta:

required string PartialJson

JsonElement Type "input_json_delta"constant

class BetaCitationsDelta:

required Citation Citation

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

JsonElement Type "citations_delta"constant

class BetaThinkingDelta:

required string Thinking

JsonElement Type "thinking_delta"constant

class BetaSignatureDelta:

required string Signature

JsonElement Type "signature_delta"constant

class BetaCompactionContentBlockDelta:

required string? Content

JsonElement Type "compaction_delta"constant

required Long Index

JsonElement Type "content_block_delta"constant

class BetaRawContentBlockStopEvent:

required Long Index

JsonElement Type "content_block_stop"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaRedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

class BetaRequestMcpServerToolConfiguration:

IReadOnlyList\<string\>? AllowedTools

Boolean? Enabled

class BetaRequestMcpServerUrlDefinition:

required string Name

JsonElement Type "url"constant

required string Url

string? AuthorizationToken

[BetaRequestMcpServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration)? ToolConfiguration

IReadOnlyList\<string\>? AllowedTools

Boolean? Enabled

class BetaRequestMcpToolResultBlockParam:

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

Boolean IsError

class BetaSearchResultBlockParam:

required IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Source

required string Title

JsonElement Type "search_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) Citations

Boolean Enabled

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUsage:

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaSignatureDelta:

required string Signature

JsonElement Type "signature_delta"constant

class BetaSkill:

A skill that was loaded in a container (response model).

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

class BetaSkillParams:

Specification for a skill to be loaded in a container (request model).

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

string Version

Skill version or 'latest' for most recent version

enum BetaStopReason:

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

class BetaTextBlock:

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaTextCitation: A class that can be one of several variants.union

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaTextCitationParam: A class that can be one of several variants.union

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaTextDelta:

required string Text

JsonElement Type "text_delta"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text_editor_code_execution_str_replace_result"constant

IReadOnlyList\<string\>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

JsonElement Type "text_editor_code_execution_tool_result_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text_editor_code_execution_view_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text_editor_code_execution_str_replace_result"constant

IReadOnlyList\<string\>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

JsonElement Type "text_editor_code_execution_tool_result_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text_editor_code_execution_view_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaThinkingConfigAdaptive:

JsonElement Type "adaptive"constant

class BetaThinkingConfigDisabled:

JsonElement Type "disabled"constant

class BetaThinkingConfigEnabled:

required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant

class BetaThinkingConfigParam: A class that can be one of several variants.union

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

class BetaThinkingConfigEnabled:

required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant

class BetaThinkingConfigDisabled:

JsonElement Type "disabled"constant

class BetaThinkingConfigAdaptive:

JsonElement Type "adaptive"constant

class BetaThinkingDelta:

required string Thinking

JsonElement Type "thinking_delta"constant

class BetaThinkingTurns:

JsonElement Type "thinking_turns"constant

required Long Value

class BetaTool:

required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary\<string, JsonElement\>? Properties

IReadOnlyList\<string\>? Required

required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class BetaToolBash20241022:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash_20241022"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash_20250124"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant

class BetaToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolComputerUse20241022:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer_20241022"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer_20250124"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer_20251124"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

Boolean EnableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolReferenceBlock:

required string ToolName

JsonElement Type "tool_reference"constant

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

required string ToolName

JsonElement Type "tool_reference"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList\<Block\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaSearchResultBlockParam:

required IReadOnlyList\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Source

required string Title

JsonElement Type "search_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) Citations

Boolean Enabled

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

required string ToolName

JsonElement Type "tool_reference"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean IsError

class BetaToolSearchToolBm25_20251119:

JsonElement Name "tool_search_tool_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool_search_tool_bm25_20251119"ToolSearchToolBm25_20251119

"tool_search_tool_bm25"ToolSearchToolBm25

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonElement Name "tool_search_tool_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool_search_tool_regex_20251119"ToolSearchToolRegex20251119

"tool_search_tool_regex"ToolSearchToolRegex

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaToolSearchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool_search_tool_search_result"constant

class BetaToolTextEditor20241022:

JsonElement Name "str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text_editor_20241022"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonElement Name "str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text_editor_20250124"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonElement Name "str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text_editor_20250429"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonElement Name "str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text_editor_20250728"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolUnion: A class that can be one of several variants.union

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

class BetaTool:

required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary\<string, JsonElement\>? Properties

IReadOnlyList\<string\>? Required

required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class BetaToolBash20241022:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash_20241022"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash_20250124"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522:

JsonElement Name "code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code_execution_20250522"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonElement Name "code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code_execution_20250825"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonElement Name "code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code_execution_20260120"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer_20241022"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818:

JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory_20250818"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer_20250124"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022:

JsonElement Name "str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text_editor_20241022"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer_20251124"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

Boolean EnableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonElement Name "str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text_editor_20250124"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonElement Name "str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text_editor_20250429"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonElement Name "str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text_editor_20250728"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

IReadOnlyList\<IReadOnlyDictionary\<string, JsonElement\>\> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305:

JsonElement Name "web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web_search_20250305"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

IReadOnlyList\<string\>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList\<string\>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

[BetaUserLocation](/docs/en/api/beta#beta_user_location)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchTool20250910:

JsonElement Name "web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web_fetch_20250910"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

IReadOnlyList\<string\>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList\<string\>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20260209:

JsonElement Name "web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web_search_20260209"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

IReadOnlyList\<string\>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList\<string\>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

[BetaUserLocation](/docs/en/api/beta#beta_user_location)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchTool20260209:

JsonElement Name "web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web_fetch_20260209"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

IReadOnlyList\<string\>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList\<string\>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolBm25_20251119:

JsonElement Name "tool_search_tool_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool_search_tool_bm25_20251119"ToolSearchToolBm25_20251119

"tool_search_tool_bm25"ToolSearchToolBm25

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonElement Name "tool_search_tool_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool_search_tool_regex_20251119"ToolSearchToolRegex20251119

"tool_search_tool_regex"ToolSearchToolRegex

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

required string McpServerName

Name of the MCP server to configure tools for

JsonElement Type "mcp_toolset"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyDictionary\<string, [BetaMcpToolConfig](/docs/en/api/beta#beta_mcp_tool_config)\>? Configs

Configuration overrides for specific tools, keyed by tool name

Boolean DeferLoading

Boolean Enabled

[BetaMcpToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) DefaultConfig

Default configuration applied to all tools from this server

Boolean DeferLoading

Boolean Enabled

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaToolUseBlockParam:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaToolUsesKeep:

JsonElement Type "tool_uses"constant

required Long Value

class BetaToolUsesTrigger:

JsonElement Type "tool_uses"constant

required Long Value

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaUsage:

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaUserLocation:

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

class BetaWebFetchTool20250910:

JsonElement Name "web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web_fetch_20250910"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

IReadOnlyList\<string\>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList\<string\>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260209:

JsonElement Name "web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web_fetch_20260209"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

IReadOnlyList\<string\>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList\<string\>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

enum BetaWebFetchToolResultErrorCode:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

class BetaWebSearchResultBlock:

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

class BetaWebSearchResultBlockParam:

required string EncryptedContent

required string Title

JsonElement Type "web_search_result"constant

required string Url

string? PageAge

class BetaWebSearchTool20250305:

JsonElement Name "web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web_search_20250305"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

IReadOnlyList\<string\>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList\<string\>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

[BetaUserLocation](/docs/en/api/beta#beta_user_location)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebSearchTool20260209:

JsonElement Name "web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web_search_20260209"constant

IReadOnlyList\<AllowedCaller\> AllowedCallers

Accepts one of the following:

"direct"Direct

"code_execution_20250825"CodeExecution20250825

"code_execution_20260120"CodeExecution20260120

IReadOnlyList\<string\>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList\<string\>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

[BetaUserLocation](/docs/en/api/beta#beta_user_location)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlockContent: A class that can be one of several variants.union

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

class BetaWebSearchToolResultBlockParam:

required [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content) Content

Accepts one of the following:

IReadOnlyList\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

required string EncryptedContent

required string Title

JsonElement Type "web_search_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlockParamContent: A class that can be one of several variants.union

IReadOnlyList\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

required string EncryptedContent

required string Title

JsonElement Type "web_search_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

enum BetaWebSearchToolResultErrorCode:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

#### BetaMessagesBatches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) Beta.Messages.Batches.Create(BatchCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) Beta.Messages.Batches.Retrieve(BatchRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

[BatchListPageResponse](/docs/en/api/beta#BatchListPageResponse) Beta.Messages.Batches.List(BatchListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) Beta.Messages.Batches.Cancel(BatchCancelParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

[BetaDeletedMessageBatch](/docs/en/api/beta#beta_deleted_message_batch) Beta.Messages.Batches.Delete(BatchDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

[BetaMessageBatchIndividualResponse](/docs/en/api/beta#beta_message_batch_individual_response) Beta.Messages.Batches.ResultsStreaming(BatchResultsParamsparameters, CancellationTokencancellationToken = default)

GET/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class BetaDeletedMessageBatch:

required string ID

ID of the Message Batch.

JsonElement Type "message_batch_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class BetaMessageBatch:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset? ArchivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

required DateTimeOffset? CancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

required DateTimeOffset? EndedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

required DateTimeOffset ExpiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

required ProcessingStatus ProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

"in_progress"InProgress

"canceling"Canceling

"ended"Ended

required [BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts) RequestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

required Long Canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

required Long Errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

required Long Expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

required Long Processing

Number of requests in the Message Batch that are processing.

required Long Succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

required string? ResultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

JsonElement Type "message_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

class BetaMessageBatchCanceledResult:

JsonElement Type "canceled"constant

class BetaMessageBatchErroredResult:

required [BetaErrorResponse](/docs/en/api/beta#beta_error_response) Error

required [BetaError](/docs/en/api/beta#beta_error) Error

Accepts one of the following:

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid_request_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not_found_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate_limit_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout_error"constant

class BetaApiError:

required string Message

JsonElement Type "api_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class BetaMessageBatchExpiredResult:

JsonElement Type "expired"constant

class BetaMessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

required string CustomID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

required [BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result) Result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult:

required [BetaMessage](/docs/en/api/beta#beta_message) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](/docs/en/api/beta#beta_container)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> Content

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

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

required [Model](/docs/en/api/messages#model) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4_6

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude_3_Opus_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude_3_Haiku_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaStopReason](/docs/en/api/beta#beta_stop_reason)? StopReason

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

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](/docs/en/api/beta#beta_usage) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "succeeded"constant

class BetaMessageBatchErroredResult:

required [BetaErrorResponse](/docs/en/api/beta#beta_error_response) Error

required [BetaError](/docs/en/api/beta#beta_error) Error

Accepts one of the following:

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid_request_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not_found_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate_limit_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout_error"constant

class BetaApiError:

required string Message

JsonElement Type "api_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class BetaMessageBatchCanceledResult:

JsonElement Type "canceled"constant

class BetaMessageBatchExpiredResult:

JsonElement Type "expired"constant

class BetaMessageBatchRequestCounts:

required Long Canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

required Long Errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

required Long Expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

required Long Processing

Number of requests in the Message Batch that are processing.

required Long Succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

class BetaMessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class BetaMessageBatchSucceededResult:

required [BetaMessage](/docs/en/api/beta#beta_message) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](/docs/en/api/beta#beta_container)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> Content

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

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

required [Model](/docs/en/api/messages#model) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4_6

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude_3_Opus_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude_3_Haiku_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaStopReason](/docs/en/api/beta#beta_stop_reason)? StopReason

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

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](/docs/en/api/beta#beta_usage) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "succeeded"constant

class BetaMessageBatchErroredResult:

required [BetaErrorResponse](/docs/en/api/beta#beta_error_response) Error

required [BetaError](/docs/en/api/beta#beta_error) Error

Accepts one of the following:

class BetaInvalidRequestError:

required string Message

JsonElement Type "invalid_request_error"constant

class BetaAuthenticationError:

required string Message

JsonElement Type "authentication_error"constant

class BetaBillingError:

required string Message

JsonElement Type "billing_error"constant

class BetaPermissionError:

required string Message

JsonElement Type "permission_error"constant

class BetaNotFoundError:

required string Message

JsonElement Type "not_found_error"constant

class BetaRateLimitError:

required string Message

JsonElement Type "rate_limit_error"constant

class BetaGatewayTimeoutError:

required string Message

JsonElement Type "timeout_error"constant

class BetaApiError:

required string Message

JsonElement Type "api_error"constant

class BetaOverloadedError:

required string Message

JsonElement Type "overloaded_error"constant

required string? RequestID

JsonElement Type "error"constant

JsonElement Type "errored"constant

class BetaMessageBatchCanceledResult:

JsonElement Type "canceled"constant

class BetaMessageBatchExpiredResult:

JsonElement Type "expired"constant

class BetaMessageBatchSucceededResult:

required [BetaMessage](/docs/en/api/beta#beta_message) Message

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required [BetaContainer](/docs/en/api/beta#beta_container)? Container

Information about the container used in the request (for the code execution tool)

required string ID

Identifier for the container used in this request

required DateTimeOffset ExpiresAt

The time at which the container will expire.

required IReadOnlyList\<[BetaSkill](/docs/en/api/beta#beta_skill)\>? Skills

Skills loaded in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

required string Version

Skill version or 'latest' for most recent version

required IReadOnlyList\<[BetaContentBlock](/docs/en/api/beta#beta_content_block)\> Content

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

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

class BetaThinkingBlock:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlock:

required string Data

JsonElement Type "redacted_thinking"constant

class BetaToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

JsonElement Type "tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaServerToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required Name Name

Accepts one of the following:

"web_search"WebSearch

"web_fetch"WebFetch

"code_execution"CodeExecution

"bash_code_execution"BashCodeExecution

"text_editor_code_execution"TextEditorCodeExecution

"tool_search_tool_regex"ToolSearchToolRegex

"tool_search_tool_bm25"ToolSearchToolBm25

JsonElement Type "server_tool_use"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebSearchToolResultBlock:

required [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content) Content

Accepts one of the following:

class BetaWebSearchToolResultError:

required [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"max_uses_exceeded"MaxUsesExceeded

"too_many_requests"TooManyRequests

"query_too_long"QueryTooLong

"request_too_large"RequestTooLarge

JsonElement Type "web_search_tool_result_error"constant

IReadOnlyList\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

required string EncryptedContent

required string? PageAge

required string Title

JsonElement Type "web_search_result"constant

required string Url

required string ToolUseID

JsonElement Type "web_search_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaWebFetchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

required [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"url_too_long"UrlTooLong

"url_not_allowed"UrlNotAllowed

"url_not_accessible"UrlNotAccessible

"unsupported_content_type"UnsupportedContentType

"too_many_requests"TooManyRequests

"max_uses_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

required [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) Content

required [BetaCitationConfig](/docs/en/api/beta#beta_citation_config)? Citations

Citation configuration for the document

required Boolean Enabled

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

required string? Title

The title of the document

JsonElement Type "document"constant

required string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

JsonElement Type "web_fetch_result"constant

required string Url

Fetched content URL

required string ToolUseID

JsonElement Type "web_fetch_tool_result"constant

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code_execution_20250825"constant

class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

required [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) Content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

required [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

JsonElement Type "code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

required IReadOnlyList\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> Content

required string FileID

JsonElement Type "code_execution_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted_code_execution_result"constant

required string ToolUseID

JsonElement Type "code_execution_tool_result"constant

class BetaBashCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"output_file_too_large"OutputFileTooLarge

JsonElement Type "bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

required IReadOnlyList\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> Content

required string FileID

JsonElement Type "bash_code_execution_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash_code_execution_result"constant

required string ToolUseID

JsonElement Type "bash_code_execution_tool_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

"file_not_found"FileNotFound

required string? ErrorMessage

JsonElement Type "text_editor_code_execution_tool_result_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

required Long? NumLines

required Long? StartLine

required Long? TotalLines

JsonElement Type "text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

required Boolean IsFileUpdate

JsonElement Type "text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

required IReadOnlyList\<string\>? Lines

required Long? NewLines

required Long? NewStart

required Long? OldLines

required Long? OldStart

JsonElement Type "text_editor_code_execution_str_replace_result"constant

required string ToolUseID

JsonElement Type "text_editor_code_execution_tool_result"constant

class BetaToolSearchToolResultBlock:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultError:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid_tool_input"InvalidToolInput

"unavailable"Unavailable

"too_many_requests"TooManyRequests

"execution_time_exceeded"ExecutionTimeExceeded

required string? ErrorMessage

JsonElement Type "tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

required IReadOnlyList\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> ToolReferences

required string ToolName

JsonElement Type "tool_reference"constant

JsonElement Type "tool_search_tool_search_result"constant

required string ToolUseID

JsonElement Type "tool_search_tool_result"constant

class BetaMcpToolUseBlock:

required string ID

required IReadOnlyDictionary\<string, JsonElement\> Input

required string Name

The name of the MCP tool

required string ServerName

The name of the MCP server

JsonElement Type "mcp_tool_use"constant

class BetaMcpToolResultBlock:

required Content Content

Accepts one of the following:

string

IReadOnlyList\<[BetaTextBlock](/docs/en/api/beta#beta_text_block)\>

required IReadOnlyList\<[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\>? Citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required string? FileID

required Long StartCharIndex

JsonElement Type "char_location"constant

class BetaCitationPageLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required string? FileID

required Long StartPageNumber

JsonElement Type "page_location"constant

class BetaCitationContentBlockLocation:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required string? FileID

required Long StartBlockIndex

JsonElement Type "content_block_location"constant

class BetaCitationsWebSearchResultLocation:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web_search_result_location"constant

required string Url

class BetaCitationSearchResultLocation:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search_result_location"constant

required string Text

JsonElement Type "text"constant

required Boolean IsError

required string ToolUseID

JsonElement Type "mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

required string FileID

JsonElement Type "container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

required string? Content

Summary of compacted content, or null if compaction failed

JsonElement Type "compaction"constant

required [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)? ContextManagement

Context management response.

Information about context management strategies applied during the request.

required IReadOnlyList\<AppliedEdit\> AppliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedToolUses

Number of tool uses that were cleared.

JsonElement Type "clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

required Long ClearedInputTokens

Number of input tokens cleared by this edit.

required Long ClearedThinkingTurns

Number of thinking turns that were cleared.

JsonElement Type "clear_thinking_20251015"constant

The type of context management edit applied.

required [Model](/docs/en/api/messages#model) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4_6

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude_3_Opus_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude_3_Haiku_20240307

Our previous most fast and cost-effective

JsonElement Role "assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

required [BetaStopReason](/docs/en/api/beta#beta_stop_reason)? StopReason

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

"end_turn"EndTurn

"max_tokens"MaxTokens

"stop_sequence"StopSequence

"tool_use"ToolUse

"pause_turn"PauseTurn

"compaction"Compaction

"refusal"Refusal

"model_context_window_exceeded"ModelContextWindowExceeded

required string? StopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonElement Type "message"constant

Object type.

For Messages, this is always `"message"`.

required [BetaUsage](/docs/en/api/beta#beta_usage) Usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long? CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long? CacheReadInputTokens

The number of input tokens read from the cache.

required string? InferenceGeo

The geographic region where inference was performed for this request.

required Long InputTokens

The number of input tokens which were used.

required IReadOnlyList\<BetaIterationsUsageItems\>? Iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

required [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)? CacheCreation

Breakdown of cached tokens by TTL

required Long Ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

required Long Ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

required Long CacheCreationInputTokens

The number of input tokens used to create the cache entry.

required Long CacheReadInputTokens

The number of input tokens read from the cache.

required Long InputTokens

The number of input tokens which were used.

required Long OutputTokens

The number of output tokens which were used.

JsonElement Type "compaction"constant

Usage for a compaction iteration

required Long OutputTokens

The number of output tokens which were used.

required [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)? ServerToolUse

The number of server tool requests.

required Long WebFetchRequests

The number of web fetch tool requests.

required Long WebSearchRequests

The number of web search tool requests.

required ServiceTier? ServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"Standard

"priority"Priority

"batch"Batch

required Speed? Speed

The inference speed mode used for this request.

Accepts one of the following:

"standard"Standard

"fast"Fast

JsonElement Type "succeeded"constant

#### BetaFiles

##### [Upload File](/docs/en/api/beta/files/upload)

[FileMetadata](/docs/en/api/beta#file_metadata) Beta.Files.Upload(FileUploadParamsparameters, CancellationTokencancellationToken = default)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

[FileListPageResponse](/docs/en/api/beta#FileListPageResponse) Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

[FileMetadata](/docs/en/api/beta#file_metadata) Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

[DeletedFile](/docs/en/api/beta#deleted_file) Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

class DeletedFile:

required string ID

ID of the deleted file.

Type Type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing when the file was created.

required string Filename

Original filename of the uploaded file.

required string MimeType

MIME type of the file.

required Long SizeBytes

Size of the file in bytes.

JsonElement Type "file"constant

Object type.

For files, this is always `"file"`.

Boolean Downloadable

Whether the file can be downloaded.

#### BetaSkills

##### [Create Skill](/docs/en/api/beta/skills/create)

[SkillCreateResponse](/docs/en/api/beta#SkillCreateResponse) Beta.Skills.Create(SkillCreateParams?parameters, CancellationTokencancellationToken = default)

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

[SkillListPageResponse](/docs/en/api/beta#SkillListPageResponse) Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

[SkillRetrieveResponse](/docs/en/api/beta#SkillRetrieveResponse) Beta.Skills.Retrieve(SkillRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

[SkillDeleteResponse](/docs/en/api/beta#SkillDeleteResponse) Beta.Skills.Delete(SkillDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill_id}

#### BetaSkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

[VersionCreateResponse](/docs/en/api/beta#VersionCreateResponse) Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

[VersionListPageResponse](/docs/en/api/beta#VersionListPageResponse) Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

[VersionRetrieveResponse](/docs/en/api/beta#VersionRetrieveResponse) Beta.Skills.Versions.Retrieve(VersionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

[VersionDeleteResponse](/docs/en/api/beta#VersionDeleteResponse) Beta.Skills.Versions.Delete(VersionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill_id}/versions/{version}
