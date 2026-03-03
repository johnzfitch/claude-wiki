---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:01:33Z"
source_url: "https://platform.claude.com/docs/en/api/java/beta/messages/create"
title: "Create a Message - Claude API Reference"
---

# Create a Message

[BetaMessage](/docs/en/api/beta#beta_message) beta().messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse 

MessageCreateParams params

Optional\<List\<AnthropicBeta\>\> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")

PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")

COMPUTER_USE_2024_10_22("computer-use-2024-10-22")

COMPUTER_USE_2025_01_24("computer-use-2025-01-24")

PDFS_2024_09_25("pdfs-2024-09-25")

TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")

TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")

OUTPUT_128K_2025_02_19("output-128k-2025-02-19")

FILES_API_2025_04_14("files-api-2025-04-14")

MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")

MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")

DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")

INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")

CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")

EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")

CONTEXT_1M_2025_08_07("context-1m-2025-08-07")

CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")

MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")

SKILLS_2025_10_02("skills-2025-10-02")

FAST_MODE_2026_02_01("fast-mode-2026-02-01")

long maxTokens

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

List\<[BetaMessageParam](/docs/en/api/beta#beta_message_param)\> messages

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

List\<[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

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

JsonValue; type "base64"constant

"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant

"file"constant

JsonValue; type "image"constant

"image"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

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

JsonValue; type "base64"constant

"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant

"file"constant

JsonValue; type "image"constant

"image"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaUrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant

"file"constant

JsonValue; type "document"constant

"document"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant

"tool_result"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaTextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

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

JsonValue; type "base64"constant

"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant

"file"constant

JsonValue; type "image"constant

"image"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

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

JsonValue; type "base64"constant

"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant

"file"constant

JsonValue; type "image"constant

"image"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaUrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant

"file"constant

JsonValue; type "document"constant

"document"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class BetaWebSearchToolResultBlockParam:

[BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

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

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) content

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant

"text/plain"constant

JsonValue; type "text"constant

"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

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

JsonValue; type "base64"constant

"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant

"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant

"file"constant

JsonValue; type "image"constant

"image"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaUrlPdfSource:

JsonValue; type "url"constant

"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant

"file"constant

JsonValue; type "document"constant

"document"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class BetaCodeExecutionToolResultBlockParam:

[BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlockParam:

List\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> content

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlockParam:

List\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> content

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

Optional\<String\> errorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

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

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlockParam:

List\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant

"mcp_tool_use"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp_tool_result"constant

"mcp_tool_result"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

Optional\<Boolean\> isError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

Optional\<String\> content

Summary of previously compacted content, or null if compaction failed

JsonValue; type "compaction"constant

"compaction"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

Optional\<Container\> container

Container identifier for reuse across requests.

class BetaContainerParams:

Container parameters with skills to be loaded.

Optional\<String\> id

Container id

Optional\<List\<[BetaSkillParams](/docs/en/api/beta#beta_skill_params)\>\> skills

List of skills to load in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional\<String\> version

Skill version or 'latest' for most recent version

String

Optional\<[BetaContextManagementConfig](/docs/en/api/beta#beta_context_management_config)\> contextManagement

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

Optional\<String\> inferenceGeo

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

Optional\<List\<[BetaRequestMcpServerUrlDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition)\>\> mcpServers

MCP servers to be utilized in this request

String name

JsonValue; type "url"constant

"url"constant

String url

Optional\<String\> authorizationToken

Optional\<[BetaRequestMcpServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration)\> toolConfiguration

Optional\<List\<String\>\> allowedTools

Optional\<Boolean\> enabled

Optional\<[BetaMetadata](/docs/en/api/beta#beta_metadata)\> metadata

An object describing metadata about the request.

Optional\<[BetaOutputConfig](/docs/en/api/beta#beta_output_config)\> outputConfig

Configuration options for the model's output, such as the output format.

DeprecatedOptional\<[BetaJsonOutputFormat](/docs/en/api/beta#beta_json_output_format)\> outputFormat

Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

Optional\<ServiceTier\> serviceTier

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

AUTO("auto")

STANDARD_ONLY("standard_only")

Optional\<Speed\> speed

The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

STANDARD("standard")

FAST("fast")

Optional\<List\<String\>\> stopSequences

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

Optional\<System\> system

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

String

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

String text

JsonValue; type "text"constant

"text"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant

"search_result_location"constant

Optional\<Double\> temperature

Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

Optional\<[BetaThinkingConfigParam](/docs/en/api/beta#beta_thinking_config_param)\> thinking

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Optional\<[BetaToolChoice](/docs/en/api/beta#beta_tool_choice)\> toolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Optional\<List\<[BetaToolUnion](/docs/en/api/beta#beta_tool_union)\>\> tools

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

class BetaTool:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaToolBash20241022:

JsonValue; name "bash"constant

"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash_20241022"constant

"bash_20241022"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaToolBash20250124:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaCodeExecutionTool20250522:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaCodeExecutionTool20250825:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaCodeExecutionTool20260120:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant

"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer_20241022"constant

"computer_20241022"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant

"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer_20250124"constant

"computer_20250124"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022:

JsonValue; name "str_replace_editor"constant

"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text_editor_20241022"constant

"text_editor_20241022"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant

"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer_20251124"constant

"computer_20251124"constant

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

CODE_EXECUTION_20260120("code_execution_20260120")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional\<Boolean\> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaToolTextEditor20250429:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaToolTextEditor20250728:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaWebSearchTool20250305:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaUserLocation](/docs/en/api/beta#beta_user_location)\> userLocation

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

class BetaWebFetchTool20250910:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

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

class BetaWebSearchTool20260209:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaUserLocation](/docs/en/api/beta#beta_user_location)\> userLocation

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

class BetaWebFetchTool20260209:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

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

class BetaToolSearchToolBm25_20251119:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaToolSearchToolRegex20251119:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

String mcpServerName

Name of the MCP server to configure tools for

JsonValue; type "mcp_toolset"constant

"mcp_toolset"constant

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Configs\> configs

Configuration overrides for specific tools, keyed by tool name

Optional\<Boolean\> deferLoading

Optional\<Boolean\> enabled

Optional\<[BetaMcpToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config)\> defaultConfig

Default configuration applied to all tools from this server

Optional\<Boolean\> deferLoading

Optional\<Boolean\> enabled

Optional\<Long\> topK

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

Optional\<Double\> topP

Use nucleus sampling.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

maximum1

minimum0

##### ReturnsExpand Collapse 

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

Optional\<List\<[BetaSkill](/docs/en/api/beta#beta_skill)\>\> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

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

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocation:

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

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](/docs/en/api/beta#beta_document_block) content

Optional\<[BetaCitationConfig](/docs/en/api/beta#beta_citation_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class BetaPlainTextSource:

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

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

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

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

List\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> content

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

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

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

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

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

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

List\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant

"mcp_tool_use"constant

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

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocation:

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

boolean isError

String toolUseId

JsonValue; type "mcp_tool_result"constant

"mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Optional\<String\> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant

"compaction"constant

Optional\<[BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)\> contextManagement

Context management response.

Information about context management strategies applied during the request.

List\<AppliedEdit\> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear_tool_uses_20250919"constant

"clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear_thinking_20251015"constant

"clear_thinking_20251015"constant

The type of context management edit applied.

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

JsonValue; type "message"constant

"message"constant

Object type.

For Messages, this is always `"message"`.

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

Optional\<List\<BetaIterationsUsageItems\>\> iterations

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

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant

"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant

"compaction"constant

Usage for a compaction iteration

long outputTokens

The number of output tokens which were used.

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

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

Optional\<Speed\> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

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

Optional\<List\<[BetaSkill](/docs/en/api/beta#beta_skill)\>\> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

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

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocation:

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

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](/docs/en/api/beta#beta_document_block) content

Optional\<[BetaCitationConfig](/docs/en/api/beta#beta_citation_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class BetaPlainTextSource:

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

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

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

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

List\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> content

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

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

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

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

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

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

List\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant

"mcp_tool_use"constant

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

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocation:

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

boolean isError

String toolUseId

JsonValue; type "mcp_tool_result"constant

"mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Optional\<String\> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant

"compaction"constant

Optional\<[BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)\> contextManagement

Context management response.

Information about context management strategies applied during the request.

List\<AppliedEdit\> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear_tool_uses_20250919"constant

"clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear_thinking_20251015"constant

"clear_thinking_20251015"constant

The type of context management edit applied.

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

JsonValue; type "message"constant

"message"constant

Object type.

For Messages, this is always `"message"`.

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

Optional\<List\<BetaIterationsUsageItems\>\> iterations

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

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant

"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant

"compaction"constant

Usage for a compaction iteration

long outputTokens

The number of output tokens which were used.

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

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

Optional\<Speed\> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "message_start"constant

"message_start"constant

class BetaRawMessageDeltaEvent:

Optional\<[BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response)\> contextManagement

Information about context management strategies applied during the request

List\<AppliedEdit\> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear_tool_uses_20250919"constant

"clear_tool_uses_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear_thinking_20251015"constant

"clear_thinking_20251015"constant

The type of context management edit applied.

Delta delta

Optional\<[BetaContainer](/docs/en/api/beta#beta_container)\> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional\<List\<[BetaSkill](/docs/en/api/beta#beta_skill)\>\> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

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

JsonValue; type "message_delta"constant

"message_delta"constant

[BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage) usage

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

Optional\<List\<BetaIterationsUsageItems\>\> iterations

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

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant

"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional\<[BetaCacheCreation](/docs/en/api/beta#beta_cache_creation)\> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant

"compaction"constant

Usage for a compaction iteration

long outputTokens

The cumulative number of output tokens which were used.

Optional\<[BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage)\> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class BetaRawMessageStopEvent:

JsonValue; type "message_stop"constant

"message_stop"constant

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

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocation:

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

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant

"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted_thinking"constant

"redacted_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool_use"constant

"tool_use"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "server_tool_use"constant

"server_tool_use"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "web_search_tool_result_error"constant

"web_search_tool_result_error"constant

List\<[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\>

String encryptedContent

Optional\<String\> pageAge

String title

JsonValue; type "web_search_result"constant

"web_search_result"constant

String url

String toolUseId

JsonValue; type "web_search_tool_result"constant

"web_search_tool_result"constant

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

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

JsonValue; type "web_fetch_tool_result_error"constant

"web_fetch_tool_result_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](/docs/en/api/beta#beta_document_block) content

Optional\<[BetaCitationConfig](/docs/en/api/beta#beta_citation_config)\> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant

"application/pdf"constant

JsonValue; type "base64"constant

"base64"constant

class BetaPlainTextSource:

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

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant

"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant

"code_execution_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code_execution_20260120"constant

"code_execution_20260120"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content) content

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant

"code_execution_tool_result_error"constant

class BetaCodeExecutionResultBlock:

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

String fileId

JsonValue; type "code_execution_output"constant

"code_execution_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant

"code_execution_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web_search results.

List\<[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\> content

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

JsonValue; type "bash_code_execution_tool_result_error"constant

"bash_code_execution_tool_result_error"constant

class BetaBashCodeExecutionResultBlock:

List\<[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\> content

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

JsonValue; type "text_editor_code_execution_tool_result_error"constant

"text_editor_code_execution_tool_result_error"constant

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

JsonValue; type "text_editor_code_execution_view_result"constant

"text_editor_code_execution_view_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant

"text_editor_code_execution_create_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

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

JsonValue; type "tool_search_tool_result_error"constant

"tool_search_tool_result_error"constant

class BetaToolSearchToolSearchResultBlock:

List\<[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant

"tool_reference"constant

JsonValue; type "tool_search_tool_search_result"constant

"tool_search_tool_search_result"constant

String toolUseId

JsonValue; type "tool_search_tool_result"constant

"tool_search_tool_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant

"mcp_tool_use"constant

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

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocation:

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

boolean isError

String toolUseId

JsonValue; type "mcp_tool_result"constant

"mcp_tool_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container_upload"constant

"container_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

Optional\<String\> content

Summary of compacted content, or null if compaction failed

JsonValue; type "compaction"constant

"compaction"constant

long index

JsonValue; type "content_block_start"constant

"content_block_start"constant

class BetaRawContentBlockDeltaEvent:

[BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta) delta

Accepts one of the following:

class BetaTextDelta:

String text

JsonValue; type "text_delta"constant

"text_delta"constant

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input_json_delta"constant

"input_json_delta"constant

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

JsonValue; type "char_location"constant

"char_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

Optional\<String\> fileId

long startPageNumber

JsonValue; type "page_location"constant

"page_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

Optional\<String\> fileId

long startBlockIndex

JsonValue; type "content_block_location"constant

"content_block_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant

"web_search_result_location"constant

String url

class BetaCitationSearchResultLocation:

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

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking_delta"constant

"thinking_delta"constant

class BetaSignatureDelta:

String signature

JsonValue; type "signature_delta"constant

"signature_delta"constant

class BetaCompactionContentBlockDelta:

Optional\<String\> content

JsonValue; type "compaction_delta"constant

"compaction_delta"constant

long index

JsonValue; type "content_block_delta"constant

"content_block_delta"constant

class BetaRawContentBlockStopEvent:

long index

JsonValue; type "content_block_stop"constant

"content_block_stop"constant

Create a Message

Java

``` shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .maxTokens(1024L)
            .addUserMessage("Hello, world")
            .model(Model.CLAUDE_OPUS_4_6)
            .build();
        BetaMessage betaMessage = client.beta().messages().create(params);
    }
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
    "service_tier": "standard",
    "speed": "standard"
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
