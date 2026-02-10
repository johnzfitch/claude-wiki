---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:08:23Z"
source_url: "https://platform.claude.com/docs/en/api/java/messages"
title: "Messages - Claude API Reference"
---

Copy page

Java

# Messages

##### [Create a Message](/docs/en/api/messages/create)

[Message](/docs/en/api/messages#message) messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages

##### [Count tokens in a Message](/docs/en/api/messages/count_tokens)

[MessageTokensCount](/docs/en/api/messages#message_tokens_count) messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages/count_tokens

##### ModelsExpand Collapse 

class Base64ImageSource:

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

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class CacheControlEphemeral:

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

class CacheCreation:

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

minimum0

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

minimum0

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class ContentBlock: A class that can be one of several variants.union

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

class ContentBlockParam: A class that can be one of several variants.union

Regular text content.

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class ThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class ToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant"tool_result"constant

Accepts one of the following:

TOOL_RESULT("tool_result")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

Optional\<Boolean\> isError

class ServerToolUseBlockParam:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class WebSearchToolResultBlockParam:

[WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class WebSearchToolRequestError:

ErrorCode errorCode

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class ContentBlockSourceContent: A class that can be one of several variants.union

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class InputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant"input_json_delta"constant

Accepts one of the following:

INPUT_JSON_DELTA("input_json_delta")

class JsonOutputFormat:

Schema schema

The JSON schema of the format

JsonValue; type "json_schema"constant"json_schema"constant

Accepts one of the following:

JSON_SCHEMA("json_schema")

class Message:

String id

Unique object identifier.

The format and length of IDs may change over time.

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

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

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webSearchRequests

The number of web search tool requests.

minimum0

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

class MessageCountTokensTool: A class that can be one of several variants.union

class Tool:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<String\> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional\<Boolean\> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<Type\> type

Accepts one of the following:

CUSTOM("custom")

class ToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20250124"constant"bash_20250124"constant

Accepts one of the following:

BASH_20250124("bash_20250124")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20250124"constant"text_editor_20250124"constant

Accepts one of the following:

TEXT_EDITOR_20250124("text_editor_20250124")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250429"constant"text_editor_20250429"constant

Accepts one of the following:

TEXT_EDITOR_20250429("text_editor_20250429")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250728"constant"text_editor_20250728"constant

Accepts one of the following:

TEXT_EDITOR_20250728("text_editor_20250728")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Long\> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305:

JsonValue; name "web_search"constant"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "web_search_20250305"constant"web_search_20250305"constant

Accepts one of the following:

WEB_SEARCH_20250305("web_search_20250305")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class MessageDeltaUsage:

Optional\<Long\> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

minimum0

Optional\<Long\> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

minimum0

Optional\<Long\> inputTokens

The cumulative number of input tokens which were used.

minimum0

long outputTokens

The cumulative number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webSearchRequests

The number of web search tool requests.

minimum0

class MessageParam:

Content content

Accepts one of the following:

String

List\<[ContentBlockParam](/docs/en/api/messages#content_block_param)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class ThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class ToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant"tool_result"constant

Accepts one of the following:

TOOL_RESULT("tool_result")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

Optional\<Boolean\> isError

class ServerToolUseBlockParam:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class WebSearchToolResultBlockParam:

[WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class WebSearchToolRequestError:

ErrorCode errorCode

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

JsonValue; type "json_schema"constant"json_schema"constant

Accepts one of the following:

JSON_SCHEMA("json_schema")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class RawContentBlockDelta: A class that can be one of several variants.union

class TextDelta:

String text

JsonValue; type "text_delta"constant"text_delta"constant

Accepts one of the following:

TEXT_DELTA("text_delta")

class InputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant"input_json_delta"constant

Accepts one of the following:

INPUT_JSON_DELTA("input_json_delta")

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant"thinking_delta"constant

Accepts one of the following:

THINKING_DELTA("thinking_delta")

class SignatureDelta:

String signature

JsonValue; type "signature_delta"constant"signature_delta"constant

Accepts one of the following:

SIGNATURE_DELTA("signature_delta")

class RawContentBlockDeltaEvent:

[RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta) delta

Accepts one of the following:

class TextDelta:

String text

JsonValue; type "text_delta"constant"text_delta"constant

Accepts one of the following:

TEXT_DELTA("text_delta")

class InputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant"input_json_delta"constant

Accepts one of the following:

INPUT_JSON_DELTA("input_json_delta")

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant"thinking_delta"constant

Accepts one of the following:

THINKING_DELTA("thinking_delta")

class SignatureDelta:

String signature

JsonValue; type "signature_delta"constant"signature_delta"constant

Accepts one of the following:

SIGNATURE_DELTA("signature_delta")

long index

JsonValue; type "content_block_delta"constant"content_block_delta"constant

Accepts one of the following:

CONTENT_BLOCK_DELTA("content_block_delta")

class RawContentBlockStartEvent:

ContentBlock contentBlock

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

long index

JsonValue; type "content_block_start"constant"content_block_start"constant

Accepts one of the following:

CONTENT_BLOCK_START("content_block_start")

class RawContentBlockStopEvent:

long index

JsonValue; type "content_block_stop"constant"content_block_stop"constant

Accepts one of the following:

CONTENT_BLOCK_STOP("content_block_stop")

class RawMessageDeltaEvent:

Delta delta

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

Accepts one of the following:

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

REFUSAL("refusal")

Optional\<String\> stopSequence

JsonValue; type "message_delta"constant"message_delta"constant

Accepts one of the following:

MESSAGE_DELTA("message_delta")

[MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) usage

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

long outputTokens

The cumulative number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webSearchRequests

The number of web search tool requests.

minimum0

class RawMessageStartEvent:

[Message](/docs/en/api/messages#message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

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

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

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

class RawMessageStopEvent:

JsonValue; type "message_stop"constant"message_stop"constant

Accepts one of the following:

MESSAGE_STOP("message_stop")

class RawMessageStreamEvent: A class that can be one of several variants.union

class RawMessageStartEvent:

[Message](/docs/en/api/messages#message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

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

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

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

class RawMessageDeltaEvent:

Delta delta

Optional\<[StopReason](/docs/en/api/messages#stop_reason)\> stopReason

Accepts one of the following:

END_TURN("end_turn")

MAX_TOKENS("max_tokens")

STOP_SEQUENCE("stop_sequence")

TOOL_USE("tool_use")

PAUSE_TURN("pause_turn")

REFUSAL("refusal")

Optional\<String\> stopSequence

JsonValue; type "message_delta"constant"message_delta"constant

Accepts one of the following:

MESSAGE_DELTA("message_delta")

[MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) usage

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

long outputTokens

The cumulative number of output tokens which were used.

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webSearchRequests

The number of web search tool requests.

minimum0

class RawMessageStopEvent:

JsonValue; type "message_stop"constant"message_stop"constant

Accepts one of the following:

MESSAGE_STOP("message_stop")

class RawContentBlockStartEvent:

ContentBlock contentBlock

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

long index

JsonValue; type "content_block_start"constant"content_block_start"constant

Accepts one of the following:

CONTENT_BLOCK_START("content_block_start")

class RawContentBlockDeltaEvent:

[RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta) delta

Accepts one of the following:

class TextDelta:

String text

JsonValue; type "text_delta"constant"text_delta"constant

Accepts one of the following:

TEXT_DELTA("text_delta")

class InputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant"input_json_delta"constant

Accepts one of the following:

INPUT_JSON_DELTA("input_json_delta")

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant"thinking_delta"constant

Accepts one of the following:

THINKING_DELTA("thinking_delta")

class SignatureDelta:

String signature

JsonValue; type "signature_delta"constant"signature_delta"constant

Accepts one of the following:

SIGNATURE_DELTA("signature_delta")

long index

JsonValue; type "content_block_delta"constant"content_block_delta"constant

Accepts one of the following:

CONTENT_BLOCK_DELTA("content_block_delta")

class RawContentBlockStopEvent:

long index

JsonValue; type "content_block_stop"constant"content_block_stop"constant

Accepts one of the following:

CONTENT_BLOCK_STOP("content_block_stop")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class RedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class ServerToolUsage:

long webSearchRequests

The number of web search tool requests.

minimum0

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class ServerToolUseBlockParam:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class SignatureDelta:

String signature

JsonValue; type "signature_delta"constant"signature_delta"constant

Accepts one of the following:

SIGNATURE_DELTA("signature_delta")

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class TextCitation: A class that can be one of several variants.union

class CitationCharLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

Optional\<String\> fileId

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class TextCitationParam: A class that can be one of several variants.union

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

class TextDelta:

String text

JsonValue; type "text_delta"constant"text_delta"constant

Accepts one of the following:

TEXT_DELTA("text_delta")

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class ThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class ThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant

Accepts one of the following:

ADAPTIVE("adaptive")

class ThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class ThinkingConfigEnabled:

long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

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

JsonValue; type "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

class ThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class ThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant

Accepts one of the following:

ADAPTIVE("adaptive")

class ThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant"thinking_delta"constant

Accepts one of the following:

THINKING_DELTA("thinking_delta")

class Tool:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<String\> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional\<Boolean\> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<Type\> type

Accepts one of the following:

CUSTOM("custom")

class ToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20250124"constant"bash_20250124"constant

Accepts one of the following:

BASH_20250124("bash_20250124")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant

Accepts one of the following:

ANY("any")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant

Accepts one of the following:

NONE("none")

class ToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant

Accepts one of the following:

ANY("any")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant

Accepts one of the following:

NONE("none")

class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant"tool_result"constant

Accepts one of the following:

TOOL_RESULT("tool_result")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class SearchResultBlockParam:

List\<[TextBlockParam](/docs/en/api/messages#text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

class DocumentBlockParam:

Source source

Accepts one of the following:

class Base64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class PlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class ContentBlockSource:

Content content

Accepts one of the following:

String

List\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

class TextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\>\> citations

Accepts one of the following:

class CitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<[CitationsConfigParam](/docs/en/api/messages#citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

Optional\<Boolean\> isError

class ToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20250124"constant"text_editor_20250124"constant

Accepts one of the following:

TEXT_EDITOR_20250124("text_editor_20250124")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250429"constant"text_editor_20250429"constant

Accepts one of the following:

TEXT_EDITOR_20250429("text_editor_20250429")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250728"constant"text_editor_20250728"constant

Accepts one of the following:

TEXT_EDITOR_20250728("text_editor_20250728")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Long\> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolUnion: A class that can be one of several variants.union

class Tool:

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<String\> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional\<Boolean\> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

Optional\<Type\> type

Accepts one of the following:

CUSTOM("custom")

class ToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20250124"constant"bash_20250124"constant

Accepts one of the following:

BASH_20250124("bash_20250124")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20250124"constant"text_editor_20250124"constant

Accepts one of the following:

TEXT_EDITOR_20250124("text_editor_20250124")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250429"constant"text_editor_20250429"constant

Accepts one of the following:

TEXT_EDITOR_20250429("text_editor_20250429")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250728"constant"text_editor_20250728"constant

Accepts one of the following:

TEXT_EDITOR_20250728("text_editor_20250728")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

Optional\<Long\> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305:

JsonValue; name "web_search"constant"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "web_search_20250305"constant"web_search_20250305"constant

Accepts one of the following:

WEB_SEARCH_20250305("web_search_20250305")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class UrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class UrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class Usage:

Optional\<[CacheCreation](/docs/en/api/messages#cache_creation)\> cacheCreation

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

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

long webSearchRequests

The number of web search tool requests.

minimum0

Optional\<ServiceTier\> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

class WebSearchResultBlock:

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

class WebSearchResultBlockParam:

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class WebSearchTool20250305:

JsonValue; name "web_search"constant"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "web_search_20250305"constant"web_search_20250305"constant

Accepts one of the following:

WEB_SEARCH_20250305("web_search_20250305")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class WebSearchToolRequestError:

ErrorCode errorCode

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

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

class WebSearchToolResultBlockContent: A class that can be one of several variants.union

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

class WebSearchToolResultBlockParam:

[WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class WebSearchToolRequestError:

ErrorCode errorCode

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

Optional\<[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\> cacheControl

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

class WebSearchToolResultBlockParamContent: A class that can be one of several variants.union

List\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

String url

Optional\<String\> pageAge

class WebSearchToolRequestError:

ErrorCode errorCode

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

class WebSearchToolResultError:

ErrorCode errorCode

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

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

[MessageBatch](/docs/en/api/messages#message_batch) messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

[MessageBatch](/docs/en/api/messages#message_batch) messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

BatchListPage messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

[MessageBatch](/docs/en/api/messages#message_batch) messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

[DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch) messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

[MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response) messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class DeletedMessageBatch:

String id

ID of the Message Batch.

JsonValue; type "message_batch_deleted"constant"message_batch_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

MESSAGE_BATCH_DELETED("message_batch_deleted")

class MessageBatch:

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

JsonValue; type "message_batch"constant"message_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

MESSAGE_BATCH("message_batch")

class MessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class MessageBatchErroredResult:

[ErrorResponse](/docs/en/api/$shared#error_response) error

[ErrorObject](/docs/en/api/$shared#error_object) error

Accepts one of the following:

class InvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant"invalid_request_error"constant

Accepts one of the following:

INVALID_REQUEST_ERROR("invalid_request_error")

class AuthenticationError:

String message

JsonValue; type "authentication_error"constant"authentication_error"constant

Accepts one of the following:

AUTHENTICATION_ERROR("authentication_error")

class BillingError:

String message

JsonValue; type "billing_error"constant"billing_error"constant

Accepts one of the following:

BILLING_ERROR("billing_error")

class PermissionError:

String message

JsonValue; type "permission_error"constant"permission_error"constant

Accepts one of the following:

PERMISSION_ERROR("permission_error")

class NotFoundError:

String message

JsonValue; type "not_found_error"constant"not_found_error"constant

Accepts one of the following:

NOT_FOUND_ERROR("not_found_error")

class RateLimitError:

String message

JsonValue; type "rate_limit_error"constant"rate_limit_error"constant

Accepts one of the following:

RATE_LIMIT_ERROR("rate_limit_error")

class GatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant"timeout_error"constant

Accepts one of the following:

TIMEOUT_ERROR("timeout_error")

class ApiErrorObject:

String message

JsonValue; type "api_error"constant"api_error"constant

Accepts one of the following:

API_ERROR("api_error")

class OverloadedError:

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

class MessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

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

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

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

class MessageBatchErroredResult:

[ErrorResponse](/docs/en/api/$shared#error_response) error

[ErrorObject](/docs/en/api/$shared#error_object) error

Accepts one of the following:

class InvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant"invalid_request_error"constant

Accepts one of the following:

INVALID_REQUEST_ERROR("invalid_request_error")

class AuthenticationError:

String message

JsonValue; type "authentication_error"constant"authentication_error"constant

Accepts one of the following:

AUTHENTICATION_ERROR("authentication_error")

class BillingError:

String message

JsonValue; type "billing_error"constant"billing_error"constant

Accepts one of the following:

BILLING_ERROR("billing_error")

class PermissionError:

String message

JsonValue; type "permission_error"constant"permission_error"constant

Accepts one of the following:

PERMISSION_ERROR("permission_error")

class NotFoundError:

String message

JsonValue; type "not_found_error"constant"not_found_error"constant

Accepts one of the following:

NOT_FOUND_ERROR("not_found_error")

class RateLimitError:

String message

JsonValue; type "rate_limit_error"constant"rate_limit_error"constant

Accepts one of the following:

RATE_LIMIT_ERROR("rate_limit_error")

class GatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant"timeout_error"constant

Accepts one of the following:

TIMEOUT_ERROR("timeout_error")

class ApiErrorObject:

String message

JsonValue; type "api_error"constant"api_error"constant

Accepts one of the following:

API_ERROR("api_error")

class OverloadedError:

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

class MessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class MessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

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

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

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

class MessageBatchErroredResult:

[ErrorResponse](/docs/en/api/$shared#error_response) error

[ErrorObject](/docs/en/api/$shared#error_object) error

Accepts one of the following:

class InvalidRequestError:

String message

JsonValue; type "invalid_request_error"constant"invalid_request_error"constant

Accepts one of the following:

INVALID_REQUEST_ERROR("invalid_request_error")

class AuthenticationError:

String message

JsonValue; type "authentication_error"constant"authentication_error"constant

Accepts one of the following:

AUTHENTICATION_ERROR("authentication_error")

class BillingError:

String message

JsonValue; type "billing_error"constant"billing_error"constant

Accepts one of the following:

BILLING_ERROR("billing_error")

class PermissionError:

String message

JsonValue; type "permission_error"constant"permission_error"constant

Accepts one of the following:

PERMISSION_ERROR("permission_error")

class NotFoundError:

String message

JsonValue; type "not_found_error"constant"not_found_error"constant

Accepts one of the following:

NOT_FOUND_ERROR("not_found_error")

class RateLimitError:

String message

JsonValue; type "rate_limit_error"constant"rate_limit_error"constant

Accepts one of the following:

RATE_LIMIT_ERROR("rate_limit_error")

class GatewayTimeoutError:

String message

JsonValue; type "timeout_error"constant"timeout_error"constant

Accepts one of the following:

TIMEOUT_ERROR("timeout_error")

class ApiErrorObject:

String message

JsonValue; type "api_error"constant"api_error"constant

Accepts one of the following:

API_ERROR("api_error")

class OverloadedError:

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

class MessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class MessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class MessageBatchSucceededResult:

[Message](/docs/en/api/messages#message) message

String id

Unique object identifier.

The format and length of IDs may change over time.

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

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class CitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class CitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class CitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class CitationsSearchResultLocation:

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

class ThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class RedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class ToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

class ServerToolUseBlock:

String id

Input input

JsonValue; name "web_search"constant"web_search"constant

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

class WebSearchToolResultBlock:

[WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content) content

Accepts one of the following:

class WebSearchToolResultError:

ErrorCode errorCode

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

List\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\>

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

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

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

long outputTokens

The number of output tokens which were used.

minimum0

Optional\<[ServerToolUsage](/docs/en/api/messages#server_tool_usage)\> serverToolUse

The number of server tool requests.

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
