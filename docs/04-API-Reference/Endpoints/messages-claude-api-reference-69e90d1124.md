---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:06:50Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/messages"
title: "Messages - Claude API Reference"
---

Copy page

TypeScript

# Messages

##### [Create a Message](/docs/en/api/messages/create)

client.messages.create(MessageCreateParamsbody, RequestOptionsoptions?): [Message](/docs/en/api/messages#message) { id, content, model, 5 more } \| Stream\<[RawMessageStreamEvent](/docs/en/api/messages#raw_message_stream_event)\>

post/v1/messages

##### [Count tokens in a Message](/docs/en/api/messages/count_tokens)

client.messages.countTokens(MessageCountTokensParams { messages, model, output_config, 4 more } body, RequestOptionsoptions?): [MessageTokensCount](/docs/en/api/messages#message_tokens_count) { input_tokens }

post/v1/messages/count_tokens

##### ModelsExpand Collapse 

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

CacheControlEphemeral { type, ttl }

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

CacheCreation { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsConfigParam { enabled }

enabled?: boolean

CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

type: "citations_delta"

Accepts one of the following:

"citations_delta"

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

ContentBlock = [TextBlock](/docs/en/api/messages#text_block) { citations, text, type } \| [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type } \| [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type } \| 3 more

Accepts one of the following:

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

ContentBlockParam = [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \| 7 more

Regular text content.

Accepts one of the following:

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

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

URLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "document"

Accepts one of the following:

"document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

ThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlockParam { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

Accepts one of the following:

"tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \>

Accepts one of the following:

string

Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

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

URLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "document"

Accepts one of the following:

"document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

is_error?: boolean

ServerToolUseBlockParam { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

WebSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

WebSearchToolRequestError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

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

ContentBlockSourceContent = [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control }

Accepts one of the following:

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

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

URLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "document"

Accepts one of the following:

"document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

InputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

Accepts one of the following:

"input_json_delta"

JSONOutputFormat { schema, type }

schema: Record\<string, unknown\>

The JSON schema of the format

type: "json_schema"

Accepts one of the following:

"json_schema"

Message { id, content, model, 5 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

MessageCountTokensTool = [Tool](/docs/en/api/messages#tool) { input_schema, name, cache_control, 4 more } \| [ToolBash20250124](/docs/en/api/messages#tool_bash_20250124) { name, type, cache_control, strict } \| [ToolTextEditor20250124](/docs/en/api/messages#tool_text_editor_20250124) { name, type, cache_control, strict } \| 3 more

Accepts one of the following:

Tool { input_schema, name, cache_control, 4 more }

input_schema: InputSchema { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

Accepts one of the following:

"object"

properties?: Record\<string, unknown\> \| null

required?: Array\<string\> \| null

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description?: string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming?: boolean \| null

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

type?: "custom" \| null

Accepts one of the following:

"custom"

ToolBash20250124 { name, type, cache_control, strict }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20250124"

Accepts one of the following:

"bash_20250124"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250124 { name, type, cache_control, strict }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20250124"

Accepts one of the following:

"text_editor_20250124"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250429 { name, type, cache_control, strict }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250429"

Accepts one of the following:

"text_editor_20250429"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250728 { name, type, cache_control, 2 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250728"

Accepts one of the following:

"text_editor_20250728"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_characters?: number \| null

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict?: boolean

When true, guarantees schema validation on tool names and inputs

WebSearchTool20250305 { name, type, allowed_domains, 5 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: "web_search_20250305"

Accepts one of the following:

"web_search_20250305"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: UserLocation \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

Accepts one of the following:

"approximate"

city?: string \| null

The city of the user.

maxLength255

minLength1

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region?: string \| null

The region of the user.

maxLength255

minLength1

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

MessageDeltaUsage { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: number \| null

The cumulative number of input tokens which were used.

minimum0

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

MessageParam { content, role }

content: string \| Array\<[ContentBlockParam](/docs/en/api/messages#content_block_param)\>

Accepts one of the following:

string

Array\<[ContentBlockParam](/docs/en/api/messages#content_block_param)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

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

URLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "document"

Accepts one of the following:

"document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

ThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlockParam { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

ToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

Accepts one of the following:

"tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \>

Accepts one of the following:

string

Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

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

URLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "document"

Accepts one of the following:

"document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

is_error?: boolean

ServerToolUseBlockParam { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

WebSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

WebSearchToolRequestError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

role: "user" \| "assistant"

Accepts one of the following:

"user"

"assistant"

MessageTokensCount { input_tokens }

input_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

Metadata { user_id }

user_id?: string \| null

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

Model = "claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more \| (string & {})

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

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

(string & {})

OutputConfig { effort, format }

effort?: "low" \| "medium" \| "high" \| "max" \| null

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format?: [JSONOutputFormat](/docs/en/api/messages#json_output_format) { schema, type } \| null

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: Record\<string, unknown\>

The JSON schema of the format

type: "json_schema"

Accepts one of the following:

"json_schema"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

RawContentBlockDelta = [TextDelta](/docs/en/api/messages#text_delta) { text, type } \| [InputJSONDelta](/docs/en/api/messages#input_json_delta) { partial_json, type } \| [CitationsDelta](/docs/en/api/messages#citations_delta) { citation, type } \| 2 more

Accepts one of the following:

TextDelta { text, type }

text: string

type: "text_delta"

Accepts one of the following:

"text_delta"

InputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

Accepts one of the following:

"input_json_delta"

CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

type: "citations_delta"

Accepts one of the following:

"citations_delta"

ThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Accepts one of the following:

"thinking_delta"

SignatureDelta { signature, type }

signature: string

type: "signature_delta"

Accepts one of the following:

"signature_delta"

RawContentBlockDeltaEvent { delta, index, type }

delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

TextDelta { text, type }

text: string

type: "text_delta"

Accepts one of the following:

"text_delta"

InputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

Accepts one of the following:

"input_json_delta"

CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

type: "citations_delta"

Accepts one of the following:

"citations_delta"

ThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Accepts one of the following:

"thinking_delta"

SignatureDelta { signature, type }

signature: string

type: "signature_delta"

Accepts one of the following:

"signature_delta"

index: number

type: "content_block_delta"

Accepts one of the following:

"content_block_delta"

RawContentBlockStartEvent { content_block, index, type }

content_block: [TextBlock](/docs/en/api/messages#text_block) { citations, text, type } \| [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type } \| [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type } \| 3 more

Accepts one of the following:

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

index: number

type: "content_block_start"

Accepts one of the following:

"content_block_start"

RawContentBlockStopEvent { index, type }

index: number

type: "content_block_stop"

Accepts one of the following:

"content_block_stop"

RawMessageDeltaEvent { delta, type, usage }

delta: Delta { stop_reason, stop_sequence }

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

type: "message_delta"

Accepts one of the following:

"message_delta"

usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: number \| null

The cumulative number of input tokens which were used.

minimum0

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

RawMessageStartEvent { message, type }

message: [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "message_start"

Accepts one of the following:

"message_start"

RawMessageStopEvent { type }

type: "message_stop"

Accepts one of the following:

"message_stop"

RawMessageStreamEvent = [RawMessageStartEvent](/docs/en/api/messages#raw_message_start_event) { message, type } \| [RawMessageDeltaEvent](/docs/en/api/messages#raw_message_delta_event) { delta, type, usage } \| [RawMessageStopEvent](/docs/en/api/messages#raw_message_stop_event) { type } \| 3 more

Accepts one of the following:

RawMessageStartEvent { message, type }

message: [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "message_start"

Accepts one of the following:

"message_start"

RawMessageDeltaEvent { delta, type, usage }

delta: Delta { stop_reason, stop_sequence }

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

type: "message_delta"

Accepts one of the following:

"message_delta"

usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number \| null

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: number \| null

The cumulative number of input tokens which were used.

minimum0

output_tokens: number

The cumulative number of output tokens which were used.

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

RawMessageStopEvent { type }

type: "message_stop"

Accepts one of the following:

"message_stop"

RawContentBlockStartEvent { content_block, index, type }

content_block: [TextBlock](/docs/en/api/messages#text_block) { citations, text, type } \| [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type } \| [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type } \| 3 more

Accepts one of the following:

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

index: number

type: "content_block_start"

Accepts one of the following:

"content_block_start"

RawContentBlockDeltaEvent { delta, index, type }

delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

TextDelta { text, type }

text: string

type: "text_delta"

Accepts one of the following:

"text_delta"

InputJSONDelta { partial_json, type }

partial_json: string

type: "input_json_delta"

Accepts one of the following:

"input_json_delta"

CitationsDelta { citation, type }

citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

type: "citations_delta"

Accepts one of the following:

"citations_delta"

ThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Accepts one of the following:

"thinking_delta"

SignatureDelta { signature, type }

signature: string

type: "signature_delta"

Accepts one of the following:

"signature_delta"

index: number

type: "content_block_delta"

Accepts one of the following:

"content_block_delta"

RawContentBlockStopEvent { index, type }

index: number

type: "content_block_stop"

Accepts one of the following:

"content_block_stop"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

RedactedThinkingBlockParam { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

ServerToolUsage { web_search_requests }

web_search_requests: number

The number of web search tool requests.

minimum0

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

ServerToolUseBlockParam { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

SignatureDelta { signature, type }

signature: string

type: "signature_delta"

Accepts one of the following:

"signature_delta"

StopReason = "end_turn" \| "max_tokens" \| "stop_sequence" \| 3 more

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

TextCitation = [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } \| [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } \| [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } \| 2 more

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

TextCitationParam = [CitationCharLocationParam](/docs/en/api/messages#citation_char_location_param) { cited_text, document_index, document_title, 3 more } \| [CitationPageLocationParam](/docs/en/api/messages#citation_page_location_param) { cited_text, document_index, document_title, 3 more } \| [CitationContentBlockLocationParam](/docs/en/api/messages#citation_content_block_location_param) { cited_text, document_index, document_title, 3 more } \| 2 more

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

TextDelta { text, type }

text: string

type: "text_delta"

Accepts one of the following:

"text_delta"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

ThinkingBlockParam { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

ThinkingConfigAdaptive { type }

type: "adaptive"

Accepts one of the following:

"adaptive"

ThinkingConfigDisabled { type }

type: "disabled"

Accepts one of the following:

"disabled"

ThinkingConfigEnabled { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

Accepts one of the following:

"enabled"

ThinkingConfigParam = [ThinkingConfigEnabled](/docs/en/api/messages#thinking_config_enabled) { budget_tokens, type } \| [ThinkingConfigDisabled](/docs/en/api/messages#thinking_config_disabled) { type } \| [ThinkingConfigAdaptive](/docs/en/api/messages#thinking_config_adaptive) { type }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

ThinkingConfigEnabled { budget_tokens, type }

budget_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"

Accepts one of the following:

"enabled"

ThinkingConfigDisabled { type }

type: "disabled"

Accepts one of the following:

"disabled"

ThinkingConfigAdaptive { type }

type: "adaptive"

Accepts one of the following:

"adaptive"

ThinkingDelta { thinking, type }

thinking: string

type: "thinking_delta"

Accepts one of the following:

"thinking_delta"

Tool { input_schema, name, cache_control, 4 more }

input_schema: InputSchema { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

Accepts one of the following:

"object"

properties?: Record\<string, unknown\> \| null

required?: Array\<string\> \| null

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description?: string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming?: boolean \| null

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

type?: "custom" \| null

Accepts one of the following:

"custom"

ToolBash20250124 { name, type, cache_control, strict }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20250124"

Accepts one of the following:

"bash_20250124"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolChoice = [ToolChoiceAuto](/docs/en/api/messages#tool_choice_auto) { type, disable_parallel_tool_use } \| [ToolChoiceAny](/docs/en/api/messages#tool_choice_any) { type, disable_parallel_tool_use } \| [ToolChoiceTool](/docs/en/api/messages#tool_choice_tool) { name, type, disable_parallel_tool_use } \| [ToolChoiceNone](/docs/en/api/messages#tool_choice_none) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

ToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

Accepts one of the following:

"auto"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

ToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

Accepts one of the following:

"any"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

Accepts one of the following:

"tool"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolChoiceNone { type }

The model will not be allowed to use tools.

type: "none"

Accepts one of the following:

"none"

ToolChoiceAny { type, disable_parallel_tool_use }

The model will use any available tools.

type: "any"

Accepts one of the following:

"any"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolChoiceAuto { type, disable_parallel_tool_use }

The model will automatically decide whether to use tools.

type: "auto"

Accepts one of the following:

"auto"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

ToolChoiceNone { type }

The model will not be allowed to use tools.

type: "none"

Accepts one of the following:

"none"

ToolChoiceTool { name, type, disable_parallel_tool_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

Accepts one of the following:

"tool"

disable_parallel_tool_use?: boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

ToolResultBlockParam { tool_use_id, type, cache_control, 2 more }

tool_use_id: string

type: "tool_result"

Accepts one of the following:

"tool_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content?: string \| Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \>

Accepts one of the following:

string

Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \| [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } \| [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } \| [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } \>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

SearchResultBlockParam { content, source, title, 3 more }

content: Array\<[TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } \>

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

source: string

title: string

type: "search_result"

Accepts one of the following:

"search_result"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }

enabled?: boolean

DocumentBlockParam { source, type, cache_control, 3 more }

source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } \| [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } \| [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } \| [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }

Accepts one of the following:

Base64PDFSource { data, media_type, type }

data: string

media_type: "application/pdf"

Accepts one of the following:

"application/pdf"

type: "base64"

Accepts one of the following:

"base64"

PlainTextSource { data, media_type, type }

data: string

media_type: "text/plain"

Accepts one of the following:

"text/plain"

type: "text"

Accepts one of the following:

"text"

ContentBlockSource { content, type }

content: string \| Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

Accepts one of the following:

string

Array\<[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\>

TextBlockParam { text, type, cache_control, citations }

text: string

type: "text"

Accepts one of the following:

"text"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: Array\<[TextCitationParam](/docs/en/api/messages#text_citation_param)\> \| null

Accepts one of the following:

CitationCharLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocationParam { cited_text, document_index, document_title, 3 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationWebSearchResultLocationParam { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationSearchResultLocationParam { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

ImageBlockParam { source, type, cache_control }

source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } \| [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }

Accepts one of the following:

Base64ImageSource { data, media_type, type }

data: string

media_type: "image/jpeg" \| "image/png" \| "image/gif" \| "image/webp"

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

Accepts one of the following:

"base64"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "image"

Accepts one of the following:

"image"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

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

URLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

type: "document"

Accepts one of the following:

"document"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations?: [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled } \| null

enabled?: boolean

context?: string \| null

title?: string \| null

is_error?: boolean

ToolTextEditor20250124 { name, type, cache_control, strict }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20250124"

Accepts one of the following:

"text_editor_20250124"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250429 { name, type, cache_control, strict }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250429"

Accepts one of the following:

"text_editor_20250429"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250728 { name, type, cache_control, 2 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250728"

Accepts one of the following:

"text_editor_20250728"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_characters?: number \| null

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolUnion = [Tool](/docs/en/api/messages#tool) { input_schema, name, cache_control, 4 more } \| [ToolBash20250124](/docs/en/api/messages#tool_bash_20250124) { name, type, cache_control, strict } \| [ToolTextEditor20250124](/docs/en/api/messages#tool_text_editor_20250124) { name, type, cache_control, strict } \| 3 more

Accepts one of the following:

Tool { input_schema, name, cache_control, 4 more }

input_schema: InputSchema { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

Accepts one of the following:

"object"

properties?: Record\<string, unknown\> \| null

required?: Array\<string\> \| null

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description?: string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming?: boolean \| null

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict?: boolean

When true, guarantees schema validation on tool names and inputs

type?: "custom" \| null

Accepts one of the following:

"custom"

ToolBash20250124 { name, type, cache_control, strict }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: "bash_20250124"

Accepts one of the following:

"bash_20250124"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250124 { name, type, cache_control, strict }

name: "str_replace_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: "text_editor_20250124"

Accepts one of the following:

"text_editor_20250124"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250429 { name, type, cache_control, strict }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250429"

Accepts one of the following:

"text_editor_20250429"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict?: boolean

When true, guarantees schema validation on tool names and inputs

ToolTextEditor20250728 { name, type, cache_control, 2 more }

name: "str_replace_based_edit_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: "text_editor_20250728"

Accepts one of the following:

"text_editor_20250728"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_characters?: number \| null

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict?: boolean

When true, guarantees schema validation on tool names and inputs

WebSearchTool20250305 { name, type, allowed_domains, 5 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: "web_search_20250305"

Accepts one of the following:

"web_search_20250305"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: UserLocation \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

Accepts one of the following:

"approximate"

city?: string \| null

The city of the user.

maxLength255

minLength1

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region?: string \| null

The region of the user.

maxLength255

minLength1

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ToolUseBlockParam { id, input, name, 2 more }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

URLImageSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

URLPDFSource { type, url }

type: "url"

Accepts one of the following:

"url"

url: string

Usage { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

WebSearchResultBlock { encrypted_content, page_age, title, 2 more }

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

WebSearchResultBlockParam { encrypted_content, title, type, 2 more }

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

WebSearchTool20250305 { name, type, allowed_domains, 5 more }

name: "web_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: "web_search_20250305"

Accepts one of the following:

"web_search_20250305"

allowed_domains?: Array\<string\> \| null

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains?: Array\<string\> \| null

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_uses?: number \| null

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict?: boolean

When true, guarantees schema validation on tool names and inputs

user_location?: UserLocation \| null

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

Accepts one of the following:

"approximate"

city?: string \| null

The city of the user.

maxLength255

minLength1

country?: string \| null

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region?: string \| null

The region of the user.

maxLength255

minLength1

timezone?: string \| null

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

WebSearchToolRequestError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

WebSearchToolResultBlockContent = [WebSearchToolResultError](/docs/en/api/messages#web_search_tool_result_error) { error_code, type } \| Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

WebSearchToolResultBlockParam { content, tool_use_id, type, cache_control }

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

WebSearchToolRequestError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

cache_control?: [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl } \| null

Create a cache control breakpoint at this content block.

type: "ephemeral"

Accepts one of the following:

"ephemeral"

ttl?: "5m" \| "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

WebSearchToolResultBlockParamContent = Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \> \| [WebSearchToolRequestError](/docs/en/api/messages#web_search_tool_request_error) { error_code, type }

Accepts one of the following:

Array\<[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } \>

encrypted_content: string

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

page_age?: string \| null

WebSearchToolRequestError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

client.messages.batches.create(BatchCreateParams { requests } body, RequestOptionsoptions?): [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

client.messages.batches.retrieve(stringmessageBatchID, RequestOptionsoptions?): [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

client.messages.batches.list(BatchListParams { after_id, before_id, limit } query?, RequestOptionsoptions?): Page\<[MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more } \>

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

client.messages.batches.cancel(stringmessageBatchID, RequestOptionsoptions?): [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

client.messages.batches.delete(stringmessageBatchID, RequestOptionsoptions?): [DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch) { id, type }

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

client.messages.batches.results(stringmessageBatchID, RequestOptionsoptions?): [MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response) { custom_id, result } \| Stream\<[MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response) { custom_id, result } \>

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

DeletedMessageBatch { id, type }

id: string

ID of the Message Batch.

type: "message_batch_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

"message_batch_deleted"

MessageBatch { id, archived_at, cancel_initiated_at, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

archived_at: string \| null

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel_initiated_at: string \| null

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended_at: string \| null

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processing_status: "in_progress" \| "canceling" \| "ended"

Processing status of the Message Batch.

Accepts one of the following:

"in_progress"

"canceling"

"ended"

request_counts: [MessageBatchRequestCounts](/docs/en/api/messages#message_batch_request_counts) { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results_url: string \| null

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: "message_batch"

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

"message_batch"

MessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

InvalidRequestError { message, type }

message: string

type: "invalid_request_error"

Accepts one of the following:

"invalid_request_error"

AuthenticationError { message, type }

message: string

type: "authentication_error"

Accepts one of the following:

"authentication_error"

BillingError { message, type }

message: string

type: "billing_error"

Accepts one of the following:

"billing_error"

PermissionError { message, type }

message: string

type: "permission_error"

Accepts one of the following:

"permission_error"

NotFoundError { message, type }

message: string

type: "not_found_error"

Accepts one of the following:

"not_found_error"

RateLimitError { message, type }

message: string

type: "rate_limit_error"

Accepts one of the following:

"rate_limit_error"

GatewayTimeoutError { message, type }

message: string

type: "timeout_error"

Accepts one of the following:

"timeout_error"

APIErrorObject { message, type }

message: string

type: "api_error"

Accepts one of the following:

"api_error"

OverloadedError { message, type }

message: string

type: "overloaded_error"

Accepts one of the following:

"overloaded_error"

request_id: string \| null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

MessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

MessageBatchIndividualResponse { custom_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [MessageBatchResult](/docs/en/api/messages#message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

Accepts one of the following:

"succeeded"

MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

InvalidRequestError { message, type }

message: string

type: "invalid_request_error"

Accepts one of the following:

"invalid_request_error"

AuthenticationError { message, type }

message: string

type: "authentication_error"

Accepts one of the following:

"authentication_error"

BillingError { message, type }

message: string

type: "billing_error"

Accepts one of the following:

"billing_error"

PermissionError { message, type }

message: string

type: "permission_error"

Accepts one of the following:

"permission_error"

NotFoundError { message, type }

message: string

type: "not_found_error"

Accepts one of the following:

"not_found_error"

RateLimitError { message, type }

message: string

type: "rate_limit_error"

Accepts one of the following:

"rate_limit_error"

GatewayTimeoutError { message, type }

message: string

type: "timeout_error"

Accepts one of the following:

"timeout_error"

APIErrorObject { message, type }

message: string

type: "api_error"

Accepts one of the following:

"api_error"

OverloadedError { message, type }

message: string

type: "overloaded_error"

Accepts one of the following:

"overloaded_error"

request_id: string \| null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

MessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

MessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

MessageBatchRequestCounts { canceled, errored, expired, 2 more }

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

MessageBatchResult = [MessageBatchSucceededResult](/docs/en/api/messages#message_batch_succeeded_result) { message, type } \| [MessageBatchErroredResult](/docs/en/api/messages#message_batch_errored_result) { error, type } \| [MessageBatchCanceledResult](/docs/en/api/messages#message_batch_canceled_result) { type } \| [MessageBatchExpiredResult](/docs/en/api/messages#message_batch_expired_result) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

Accepts one of the following:

"succeeded"

MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

InvalidRequestError { message, type }

message: string

type: "invalid_request_error"

Accepts one of the following:

"invalid_request_error"

AuthenticationError { message, type }

message: string

type: "authentication_error"

Accepts one of the following:

"authentication_error"

BillingError { message, type }

message: string

type: "billing_error"

Accepts one of the following:

"billing_error"

PermissionError { message, type }

message: string

type: "permission_error"

Accepts one of the following:

"permission_error"

NotFoundError { message, type }

message: string

type: "not_found_error"

Accepts one of the following:

"not_found_error"

RateLimitError { message, type }

message: string

type: "rate_limit_error"

Accepts one of the following:

"rate_limit_error"

GatewayTimeoutError { message, type }

message: string

type: "timeout_error"

Accepts one of the following:

"timeout_error"

APIErrorObject { message, type }

message: string

type: "api_error"

Accepts one of the following:

"api_error"

OverloadedError { message, type }

message: string

type: "overloaded_error"

Accepts one of the following:

"overloaded_error"

request_id: string \| null

type: "error"

Accepts one of the following:

"error"

type: "errored"

Accepts one of the following:

"errored"

MessageBatchCanceledResult { type }

type: "canceled"

Accepts one of the following:

"canceled"

MessageBatchExpiredResult { type }

type: "expired"

Accepts one of the following:

"expired"

MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

content: Array\<[ContentBlock](/docs/en/api/messages#content_block)\>

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

TextBlock { citations, text, type }

citations: Array\<[TextCitation](/docs/en/api/messages#text_citation)\> \| null

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_char_index: number

file_id: string \| null

start_char_index: number

type: "char_location"

Accepts one of the following:

"char_location"

CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_page_number: number

file_id: string \| null

start_page_number: number

type: "page_location"

Accepts one of the following:

"page_location"

CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: string

document_index: number

document_title: string \| null

end_block_index: number

file_id: string \| null

start_block_index: number

type: "content_block_location"

Accepts one of the following:

"content_block_location"

CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: string

encrypted_index: string

title: string \| null

type: "web_search_result_location"

Accepts one of the following:

"web_search_result_location"

url: string

CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: string

end_block_index: number

search_result_index: number

source: string

start_block_index: number

title: string \| null

type: "search_result_location"

Accepts one of the following:

"search_result_location"

text: string

type: "text"

Accepts one of the following:

"text"

ThinkingBlock { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

Accepts one of the following:

"thinking"

RedactedThinkingBlock { data, type }

data: string

type: "redacted_thinking"

Accepts one of the following:

"redacted_thinking"

ToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: string

type: "tool_use"

Accepts one of the following:

"tool_use"

ServerToolUseBlock { id, input, name, type }

id: string

input: Record\<string, unknown\>

name: "web_search"

Accepts one of the following:

"web_search"

type: "server_tool_use"

Accepts one of the following:

"server_tool_use"

WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

WebSearchToolResultError { error_code, type }

error_code: "invalid_tool_input" \| "unavailable" \| "max_uses_exceeded" \| 3 more

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

Array\<[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \>

encrypted_content: string

page_age: string \| null

title: string

type: "web_search_result"

Accepts one of the following:

"web_search_result"

url: string

tool_use_id: string

type: "web_search_tool_result"

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" \| "claude-opus-4-5-20251101" \| "claude-opus-4-5" \| 18 more

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

(string & {})

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: [StopReason](/docs/en/api/messages#stop_reason) \| null

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

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: string \| null

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } \| null

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: number \| null

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: number \| null

The number of input tokens read from the cache.

minimum0

inference_geo: string \| null

The geographic region where inference was performed for this request.

input_tokens: number

The number of input tokens which were used.

minimum0

output_tokens: number

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests } \| null

The number of server tool requests.

web_search_requests: number

The number of web search tool requests.

minimum0

service_tier: "standard" \| "priority" \| "batch" \| null

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: "succeeded"

Accepts one of the following:

"succeeded"

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
