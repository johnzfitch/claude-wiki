---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:09:37Z"
source_url: "https://platform.claude.com/docs/en/api/go/messages/count_tokens"
title: "Count tokens in a Message - Claude API Reference"
---

Copy page

Go

# Count tokens in a Message

client.Messages.CountTokens(ctx, body) (\*[MessageTokensCount](/docs/en/api/messages#message_tokens_count), error)

post/v1/messages/count_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse 

body MessageCountTokensParams

Messages param.Field\[\[\][MessageParamResp](/docs/en/api/messages#message_param)\]

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

Model param.Field\[Model\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

OutputConfig param.Field\[[OutputConfig](/docs/en/api/messages#output_config)\]optional

Configuration options for the model's output, such as the output format.

System param.Field\[[MessageCountTokensParamsSystemUnion](/docs/en/api/messages/count_tokens)\]optional

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

string

type MessageCountTokensParamsSystemArray \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

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

Thinking param.Field\[[ThinkingConfigParamUnionResp](/docs/en/api/messages#thinking_config_param)\]optional

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

ToolChoice param.Field\[[ToolChoiceUnion](/docs/en/api/messages#tool_choice)\]optional

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Tools param.Field\[\[\][MessageCountTokensToolUnion](/docs/en/api/messages#message_count_tokens_tool)\]optional

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

##### ReturnsExpand Collapse 

type MessageTokensCount struct{…}

InputTokens int64

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

Go

``` shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  messageTokensCount, err := client.Messages.CountTokens(context.TODO(), anthropic.MessageCountTokensParams{
    Messages: []anthropic.MessageParam{anthropic.MessageParam{
      Content: []anthropic.ContentBlockParamUnion{anthropic.ContentBlockParamUnion{
        OfText: &anthropic.TextBlockParam{
          Text: "x",
        },
      }},
      Role: anthropic.MessageParamRoleUser,
    }},
    Model: anthropic.ModelClaudeOpus4_6,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", messageTokensCount.InputTokens)
}
```

Response 200

``` shiki
{
  "input_tokens": 2095
}
```

##### Returns Examples

Response 200

``` shiki
{
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
