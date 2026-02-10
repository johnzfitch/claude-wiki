---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:10:04Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/messages/batches/create"
title: "Create a Message Batch - Claude API Reference"
---

Copy page

Go

# Create a Message Batch

client.Beta.Messages.Batches.New(ctx, params) (\*[BetaMessageBatch](/docs/en/api/beta#beta_message_batch), error)

post/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse 

params BetaMessageBatchNewParams

Requests param.Field\[\[\]BetaMessageBatchNewParamsRequest\]

Body param: List of requests for prompt completion. Each is an individual request to create a Message.

CustomID string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1

Params BetaMessageBatchNewParamsRequestParams

Messages API creation parameters for the individual request.

See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.

MaxTokens int64

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

Messages \[\][BetaMessageParamResp](/docs/en/api/beta#beta_message_param)

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

Container BetaMessageBatchNewParamsRequestParamsContainerUnionoptional

Container identifier for reuse across requests.

Accepts one of the following:

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

ContextManagement [BetaContextManagementConfig](/docs/en/api/beta#beta_context_management_config)optional

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

Edits \[\]BetaContextManagementConfigEditUnionoptional

List of context management edits to apply

Accepts one of the following:

type BetaClearToolUses20250919Edit struct{…}

Type ClearToolUses20250919

Accepts one of the following:

const ClearToolUses20250919ClearToolUses20250919 ClearToolUses20250919 = "clear_tool_uses_20250919"

ClearAtLeast [BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least)optional

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

Type InputTokens

Accepts one of the following:

const InputTokensInputTokens InputTokens = "input_tokens"

Value int64

ClearToolInputs BetaClearToolUses20250919EditClearToolInputsUnionoptional

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

bool

\[\]string

ExcludeTools \[\]stringoptional

Tool names whose uses are preserved from clearing

Keep [BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep)optional

Number of tool uses to retain in the conversation

Type ToolUses

Accepts one of the following:

const ToolUsesToolUses ToolUses = "tool_uses"

Value int64

Trigger BetaClearToolUses20250919EditTriggerUnionoptional

Condition that triggers the context management strategy

Accepts one of the following:

type BetaInputTokensTrigger struct{…}

Type InputTokens

Accepts one of the following:

const InputTokensInputTokens InputTokens = "input_tokens"

Value int64

type BetaToolUsesTrigger struct{…}

Type ToolUses

Accepts one of the following:

const ToolUsesToolUses ToolUses = "tool_uses"

Value int64

type BetaClearThinking20251015Edit struct{…}

Type ClearThinking20251015

Accepts one of the following:

const ClearThinking20251015ClearThinking20251015 ClearThinking20251015 = "clear_thinking_20251015"

Keep BetaClearThinking20251015EditKeepUnionoptional

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

type BetaThinkingTurns struct{…}

Type ThinkingTurns

Accepts one of the following:

const ThinkingTurnsThinkingTurns ThinkingTurns = "thinking_turns"

Value int64

type BetaAllThinkingTurns struct{…}

Type All

Accepts one of the following:

const AllAll All = "all"

All

Accepts one of the following:

const AllAll All = "all"

type BetaCompact20260112Edit struct{…}

Automatically compact older context when reaching the configured trigger threshold.

Type Compact20260112

Accepts one of the following:

const Compact20260112Compact20260112 Compact20260112 = "compact_20260112"

Instructions stringoptional

Additional instructions for summarization.

PauseAfterCompaction booloptional

Whether to pause after compaction and return the compaction block to the user.

Trigger [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger)optional

When to trigger compaction. Defaults to 150000 input tokens.

Type InputTokens

Accepts one of the following:

const InputTokensInputTokens InputTokens = "input_tokens"

Value int64

InferenceGeo stringoptional

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

MCPServers \[\][BetaRequestMCPServerURLDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition)optional

MCP servers to be utilized in this request

Name string

Type URL

Accepts one of the following:

const URLURL URL = "url"

URL string

AuthorizationToken stringoptional

ToolConfiguration [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration)optional

AllowedTools \[\]stringoptional

Enabled booloptional

Metadata [BetaMetadata](/docs/en/api/beta#beta_metadata)optional

An object describing metadata about the request.

UserID stringoptional

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

OutputConfig [BetaOutputConfig](/docs/en/api/beta#beta_output_config)optional

Configuration options for the model's output, such as the output format.

Effort BetaOutputConfigEffortoptional

All possible effort levels.

Accepts one of the following:

const BetaOutputConfigEffortLow BetaOutputConfigEffort = "low"

const BetaOutputConfigEffortMedium BetaOutputConfigEffort = "medium"

const BetaOutputConfigEffortHigh BetaOutputConfigEffort = "high"

const BetaOutputConfigEffortMax BetaOutputConfigEffort = "max"

Format [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format)optional

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

Schema map\[string, any\]

The JSON schema of the format

Type JSONSchema

Accepts one of the following:

const JSONSchemaJSONSchema JSONSchema = "json_schema"

DeprecatedOutputFormat [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format)optional

Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

Schema map\[string, any\]

The JSON schema of the format

Type JSONSchema

Accepts one of the following:

const JSONSchemaJSONSchema JSONSchema = "json_schema"

ServiceTier stringoptional

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

Accepts one of the following:

const BetaMessageBatchNewParamsRequestParamsServiceTierAuto BetaMessageBatchNewParamsRequestParamsServiceTier = "auto"

const BetaMessageBatchNewParamsRequestParamsServiceTierStandardOnly BetaMessageBatchNewParamsRequestParamsServiceTier = "standard_only"

StopSequences \[\]stringoptional

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

Stream booloptional

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

System \[\][BetaTextBlockParamResp](/docs/en/api/beta#beta_text_block_param)optional

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

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

Temperature float64optional

Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

Thinking [BetaThinkingConfigParamUnionResp](/docs/en/api/beta#beta_thinking_config_param)optional

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

type BetaThinkingConfigEnabled struct{…}

BudgetTokens int64

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

Type Enabled

Accepts one of the following:

const EnabledEnabled Enabled = "enabled"

type BetaThinkingConfigDisabled struct{…}

Type Disabled

Accepts one of the following:

const DisabledDisabled Disabled = "disabled"

type BetaThinkingConfigAdaptive struct{…}

Type Adaptive

Accepts one of the following:

const AdaptiveAdaptive Adaptive = "adaptive"

ToolChoice [BetaToolChoiceUnion](/docs/en/api/beta#beta_tool_choice)optional

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

type BetaToolChoiceAuto struct{…}

The model will automatically decide whether to use tools.

Type Auto

Accepts one of the following:

const AutoAuto Auto = "auto"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

type BetaToolChoiceAny struct{…}

The model will use any available tools.

Type Any

Accepts one of the following:

const AnyAny Any = "any"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type BetaToolChoiceTool struct{…}

The model will use the specified tool with `tool_choice.name`.

Name string

The name of the tool to use.

Type Tool

Accepts one of the following:

const ToolTool Tool = "tool"

DisableParallelToolUse booloptional

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

type BetaToolChoiceNone struct{…}

The model will not be allowed to use tools.

Type None

Accepts one of the following:

const NoneNone None = "none"

Tools \[\][BetaToolUnion](/docs/en/api/beta#beta_tool_union)optional

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

Accepts one of the following:

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

TopK int64optional

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

TopP float64optional

Use nucleus sampling.

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

type BetaMessageBatch struct{…}

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

ProcessingStatus BetaMessageBatchProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

const BetaMessageBatchProcessingStatusInProgress BetaMessageBatchProcessingStatus = "in_progress"

const BetaMessageBatchProcessingStatusCanceling BetaMessageBatchProcessingStatus = "canceling"

const BetaMessageBatchProcessingStatusEnded BetaMessageBatchProcessingStatus = "ended"

RequestCounts [BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts)

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

Create a Message Batch

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
  betaMessageBatch, err := client.Beta.Messages.Batches.New(context.TODO(), anthropic.BetaMessageBatchNewParams{
    Requests: []anthropic.BetaMessageBatchNewParamsRequest{anthropic.BetaMessageBatchNewParamsRequest{
      CustomID: "my-custom-id-1",
      Params: anthropic.BetaMessageBatchNewParamsRequestParams{
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
      },
    }},
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaMessageBatch.ID)
}
```

Response 200

``` shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
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
