---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:09:35Z"
source_url: "https://platform.claude.com/docs/en/api/go/messages"
title: "Messages - Claude API Reference"
---

Copy page

Go

# Messages

##### [Create a Message](/docs/en/api/messages/create)

client.Messages.New(ctx, body) (\*[Message](/docs/en/api/messages#message), error)

post/v1/messages

##### [Count tokens in a Message](/docs/en/api/messages/count_tokens)

client.Messages.CountTokens(ctx, body) (\*[MessageTokensCount](/docs/en/api/messages#message_tokens_count), error)

post/v1/messages/count_tokens

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type CacheControlEphemeral struct{…}

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

minimum0

Ephemeral5mInputTokens int64

The number of input tokens used to create the 5 minute cache entry.

minimum0

type CitationCharLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

FileID string

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsConfigParamResp struct{…}

Enabled booloptional

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Type CitationsDelta

Accepts one of the following:

const CitationsDeltaCitationsDelta CitationsDelta = "citations_delta"

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type ContentBlockUnion interface{…}

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

type ContentBlockParamUnionResp interface{…}

Regular text content.

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type URLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Source string

Title string

Type SearchResult

Accepts one of the following:

const SearchResultSearchResult SearchResult = "search_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const ToolResultToolResult ToolResult = "tool_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Content \[\]ToolResultBlockParamContentUnionRespoptional

Accepts one of the following:

\[\]ToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Source string

Title string

Type SearchResult

Accepts one of the following:

const SearchResultSearchResult SearchResult = "search_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type URLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

IsError booloptional

type ServerToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type WebSearchToolResultBlockParamResp struct{…}

Content [WebSearchToolResultBlockParamContentUnionResp](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

PageAge stringoptional

type WebSearchToolRequestError struct{…}

ErrorCode WebSearchToolRequestErrorErrorCode

Accepts one of the following:

const WebSearchToolRequestErrorErrorCodeInvalidToolInput WebSearchToolRequestErrorErrorCode = "invalid_tool_input"

const WebSearchToolRequestErrorErrorCodeUnavailable WebSearchToolRequestErrorErrorCode = "unavailable"

const WebSearchToolRequestErrorErrorCodeMaxUsesExceeded WebSearchToolRequestErrorErrorCode = "max_uses_exceeded"

const WebSearchToolRequestErrorErrorCodeTooManyRequests WebSearchToolRequestErrorErrorCode = "too_many_requests"

const WebSearchToolRequestErrorErrorCodeQueryTooLong WebSearchToolRequestErrorErrorCode = "query_too_long"

const WebSearchToolRequestErrorErrorCodeRequestTooLarge WebSearchToolRequestErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web_search_tool_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type ContentBlockSourceContentItemUnion interface{…}

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type URLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const InputJSONDeltaInputJSONDelta InputJSONDelta = "input_json_delta"

type JSONOutputFormat struct{…}

Schema map\[string, any\]

The JSON schema of the format

Type JSONSchema

Accepts one of the following:

const JSONSchemaJSONSchema JSONSchema = "json_schema"

type Message struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

Accepts one of the following:

const MessageMessage Message = "message"

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

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

type MessageCountTokensToolUnion interface{…}

Accepts one of the following:

type Tool struct{…}

InputSchema ToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Accepts one of the following:

const ObjectObject Object = "object"

Properties map\[string, any\]optional

Required \[\]stringoptional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Description stringoptional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming booloptional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

Type ToolTypeoptional

Accepts one of the following:

const ToolTypeCustom ToolType = "custom"

type ToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const BashBash Bash = "bash"

Type Bash20250124

Accepts one of the following:

const Bash20250124Bash20250124 Bash20250124 = "bash_20250124"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceEditorStrReplaceEditor StrReplaceEditor = "str_replace_editor"

Type TextEditor20250124

Accepts one of the following:

const TextEditor20250124TextEditor20250124 TextEditor20250124 = "text_editor_20250124"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"

Type TextEditor20250429

Accepts one of the following:

const TextEditor20250429TextEditor20250429 TextEditor20250429 = "text_editor_20250429"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"

Type TextEditor20250728

Accepts one of the following:

const TextEditor20250728TextEditor20250728 TextEditor20250728 = "text_editor_20250728"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

MaxCharacters int64optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type WebSearch20250305

Accepts one of the following:

const WebSearch20250305WebSearch20250305 WebSearch20250305 = "web_search_20250305"

AllowedDomains \[\]stringoptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]stringoptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Strict booloptional

When true, guarantees schema validation on tool names and inputs

UserLocation WebSearchTool20250305UserLocationoptional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

Accepts one of the following:

const ApproximateApproximate Approximate = "approximate"

City stringoptional

The city of the user.

maxLength255

minLength1

Country stringoptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

Region stringoptional

The region of the user.

maxLength255

minLength1

Timezone stringoptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

type MessageDeltaUsage struct{…}

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

minimum0

InputTokens int64

The cumulative number of input tokens which were used.

minimum0

OutputTokens int64

The cumulative number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

type MessageParamResp struct{…}

Content \[\][ContentBlockParamUnionResp](/docs/en/api/messages#content_block_param)

Accepts one of the following:

\[\][ContentBlockParamUnionResp](/docs/en/api/messages#content_block_param)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type URLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Source string

Title string

Type SearchResult

Accepts one of the following:

const SearchResultSearchResult SearchResult = "search_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const ToolResultToolResult ToolResult = "tool_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Content \[\]ToolResultBlockParamContentUnionRespoptional

Accepts one of the following:

\[\]ToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Source string

Title string

Type SearchResult

Accepts one of the following:

const SearchResultSearchResult SearchResult = "search_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type URLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

IsError booloptional

type ServerToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type WebSearchToolResultBlockParamResp struct{…}

Content [WebSearchToolResultBlockParamContentUnionResp](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

PageAge stringoptional

type WebSearchToolRequestError struct{…}

ErrorCode WebSearchToolRequestErrorErrorCode

Accepts one of the following:

const WebSearchToolRequestErrorErrorCodeInvalidToolInput WebSearchToolRequestErrorErrorCode = "invalid_tool_input"

const WebSearchToolRequestErrorErrorCodeUnavailable WebSearchToolRequestErrorErrorCode = "unavailable"

const WebSearchToolRequestErrorErrorCodeMaxUsesExceeded WebSearchToolRequestErrorErrorCode = "max_uses_exceeded"

const WebSearchToolRequestErrorErrorCodeTooManyRequests WebSearchToolRequestErrorErrorCode = "too_many_requests"

const WebSearchToolRequestErrorErrorCodeQueryTooLong WebSearchToolRequestErrorErrorCode = "query_too_long"

const WebSearchToolRequestErrorErrorCodeRequestTooLarge WebSearchToolRequestErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web_search_tool_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

UserID stringoptional

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

Effort OutputConfigEffortoptional

All possible effort levels.

Accepts one of the following:

const OutputConfigEffortLow OutputConfigEffort = "low"

const OutputConfigEffortMedium OutputConfigEffort = "medium"

const OutputConfigEffortHigh OutputConfigEffort = "high"

const OutputConfigEffortMax OutputConfigEffort = "max"

Format [JSONOutputFormat](/docs/en/api/messages#json_output_format)optional

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

Schema map\[string, any\]

The JSON schema of the format

Type JSONSchema

Accepts one of the following:

const JSONSchemaJSONSchema JSONSchema = "json_schema"

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

type RawContentBlockDeltaUnion interface{…}

Accepts one of the following:

type TextDelta struct{…}

Text string

Type TextDelta

Accepts one of the following:

const TextDeltaTextDelta TextDelta = "text_delta"

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta

Accepts one of the following:

const InputJSONDeltaInputJSONDelta InputJSONDelta = "input_json_delta"

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Type CitationsDelta

Accepts one of the following:

const CitationsDeltaCitationsDelta CitationsDelta = "citations_delta"

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

Accepts one of the following:

const ThinkingDeltaThinkingDelta ThinkingDelta = "thinking_delta"

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Accepts one of the following:

const SignatureDeltaSignatureDelta SignatureDelta = "signature_delta"

type ContentBlockDeltaEvent struct{…}

Delta [RawContentBlockDeltaUnion](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

type TextDelta struct{…}

Text string

Type TextDelta

Accepts one of the following:

const TextDeltaTextDelta TextDelta = "text_delta"

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta

Accepts one of the following:

const InputJSONDeltaInputJSONDelta InputJSONDelta = "input_json_delta"

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Type CitationsDelta

Accepts one of the following:

const CitationsDeltaCitationsDelta CitationsDelta = "citations_delta"

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

Accepts one of the following:

const ThinkingDeltaThinkingDelta ThinkingDelta = "thinking_delta"

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Accepts one of the following:

const SignatureDeltaSignatureDelta SignatureDelta = "signature_delta"

Index int64

Type ContentBlockDelta

Accepts one of the following:

const ContentBlockDeltaContentBlockDelta ContentBlockDelta = "content_block_delta"

type ContentBlockStartEvent struct{…}

ContentBlock ContentBlockStartEventContentBlockUnion

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

Index int64

Type ContentBlockStart

Accepts one of the following:

const ContentBlockStartContentBlockStart ContentBlockStart = "content_block_start"

type ContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop

Accepts one of the following:

const ContentBlockStopContentBlockStop ContentBlockStop = "content_block_stop"

type MessageDeltaEvent struct{…}

Delta MessageDeltaEventDelta

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

Accepts one of the following:

const MessageDeltaMessageDelta MessageDelta = "message_delta"

Usage [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

minimum0

InputTokens int64

The cumulative number of input tokens which were used.

minimum0

OutputTokens int64

The cumulative number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

type MessageStartEvent struct{…}

Message [Message](/docs/en/api/messages#message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

Accepts one of the following:

const MessageMessage Message = "message"

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

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type MessageStart

Accepts one of the following:

const MessageStartMessageStart MessageStart = "message_start"

type MessageStopEvent struct{…}

Type MessageStop

Accepts one of the following:

const MessageStopMessageStop MessageStop = "message_stop"

type MessageStreamEventUnion interface{…}

Accepts one of the following:

type MessageStartEvent struct{…}

Message [Message](/docs/en/api/messages#message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

Accepts one of the following:

const MessageMessage Message = "message"

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

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type MessageStart

Accepts one of the following:

const MessageStartMessageStart MessageStart = "message_start"

type MessageDeltaEvent struct{…}

Delta MessageDeltaEventDelta

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

Accepts one of the following:

const MessageDeltaMessageDelta MessageDelta = "message_delta"

Usage [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

CacheCreationInputTokens int64

The cumulative number of input tokens used to create the cache entry.

minimum0

CacheReadInputTokens int64

The cumulative number of input tokens read from the cache.

minimum0

InputTokens int64

The cumulative number of input tokens which were used.

minimum0

OutputTokens int64

The cumulative number of output tokens which were used.

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

type MessageStopEvent struct{…}

Type MessageStop

Accepts one of the following:

const MessageStopMessageStop MessageStop = "message_stop"

type ContentBlockStartEvent struct{…}

ContentBlock ContentBlockStartEventContentBlockUnion

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

Index int64

Type ContentBlockStart

Accepts one of the following:

const ContentBlockStartContentBlockStart ContentBlockStart = "content_block_start"

type ContentBlockDeltaEvent struct{…}

Delta [RawContentBlockDeltaUnion](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

type TextDelta struct{…}

Text string

Type TextDelta

Accepts one of the following:

const TextDeltaTextDelta TextDelta = "text_delta"

type InputJSONDelta struct{…}

PartialJSON string

Type InputJSONDelta

Accepts one of the following:

const InputJSONDeltaInputJSONDelta InputJSONDelta = "input_json_delta"

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Type CitationsDelta

Accepts one of the following:

const CitationsDeltaCitationsDelta CitationsDelta = "citations_delta"

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

Accepts one of the following:

const ThinkingDeltaThinkingDelta ThinkingDelta = "thinking_delta"

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Accepts one of the following:

const SignatureDeltaSignatureDelta SignatureDelta = "signature_delta"

Index int64

Type ContentBlockDelta

Accepts one of the following:

const ContentBlockDeltaContentBlockDelta ContentBlockDelta = "content_block_delta"

type ContentBlockStopEvent struct{…}

Index int64

Type ContentBlockStop

Accepts one of the following:

const ContentBlockStopContentBlockStop ContentBlockStop = "content_block_stop"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Source string

Title string

Type SearchResult

Accepts one of the following:

const SearchResultSearchResult SearchResult = "search_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

type ServerToolUsage struct{…}

WebSearchRequests int64

The number of web search tool requests.

minimum0

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type ServerToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type SignatureDelta struct{…}

Signature string

Type SignatureDelta

Accepts one of the following:

const SignatureDeltaSignatureDelta SignatureDelta = "signature_delta"

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type TextCitationParamUnionResp interface{…}

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type TextDelta struct{…}

Text string

Type TextDelta

Accepts one of the following:

const TextDeltaTextDelta TextDelta = "text_delta"

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type ThinkingConfigAdaptive struct{…}

Type Adaptive

Accepts one of the following:

const AdaptiveAdaptive Adaptive = "adaptive"

type ThinkingConfigDisabled struct{…}

Type Disabled

Accepts one of the following:

const DisabledDisabled Disabled = "disabled"

type ThinkingConfigEnabled struct{…}

BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

Type Enabled

Accepts one of the following:

const EnabledEnabled Enabled = "enabled"

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

Accepts one of the following:

const EnabledEnabled Enabled = "enabled"

type ThinkingConfigDisabled struct{…}

Type Disabled

Accepts one of the following:

const DisabledDisabled Disabled = "disabled"

type ThinkingConfigAdaptive struct{…}

Type Adaptive

Accepts one of the following:

const AdaptiveAdaptive Adaptive = "adaptive"

type ThinkingDelta struct{…}

Thinking string

Type ThinkingDelta

Accepts one of the following:

const ThinkingDeltaThinkingDelta ThinkingDelta = "thinking_delta"

type Tool struct{…}

InputSchema ToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Accepts one of the following:

const ObjectObject Object = "object"

Properties map\[string, any\]optional

Required \[\]stringoptional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Description stringoptional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming booloptional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

Type ToolTypeoptional

Accepts one of the following:

const ToolTypeCustom ToolType = "custom"

type ToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const BashBash Bash = "bash"

Type Bash20250124

Accepts one of the following:

const Bash20250124Bash20250124 Bash20250124 = "bash_20250124"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolChoiceUnion interface{…}

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

type ToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto

Accepts one of the following:

const AutoAuto Auto = "auto"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

type ToolChoiceAny struct{…}

The model will use any available tools.

Type Any

Accepts one of the following:

const AnyAny Any = "any"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type ToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool

Accepts one of the following:

const ToolTool Tool = "tool"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type ToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None

Accepts one of the following:

const NoneNone None = "none"

type ToolChoiceAny struct{…}

The model will use any available tools.

Type Any

Accepts one of the following:

const AnyAny Any = "any"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type ToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto

Accepts one of the following:

const AutoAuto Auto = "auto"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

type ToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None

Accepts one of the following:

const NoneNone None = "none"

type ToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool

Accepts one of the following:

const ToolTool Tool = "tool"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type ToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult

Accepts one of the following:

const ToolResultToolResult ToolResult = "tool_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Content \[\]ToolResultBlockParamContentUnionRespoptional

Accepts one of the following:

\[\]ToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

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

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Source string

Title string

Type SearchResult

Accepts one of the following:

const SearchResultSearchResult SearchResult = "search_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Accepts one of the following:

const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Accepts one of the following:

const TextPlainTextPlain TextPlain = "text/plain"

Type Text

Accepts one of the following:

const TextText Text = "text"

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

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

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type URLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

IsError booloptional

type ToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceEditorStrReplaceEditor StrReplaceEditor = "str_replace_editor"

Type TextEditor20250124

Accepts one of the following:

const TextEditor20250124TextEditor20250124 TextEditor20250124 = "text_editor_20250124"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"

Type TextEditor20250429

Accepts one of the following:

const TextEditor20250429TextEditor20250429 TextEditor20250429 = "text_editor_20250429"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"

Type TextEditor20250728

Accepts one of the following:

const TextEditor20250728TextEditor20250728 TextEditor20250728 = "text_editor_20250728"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

MaxCharacters int64optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolUnion interface{…}

Accepts one of the following:

type Tool struct{…}

InputSchema ToolInputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

Type Object

Accepts one of the following:

const ObjectObject Object = "object"

Properties map\[string, any\]optional

Required \[\]stringoptional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Description stringoptional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming booloptional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

Type ToolTypeoptional

Accepts one of the following:

const ToolTypeCustom ToolType = "custom"

type ToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const BashBash Bash = "bash"

Type Bash20250124

Accepts one of the following:

const Bash20250124Bash20250124 Bash20250124 = "bash_20250124"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceEditorStrReplaceEditor StrReplaceEditor = "str_replace_editor"

Type TextEditor20250124

Accepts one of the following:

const TextEditor20250124TextEditor20250124 TextEditor20250124 = "text_editor_20250124"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"

Type TextEditor20250429

Accepts one of the following:

const TextEditor20250429TextEditor20250429 TextEditor20250429 = "text_editor_20250429"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"

Type TextEditor20250728

Accepts one of the following:

const TextEditor20250728TextEditor20250728 TextEditor20250728 = "text_editor_20250728"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

MaxCharacters int64optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type WebSearch20250305

Accepts one of the following:

const WebSearch20250305WebSearch20250305 WebSearch20250305 = "web_search_20250305"

AllowedDomains \[\]stringoptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]stringoptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Strict booloptional

When true, guarantees schema validation on tool names and inputs

UserLocation WebSearchTool20250305UserLocationoptional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

Accepts one of the following:

const ApproximateApproximate Approximate = "approximate"

City stringoptional

The city of the user.

maxLength255

minLength1

Country stringoptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

Region stringoptional

The region of the user.

maxLength255

minLength1

Timezone stringoptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type URLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type URLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type Usage struct{…}

CacheCreation [CacheCreation](/docs/en/api/messages#cache_creation)

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

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

type WebSearchResultBlock struct{…}

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

type WebSearchResultBlockParamResp struct{…}

EncryptedContent string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

PageAge stringoptional

type WebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type WebSearch20250305

Accepts one of the following:

const WebSearch20250305WebSearch20250305 WebSearch20250305 = "web_search_20250305"

AllowedDomains \[\]stringoptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]stringoptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Strict booloptional

When true, guarantees schema validation on tool names and inputs

UserLocation WebSearchTool20250305UserLocationoptional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

Accepts one of the following:

const ApproximateApproximate Approximate = "approximate"

City stringoptional

The city of the user.

maxLength255

minLength1

Country stringoptional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

Region stringoptional

The region of the user.

maxLength255

minLength1

Timezone stringoptional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

type WebSearchToolRequestError struct{…}

ErrorCode WebSearchToolRequestErrorErrorCode

Accepts one of the following:

const WebSearchToolRequestErrorErrorCodeInvalidToolInput WebSearchToolRequestErrorErrorCode = "invalid_tool_input"

const WebSearchToolRequestErrorErrorCodeUnavailable WebSearchToolRequestErrorErrorCode = "unavailable"

const WebSearchToolRequestErrorErrorCodeMaxUsesExceeded WebSearchToolRequestErrorErrorCode = "max_uses_exceeded"

const WebSearchToolRequestErrorErrorCodeTooManyRequests WebSearchToolRequestErrorErrorCode = "too_many_requests"

const WebSearchToolRequestErrorErrorCodeQueryTooLong WebSearchToolRequestErrorErrorCode = "query_too_long"

const WebSearchToolRequestErrorErrorCodeRequestTooLarge WebSearchToolRequestErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

type WebSearchToolResultBlockContentUnion interface{…}

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

EncryptedContent string

PageAge string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

type WebSearchToolResultBlockParamResp struct{…}

Content [WebSearchToolResultBlockParamContentUnionResp](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

PageAge stringoptional

type WebSearchToolRequestError struct{…}

ErrorCode WebSearchToolRequestErrorErrorCode

Accepts one of the following:

const WebSearchToolRequestErrorErrorCodeInvalidToolInput WebSearchToolRequestErrorErrorCode = "invalid_tool_input"

const WebSearchToolRequestErrorErrorCodeUnavailable WebSearchToolRequestErrorErrorCode = "unavailable"

const WebSearchToolRequestErrorErrorCodeMaxUsesExceeded WebSearchToolRequestErrorErrorCode = "max_uses_exceeded"

const WebSearchToolRequestErrorErrorCodeTooManyRequests WebSearchToolRequestErrorErrorCode = "too_many_requests"

const WebSearchToolRequestErrorErrorCodeQueryTooLong WebSearchToolRequestErrorErrorCode = "query_too_long"

const WebSearchToolRequestErrorErrorCodeRequestTooLarge WebSearchToolRequestErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web_search_tool_result"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL CacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type WebSearchToolResultBlockParamContentUnionResp interface{…}

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

PageAge stringoptional

type WebSearchToolRequestError struct{…}

ErrorCode WebSearchToolRequestErrorErrorCode

Accepts one of the following:

const WebSearchToolRequestErrorErrorCodeInvalidToolInput WebSearchToolRequestErrorErrorCode = "invalid_tool_input"

const WebSearchToolRequestErrorErrorCodeUnavailable WebSearchToolRequestErrorErrorCode = "unavailable"

const WebSearchToolRequestErrorErrorCodeMaxUsesExceeded WebSearchToolRequestErrorErrorCode = "max_uses_exceeded"

const WebSearchToolRequestErrorErrorCodeTooManyRequests WebSearchToolRequestErrorErrorCode = "too_many_requests"

const WebSearchToolRequestErrorErrorCodeQueryTooLong WebSearchToolRequestErrorErrorCode = "query_too_long"

const WebSearchToolRequestErrorErrorCodeRequestTooLarge WebSearchToolRequestErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

client.Messages.Batches.New(ctx, body) (\*[MessageBatch](/docs/en/api/messages#message_batch), error)

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

client.Messages.Batches.Get(ctx, messageBatchID) (\*[MessageBatch](/docs/en/api/messages#message_batch), error)

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

client.Messages.Batches.List(ctx, query) (\*Page\[[MessageBatch](/docs/en/api/messages#message_batch)\], error)

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

client.Messages.Batches.Cancel(ctx, messageBatchID) (\*[MessageBatch](/docs/en/api/messages#message_batch), error)

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

client.Messages.Batches.Delete(ctx, messageBatchID) (\*[DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch), error)

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

client.Messages.Batches.Results(ctx, messageBatchID) (\*[MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response), error)

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

type DeletedMessageBatch struct{…}

ID string

ID of the Message Batch.

Type MessageBatchDeleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

const MessageBatchDeletedMessageBatchDeleted MessageBatchDeleted = "message_batch_deleted"

type MessageBatch struct{…}

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

Accepts one of the following:

const MessageBatchMessageBatch MessageBatch = "message_batch"

type MessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](/docs/en/api/$shared#error_response)

Error [ErrorObjectUnion](/docs/en/api/$shared#error_object)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid_request_error"

type AuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication_error"

type BillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing_error"

type PermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission_error"

type NotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not_found_error"

type RateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate_limit_error"

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout_error"

type APIErrorObject struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api_error"

type OverloadedError struct{…}

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

type MessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

Accepts one of the following:

const MessageMessage Message = "message"

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

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

Accepts one of the following:

const SucceededSucceeded Succeeded = "succeeded"

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](/docs/en/api/$shared#error_response)

Error [ErrorObjectUnion](/docs/en/api/$shared#error_object)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid_request_error"

type AuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication_error"

type BillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing_error"

type PermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission_error"

type NotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not_found_error"

type RateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate_limit_error"

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout_error"

type APIErrorObject struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api_error"

type OverloadedError struct{…}

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

type MessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type MessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

Accepts one of the following:

const MessageMessage Message = "message"

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

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

Type Succeeded

Accepts one of the following:

const SucceededSucceeded Succeeded = "succeeded"

type MessageBatchErroredResult struct{…}

Error [ErrorResponse](/docs/en/api/$shared#error_response)

Error [ErrorObjectUnion](/docs/en/api/$shared#error_object)

Accepts one of the following:

type InvalidRequestError struct{…}

Message string

Type InvalidRequestError

Accepts one of the following:

const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid_request_error"

type AuthenticationError struct{…}

Message string

Type AuthenticationError

Accepts one of the following:

const AuthenticationErrorAuthenticationError AuthenticationError = "authentication_error"

type BillingError struct{…}

Message string

Type BillingError

Accepts one of the following:

const BillingErrorBillingError BillingError = "billing_error"

type PermissionError struct{…}

Message string

Type PermissionError

Accepts one of the following:

const PermissionErrorPermissionError PermissionError = "permission_error"

type NotFoundError struct{…}

Message string

Type NotFoundError

Accepts one of the following:

const NotFoundErrorNotFoundError NotFoundError = "not_found_error"

type RateLimitError struct{…}

Message string

Type RateLimitError

Accepts one of the following:

const RateLimitErrorRateLimitError RateLimitError = "rate_limit_error"

type GatewayTimeoutError struct{…}

Message string

Type TimeoutError

Accepts one of the following:

const TimeoutErrorTimeoutError TimeoutError = "timeout_error"

type APIErrorObject struct{…}

Message string

Type APIError

Accepts one of the following:

const APIErrorAPIError APIError = "api_error"

type OverloadedError struct{…}

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

type MessageBatchCanceledResult struct{…}

Type Canceled

Accepts one of the following:

const CanceledCanceled Canceled = "canceled"

type MessageBatchExpiredResult struct{…}

Type Expired

Accepts one of the following:

const ExpiredExpired Expired = "expired"

type MessageBatchSucceededResult struct{…}

Message [Message](/docs/en/api/messages#message)

ID string

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type CitationPageLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

FileID string

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type CitationContentBlockLocation struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

FileID string

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type CitationsWebSearchResultLocation struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type CitationsSearchResultLocation struct{…}

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

type ThinkingBlock struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type RedactedThinkingBlock struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type ToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

type ServerToolUseBlock struct{…}

ID string

Input map\[string, any\]

Name WebSearch

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

type WebSearchToolResultBlock struct{…}

Content [WebSearchToolResultBlockContentUnion](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

type WebSearchToolResultError struct{…}

ErrorCode WebSearchToolResultErrorErrorCode

Accepts one of the following:

const WebSearchToolResultErrorErrorCodeInvalidToolInput WebSearchToolResultErrorErrorCode = "invalid_tool_input"

const WebSearchToolResultErrorErrorCodeUnavailable WebSearchToolResultErrorErrorCode = "unavailable"

const WebSearchToolResultErrorErrorCodeMaxUsesExceeded WebSearchToolResultErrorErrorCode = "max_uses_exceeded"

const WebSearchToolResultErrorErrorCodeTooManyRequests WebSearchToolResultErrorErrorCode = "too_many_requests"

const WebSearchToolResultErrorErrorCodeQueryTooLong WebSearchToolResultErrorErrorCode = "query_too_long"

const WebSearchToolResultErrorErrorCodeRequestTooLarge WebSearchToolResultErrorErrorCode = "request_too_large"

Type WebSearchToolResultError

Accepts one of the following:

const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"

type WebSearchToolResultBlockContentArray \[\][WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)

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

Accepts one of the following:

const MessageMessage Message = "message"

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

OutputTokens int64

The number of output tokens which were used.

minimum0

ServerToolUse [ServerToolUsage](/docs/en/api/messages#server_tool_usage)

The number of server tool requests.

WebSearchRequests int64

The number of web search tool requests.

minimum0

ServiceTier UsageServiceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

const UsageServiceTierStandard UsageServiceTier = "standard"

const UsageServiceTierPriority UsageServiceTier = "priority"

const UsageServiceTierBatch UsageServiceTier = "batch"

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
