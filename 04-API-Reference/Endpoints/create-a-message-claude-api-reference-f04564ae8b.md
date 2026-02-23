---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:39:08Z"
source_url: "https://platform.claude.com/docs/en/api/python/messages/create"
title: "Create a Message - Claude API Reference"
---

Copy page

Python

# Create a Message

messages.create(MessageCreateParams\*\*kwargs) -\> [Message](/docs/en/api/messages#message)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

##### ParametersExpand Collapse 

max_tokens: int

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

messages: [Iterable](/docs/en/api/messages/create)\[[MessageParam](/docs/en/api/messages#message_param)\]

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

content: Union\[str, List\[Union\[[TextBlockParam](/docs/en/api/messages#text_block_param), [ImageBlockParam](/docs/en/api/messages#image_block_param), [DocumentBlockParam](/docs/en/api/messages#document_block_param), 14 more\]\]\]

Accepts one of the following:

str

List\[Union\[[TextBlockParam](/docs/en/api/messages#text_block_param), [ImageBlockParam](/docs/en/api/messages#image_block_param), [DocumentBlockParam](/docs/en/api/messages#document_block_param), 14 more\]\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]\]

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

class URLImageSource: …

type: Literal\["url"\]

url: str

type: Literal\["image"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class DocumentBlockParam: …

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

str

List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]\]

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

class URLImageSource: …

type: Literal\["url"\]

url: str

type: Literal\["image"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

class URLPDFSource: …

type: Literal\["url"\]

url: str

type: Literal\["document"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[CitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class SearchResultBlockParam: …

content: List\[[TextBlockParam](/docs/en/api/messages#text_block_param)\]

text: str

type: Literal\["text"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]\]

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

source: str

title: str

type: Literal\["search_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[CitationsConfigParam\]

enabled: Optional\[bool\]

class ThinkingBlockParam: …

signature: str

thinking: str

type: Literal\["thinking"\]

class RedactedThinkingBlockParam: …

data: str

type: Literal\["redacted_thinking"\]

class ToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class ToolResultBlockParam: …

tool_use_id: str

type: Literal\["tool_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional\[Union\[str, List\[Content\], null\]\]

Accepts one of the following:

str

List\[Content\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]\]

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

class URLImageSource: …

type: Literal\["url"\]

url: str

type: Literal\["image"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class SearchResultBlockParam: …

content: List\[[TextBlockParam](/docs/en/api/messages#text_block_param)\]

text: str

type: Literal\["text"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]\]

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

source: str

title: str

type: Literal\["search_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[CitationsConfigParam\]

enabled: Optional\[bool\]

class DocumentBlockParam: …

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

str

List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]\]

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

class URLImageSource: …

type: Literal\["url"\]

url: str

type: Literal\["image"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

class URLPDFSource: …

type: Literal\["url"\]

url: str

type: Literal\["document"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[CitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class ToolReferenceBlockParam: …

Tool reference block that can be included in tool_result content.

tool_name: str

type: Literal\["tool_reference"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error: Optional\[bool\]

class ServerToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

List\[[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

url: str

page_age: Optional\[str\]

class WebSearchToolRequestError: …

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

tool_use_id: str

type: Literal\["web_search_tool_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class WebFetchToolResultBlockParam: …

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlockParam: …

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

class WebFetchBlockParam: …

content: [DocumentBlockParam](/docs/en/api/messages#document_block_param)

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

str

List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]\]

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

class URLImageSource: …

type: Literal\["url"\]

url: str

type: Literal\["image"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

class URLPDFSource: …

type: Literal\["url"\]

url: str

type: Literal\["document"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[CitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

type: Literal\["web_fetch_result"\]

url: str

Fetched content URL

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

class CodeExecutionToolResultBlockParam: …

content: [CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam: …

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

class CodeExecutionResultBlockParam: …

content: List\[[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\]

file_id: str

type: Literal\["code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

class EncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web_search results.

content: List\[[CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param)\]

file_id: str

type: Literal\["code_execution_output"\]

encrypted_stdout: str

return_code: int

stderr: str

type: Literal\["encrypted_code_execution_result"\]

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BashCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam: …

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

class BashCodeExecutionResultBlockParam: …

content: List\[[BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class TextEditorCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam: …

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: Literal\["text_editor_code_execution_tool_result_error"\]

error_message: Optional\[str\]

class TextEditorCodeExecutionViewResultBlockParam: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal\["text_editor_code_execution_view_result"\]

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

class TextEditorCodeExecutionCreateResultBlockParam: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

class TextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal\["text_editor_code_execution_str_replace_result"\]

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ToolSearchToolResultBlockParam: …

content: Content

Accepts one of the following:

class ToolSearchToolResultErrorParam: …

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["tool_search_tool_result_error"\]

class ToolSearchToolSearchResultBlockParam: …

tool_references: List\[[ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param)\]

tool_name: str

type: Literal\["tool_reference"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["tool_search_tool_search_result"\]

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: str

type: Literal\["container_upload"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

role: Literal\["user", "assistant"\]

Accepts one of the following:

"user"

"assistant"

model: [ModelParam](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal\["claude-opus-4-6", "claude-sonnet-4-6", "claude-opus-4-5-20251101", 19 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Frontier intelligence at scale — built for coding, agents, and enterprise workflows
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

str

cache_control: Optional\[CacheControlEphemeralParam\]

Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

container: Optional\[str\]

Container identifier for reuse across requests.

inference_geo: Optional\[str\]

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

metadata: Optional\[[MetadataParam](/docs/en/api/messages#metadata)\]

An object describing metadata about the request.

user_id: Optional\[str\]

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

output_config: Optional\[[OutputConfigParam](/docs/en/api/messages#output_config)\]

Configuration options for the model's output, such as the output format.

effort: Optional\[Literal\["low", "medium", "high", "max"\]\]

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format: Optional\[JSONOutputFormat\]

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: Dict\[str, object\]

The JSON schema of the format

type: Literal\["json_schema"\]

service_tier: Optional\[Literal\["auto", "standard_only"\]\]

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

Accepts one of the following:

"auto"

"standard_only"

stop_sequences: Optional\[[SequenceNotStr](/docs/en/api/messages/create)\[str\]\]

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

stream: Optional\[Literal\[false\]\]

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

system: Optional\[Union\[str, Iterable\[[TextBlockParam](/docs/en/api/messages#text_block_param)\]\]\]

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

str

Iterable\[[TextBlockParam](/docs/en/api/messages#text_block_param)\]

text: str

type: Literal\["text"\]

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[TextCitationParam](/docs/en/api/messages#text_citation_param)\]\]

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

temperature: Optional\[float\]

Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

thinking: Optional\[[ThinkingConfigParam](/docs/en/api/messages#thinking_config_param)\]

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class ThinkingConfigEnabled: …

budget_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: Literal\["enabled"\]

class ThinkingConfigDisabled: …

type: Literal\["disabled"\]

class ThinkingConfigAdaptive: …

type: Literal\["adaptive"\]

tool_choice: Optional\[[ToolChoiceParam](/docs/en/api/messages#tool_choice)\]

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class ToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal\["auto"\]

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny: …

The model will use any available tools.

type: Literal\["any"\]

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal\["tool"\]

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal\["none"\]

tools: Optional\[[Iterable](/docs/en/api/messages/create)\[[ToolUnionParam](/docs/en/api/messages#tool_union)\]\]

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

class Tool: …

input_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal\["object"\]

properties: Optional\[Dict\[str, object\]\]

required: Optional\[List\[str\]\]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description: Optional\[str\]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: Optional\[bool\]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

type: Optional\[Literal\["custom"\]\]

class ToolBash20250124: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["bash_20250124"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250522: …

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["code_execution_20250522"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250825: …

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["code_execution_20250825"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20260120: …

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["code_execution_20260120"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class MemoryTool20250818: …

name: Literal\["memory"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["memory_20250818"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["text_editor_20250124"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["text_editor_20250429"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["text_editor_20250728"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

max_characters: Optional\[int\]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305: …

name: Literal\["web_search"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["web_search_20250305"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: Optional\[List\[str\]\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Optional\[List\[str\]\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

user_location: Optional\[UserLocation\]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal\["approximate"\]

city: Optional\[str\]

The city of the user.

country: Optional\[str\]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional\[str\]

The region of the user.

timezone: Optional\[str\]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20250910: …

name: Literal\["web_fetch"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["web_fetch_20250910"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: Optional\[List\[str\]\]

List of domains to allow fetching from

blocked_domains: Optional\[List\[str\]\]

List of domains to block fetching from

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[CitationsConfigParam\]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional\[bool\]

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: Optional\[int\]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20260209: …

name: Literal\["web_search"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["web_search_20260209"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: Optional\[List\[str\]\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Optional\[List\[str\]\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

user_location: Optional\[UserLocation\]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal\["approximate"\]

city: Optional\[str\]

The city of the user.

country: Optional\[str\]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional\[str\]

The region of the user.

timezone: Optional\[str\]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20260209: …

name: Literal\["web_fetch"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["web_fetch_20260209"\]

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

allowed_domains: Optional\[List\[str\]\]

List of domains to allow fetching from

blocked_domains: Optional\[List\[str\]\]

List of domains to block fetching from

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[CitationsConfigParam\]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional\[bool\]

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: Optional\[int\]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolBm25_20251119: …

name: Literal\["tool_search_tool_bm25"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["tool_search_tool_bm25_20251119", "tool_search_tool_bm25"\]

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolRegex20251119: …

name: Literal\["tool_search_tool_regex"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal\["tool_search_tool_regex_20251119", "tool_search_tool_regex"\]

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825", "code_execution_20260120"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

"code_execution_20260120"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

top_k: Optional\[int\]

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

top_p: Optional\[float\]

Use nucleus sampling.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

maximum1

minimum0

##### ReturnsExpand Collapse 

class Message: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[Container\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

content: List\[[ContentBlock](/docs/en/api/messages#content_block)\]

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

class TextBlock: …

citations: Optional\[List\[[TextCitation](/docs/en/api/messages#text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

class WebFetchBlock: …

content: [DocumentBlock](/docs/en/api/messages#document_block)

citations: Optional\[CitationsConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

class CodeExecutionResultBlock: …

content: List\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web_search results.

content: List\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

encrypted_stdout: str

return_code: int

stderr: str

type: Literal\["encrypted_code_execution_result"\]

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

class BashCodeExecutionResultBlock: …

content: List\[[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

class TextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

class ToolSearchToolSearchResultBlock: …

tool_references: List\[[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

type: Literal\["tool_search_tool_search_result"\]

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal\["claude-opus-4-6", "claude-sonnet-4-6", "claude-opus-4-5-20251101", 19 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Frontier intelligence at scale — built for coding, agents, and enterprise workflows
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: Optional\[StopReason\]

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

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

usage: [Usage](/docs/en/api/messages#usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[CacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

output_tokens: int

The number of output tokens which were used.

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

web_search_requests: int

The number of web search tool requests.

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

[RawMessageStreamEvent](/docs/en/api/messages#raw_message_stream_event)

Accepts one of the following:

class RawMessageStartEvent: …

message: [Message](/docs/en/api/messages#message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[Container\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

content: List\[[ContentBlock](/docs/en/api/messages#content_block)\]

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

class TextBlock: …

citations: Optional\[List\[[TextCitation](/docs/en/api/messages#text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

class WebFetchBlock: …

content: [DocumentBlock](/docs/en/api/messages#document_block)

citations: Optional\[CitationsConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

class CodeExecutionResultBlock: …

content: List\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web_search results.

content: List\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

encrypted_stdout: str

return_code: int

stderr: str

type: Literal\["encrypted_code_execution_result"\]

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

class BashCodeExecutionResultBlock: …

content: List\[[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

class TextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

class ToolSearchToolSearchResultBlock: …

tool_references: List\[[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

type: Literal\["tool_search_tool_search_result"\]

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal\["claude-opus-4-6", "claude-sonnet-4-6", "claude-opus-4-5-20251101", 19 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Frontier intelligence at scale — built for coding, agents, and enterprise workflows
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Frontier intelligence at scale — built for coding, agents, and enterprise workflows

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

str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

stop_reason: Optional\[StopReason\]

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

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

usage: [Usage](/docs/en/api/messages#usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[CacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

output_tokens: int

The number of output tokens which were used.

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

web_search_requests: int

The number of web search tool requests.

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["message_start"\]

class RawMessageDeltaEvent: …

delta: Delta

container: Optional\[Container\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

stop_reason: Optional\[StopReason\]

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

stop_sequence: Optional\[str\]

type: Literal\["message_delta"\]

usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: Optional\[int\]

The cumulative number of input tokens used to create the cache entry.

cache_read_input_tokens: Optional\[int\]

The cumulative number of input tokens read from the cache.

input_tokens: Optional\[int\]

The cumulative number of input tokens which were used.

output_tokens: int

The cumulative number of output tokens which were used.

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

web_search_requests: int

The number of web search tool requests.

class RawMessageStopEvent: …

type: Literal\["message_stop"\]

class RawContentBlockStartEvent: …

content_block: ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class TextBlock: …

citations: Optional\[List\[[TextCitation](/docs/en/api/messages#text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

text: str

type: Literal\["text"\]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

class ServerToolCaller20260120: …

tool_id: str

type: Literal\["code_execution_20260120"\]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

class WebFetchBlock: …

content: [DocumentBlock](/docs/en/api/messages#document_block)

citations: Optional\[CitationsConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

type: Literal\["base64"\]

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

type: Literal\["text"\]

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)

Code execution result with encrypted stdout for PFC + web_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

class CodeExecutionResultBlock: …

content: List\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web_search results.

content: List\[[CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

encrypted_stdout: str

return_code: int

stderr: str

type: Literal\["encrypted_code_execution_result"\]

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

class BashCodeExecutionResultBlock: …

content: List\[[BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

class TextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

class ToolSearchToolSearchResultBlock: …

tool_references: List\[[ToolReferenceBlock](/docs/en/api/messages#tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

type: Literal\["tool_search_tool_search_result"\]

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

index: int

type: Literal\["content_block_start"\]

class RawContentBlockDeltaEvent: …

delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal\["text_delta"\]

class InputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

class CitationsDelta: …

citation: Citation

Accepts one of the following:

class CitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

type: Literal\["citations_delta"\]

class ThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

class SignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

index: int

type: Literal\["content_block_delta"\]

class RawContentBlockStopEvent: …

index: int

type: Literal\["content_block_stop"\]

Create a Message

Python

``` shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
message = client.messages.create(
    max_tokens=1024,
    messages=[{
        "content": "Hello, world",
        "role": "user",
    }],
    model="claude-opus-4-6",
)
print(message.id)
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
