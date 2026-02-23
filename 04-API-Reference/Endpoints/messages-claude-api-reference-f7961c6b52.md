---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:44:42Z"
source_url: "https://platform.claude.com/docs/en/api/java/messages"
title: "Messages - Claude API Reference"
---

Copy page

Java

# Messages

##### [Create a Message](/docs/en/api/messages/create)

[Message](/docs/en/api/messages#message) messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages

##### [Count tokens in a Message](/docs/en/api/messages/count_tokens)

[MessageTokensCount](/docs/en/api/messages#message_tokens_count) messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/count_tokens

##### ModelsExpand Collapse 

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class BashCodeExecutionOutputBlock:

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

class BashCodeExecutionOutputBlockParam:

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

class BashCodeExecutionResultBlockParam:

List\<[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class BashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlockParam:

List\<[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

enum BashCodeExecutionToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

class BashCodeExecutionToolResultErrorParam:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class CacheControlEphemeral:

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class CacheCreation:

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsConfig:

boolean enabled

class CitationsConfigParam:

Optional\<Boolean\> enabled

class CitationsDelta:

Citation citation

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

JsonValue; type "citations_delta"constant

"citations_delta"constant

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CodeExecutionOutputBlock:

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

class CodeExecutionOutputBlockParam:

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class CodeExecutionResultBlockParam:

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class CodeExecutionTool20250522:

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20250522"constant

"code_execution_20250522"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionTool20250825:

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class CodeExecutionToolResultBlockContent: A class that can be one of several variants.union

Code execution result with encrypted stdout for PFC + web_search results.

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

class CodeExecutionToolResultBlockParam:

[CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlockParam:

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class CodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union

Code execution result with encrypted stdout for PFC + web_search results.

class CodeExecutionToolResultErrorParam:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlockParam:

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

enum CodeExecutionToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

class CodeExecutionToolResultErrorParam:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class Container:

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

class ContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class ContentBlock: A class that can be one of several variants.union

Response model for a file uploaded to the container.

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

class ContentBlockParam: A class that can be one of several variants.union

Regular text content.

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String source

String title

JsonValue; type "search_result"constant

"search_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class ThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class ToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant

"tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String source

String title

JsonValue; type "search_result"constant

"search_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class ToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ServerToolUseBlockParam:

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class WebSearchToolResultBlockParam:

[WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

Optional\<String\> pageAge

class WebSearchToolRequestError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class WebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlockParam:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlockParam:

[DocumentBlockParam](/docs/en/api/messages#document_block_param) content

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class CodeExecutionToolResultBlockParam:

[CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlockParam:

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlockParam:

List\<[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class TextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

Optional\<String\> errorMessage

class TextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class TextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class ToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class ToolSearchToolResultErrorParam:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlockParam:

List\<[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class ContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class ContentBlockSourceContent: A class that can be one of several variants.union

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class DocumentBlock:

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class InputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant

"input_json_delta"constant

class JsonOutputFormat:

Schema schema

The JSON schema of the format

JsonValue; type "json_schema"constant

"json_schema"constant

class MemoryTool20250818:

JsonValue; name "memory"constant

"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "memory_20250818"constant

"memory_20250818"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class Message:

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[Container](/docs/en/api/messages#container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

List\<[ContentBlock](/docs/en/api/messages#content_block)\> content

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

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_SONNET_4_6("claude-sonnet-4-6")

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

JsonValue; role "assistant"constant

"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

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

REFUSAL("refusal")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant

"message"constant

Object type.

For Messages, this is always `"message"`.

[Usage](/docs/en/api/messages#usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[CacheCreation](/docs/en/api/messages#cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

class MessageCountTokensTool: A class that can be one of several variants.union

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

class Tool:

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant

"object"constant

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

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolBash20250124:

JsonValue; name "bash"constant

"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash_20250124"constant

"bash_20250124"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionTool20250522:

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20250522"constant

"code_execution_20250522"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionTool20250825:

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class MemoryTool20250818:

JsonValue; name "memory"constant

"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "memory_20250818"constant

"memory_20250818"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant

"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250124"constant

"text_editor_20250124"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant

"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250429"constant

"text_editor_20250429"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant

"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250728"constant

"text_editor_20250728"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305:

JsonValue; name "web_search"constant

"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_search_20250305"constant

"web_search_20250305"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<[UserLocation](/docs/en/api/messages#user_location)\> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant

"approximate"constant

Optional\<String\> city

The city of the user.

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional\<String\> region

The region of the user.

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20250910:

JsonValue; name "web_fetch"constant

"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_fetch_20250910"constant

"web_fetch_20250910"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20260209:

JsonValue; name "web_search"constant

"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_search_20260209"constant

"web_search_20260209"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<[UserLocation](/docs/en/api/messages#user_location)\> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant

"approximate"constant

Optional\<String\> city

The city of the user.

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional\<String\> region

The region of the user.

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20260209:

JsonValue; name "web_fetch"constant

"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_fetch_20260209"constant

"web_fetch_20260209"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolBm25_20251119:

JsonValue; name "tool_search_tool_bm25"constant

"tool_search_tool_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolSearchToolRegex20251119:

JsonValue; name "tool_search_tool_regex"constant

"tool_search_tool_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class MessageDeltaUsage:

Optional\<Long\> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional\<Long\> inputTokens

The cumulative number of input tokens which were used.

long outputTokens

The cumulative number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class MessageParam:

Content content

Accepts one of the following:

String

List\<[ContentBlockParam](/docs/en/api/messages#content_block_param)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String source

String title

JsonValue; type "search_result"constant

"search_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class ThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class ToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant

"tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String source

String title

JsonValue; type "search_result"constant

"search_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class ToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ServerToolUseBlockParam:

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class WebSearchToolResultBlockParam:

[WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

Optional\<String\> pageAge

class WebSearchToolRequestError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class WebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlockParam:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlockParam:

[DocumentBlockParam](/docs/en/api/messages#document_block_param) content

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class CodeExecutionToolResultBlockParam:

[CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlockParam:

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class BashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlockParam:

List\<[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class TextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

Optional\<String\> errorMessage

class TextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class TextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class ToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class ToolSearchToolResultErrorParam:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlockParam:

List\<[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class ContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class MessageTokensCount:

long inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

class Metadata:

Optional\<String\> userId

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

class OutputConfig:

Optional\<Effort\> effort

All possible effort levels.

Accepts one of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

MAX("max")

Optional\<[JsonOutputFormat](/docs/en/api/messages#json_output_format)\> format

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

Schema schema

The JSON schema of the format

JsonValue; type "json_schema"constant

"json_schema"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class RawContentBlockDelta: A class that can be one of several variants.union

class TextDelta:

String text

JsonValue; type "text_delta"constant

"text_delta"constant

class InputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant

"input_json_delta"constant

class CitationsDelta:

Citation citation

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

JsonValue; type "citations_delta"constant

"citations_delta"constant

class ThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant

"thinking_delta"constant

class SignatureDelta:

String signature

JsonValue; type "signature_delta"constant

"signature_delta"constant

class RawContentBlockDeltaEvent:

[RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta) delta

Accepts one of the following:

class TextDelta:

String text

JsonValue; type "text_delta"constant

"text_delta"constant

class InputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant

"input_json_delta"constant

class CitationsDelta:

Citation citation

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

JsonValue; type "citations_delta"constant

"citations_delta"constant

class ThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant

"thinking_delta"constant

class SignatureDelta:

String signature

JsonValue; type "signature_delta"constant

"signature_delta"constant

long index

JsonValue; type "content_block_delta"constant

"content_block_delta"constant

class RawContentBlockStartEvent:

ContentBlock contentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

long index

JsonValue; type "content_block_start"constant

"content_block_start"constant

class RawContentBlockStopEvent:

long index

JsonValue; type "content_block_stop"constant

"content_block_stop"constant

class RawMessageDeltaEvent:

Delta delta

Optional\<[Container](/docs/en/api/messages#container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

Accepts one of the following:

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

REFUSAL("refusal")

Optional\<String\> stopSequence

JsonValue; type "message_delta"constant

"message_delta"constant

[MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<Long\> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional\<Long\> inputTokens

The cumulative number of input tokens which were used.

long outputTokens

The cumulative number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class RawMessageStartEvent:

[Message](/docs/en/api/messages#message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[Container](/docs/en/api/messages#container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

List\<[ContentBlock](/docs/en/api/messages#content_block)\> content

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

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_SONNET_4_6("claude-sonnet-4-6")

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

JsonValue; role "assistant"constant

"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

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

REFUSAL("refusal")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant

"message"constant

Object type.

For Messages, this is always `"message"`.

[Usage](/docs/en/api/messages#usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[CacheCreation](/docs/en/api/messages#cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

JsonValue; type "message_start"constant

"message_start"constant

class RawMessageStopEvent:

JsonValue; type "message_stop"constant

"message_stop"constant

class RawMessageStreamEvent: A class that can be one of several variants.union

class RawMessageStartEvent:

[Message](/docs/en/api/messages#message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[Container](/docs/en/api/messages#container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

List\<[ContentBlock](/docs/en/api/messages#content_block)\> content

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

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_SONNET_4_6("claude-sonnet-4-6")

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

JsonValue; role "assistant"constant

"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

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

REFUSAL("refusal")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant

"message"constant

Object type.

For Messages, this is always `"message"`.

[Usage](/docs/en/api/messages#usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[CacheCreation](/docs/en/api/messages#cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

JsonValue; type "message_start"constant

"message_start"constant

class RawMessageDeltaEvent:

Delta delta

Optional\<[Container](/docs/en/api/messages#container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

Accepts one of the following:

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

REFUSAL("refusal")

Optional\<String\> stopSequence

JsonValue; type "message_delta"constant

"message_delta"constant

[MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<Long\> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional\<Long\> inputTokens

The cumulative number of input tokens which were used.

long outputTokens

The cumulative number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class RawMessageStopEvent:

JsonValue; type "message_stop"constant

"message_stop"constant

class RawContentBlockStartEvent:

ContentBlock contentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

long index

JsonValue; type "content_block_start"constant

"content_block_start"constant

class RawContentBlockDeltaEvent:

[RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta) delta

Accepts one of the following:

class TextDelta:

String text

JsonValue; type "text_delta"constant

"text_delta"constant

class InputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant

"input_json_delta"constant

class CitationsDelta:

Citation citation

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

JsonValue; type "citations_delta"constant

"citations_delta"constant

class ThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant

"thinking_delta"constant

class SignatureDelta:

String signature

JsonValue; type "signature_delta"constant

"signature_delta"constant

long index

JsonValue; type "content_block_delta"constant

"content_block_delta"constant

class RawContentBlockStopEvent:

long index

JsonValue; type "content_block_stop"constant

"content_block_stop"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class RedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String source

String title

JsonValue; type "search_result"constant

"search_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class ServerToolUsage:

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class ServerToolUseBlockParam:

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class SignatureDelta:

String signature

JsonValue; type "signature_delta"constant

"signature_delta"constant

enum StopReason:

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

REFUSAL("refusal")

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class TextCitation: A class that can be one of several variants.union

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class TextCitationParam: A class that can be one of several variants.union

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class TextDelta:

String text

JsonValue; type "text_delta"constant

"text_delta"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

Optional\<String\> errorMessage

class TextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class TextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

enum TextEditorCodeExecutionToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

class TextEditorCodeExecutionToolResultErrorParam:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

Optional\<String\> errorMessage

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class ThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class ThinkingConfigAdaptive:

JsonValue; type "adaptive"constant

"adaptive"constant

class ThinkingConfigDisabled:

JsonValue; type "disabled"constant

"disabled"constant

class ThinkingConfigEnabled:

long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonValue; type "enabled"constant

"enabled"constant

class ThinkingConfigParam: A class that can be one of several variants.union

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

class ThinkingConfigEnabled:

long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonValue; type "enabled"constant

"enabled"constant

class ThinkingConfigDisabled:

JsonValue; type "disabled"constant

"disabled"constant

class ThinkingConfigAdaptive:

JsonValue; type "adaptive"constant

"adaptive"constant

class ThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant

"thinking_delta"constant

class Tool:

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant

"object"constant

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

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolBash20250124:

JsonValue; name "bash"constant

"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash_20250124"constant

"bash_20250124"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant

"auto"constant

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant

"any"constant

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant

"tool"constant

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant

"none"constant

class ToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant

"any"constant

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant

"auto"constant

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant

"none"constant

class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant

"tool"constant

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolReferenceBlock:

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

class ToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class ToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant

"tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String source

String title

JsonValue; type "search_result"constant

"search_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class ToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolSearchToolBm25_20251119:

JsonValue; name "tool_search_tool_bm25"constant

"tool_search_tool_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolSearchToolRegex20251119:

JsonValue; name "tool_search_tool_regex"constant

"tool_search_tool_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class ToolSearchToolResultErrorParam:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlockParam:

List\<[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

enum ToolSearchToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

class ToolSearchToolResultErrorParam:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

class ToolSearchToolSearchResultBlockParam:

List\<[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

class ToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant

"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250124"constant

"text_editor_20250124"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant

"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250429"constant

"text_editor_20250429"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant

"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250728"constant

"text_editor_20250728"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolUnion: A class that can be one of several variants.union

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

class Tool:

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant

"object"constant

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

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolBash20250124:

JsonValue; name "bash"constant

"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash_20250124"constant

"bash_20250124"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionTool20250522:

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20250522"constant

"code_execution_20250522"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionTool20250825:

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class CodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonValue; name "code_execution"constant

"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class MemoryTool20250818:

JsonValue; name "memory"constant

"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "memory_20250818"constant

"memory_20250818"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant

"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250124"constant

"text_editor_20250124"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant

"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250429"constant

"text_editor_20250429"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant

"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20250728"constant

"text_editor_20250728"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305:

JsonValue; name "web_search"constant

"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_search_20250305"constant

"web_search_20250305"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<[UserLocation](/docs/en/api/messages#user_location)\> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant

"approximate"constant

Optional\<String\> city

The city of the user.

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional\<String\> region

The region of the user.

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20250910:

JsonValue; name "web_fetch"constant

"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_fetch_20250910"constant

"web_fetch_20250910"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20260209:

JsonValue; name "web_search"constant

"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_search_20260209"constant

"web_search_20260209"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<[UserLocation](/docs/en/api/messages#user_location)\> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant

"approximate"constant

Optional\<String\> city

The city of the user.

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional\<String\> region

The region of the user.

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20260209:

JsonValue; name "web_fetch"constant

"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_fetch_20260209"constant

"web_fetch_20260209"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolBm25_20251119:

JsonValue; name "tool_search_tool_bm25"constant

"tool_search_tool_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolSearchToolRegex20251119:

JsonValue; name "tool_search_tool_regex"constant

"tool_search_tool_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

class Usage:

Optional\<[CacheCreation](/docs/en/api/messages#cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

class UserLocation:

JsonValue; type "approximate"constant

"approximate"constant

Optional\<String\> city

The city of the user.

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional\<String\> region

The region of the user.

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

class WebFetchBlockParam:

[DocumentBlockParam](/docs/en/api/messages#document_block_param) content

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

class WebFetchTool20250910:

JsonValue; name "web_fetch"constant

"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_fetch_20250910"constant

"web_fetch_20250910"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class WebFetchTool20260209:

JsonValue; name "web_fetch"constant

"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_fetch_20260209"constant

"web_fetch_20260209"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class WebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlockParam:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlockParam:

[DocumentBlockParam](/docs/en/api/messages#document_block_param) content

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

class ImageBlockParam:

Source source

Accepts one of the following:

class Base64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE_JPEG("image/jpeg")

IMAGE_PNG("image/png")

IMAGE_GIF("image/gif")

IMAGE_WEBP("image/webp")

JsonValue; type "base64"constant

"base64"constant

class UrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "image"constant

"image"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

JsonValue; type "content"constant

"content"constant

class UrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

JsonValue; type "document"constant

"document"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

Optional\<Ttl\> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL_5M("5m")

TTL_1H("1h")

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchToolResultErrorBlockParam:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

enum WebFetchToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

class WebSearchResultBlock:

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

class WebSearchResultBlockParam:

String encryptedContent

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

Optional\<String\> pageAge

class WebSearchTool20250305:

JsonValue; name "web_search"constant

"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_search_20250305"constant

"web_search_20250305"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<[UserLocation](/docs/en/api/messages#user_location)\> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant

"approximate"constant

Optional\<String\> city

The city of the user.

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional\<String\> region

The region of the user.

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebSearchTool20260209:

JsonValue; name "web_search"constant

"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web_search_20260209"constant

"web_search_20260209"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<[UserLocation](/docs/en/api/messages#user_location)\> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant

"approximate"constant

Optional\<String\> city

The city of the user.

Optional\<String\> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional\<String\> region

The region of the user.

Optional\<String\> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebSearchToolRequestError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebSearchToolResultBlockContent: A class that can be one of several variants.union

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

class WebSearchToolResultBlockParam:

[WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

Optional\<String\> pageAge

class WebSearchToolRequestError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant

"ephemeral"constant

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

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class WebSearchToolResultBlockParamContent: A class that can be one of several variants.union

List\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

Optional\<String\> pageAge

class WebSearchToolRequestError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

enum WebSearchToolResultErrorCode:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

[MessageBatch](/docs/en/api/messages#message_batch) messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

[MessageBatch](/docs/en/api/messages#message_batch) messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

BatchListPage messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

[MessageBatch](/docs/en/api/messages#message_batch) messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

[DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch) messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

[MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response) messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class DeletedMessageBatch:

String id

ID of the Message Batch.

JsonValue; type "message_batch_deleted"constant

"message_batch_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class MessageBatch:

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<LocalDateTime\> archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

Optional\<LocalDateTime\> cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

Optional\<LocalDateTime\> endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

LocalDateTime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus processingStatus

Processing status of the Message Batch.

Accepts one of the following:

IN_PROGRESS("in_progress")

CANCELING("canceling")

ENDED("ended")

[MessageBatchRequestCounts](/docs/en/api/messages#message_batch_request_counts) requestCounts

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

JsonValue; type "message_batch"constant

"message_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

class MessageBatchCanceledResult:

JsonValue; type "canceled"constant

"canceled"constant

class MessageBatchErroredResult:

[ErrorResponse](/docs/en/api/$shared#error_response) error

[ErrorObject](/docs/en/api/$shared#error_object) error

Accepts one of the following:

class InvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant

"invalid_request_error"constant

class AuthenticationError:

String message

JsonValue; type "authentication_error"constant

"authentication_error"constant

class BillingError:

String message

JsonValue; type "billing_error"constant

"billing_error"constant

class PermissionError:

String message

JsonValue; type "permission_error"constant

"permission_error"constant

class NotFoundError:

String message

JsonValue; type "not_found_error"constant

"not_found_error"constant

class RateLimitError:

String message

JsonValue; type "rate_limit_error"constant

"rate_limit_error"constant

class GatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant

"timeout_error"constant

class ApiErrorObject:

String message

JsonValue; type "api_error"constant

"api_error"constant

class OverloadedError:

String message

JsonValue; type "overloaded_error"constant

"overloaded_error"constant

Optional\<String\> requestId

JsonValue; type "error"constant

"error"constant

JsonValue; type "errored"constant

"errored"constant

class MessageBatchExpiredResult:

JsonValue; type "expired"constant

"expired"constant

class MessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

String customId

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[MessageBatchResult](/docs/en/api/messages#message_batch_result) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult:

[Message](/docs/en/api/messages#message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[Container](/docs/en/api/messages#container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

List\<[ContentBlock](/docs/en/api/messages#content_block)\> content

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

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_SONNET_4_6("claude-sonnet-4-6")

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

JsonValue; role "assistant"constant

"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

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

REFUSAL("refusal")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant

"message"constant

Object type.

For Messages, this is always `"message"`.

[Usage](/docs/en/api/messages#usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[CacheCreation](/docs/en/api/messages#cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

JsonValue; type "succeeded"constant

"succeeded"constant

class MessageBatchErroredResult:

[ErrorResponse](/docs/en/api/$shared#error_response) error

[ErrorObject](/docs/en/api/$shared#error_object) error

Accepts one of the following:

class InvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant

"invalid_request_error"constant

class AuthenticationError:

String message

JsonValue; type "authentication_error"constant

"authentication_error"constant

class BillingError:

String message

JsonValue; type "billing_error"constant

"billing_error"constant

class PermissionError:

String message

JsonValue; type "permission_error"constant

"permission_error"constant

class NotFoundError:

String message

JsonValue; type "not_found_error"constant

"not_found_error"constant

class RateLimitError:

String message

JsonValue; type "rate_limit_error"constant

"rate_limit_error"constant

class GatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant

"timeout_error"constant

class ApiErrorObject:

String message

JsonValue; type "api_error"constant

"api_error"constant

class OverloadedError:

String message

JsonValue; type "overloaded_error"constant

"overloaded_error"constant

Optional\<String\> requestId

JsonValue; type "error"constant

"error"constant

JsonValue; type "errored"constant

"errored"constant

class MessageBatchCanceledResult:

JsonValue; type "canceled"constant

"canceled"constant

class MessageBatchExpiredResult:

JsonValue; type "expired"constant

"expired"constant

class MessageBatchRequestCounts:

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

class MessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class MessageBatchSucceededResult:

[Message](/docs/en/api/messages#message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[Container](/docs/en/api/messages#container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

List\<[ContentBlock](/docs/en/api/messages#content_block)\> content

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

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_SONNET_4_6("claude-sonnet-4-6")

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

JsonValue; role "assistant"constant

"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

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

REFUSAL("refusal")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant

"message"constant

Object type.

For Messages, this is always `"message"`.

[Usage](/docs/en/api/messages#usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[CacheCreation](/docs/en/api/messages#cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

JsonValue; type "succeeded"constant

"succeeded"constant

class MessageBatchErroredResult:

[ErrorResponse](/docs/en/api/$shared#error_response) error

[ErrorObject](/docs/en/api/$shared#error_object) error

Accepts one of the following:

class InvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant

"invalid_request_error"constant

class AuthenticationError:

String message

JsonValue; type "authentication_error"constant

"authentication_error"constant

class BillingError:

String message

JsonValue; type "billing_error"constant

"billing_error"constant

class PermissionError:

String message

JsonValue; type "permission_error"constant

"permission_error"constant

class NotFoundError:

String message

JsonValue; type "not_found_error"constant

"not_found_error"constant

class RateLimitError:

String message

JsonValue; type "rate_limit_error"constant

"rate_limit_error"constant

class GatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant

"timeout_error"constant

class ApiErrorObject:

String message

JsonValue; type "api_error"constant

"api_error"constant

class OverloadedError:

String message

JsonValue; type "overloaded_error"constant

"overloaded_error"constant

Optional\<String\> requestId

JsonValue; type "error"constant

"error"constant

JsonValue; type "errored"constant

"errored"constant

class MessageBatchCanceledResult:

JsonValue; type "canceled"constant

"canceled"constant

class MessageBatchExpiredResult:

JsonValue; type "expired"constant

"expired"constant

class MessageBatchSucceededResult:

[Message](/docs/en/api/messages#message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional\<[Container](/docs/en/api/messages#container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

List\<[ContentBlock](/docs/en/api/messages#content_block)\> content

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

class TextBlock:

Optional\<List\<[TextCitation](/docs/en/api/messages#text_citation)\>\> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

String text

JsonValue; type "text"constant

"text"constant

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class ToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

class ServerToolUseBlock:

String id

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

class WebSearchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

[WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

MAX_USES_EXCEEDED("max_uses_exceeded")

TOO_MANY_REQUESTS("too_many_requests")

QUERY_TOO_LONG("query_too_long")

REQUEST_TOO_LARGE("request_too_large")

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

class WebFetchToolResultBlock:

Caller caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class ServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class ServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

Content content

Accepts one of the following:

class WebFetchToolResultErrorBlock:

[WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

URL_TOO_LONG("url_too_long")

URL_NOT_ALLOWED("url_not_allowed")

URL_NOT_ACCESSIBLE("url_not_accessible")

UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")

TOO_MANY_REQUESTS("too_many_requests")

MAX_USES_EXCEEDED("max_uses_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class WebFetchBlock:

[DocumentBlock](/docs/en/api/messages#document_block) content

Optional\<[CitationsConfig](/docs/en/api/messages#citations_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

Optional\<String\> title

The title of the document

JsonValue; type "document"constant

"document"constant

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web_fetch_result"constant

"web_fetch_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web_fetch_tool_result"constant

"web_fetch_tool_result"constant

class CodeExecutionToolResultBlock:

[CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError:

[CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class CodeExecutionResultBlock:

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class EncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted_code_execution_result"constant

"encrypted_code_execution_result"constant

String toolUseId

JsonValue; type "code_execution_tool_result"constant

"code_execution_tool_result"constant

class BashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BashCodeExecutionToolResultError:

[BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

OUTPUT_FILE_TOO_LARGE("output_file_too_large")

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BashCodeExecutionResultBlock:

List\<[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant

"bash_code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant

"bash_code_execution_result"constant

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant

"bash_code_execution_tool_result"constant

class TextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError:

[TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

FILE_NOT_FOUND("file_not_found")

Optional\<String\> errorMessage

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

class TextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class TextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class TextEditorCodeExecutionStrReplaceResultBlock:

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

JsonValue; type "text_editor_code_execution_str_replace_result"constant

"text_editor_code_execution_str_replace_result"constant

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant

"text_editor_code_execution_tool_result"constant

class ToolSearchToolResultBlock:

Content content

Accepts one of the following:

class ToolSearchToolResultError:

[ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

Optional\<String\> errorMessage

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class ToolSearchToolSearchResultBlock:

List\<[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class ContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_SONNET_4_6("claude-sonnet-4-6")

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

JsonValue; role "assistant"constant

"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

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

REFUSAL("refusal")

Optional\<String\> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant

"message"constant

Object type.

For Messages, this is always `"message"`.

[Usage](/docs/en/api/messages#usage) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional\<[CacheCreation](/docs/en/api/messages#cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional\<Long\> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional\<Long\> cacheReadInputTokens

The number of input tokens read from the cache.

Optional\<String\> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

JsonValue; type "succeeded"constant

"succeeded"constant

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
