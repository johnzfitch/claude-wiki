---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:09:59Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/messages/create"
title: "Create a Message - Claude API Reference"
---

Copy page

Go

# Create a Message

client.Beta.Messages.New(ctx, params) (\*[BetaMessage](/docs/en/api/beta#beta_message), error)

post/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse 

params BetaMessageNewParams

MaxTokens param.Field\[int64\]

Body param: The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

Messages param.Field\[\[\][BetaMessageParamResp](/docs/en/api/beta#beta_message_param)\]

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

Content \[\][BetaContentBlockParamUnionResp](/docs/en/api/beta#beta_content_block_param)

Accepts one of the following:

\[\][BetaContentBlockParamUnionResp](/docs/en/api/beta#beta_content_block_param)

Accepts one of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

Accepts one of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

Accepts one of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaURLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Accepts one of the following:

const FileFile File = "file"

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaRequestDocumentBlock struct{…}

Source BetaRequestDocumentBlockSourceUnion

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

type BetaContentBlockSource struct{…}

Content BetaContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][BetaContentBlockSourceContentUnion](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

Accepts one of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

Accepts one of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaURLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Accepts one of the following:

const FileFile File = "file"

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type BetaURLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type BetaFileDocumentSource struct{…}

FileID string

Type File

Accepts one of the following:

const FileFile File = "file"

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](/docs/en/api/beta#beta_citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

type BetaSearchResultBlockParamResp struct{…}

Content \[\][BetaTextBlockParamResp](/docs/en/api/beta#beta_text_block_param)

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](/docs/en/api/beta#beta_citations_config_param)optional

Enabled booloptional

type BetaThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

Accepts one of the following:

const ThinkingThinking Thinking = "thinking"

type BetaRedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

Accepts one of the following:

const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"

type BetaToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

Accepts one of the following:

const ToolUseToolUse ToolUse = "tool_use"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Caller BetaToolUseBlockParamCallerUnionRespoptional

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

type BetaToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult

Accepts one of the following:

const ToolResultToolResult ToolResult = "tool_result"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Content \[\]BetaToolResultBlockParamContentUnionRespoptional

Accepts one of the following:

\[\]BetaToolResultBlockParamContentUnionResp

Accepts one of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

Accepts one of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

Accepts one of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaURLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Accepts one of the following:

const FileFile File = "file"

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaSearchResultBlockParamResp struct{…}

Content \[\][BetaTextBlockParamResp](/docs/en/api/beta#beta_text_block_param)

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

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

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](/docs/en/api/beta#beta_citations_config_param)optional

Enabled booloptional

type BetaRequestDocumentBlock struct{…}

Source BetaRequestDocumentBlockSourceUnion

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

type BetaContentBlockSource struct{…}

Content BetaContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][BetaContentBlockSourceContentUnion](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

Accepts one of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

Accepts one of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaURLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Accepts one of the following:

const FileFile File = "file"

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type BetaURLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type BetaFileDocumentSource struct{…}

FileID string

Type File

Accepts one of the following:

const FileFile File = "file"

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](/docs/en/api/beta#beta_citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

type BetaToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool_result content.

ToolName string

Type ToolReference

Accepts one of the following:

const ToolReferenceToolReference ToolReference = "tool_reference"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

IsError booloptional

type BetaServerToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name BetaServerToolUseBlockParamName

Accepts one of the following:

const BetaServerToolUseBlockParamNameWebSearch BetaServerToolUseBlockParamName = "web_search"

const BetaServerToolUseBlockParamNameWebFetch BetaServerToolUseBlockParamName = "web_fetch"

const BetaServerToolUseBlockParamNameCodeExecution BetaServerToolUseBlockParamName = "code_execution"

const BetaServerToolUseBlockParamNameBashCodeExecution BetaServerToolUseBlockParamName = "bash_code_execution"

const BetaServerToolUseBlockParamNameTextEditorCodeExecution BetaServerToolUseBlockParamName = "text_editor_code_execution"

const BetaServerToolUseBlockParamNameToolSearchToolRegex BetaServerToolUseBlockParamName = "tool_search_tool_regex"

const BetaServerToolUseBlockParamNameToolSearchToolBm25 BetaServerToolUseBlockParamName = "tool_search_tool_bm25"

Type ServerToolUse

Accepts one of the following:

const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Caller BetaServerToolUseBlockParamCallerUnionRespoptional

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

type BetaWebSearchToolResultBlockParamResp struct{…}

Content [BetaWebSearchToolResultBlockParamContentUnionResp](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

\[\][BetaWebSearchResultBlockParamResp](/docs/en/api/beta#beta_web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

Accepts one of the following:

const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"

URL string

PageAge stringoptional

type BetaWebSearchToolRequestError struct{…}

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

ToolUseID string

Type WebSearchToolResult

Accepts one of the following:

const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web_search_tool_result"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaWebFetchToolResultBlockParamResp struct{…}

Content BetaWebFetchToolResultBlockParamContentUnionResp

Accepts one of the following:

type BetaWebFetchToolResultErrorBlockParamResp struct{…}

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

type BetaWebFetchBlockParamResp struct{…}

Content [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block)

Source BetaRequestDocumentBlockSourceUnion

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

type BetaContentBlockSource struct{…}

Content BetaContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][BetaContentBlockSourceContentUnion](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

type BetaTextBlockParamResp struct{…}

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

type BetaImageBlockParamResp struct{…}

Source BetaImageBlockParamSourceUnionResp

Accepts one of the following:

type BetaBase64ImageSource struct{…}

Data string

MediaType BetaBase64ImageSourceMediaType

Accepts one of the following:

const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"

const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"

const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"

const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"

Type Base64

Accepts one of the following:

const Base64Base64 Base64 = "base64"

type BetaURLImageSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type BetaFileImageSource struct{…}

FileID string

Type File

Accepts one of the following:

const FileFile File = "file"

Type Image

Accepts one of the following:

const ImageImage Image = "image"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type Content

Accepts one of the following:

const ContentContent Content = "content"

type BetaURLPDFSource struct{…}

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

type BetaFileDocumentSource struct{…}

FileID string

Type File

Accepts one of the following:

const FileFile File = "file"

Type Document

Accepts one of the following:

const DocumentDocument Document = "document"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](/docs/en/api/beta#beta_citations_config_param)optional

Enabled booloptional

Context stringoptional

Title stringoptional

Type WebFetchResult

Accepts one of the following:

const WebFetchResultWebFetchResult WebFetchResult = "web_fetch_result"

URL string

Fetched content URL

RetrievedAt stringoptional

ISO 8601 timestamp when the content was retrieved

ToolUseID string

Type WebFetchToolResult

Accepts one of the following:

const WebFetchToolResultWebFetchToolResult WebFetchToolResult = "web_fetch_tool_result"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaCodeExecutionToolResultBlockParamResp struct{…}

Content [BetaCodeExecutionToolResultBlockParamContentUnionResp](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

type BetaCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

const BetaCodeExecutionToolResultErrorCodeInvalidToolInput [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "invalid_tool_input"

const BetaCodeExecutionToolResultErrorCodeUnavailable [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "unavailable"

const BetaCodeExecutionToolResultErrorCodeTooManyRequests [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "too_many_requests"

const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

Accepts one of the following:

const CodeExecutionToolResultErrorCodeExecutionToolResultError CodeExecutionToolResultError = "code_execution_tool_result_error"

type BetaCodeExecutionResultBlockParamResp struct{…}

Content \[\][BetaCodeExecutionOutputBlockParamResp](/docs/en/api/beta#beta_code_execution_output_block_param)

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

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaBashCodeExecutionToolResultBlockParamResp struct{…}

Content BetaBashCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type BetaBashCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode BetaBashCodeExecutionToolResultErrorParamErrorCode

Accepts one of the following:

const BetaBashCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorParamErrorCode = "invalid_tool_input"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorParamErrorCode = "too_many_requests"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorParamErrorCode = "execution_time_exceeded"

const BetaBashCodeExecutionToolResultErrorParamErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorParamErrorCode = "output_file_too_large"

Type BashCodeExecutionToolResultError

Accepts one of the following:

const BashCodeExecutionToolResultErrorBashCodeExecutionToolResultError BashCodeExecutionToolResultError = "bash_code_execution_tool_result_error"

type BetaBashCodeExecutionResultBlockParamResp struct{…}

Content \[\][BetaBashCodeExecutionOutputBlockParamResp](/docs/en/api/beta#beta_bash_code_execution_output_block_param)

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

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaTextEditorCodeExecutionToolResultBlockParamResp struct{…}

Content BetaTextEditorCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type BetaTextEditorCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode BetaTextEditorCodeExecutionToolResultErrorParamErrorCode

Accepts one of the following:

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "invalid_tool_input"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "unavailable"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "too_many_requests"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "execution_time_exceeded"

const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "file_not_found"

Type TextEditorCodeExecutionToolResultError

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorTextEditorCodeExecutionToolResultError TextEditorCodeExecutionToolResultError = "text_editor_code_execution_tool_result_error"

ErrorMessage stringoptional

type BetaTextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string

FileType BetaTextEditorCodeExecutionViewResultBlockParamFileType

Accepts one of the following:

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeText BetaTextEditorCodeExecutionViewResultBlockParamFileType = "text"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeImage BetaTextEditorCodeExecutionViewResultBlockParamFileType = "image"

const BetaTextEditorCodeExecutionViewResultBlockParamFileTypePDF BetaTextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

Accepts one of the following:

const TextEditorCodeExecutionViewResultTextEditorCodeExecutionViewResult TextEditorCodeExecutionViewResult = "text_editor_code_execution_view_result"

NumLines int64optional

StartLine int64optional

TotalLines int64optional

type BetaTextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

Accepts one of the following:

const TextEditorCodeExecutionCreateResultTextEditorCodeExecutionCreateResult TextEditorCodeExecutionCreateResult = "text_editor_code_execution_create_result"

type BetaTextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Accepts one of the following:

const TextEditorCodeExecutionStrReplaceResultTextEditorCodeExecutionStrReplaceResult TextEditorCodeExecutionStrReplaceResult = "text_editor_code_execution_str_replace_result"

Lines \[\]stringoptional

NewLines int64optional

NewStart int64optional

OldLines int64optional

OldStart int64optional

ToolUseID string

Type TextEditorCodeExecutionToolResult

Accepts one of the following:

const TextEditorCodeExecutionToolResultTextEditorCodeExecutionToolResult TextEditorCodeExecutionToolResult = "text_editor_code_execution_tool_result"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaToolSearchToolResultBlockParamResp struct{…}

Content BetaToolSearchToolResultBlockParamContentUnionResp

Accepts one of the following:

type BetaToolSearchToolResultErrorParamResp struct{…}

ErrorCode BetaToolSearchToolResultErrorParamErrorCode

Accepts one of the following:

const BetaToolSearchToolResultErrorParamErrorCodeInvalidToolInput BetaToolSearchToolResultErrorParamErrorCode = "invalid_tool_input"

const BetaToolSearchToolResultErrorParamErrorCodeUnavailable BetaToolSearchToolResultErrorParamErrorCode = "unavailable"

const BetaToolSearchToolResultErrorParamErrorCodeTooManyRequests BetaToolSearchToolResultErrorParamErrorCode = "too_many_requests"

const BetaToolSearchToolResultErrorParamErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorParamErrorCode = "execution_time_exceeded"

Type ToolSearchToolResultError

Accepts one of the following:

const ToolSearchToolResultErrorToolSearchToolResultError ToolSearchToolResultError = "tool_search_tool_result_error"

type BetaToolSearchToolSearchResultBlockParamResp struct{…}

ToolReferences \[\][BetaToolReferenceBlockParamResp](/docs/en/api/beta#beta_tool_reference_block_param)

ToolName string

Type ToolReference

Accepts one of the following:

const ToolReferenceToolReference ToolReference = "tool_reference"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

Accepts one of the following:

const ToolSearchToolSearchResultToolSearchToolSearchResult ToolSearchToolSearchResult = "tool_search_tool_search_result"

ToolUseID string

Type ToolSearchToolResult

Accepts one of the following:

const ToolSearchToolResultToolSearchToolResult ToolSearchToolResult = "tool_search_tool_result"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaMCPToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

ServerName string

The name of the MCP server

Type MCPToolUse

Accepts one of the following:

const MCPToolUseMCPToolUse MCPToolUse = "mcp_tool_use"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaRequestMCPToolResultBlockParamResp struct{…}

ToolUseID string

Type MCPToolResult

Accepts one of the following:

const MCPToolResultMCPToolResult MCPToolResult = "mcp_tool_result"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Content BetaRequestMCPToolResultBlockParamContentUnionRespoptional

Accepts one of the following:

string

\[\][BetaTextBlockParamResp](/docs/en/api/beta#beta_text_block_param)

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

IsError booloptional

type BetaContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload

Accepts one of the following:

const ContainerUploadContainerUpload ContainerUpload = "container_upload"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

type BetaCompactionBlockParamResp struct{…}

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

Content string

Summary of previously compacted content, or null if compaction failed

Type Compaction

Accepts one of the following:

const CompactionCompaction Compaction = "compaction"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Role BetaMessageParamRole

Accepts one of the following:

const BetaMessageParamRoleUser BetaMessageParamRole = "user"

const BetaMessageParamRoleAssistant BetaMessageParamRole = "assistant"

Model param.Field\[Model\]

Body param: The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Container param.Field\[[BetaMessageNewParamsContainerUnion](/docs/en/api/beta/messages/create)\]optional

Body param: Container identifier for reuse across requests.

type BetaContainerParamsResp struct{…}

Container parameters with skills to be loaded.

ID stringoptional

Container id

Skills \[\][BetaSkillParamsResp](/docs/en/api/beta#beta_skill_params)optional

List of skills to load in the container

SkillID string

Skill ID

maxLength64

minLength1

Type BetaSkillParamsType

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

const BetaSkillParamsTypeAnthropic BetaSkillParamsType = "anthropic"

const BetaSkillParamsTypeCustom BetaSkillParamsType = "custom"

Version stringoptional

Skill version or 'latest' for most recent version

maxLength64

minLength1

string

ContextManagement param.Field\[[BetaContextManagementConfig](/docs/en/api/beta#beta_context_management_config)\]optional

Body param: Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

InferenceGeo param.Field\[string\]optional

Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

MCPServers param.Field\[\[\][BetaRequestMCPServerURLDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition)\]optional

Body param: MCP servers to be utilized in this request

Name string

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

AuthorizationToken stringoptional

ToolConfiguration [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration)optional

AllowedTools \[\]stringoptional

Enabled booloptional

Metadata param.Field\[[BetaMetadata](/docs/en/api/beta#beta_metadata)\]optional

Body param: An object describing metadata about the request.

OutputConfig param.Field\[[BetaOutputConfig](/docs/en/api/beta#beta_output_config)\]optional

Body param: Configuration options for the model's output, such as the output format.

DeprecatedOutputFormat param.Field\[[BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format)\]optional

Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

ServiceTier param.Field\[[BetaMessageNewParamsServiceTier](/docs/en/api/beta/messages/create)\]optional

Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

const BetaMessageNewParamsServiceTierAuto [BetaMessageNewParamsServiceTier](/docs/en/api/beta/messages/create) = "auto"

const BetaMessageNewParamsServiceTierStandardOnly [BetaMessageNewParamsServiceTier](/docs/en/api/beta/messages/create) = "standard_only"

StopSequences param.Field\[\[\]string\]optional

Body param: Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

System param.Field\[\[\][BetaTextBlockParamResp](/docs/en/api/beta#beta_text_block_param)\]optional

Body param: System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

\[\][BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)

Text string

Type Text

Accepts one of the following:

const TextText Text = "text"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations \[\][BetaTextCitationParamUnionResp](/docs/en/api/beta#beta_text_citation_param)optional

Accepts one of the following:

type BetaCitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

Accepts one of the following:

const CharLocationCharLocation CharLocation = "char_location"

type BetaCitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

Accepts one of the following:

const PageLocationPageLocation PageLocation = "page_location"

type BetaCitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

Accepts one of the following:

const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"

type BetaCitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

Accepts one of the following:

const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"

URL string

type BetaCitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Accepts one of the following:

const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"

Temperature param.Field\[float64\]optional

Body param: Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

Thinking param.Field\[[BetaThinkingConfigParamUnionResp](/docs/en/api/beta#beta_thinking_config_param)\]optional

Body param: Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

ToolChoice param.Field\[[BetaToolChoiceUnion](/docs/en/api/beta#beta_tool_choice)\]optional

Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Tools param.Field\[\[\][BetaToolUnion](/docs/en/api/beta#beta_tool_union)\]optional

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

type BetaTool struct{…}

InputSchema BetaToolInputSchema

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

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolAllowedCallerDirect BetaToolAllowedCaller = "direct"

const BetaToolAllowedCallerCodeExecution20250825 BetaToolAllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Description stringoptional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming booloptional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

Type BetaToolTypeoptional

Accepts one of the following:

const BetaToolTypeCustom BetaToolType = "custom"

type BetaToolBash20241022 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const BashBash Bash = "bash"

Type Bash20241022

Accepts one of the following:

const Bash20241022Bash20241022 Bash20241022 = "bash_20241022"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolBash20241022AllowedCallerDirect BetaToolBash20241022AllowedCaller = "direct"

const BetaToolBash20241022AllowedCallerCodeExecution20250825 BetaToolBash20241022AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const BashBash Bash = "bash"

Type Bash20250124

Accepts one of the following:

const Bash20250124Bash20250124 Bash20250124 = "bash_20250124"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolBash20250124AllowedCallerDirect BetaToolBash20250124AllowedCaller = "direct"

const BetaToolBash20250124AllowedCallerCodeExecution20250825 BetaToolBash20250124AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaCodeExecutionTool20250522 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const CodeExecutionCodeExecution CodeExecution = "code_execution"

Type CodeExecution20250522

Accepts one of the following:

const CodeExecution20250522CodeExecution20250522 CodeExecution20250522 = "code_execution_20250522"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaCodeExecutionTool20250522AllowedCallerDirect BetaCodeExecutionTool20250522AllowedCaller = "direct"

const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250522AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaCodeExecutionTool20250825 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const CodeExecutionCodeExecution CodeExecution = "code_execution"

Type CodeExecution20250825

Accepts one of the following:

const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaCodeExecutionTool20250825AllowedCallerDirect BetaCodeExecutionTool20250825AllowedCaller = "direct"

const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250825AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolComputerUse20241022 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

minimum1

DisplayWidthPx int64

The width of the display in pixels.

minimum1

Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const ComputerComputer Computer = "computer"

Type Computer20241022

Accepts one of the following:

const Computer20241022Computer20241022 Computer20241022 = "computer_20241022"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolComputerUse20241022AllowedCallerDirect BetaToolComputerUse20241022AllowedCaller = "direct"

const BetaToolComputerUse20241022AllowedCallerCodeExecution20250825 BetaToolComputerUse20241022AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

DisplayNumber int64optional

The X11 display number (e.g. 0, 1) for the display.

minimum0

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaMemoryTool20250818 struct{…}

Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const MemoryMemory Memory = "memory"

Type Memory20250818

Accepts one of the following:

const Memory20250818Memory20250818 Memory20250818 = "memory_20250818"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaMemoryTool20250818AllowedCallerDirect BetaMemoryTool20250818AllowedCaller = "direct"

const BetaMemoryTool20250818AllowedCallerCodeExecution20250825 BetaMemoryTool20250818AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolComputerUse20250124 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

minimum1

DisplayWidthPx int64

The width of the display in pixels.

minimum1

Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const ComputerComputer Computer = "computer"

Type Computer20250124

Accepts one of the following:

const Computer20250124Computer20250124 Computer20250124 = "computer_20250124"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolComputerUse20250124AllowedCallerDirect BetaToolComputerUse20250124AllowedCaller = "direct"

const BetaToolComputerUse20250124AllowedCallerCodeExecution20250825 BetaToolComputerUse20250124AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

DisplayNumber int64optional

The X11 display number (e.g. 0, 1) for the display.

minimum0

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolTextEditor20241022 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceEditorStrReplaceEditor StrReplaceEditor = "str_replace_editor"

Type TextEditor20241022

Accepts one of the following:

const TextEditor20241022TextEditor20241022 TextEditor20241022 = "text_editor_20241022"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolTextEditor20241022AllowedCallerDirect BetaToolTextEditor20241022AllowedCaller = "direct"

const BetaToolTextEditor20241022AllowedCallerCodeExecution20250825 BetaToolTextEditor20241022AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolComputerUse20251124 struct{…}

DisplayHeightPx int64

The height of the display in pixels.

minimum1

DisplayWidthPx int64

The width of the display in pixels.

minimum1

Name Computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const ComputerComputer Computer = "computer"

Type Computer20251124

Accepts one of the following:

const Computer20251124Computer20251124 Computer20251124 = "computer_20251124"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolComputerUse20251124AllowedCallerDirect BetaToolComputerUse20251124AllowedCaller = "direct"

const BetaToolComputerUse20251124AllowedCallerCodeExecution20250825 BetaToolComputerUse20251124AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

DisplayNumber int64optional

The X11 display number (e.g. 0, 1) for the display.

minimum0

EnableZoom booloptional

Whether to enable an action to take a zoomed-in screenshot of the screen.

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceEditorStrReplaceEditor StrReplaceEditor = "str_replace_editor"

Type TextEditor20250124

Accepts one of the following:

const TextEditor20250124TextEditor20250124 TextEditor20250124 = "text_editor_20250124"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolTextEditor20250124AllowedCallerDirect BetaToolTextEditor20250124AllowedCaller = "direct"

const BetaToolTextEditor20250124AllowedCallerCodeExecution20250825 BetaToolTextEditor20250124AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"

Type TextEditor20250429

Accepts one of the following:

const TextEditor20250429TextEditor20250429 TextEditor20250429 = "text_editor_20250429"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolTextEditor20250429AllowedCallerDirect BetaToolTextEditor20250429AllowedCaller = "direct"

const BetaToolTextEditor20250429AllowedCallerCodeExecution20250825 BetaToolTextEditor20250429AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]optional

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"

Type TextEditor20250728

Accepts one of the following:

const TextEditor20250728TextEditor20250728 TextEditor20250728 = "text_editor_20250728"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolTextEditor20250728AllowedCallerDirect BetaToolTextEditor20250728AllowedCaller = "direct"

const BetaToolTextEditor20250728AllowedCallerCodeExecution20250825 BetaToolTextEditor20250728AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]optional

MaxCharacters int64optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaWebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const WebSearchWebSearch WebSearch = "web_search"

Type WebSearch20250305

Accepts one of the following:

const WebSearch20250305WebSearch20250305 WebSearch20250305 = "web_search_20250305"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaWebSearchTool20250305AllowedCallerDirect BetaWebSearchTool20250305AllowedCaller = "direct"

const BetaWebSearchTool20250305AllowedCallerCodeExecution20250825 BetaWebSearchTool20250305AllowedCaller = "code_execution_20250825"

AllowedDomains \[\]stringoptional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]stringoptional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Strict booloptional

When true, guarantees schema validation on tool names and inputs

UserLocation BetaWebSearchTool20250305UserLocationoptional

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

type BetaWebFetchTool20250910 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const WebFetchWebFetch WebFetch = "web_fetch"

Type WebFetch20250910

Accepts one of the following:

const WebFetch20250910WebFetch20250910 WebFetch20250910 = "web_fetch_20250910"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaWebFetchTool20250910AllowedCallerDirect BetaWebFetchTool20250910AllowedCaller = "direct"

const BetaWebFetchTool20250910AllowedCallerCodeExecution20250825 BetaWebFetchTool20250910AllowedCaller = "code_execution_20250825"

AllowedDomains \[\]stringoptional

List of domains to allow fetching from

BlockedDomains \[\]stringoptional

List of domains to block fetching from

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Citations [BetaCitationsConfigParamResp](/docs/en/api/beta#beta_citations_config_param)optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled booloptional

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

MaxUses int64optional

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolSearchToolBm25_20251119 struct{…}

Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const ToolSearchToolBm25ToolSearchToolBm25 ToolSearchToolBm25 = "tool_search_tool_bm25"

Type BetaToolSearchToolBm25_20251119Type

Accepts one of the following:

const BetaToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 BetaToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"

const BetaToolSearchToolBm25_20251119TypeToolSearchToolBm25 BetaToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolSearchToolBm25_20251119AllowedCallerDirect BetaToolSearchToolBm25_20251119AllowedCaller = "direct"

const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaToolSearchToolRegex20251119 struct{…}

Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

const ToolSearchToolRegexToolSearchToolRegex ToolSearchToolRegex = "tool_search_tool_regex"

Type BetaToolSearchToolRegex20251119Type

Accepts one of the following:

const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 BetaToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"

const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex BetaToolSearchToolRegex20251119Type = "tool_search_tool_regex"

AllowedCallers \[\]stringoptional

Accepts one of the following:

const BetaToolSearchToolRegex20251119AllowedCallerDirect BetaToolSearchToolRegex20251119AllowedCaller = "direct"

const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

DeferLoading booloptional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict booloptional

When true, guarantees schema validation on tool names and inputs

type BetaMCPToolset struct{…}

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

MCPServerName string

Name of the MCP server to configure tools for

maxLength255

minLength1

Type MCPToolset

Accepts one of the following:

const MCPToolsetMCPToolset MCPToolset = "mcp_toolset"

CacheControl [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)optional

Create a cache control breakpoint at this content block.

Type Ephemeral

Accepts one of the following:

const EphemeralEphemeral Ephemeral = "ephemeral"

TTL BetaCacheControlEphemeralTTLoptional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"

const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"

Configs map\[string, [BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config)\]optional

Configuration overrides for specific tools, keyed by tool name

DeferLoading booloptional

Enabled booloptional

DefaultConfig [BetaMCPToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config)optional

Default configuration applied to all tools from this server

DeferLoading booloptional

Enabled booloptional

TopK param.Field\[int64\]optional

Body param: Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

TopP param.Field\[float64\]optional

Body param: Use nucleus sampling.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

maximum1

minimum0

Betas param.Field\[\[\]AnthropicBeta\]optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"

##### ReturnsExpand Collapse 

type BetaMessage struct{…}

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

Create a Message

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
  betaMessage, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
    MaxTokens: 1024,
    Messages: []anthropic.BetaMessageParam{anthropic.BetaMessageParam{
      Content: []anthropic.BetaContentBlockParamUnion{anthropic.BetaContentBlockParamUnion{
        OfText: &anthropic.BetaTextBlockParam{
          Text: "x",
        },
      }},
      Role: anthropic.BetaMessageParamRoleUser,
    }},
    Model: anthropic.ModelClaudeOpus4_6,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaMessage.ID)
}
```

Response 200

``` shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "x",
        "type": "anthropic",
        "version": "x"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard"
  }
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "x",
        "type": "anthropic",
        "version": "x"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard"
  }
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
