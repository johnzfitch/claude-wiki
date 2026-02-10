---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:08:55Z"
source_url: "https://platform.claude.com/docs/en/api/java/beta/messages/batches/create"
title: "Create a Message Batch - Claude API Reference"
---

Copy page

Java

# Create a Message Batch

[BetaMessageBatch](/docs/en/api/beta#beta_message_batch) beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse 

BatchCreateParams params

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

List\<Request\> requests

List of requests for prompt completion. Each is an individual request to create a Message.

String customId

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1

Params params

Messages API creation parameters for the individual request.

See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.

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

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted_thinking"constant"redacted_thinking"constant

Accepts one of the following:

REDACTED_THINKING("redacted_thinking")

class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool_use"constant"tool_use"constant

Accepts one of the following:

TOOL_USE("tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool_result"constant"tool_result"constant

Accepts one of the following:

TOOL_RESULT("tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaSearchResultBlockParam:

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\> content

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

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

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool_result content.

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "server_tool_use"constant"server_tool_use"constant

Accepts one of the following:

SERVER_TOOL_USE("server_tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Caller\> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

class BetaWebSearchToolResultBlockParam:

[BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content) content

Accepts one of the following:

List\<[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\>

String encryptedContent

String title

JsonValue; type "web_search_result"constant"web_search_result"constant

Accepts one of the following:

WEB_SEARCH_RESULT("web_search_result")

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

JsonValue; type "web_search_tool_result_error"constant"web_search_tool_result_error"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")

String toolUseId

JsonValue; type "web_search_tool_result"constant"web_search_tool_result"constant

Accepts one of the following:

WEB_SEARCH_TOOL_RESULT("web_search_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "web_fetch_tool_result_error"constant"web_fetch_tool_result_error"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) content

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION_PDF("application/pdf")

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT_PLAIN("text/plain")

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List\<[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

JsonValue; type "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

Accepts one of the following:

FILE("file")

JsonValue; type "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Optional\<Boolean\> enabled

Optional\<String\> context

Optional\<String\> title

JsonValue; type "web_fetch_result"constant"web_fetch_result"constant

Accepts one of the following:

WEB_FETCH_RESULT("web_fetch_result")

String url

Fetched content URL

Optional\<String\> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web_fetch_tool_result"constant"web_fetch_tool_result"constant

Accepts one of the following:

WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaCodeExecutionToolResultBlockParam:

[BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content) content

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code) errorCode

Accepts one of the following:

INVALID_TOOL_INPUT("invalid_tool_input")

UNAVAILABLE("unavailable")

TOO_MANY_REQUESTS("too_many_requests")

EXECUTION_TIME_EXCEEDED("execution_time_exceeded")

JsonValue; type "code_execution_tool_result_error"constant"code_execution_tool_result_error"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")

class BetaCodeExecutionResultBlockParam:

List\<[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\> content

String fileId

JsonValue; type "code_execution_output"constant"code_execution_output"constant

Accepts one of the following:

CODE_EXECUTION_OUTPUT("code_execution_output")

long returnCode

String stderr

String stdout

JsonValue; type "code_execution_result"constant"code_execution_result"constant

Accepts one of the following:

CODE_EXECUTION_RESULT("code_execution_result")

String toolUseId

JsonValue; type "code_execution_tool_result"constant"code_execution_tool_result"constant

Accepts one of the following:

CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "bash_code_execution_tool_result_error"constant"bash_code_execution_tool_result_error"constant

Accepts one of the following:

BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")

class BetaBashCodeExecutionResultBlockParam:

List\<[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\> content

String fileId

JsonValue; type "bash_code_execution_output"constant"bash_code_execution_output"constant

Accepts one of the following:

BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")

long returnCode

String stderr

String stdout

JsonValue; type "bash_code_execution_result"constant"bash_code_execution_result"constant

Accepts one of the following:

BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")

String toolUseId

JsonValue; type "bash_code_execution_tool_result"constant"bash_code_execution_tool_result"constant

Accepts one of the following:

BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "text_editor_code_execution_tool_result_error"constant"text_editor_code_execution_tool_result_error"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")

Optional\<String\> errorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text_editor_code_execution_view_result"constant"text_editor_code_execution_view_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")

Optional\<Long\> numLines

Optional\<Long\> startLine

Optional\<Long\> totalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text_editor_code_execution_create_result"constant"text_editor_code_execution_create_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text_editor_code_execution_str_replace_result"constant"text_editor_code_execution_str_replace_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")

Optional\<List\<String\>\> lines

Optional\<Long\> newLines

Optional\<Long\> newStart

Optional\<Long\> oldLines

Optional\<Long\> oldStart

String toolUseId

JsonValue; type "text_editor_code_execution_tool_result"constant"text_editor_code_execution_tool_result"constant

Accepts one of the following:

TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "tool_search_tool_result_error"constant"tool_search_tool_result_error"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")

class BetaToolSearchToolSearchResultBlockParam:

List\<[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\> toolReferences

String toolName

JsonValue; type "tool_reference"constant"tool_reference"constant

Accepts one of the following:

TOOL_REFERENCE("tool_reference")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

JsonValue; type "tool_search_tool_search_result"constant"tool_search_tool_search_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")

String toolUseId

JsonValue; type "tool_search_tool_result"constant"tool_search_tool_result"constant

Accepts one of the following:

TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp_tool_use"constant"mcp_tool_use"constant

Accepts one of the following:

MCP_TOOL_USE("mcp_tool_use")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp_tool_result"constant"mcp_tool_result"constant

Accepts one of the following:

MCP_TOOL_RESULT("mcp_tool_result")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

Optional\<Boolean\> isError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container_upload"constant"container_upload"constant

Accepts one of the following:

CONTAINER_UPLOAD("container_upload")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

Optional\<String\> content

Summary of previously compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Accepts one of the following:

COMPACTION("compaction")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Container\> container

Container identifier for reuse across requests.

Accepts one of the following:

class BetaContainerParams:

Container parameters with skills to be loaded.

Optional\<String\> id

Container id

Optional\<List\<[BetaSkillParams](/docs/en/api/beta#beta_skill_params)\>\> skills

List of skills to load in the container

String skillId

Skill ID

maxLength64

minLength1

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional\<String\> version

Skill version or 'latest' for most recent version

maxLength64

minLength1

String

Optional\<[BetaContextManagementConfig](/docs/en/api/beta#beta_context_management_config)\> contextManagement

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

Optional\<List\<Edit\>\> edits

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit:

JsonValue; type "clear_tool_uses_20250919"constant"clear_tool_uses_20250919"constant

Accepts one of the following:

CLEAR_TOOL_USES_20250919("clear_tool_uses_20250919")

Optional\<[BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least)\> clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

Optional\<ClearToolInputs\> clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

boolean

List\<String\>

Optional\<List\<String\>\> excludeTools

Tool names whose uses are preserved from clearing

Optional\<[BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep)\> keep

Number of tool uses to retain in the conversation

JsonValue; type "tool_uses"constant"tool_uses"constant

Accepts one of the following:

TOOL_USES("tool_uses")

long value

Optional\<Trigger\> trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

class BetaToolUsesTrigger:

JsonValue; type "tool_uses"constant"tool_uses"constant

Accepts one of the following:

TOOL_USES("tool_uses")

long value

class BetaClearThinking20251015Edit:

JsonValue; type "clear_thinking_20251015"constant"clear_thinking_20251015"constant

Accepts one of the following:

CLEAR_THINKING_20251015("clear_thinking_20251015")

Optional\<Keep\> keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonValue; type "thinking_turns"constant"thinking_turns"constant

Accepts one of the following:

THINKING_TURNS("thinking_turns")

long value

class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

Accepts one of the following:

ALL("all")

JsonValue;

Accepts one of the following:

ALL("all")

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonValue; type "compact_20260112"constant"compact_20260112"constant

Accepts one of the following:

COMPACT_20260112("compact_20260112")

Optional\<String\> instructions

Additional instructions for summarization.

Optional\<Boolean\> pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

Optional\<[BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger)\> trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonValue; type "input_tokens"constant"input_tokens"constant

Accepts one of the following:

INPUT_TOKENS("input_tokens")

long value

Optional\<String\> inferenceGeo

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

Optional\<List\<[BetaRequestMcpServerUrlDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition)\>\> mcpServers

MCP servers to be utilized in this request

String name

JsonValue; type "url"constant"url"constant

Accepts one of the following:

URL("url")

String url

Optional\<String\> authorizationToken

Optional\<[BetaRequestMcpServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration)\> toolConfiguration

Optional\<List\<String\>\> allowedTools

Optional\<Boolean\> enabled

Optional\<[BetaMetadata](/docs/en/api/beta#beta_metadata)\> metadata

An object describing metadata about the request.

Optional\<String\> userId

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

Optional\<[BetaOutputConfig](/docs/en/api/beta#beta_output_config)\> outputConfig

Configuration options for the model's output, such as the output format.

Optional\<Effort\> effort

All possible effort levels.

Accepts one of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

MAX("max")

Optional\<[BetaJsonOutputFormat](/docs/en/api/beta#beta_json_output_format)\> format

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

Schema schema

The JSON schema of the format

JsonValue; type "json_schema"constant"json_schema"constant

Accepts one of the following:

JSON_SCHEMA("json_schema")

DeprecatedOptional\<[BetaJsonOutputFormat](/docs/en/api/beta#beta_json_output_format)\> outputFormat

Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

Schema schema

The JSON schema of the format

JsonValue; type "json_schema"constant"json_schema"constant

Accepts one of the following:

JSON_SCHEMA("json_schema")

Optional\<ServiceTier\> serviceTier

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

Accepts one of the following:

AUTO("auto")

STANDARD_ONLY("standard_only")

Optional\<List\<String\>\> stopSequences

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

Optional\<Boolean\> stream

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

Optional\<System\> system

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

String

List\<[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\>

String text

JsonValue; type "text"constant"text"constant

Accepts one of the following:

TEXT("text")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<List\<[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\>\> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char_location"constant"char_location"constant

Accepts one of the following:

CHAR_LOCATION("char_location")

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page_location"constant"page_location"constant

Accepts one of the following:

PAGE_LOCATION("page_location")

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional\<String\> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content_block_location"constant"content_block_location"constant

Accepts one of the following:

CONTENT_BLOCK_LOCATION("content_block_location")

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional\<String\> title

JsonValue; type "web_search_result_location"constant"web_search_result_location"constant

Accepts one of the following:

WEB_SEARCH_RESULT_LOCATION("web_search_result_location")

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional\<String\> title

JsonValue; type "search_result_location"constant"search_result_location"constant

Accepts one of the following:

SEARCH_RESULT_LOCATION("search_result_location")

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

Accepts one of the following:

class BetaThinkingConfigEnabled:

long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant

Accepts one of the following:

ADAPTIVE("adaptive")

Optional\<[BetaToolChoice](/docs/en/api/beta#beta_tool_choice)\> toolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant

Accepts one of the following:

ANY("any")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

Optional\<Boolean\> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant

Accepts one of the following:

NONE("none")

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

Accepts one of the following:

class BetaTool:

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

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Accepts one of the following:

CUSTOM("custom")

class BetaToolBash20241022:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20241022"constant"bash_20241022"constant

Accepts one of the following:

BASH_20241022("bash_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

JsonValue; type "bash_20250124"constant"bash_20250124"constant

Accepts one of the following:

BASH_20250124("bash_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522:

JsonValue; name "code_execution"constant"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE_EXECUTION("code_execution")

JsonValue; type "code_execution_20250522"constant"code_execution_20250522"constant

Accepts one of the following:

CODE_EXECUTION_20250522("code_execution_20250522")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonValue; name "code_execution"constant"code_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE_EXECUTION("code_execution")

JsonValue; type "code_execution_20250825"constant"code_execution_20250825"constant

Accepts one of the following:

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20241022"constant"computer_20241022"constant

Accepts one of the following:

COMPUTER_20241022("computer_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818:

JsonValue; name "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

MEMORY("memory")

JsonValue; type "memory_20250818"constant"memory_20250818"constant

Accepts one of the following:

MEMORY_20250818("memory_20250818")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20250124"constant"computer_20250124"constant

Accepts one of the following:

COMPUTER_20250124("computer_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20241022"constant"text_editor_20241022"constant

Accepts one of the following:

TEXT_EDITOR_20241022("text_editor_20241022")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

minimum1

long displayWidthPx

The width of the display in pixels.

minimum1

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

JsonValue; type "computer_20251124"constant"computer_20251124"constant

Accepts one of the following:

COMPUTER_20251124("computer_20251124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> displayNumber

The X11 display number (e.g. 0, 1) for the display.

minimum0

Optional\<Boolean\> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonValue; name "str_replace_editor"constant"str_replace_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_EDITOR("str_replace_editor")

JsonValue; type "text_editor_20250124"constant"text_editor_20250124"constant

Accepts one of the following:

TEXT_EDITOR_20250124("text_editor_20250124")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250429"constant"text_editor_20250429"constant

Accepts one of the following:

TEXT_EDITOR_20250429("text_editor_20250429")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonValue; name "str_replace_based_edit_tool"constant"str_replace_based_edit_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")

JsonValue; type "text_editor_20250728"constant"text_editor_20250728"constant

Accepts one of the following:

TEXT_EDITOR_20250728("text_editor_20250728")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<List\<InputExample\>\> inputExamples

Optional\<Long\> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305:

JsonValue; name "web_search"constant"web_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_SEARCH("web_search")

JsonValue; type "web_search_20250305"constant"web_search_20250305"constant

Accepts one of the following:

WEB_SEARCH_20250305("web_search_20250305")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<String\>\> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional\<List\<String\>\> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

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

class BetaWebFetchTool20250910:

JsonValue; name "web_fetch"constant"web_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB_FETCH("web_fetch")

JsonValue; type "web_fetch_20250910"constant"web_fetch_20250910"constant

Accepts one of the following:

WEB_FETCH_20250910("web_fetch_20250910")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<List\<String\>\> allowedDomains

List of domains to allow fetching from

Optional\<List\<String\>\> blockedDomains

List of domains to block fetching from

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<[BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param)\> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional\<Boolean\> enabled

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Long\> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

Optional\<Long\> maxUses

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolBm25_20251119:

JsonValue; name "tool_search_tool_bm25"constant"tool_search_tool_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")

TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonValue; name "tool_search_tool_regex"constant"tool_search_tool_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Type type

Accepts one of the following:

TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")

TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")

Optional\<List\<AllowedCaller\>\> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE_EXECUTION_20250825("code_execution_20250825")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

Optional\<Boolean\> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

Optional\<Boolean\> strict

When true, guarantees schema validation on tool names and inputs

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

String mcpServerName

Name of the MCP server to configure tools for

maxLength255

minLength1

JsonValue; type "mcp_toolset"constant"mcp_toolset"constant

Accepts one of the following:

MCP_TOOLSET("mcp_toolset")

Optional\<[BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral)\> cacheControl

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

class BetaMessageBatch:

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

[BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts) requestCounts

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

Create a Message Batch

Java

``` shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.batches.BatchCreateParams;
import com.anthropic.models.beta.messages.batches.BetaMessageBatch;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchCreateParams params = BatchCreateParams.builder()
            .addRequest(BatchCreateParams.Request.builder()
                .customId("my-custom-id-1")
                .params(BatchCreateParams.Request.Params.builder()
                    .maxTokens(1024L)
                    .addUserMessage("Hello, world")
                    .model(Model.CLAUDE_OPUS_4_6)
                    .build())
                .build())
            .build();
        BetaMessageBatch betaMessageBatch = client.beta().messages().batches().create(params);
    }
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
