---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:10:21Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/messages/create"
title: "Create a Message - Claude API Reference"
---

Copy page

Ruby

# Create a Message

messages.create(\*\*kwargs) -\> [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

post/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse 

max_tokens: Integer

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

messages: Array\[[MessageParam](/docs/en/api/messages#message_param) { content, role } \]

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

content: String \| Array\[[ContentBlockParam](/docs/en/api/messages#content_block_param)\]

Accepts one of the following:

String

Array\[[ContentBlockParam](/docs/en/api/messages#content_block_param)\]

Accepts one of the following:

class TextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]

Accepts one of the following:

class CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media_type, type }

data: String

media_type: :"image/jpeg" \| :"image/png" \| :"image/gif" \| :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class PlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class ContentBlockSource { content, type }

content: String \| Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

String

Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]

Accepts one of the following:

class CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media_type, type }

data: String

media_type: :"image/jpeg" \| :"image/png" \| :"image/gif" \| :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :document

Accepts one of the following:

:document

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled: bool

context: String

title: String

class SearchResultBlockParam { content, source, title, 3 more }

content: Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \]

text: String

type: :text

Accepts one of the following:

:text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]

Accepts one of the following:

class CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

source: String

title: String

type: :search_result

Accepts one of the following:

:search_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled: bool

class ThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlockParam { data, type }

data: String

type: :redacted_thinking

Accepts one of the following:

:redacted_thinking

class ToolUseBlockParam { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

Accepts one of the following:

:tool_use

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: String

type: :tool_result

Accepts one of the following:

:tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String \| Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \]

Accepts one of the following:

String

Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \]

Accepts one of the following:

class TextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]

Accepts one of the following:

class CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media_type, type }

data: String

media_type: :"image/jpeg" \| :"image/png" \| :"image/gif" \| :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class SearchResultBlockParam { content, source, title, 3 more }

content: Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \]

text: String

type: :text

Accepts one of the following:

:text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]

Accepts one of the following:

class CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

source: String

title: String

type: :search_result

Accepts one of the following:

:search_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled: bool

class DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class PlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class ContentBlockSource { content, type }

content: String \| Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

String

Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]

Accepts one of the following:

class CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media_type, type }

data: String

media_type: :"image/jpeg" \| :"image/png" \| :"image/gif" \| :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :document

Accepts one of the following:

:document

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled: bool

context: String

title: String

is_error: bool

class ServerToolUseBlockParam { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search

Accepts one of the following:

:web_search

type: :server_tool_use

Accepts one of the following:

:server_tool_use

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class WebSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

Array\[[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \]

encrypted_content: String

title: String

type: :web_search_result

Accepts one of the following:

:web_search_result

url: String

page_age: String

class WebSearchToolRequestError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :max_uses_exceeded \| 3 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Accepts one of the following:

:web_search_tool_result_error

tool_use_id: String

type: :web_search_tool_result

Accepts one of the following:

:web_search_tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

role: :user \| :assistant

Accepts one of the following:

:user

:assistant

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-opus-4-5-20251101" \| :"claude-opus-4-5" \| 18 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

inference_geo: String

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

metadata: [Metadata](/docs/en/api/messages#metadata) { user_id }

An object describing metadata about the request.

user_id: String

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

output_config: [OutputConfig](/docs/en/api/messages#output_config) { effort, format\_ }

Configuration options for the model's output, such as the output format.

effort: :low \| :medium \| :high \| :max

All possible effort levels.

Accepts one of the following:

:low

:medium

:high

:max

format\_: [JSONOutputFormat](/docs/en/api/messages#json_output_format) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: Hash\[Symbol, untyped\]

The JSON schema of the format

type: :json_schema

Accepts one of the following:

:json_schema

service_tier: :auto \| :standard_only

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

Accepts one of the following:

:auto

:standard_only

stop_sequences: Array\[String\]

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

stream: false

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

Accepts one of the following:

false

system\_: String \| Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \]

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

String

Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \]

text: String

type: :text

Accepts one of the following:

:text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]

Accepts one of the following:

class CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

temperature: Float

Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

thinking: [ThinkingConfigParam](/docs/en/api/messages#thinking_config_param)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class ThinkingConfigEnabled { budget_tokens, type }

budget_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

Accepts one of the following:

:enabled

class ThinkingConfigDisabled { type }

type: :disabled

Accepts one of the following:

:disabled

class ThinkingConfigAdaptive { type }

type: :adaptive

Accepts one of the following:

:adaptive

tool_choice: [ToolChoice](/docs/en/api/messages#tool_choice)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class ToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: :auto

Accepts one of the following:

:auto

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: :any

Accepts one of the following:

:any

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

Accepts one of the following:

:tool

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

Accepts one of the following:

:none

tools: Array\[[ToolUnion](/docs/en/api/messages#tool_union)\]

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

class Tool { input_schema, name, cache_control, 4 more }

input_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

Accepts one of the following:

:object

properties: Hash\[Symbol, untyped\]

required: Array\[String\]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: bool

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict: bool

When true, guarantees schema validation on tool names and inputs

type: :custom

Accepts one of the following:

:custom

class ToolBash20250124 { name, type, cache_control, strict }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash_20250124

Accepts one of the following:

:bash_20250124

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124 { name, type, cache_control, strict }

name: :str_replace_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str_replace_editor

type: :text_editor_20250124

Accepts one of the following:

:text_editor_20250124

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429 { name, type, cache_control, strict }

name: :str_replace_based_edit_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str_replace_based_edit_tool

type: :text_editor_20250429

Accepts one of the following:

:text_editor_20250429

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728 { name, type, cache_control, 2 more }

name: :str_replace_based_edit_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str_replace_based_edit_tool

type: :text_editor_20250728

Accepts one of the following:

:text_editor_20250728

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

max_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: bool

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305 { name, type, allowed_domains, 5 more }

name: :web_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web_search

type: :web_search_20250305

Accepts one of the following:

:web_search_20250305

allowed_domains: Array\[String\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Array\[String\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

max_uses: Integer

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: bool

When true, guarantees schema validation on tool names and inputs

user_location: { type, city, country, 2 more}

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

Accepts one of the following:

:approximate

city: String

The city of the user.

maxLength255

minLength1

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: String

The region of the user.

maxLength255

minLength1

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

top_k: Integer

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

top_p: Float

Use nucleus sampling.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

maximum1

minimum0

##### ReturnsExpand Collapse 

class Message { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array\[[ContentBlock](/docs/en/api/messages#content_block)\]

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

class TextBlock { citations, text, type }

citations: Array\[[TextCitation](/docs/en/api/messages#text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

Accepts one of the following:

:redacted_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

Accepts one of the following:

:tool_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search

Accepts one of the following:

:web_search

type: :server_tool_use

Accepts one of the following:

:server_tool_use

class WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :max_uses_exceeded \| 3 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Accepts one of the following:

:web_search_tool_result_error

Array\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

Accepts one of the following:

:web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

Accepts one of the following:

:web_search_tool_result

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-opus-4-5-20251101" \| :"claude-opus-4-5" \| 18 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop_reason: [StopReason](/docs/en/api/messages#stop_reason)

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

:end_turn

:max_tokens

:stop_sequence

:tool_use

:pause_turn

:refusal

stop_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

minimum0

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

minimum0

output_tokens: Integer

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests }

The number of server tool requests.

web_search_requests: Integer

The number of web search tool requests.

minimum0

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

Create a Message

Ruby

``` shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message = anthropic.messages.create(
  max_tokens: 1024,
  messages: [{content: "Hello, world", role: :user}],
  model: :"claude-opus-4-6"
)

puts(message)
```

Response 200

``` shiki
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
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
    "output_tokens": 503,
    "server_tool_use": {
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
    "output_tokens": 503,
    "server_tool_use": {
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
