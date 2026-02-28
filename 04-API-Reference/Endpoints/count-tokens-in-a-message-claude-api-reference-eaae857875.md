---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:45:02Z"
source_url: "https://platform.claude.com/docs/en/api/java/messages/count_tokens"
title: "Count tokens in a Message - Claude API Reference"
---
# Count tokens in a Message

[MessageTokensCount](/docs/en/api/messages#message_tokens_count) messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse 

MessageCountTokensParams params

List\<[MessageParam](/docs/en/api/messages#message_param)\> messages

Input messages.

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

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

Optional\<[OutputConfig](/docs/en/api/messages#output_config)\> outputConfig

Configuration options for the model's output, such as the output format.

Optional\<System\> system

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

String

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\>

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

Optional\<[ThinkingConfigParam](/docs/en/api/messages#thinking_config_param)\> thinking

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Optional\<[ToolChoice](/docs/en/api/messages#tool_choice)\> toolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Optional\<List\<[MessageCountTokensTool](/docs/en/api/messages#message_count_tokens_tool)\>\> tools

Definitions of tools that the model may use.

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

##### ReturnsExpand Collapse 

class MessageTokensCount:

long inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

Java

``` shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCountTokensParams;
import com.anthropic.models.messages.MessageTokensCount;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCountTokensParams params = MessageCountTokensParams.builder()
            .addUserMessage("Hello, world")
            .model(Model.CLAUDE_OPUS_4_6)
            .build();
        MessageTokensCount messageTokensCount = client.messages().countTokens(params);
