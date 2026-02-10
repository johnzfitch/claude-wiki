---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:07:37Z"
source_url: "https://platform.claude.com/docs/en/api/python/messages"
title: "Messages - Claude API Reference"
---

Copy page

Python

# Messages

##### [Create a Message](/docs/en/api/messages/create)

messages.create(MessageCreateParams\*\*kwargs) -\> [Message](/docs/en/api/messages#message)

post/v1/messages

##### [Count tokens in a Message](/docs/en/api/messages/count_tokens)

messages.count_tokens(MessageCountTokensParams\*\*kwargs) -\> [MessageTokensCount](/docs/en/api/messages#message_tokens_count)

post/v1/messages/count_tokens

##### ModelsExpand Collapse 

class Base64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class Base64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class CacheControlEphemeral: …

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class CacheCreation: …

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

class CitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsConfigParam: …

enabled: Optional\[bool\]

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

type: Literal\["citations_delta"\]

Accepts one of the following:

"citations_delta"

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

ContentBlock = [ContentBlock](/docs/en/api/messages#content_block)

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

ContentBlockParam = Union\[[TextBlockParam](/docs/en/api/messages#text_block_param), [ImageBlockParam](/docs/en/api/messages#image_block_param), [DocumentBlockParam](/docs/en/api/messages#document_block_param), 7 more\]

Regular text content.

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"thinking"

class RedactedThinkingBlockParam: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ToolResultBlockParam: …

tool_use_id: str

type: Literal\["tool_result"\]

Accepts one of the following:

"tool_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

ContentUnionMember0 = str

Content = List\[Content\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

is_error: Optional\[bool\]

class ServerToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

WebSearchToolResultBlockItem = List\[[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class WebSearchToolRequestError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

ContentBlockSourceContent = [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class InputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

Accepts one of the following:

"input_json_delta"

class JSONOutputFormat: …

schema: Dict\[str, object\]

The JSON schema of the format

type: Literal\["json_schema"\]

Accepts one of the following:

"json_schema"

class Message: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
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

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

MessageCountTokensTool = [MessageCountTokensTool](/docs/en/api/messages#message_count_tokens_tool)

Accepts one of the following:

class Tool: …

input_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal\["object"\]

Accepts one of the following:

"object"

properties: Optional\[Dict\[str, object\]\]

required: Optional\[List\[str\]\]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description: Optional\[str\]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: Optional\[bool\]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

type: Optional\[Literal\["custom"\]\]

Accepts one of the following:

"custom"

class ToolBash20250124: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20250124"\]

Accepts one of the following:

"bash_20250124"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20250124"\]

Accepts one of the following:

"text_editor_20250124"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250429"\]

Accepts one of the following:

"text_editor_20250429"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250728"\]

Accepts one of the following:

"text_editor_20250728"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_characters: Optional\[int\]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305: …

name: Literal\["web_search"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: Literal\["web_search_20250305"\]

Accepts one of the following:

"web_search_20250305"

allowed_domains: Optional\[List\[str\]\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Optional\[List\[str\]\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

user_location: Optional\[UserLocation\]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal\["approximate"\]

Accepts one of the following:

"approximate"

city: Optional\[str\]

The city of the user.

maxLength255

minLength1

country: Optional\[str\]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional\[str\]

The region of the user.

maxLength255

minLength1

timezone: Optional\[str\]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class MessageDeltaUsage: …

cache_creation_input_tokens: Optional\[int\]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: Optional\[int\]

The cumulative number of input tokens which were used.

minimum0

output_tokens: int

The cumulative number of output tokens which were used.

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

class MessageParam: …

content: Union\[str, List\[Union\[[TextBlockParam](/docs/en/api/messages#text_block_param), [ImageBlockParam](/docs/en/api/messages#image_block_param), [DocumentBlockParam](/docs/en/api/messages#document_block_param), 8 more\]\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentUnionMember1 = List\[Union\[[TextBlockParam](/docs/en/api/messages#text_block_param), [ImageBlockParam](/docs/en/api/messages#image_block_param), [DocumentBlockParam](/docs/en/api/messages#document_block_param), 8 more\]\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"thinking"

class RedactedThinkingBlockParam: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ToolResultBlockParam: …

tool_use_id: str

type: Literal\["tool_result"\]

Accepts one of the following:

"tool_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

ContentUnionMember0 = str

Content = List\[Content\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

is_error: Optional\[bool\]

class ServerToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

WebSearchToolResultBlockItem = List\[[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class WebSearchToolRequestError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

class MessageTokensCount: …

input_tokens: int

The total number of tokens across the provided list of messages, system prompt, and tools.

class Metadata: …

user_id: Optional\[str\]

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

Model = Union\[Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\], str\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
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

UnionMember1 = str

class OutputConfig: …

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

Accepts one of the following:

"json_schema"

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

RawContentBlockDelta = [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal\["text_delta"\]

Accepts one of the following:

"text_delta"

class InputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

Accepts one of the following:

"input_json_delta"

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

type: Literal\["citations_delta"\]

Accepts one of the following:

"citations_delta"

class ThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

Accepts one of the following:

"thinking_delta"

class SignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

Accepts one of the following:

"signature_delta"

class RawContentBlockDeltaEvent: …

delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal\["text_delta"\]

Accepts one of the following:

"text_delta"

class InputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

Accepts one of the following:

"input_json_delta"

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

type: Literal\["citations_delta"\]

Accepts one of the following:

"citations_delta"

class ThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

Accepts one of the following:

"thinking_delta"

class SignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

Accepts one of the following:

"signature_delta"

index: int

type: Literal\["content_block_delta"\]

Accepts one of the following:

"content_block_delta"

class RawContentBlockStartEvent: …

content_block: ContentBlock

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

index: int

type: Literal\["content_block_start"\]

Accepts one of the following:

"content_block_start"

class RawContentBlockStopEvent: …

index: int

type: Literal\["content_block_stop"\]

Accepts one of the following:

"content_block_stop"

class RawMessageDeltaEvent: …

delta: Delta

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

Accepts one of the following:

"message_delta"

usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: Optional\[int\]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: Optional\[int\]

The cumulative number of input tokens which were used.

minimum0

output_tokens: int

The cumulative number of output tokens which were used.

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

class RawMessageStartEvent: …

message: [Message](/docs/en/api/messages#message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
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

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["message_start"\]

Accepts one of the following:

"message_start"

class RawMessageStopEvent: …

type: Literal\["message_stop"\]

Accepts one of the following:

"message_stop"

RawMessageStreamEvent = [RawMessageStreamEvent](/docs/en/api/messages#raw_message_stream_event)

Accepts one of the following:

class RawMessageStartEvent: …

message: [Message](/docs/en/api/messages#message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
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

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["message_start"\]

Accepts one of the following:

"message_start"

class RawMessageDeltaEvent: …

delta: Delta

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

Accepts one of the following:

"message_delta"

usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: Optional\[int\]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: Optional\[int\]

The cumulative number of input tokens which were used.

minimum0

output_tokens: int

The cumulative number of output tokens which were used.

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

class RawMessageStopEvent: …

type: Literal\["message_stop"\]

Accepts one of the following:

"message_stop"

class RawContentBlockStartEvent: …

content_block: ContentBlock

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

index: int

type: Literal\["content_block_start"\]

Accepts one of the following:

"content_block_start"

class RawContentBlockDeltaEvent: …

delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal\["text_delta"\]

Accepts one of the following:

"text_delta"

class InputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

Accepts one of the following:

"input_json_delta"

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

type: Literal\["citations_delta"\]

Accepts one of the following:

"citations_delta"

class ThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

Accepts one of the following:

"thinking_delta"

class SignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

Accepts one of the following:

"signature_delta"

index: int

type: Literal\["content_block_delta"\]

Accepts one of the following:

"content_block_delta"

class RawContentBlockStopEvent: …

index: int

type: Literal\["content_block_stop"\]

Accepts one of the following:

"content_block_stop"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class RedactedThinkingBlockParam: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class SearchResultBlockParam: …

content: List\[[TextBlockParam](/docs/en/api/messages#text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

class ServerToolUsage: …

web_search_requests: int

The number of web search tool requests.

minimum0

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class ServerToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class SignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

Accepts one of the following:

"signature_delta"

StopReason = Literal\["end_turn", "max_tokens", "stop_sequence", 3 more\]

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"refusal"

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

TextCitation = [TextCitation](/docs/en/api/messages#text_citation)

Accepts one of the following:

class CitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

TextCitationParam = [TextCitationParam](/docs/en/api/messages#text_citation_param)

Accepts one of the following:

class CitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class TextDelta: …

text: str

type: Literal\["text_delta"\]

Accepts one of the following:

"text_delta"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class ThinkingBlockParam: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class ThinkingConfigAdaptive: …

type: Literal\["adaptive"\]

Accepts one of the following:

"adaptive"

class ThinkingConfigDisabled: …

type: Literal\["disabled"\]

Accepts one of the following:

"disabled"

class ThinkingConfigEnabled: …

budget_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: Literal\["enabled"\]

Accepts one of the following:

"enabled"

ThinkingConfigParam = [ThinkingConfigParam](/docs/en/api/messages#thinking_config_param)

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

Accepts one of the following:

"enabled"

class ThinkingConfigDisabled: …

type: Literal\["disabled"\]

Accepts one of the following:

"disabled"

class ThinkingConfigAdaptive: …

type: Literal\["adaptive"\]

Accepts one of the following:

"adaptive"

class ThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

Accepts one of the following:

"thinking_delta"

class Tool: …

input_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal\["object"\]

Accepts one of the following:

"object"

properties: Optional\[Dict\[str, object\]\]

required: Optional\[List\[str\]\]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description: Optional\[str\]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: Optional\[bool\]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

type: Optional\[Literal\["custom"\]\]

Accepts one of the following:

"custom"

class ToolBash20250124: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20250124"\]

Accepts one of the following:

"bash_20250124"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

ToolChoice = [ToolChoice](/docs/en/api/messages#tool_choice)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class ToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal\["auto"\]

Accepts one of the following:

"auto"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny: …

The model will use any available tools.

type: Literal\["any"\]

Accepts one of the following:

"any"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal\["tool"\]

Accepts one of the following:

"tool"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal\["none"\]

Accepts one of the following:

"none"

class ToolChoiceAny: …

The model will use any available tools.

type: Literal\["any"\]

Accepts one of the following:

"any"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal\["auto"\]

Accepts one of the following:

"auto"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal\["none"\]

Accepts one of the following:

"none"

class ToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal\["tool"\]

Accepts one of the following:

"tool"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolResultBlockParam: …

tool_use_id: str

type: Literal\["tool_result"\]

Accepts one of the following:

"tool_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

ContentUnionMember0 = str

Content = List\[Content\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union\[str, List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List\[[ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)\]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char_location"

class CitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

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

is_error: Optional\[bool\]

class ToolTextEditor20250124: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20250124"\]

Accepts one of the following:

"text_editor_20250124"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250429"\]

Accepts one of the following:

"text_editor_20250429"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250728"\]

Accepts one of the following:

"text_editor_20250728"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_characters: Optional\[int\]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

ToolUnion = [ToolUnion](/docs/en/api/messages#tool_union)

Accepts one of the following:

class Tool: …

input_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal\["object"\]

Accepts one of the following:

"object"

properties: Optional\[Dict\[str, object\]\]

required: Optional\[List\[str\]\]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description: Optional\[str\]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: Optional\[bool\]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

type: Optional\[Literal\["custom"\]\]

Accepts one of the following:

"custom"

class ToolBash20250124: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20250124"\]

Accepts one of the following:

"bash_20250124"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20250124"\]

Accepts one of the following:

"text_editor_20250124"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250429"\]

Accepts one of the following:

"text_editor_20250429"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250728"\]

Accepts one of the following:

"text_editor_20250728"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_characters: Optional\[int\]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305: …

name: Literal\["web_search"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: Literal\["web_search_20250305"\]

Accepts one of the following:

"web_search_20250305"

allowed_domains: Optional\[List\[str\]\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Optional\[List\[str\]\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

user_location: Optional\[UserLocation\]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal\["approximate"\]

Accepts one of the following:

"approximate"

city: Optional\[str\]

The city of the user.

maxLength255

minLength1

country: Optional\[str\]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional\[str\]

The region of the user.

maxLength255

minLength1

timezone: Optional\[str\]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class URLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class URLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class Usage: …

cache_creation: Optional\[CacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

class WebSearchResultBlock: …

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

class WebSearchResultBlockParam: …

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class WebSearchTool20250305: …

name: Literal\["web_search"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: Literal\["web_search_20250305"\]

Accepts one of the following:

"web_search_20250305"

allowed_domains: Optional\[List\[str\]\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Optional\[List\[str\]\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

user_location: Optional\[UserLocation\]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal\["approximate"\]

Accepts one of the following:

"approximate"

city: Optional\[str\]

The city of the user.

maxLength255

minLength1

country: Optional\[str\]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional\[str\]

The region of the user.

maxLength255

minLength1

timezone: Optional\[str\]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class WebSearchToolRequestError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

WebSearchToolResultBlockContent = [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

WebSearchToolResultBlockItem = List\[[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class WebSearchToolRequestError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

cache_control: Optional\[CacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

WebSearchToolResultBlockParamContent = [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)

Accepts one of the following:

WebSearchToolResultBlockItem = List\[[WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class WebSearchToolRequestError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

messages.batches.create(BatchCreateParams\*\*kwargs) -\> [MessageBatch](/docs/en/api/messages#message_batch)

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

messages.batches.retrieve(strmessage_batch_id) -\> [MessageBatch](/docs/en/api/messages#message_batch)

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

messages.batches.list(BatchListParams\*\*kwargs) -\> SyncPage\[[MessageBatch](/docs/en/api/messages#message_batch)\]

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

messages.batches.cancel(strmessage_batch_id) -\> [MessageBatch](/docs/en/api/messages#message_batch)

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

messages.batches.delete(strmessage_batch_id) -\> [DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch)

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

messages.batches.results(strmessage_batch_id) -\> [MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response)

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class DeletedMessageBatch: …

id: str

ID of the Message Batch.

type: Literal\["message_batch_deleted"\]

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

"message_batch_deleted"

class MessageBatch: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

archived_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel_initiated_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processing_status: Literal\["in_progress", "canceling", "ended"\]

Processing status of the Message Batch.

Accepts one of the following:

"in_progress"

"canceling"

"ended"

request_counts: [MessageBatchRequestCounts](/docs/en/api/messages#message_batch_request_counts)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.

succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results_url: Optional\[str\]

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: Literal\["message_batch"\]

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

"message_batch"

class MessageBatchCanceledResult: …

type: Literal\["canceled"\]

Accepts one of the following:

"canceled"

class MessageBatchErroredResult: …

error: [ErrorResponse](/docs/en/api/$shared#error_response)

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

Accepts one of the following:

"invalid_request_error"

class AuthenticationError: …

message: str

type: Literal\["authentication_error"\]

Accepts one of the following:

"authentication_error"

class BillingError: …

message: str

type: Literal\["billing_error"\]

Accepts one of the following:

"billing_error"

class PermissionError: …

message: str

type: Literal\["permission_error"\]

Accepts one of the following:

"permission_error"

class NotFoundError: …

message: str

type: Literal\["not_found_error"\]

Accepts one of the following:

"not_found_error"

class RateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

Accepts one of the following:

"rate_limit_error"

class GatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

Accepts one of the following:

"timeout_error"

class APIErrorObject: …

message: str

type: Literal\["api_error"\]

Accepts one of the following:

"api_error"

class OverloadedError: …

message: str

type: Literal\["overloaded_error"\]

Accepts one of the following:

"overloaded_error"

request_id: Optional\[str\]

type: Literal\["error"\]

Accepts one of the following:

"error"

type: Literal\["errored"\]

Accepts one of the following:

"errored"

class MessageBatchExpiredResult: …

type: Literal\["expired"\]

Accepts one of the following:

"expired"

class MessageBatchIndividualResponse: …

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: str

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [MessageBatchResult](/docs/en/api/messages#message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult: …

message: [Message](/docs/en/api/messages#message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
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

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["succeeded"\]

Accepts one of the following:

"succeeded"

class MessageBatchErroredResult: …

error: [ErrorResponse](/docs/en/api/$shared#error_response)

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

Accepts one of the following:

"invalid_request_error"

class AuthenticationError: …

message: str

type: Literal\["authentication_error"\]

Accepts one of the following:

"authentication_error"

class BillingError: …

message: str

type: Literal\["billing_error"\]

Accepts one of the following:

"billing_error"

class PermissionError: …

message: str

type: Literal\["permission_error"\]

Accepts one of the following:

"permission_error"

class NotFoundError: …

message: str

type: Literal\["not_found_error"\]

Accepts one of the following:

"not_found_error"

class RateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

Accepts one of the following:

"rate_limit_error"

class GatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

Accepts one of the following:

"timeout_error"

class APIErrorObject: …

message: str

type: Literal\["api_error"\]

Accepts one of the following:

"api_error"

class OverloadedError: …

message: str

type: Literal\["overloaded_error"\]

Accepts one of the following:

"overloaded_error"

request_id: Optional\[str\]

type: Literal\["error"\]

Accepts one of the following:

"error"

type: Literal\["errored"\]

Accepts one of the following:

"errored"

class MessageBatchCanceledResult: …

type: Literal\["canceled"\]

Accepts one of the following:

"canceled"

class MessageBatchExpiredResult: …

type: Literal\["expired"\]

Accepts one of the following:

"expired"

class MessageBatchRequestCounts: …

canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.

succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

MessageBatchResult = [MessageBatchResult](/docs/en/api/messages#message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult: …

message: [Message](/docs/en/api/messages#message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
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

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["succeeded"\]

Accepts one of the following:

"succeeded"

class MessageBatchErroredResult: …

error: [ErrorResponse](/docs/en/api/$shared#error_response)

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

Accepts one of the following:

"invalid_request_error"

class AuthenticationError: …

message: str

type: Literal\["authentication_error"\]

Accepts one of the following:

"authentication_error"

class BillingError: …

message: str

type: Literal\["billing_error"\]

Accepts one of the following:

"billing_error"

class PermissionError: …

message: str

type: Literal\["permission_error"\]

Accepts one of the following:

"permission_error"

class NotFoundError: …

message: str

type: Literal\["not_found_error"\]

Accepts one of the following:

"not_found_error"

class RateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

Accepts one of the following:

"rate_limit_error"

class GatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

Accepts one of the following:

"timeout_error"

class APIErrorObject: …

message: str

type: Literal\["api_error"\]

Accepts one of the following:

"api_error"

class OverloadedError: …

message: str

type: Literal\["overloaded_error"\]

Accepts one of the following:

"overloaded_error"

request_id: Optional\[str\]

type: Literal\["error"\]

Accepts one of the following:

"error"

type: Literal\["errored"\]

Accepts one of the following:

"errored"

class MessageBatchCanceledResult: …

type: Literal\["canceled"\]

Accepts one of the following:

"canceled"

class MessageBatchExpiredResult: …

type: Literal\["expired"\]

Accepts one of the following:

"expired"

class MessageBatchSucceededResult: …

message: [Message](/docs/en/api/messages#message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char_location"

class CitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class CitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class CitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class CitationsSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class ToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

class ServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search"\]

Accepts one of the following:

"web_search"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
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

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[ServerToolUsage\]

The number of server tool requests.

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["succeeded"\]

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
