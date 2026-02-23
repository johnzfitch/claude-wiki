---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:21:58Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/messages/count_tokens"
title: "Count tokens in a Message - Claude API Reference"
---

Copy page

C#

# Count tokens in a Message

[BetaMessageTokensCount](/docs/en/api/beta#beta_message_tokens_count) Beta.Messages.CountTokens(MessageCountTokensParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse 

MessageCountTokensParams parameters

required IReadOnlyList\<[BetaMessageParam](/docs/en/api/beta#beta_message_param)\> messages

Body param: Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single `user` message:

``` shiki
[{"role": "user", "content": "Hello, Claude"}]
```

Example with multiple conversational turns:

``` shiki
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```

Example with a partially-filled response from Claude:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]
```

Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

``` shiki
{"role": "user", "content": "Hello, Claude"}
```

``` shiki
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```

See [input examples](https://docs.claude.com/en/api/messages-examples).

Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.

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

required [Model](/docs/en/api/messages#model) model

Body param: The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)? cacheControl

Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

[BetaContextManagementConfig](/docs/en/api/beta#beta_context_management_config)? contextManagement

Body param: Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

IReadOnlyList\<[BetaRequestMcpServerUrlDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition)\> mcpServers

Body param: MCP servers to be utilized in this request

required string Name

JsonElement Type "url"constant

required string Url

string? AuthorizationToken

[BetaRequestMcpServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration)? ToolConfiguration

IReadOnlyList\<string\>? AllowedTools

Boolean? Enabled

[BetaOutputConfig](/docs/en/api/beta#beta_output_config) outputConfig

Body param: Configuration options for the model's output, such as the output format.

Deprecated[BetaJsonOutputFormat](/docs/en/api/beta#beta_json_output_format)? outputFormat

Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

[Speed](/docs/en/api/beta/messages/count_tokens)? speed

Body param: The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

"standard"Standard

"fast"Fast

[System](/docs/en/api/beta/messages/count_tokens) system

Body param: System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

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

[BetaThinkingConfigParam](/docs/en/api/beta#beta_thinking_config_param) thinking

Body param: Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

[BetaToolChoice](/docs/en/api/beta#beta_tool_choice) toolChoice

Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

IReadOnlyList\<Tool\> tools

Body param: Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

Each tool definition includes:

- `name`: Name of the tool.
- `description`: Optional, but strongly-recommended description of the tool.
- `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

For example, if you defined `tools` as:

``` shiki
[
  {
    "name": "get_stock_price",
    "description": "Get the current stock price for a given ticker symbol.",
    "input_schema": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
        }
      },
      "required": ["ticker"]
    }
  }
]
```

And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

``` shiki
[
  {
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
  }
]
```

You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

``` shiki
[
  {
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
  }
]
```

Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

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

IReadOnlyList\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024_09_24

"prompt-caching-2024-07-31"PromptCaching2024_07_31

"computer-use-2024-10-22"ComputerUse2024_10_22

"computer-use-2025-01-24"ComputerUse2025_01_24

"pdfs-2024-09-25"Pdfs2024_09_25

"token-counting-2024-11-01"TokenCounting2024_11_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19

"output-128k-2025-02-19"Output128k2025_02_19

"files-api-2025-04-14"FilesApi2025_04_14

"mcp-client-2025-04-04"McpClient2025_04_04

"mcp-client-2025-11-20"McpClient2025_11_20

"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14

"code-execution-2025-05-22"CodeExecution2025_05_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11

"context-1m-2025-08-07"Context1m2025_08_07

"context-management-2025-06-27"ContextManagement2025_06_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26

"skills-2025-10-02"Skills2025_10_02

"fast-mode-2026-02-01"FastMode2026_02_01

##### ReturnsExpand Collapse 

class BetaMessageTokensCount:

required [BetaCountTokensContextManagementResponse](/docs/en/api/beta#beta_count_tokens_context_management_response)? ContextManagement

Information about context management applied to the message.

required Long OriginalInputTokens

The original token count before context management was applied

required Long InputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

C#

``` shiki
MessageCountTokensParams parameters = new()
{
    Messages =
    [
        new()
        {
            Content = "string",
            Role = Role.User,
        },
    ],
    Model = Model.ClaudeOpus4_6,
};

var betaMessageTokensCount = await client.Beta.Messages.CountTokens(parameters);

Console.WriteLine(betaMessageTokensCount);
```

Response 200

``` shiki
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

##### Returns Examples

Response 200

``` shiki
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

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
