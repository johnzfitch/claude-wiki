---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:08:48Z"
source_url: "https://platform.claude.com/docs/en/api/java/beta/messages"
title: "Messages - Claude API Reference"
---

Copy page

Java

# Messages

##### [Create a Message](/docs/en/api/beta/messages/create)

[BetaMessage](/docs/en/api/beta#beta_message) beta().messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages

##### [Count tokens in a Message](/docs/en/api/beta/messages/count_tokens)

[BetaMessageTokensCount](/docs/en/api/beta#beta_message_tokens_count) beta().messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages/count_tokens

##### ModelsExpand Collapse 

class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

Accepts one of the following:

ALL("all")

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaBashCodeExecutionOutputBlock:

String fileId

JsonValue; type "bash_code_execution_output"constant"bash_code_execution_output"constant

Accepts one of the following:

BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")

class BetaBashCodeExecutionOutputBlockParam:

String fileId

JsonValue; type "bash_code_execution_output"constant"bash_code_execution_output"constant

Accepts one of the following:

BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")

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

class BetaBashCodeExecutionResultBlockParam:

List\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> content

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

class BetaBashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

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

class BetaBashCodeExecutionResultBlockParam:

List\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> content

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaBashCodeExecutionToolResultErrorParam:

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

class BetaCacheControlEphemeral:

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaCacheCreation:

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

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

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationConfig:

boolean enabled

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

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

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

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

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

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationsConfigParam:

Optional\<Boolean\> enabled

class BetaCitationsDelta:

Citation citation

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

JsonValue; type "citations_delta"constant"citations_delta"constant

Accepts one of the following:

CITATIONS_DELTA("citations_delta")

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaClearThinking20251015Edit:

JsonValue; type "clear_thinking_20251015"constant"clear_thinking_20251015"constant

Accepts one of the following:

CLEAR_THINKING_20251015("clear_thinking_20251015")

Optional\<Keep\> keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonValue; type "thinking_turns"constant"thinking_turns"constant

Accepts one of the following:

THINKING_TURNS("thinking_turns")

long value

class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

Accepts one of the following:

ALL("all")

JsonValue;

Accepts one of the following:

ALL("all")

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

class BetaClearToolUses20250919Edit:

JsonValue; type "clear_tool_uses_20250919"constant"clear_tool_uses_20250919"constant

Accepts one of the following:

CLEAR_TOOL_USES_20250919("clear_tool_uses_20250919")

Optional\<[BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least)\> clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

Optional\<ClearToolInputs\> clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

boolean

List\<String\>

Optional\<List\<String\>\> excludeTools

Tool names whose uses are preserved from clearing

Optional\<[BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep)\> keep

Number of tool uses to retain in the conversation

JsonValue; type "tool_uses"constant"tool_uses"constant

Accepts one of the following:

TOOL_USES("tool_uses")

long value

Optional\<Trigger\> trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

class BetaToolUsesTrigger:

JsonValue; type "tool_uses"constant"tool_uses"constant

Accepts one of the following:

TOOL_USES("tool_uses")

long value

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

class BetaCodeExecutionOutputBlock:

String fileId

JsonValue; type "code_execution_output"constant"code_execution_output"constant

Accepts one of the following:

CODE_EXECUTION_OUTPUT("code_execution_output")

class BetaCodeExecutionOutputBlockParam:

String fileId

JsonValue; type "code_execution_output"constant"code_execution_output"constant

Accepts one of the following:

CODE_EXECUTION_OUTPUT("code_execution_output")

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

class BetaCodeExecutionResultBlockParam:

List\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> content

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

class BetaCodeExecutionTool20250522:

JsonValue; name "code_execution"constant"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE_EXECUTION("code_execution")

JsonValue; type "code_execution_20250522"constant"code_execution_20250522"constant

Accepts one of the following:

CODE_EXECUTION_20250522("code_execution_20250522")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonValue; name "code_execution"constant"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE_EXECUTION("code_execution")

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

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

class BetaCodeExecutionToolResultBlockContent: A class that can be one of several variants.union

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

class BetaCodeExecutionToolResultBlockParam:

[BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content) content

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCodeExecutionResultBlockParam:

List\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> content

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaCodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCodeExecutionResultBlockParam:

List\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> content

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

enum BetaCodeExecutionToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonValue; type "compact_20260112"constant"compact_20260112"constant

Accepts one of the following:

COMPACT_20260112("compact_20260112")

Optional\<String\> instructions

Additional instructions for summarization.

Optional\<Boolean\> pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

Optional\<[BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger)\> trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Optional\<String\> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Accepts one of the following:

COMPACTION("compaction")

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

Optional\<String\> content

Summary of previously compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Accepts one of the following:

COMPACTION("compaction")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaCompactionContentBlockDelta:

Optional\<String\> content

JsonValue; type "compaction_delta"constant"compaction_delta"constant

Accepts one of the following:

COMPACTION_DELTA("compaction_delta")

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

class BetaContainer:

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

class BetaContainerParams:

Container parameters with skills to be loaded.

Optional\<String\> id

Container id

Optional\<List\<[BetaSkillParams](/docs/en/api/beta#beta_skill_params)\>\> skills

List of skills to load in the container

String skillId

Skill ID

maxLength64

minLength1

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional\<String\> version

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant"container_upload"constant

Accepts one of the following:

CONTAINER_UPLOAD("container_upload")

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container_upload"constant"container_upload"constant

Accepts one of the following:

CONTAINER_UPLOAD("container_upload")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaContentBlock: A class that can be one of several variants.union

Response model for a file uploaded to the container.

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

class BetaContentBlockParam: A class that can be one of several variants.union

Regular text content.

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaRequestDocumentBlock:

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String source

String title

JsonValue; type "search_result"constant"search_result"constant

Accepts one of the following:

SEARCH_RESULT("search_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant"tool_result"constant

Accepts one of the following:

TOOL_RESULT("tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Content\> content

Accepts one of the following:

String

List\<Block\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String source

String title

JsonValue; type "search_result"constant"search_result"constant

Accepts one of the following:

SEARCH_RESULT("search_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaRequestDocumentBlock:

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> isError

class BetaServerToolUseBlockParam:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaWebSearchToolResultBlockParam:

[BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class BetaWebSearchToolRequestError:

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

String toolUseId

JsonValue; type "web_search_tool_result"constant"web_search_tool_result"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT("web_search_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaWebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

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

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) content

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant"web_fetch_result"constant

Accepts one of the following:

WEB_FETCH_RESULT("web_fetch_result")

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web_fetch_tool_result"constant"web_fetch_tool_result"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaCodeExecutionToolResultBlockParam:

[BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content) content

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCodeExecutionResultBlockParam:

List\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> content

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaBashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

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

class BetaBashCodeExecutionResultBlockParam:

List\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> content

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaTextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

JsonValue; type "text_editor_code_execution_tool_result_error"constant"text_editor_code_execution_tool_result_error"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")

Optional\<String\> errorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant"text_editor_code_execution_view_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant"text_editor_code_execution_create_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant"text_editor_code_execution_str_replace_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant"text_editor_code_execution_tool_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "tool_search_tool_result_error"constant"tool_search_tool_result_error"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")

class BetaToolSearchToolSearchResultBlockParam:

List\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "tool_search_tool_search_result"constant"tool_search_tool_search_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")

String toolUseId

JsonValue; type "tool_search_tool_result"constant"tool_search_tool_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant"mcp_tool_use"constant

Accepts one of the following:

MCP_TOOL_USE("mcp_tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp_tool_result"constant"mcp_tool_result"constant

Accepts one of the following:

MCP_TOOL_RESULT("mcp_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Content\> content

Accepts one of the following:

String

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

Optional\<Boolean\> isError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container_upload"constant"container_upload"constant

Accepts one of the following:

CONTAINER_UPLOAD("container_upload")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

Optional\<String\> content

Summary of previously compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Accepts one of the following:

COMPACTION("compaction")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaContentBlockSourceContent: A class that can be one of several variants.union

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaContextManagementConfig:

Optional\<List\<Edit\>\> edits

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit:

JsonValue; type "clear_tool_uses_20250919"constant"clear_tool_uses_20250919"constant

Accepts one of the following:

CLEAR_TOOL_USES_20250919("clear_tool_uses_20250919")

Optional\<[BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least)\> clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

Optional\<ClearToolInputs\> clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

boolean

List\<String\>

Optional\<List\<String\>\> excludeTools

Tool names whose uses are preserved from clearing

Optional\<[BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep)\> keep

Number of tool uses to retain in the conversation

JsonValue; type "tool_uses"constant"tool_uses"constant

Accepts one of the following:

TOOL_USES("tool_uses")

long value

Optional\<Trigger\> trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

class BetaToolUsesTrigger:

JsonValue; type "tool_uses"constant"tool_uses"constant

Accepts one of the following:

TOOL_USES("tool_uses")

long value

class BetaClearThinking20251015Edit:

JsonValue; type "clear_thinking_20251015"constant"clear_thinking_20251015"constant

Accepts one of the following:

CLEAR_THINKING_20251015("clear_thinking_20251015")

Optional\<Keep\> keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonValue; type "thinking_turns"constant"thinking_turns"constant

Accepts one of the following:

THINKING_TURNS("thinking_turns")

long value

class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

Accepts one of the following:

ALL("all")

JsonValue;

Accepts one of the following:

ALL("all")

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonValue; type "compact_20260112"constant"compact_20260112"constant

Accepts one of the following:

COMPACT_20260112("compact_20260112")

Optional\<String\> instructions

Additional instructions for summarization.

Optional\<Boolean\> pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

Optional\<[BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger)\> trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

class BetaContextManagementResponse:

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

class BetaCountTokensContextManagementResponse:

long originalInputTokens

The original token count before context management was applied

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaDocumentBlock:

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

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant"input_json_delta"constant

Accepts one of the following:

INPUT_JSON_DELTA("input_json_delta")

class BetaInputTokensClearAtLeast:

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

class BetaInputTokensTrigger:

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

class BetaJsonOutputFormat:

Schema schema

The JSON schema of the format

JsonValue; type "json_schema"constant"json_schema"constant

Accepts one of the following:

JSON_SCHEMA("json_schema")

class BetaMcpToolConfig:

Configuration for a specific tool in an MCP toolset.

Optional\<Boolean\> deferLoading

Optional\<Boolean\> enabled

class BetaMcpToolDefaultConfig:

Default configuration for tools in an MCP toolset.

Optional\<Boolean\> deferLoading

Optional\<Boolean\> enabled

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

class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant"mcp_tool_use"constant

Accepts one of the following:

MCP_TOOL_USE("mcp_tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

String mcpServerName

Name of the MCP server to configure tools for

maxLength255

minLength1

JsonValue; type "mcp_toolset"constant"mcp_toolset"constant

Accepts one of the following:

MCP_TOOLSET("mcp_toolset")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Configs\> configs

Configuration overrides for specific tools, keyed by tool name

Optional\<Boolean\> deferLoading

Optional\<Boolean\> enabled

Optional\<[BetaMcpToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config)\> defaultConfig

Default configuration applied to all tools from this server

Optional\<Boolean\> deferLoading

Optional\<Boolean\> enabled

class BetaMemoryTool20250818:

JsonValue; name "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

MEMORY("memory")

JsonValue; type "memory_20250818"constant"memory_20250818"constant

Accepts one of the following:

MEMORY_20250818("memory_20250818")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818Command: A class that can be one of several variants.union

class BetaMemoryTool20250818ViewCommand:

JsonValue; command "view"constant"view"constant

Command type identifier

Accepts one of the following:

VIEW("view")

String path

Path to directory or file to view

Optional\<List\<Long\>\> viewRange

Optional line range for viewing specific lines

class BetaMemoryTool20250818CreateCommand:

JsonValue; command "create"constant"create"constant

Command type identifier

Accepts one of the following:

CREATE("create")

String fileText

Content to write to the file

String path

Path where the file should be created

class BetaMemoryTool20250818StrReplaceCommand:

JsonValue; command "str_replace"constant"str_replace"constant

Command type identifier

Accepts one of the following:

STR_REPLACE("str_replace")

String newStr

Text to replace with

String oldStr

Text to search for and replace

String path

Path to the file where text should be replaced

class BetaMemoryTool20250818InsertCommand:

JsonValue; command "insert"constant"insert"constant

Command type identifier

Accepts one of the following:

INSERT("insert")

long insertLine

Line number where text should be inserted

minimum1

String insertText

Text to insert at the specified line

String path

Path to the file where text should be inserted

class BetaMemoryTool20250818DeleteCommand:

JsonValue; command "delete"constant"delete"constant

Command type identifier

Accepts one of the following:

DELETE("delete")

String path

Path to the file or directory to delete

class BetaMemoryTool20250818RenameCommand:

JsonValue; command "rename"constant"rename"constant

Command type identifier

Accepts one of the following:

RENAME("rename")

String newPath

New path for the file or directory

String oldPath

Current path of the file or directory

class BetaMemoryTool20250818CreateCommand:

JsonValue; command "create"constant"create"constant

Command type identifier

Accepts one of the following:

CREATE("create")

String fileText

Content to write to the file

String path

Path where the file should be created

class BetaMemoryTool20250818DeleteCommand:

JsonValue; command "delete"constant"delete"constant

Command type identifier

Accepts one of the following:

DELETE("delete")

String path

Path to the file or directory to delete

class BetaMemoryTool20250818InsertCommand:

JsonValue; command "insert"constant"insert"constant

Command type identifier

Accepts one of the following:

INSERT("insert")

long insertLine

Line number where text should be inserted

minimum1

String insertText

Text to insert at the specified line

String path

Path to the file where text should be inserted

class BetaMemoryTool20250818RenameCommand:

JsonValue; command "rename"constant"rename"constant

Command type identifier

Accepts one of the following:

RENAME("rename")

String newPath

New path for the file or directory

String oldPath

Current path of the file or directory

class BetaMemoryTool20250818StrReplaceCommand:

JsonValue; command "str_replace"constant"str_replace"constant

Command type identifier

Accepts one of the following:

STR_REPLACE("str_replace")

String newStr

Text to replace with

String oldStr

Text to search for and replace

String path

Path to the file where text should be replaced

class BetaMemoryTool20250818ViewCommand:

JsonValue; command "view"constant"view"constant

Command type identifier

Accepts one of the following:

VIEW("view")

String path

Path to directory or file to view

Optional\<List\<Long\>\> viewRange

Optional line range for viewing specific lines

class BetaMessage:

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

class BetaMessageDeltaUsage:

Optional\<Long\> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

minimum0

Optional\<Long\> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

minimum0

Optional\<Long\> inputTokens

The cumulative number of input tokens which were used.

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

The cumulative number of output tokens which were used.

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

minimum0

long webSearchRequests

The number of web search tool requests.

minimum0

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

class BetaMessageParam:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaRequestDocumentBlock:

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String source

String title

JsonValue; type "search_result"constant"search_result"constant

Accepts one of the following:

SEARCH_RESULT("search_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant"tool_result"constant

Accepts one of the following:

TOOL_RESULT("tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Content\> content

Accepts one of the following:

String

List\<Block\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String source

String title

JsonValue; type "search_result"constant"search_result"constant

Accepts one of the following:

SEARCH_RESULT("search_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaRequestDocumentBlock:

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> isError

class BetaServerToolUseBlockParam:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaWebSearchToolResultBlockParam:

[BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class BetaWebSearchToolRequestError:

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

String toolUseId

JsonValue; type "web_search_tool_result"constant"web_search_tool_result"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT("web_search_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaWebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

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

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) content

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant"web_fetch_result"constant

Accepts one of the following:

WEB_FETCH_RESULT("web_fetch_result")

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web_fetch_tool_result"constant"web_fetch_tool_result"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaCodeExecutionToolResultBlockParam:

[BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content) content

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCodeExecutionResultBlockParam:

List\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> content

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaBashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

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

class BetaBashCodeExecutionResultBlockParam:

List\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> content

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaTextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

JsonValue; type "text_editor_code_execution_tool_result_error"constant"text_editor_code_execution_tool_result_error"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")

Optional\<String\> errorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant"text_editor_code_execution_view_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant"text_editor_code_execution_create_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant"text_editor_code_execution_str_replace_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant"text_editor_code_execution_tool_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "tool_search_tool_result_error"constant"tool_search_tool_result_error"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")

class BetaToolSearchToolSearchResultBlockParam:

List\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "tool_search_tool_search_result"constant"tool_search_tool_search_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")

String toolUseId

JsonValue; type "tool_search_tool_result"constant"tool_search_tool_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant"mcp_tool_use"constant

Accepts one of the following:

MCP_TOOL_USE("mcp_tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp_tool_result"constant"mcp_tool_result"constant

Accepts one of the following:

MCP_TOOL_RESULT("mcp_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Content\> content

Accepts one of the following:

String

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

Optional\<Boolean\> isError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container_upload"constant"container_upload"constant

Accepts one of the following:

CONTAINER_UPLOAD("container_upload")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

Optional\<String\> content

Summary of previously compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Accepts one of the following:

COMPACTION("compaction")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Role role

Accepts one of the following:

USER("user")

ASSISTANT("assistant")

class BetaMessageTokensCount:

Optional\<[BetaCountTokensContextManagementResponse](/docs/en/api/beta#beta_count_tokens_context_management_response)\> contextManagement

Information about context management applied to the message.

long originalInputTokens

The original token count before context management was applied

long inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

class BetaMetadata:

Optional\<String\> userId

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

class BetaOutputConfig:

Optional\<Effort\> effort

All possible effort levels.

Accepts one of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

MAX("max")

Optional\<[BetaJsonOutputFormat](/docs/en/api/beta#beta_json_output_format)\> format

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

Schema schema

The JSON schema of the format

JsonValue; type "json_schema"constant"json_schema"constant

Accepts one of the following:

JSON_SCHEMA("json_schema")

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaRawContentBlockDelta: A class that can be one of several variants.union

class BetaTextDelta:

String text

JsonValue; type "text_delta"constant"text_delta"constant

Accepts one of the following:

TEXT_DELTA("text_delta")

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant"input_json_delta"constant

Accepts one of the following:

INPUT_JSON_DELTA("input_json_delta")

class BetaCitationsDelta:

Citation citation

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

JsonValue; type "citations_delta"constant"citations_delta"constant

Accepts one of the following:

CITATIONS_DELTA("citations_delta")

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant"thinking_delta"constant

Accepts one of the following:

THINKING_DELTA("thinking_delta")

class BetaSignatureDelta:

String signature

JsonValue; type "signature_delta"constant"signature_delta"constant

Accepts one of the following:

SIGNATURE_DELTA("signature_delta")

class BetaCompactionContentBlockDelta:

Optional\<String\> content

JsonValue; type "compaction_delta"constant"compaction_delta"constant

Accepts one of the following:

COMPACTION_DELTA("compaction_delta")

class BetaRawContentBlockDeltaEvent:

[BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta) delta

Accepts one of the following:

class BetaTextDelta:

String text

JsonValue; type "text_delta"constant"text_delta"constant

Accepts one of the following:

TEXT_DELTA("text_delta")

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant"input_json_delta"constant

Accepts one of the following:

INPUT_JSON_DELTA("input_json_delta")

class BetaCitationsDelta:

Citation citation

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

JsonValue; type "citations_delta"constant"citations_delta"constant

Accepts one of the following:

CITATIONS_DELTA("citations_delta")

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant"thinking_delta"constant

Accepts one of the following:

THINKING_DELTA("thinking_delta")

class BetaSignatureDelta:

String signature

JsonValue; type "signature_delta"constant"signature_delta"constant

Accepts one of the following:

SIGNATURE_DELTA("signature_delta")

class BetaCompactionContentBlockDelta:

Optional\<String\> content

JsonValue; type "compaction_delta"constant"compaction_delta"constant

Accepts one of the following:

COMPACTION_DELTA("compaction_delta")

long index

JsonValue; type "content_block_delta"constant"content_block_delta"constant

Accepts one of the following:

CONTENT_BLOCK_DELTA("content_block_delta")

class BetaRawContentBlockStartEvent:

ContentBlock contentBlock

Response model for a file uploaded to the container.

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

long index

JsonValue; type "content_block_start"constant"content_block_start"constant

Accepts one of the following:

CONTENT_BLOCK_START("content_block_start")

class BetaRawContentBlockStopEvent:

long index

JsonValue; type "content_block_stop"constant"content_block_stop"constant

Accepts one of the following:

CONTENT_BLOCK_STOP("content_block_stop")

class BetaRawMessageDeltaEvent:

Optional\<[BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)\> contextManagement

Information about context management strategies applied during the request

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

Delta delta

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

Optional\<[BetaStopReason](/docs/en/api/beta#beta_stop_reason)\> stopReason

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

JsonValue; type "message_delta"constant"message_delta"constant

Accepts one of the following:

MESSAGE_DELTA("message_delta")

[BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<Long\> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

minimum0

Optional\<Long\> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

minimum0

Optional\<Long\> inputTokens

The cumulative number of input tokens which were used.

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

The cumulative number of output tokens which were used.

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

minimum0

long webSearchRequests

The number of web search tool requests.

minimum0

class BetaRawMessageStartEvent:

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

JsonValue; type "message_start"constant"message_start"constant

Accepts one of the following:

MESSAGE_START("message_start")

class BetaRawMessageStopEvent:

JsonValue; type "message_stop"constant"message_stop"constant

Accepts one of the following:

MESSAGE_STOP("message_stop")

class BetaRawMessageStreamEvent: A class that can be one of several variants.union

class BetaRawMessageStartEvent:

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

JsonValue; type "message_start"constant"message_start"constant

Accepts one of the following:

MESSAGE_START("message_start")

class BetaRawMessageDeltaEvent:

Optional\<[BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)\> contextManagement

Information about context management strategies applied during the request

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

Delta delta

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

Optional\<[BetaStopReason](/docs/en/api/beta#beta_stop_reason)\> stopReason

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

JsonValue; type "message_delta"constant"message_delta"constant

Accepts one of the following:

MESSAGE_DELTA("message_delta")

[BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<Long\> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

minimum0

Optional\<Long\> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

minimum0

Optional\<Long\> inputTokens

The cumulative number of input tokens which were used.

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

The cumulative number of output tokens which were used.

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

minimum0

long webSearchRequests

The number of web search tool requests.

minimum0

class BetaRawMessageStopEvent:

JsonValue; type "message_stop"constant"message_stop"constant

Accepts one of the following:

MESSAGE_STOP("message_stop")

class BetaRawContentBlockStartEvent:

ContentBlock contentBlock

Response model for a file uploaded to the container.

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

long index

JsonValue; type "content_block_start"constant"content_block_start"constant

Accepts one of the following:

CONTENT_BLOCK_START("content_block_start")

class BetaRawContentBlockDeltaEvent:

[BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta) delta

Accepts one of the following:

class BetaTextDelta:

String text

JsonValue; type "text_delta"constant"text_delta"constant

Accepts one of the following:

TEXT_DELTA("text_delta")

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant"input_json_delta"constant

Accepts one of the following:

INPUT_JSON_DELTA("input_json_delta")

class BetaCitationsDelta:

Citation citation

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

JsonValue; type "citations_delta"constant"citations_delta"constant

Accepts one of the following:

CITATIONS_DELTA("citations_delta")

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant"thinking_delta"constant

Accepts one of the following:

THINKING_DELTA("thinking_delta")

class BetaSignatureDelta:

String signature

JsonValue; type "signature_delta"constant"signature_delta"constant

Accepts one of the following:

SIGNATURE_DELTA("signature_delta")

class BetaCompactionContentBlockDelta:

Optional\<String\> content

JsonValue; type "compaction_delta"constant"compaction_delta"constant

Accepts one of the following:

COMPACTION_DELTA("compaction_delta")

long index

JsonValue; type "content_block_delta"constant"content_block_delta"constant

Accepts one of the following:

CONTENT_BLOCK_DELTA("content_block_delta")

class BetaRawContentBlockStopEvent:

long index

JsonValue; type "content_block_stop"constant"content_block_stop"constant

Accepts one of the following:

CONTENT_BLOCK_STOP("content_block_stop")

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class BetaRequestDocumentBlock:

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaRequestMcpServerToolConfiguration:

Optional\<List\<String\>\> allowedTools

Optional\<Boolean\> enabled

class BetaRequestMcpServerUrlDefinition:

String name

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

Optional\<String\> authorizationToken

Optional\<[BetaRequestMcpServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration)\> toolConfiguration

Optional\<List\<String\>\> allowedTools

Optional\<Boolean\> enabled

class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp_tool_result"constant"mcp_tool_result"constant

Accepts one of the following:

MCP_TOOL_RESULT("mcp_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Content\> content

Accepts one of the following:

String

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

Optional\<Boolean\> isError

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String source

String title

JsonValue; type "search_result"constant"search_result"constant

Accepts one of the following:

SEARCH_RESULT("search_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaServerToolUsage:

long webFetchRequests

The number of web fetch tool requests.

minimum0

long webSearchRequests

The number of web search tool requests.

minimum0

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

class BetaServerToolUseBlockParam:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaSignatureDelta:

String signature

JsonValue; type "signature_delta"constant"signature_delta"constant

Accepts one of the following:

SIGNATURE_DELTA("signature_delta")

class BetaSkill:

A skill that was loaded in a container (response model).

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

class BetaSkillParams:

Specification for a skill to be loaded in a container (request model).

String skillId

Skill ID

maxLength64

minLength1

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional\<String\> version

Skill version or 'latest' for most recent version

maxLength64

minLength1

enum BetaStopReason:

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")

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

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaTextCitation: A class that can be one of several variants.union

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

class BetaTextCitationParam: A class that can be one of several variants.union

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaTextDelta:

String text

JsonValue; type "text_delta"constant"text_delta"constant

Accepts one of the following:

TEXT_DELTA("text_delta")

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant"text_editor_code_execution_create_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")

class BetaTextEditorCodeExecutionCreateResultBlockParam:

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

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant"text_editor_code_execution_str_replace_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

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

class BetaTextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

JsonValue; type "text_editor_code_execution_tool_result_error"constant"text_editor_code_execution_tool_result_error"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")

Optional\<String\> errorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant"text_editor_code_execution_view_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant"text_editor_code_execution_create_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant"text_editor_code_execution_str_replace_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant"text_editor_code_execution_tool_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaTextEditorCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

JsonValue; type "text_editor_code_execution_tool_result_error"constant"text_editor_code_execution_tool_result_error"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")

Optional\<String\> errorMessage

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

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant"text_editor_code_execution_view_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant

Accepts one of the following:

ADAPTIVE("adaptive")

class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class BetaThinkingConfigEnabled:

long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

class BetaThinkingConfigParam: A class that can be one of several variants.union

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

class BetaThinkingConfigEnabled:

long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant

Accepts one of the following:

ADAPTIVE("adaptive")

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant"thinking_delta"constant

Accepts one of the following:

THINKING_DELTA("thinking_delta")

class BetaThinkingTurns:

JsonValue; type "thinking_turns"constant"thinking_turns"constant

Accepts one of the following:

THINKING_TURNS("thinking_turns")

long value

class BetaTool:

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant"object"constant

Accepts one of the following:

OBJECT("object")

Optional\<Properties\> properties

Optional\<List\<String\>\> required

String name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<String\> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional\<Boolean\> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<Type\> type

Accepts one of the following:

CUSTOM("custom")

class BetaToolBash20241022:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20241022"constant"bash_20241022"constant

Accepts one of the following:

BASH_20241022("bash_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20250124"constant"bash_20250124"constant

Accepts one of the following:

BASH_20250124("bash_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant

Accepts one of the following:

ANY("any")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant

Accepts one of the following:

NONE("none")

class BetaToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant

Accepts one of the following:

ANY("any")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant

Accepts one of the following:

NONE("none")

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20241022"constant"computer_20241022"constant

Accepts one of the following:

COMPUTER_20241022("computer_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20250124"constant"computer_20250124"constant

Accepts one of the following:

COMPUTER_20250124("computer_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20251124"constant"computer_20251124"constant

Accepts one of the following:

COMPUTER_20251124("computer_20251124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<Boolean\> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolReferenceBlock:

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant"tool_result"constant

Accepts one of the following:

TOOL_RESULT("tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Content\> content

Accepts one of the following:

String

List\<Block\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

String source

String title

JsonValue; type "search_result"constant"search_result"constant

Accepts one of the following:

SEARCH_RESULT("search_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaRequestDocumentBlock:

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> isError

class BetaToolSearchToolBm25_20251119:

JsonValue; name "tool_search_tool_bm25"constant"tool_search_tool_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonValue; name "tool_search_tool_regex"constant"tool_search_tool_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

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

class BetaToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "tool_search_tool_result_error"constant"tool_search_tool_result_error"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")

class BetaToolSearchToolSearchResultBlockParam:

List\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "tool_search_tool_search_result"constant"tool_search_tool_search_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")

String toolUseId

JsonValue; type "tool_search_tool_result"constant"tool_search_tool_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaToolSearchToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

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

class BetaToolSearchToolSearchResultBlockParam:

List\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "tool_search_tool_search_result"constant"tool_search_tool_search_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")

class BetaToolTextEditor20241022:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20241022"constant"text_editor_20241022"constant

Accepts one of the following:

TEXT_EDITOR_20241022("text_editor_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20250124"constant"text_editor_20250124"constant

Accepts one of the following:

TEXT_EDITOR_20250124("text_editor_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250429"constant"text_editor_20250429"constant

Accepts one of the following:

TEXT_EDITOR_20250429("text_editor_20250429")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250728"constant"text_editor_20250728"constant

Accepts one of the following:

TEXT_EDITOR_20250728("text_editor_20250728")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Long\> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolUnion: A class that can be one of several variants.union

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

class BetaTool:

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant"object"constant

Accepts one of the following:

OBJECT("object")

Optional\<Properties\> properties

Optional\<List\<String\>\> required

String name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<String\> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional\<Boolean\> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<Type\> type

Accepts one of the following:

CUSTOM("custom")

class BetaToolBash20241022:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20241022"constant"bash_20241022"constant

Accepts one of the following:

BASH_20241022("bash_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20250124"constant"bash_20250124"constant

Accepts one of the following:

BASH_20250124("bash_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522:

JsonValue; name "code_execution"constant"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE_EXECUTION("code_execution")

JsonValue; type "code_execution_20250522"constant"code_execution_20250522"constant

Accepts one of the following:

CODE_EXECUTION_20250522("code_execution_20250522")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonValue; name "code_execution"constant"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE_EXECUTION("code_execution")

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20241022"constant"computer_20241022"constant

Accepts one of the following:

COMPUTER_20241022("computer_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818:

JsonValue; name "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

MEMORY("memory")

JsonValue; type "memory_20250818"constant"memory_20250818"constant

Accepts one of the following:

MEMORY_20250818("memory_20250818")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20250124"constant"computer_20250124"constant

Accepts one of the following:

COMPUTER_20250124("computer_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20241022"constant"text_editor_20241022"constant

Accepts one of the following:

TEXT_EDITOR_20241022("text_editor_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20251124"constant"computer_20251124"constant

Accepts one of the following:

COMPUTER_20251124("computer_20251124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<Boolean\> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20250124"constant"text_editor_20250124"constant

Accepts one of the following:

TEXT_EDITOR_20250124("text_editor_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250429"constant"text_editor_20250429"constant

Accepts one of the following:

TEXT_EDITOR_20250429("text_editor_20250429")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250728"constant"text_editor_20250728"constant

Accepts one of the following:

TEXT_EDITOR_20250728("text_editor_20250728")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Long\> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305:

JsonValue; name "web_search"constant"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "web_search_20250305"constant"web_search_20250305"constant

Accepts one of the following:

WEB_SEARCH_20250305("web_search_20250305")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<UserLocation\> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Accepts one of the following:

APPROXIMATE("approximate")

Optional\<String\> city

The city of the user.

maxLength255

minLength1

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

Optional\<String\> region

The region of the user.

maxLength255

minLength1

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebFetchTool20250910:

JsonValue; name "web_fetch"constant"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_FETCH("web_fetch")

JsonValue; type "web_fetch_20250910"constant"web_fetch_20250910"constant

Accepts one of the following:

WEB_FETCH_20250910("web_fetch_20250910")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolBm25_20251119:

JsonValue; name "tool_search_tool_bm25"constant"tool_search_tool_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonValue; name "tool_search_tool_regex"constant"tool_search_tool_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

String mcpServerName

Name of the MCP server to configure tools for

maxLength255

minLength1

JsonValue; type "mcp_toolset"constant"mcp_toolset"constant

Accepts one of the following:

MCP_TOOLSET("mcp_toolset")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Configs\> configs

Configuration overrides for specific tools, keyed by tool name

Optional\<Boolean\> deferLoading

Optional\<Boolean\> enabled

Optional\<[BetaMcpToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config)\> defaultConfig

Default configuration applied to all tools from this server

Optional\<Boolean\> deferLoading

Optional\<Boolean\> enabled

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

class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaToolUsesKeep:

JsonValue; type "tool_uses"constant"tool_uses"constant

Accepts one of the following:

TOOL_USES("tool_uses")

long value

class BetaToolUsesTrigger:

JsonValue; type "tool_uses"constant"tool_uses"constant

Accepts one of the following:

TOOL_USES("tool_uses")

long value

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaUsage:

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

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) content

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant"web_fetch_result"constant

Accepts one of the following:

WEB_FETCH_RESULT("web_fetch_result")

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

class BetaWebFetchTool20250910:

JsonValue; name "web_fetch"constant"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_FETCH("web_fetch")

JsonValue; type "web_fetch_20250910"constant"web_fetch_20250910"constant

Accepts one of the following:

WEB_FETCH_20250910("web_fetch_20250910")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

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

class BetaWebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

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

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) content

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

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant"web_fetch_result"constant

Accepts one of the following:

WEB_FETCH_RESULT("web_fetch_result")

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web_fetch_tool_result"constant"web_fetch_tool_result"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

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

class BetaWebFetchToolResultErrorBlockParam:

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

enum BetaWebFetchToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

class BetaWebSearchResultBlock:

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

class BetaWebSearchResultBlockParam:

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class BetaWebSearchTool20250305:

JsonValue; name "web_search"constant"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "web_search_20250305"constant"web_search_20250305"constant

Accepts one of the following:

WEB_SEARCH_20250305("web_search_20250305")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<UserLocation\> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Accepts one of the following:

APPROXIMATE("approximate")

Optional\<String\> city

The city of the user.

maxLength255

minLength1

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

Optional\<String\> region

The region of the user.

maxLength255

minLength1

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebSearchToolRequestError:

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

class BetaWebSearchToolResultBlockContent: A class that can be one of several variants.union

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

class BetaWebSearchToolResultBlockParam:

[BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class BetaWebSearchToolRequestError:

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

String toolUseId

JsonValue; type "web_search_tool_result"constant"web_search_tool_result"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT("web_search_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BetaWebSearchToolResultBlockParamContent: A class that can be one of several variants.union

List\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class BetaWebSearchToolRequestError:

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

enum BetaWebSearchToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

#### MessagesBatches

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
