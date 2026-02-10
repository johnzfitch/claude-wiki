---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:08:04Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/messages/count_tokens"
title: "Count tokens in a Message - Claude API Reference"
---

Copy page

Python

# Count tokens in a Message

beta.messages.count_tokens(MessageCountTokensParams\*\*kwargs) -\> [BetaMessageTokensCount](/docs/en/api/beta#beta_message_tokens_count)

post/v1/messages/count_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse 

messages: [Iterable](/docs/en/api/beta/messages/count_tokens)\[[BetaMessageParam](/docs/en/api/beta#beta_message_param)\]

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

content: Union\[str, List\[[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentUnionMember1 = List\[[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

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

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaRequestDocumentBlock: …

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

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

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class BetaSearchResultBlockParam: …

content: List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

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

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

class BetaThinkingBlockParam: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlockParam: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaToolResultBlockParam: …

tool_use_id: str

type: Literal\["tool_result"\]

Accepts one of the following:

"tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

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

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaSearchResultBlockParam: …

content: List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

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

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

class BetaRequestDocumentBlock: …

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

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

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool_result content.

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

is_error: Optional\[bool\]

class BetaServerToolUseBlockParam: …

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

Accepts one of the following:

"server_tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlockParam: …

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = List\[[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class BetaWebSearchToolRequestError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

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

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaWebFetchToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam: …

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

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlockParam: …

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block)

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

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

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaCodeExecutionToolResultBlockParam: …

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlockParam: …

content: List\[[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaBashCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlockParam: …

content: List\[[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaTextEditorCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message: Optional\[str\]

class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaToolSearchToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlockParam: …

tool_references: List\[[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaMCPToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaRequestMCPToolResultBlockParam: …

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

content: Optional\[Union\[str, List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\], null\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockParamContent = List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

is_error: Optional\[bool\]

class BetaContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

class BetaCompactionBlockParam: …

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: Optional\[str\]

Summary of previously compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

model: [ModelParam](/docs/en/api/messages#model)

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

context_management: Optional\[BetaContextManagementConfigParam\]

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

edits: Optional\[List\[Edit\]\]

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit: …

type: Literal\["clear_tool_uses_20250919"\]

Accepts one of the following:

"clear_tool_uses_20250919"

clear_at_least: Optional\[BetaInputTokensClearAtLeast\]

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

clear_tool_inputs: Optional\[Union\[bool, List\[str\], null\]\]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

ClearToolInputsUnionMember0 = bool

ClearToolInputsUnionMember1 = List\[str\]

exclude_tools: Optional\[List\[str\]\]

Tool names whose uses are preserved from clearing

keep: Optional\[BetaToolUsesKeep\]

Number of tool uses to retain in the conversation

type: Literal\["tool_uses"\]

Accepts one of the following:

"tool_uses"

value: int

trigger: Optional\[Trigger\]

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger: …

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

class BetaToolUsesTrigger: …

type: Literal\["tool_uses"\]

Accepts one of the following:

"tool_uses"

value: int

class BetaClearThinking20251015Edit: …

type: Literal\["clear_thinking_20251015"\]

Accepts one of the following:

"clear_thinking_20251015"

keep: Optional\[Keep\]

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns: …

type: Literal\["thinking_turns"\]

Accepts one of the following:

"thinking_turns"

value: int

class BetaAllThinkingTurns: …

type: Literal\["all"\]

Accepts one of the following:

"all"

KeepUnionMember2 = Literal\["all"\]

Accepts one of the following:

"all"

class BetaCompact20260112Edit: …

Automatically compact older context when reaching the configured trigger threshold.

type: Literal\["compact_20260112"\]

Accepts one of the following:

"compact_20260112"

instructions: Optional\[str\]

Additional instructions for summarization.

pause_after_compaction: Optional\[bool\]

Whether to pause after compaction and return the compaction block to the user.

trigger: Optional\[BetaInputTokensTrigger\]

When to trigger compaction. Defaults to 150000 input tokens.

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

mcp_servers: Optional\[[Iterable](/docs/en/api/beta/messages/count_tokens)\[[BetaRequestMCPServerURLDefinitionParam](/docs/en/api/beta#beta_request_mcp_server_url_definition)\]\]

MCP servers to be utilized in this request

name: str

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

authorization_token: Optional\[str\]

tool_configuration: Optional\[BetaRequestMCPServerToolConfiguration\]

allowed_tools: Optional\[List\[str\]\]

enabled: Optional\[bool\]

output_config: Optional\[[BetaOutputConfigParam](/docs/en/api/beta#beta_output_config)\]

Configuration options for the model's output, such as the output format.

effort: Optional\[Literal\["low", "medium", "high", "max"\]\]

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format: Optional\[BetaJSONOutputFormat\]

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: Dict\[str, object\]

The JSON schema of the format

type: Literal\["json_schema"\]

Accepts one of the following:

"json_schema"

Deprecatedoutput_format: Optional\[BetaJSONOutputFormatParam\]

Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

schema: Dict\[str, object\]

The JSON schema of the format

type: Literal\["json_schema"\]

Accepts one of the following:

"json_schema"

system: Optional\[Union\[str, Iterable\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]\]\]

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

SystemUnionMember0 = str

SystemUnionMember1 = Iterable\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

thinking: Optional\[[BetaThinkingConfigParam](/docs/en/api/beta#beta_thinking_config_param)\]

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class BetaThinkingConfigEnabled: …

budget_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: Literal\["enabled"\]

Accepts one of the following:

"enabled"

class BetaThinkingConfigDisabled: …

type: Literal\["disabled"\]

Accepts one of the following:

"disabled"

class BetaThinkingConfigAdaptive: …

type: Literal\["adaptive"\]

Accepts one of the following:

"adaptive"

tool_choice: Optional\[[BetaToolChoiceParam](/docs/en/api/beta#beta_tool_choice)\]

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class BetaToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal\["auto"\]

Accepts one of the following:

"auto"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny: …

The model will use any available tools.

type: Literal\["any"\]

Accepts one of the following:

"any"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal\["tool"\]

Accepts one of the following:

"tool"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal\["none"\]

Accepts one of the following:

"none"

tools: Optional\[[Iterable](/docs/en/api/beta/messages/count_tokens)\[Tool\]\]

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

class BetaTool: …

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

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

Accepts one of the following:

"custom"

class BetaToolBash20241022: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20241022"\]

Accepts one of the following:

"bash_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20250124"\]

Accepts one of the following:

"bash_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522: …

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: Literal\["code_execution_20250522"\]

Accepts one of the following:

"code_execution_20250522"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825: …

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20241022"\]

Accepts one of the following:

"computer_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818: …

name: Literal\["memory"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"memory"

type: Literal\["memory_20250818"\]

Accepts one of the following:

"memory_20250818"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20250124"\]

Accepts one of the following:

"computer_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20241022"\]

Accepts one of the following:

"text_editor_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20251124"\]

Accepts one of the following:

"computer_20251124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

enable_zoom: Optional\[bool\]

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20250124"\]

Accepts one of the following:

"text_editor_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250429"\]

Accepts one of the following:

"text_editor_20250429"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250728"\]

Accepts one of the following:

"text_editor_20250728"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

max_characters: Optional\[int\]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305: …

name: Literal\["web_search"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: Literal\["web_search_20250305"\]

Accepts one of the following:

"web_search_20250305"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains: Optional\[List\[str\]\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Optional\[List\[str\]\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

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

class BetaWebFetchTool20250910: …

name: Literal\["web_fetch"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_fetch"

type: Literal\["web_fetch_20250910"\]

Accepts one of the following:

"web_fetch_20250910"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains: Optional\[List\[str\]\]

List of domains to allow fetching from

blocked_domains: Optional\[List\[str\]\]

List of domains to block fetching from

cache_control: Optional\[BetaCacheControlEphemeral\]

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

citations: Optional\[BetaCitationsConfigParam\]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional\[bool\]

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: Optional\[int\]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolBm25_20251119: …

name: Literal\["tool_search_tool_bm25"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_bm25"

type: Literal\["tool_search_tool_bm25_20251119", "tool_search_tool_bm25"\]

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119: …

name: Literal\["tool_search_tool_regex"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_regex"

type: Literal\["tool_search_tool_regex_20251119", "tool_search_tool_regex"\]

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaMCPToolset: …

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: str

Name of the MCP server to configure tools for

maxLength255

minLength1

type: Literal\["mcp_toolset"\]

Accepts one of the following:

"mcp_toolset"

cache_control: Optional\[BetaCacheControlEphemeral\]

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

configs: Optional\[Dict\[str, [BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config)\]\]

Configuration overrides for specific tools, keyed by tool name

defer_loading: Optional\[bool\]

enabled: Optional\[bool\]

default_config: Optional\[BetaMCPToolDefaultConfig\]

Default configuration applied to all tools from this server

defer_loading: Optional\[bool\]

enabled: Optional\[bool\]

betas: Optional\[List\[[AnthropicBetaParam](/docs/en/api/beta#anthropic_beta)\]\]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = str

UnionMember1 = Literal\["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 16 more\]

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

##### ReturnsExpand Collapse 

class BetaMessageTokensCount: …

context_management: Optional\[BetaCountTokensContextManagementResponse\]

Information about context management applied to the message.

original_input_tokens: int

The original token count before context management was applied

input_tokens: int

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

Python

``` shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_message_tokens_count = client.beta.messages.count_tokens(
    messages=[{
        "content": "string",
        "role": "user",
    }],
    model="claude-opus-4-6",
)
print(beta_message_tokens_count.context_management)
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
