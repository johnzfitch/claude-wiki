---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:55:09Z"
source_url: "https://platform.claude.com/docs/en/api/go/messages/count_tokens"
title: "Count tokens in a Message - Claude API Reference"
---

Copy page

Go

# Count tokens in a Message

client.Messages.CountTokens(ctx, body) (\*[MessageTokensCount](/docs/en/api/messages#message_tokens_count), error)

POST/v1/messages/count_tokens

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

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

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

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

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

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

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

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

type SearchResultBlockParamResp struct{…}

Content \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

type ThinkingBlockParamResp struct{…}

Signature string

Thinking string

Type Thinking

type RedactedThinkingBlockParamResp struct{…}

Data string

Type RedactedThinking

type ToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name string

Type ToolUse

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ToolUseBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type ToolResultBlockParamResp struct{…}

ToolUseID string

Type ToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Content \[\]ToolResultBlockParamContentUnionResp

optional

Accepts one of the following:

\[\]ToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

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

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

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

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Source string

Title string

Type SearchResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

type DocumentBlockParamResp struct{…}

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

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

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

type ToolReferenceBlockParamResp struct{…}

Tool reference block that can be included in tool_result content.

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

IsError bool

optional

type ServerToolUseBlockParamResp struct{…}

ID string

Input map\[string, any\]

Name ServerToolUseBlockParamName

Accepts one of the following:

const ServerToolUseBlockParamNameWebSearch ServerToolUseBlockParamName = "web_search"

const ServerToolUseBlockParamNameWebFetch ServerToolUseBlockParamName = "web_fetch"

const ServerToolUseBlockParamNameCodeExecution ServerToolUseBlockParamName = "code_execution"

const ServerToolUseBlockParamNameBashCodeExecution ServerToolUseBlockParamName = "bash_code_execution"

const ServerToolUseBlockParamNameTextEditorCodeExecution ServerToolUseBlockParamName = "text_editor_code_execution"

const ServerToolUseBlockParamNameToolSearchToolRegex ServerToolUseBlockParamName = "tool_search_tool_regex"

const ServerToolUseBlockParamNameToolSearchToolBm25 ServerToolUseBlockParamName = "tool_search_tool_bm25"

Type ServerToolUse

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller ServerToolUseBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebSearchToolResultBlockParamResp struct{…}

Content [WebSearchToolResultBlockParamContentUnionResp](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

\[\][WebSearchResultBlockParamResp](/docs/en/api/messages#web_search_result_block_param)

EncryptedContent string

Title string

Type WebSearchResult

URL string

PageAge string

optional

type WebSearchToolRequestError struct{…}

ErrorCode [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

const WebSearchToolResultErrorCodeInvalidToolInput [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "invalid_tool_input"

const WebSearchToolResultErrorCodeUnavailable [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "unavailable"

const WebSearchToolResultErrorCodeMaxUsesExceeded [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "max_uses_exceeded"

const WebSearchToolResultErrorCodeTooManyRequests [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "too_many_requests"

const WebSearchToolResultErrorCodeQueryTooLong [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "query_too_long"

const WebSearchToolResultErrorCodeRequestTooLarge [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code) = "request_too_large"

Type WebSearchToolResultError

ToolUseID string

Type WebSearchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebSearchToolResultBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type WebFetchToolResultBlockParamResp struct{…}

Content WebFetchToolResultBlockParamContentUnionResp

Accepts one of the following:

type WebFetchToolResultErrorBlockParamResp struct{…}

ErrorCode [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

const WebFetchToolResultErrorCodeInvalidToolInput [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "invalid_tool_input"

const WebFetchToolResultErrorCodeURLTooLong [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_too_long"

const WebFetchToolResultErrorCodeURLNotAllowed [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_allowed"

const WebFetchToolResultErrorCodeURLNotAccessible [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "url_not_accessible"

const WebFetchToolResultErrorCodeUnsupportedContentType [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unsupported_content_type"

const WebFetchToolResultErrorCodeTooManyRequests [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "too_many_requests"

const WebFetchToolResultErrorCodeMaxUsesExceeded [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "max_uses_exceeded"

const WebFetchToolResultErrorCodeUnavailable [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code) = "unavailable"

Type WebFetchToolResultError

type WebFetchBlockParamResp struct{…}

Content [DocumentBlockParamResp](/docs/en/api/messages#document_block_param)

Source DocumentBlockParamSourceUnionResp

Accepts one of the following:

type Base64PDFSource struct{…}

Data string

MediaType ApplicationPDF

Type Base64

type PlainTextSource struct{…}

Data string

MediaType TextPlain

Type Text

type ContentBlockSource struct{…}

Content ContentBlockSourceContentUnion

Accepts one of the following:

string

\[\][ContentBlockSourceContentItemUnion](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

type TextBlockParamResp struct{…}

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

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

type URLImageSource struct{…}

Type URL

URL string

Type Image

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type Content

type URLPDFSource struct{…}

Type URL

URL string

Type Document

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Enabled bool

optional

Context string

optional

Title string

optional

Type WebFetchResult

URL string

Fetched content URL

RetrievedAt string

optional

ISO 8601 timestamp when the content was retrieved

ToolUseID string

Type WebFetchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Caller WebFetchToolResultBlockParamCallerUnionResp

optional

Tool invocation directly from the model.

Accepts one of the following:

type DirectCaller struct{…}

Tool invocation directly from the model.

Type Direct

type ServerToolCaller struct{…}

Tool invocation generated by a server-side tool.

ToolID string

Type CodeExecution20250825

type ServerToolCaller20260120 struct{…}

ToolID string

Type CodeExecution20260120

type CodeExecutionToolResultBlockParamResp struct{…}

Content [CodeExecutionToolResultBlockParamContentUnionResp](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

type CodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

const CodeExecutionToolResultErrorCodeInvalidToolInput [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "invalid_tool_input"

const CodeExecutionToolResultErrorCodeUnavailable [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "unavailable"

const CodeExecutionToolResultErrorCodeTooManyRequests [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "too_many_requests"

const CodeExecutionToolResultErrorCodeExecutionTimeExceeded [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code) = "execution_time_exceeded"

Type CodeExecutionToolResultError

type CodeExecutionResultBlockParamResp struct{…}

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type CodeExecutionResult

type EncryptedCodeExecutionResultBlockParamResp struct{…}

Code execution result with encrypted stdout for PFC + web_search results.

Content \[\][CodeExecutionOutputBlockParamResp](/docs/en/api/messages#code_execution_output_block_param)

FileID string

Type CodeExecutionOutput

EncryptedStdout string

ReturnCode int64

Stderr string

Type EncryptedCodeExecutionResult

ToolUseID string

Type CodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type BashCodeExecutionToolResultBlockParamResp struct{…}

Content BashCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type BashCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

const BashCodeExecutionToolResultErrorCodeInvalidToolInput [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "invalid_tool_input"

const BashCodeExecutionToolResultErrorCodeUnavailable [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "unavailable"

const BashCodeExecutionToolResultErrorCodeTooManyRequests [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "too_many_requests"

const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "execution_time_exceeded"

const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code) = "output_file_too_large"

Type BashCodeExecutionToolResultError

type BashCodeExecutionResultBlockParamResp struct{…}

Content \[\][BashCodeExecutionOutputBlockParamResp](/docs/en/api/messages#bash_code_execution_output_block_param)

FileID string

Type BashCodeExecutionOutput

ReturnCode int64

Stderr string

Stdout string

Type BashCodeExecutionResult

ToolUseID string

Type BashCodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type TextEditorCodeExecutionToolResultBlockParamResp struct{…}

Content TextEditorCodeExecutionToolResultBlockParamContentUnionResp

Accepts one of the following:

type TextEditorCodeExecutionToolResultErrorParamResp struct{…}

ErrorCode [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "invalid_tool_input"

const TextEditorCodeExecutionToolResultErrorCodeUnavailable [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "unavailable"

const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "too_many_requests"

const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "execution_time_exceeded"

const TextEditorCodeExecutionToolResultErrorCodeFileNotFound [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code) = "file_not_found"

Type TextEditorCodeExecutionToolResultError

ErrorMessage string

optional

type TextEditorCodeExecutionViewResultBlockParamResp struct{…}

Content string

FileType TextEditorCodeExecutionViewResultBlockParamFileType

Accepts one of the following:

const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"

const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"

const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"

Type TextEditorCodeExecutionViewResult

NumLines int64

optional

StartLine int64

optional

TotalLines int64

optional

type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}

IsFileUpdate bool

Type TextEditorCodeExecutionCreateResult

type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}

Type TextEditorCodeExecutionStrReplaceResult

Lines \[\]string

optional

NewLines int64

optional

NewStart int64

optional

OldLines int64

optional

OldStart int64

optional

ToolUseID string

Type TextEditorCodeExecutionToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ToolSearchToolResultBlockParamResp struct{…}

Content ToolSearchToolResultBlockParamContentUnionResp

Accepts one of the following:

type ToolSearchToolResultErrorParamResp struct{…}

ErrorCode [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

const ToolSearchToolResultErrorCodeInvalidToolInput [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "invalid_tool_input"

const ToolSearchToolResultErrorCodeUnavailable [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "unavailable"

const ToolSearchToolResultErrorCodeTooManyRequests [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "too_many_requests"

const ToolSearchToolResultErrorCodeExecutionTimeExceeded [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code) = "execution_time_exceeded"

Type ToolSearchToolResultError

type ToolSearchToolSearchResultBlockParamResp struct{…}

ToolReferences \[\][ToolReferenceBlockParamResp](/docs/en/api/messages#tool_reference_block_param)

ToolName string

Type ToolReference

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Type ToolSearchToolSearchResult

ToolUseID string

Type ToolSearchToolResult

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

type ContainerUploadBlockParamResp struct{…}

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

FileID string

Type ContainerUpload

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

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

CacheControl param.Field\[[CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)\]

optional

Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

OutputConfig param.Field\[[OutputConfig](/docs/en/api/messages#output_config)\]

optional

Configuration options for the model's output, such as the output format.

System param.Field\[[MessageCountTokensParamsSystemUnion](/docs/en/api/messages/count_tokens)\]

optional

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

string

type MessageCountTokensParamsSystemArray \[\][TextBlockParamResp](/docs/en/api/messages#text_block_param)

Text string

Type Text

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations \[\][TextCitationParamUnionResp](/docs/en/api/messages#text_citation_param)

optional

Accepts one of the following:

type CitationCharLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndCharIndex int64

StartCharIndex int64

Type CharLocation

type CitationPageLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndPageNumber int64

StartPageNumber int64

Type PageLocation

type CitationContentBlockLocationParamResp struct{…}

CitedText string

DocumentIndex int64

DocumentTitle string

EndBlockIndex int64

StartBlockIndex int64

Type ContentBlockLocation

type CitationWebSearchResultLocationParamResp struct{…}

CitedText string

EncryptedIndex string

Title string

Type WebSearchResultLocation

URL string

type CitationSearchResultLocationParamResp struct{…}

CitedText string

EndBlockIndex int64

SearchResultIndex int64

Source string

StartBlockIndex int64

Title string

Type SearchResultLocation

Thinking param.Field\[[ThinkingConfigParamUnionResp](/docs/en/api/messages#thinking_config_param)\]

optional

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

ToolChoice param.Field\[[ToolChoiceUnion](/docs/en/api/messages#tool_choice)\]

optional

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Tools param.Field\[\[\][MessageCountTokensToolUnion](/docs/en/api/messages#message_count_tokens_tool)\]

optional

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

Properties map\[string, any\]

optional

Required \[\]string

optional

Name string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolAllowedCallerDirect ToolAllowedCaller = "direct"

const ToolAllowedCallerCodeExecution20250825 ToolAllowedCaller = "code_execution_20250825"

const ToolAllowedCallerCodeExecution20260120 ToolAllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Description string

optional

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

EagerInputStreaming bool

optional

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

Type ToolType

optional

type ToolBash20250124 struct{…}

Name Bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Bash20250124

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolBash20250124AllowedCallerDirect ToolBash20250124AllowedCaller = "direct"

const ToolBash20250124AllowedCallerCodeExecution20250825 ToolBash20250124AllowedCaller = "code_execution_20250825"

const ToolBash20250124AllowedCallerCodeExecution20260120 ToolBash20250124AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250522 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250522

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20250522AllowedCallerDirect CodeExecutionTool20250522AllowedCaller = "direct"

const CodeExecutionTool20250522AllowedCallerCodeExecution20250825 CodeExecutionTool20250522AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20250522AllowedCallerCodeExecution20260120 CodeExecutionTool20250522AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20250825 struct{…}

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20250825

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20250825AllowedCallerDirect CodeExecutionTool20250825AllowedCaller = "direct"

const CodeExecutionTool20250825AllowedCallerCodeExecution20250825 CodeExecutionTool20250825AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20250825AllowedCallerCodeExecution20260120 CodeExecutionTool20250825AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type CodeExecutionTool20260120 struct{…}

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Name CodeExecution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type CodeExecution20260120

AllowedCallers \[\]string

optional

Accepts one of the following:

const CodeExecutionTool20260120AllowedCallerDirect CodeExecutionTool20260120AllowedCaller = "direct"

const CodeExecutionTool20260120AllowedCallerCodeExecution20250825 CodeExecutionTool20260120AllowedCaller = "code_execution_20250825"

const CodeExecutionTool20260120AllowedCallerCodeExecution20260120 CodeExecutionTool20260120AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type MemoryTool20250818 struct{…}

Name Memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type Memory20250818

AllowedCallers \[\]string

optional

Accepts one of the following:

const MemoryTool20250818AllowedCallerDirect MemoryTool20250818AllowedCaller = "direct"

const MemoryTool20250818AllowedCallerCodeExecution20250825 MemoryTool20250818AllowedCaller = "code_execution_20250825"

const MemoryTool20250818AllowedCallerCodeExecution20260120 MemoryTool20250818AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250124 struct{…}

Name StrReplaceEditor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250124

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250124AllowedCallerDirect ToolTextEditor20250124AllowedCaller = "direct"

const ToolTextEditor20250124AllowedCallerCodeExecution20250825 ToolTextEditor20250124AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250124AllowedCallerCodeExecution20260120 ToolTextEditor20250124AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250429 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250429

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250429AllowedCallerDirect ToolTextEditor20250429AllowedCaller = "direct"

const ToolTextEditor20250429AllowedCallerCodeExecution20250825 ToolTextEditor20250429AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250429AllowedCallerCodeExecution20260120 ToolTextEditor20250429AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolTextEditor20250728 struct{…}

Name StrReplaceBasedEditTool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type TextEditor20250728

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolTextEditor20250728AllowedCallerDirect ToolTextEditor20250728AllowedCaller = "direct"

const ToolTextEditor20250728AllowedCallerCodeExecution20250825 ToolTextEditor20250728AllowedCaller = "code_execution_20250825"

const ToolTextEditor20250728AllowedCallerCodeExecution20260120 ToolTextEditor20250728AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

InputExamples \[\]map\[string, any\]

optional

MaxCharacters int64

optional

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20250305 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20250305

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebSearchTool20250305AllowedCallerDirect WebSearchTool20250305AllowedCaller = "direct"

const WebSearchTool20250305AllowedCallerCodeExecution20250825 WebSearchTool20250305AllowedCaller = "code_execution_20250825"

const WebSearchTool20250305AllowedCallerCodeExecution20260120 WebSearchTool20250305AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]string

optional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](/docs/en/api/messages#user_location)

optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchTool20250910 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20250910

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebFetchTool20250910AllowedCallerDirect WebFetchTool20250910AllowedCaller = "direct"

const WebFetchTool20250910AllowedCallerCodeExecution20250825 WebFetchTool20250910AllowedCaller = "code_execution_20250825"

const WebFetchTool20250910AllowedCallerCodeExecution20260120 WebFetchTool20250910AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

List of domains to allow fetching from

BlockedDomains \[\]string

optional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled bool

optional

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64

optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type WebSearchTool20260209 struct{…}

Name WebSearch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebSearch20260209

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebSearchTool20260209AllowedCallerDirect WebSearchTool20260209AllowedCaller = "direct"

const WebSearchTool20260209AllowedCallerCodeExecution20250825 WebSearchTool20260209AllowedCaller = "code_execution_20250825"

const WebSearchTool20260209AllowedCallerCodeExecution20260120 WebSearchTool20260209AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

BlockedDomains \[\]string

optional

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

UserLocation [UserLocation](/docs/en/api/messages#user_location)

optional

Parameters for the user's location. Used to provide more relevant search results.

Type Approximate

City string

optional

The city of the user.

Country string

optional

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Region string

optional

The region of the user.

Timezone string

optional

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

type WebFetchTool20260209 struct{…}

Name WebFetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type WebFetch20260209

AllowedCallers \[\]string

optional

Accepts one of the following:

const WebFetchTool20260209AllowedCallerDirect WebFetchTool20260209AllowedCaller = "direct"

const WebFetchTool20260209AllowedCallerCodeExecution20250825 WebFetchTool20260209AllowedCaller = "code_execution_20250825"

const WebFetchTool20260209AllowedCallerCodeExecution20260120 WebFetchTool20260209AllowedCaller = "code_execution_20260120"

AllowedDomains \[\]string

optional

List of domains to allow fetching from

BlockedDomains \[\]string

optional

List of domains to block fetching from

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

Citations [CitationsConfigParamResp](/docs/en/api/messages#citations_config_param)

optional

Citations configuration for fetched documents. Citations are disabled by default.

Enabled bool

optional

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

MaxContentTokens int64

optional

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

MaxUses int64

optional

Maximum number of times the tool can be used in the API request.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolBm25_20251119 struct{…}

Name ToolSearchToolBm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolBm25_20251119Type

Accepts one of the following:

const ToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"

const ToolSearchToolBm25_20251119TypeToolSearchToolBm25 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolSearchToolBm25_20251119AllowedCallerDirect ToolSearchToolBm25_20251119AllowedCaller = "direct"

const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"

const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

type ToolSearchToolRegex20251119 struct{…}

Name ToolSearchToolRegex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type ToolSearchToolRegex20251119Type

Accepts one of the following:

const ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 ToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"

const ToolSearchToolRegex20251119TypeToolSearchToolRegex ToolSearchToolRegex20251119Type = "tool_search_tool_regex"

AllowedCallers \[\]string

optional

Accepts one of the following:

const ToolSearchToolRegex20251119AllowedCallerDirect ToolSearchToolRegex20251119AllowedCaller = "direct"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"

const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"

CacheControl [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral)

optional

Create a cache control breakpoint at this content block.

Type Ephemeral

TTL CacheControlEphemeralTTL

optional

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"

const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"

DeferLoading bool

optional

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Strict bool

optional

When true, guarantees schema validation on tool names and inputs

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
