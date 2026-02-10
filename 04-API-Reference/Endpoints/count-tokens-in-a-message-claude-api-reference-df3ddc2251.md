---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:06:31Z"
source_url: "https://platform.claude.com/docs/en/api/beta/messages/count_tokens"
title: "Count tokens in a Message - Claude API Reference"
---

Copy page

cURL

# Count tokens in a Message

post/v1/messages/count_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### Header ParametersExpand Collapse 

"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 16 more

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

##### Body ParametersExpand Collapse 

messages: array of [BetaMessageParam](/docs/en/api/beta#beta_message_param) { content, role }

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

content: string or array of [BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestDocumentBlock = object { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaSearchResultBlockParam = object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaThinkingBlockParam = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

BetaRedactedThinkingBlockParam = object { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

BetaToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

Accepts one of the following:

"tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or 2 more

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } or 2 more

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaSearchResultBlockParam = object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

BetaRequestDocumentBlock = object { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

BetaToolReferenceBlockParam = object { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error: optional boolean

BetaServerToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: "web_search" or "web_fetch" or "code_execution" or 4 more

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: optional [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

BetaDirectCaller = object { type }

Tool invocation directly from the model.

type: "direct"

Accepts one of the following:

"direct"

BetaServerToolCaller = object { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: string

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

BetaWebSearchToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = array of [BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age: optional string

BetaWebSearchToolRequestError = object { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: "web_search_tool_result_error"

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaWebFetchToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type } or [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

BetaWebFetchToolResultErrorBlockParam = object { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: "web_fetch_tool_result_error"

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchBlockParam = object { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } or 2 more

Accepts one of the following:

BetaBase64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

BetaPlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

BetaContentBlockSource = object { content, type }

content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

UnionMember0 = string

BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

BetaTextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

BetaImageBlockParam = object { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

BetaBase64ImageSource = object { data, media_type, type }

data: string

media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

BetaURLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileImageSource = object { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "image"

Accepts one of the following:

"image"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "content"

Accepts one of the following:

"content"

BetaURLPDFSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

BetaFileDocumentSource = object { file_id, type }

file_id: string

type: "file"

Accepts one of the following:

"file"

type: "document"

Accepts one of the following:

"document"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web_fetch_result"

Accepts one of the following:

"web_fetch_result"

url: string

Fetched content URL

retrieved_at: optional string

ISO 8601 timestamp when the content was retrieved

tool_use_id: string

type: "web_fetch_tool_result"

Accepts one of the following:

"web_fetch_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

BetaCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "code_execution_tool_result_error"

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type }

file_id: string

type: "code_execution_output"

Accepts one of the following:

"code_execution_output"

return_code: number

stderr: string

stdout: string

type: "code_execution_result"

Accepts one of the following:

"code_execution_result"

tool_use_id: string

type: "code_execution_tool_result"

Accepts one of the following:

"code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaBashCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type } or [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

BetaBashCodeExecutionToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: "bash_code_execution_tool_result_error"

Accepts one of the following:

"bash_code_execution_tool_result_error"

BetaBashCodeExecutionResultBlockParam = object { content, return_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type }

file_id: string

type: "bash_code_execution_output"

Accepts one of the following:

"bash_code_execution_output"

return_code: number

stderr: string

stdout: string

type: "bash_code_execution_result"

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: string

type: "bash_code_execution_tool_result"

Accepts one of the following:

"bash_code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaTextEditorCodeExecutionToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } or [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

BetaTextEditorCodeExecutionToolResultErrorParam = object { error_code, type, error_message }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: "text_editor_code_execution_tool_result_error"

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message: optional string

BetaTextEditorCodeExecutionViewResultBlockParam = object { content, file_type, type, 3 more }

content: string

file_type: "text" or "image" or "pdf"

Accepts one of the following:

"text"

"image"

"pdf"

type: "text_editor_code_execution_view_result"

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines: optional number

start_line: optional number

total_lines: optional number

BetaTextEditorCodeExecutionCreateResultBlockParam = object { is_file_update, type }

is_file_update: boolean

type: "text_editor_code_execution_create_result"

Accepts one of the following:

"text_editor_code_execution_create_result"

BetaTextEditorCodeExecutionStrReplaceResultBlockParam = object { type, lines, new_lines, 3 more }

type: "text_editor_code_execution_str_replace_result"

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines: optional array of string

new_lines: optional number

new_start: optional number

old_lines: optional number

old_start: optional number

tool_use_id: string

type: "text_editor_code_execution_tool_result"

Accepts one of the following:

"text_editor_code_execution_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaToolSearchToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type } or [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

BetaToolSearchToolResultErrorParam = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: "tool_search_tool_result_error"

Accepts one of the following:

"tool_search_tool_result_error"

BetaToolSearchToolSearchResultBlockParam = object { tool_references, type }

tool_references: array of [BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control }

tool_name: string

type: "tool_reference"

Accepts one of the following:

"tool_reference"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: "tool_search_tool_search_result"

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: string

type: "tool_search_tool_result"

Accepts one of the following:

"tool_search_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaMCPToolUseBlockParam = object { id, input, name, 3 more }

id: string

input: map\[unknown\]

name: string

server_name: string

The name of the MCP server

type: "mcp_tool_use"

Accepts one of the following:

"mcp_tool_use"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaRequestMCPToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "mcp_tool_result"

Accepts one of the following:

"mcp_tool_result"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

Accepts one of the following:

UnionMember0 = string

BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

is_error: optional boolean

BetaContainerUploadBlockParam = object { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string

type: "container_upload"

Accepts one of the following:

"container_upload"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCompactionBlockParam = object { content, type, cache_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

Accepts one of the following:

"compaction"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

role: "user" or "assistant"

Accepts one of the following:

"user"

"assistant"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = "claude-opus-4-6" or "claude-opus-4-5-20251101" or "claude-opus-4-5" or 18 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = string

context_management: optional [BetaContextManagementConfig](/docs/en/api/beta#beta_context_management_config) { edits }

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

edits: optional array of [BetaClearToolUses20250919Edit](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit) { type, clear_at_least, clear_tool_inputs, 3 more } or [BetaClearThinking20251015Edit](/docs/en/api/beta#beta_clear_thinking_20251015_edit) { type, keep } or [BetaCompact20260112Edit](/docs/en/api/beta#beta_compact_20260112_edit) { type, instructions, pause_after_compaction, trigger }

List of context management edits to apply

Accepts one of the following:

BetaClearToolUses20250919Edit = object { type, clear_at_least, clear_tool_inputs, 3 more }

type: "clear_tool_uses_20250919"

Accepts one of the following:

"clear_tool_uses_20250919"

clear_at_least: optional [BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

clear_tool_inputs: optional boolean or array of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

UnionMember0 = boolean

UnionMember1 = array of string

exclude_tools: optional array of string

Tool names whose uses are preserved from clearing

keep: optional [BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: "tool_uses"

Accepts one of the following:

"tool_uses"

value: number

trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value } or [BetaToolUsesTrigger](/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

BetaInputTokensTrigger = object { type, value }

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

BetaToolUsesTrigger = object { type, value }

type: "tool_uses"

Accepts one of the following:

"tool_uses"

value: number

BetaClearThinking20251015Edit = object { type, keep }

type: "clear_thinking_20251015"

Accepts one of the following:

"clear_thinking_20251015"

keep: optional [BetaThinkingTurns](/docs/en/api/beta#beta_thinking_turns) { type, value } or [BetaAllThinkingTurns](/docs/en/api/beta#beta_all_thinking_turns) { type } or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

BetaThinkingTurns = object { type, value }

type: "thinking_turns"

Accepts one of the following:

"thinking_turns"

value: number

BetaAllThinkingTurns = object { type }

type: "all"

Accepts one of the following:

"all"

UnionMember2 = "all"

Accepts one of the following:

"all"

BetaCompact20260112Edit = object { type, instructions, pause_after_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact_20260112"

Accepts one of the following:

"compact_20260112"

instructions: optional string

Additional instructions for summarization.

pause_after_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.

trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: "input_tokens"

Accepts one of the following:

"input_tokens"

value: number

mcp_servers: optional array of [BetaRequestMCPServerURLDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition) { name, type, url, 2 more }

MCP servers to be utilized in this request

name: string

type: "url"

Accepts one of the following:

"url"

url: string

authorization_token: optional string

tool_configuration: optional [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled }

allowed_tools: optional array of string

enabled: optional boolean

output_config: optional [BetaOutputConfig](/docs/en/api/beta#beta_output_config) { effort, format }

Configuration options for the model's output, such as the output format.

effort: optional "low" or "medium" or "high" or "max"

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format: optional [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: map\[unknown\]

The JSON schema of the format

type: "json_schema"

Accepts one of the following:

"json_schema"

Deprecatedoutput_format: optional [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format) { schema, type }

Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

schema: map\[unknown\]

The JSON schema of the format

type: "json_schema"

Accepts one of the following:

"json_schema"

system: optional string or array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

BetaCitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

BetaCitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

BetaCitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

BetaCitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

BetaCitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

thinking: optional [BetaThinkingConfigParam](/docs/en/api/beta#beta_thinking_config_param)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

BetaThinkingConfigEnabled = object { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

Accepts one of the following:

"enabled"

BetaThinkingConfigDisabled = object { type }

type: "disabled"

Accepts one of the following:

"disabled"

BetaThinkingConfigAdaptive = object { type }

type: "adaptive"

Accepts one of the following:

"adaptive"

tool_choice: optional [BetaToolChoice](/docs/en/api/beta#beta_tool_choice)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

BetaToolChoiceAuto = object { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

Accepts one of the following:

"auto"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

BetaToolChoiceAny = object { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

Accepts one of the following:

"any"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceTool = object { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

Accepts one of the following:

"tool"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

BetaToolChoiceNone = object { type }

The model will not be allowed to use tools.

type: "none"

Accepts one of the following:

"none"

tools: optional array of [BetaTool](/docs/en/api/beta#beta_tool) { input_schema, name, allowed_callers, 7 more } or [BetaToolBash20241022](/docs/en/api/beta#beta_tool_bash_20241022) { name, type, allowed_callers, 4 more } or [BetaToolBash20250124](/docs/en/api/beta#beta_tool_bash_20250124) { name, type, allowed_callers, 4 more } or 15 more

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

BetaTool = object { input_schema, name, allowed_callers, 7 more }

input_schema: object { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

Accepts one of the following:

"object"

properties: optional map\[unknown\]

required: optional array of string

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

Accepts one of the following:

"custom"

BetaToolBash20241022 = object { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20241022"

Accepts one of the following:

"bash_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolBash20250124 = object { name, type, allowed_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20250124"

Accepts one of the following:

"bash_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250522 = object { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: "code_execution_20250522"

Accepts one of the following:

"code_execution_20250522"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaCodeExecutionTool20250825 = object { name, type, allowed_callers, 3 more }

name: "code_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: "code_execution_20250825"

Accepts one of the following:

"code_execution_20250825"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20241022 = object { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20241022"

Accepts one of the following:

"computer_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818 = object { name, type, allowed_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"memory"

type: "memory_20250818"

Accepts one of the following:

"memory_20250818"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20250124 = object { display_height_px, display_width_px, name, 7 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20250124"

Accepts one of the following:

"computer_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20241022 = object { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20241022"

Accepts one of the following:

"text_editor_20241022"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolComputerUse20251124 = object { display_height_px, display_width_px, name, 8 more }

display_height_px: number

The height of the display in pixels.

minimum1

display_width_px: number

The width of the display in pixels.

minimum1

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: "computer_20251124"

Accepts one of the following:

"computer_20251124"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: optional number

The X11 display number (e.g. 0, 1) for the display.

minimum0

enable_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250124 = object { name, type, allowed_callers, 4 more }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20250124"

Accepts one of the following:

"text_editor_20250124"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250429 = object { name, type, allowed_callers, 4 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250429"

Accepts one of the following:

"text_editor_20250429"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolTextEditor20250728 = object { name, type, allowed_callers, 5 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250728"

Accepts one of the following:

"text_editor_20250728"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: optional array of map\[unknown\]

max_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaWebSearchTool20250305 = object { name, type, allowed_callers, 7 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: "web_search_20250305"

Accepts one of the following:

"web_search_20250305"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: optional number

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user_location: optional object { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

Accepts one of the following:

"approximate"

city: optional string

The city of the user.

maxLength255

minLength1

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: optional string

The region of the user.

maxLength255

minLength1

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

BetaWebFetchTool20250910 = object { name, type, allowed_callers, 8 more }

name: "web_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_fetch"

type: "web_fetch_20250910"

Accepts one of the following:

"web_fetch_20250910"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains: optional array of string

List of domains to allow fetching from

blocked_domains: optional array of string

List of domains to block fetching from

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: optional [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

max_uses: optional number

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolBm25_20251119 = object { name, type, allowed_callers, 3 more }

name: "tool_search_tool_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_bm25"

type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaToolSearchToolRegex20251119 = object { name, type, allowed_callers, 3 more }

name: "tool_search_tool_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_regex"

type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers: optional array of "direct" or "code_execution_20250825"

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

BetaMCPToolset = object { mcp_server_name, type, cache_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: string

Name of the MCP server to configure tools for

maxLength255

minLength1

type: "mcp_toolset"

Accepts one of the following:

"mcp_toolset"

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs: optional map\[[BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config) { defer_loading, enabled } \]

Configuration overrides for specific tools, keyed by tool name

defer_loading: optional boolean

enabled: optional boolean

default_config: optional [BetaMCPToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) { defer_loading, enabled }

Default configuration applied to all tools from this server

defer_loading: optional boolean

enabled: optional boolean

##### ReturnsExpand Collapse 

BetaMessageTokensCount = object { context_management, input_tokens }

context_management: [BetaCountTokensContextManagementResponse](/docs/en/api/beta#beta_count_tokens_context_management_response) { original_input_tokens }

Information about context management applied to the message.

original_input_tokens: number

The original token count before context management was applied

input_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

cURL

``` shiki
curl https://api.anthropic.com/v1/messages/count_tokens \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "messages": [
            {
              "content": "string",
              "role": "user"
            }
          ],
          "model": "claude-opus-4-6"
        }'
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
