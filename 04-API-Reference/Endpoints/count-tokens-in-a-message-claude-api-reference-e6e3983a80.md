---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:06:05Z"
source_url: "https://platform.claude.com/docs/en/api/messages/count_tokens"
title: "Count tokens in a Message - Claude API Reference"
---

Copy page

cURL

# Count tokens in a Message

post/v1/messages/count_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### Body ParametersExpand Collapse 

messages: array of [MessageParam](/docs/en/api/messages#message_param) { content, role }

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

content: string or array of [ContentBlockParam](/docs/en/api/messages#content_block_param)

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [ContentBlockParam](/docs/en/api/messages#content_block_param)

Accepts one of the following:

TextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)

Accepts one of the following:

CitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam = object { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource = object { data, media_type, type }

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

URLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

DocumentBlockParam = object { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } or [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } or [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

PlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

ContentBlockSource = object { content, type }

content: string or array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

UnionMember0 = string

ContentBlockSourceContent = array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

TextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)

Accepts one of the following:

CitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam = object { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource = object { data, media_type, type }

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

URLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

URLPDFSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "document"

Accepts one of the following:

"document"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

SearchResultBlockParam = object { content, source, title, 3 more }

content: array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)

Accepts one of the following:

CitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

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

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled: optional boolean

ThinkingBlockParam = object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlockParam = object { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlockParam = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

ToolResultBlockParam = object { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

Accepts one of the following:

"tool_result"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

content: optional string or array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } or [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } or [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } or [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more }

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } or [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } or [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } or [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more }

Accepts one of the following:

TextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)

Accepts one of the following:

CitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam = object { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource = object { data, media_type, type }

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

URLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

SearchResultBlockParam = object { content, source, title, 3 more }

content: array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)

Accepts one of the following:

CitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

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

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled: optional boolean

DocumentBlockParam = object { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } or [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } or [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource = object { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

PlainTextSource = object { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

ContentBlockSource = object { content, type }

content: string or array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

UnionMember0 = string

ContentBlockSourceContent = array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

TextBlockParam = object { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)

Accepts one of the following:

CitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam = object { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource = object { data, media_type, type }

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

URLImageSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

URLPDFSource = object { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "document"

Accepts one of the following:

"document"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled: optional boolean

context: optional string

title: optional string

is_error: optional boolean

ServerToolUseBlockParam = object { id, input, name, 2 more }

id: string

input: map\[unknown\]

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

WebSearchToolResultBlockParam = object { content, tool_use_id, type, cache_control }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age: optional string

WebSearchToolRequestError = object { error_code, type }

error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more

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

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

output_config: optional [OutputConfig](/docs/en/api/messages#output_config) { effort, format }

Configuration options for the model's output, such as the output format.

effort: optional "low" or "medium" or "high" or "max"

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format: optional [JSONOutputFormat](/docs/en/api/messages#json_output_format) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: map\[unknown\]

The JSON schema of the format

type: "json_schema"

Accepts one of the following:

"json_schema"

system: optional string or array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

UnionMember0 = string

UnionMember1 = array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)

Accepts one of the following:

CitationCharLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam = object { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam = object { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam = object { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string

type: "search_result_location"

Accepts one of the following:

"search_result_location"

thinking: optional [ThinkingConfigParam](/docs/en/api/messages#thinking_config_param)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

ThinkingConfigEnabled = object { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

Accepts one of the following:

"enabled"

ThinkingConfigDisabled = object { type }

type: "disabled"

Accepts one of the following:

"disabled"

ThinkingConfigAdaptive = object { type }

type: "adaptive"

Accepts one of the following:

"adaptive"

tool_choice: optional [ToolChoice](/docs/en/api/messages#tool_choice)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

ToolChoiceAuto = object { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

Accepts one of the following:

"auto"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

ToolChoiceAny = object { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

Accepts one of the following:

"any"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolChoiceTool = object { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

Accepts one of the following:

"tool"

disable_parallel_tool_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolChoiceNone = object { type }

The model will not be allowed to use tools.

type: "none"

Accepts one of the following:

"none"

tools: optional array of [MessageCountTokensTool](/docs/en/api/messages#message_count_tokens_tool)

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

Tool = object { input_schema, name, cache_control, 4 more }

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

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

Accepts one of the following:

"custom"

ToolBash20250124 = object { name, type, cache_control, strict }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20250124"

Accepts one of the following:

"bash_20250124"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250124 = object { name, type, cache_control, strict }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20250124"

Accepts one of the following:

"text_editor_20250124"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250429 = object { name, type, cache_control, strict }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250429"

Accepts one of the following:

"text_editor_20250429"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250728 = object { name, type, cache_control, 2 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250728"

Accepts one of the following:

"text_editor_20250728"

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

max_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

WebSearchTool20250305 = object { name, type, allowed_domains, 5 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: "web_search_20250305"

Accepts one of the following:

"web_search_20250305"

allowed_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

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

##### ReturnsExpand Collapse 

MessageTokensCount = object { input_tokens }

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
