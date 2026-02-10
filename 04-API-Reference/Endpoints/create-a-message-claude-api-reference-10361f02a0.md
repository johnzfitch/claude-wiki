---
category: "04-API-Reference"
fetched_at: "2026-02-07T01:27:12Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/beta/messages/create"
title: "Create a Message - Claude API Reference"
---

Copy page

Ruby

# Create a Message

beta.messages.create(\*\*kwargs) -\> [BetaMessage](/docs/en/api/beta#beta_message) { id, container, content, 7 more }

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

messages: Array\[[BetaMessageParam](/docs/en/api/beta#beta_message_param) { content, role } \]

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

content: String \| Array\[[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\]

Accepts one of the following:

String

Array\[[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media_type, type }

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

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file_id, type }

file_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaRequestDocumentBlock { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String \| Array\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

String

Array\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media_type, type }

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

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file_id, type }

file_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file_id, type }

file_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: bool

context: String

title: String

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \]

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

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

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: bool

class BetaThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlockParam { data, type }

data: String

type: :redacted_thinking

Accepts one of the following:

:redacted_thinking

class BetaToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

Accepts one of the following:

:tool_use

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

Accepts one of the following:

:code_execution_20250825

class BetaToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: String

type: :tool_result

Accepts one of the following:

:tool_result

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

content: String \| Array\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } \| 2 more\]

Accepts one of the following:

String

Array\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \| [BetaImageBlockParam](/docs/en/api/beta#beta_image_block_param) { source, type, cache_control } \| [BetaSearchResultBlockParam](/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more } \| 2 more\]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media_type, type }

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

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file_id, type }

file_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \]

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

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

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: bool

class BetaRequestDocumentBlock { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String \| Array\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

String

Array\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media_type, type }

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

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file_id, type }

file_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file_id, type }

file_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: bool

context: String

title: String

class BetaToolReferenceBlockParam { tool_name, type, cache_control }

Tool reference block that can be included in tool_result content.

tool_name: String

type: :tool_reference

Accepts one of the following:

:tool_reference

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

is_error: bool

class BetaServerToolUseBlockParam { id, input, name, 3 more }

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

Accepts one of the following:

:server_tool_use

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

Accepts one of the following:

:code_execution_20250825

class BetaWebSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

Array\[[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more } \]

encrypted_content: String

title: String

type: :web_search_result

Accepts one of the following:

:web_search_result

url: String

page_age: String

class BetaWebSearchToolRequestError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

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

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaWebFetchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type } \| [BetaWebFetchBlockParam](/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

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

Accepts one of the following:

:web_fetch_tool_result_error

class BetaWebFetchBlockParam { content, type, url, retrieved_at }

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more }

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } \| [BetaContentBlockSource](/docs/en/api/beta#beta_content_block_source) { content, type } \| 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String \| Array\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

String

Array\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

class BetaImageBlockParam { source, type, cache_control }

source: [BetaBase64ImageSource](/docs/en/api/beta#beta_base64_image_source) { data, media_type, type } \| [BetaURLImageSource](/docs/en/api/beta#beta_url_image_source) { type, url } \| [BetaFileImageSource](/docs/en/api/beta#beta_file_image_source) { file_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media_type, type }

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

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file_id, type }

file_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file_id, type }

file_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

enabled: bool

context: String

title: String

type: :web_fetch_result

Accepts one of the following:

:web_fetch_result

url: String

Fetched content URL

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

tool_use_id: String

type: :web_fetch_tool_result

Accepts one of the following:

:web_fetch_tool_result

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

Accepts one of the following:

:code_execution_tool_result_error

class BetaCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\[[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type } \]

file_id: String

type: :code_execution_output

Accepts one of the following:

:code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

Accepts one of the following:

:code_execution_result

tool_use_id: String

type: :code_execution_tool_result

Accepts one of the following:

:code_execution_tool_result

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaBashCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type } \| [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

Accepts one of the following:

:bash_code_execution_tool_result_error

class BetaBashCodeExecutionResultBlockParam { content, return_code, stderr, 2 more }

content: Array\[[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

Accepts one of the following:

:bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

Accepts one of the following:

:bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

Accepts one of the following:

:bash_code_execution_tool_result

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaTextEditorCodeExecutionToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } \| [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam { error_code, type, error_message }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

type: :text_editor_code_execution_tool_result_error

Accepts one of the following:

:text_editor_code_execution_tool_result_error

error_message: String

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file_type, type, 3 more }

content: String

file_type: :text \| :image \| :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text_editor_code_execution_view_result

Accepts one of the following:

:text_editor_code_execution_view_result

num_lines: Integer

start_line: Integer

total_lines: Integer

class BetaTextEditorCodeExecutionCreateResultBlockParam { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

Accepts one of the following:

:text_editor_code_execution_create_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new_lines, 3 more }

type: :text_editor_code_execution_str_replace_result

Accepts one of the following:

:text_editor_code_execution_str_replace_result

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

tool_use_id: String

type: :text_editor_code_execution_tool_result

Accepts one of the following:

:text_editor_code_execution_tool_result

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaToolSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type } \| [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type }

Accepts one of the following:

class BetaToolSearchToolResultErrorParam { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| :execution_time_exceeded

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :tool_search_tool_result_error

Accepts one of the following:

:tool_search_tool_result_error

class BetaToolSearchToolSearchResultBlockParam { tool_references, type }

tool_references: Array\[[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control } \]

tool_name: String

type: :tool_reference

Accepts one of the following:

:tool_reference

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

type: :tool_search_tool_search_result

Accepts one of the following:

:tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

Accepts one of the following:

:tool_search_tool_result

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

server_name: String

The name of the MCP server

type: :mcp_tool_use

Accepts one of the following:

:mcp_tool_use

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaRequestMCPToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: String

type: :mcp_tool_result

Accepts one of the following:

:mcp_tool_result

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

content: String \| Array\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \]

Accepts one of the following:

String

Array\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \]

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

is_error: bool

class BetaContainerUploadBlockParam { file_id, type, cache_control }

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: String

type: :container_upload

Accepts one of the following:

:container_upload

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

class BetaCompactionBlockParam { content, type, cache_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: String

Summary of previously compacted content, or null if compaction failed

type: :compaction

Accepts one of the following:

:compaction

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

container: [BetaContainerParams](/docs/en/api/beta#beta_container_params) { id, skills } \| String

Container identifier for reuse across requests.

Accepts one of the following:

class BetaContainerParams { id, skills }

Container parameters with skills to be loaded.

id: String

Container id

skills: Array\[[BetaSkillParams](/docs/en/api/beta#beta_skill_params) { skill_id, type, version } \]

List of skills to load in the container

skill_id: String

Skill ID

maxLength64

minLength1

type: :anthropic \| :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

String

context_management: [BetaContextManagementConfig](/docs/en/api/beta#beta_context_management_config) { edits }

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

edits: Array\[[BetaClearToolUses20250919Edit](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit) { type, clear_at_least, clear_tool_inputs, 3 more } \| [BetaClearThinking20251015Edit](/docs/en/api/beta#beta_clear_thinking_20251015_edit) { type, keep } \| [BetaCompact20260112Edit](/docs/en/api/beta#beta_compact_20260112_edit) { type, instructions, pause_after_compaction, trigger } \]

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit { type, clear_at_least, clear_tool_inputs, 3 more }

type: :clear_tool_uses_20250919

Accepts one of the following:

:clear_tool_uses_20250919

clear_at_least: [BetaInputTokensClearAtLeast](/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: :input_tokens

Accepts one of the following:

:input_tokens

value: Integer

clear_tool_inputs: bool \| Array\[String\]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

bool

Array\[String\]

exclude_tools: Array\[String\]

Tool names whose uses are preserved from clearing

keep: [BetaToolUsesKeep](/docs/en/api/beta#beta_tool_uses_keep) { type, value }

Number of tool uses to retain in the conversation

type: :tool_uses

Accepts one of the following:

:tool_uses

value: Integer

trigger: [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value } \| [BetaToolUsesTrigger](/docs/en/api/beta#beta_tool_uses_trigger) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger { type, value }

type: :input_tokens

Accepts one of the following:

:input_tokens

value: Integer

class BetaToolUsesTrigger { type, value }

type: :tool_uses

Accepts one of the following:

:tool_uses

value: Integer

class BetaClearThinking20251015Edit { type, keep }

type: :clear_thinking_20251015

Accepts one of the following:

:clear_thinking_20251015

keep: [BetaThinkingTurns](/docs/en/api/beta#beta_thinking_turns) { type, value } \| [BetaAllThinkingTurns](/docs/en/api/beta#beta_all_thinking_turns) { type } \| :all

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns { type, value }

type: :thinking_turns

Accepts one of the following:

:thinking_turns

value: Integer

class BetaAllThinkingTurns { type }

type: :all

Accepts one of the following:

:all

Keep = :all

Accepts one of the following:

:all

class BetaCompact20260112Edit { type, instructions, pause_after_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: :compact_20260112

Accepts one of the following:

:compact_20260112

instructions: String

Additional instructions for summarization.

pause_after_compaction: bool

Whether to pause after compaction and return the compaction block to the user.

trigger: [BetaInputTokensTrigger](/docs/en/api/beta#beta_input_tokens_trigger) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: :input_tokens

Accepts one of the following:

:input_tokens

value: Integer

inference_geo: String

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

mcp_servers: Array\[[BetaRequestMCPServerURLDefinition](/docs/en/api/beta#beta_request_mcp_server_url_definition) { name, type, url, 2 more } \]

MCP servers to be utilized in this request

name: String

type: :url

Accepts one of the following:

:url

url: String

authorization_token: String

tool_configuration: [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled }

allowed_tools: Array\[String\]

enabled: bool

metadata: [BetaMetadata](/docs/en/api/beta#beta_metadata) { user_id }

An object describing metadata about the request.

user_id: String

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

output_config: [BetaOutputConfig](/docs/en/api/beta#beta_output_config) { effort, format\_ }

Configuration options for the model's output, such as the output format.

effort: :low \| :medium \| :high \| :max

All possible effort levels.

Accepts one of the following:

:low

:medium

:high

:max

format\_: [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: Hash\[Symbol, untyped\]

The JSON schema of the format

type: :json_schema

Accepts one of the following:

:json_schema

Deprecatedoutput_format: [BetaJSONOutputFormat](/docs/en/api/beta#beta_json_output_format) { schema, type }

Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

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

system\_: String \| Array\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \]

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

String

Array\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } \]

text: String

type: :text

Accepts one of the following:

:text

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: Array\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]

Accepts one of the following:

class BetaCitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

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

thinking: [BetaThinkingConfigParam](/docs/en/api/beta#beta_thinking_config_param)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class BetaThinkingConfigEnabled { budget_tokens, type }

budget_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

Accepts one of the following:

:enabled

class BetaThinkingConfigDisabled { type }

type: :disabled

Accepts one of the following:

:disabled

class BetaThinkingConfigAdaptive { type }

type: :adaptive

Accepts one of the following:

:adaptive

tool_choice: [BetaToolChoice](/docs/en/api/beta#beta_tool_choice)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class BetaToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: :auto

Accepts one of the following:

:auto

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: :any

Accepts one of the following:

:any

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

Accepts one of the following:

:tool

disable_parallel_tool_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

Accepts one of the following:

:none

tools: Array\[[BetaToolUnion](/docs/en/api/beta#beta_tool_union)\]

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

class BetaTool { input_schema, name, allowed_callers, 7 more }

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

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

Accepts one of the following:

:custom

class BetaToolBash20241022 { name, type, allowed_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash_20241022

Accepts one of the following:

:bash_20241022

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124 { name, type, allowed_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash_20250124

Accepts one of the following:

:bash_20250124

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522 { name, type, allowed_callers, 3 more }

name: :code_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:code_execution

type: :code_execution_20250522

Accepts one of the following:

:code_execution_20250522

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825 { name, type, allowed_callers, 3 more }

name: :code_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:code_execution

type: :code_execution_20250825

Accepts one of the following:

:code_execution_20250825

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022 { display_height_px, display_width_px, name, 7 more }

display_height_px: Integer

The height of the display in pixels.

minimum1

display_width_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer_20241022

Accepts one of the following:

:computer_20241022

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Integer

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818 { name, type, allowed_callers, 4 more }

name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:memory

type: :memory_20250818

Accepts one of the following:

:memory_20250818

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124 { display_height_px, display_width_px, name, 7 more }

display_height_px: Integer

The height of the display in pixels.

minimum1

display_width_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer_20250124

Accepts one of the following:

:computer_20250124

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Integer

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022 { name, type, allowed_callers, 4 more }

name: :str_replace_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str_replace_editor

type: :text_editor_20241022

Accepts one of the following:

:text_editor_20241022

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124 { display_height_px, display_width_px, name, 8 more }

display_height_px: Integer

The height of the display in pixels.

minimum1

display_width_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer_20251124

Accepts one of the following:

:computer_20251124

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Integer

The X11 display number (e.g. 0, 1) for the display.

minimum0

enable_zoom: bool

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124 { name, type, allowed_callers, 4 more }

name: :str_replace_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str_replace_editor

type: :text_editor_20250124

Accepts one of the following:

:text_editor_20250124

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429 { name, type, allowed_callers, 4 more }

name: :str_replace_based_edit_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str_replace_based_edit_tool

type: :text_editor_20250429

Accepts one of the following:

:text_editor_20250429

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728 { name, type, allowed_callers, 5 more }

name: :str_replace_based_edit_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str_replace_based_edit_tool

type: :text_editor_20250728

Accepts one of the following:

:text_editor_20250728

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Array\[Hash\[Symbol, untyped\]\]

max_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305 { name, type, allowed_callers, 7 more }

name: :web_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web_search

type: :web_search_20250305

Accepts one of the following:

:web_search_20250305

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

allowed_domains: Array\[String\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Array\[String\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

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

class BetaWebFetchTool20250910 { name, type, allowed_callers, 8 more }

name: :web_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web_fetch

type: :web_fetch_20250910

Accepts one of the following:

:web_fetch_20250910

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

allowed_domains: Array\[String\]

List of domains to allow fetching from

blocked_domains: Array\[String\]

List of domains to block fetching from

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

citations: [BetaCitationsConfigParam](/docs/en/api/beta#beta_citations_config_param) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

max_uses: Integer

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolBm25_20251119 { name, type, allowed_callers, 3 more }

name: :tool_search_tool_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:tool_search_tool_bm25

type: :tool_search_tool_bm25_20251119 \| :tool_search_tool_bm25

Accepts one of the following:

:tool_search_tool_bm25_20251119

:tool_search_tool_bm25

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119 { name, type, allowed_callers, 3 more }

name: :tool_search_tool_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:tool_search_tool_regex

type: :tool_search_tool_regex_20251119 \| :tool_search_tool_regex

Accepts one of the following:

:tool_search_tool_regex_20251119

:tool_search_tool_regex

allowed_callers: Array\[:direct \| :code_execution_20250825\]

Accepts one of the following:

:direct

:code_execution_20250825

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

defer_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaMCPToolset { mcp_server_name, type, cache_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: String

Name of the MCP server to configure tools for

maxLength255

minLength1

type: :mcp_toolset

Accepts one of the following:

:mcp_toolset

cache_control: [BetaCacheControlEphemeral](/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl }

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

configs: Hash\[Symbol, [BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config) { defer_loading, enabled } \]

Configuration overrides for specific tools, keyed by tool name

defer_loading: bool

enabled: bool

default_config: [BetaMCPToolDefaultConfig](/docs/en/api/beta#beta_mcp_tool_default_config) { defer_loading, enabled }

Default configuration applied to all tools from this server

defer_loading: bool

enabled: bool

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

anthropic_beta: Array\[[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" \| :"prompt-caching-2024-07-31" \| :"computer-use-2024-10-22" \| 16 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

##### ReturnsExpand Collapse 

class BetaMessage { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](/docs/en/api/beta#beta_container) { id, expires_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires_at: Time

The time at which the container will expire.

formatdate-time

skills: Array\[[BetaSkill](/docs/en/api/beta#beta_skill) { skill_id, type, version } \]

Skills loaded in the container

skill_id: String

Skill ID

maxLength64

minLength1

type: :anthropic \| :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: Array\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

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

class BetaTextBlock { citations, text, type }

citations: Array\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

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

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

Accepts one of the following:

:redacted_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

Accepts one of the following:

:tool_use

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

Accepts one of the following:

:code_execution_20250825

class BetaServerToolUseBlock { id, input, name, 2 more }

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

Accepts one of the following:

:server_tool_use

caller\_: [BetaDirectCaller](/docs/en/api/beta#beta_direct_caller) { type } \| [BetaServerToolCaller](/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool_id, type }

Tool invocation generated by a server-side tool.

tool_id: String

type: :code_execution_20250825

Accepts one of the following:

:code_execution_20250825

class BetaWebSearchToolResultBlock { content, tool_use_id, type }

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError { error_code, type }

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

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

Array\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

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

class BetaWebFetchToolResultBlock { content, tool_use_id, type }

content: [BetaWebFetchToolResultErrorBlock](/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type } \| [BetaWebFetchBlock](/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error_code, type }

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

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

Accepts one of the following:

:web_fetch_tool_result_error

class BetaWebFetchBlock { content, retrieved_at, type, url }

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block) { citations, source, title, type }

citations: [BetaCitationConfig](/docs/en/api/beta#beta_citation_config) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type } \| [BetaPlainTextSource](/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media_type, type }

data: String

media_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media_type, type }

data: String

media_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved_at: String

ISO 8601 timestamp when the content was retrieved

type: :web_fetch_result

Accepts one of the following:

:web_fetch_result

url: String

Fetched content URL

tool_use_id: String

type: :web_fetch_tool_result

Accepts one of the following:

:web_fetch_tool_result

class BetaCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error_code, type }

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

type: :code_execution_tool_result_error

Accepts one of the following:

:code_execution_tool_result_error

class BetaCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } \]

file_id: String

type: :code_execution_output

Accepts one of the following:

:code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :code_execution_result

Accepts one of the following:

:code_execution_result

tool_use_id: String

type: :code_execution_tool_result

Accepts one of the following:

:code_execution_tool_result

class BetaBashCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaBashCodeExecutionToolResultError](/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type } \| [BetaBashCodeExecutionResultBlock](/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:output_file_too_large

type: :bash_code_execution_tool_result_error

Accepts one of the following:

:bash_code_execution_tool_result_error

class BetaBashCodeExecutionResultBlock { content, return_code, stderr, 2 more }

content: Array\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } \]

file_id: String

type: :bash_code_execution_output

Accepts one of the following:

:bash_code_execution_output

return_code: Integer

stderr: String

stdout: String

type: :bash_code_execution_result

Accepts one of the following:

:bash_code_execution_result

tool_use_id: String

type: :bash_code_execution_tool_result

Accepts one of the following:

:bash_code_execution_tool_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool_use_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type } \| [BetaTextEditorCodeExecutionViewResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } \| [BetaTextEditorCodeExecutionCreateResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type } \| [BetaTextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error_code, error_message, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| 2 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

:file_not_found

error_message: String

type: :text_editor_code_execution_tool_result_error

Accepts one of the following:

:text_editor_code_execution_tool_result_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file_type, num_lines, 3 more }

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

Accepts one of the following:

:text_editor_code_execution_view_result

class BetaTextEditorCodeExecutionCreateResultBlock { is_file_update, type }

is_file_update: bool

type: :text_editor_code_execution_create_result

Accepts one of the following:

:text_editor_code_execution_create_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new_lines, new_start, 3 more }

lines: Array\[String\]

new_lines: Integer

new_start: Integer

old_lines: Integer

old_start: Integer

type: :text_editor_code_execution_str_replace_result

Accepts one of the following:

:text_editor_code_execution_str_replace_result

tool_use_id: String

type: :text_editor_code_execution_tool_result

Accepts one of the following:

:text_editor_code_execution_tool_result

class BetaToolSearchToolResultBlock { content, tool_use_id, type }

content: [BetaToolSearchToolResultError](/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type } \| [BetaToolSearchToolSearchResultBlock](/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error_code, error_message, type }

error_code: :invalid_tool_input \| :unavailable \| :too_many_requests \| :execution_time_exceeded

Accepts one of the following:

:invalid_tool_input

:unavailable

:too_many_requests

:execution_time_exceeded

error_message: String

type: :tool_search_tool_result_error

Accepts one of the following:

:tool_search_tool_result_error

class BetaToolSearchToolSearchResultBlock { tool_references, type }

tool_references: Array\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } \]

tool_name: String

type: :tool_reference

Accepts one of the following:

:tool_reference

type: :tool_search_tool_search_result

Accepts one of the following:

:tool_search_tool_search_result

tool_use_id: String

type: :tool_search_tool_result

Accepts one of the following:

:tool_search_tool_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash\[Symbol, untyped\]

name: String

The name of the MCP tool

server_name: String

The name of the MCP server

type: :mcp_tool_use

Accepts one of the following:

:mcp_tool_use

class BetaMCPToolResultBlock { content, is_error, tool_use_id, type }

content: String \| Array\[[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \]

Accepts one of the following:

String

Array\[[BetaTextBlock](/docs/en/api/beta#beta_text_block) { citations, text, type } \]

citations: Array\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class BetaCitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class BetaCitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class BetaCitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class BetaCitationSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

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

is_error: bool

tool_use_id: String

type: :mcp_tool_result

Accepts one of the following:

:mcp_tool_result

class BetaContainerUploadBlock { file_id, type }

Response model for a file uploaded to the container.

file_id: String

type: :container_upload

Accepts one of the following:

:container_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

Accepts one of the following:

:compaction

context_management: [BetaContextManagementResponse](/docs/en/api/beta#beta_context_management_response) { applied_edits }

Context management response.

Information about context management strategies applied during the request.

applied_edits: Array\[[BetaClearToolUses20250919EditResponse](/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type } \| [BetaClearThinking20251015EditResponse](/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } \]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared_input_tokens, cleared_tool_uses, type }

cleared_input_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear_tool_uses_20250919

The type of context management edit applied.

Accepts one of the following:

:clear_tool_uses_20250919

class BetaClearThinking20251015EditResponse { cleared_input_tokens, cleared_thinking_turns, type }

cleared_input_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear_thinking_20251015

The type of context management edit applied.

Accepts one of the following:

:clear_thinking_20251015

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

stop_reason: [BetaStopReason](/docs/en/api/beta#beta_stop_reason)

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

:compaction

:refusal

:model_context_window_exceeded

stop_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [BetaUsage](/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

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

iterations: Array\[[BetaMessageIterationUsage](/docs/en/api/beta#beta_message_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \| [BetaCompactionIterationUsage](/docs/en/api/beta#beta_compaction_iteration_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } \]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a sampling iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

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

input_tokens: Integer

The number of input tokens which were used.

minimum0

output_tokens: Integer

The number of output tokens which were used.

minimum0

type: :message

Usage for a sampling iteration

Accepts one of the following:

:message

class BetaCompactionIterationUsage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }

Token usage for a compaction iteration.

cache_creation: [BetaCacheCreation](/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

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

input_tokens: Integer

The number of input tokens which were used.

minimum0

output_tokens: Integer

The number of output tokens which were used.

minimum0

type: :compaction

Usage for a compaction iteration

Accepts one of the following:

:compaction

output_tokens: Integer

The number of output tokens which were used.

minimum0

server_tool_use: [BetaServerToolUsage](/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests }

The number of server tool requests.

web_fetch_requests: Integer

The number of web fetch tool requests.

minimum0

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

beta_message = anthropic.beta.messages.create(
  max_tokens: 1024,
  messages: [{content: "Hello, world", role: :user}],
  model: :"claude-opus-4-6"
)

puts(beta_message)
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
