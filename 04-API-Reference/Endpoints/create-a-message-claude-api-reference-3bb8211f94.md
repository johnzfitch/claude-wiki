---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:00:38Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/messages/create"
title: "Create a Message - Claude API Reference"
---
# Create a Message

messages.create(\*\*kwargs) -\> [Message](/docs/en/api/messages#message) { id, container, content, 6 more }

POST/v1/messages

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

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

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

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

type: :base64

class PlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

class ContentBlockSource { content, type }

content: String \| Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

String

Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam { text, type, cache_control, citations }

text: String

type: :text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

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

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class URLPDFSource { type, url }

type: :url

url: String

type: :document

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

source: String

title: String

type: :search_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class RedactedThinkingBlockParam { data, type }

data: String

type: :redacted_thinking

class ToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class ToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: String

type: :tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String \| Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| 2 more\]

Accepts one of the following:

String

Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| 2 more\]

Accepts one of the following:

class TextBlockParam { text, type, cache_control, citations }

text: String

type: :text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

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

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

source: String

title: String

type: :search_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

type: :base64

class PlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

class ContentBlockSource { content, type }

content: String \| Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

String

Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam { text, type, cache_control, citations }

text: String

type: :text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

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

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class URLPDFSource { type, url }

type: :url

url: String

type: :document

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class ToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: String

type: :tool_reference

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

is_error: bool

class ServerToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search \| :web_fetch \| :code_execution \| 4 more

Accepts one of the following:

:web_search

:web_fetch

:code_execution

:bash_code_execution

:text_editor_code_execution

:tool_search_tool_regex

:tool_search_tool_bm25

type: :server_tool_use

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class WebSearchToolResultBlockParam { content, tool_use_id, type, 2 more }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

Array\[[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \]

encrypted_content: String

title: String

type: :web_search_result

url: String

page_age: String

class WebSearchToolRequestError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

tool_use_id: String

type: :web_search_tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class WebFetchToolResultBlockParam { content, tool_use_id, type, 2 more }

content: [WebFetchToolResultErrorBlockParam](/docs/en/api/messages#web_fetch_tool_result_error_block_param) { error_code, type } \| [WebFetchBlockParam](/docs/en/api/messages#web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

class WebFetchToolResultErrorBlockParam { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:url_too_long

:url_not_allowed

:url_not_accessible

:unsupported_content_type

:too_many_requests

:max_uses_exceeded

:unavailable

type: :web_fetch_tool_result_error

class WebFetchBlockParam { content, type, url, retrieved_at }

content: [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

class ContentBlockSource { content, type }

content: String \| Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

String

Array\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam { text, type, cache_control, citations }

text: String

type: :text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

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

class URLImageSource { type, url }

type: :url

url: String

type: :image

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class URLPDFSource { type, url }

type: :url

url: String

type: :document

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

type: :web_fetch_result

url: String

Fetched content URL

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

tool_use_id: String

type: :web_fetch_tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

class CodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

class CodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\[[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \]

file_id: String

type: :code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

class EncryptedCodeExecutionResultBlockParam { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\[[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type } \]

file_id: String

type: :code_execution_output

encrypted_stdout: String

return_code: Integer

stderr: String

type: :encrypted_code_execution_result

tool_use_id: String

type: :code_execution_tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BashCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BashCodeExecutionToolResultErrorParam](/docs/en/api/messages#bash_code_execution_tool_result_error_param) { error_code, type } \| [BashCodeExecutionResultBlockParam](/docs/en/api/messages#bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

class BashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\[[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class TextEditorCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [TextEditorCodeExecutionToolResultErrorParam](/docs/en/api/messages#text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } \| [TextEditorCodeExecutionViewResultBlockParam](/docs/en/api/messages#text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } \| [TextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/messages#text_editor_code_execution_create_result_block_param) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

type: :text_editor_code_execution_tool_result_error

error_message: String

class TextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: String

file_type: :text \| :image \| :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text_editor_code_execution_view_result

num_lines: Integer

start_line: Integer

total_lines: Integer

class TextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

class TextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: :text_editor_code_execution_str_replace_result

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

tool_use_id: String

type: :text_editor_code_execution_tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [ToolSearchToolResultErrorParam](/docs/en/api/messages#tool_search_tool_result_error_param) { error_code, type } \| [ToolSearchToolSearchResultBlockParam](/docs/en/api/messages#tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

class ToolSearchToolResultErrorParam { error_code, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :tool_search_tool_result_error

class ToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\[[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param) { tool_name, type, cache_control } \]

tool_name: String

type: :tool_reference

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ContainerUploadBlockParam { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: String

type: :container_upload

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

:"claude-opus-4-6" \| :"claude-sonnet-4-6" \| :"claude-opus-4-5-20251101" \| 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

container: String

Container identifier for reuse across requests.

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

system\_: String \| Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \]

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

String

Array\[[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \]

text: String

type: :text

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

class CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

class CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

class CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

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

class ThinkingConfigDisabled { type }

type: :disabled

class ThinkingConfigAdaptive { type }

type: :adaptive

tool_choice: [ToolChoice](/docs/en/api/messages#tool_choice)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class ToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: :auto

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: :any

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

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

class Tool { input_schema, name, allowed_callers, 7 more }

input_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

properties: Hash\[Symbol, untyped\]

required: Array\[String\]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: bool

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

type: :custom

class ToolBash20250124 { name, type, allowed_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash_20250124

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250522 { name, type, allowed_callers, 3 more }

name: :code_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code_execution_20250522

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250825 { name, type, allowed_callers, 3 more }

name: :code_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code_execution_20250825

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20260120 { name, type, allowed_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: :code_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code_execution_20260120

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class MemoryTool20250818 { name, type, allowed_callers, 4 more }

name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :memory_20250818

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124 { name, type, allowed_callers, 4 more }

name: :str_replace_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text_editor_20250124

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429 { name, type, allowed_callers, 4 more }

name: :str_replace_based_edit_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text_editor_20250429

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728 { name, type, allowed_callers, 5 more }

name: :str_replace_based_edit_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text_editor_20250728

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

max_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: bool

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305 { name, type, allowed_callers, 7 more }

name: :web_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web_search_20250305

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

allowed_domains: Array\[String\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Array\[String\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

user_location: [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20250910 { name, type, allowed_callers, 8 more }

name: :web_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web_fetch_20250910

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

allowed_domains: Array\[String\]

List of domains to allow fetching from

blocked_domains: Array\[String\]

List of domains to block fetching from

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20260209 { name, type, allowed_callers, 7 more }

name: :web_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web_search_20260209

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

allowed_domains: Array\[String\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Array\[String\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

user_location: [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20260209 { name, type, allowed_callers, 8 more }

name: :web_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web_fetch_20260209

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

allowed_domains: Array\[String\]

List of domains to allow fetching from

blocked_domains: Array\[String\]

List of domains to block fetching from

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

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

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolBm25_20251119 { name, type, allowed_callers, 3 more }

name: :tool_search_tool_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :tool_search_tool_bm25_20251119 \| :tool_search_tool_bm25

Accepts one of the following:

:tool_search_tool_bm25_20251119

:tool_search_tool_bm25

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolRegex20251119 { name, type, allowed_callers, 3 more }

name: :tool_search_tool_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :tool_search_tool_regex_20251119 \| :tool_search_tool_regex

Accepts one of the following:

:tool_search_tool_regex_20251119

:tool_search_tool_regex

allowed_callers: Array\[:direct \| :code_execution_20250825 \| :code_execution_20260120\]

Accepts one of the following:

:direct

:code_execution_20250825

:code_execution_20260120

cache_control: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" \| :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

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

class Message { id, container, content, 6 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](/docs/en/api/messages#container) { id, expires_at }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires_at: Time

The time at which the container will expire.

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

class CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

class ToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

class ServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

input: Hash\[Symbol, untyped\]

name: :web_search \| :web_fetch \| :code_execution \| 4 more

Accepts one of the following:

:web_search

:web_fetch

:code_execution

:bash_code_execution

:text_editor_code_execution

:tool_search_tool_regex

:tool_search_tool_bm25

type: :server_tool_use

class WebSearchToolResultBlock { caller\_, content, tool_use_id, type }

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Array\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

class WebFetchToolResultBlock { caller\_, content, tool_use_id, type }

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

class WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:url_too_long

:url_not_allowed

:url_not_accessible

:unsupported_content_type

:too_many_requests

:max_uses_exceeded

:unavailable

type: :web_fetch_tool_result_error

class WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled }

Citation configuration for the document

enabled: bool

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

class Base64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

type: :web_fetch_result

url: String

Fetched content URL

tool_use_id: String

type: :web_fetch_tool_result

class CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

class CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

class EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

encrypted_stdout: String

return_code: Integer

stderr: String

type: :encrypted_code_execution_result

tool_use_id: String

type: :code_execution_tool_result

class BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

class BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

class TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

class TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

error_message: String

type: :text_editor_code_execution_tool_result_error

class TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: String

file_type: :text \| :image \| :pdf

Accepts one of the following:

:text

:image

:pdf

num_lines: Integer

start_line: Integer

total_lines: Integer

type: :text_editor_code_execution_view_result

class TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

class TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

type: :text_editor_code_execution_str_replace_result

tool_use_id: String

type: :text_editor_code_execution_tool_result

class ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

class ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

error_message: String

type: :tool_search_tool_result_error

class ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\[[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \]

tool_name: String

type: :tool_reference

type: :tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

class ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: String

type: :container_upload

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-sonnet-4-6" \| :"claude-opus-4-5-20251101" \| 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

output_tokens: Integer

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: Integer

The number of web fetch tool requests.

web_search_requests: Integer

The number of web search tool requests.

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

RawMessageStreamEvent = [RawMessageStartEvent](/docs/en/api/messages#raw_message_start_event) { message, type } \| [RawMessageDeltaEvent](/docs/en/api/messages#raw_message_delta_event) { delta, type, usage } \| [RawMessageStopEvent](/docs/en/api/messages#raw_message_stop_event) { type } \| 3 more

Accepts one of the following:

class RawMessageStartEvent { message, type }

message: [Message](/docs/en/api/messages#message) { id, container, content, 6 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [Container](/docs/en/api/messages#container) { id, expires_at }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires_at: Time

The time at which the container will expire.

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

class CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

class ToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

class ServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

input: Hash\[Symbol, untyped\]

name: :web_search \| :web_fetch \| :code_execution \| 4 more

Accepts one of the following:

:web_search

:web_fetch

:code_execution

:bash_code_execution

:text_editor_code_execution

:tool_search_tool_regex

:tool_search_tool_bm25

type: :server_tool_use

class WebSearchToolResultBlock { caller\_, content, tool_use_id, type }

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Array\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

class WebFetchToolResultBlock { caller\_, content, tool_use_id, type }

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

class WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:url_too_long

:url_not_allowed

:url_not_accessible

:unsupported_content_type

:too_many_requests

:max_uses_exceeded

:unavailable

type: :web_fetch_tool_result_error

class WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled }

Citation configuration for the document

enabled: bool

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

class Base64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

type: :web_fetch_result

url: String

Fetched content URL

tool_use_id: String

type: :web_fetch_tool_result

class CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

class CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

class EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

encrypted_stdout: String

return_code: Integer

stderr: String

type: :encrypted_code_execution_result

tool_use_id: String

type: :code_execution_tool_result

class BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

class BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

class TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

class TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

error_message: String

type: :text_editor_code_execution_tool_result_error

class TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: String

file_type: :text \| :image \| :pdf

Accepts one of the following:

:text

:image

:pdf

num_lines: Integer

start_line: Integer

total_lines: Integer

type: :text_editor_code_execution_view_result

class TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

class TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

type: :text_editor_code_execution_str_replace_result

tool_use_id: String

type: :text_editor_code_execution_tool_result

class ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

class ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

error_message: String

type: :tool_search_tool_result_error

class ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\[[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \]

tool_name: String

type: :tool_reference

type: :tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

class ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: String

type: :container_upload

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-sonnet-4-6" \| :"claude-opus-4-5-20251101" \| 19 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

output_tokens: Integer

The number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: Integer

The number of web fetch tool requests.

web_search_requests: Integer

The number of web search tool requests.

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :message_start

class RawMessageDeltaEvent { delta, type, usage }

delta: { container, stop_reason, stop_sequence}

container: [Container](/docs/en/api/messages#container) { id, expires_at }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires_at: Time

The time at which the container will expire.

stop_reason: [StopReason](/docs/en/api/messages#stop_reason)

Accepts one of the following:

:end_turn

:max_tokens

:stop_sequence

:tool_use

:pause_turn

:refusal

stop_sequence: String

type: :message_delta

usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

cache_read_input_tokens: Integer

The cumulative number of input tokens read from the cache.

input_tokens: Integer

The cumulative number of input tokens which were used.

output_tokens: Integer

The cumulative number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: Integer

The number of web fetch tool requests.

web_search_requests: Integer

The number of web search tool requests.

class RawMessageStopEvent { type }

type: :message_stop

class RawContentBlockStartEvent { content_block, index, type }

content_block: [TextBlock](/docs/en/api/messages#text_block) { citations, text, type } \| [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type } \| [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type } \| 9 more

Response model for a file uploaded to the container.

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

class CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

text: String

type: :text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

class ToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

class ServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

input: Hash\[Symbol, untyped\]

name: :web_search \| :web_fetch \| :code_execution \| 4 more

Accepts one of the following:

:web_search

:web_fetch

:code_execution

:bash_code_execution

:text_editor_code_execution

:tool_search_tool_regex

:tool_search_tool_bm25

type: :server_tool_use

class WebSearchToolResultBlock { caller\_, content, tool_use_id, type }

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError { error_code, type }

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Array\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

class WebFetchToolResultBlock { caller\_, content, tool_use_id, type }

caller\_: [DirectCaller](/docs/en/api/messages#direct_caller) { type } \| [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } \| [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller { type }

Tool invocation directly from the model.

type: :direct

class ServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

class ServerToolCaller20260120 { tool_id, type }

tool_id: String

type: :code_execution_20260120

content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } \| [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

class WebFetchToolResultErrorBlock { error_code, type }

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:url_too_long

:url_not_allowed

:url_not_accessible

:unsupported_content_type

:too_many_requests

:max_uses_exceeded

:unavailable

type: :web_fetch_tool_result_error

class WebFetchBlock { content, retrieved_at, type, url }

content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }

citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled }

Citation configuration for the document

enabled: bool

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }

Accepts one of the following:

class Base64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

type: :base64

class PlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

type: :web_fetch_result

url: String

Fetched content URL

tool_use_id: String

type: :web_fetch_tool_result

class CodeExecutionToolResultBlock { content, tool_use_id, type }

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError { error_code, type }

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

class CodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

class EncryptedCodeExecutionResultBlock { content, encrypted_stdout, return_code, 2 more }

Code execution result with encrypted stdout for PFC + web_search results.

content: Array\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

encrypted_stdout: String

return_code: Integer

stderr: String

type: :encrypted_code_execution_result

tool_use_id: String

type: :code_execution_tool_result

class BashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } \| [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BashCodeExecutionToolResultError { error_code, type }

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

class BashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

class TextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } \| [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

class TextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

error_message: String

type: :text_editor_code_execution_tool_result_error

class TextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

content: String

file_type: :text \| :image \| :pdf

Accepts one of the following:

:text

:image

:pdf

num_lines: Integer

start_line: Integer

total_lines: Integer

type: :text_editor_code_execution_view_result

class TextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

class TextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

type: :text_editor_code_execution_str_replace_result

tool_use_id: String

type: :text_editor_code_execution_tool_result

class ToolSearchToolResultBlock { content, tool_use_id, type }

content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } \| [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

class ToolSearchToolResultError { error_code, error_message, type }

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

error_message: String

type: :tool_search_tool_result_error

class ToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\[[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type } \]

tool_name: String

type: :tool_reference

type: :tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

class ContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: String

type: :container_upload

index: Integer

type: :content_block_start

class RawContentBlockDeltaEvent { delta, index, type }

delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

class TextDelta { text, type }

text: String

type: :text_delta

class InputJSONDelta { partial_json, type }

partial_json: String

type: :input_json_delta

class CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

class CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

class CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

class CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

class CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

url: String

class CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

type: :citations_delta

class ThinkingDelta { thinking, type }

thinking: String

type: :thinking_delta

class SignatureDelta { signature, type }

signature: String

type: :signature_delta

index: Integer

type: :content_block_delta

class RawContentBlockStopEvent { index, type }

index: Integer

type: :content_block_stop

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
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z"
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
    "expires_at": "2019-12-27T18:11:19.117Z"
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
