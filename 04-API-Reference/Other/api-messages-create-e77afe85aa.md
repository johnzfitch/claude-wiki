---
title: "Create a Message - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/messages/create"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:50Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Create




cURL



A beta version of this method exists and may have additional functionality. [View the beta version](/docs/en/api/beta/messages/create).

# Create a Message

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

##### Header ParametersExpand Collapse 

"anthropic-user-profile-id": optional string



The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

[](#create.user_profile_id)

##### Body ParametersJSONExpand Collapse 



max_tokens: number



The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

minimum0

[](#create.max_tokens)



messages: array of [MessageParam](/docs/en/api/messages#message_param) { content, role }



Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single `user` message:

```python
[{"role": "user", "content": "Hello, Claude"}]
```



Example with multiple conversational turns:

```python
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```



Example with a partially-filled response from Claude:

```python
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]
```



Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

```python
{"role": "user", "content": "Hello, Claude"}
```



```python
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```



See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.



content: string or array of [ContentBlockParam](/docs/en/api/messages#content_block_param)



One of the following:

string



[](#message_param.content%5B0%5D)



array of [ContentBlockParam](/docs/en/api/messages#content_block_param)



One of the following:



TextBlockParam object { text, type, cache_control, citations }



text: string



[](#text_block_param.text)

type: "text"



[](#text_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_block_param.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_char_location_param.cited_text)

document_index: number



[](#citation_char_location_param.document_index)

document_title: string



[](#citation_char_location_param.document_title)

end_char_index: number



[](#citation_char_location_param.end_char_index)

start_char_index: number



[](#citation_char_location_param.start_char_index)

type: "char_location"



[](#citation_char_location_param.type)

[](#citation_char_location_param)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_page_location_param.cited_text)

document_index: number



[](#citation_page_location_param.document_index)

document_title: string



[](#citation_page_location_param.document_title)

end_page_number: number



[](#citation_page_location_param.end_page_number)

start_page_number: number



[](#citation_page_location_param.start_page_number)

type: "page_location"



[](#citation_page_location_param.type)

[](#citation_page_location_param)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location_param.cited_text)

document_index: number



[](#citation_content_block_location_param.document_index)

document_title: string



[](#citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#citation_content_block_location_param.type)

[](#citation_content_block_location_param)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#citation_web_search_result_location_param.encrypted_index)

title: string



[](#citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#citation_web_search_result_location_param.type)

url: string



[](#citation_web_search_result_location_param.url)

[](#citation_web_search_result_location_param)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citation_search_result_location_param.search_result_index)

source: string



[](#citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_search_result_location_param.start_block_index)

title: string



[](#citation_search_result_location_param.title)

type: "search_result_location"



[](#citation_search_result_location_param.type)

[](#citation_search_result_location_param)

[](#text_block_param.citations)

[](#text_block_param)



ImageBlockParam object { source, type, cache_control }





source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }



One of the following:



Base64ImageSource object { data, media_type, type }



data: string



[](#base64_image_source.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#base64_image_source.media_type%5B0%5D)

"image/png"



[](#base64_image_source.media_type%5B1%5D)

"image/gif"



[](#base64_image_source.media_type%5B2%5D)

"image/webp"



[](#base64_image_source.media_type%5B3%5D)

[](#base64_image_source.media_type)

type: "base64"



[](#base64_image_source.type)

[](#base64_image_source)



URLImageSource object { type, url }



type: "url"



[](#url_image_source.type)

url: string



[](#url_image_source.url)

[](#url_image_source)

[](#image_block_param.source)

type: "image"



[](#image_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#image_block_param.cache_control)

[](#image_block_param)



DocumentBlockParam object { source, type, cache_control, 3 more }





source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } or [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } or [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }



One of the following:



Base64PDFSource object { data, media_type, type }



data: string



[](#base64_pdf_source.data)

media_type: "application/pdf"



[](#base64_pdf_source.media_type)

type: "base64"



[](#base64_pdf_source.type)

[](#base64_pdf_source)



PlainTextSource object { data, media_type, type }



data: string



[](#plain_text_source.data)

media_type: "text/plain"



[](#plain_text_source.media_type)

type: "text"



[](#plain_text_source.type)

[](#plain_text_source)



ContentBlockSource object { content, type }





content: string or array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)



One of the following:

string



[](#content_block_source.content%5B0%5D)



ContentBlockSourceContent = array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)



One of the following:



TextBlockParam object { text, type, cache_control, citations }



text: string



[](#text_block_param.text)

type: "text"



[](#text_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_block_param.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_char_location_param.cited_text)

document_index: number



[](#citation_char_location_param.document_index)

document_title: string



[](#citation_char_location_param.document_title)

end_char_index: number



[](#citation_char_location_param.end_char_index)

start_char_index: number



[](#citation_char_location_param.start_char_index)

type: "char_location"



[](#citation_char_location_param.type)

[](#citation_char_location_param)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_page_location_param.cited_text)

document_index: number



[](#citation_page_location_param.document_index)

document_title: string



[](#citation_page_location_param.document_title)

end_page_number: number



[](#citation_page_location_param.end_page_number)

start_page_number: number



[](#citation_page_location_param.start_page_number)

type: "page_location"



[](#citation_page_location_param.type)

[](#citation_page_location_param)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location_param.cited_text)

document_index: number



[](#citation_content_block_location_param.document_index)

document_title: string



[](#citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#citation_content_block_location_param.type)

[](#citation_content_block_location_param)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#citation_web_search_result_location_param.encrypted_index)

title: string



[](#citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#citation_web_search_result_location_param.type)

url: string



[](#citation_web_search_result_location_param.url)

[](#citation_web_search_result_location_param)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citation_search_result_location_param.search_result_index)

source: string



[](#citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_search_result_location_param.start_block_index)

title: string



[](#citation_search_result_location_param.title)

type: "search_result_location"



[](#citation_search_result_location_param.type)

[](#citation_search_result_location_param)

[](#text_block_param.citations)

[](#text_block_param)



ImageBlockParam object { source, type, cache_control }





source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }



One of the following:



Base64ImageSource object { data, media_type, type }



data: string



[](#base64_image_source.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#base64_image_source.media_type%5B0%5D)

"image/png"



[](#base64_image_source.media_type%5B1%5D)

"image/gif"



[](#base64_image_source.media_type%5B2%5D)

"image/webp"



[](#base64_image_source.media_type%5B3%5D)

[](#base64_image_source.media_type)

type: "base64"



[](#base64_image_source.type)

[](#base64_image_source)



URLImageSource object { type, url }



type: "url"



[](#url_image_source.type)

url: string



[](#url_image_source.url)

[](#url_image_source)

[](#image_block_param.source)

type: "image"



[](#image_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#image_block_param.cache_control)

[](#image_block_param)

[](#content_block_source.content%5B1%5D)

[](#content_block_source.content)

type: "content"



[](#content_block_source.type)

[](#content_block_source)



URLPDFSource object { type, url }



type: "url"



[](#url_pdf_source.type)

url: string



[](#url_pdf_source.url)

[](#url_pdf_source)

[](#document_block_param.source)

type: "document"



[](#document_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#document_block_param.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



enabled: optional boolean



[](#document_block_param.citations%20%2B%20(resource)%20messages.enabled)

[](#document_block_param.citations)

context: optional string



[](#document_block_param.context)

title: optional string



[](#document_block_param.title)

[](#document_block_param)



SearchResultBlockParam object { content, source, title, 3 more }





content: array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }



text: string



[](#text_block_param.text)

type: "text"



[](#text_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_block_param.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_char_location_param.cited_text)

document_index: number



[](#citation_char_location_param.document_index)

document_title: string



[](#citation_char_location_param.document_title)

end_char_index: number



[](#citation_char_location_param.end_char_index)

start_char_index: number



[](#citation_char_location_param.start_char_index)

type: "char_location"



[](#citation_char_location_param.type)

[](#citation_char_location_param)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_page_location_param.cited_text)

document_index: number



[](#citation_page_location_param.document_index)

document_title: string



[](#citation_page_location_param.document_title)

end_page_number: number



[](#citation_page_location_param.end_page_number)

start_page_number: number



[](#citation_page_location_param.start_page_number)

type: "page_location"



[](#citation_page_location_param.type)

[](#citation_page_location_param)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location_param.cited_text)

document_index: number



[](#citation_content_block_location_param.document_index)

document_title: string



[](#citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#citation_content_block_location_param.type)

[](#citation_content_block_location_param)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#citation_web_search_result_location_param.encrypted_index)

title: string



[](#citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#citation_web_search_result_location_param.type)

url: string



[](#citation_web_search_result_location_param.url)

[](#citation_web_search_result_location_param)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citation_search_result_location_param.search_result_index)

source: string



[](#citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_search_result_location_param.start_block_index)

title: string



[](#citation_search_result_location_param.title)

type: "search_result_location"



[](#citation_search_result_location_param.type)

[](#citation_search_result_location_param)

[](#text_block_param.citations)

[](#search_result_block_param.content)

source: string



[](#search_result_block_param.source)

title: string



[](#search_result_block_param.title)

type: "search_result"



[](#search_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#search_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#search_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#search_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#search_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#search_result_block_param.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



enabled: optional boolean



[](#search_result_block_param.citations%20%2B%20(resource)%20messages.enabled)

[](#search_result_block_param.citations)

[](#search_result_block_param)



ThinkingBlockParam object { signature, thinking, type }



signature: string



[](#thinking_block_param.signature)

thinking: string



[](#thinking_block_param.thinking)

type: "thinking"



[](#thinking_block_param.type)

[](#thinking_block_param)



RedactedThinkingBlockParam object { data, type }



data: string



[](#redacted_thinking_block_param.data)

type: "redacted_thinking"



[](#redacted_thinking_block_param.type)

[](#redacted_thinking_block_param)



ToolUseBlockParam object { id, input, name, 3 more }



id: string



[](#tool_use_block_param.id)

input: map\[unknown\]



[](#tool_use_block_param.input)

name: string



[](#tool_use_block_param.name)

type: "tool_use"



[](#tool_use_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_use_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_use_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_use_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_use_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_use_block_param.cache_control)



caller: optional [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#tool_use_block_param.caller)

[](#tool_use_block_param)



ToolResultBlockParam object { tool_use_id, type, cache_control, 2 more }



tool_use_id: string



[](#tool_result_block_param.tool_use_id)

type: "tool_result"



[](#tool_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_result_block_param.cache_control)



content: optional string or array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } or [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } or [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } or 2 more



One of the following:

string



[](#tool_result_block_param.content%5B0%5D)



array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } or [ImageBlockParam](/docs/en/api/messages#image_block_param) { source, type, cache_control } or [SearchResultBlockParam](/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more } or 2 more



One of the following:



TextBlockParam object { text, type, cache_control, citations }



text: string



[](#text_block_param.text)

type: "text"



[](#text_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_block_param.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_char_location_param.cited_text)

document_index: number



[](#citation_char_location_param.document_index)

document_title: string



[](#citation_char_location_param.document_title)

end_char_index: number



[](#citation_char_location_param.end_char_index)

start_char_index: number



[](#citation_char_location_param.start_char_index)

type: "char_location"



[](#citation_char_location_param.type)

[](#citation_char_location_param)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_page_location_param.cited_text)

document_index: number



[](#citation_page_location_param.document_index)

document_title: string



[](#citation_page_location_param.document_title)

end_page_number: number



[](#citation_page_location_param.end_page_number)

start_page_number: number



[](#citation_page_location_param.start_page_number)

type: "page_location"



[](#citation_page_location_param.type)

[](#citation_page_location_param)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location_param.cited_text)

document_index: number



[](#citation_content_block_location_param.document_index)

document_title: string



[](#citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#citation_content_block_location_param.type)

[](#citation_content_block_location_param)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#citation_web_search_result_location_param.encrypted_index)

title: string



[](#citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#citation_web_search_result_location_param.type)

url: string



[](#citation_web_search_result_location_param.url)

[](#citation_web_search_result_location_param)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citation_search_result_location_param.search_result_index)

source: string



[](#citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_search_result_location_param.start_block_index)

title: string



[](#citation_search_result_location_param.title)

type: "search_result_location"



[](#citation_search_result_location_param.type)

[](#citation_search_result_location_param)

[](#text_block_param.citations)

[](#text_block_param)



ImageBlockParam object { source, type, cache_control }





source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }



One of the following:



Base64ImageSource object { data, media_type, type }



data: string



[](#base64_image_source.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#base64_image_source.media_type%5B0%5D)

"image/png"



[](#base64_image_source.media_type%5B1%5D)

"image/gif"



[](#base64_image_source.media_type%5B2%5D)

"image/webp"



[](#base64_image_source.media_type%5B3%5D)

[](#base64_image_source.media_type)

type: "base64"



[](#base64_image_source.type)

[](#base64_image_source)



URLImageSource object { type, url }



type: "url"



[](#url_image_source.type)

url: string



[](#url_image_source.url)

[](#url_image_source)

[](#image_block_param.source)

type: "image"



[](#image_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#image_block_param.cache_control)

[](#image_block_param)



SearchResultBlockParam object { content, source, title, 3 more }





content: array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }



text: string



[](#text_block_param.text)

type: "text"



[](#text_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_block_param.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_char_location_param.cited_text)

document_index: number



[](#citation_char_location_param.document_index)

document_title: string



[](#citation_char_location_param.document_title)

end_char_index: number



[](#citation_char_location_param.end_char_index)

start_char_index: number



[](#citation_char_location_param.start_char_index)

type: "char_location"



[](#citation_char_location_param.type)

[](#citation_char_location_param)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_page_location_param.cited_text)

document_index: number



[](#citation_page_location_param.document_index)

document_title: string



[](#citation_page_location_param.document_title)

end_page_number: number



[](#citation_page_location_param.end_page_number)

start_page_number: number



[](#citation_page_location_param.start_page_number)

type: "page_location"



[](#citation_page_location_param.type)

[](#citation_page_location_param)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location_param.cited_text)

document_index: number



[](#citation_content_block_location_param.document_index)

document_title: string



[](#citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#citation_content_block_location_param.type)

[](#citation_content_block_location_param)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#citation_web_search_result_location_param.encrypted_index)

title: string



[](#citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#citation_web_search_result_location_param.type)

url: string



[](#citation_web_search_result_location_param.url)

[](#citation_web_search_result_location_param)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citation_search_result_location_param.search_result_index)

source: string



[](#citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_search_result_location_param.start_block_index)

title: string



[](#citation_search_result_location_param.title)

type: "search_result_location"



[](#citation_search_result_location_param.type)

[](#citation_search_result_location_param)

[](#text_block_param.citations)

[](#search_result_block_param.content)

source: string



[](#search_result_block_param.source)

title: string



[](#search_result_block_param.title)

type: "search_result"



[](#search_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#search_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#search_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#search_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#search_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#search_result_block_param.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



enabled: optional boolean



[](#search_result_block_param.citations%20%2B%20(resource)%20messages.enabled)

[](#search_result_block_param.citations)

[](#search_result_block_param)



DocumentBlockParam object { source, type, cache_control, 3 more }





source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } or [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } or [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }



One of the following:



Base64PDFSource object { data, media_type, type }



data: string



[](#base64_pdf_source.data)

media_type: "application/pdf"



[](#base64_pdf_source.media_type)

type: "base64"



[](#base64_pdf_source.type)

[](#base64_pdf_source)



PlainTextSource object { data, media_type, type }



data: string



[](#plain_text_source.data)

media_type: "text/plain"



[](#plain_text_source.media_type)

type: "text"



[](#plain_text_source.type)

[](#plain_text_source)



ContentBlockSource object { content, type }





content: string or array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)



One of the following:

string



[](#content_block_source.content%5B0%5D)



ContentBlockSourceContent = array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)



One of the following:



TextBlockParam object { text, type, cache_control, citations }



text: string



[](#text_block_param.text)

type: "text"



[](#text_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_block_param.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_char_location_param.cited_text)

document_index: number



[](#citation_char_location_param.document_index)

document_title: string



[](#citation_char_location_param.document_title)

end_char_index: number



[](#citation_char_location_param.end_char_index)

start_char_index: number



[](#citation_char_location_param.start_char_index)

type: "char_location"



[](#citation_char_location_param.type)

[](#citation_char_location_param)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_page_location_param.cited_text)

document_index: number



[](#citation_page_location_param.document_index)

document_title: string



[](#citation_page_location_param.document_title)

end_page_number: number



[](#citation_page_location_param.end_page_number)

start_page_number: number



[](#citation_page_location_param.start_page_number)

type: "page_location"



[](#citation_page_location_param.type)

[](#citation_page_location_param)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location_param.cited_text)

document_index: number



[](#citation_content_block_location_param.document_index)

document_title: string



[](#citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#citation_content_block_location_param.type)

[](#citation_content_block_location_param)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#citation_web_search_result_location_param.encrypted_index)

title: string



[](#citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#citation_web_search_result_location_param.type)

url: string



[](#citation_web_search_result_location_param.url)

[](#citation_web_search_result_location_param)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citation_search_result_location_param.search_result_index)

source: string



[](#citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_search_result_location_param.start_block_index)

title: string



[](#citation_search_result_location_param.title)

type: "search_result_location"



[](#citation_search_result_location_param.type)

[](#citation_search_result_location_param)

[](#text_block_param.citations)

[](#text_block_param)



ImageBlockParam object { source, type, cache_control }





source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }



One of the following:



Base64ImageSource object { data, media_type, type }



data: string



[](#base64_image_source.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#base64_image_source.media_type%5B0%5D)

"image/png"



[](#base64_image_source.media_type%5B1%5D)

"image/gif"



[](#base64_image_source.media_type%5B2%5D)

"image/webp"



[](#base64_image_source.media_type%5B3%5D)

[](#base64_image_source.media_type)

type: "base64"



[](#base64_image_source.type)

[](#base64_image_source)



URLImageSource object { type, url }



type: "url"



[](#url_image_source.type)

url: string



[](#url_image_source.url)

[](#url_image_source)

[](#image_block_param.source)

type: "image"



[](#image_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#image_block_param.cache_control)

[](#image_block_param)

[](#content_block_source.content%5B1%5D)

[](#content_block_source.content)

type: "content"



[](#content_block_source.type)

[](#content_block_source)



URLPDFSource object { type, url }



type: "url"



[](#url_pdf_source.type)

url: string



[](#url_pdf_source.url)

[](#url_pdf_source)

[](#document_block_param.source)

type: "document"



[](#document_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#document_block_param.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



enabled: optional boolean



[](#document_block_param.citations%20%2B%20(resource)%20messages.enabled)

[](#document_block_param.citations)

context: optional string



[](#document_block_param.context)

title: optional string



[](#document_block_param.title)

[](#document_block_param)



ToolReferenceBlockParam object { tool_name, type, cache_control }



Tool reference block that can be included in tool_result content.

tool_name: string



[](#tool_reference_block_param.tool_name)

type: "tool_reference"



[](#tool_reference_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_reference_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_reference_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_reference_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_reference_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_reference_block_param.cache_control)

[](#tool_reference_block_param)

[](#tool_result_block_param.content%5B1%5D)

[](#tool_result_block_param.content)

is_error: optional boolean



[](#tool_result_block_param.is_error)

[](#tool_result_block_param)



ServerToolUseBlockParam object { id, input, name, 3 more }



id: string



[](#server_tool_use_block_param.id)

input: map\[unknown\]



[](#server_tool_use_block_param.input)



name: "web_search" or "web_fetch" or "code_execution" or 4 more



One of the following:

"web_search"



[](#server_tool_use_block_param.name%5B0%5D)

"web_fetch"



[](#server_tool_use_block_param.name%5B1%5D)

"code_execution"



[](#server_tool_use_block_param.name%5B2%5D)

"bash_code_execution"



[](#server_tool_use_block_param.name%5B3%5D)

"text_editor_code_execution"



[](#server_tool_use_block_param.name%5B4%5D)

"tool_search_tool_regex"



[](#server_tool_use_block_param.name%5B5%5D)

"tool_search_tool_bm25"



[](#server_tool_use_block_param.name%5B6%5D)

[](#server_tool_use_block_param.name)

type: "server_tool_use"



[](#server_tool_use_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#server_tool_use_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#server_tool_use_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#server_tool_use_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#server_tool_use_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#server_tool_use_block_param.cache_control)



caller: optional [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#server_tool_use_block_param.caller)

[](#server_tool_use_block_param)



WebSearchToolResultBlockParam object { content, tool_use_id, type, 2 more }





content: [WebSearchToolResultBlockParamContent](/docs/en/api/messages#web_search_tool_result_block_param_content)



One of the following:



WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more }



encrypted_content: string



[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages.encrypted_content)

title: string



[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages.title)

type: "web_search_result"



[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages.type)

url: string



[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages.url)

page_age: optional string



[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages.page_age)

[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages%5B0%5D)



WebSearchToolRequestError object { error_code, type }





error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#web_search_tool_request_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#web_search_tool_request_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"max_uses_exceeded"



[](#web_search_tool_request_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"too_many_requests"



[](#web_search_tool_request_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"query_too_long"



[](#web_search_tool_request_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

"request_too_large"



[](#web_search_tool_request_error.error_code%20%2B%20(resource)%20messages%5B5%5D)

[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages.error_code)

type: "web_search_tool_result_error"



[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_search_tool_result_block_param.content%20%2B%20(resource)%20messages)

[](#web_search_tool_result_block_param.content)

tool_use_id: string



[](#web_search_tool_result_block_param.tool_use_id)

type: "web_search_tool_result"



[](#web_search_tool_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_search_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_search_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_search_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_search_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_search_tool_result_block_param.cache_control)



caller: optional [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#web_search_tool_result_block_param.caller)

[](#web_search_tool_result_block_param)



WebFetchToolResultBlockParam object { content, tool_use_id, type, 2 more }





content: [WebFetchToolResultErrorBlockParam](/docs/en/api/messages#web_fetch_tool_result_error_block_param) { error_code, type } or [WebFetchBlockParam](/docs/en/api/messages#web_fetch_block_param) { content, type, url, retrieved_at }



One of the following:



WebFetchToolResultErrorBlockParam object { error_code, type }





error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B0%5D)

"url_too_long"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B1%5D)

"url_not_allowed"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B2%5D)

"url_not_in_prior_context"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B3%5D)

"url_not_accessible"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B4%5D)

"unsupported_content_type"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B5%5D)

"too_many_requests"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B6%5D)

"max_uses_exceeded"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B7%5D)

"unavailable"



[](#web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20messages%5B8%5D)

[](#web_fetch_tool_result_error_block_param.error_code)

type: "web_fetch_tool_result_error"



[](#web_fetch_tool_result_error_block_param.type)

[](#web_fetch_tool_result_error_block_param)



WebFetchBlockParam object { content, type, url, retrieved_at }





content: [DocumentBlockParam](/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more }





source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type } or [ContentBlockSource](/docs/en/api/messages#content_block_source) { content, type } or [URLPDFSource](/docs/en/api/messages#url_pdf_source) { type, url }



One of the following:



Base64PDFSource object { data, media_type, type }



data: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.data)

media_type: "application/pdf"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.media_type)

type: "base64"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



PlainTextSource object { data, media_type, type }



data: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.data)

media_type: "text/plain"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.media_type)

type: "text"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



ContentBlockSource object { content, type }





content: string or array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)



One of the following:

string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.content%5B0%5D)



ContentBlockSourceContent = array of [ContentBlockSourceContent](/docs/en/api/messages#content_block_source_content)



One of the following:



TextBlockParam object { text, type, cache_control, citations }



text: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.text)

type: "text"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.document_title)

end_char_index: number



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.end_char_index)

start_char_index: number



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.start_char_index)

type: "char_location"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.document_title)

end_page_number: number



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.end_page_number)

start_page_number: number



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.start_page_number)

type: "page_location"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.start_block_index)

type: "content_block_location"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.cited_text)

encrypted_index: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.encrypted_index)

title: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.title)

type: "web_search_result_location"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

url: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.url)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.search_result_index)

source: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.start_block_index)

title: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.title)

type: "search_result_location"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.citations)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



ImageBlockParam object { source, type, cache_control }





source: [Base64ImageSource](/docs/en/api/messages#base64_image_source) { data, media_type, type } or [URLImageSource](/docs/en/api/messages#url_image_source) { type, url }



One of the following:



Base64ImageSource object { data, media_type, type }



data: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.media_type%5B0%5D)

"image/png"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.media_type%5B1%5D)

"image/gif"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.media_type%5B2%5D)

"image/webp"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.media_type%5B3%5D)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.media_type)

type: "base64"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



URLImageSource object { type, url }



type: "url"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

url: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.url)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.source)

type: "image"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#image_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.cache_control)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.content%5B1%5D)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.content)

type: "content"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)



URLPDFSource object { type, url }



type: "url"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)

url: string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.url)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.source)

type: "document"



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#document_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



enabled: optional boolean



[](#document_block_param.citations%20%2B%20(resource)%20messages.enabled)

[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.citations)

context: optional string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.context)

title: optional string



[](#web_fetch_block_param.content%20%2B%20(resource)%20messages.title)

[](#web_fetch_block_param.content)

type: "web_fetch_result"



[](#web_fetch_block_param.type)

url: string



Fetched content URL

[](#web_fetch_block_param.url)

retrieved_at: optional string



ISO 8601 timestamp when the content was retrieved

[](#web_fetch_block_param.retrieved_at)

[](#web_fetch_block_param)

[](#web_fetch_tool_result_block_param.content)

tool_use_id: string



[](#web_fetch_tool_result_block_param.tool_use_id)

type: "web_fetch_tool_result"



[](#web_fetch_tool_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_fetch_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_fetch_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_fetch_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_fetch_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_fetch_tool_result_block_param.cache_control)



caller: optional [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#web_fetch_tool_result_block_param.caller)

[](#web_fetch_tool_result_block_param)



CodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [CodeExecutionToolResultBlockParamContent](/docs/en/api/messages#code_execution_tool_result_block_param_content)



Code execution result with encrypted stdout for PFC + web_search results.

One of the following:



CodeExecutionToolResultErrorParam object { error_code, type }





error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B3%5D)

[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.error_code)

type: "code_execution_tool_result_error"



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages)



CodeExecutionResultBlockParam object { content, return_code, stderr, 2 more }





content: array of [CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type }



file_id: string



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.file_id)

type: "code_execution_output"



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.content)

return_code: number



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.stderr)

stdout: string



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.stdout)

type: "code_execution_result"



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages)



EncryptedCodeExecutionResultBlockParam object { content, encrypted_stdout, return_code, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.



content: array of [CodeExecutionOutputBlockParam](/docs/en/api/messages#code_execution_output_block_param) { file_id, type }



file_id: string



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.file_id)

type: "code_execution_output"



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.content)

encrypted_stdout: string



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.encrypted_stdout)

return_code: number



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.stderr)

type: "encrypted_code_execution_result"



[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block_param.content%20%2B%20(resource)%20messages)

[](#code_execution_tool_result_block_param.content)

tool_use_id: string



[](#code_execution_tool_result_block_param.tool_use_id)

type: "code_execution_tool_result"



[](#code_execution_tool_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#code_execution_tool_result_block_param.cache_control)

[](#code_execution_tool_result_block_param)



BashCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [BashCodeExecutionToolResultErrorParam](/docs/en/api/messages#bash_code_execution_tool_result_error_param) { error_code, type } or [BashCodeExecutionResultBlockParam](/docs/en/api/messages#bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }



One of the following:



BashCodeExecutionToolResultErrorParam object { error_code, type }





error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#bash_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#bash_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#bash_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#bash_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B3%5D)

"output_file_too_large"



[](#bash_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B4%5D)

[](#bash_code_execution_tool_result_error_param.error_code)

type: "bash_code_execution_tool_result_error"



[](#bash_code_execution_tool_result_error_param.type)

[](#bash_code_execution_tool_result_error_param)



BashCodeExecutionResultBlockParam object { content, return_code, stderr, 2 more }





content: array of [BashCodeExecutionOutputBlockParam](/docs/en/api/messages#bash_code_execution_output_block_param) { file_id, type }



file_id: string



[](#bash_code_execution_output_block_param.file_id)

type: "bash_code_execution_output"



[](#bash_code_execution_output_block_param.type)

[](#bash_code_execution_result_block_param.content)

return_code: number



[](#bash_code_execution_result_block_param.return_code)

stderr: string



[](#bash_code_execution_result_block_param.stderr)

stdout: string



[](#bash_code_execution_result_block_param.stdout)

type: "bash_code_execution_result"



[](#bash_code_execution_result_block_param.type)

[](#bash_code_execution_result_block_param)

[](#bash_code_execution_tool_result_block_param.content)

tool_use_id: string



[](#bash_code_execution_tool_result_block_param.tool_use_id)

type: "bash_code_execution_tool_result"



[](#bash_code_execution_tool_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#bash_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#bash_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#bash_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#bash_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#bash_code_execution_tool_result_block_param.cache_control)

[](#bash_code_execution_tool_result_block_param)



TextEditorCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [TextEditorCodeExecutionToolResultErrorParam](/docs/en/api/messages#text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } or [TextEditorCodeExecutionViewResultBlockParam](/docs/en/api/messages#text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } or [TextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/messages#text_editor_code_execution_create_result_block_param) { is_file_update, type } or [TextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }



One of the following:



TextEditorCodeExecutionToolResultErrorParam object { error_code, type, error_message }





error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B3%5D)

"file_not_found"



[](#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B4%5D)

[](#text_editor_code_execution_tool_result_error_param.error_code)

type: "text_editor_code_execution_tool_result_error"



[](#text_editor_code_execution_tool_result_error_param.type)

error_message: optional string



[](#text_editor_code_execution_tool_result_error_param.error_message)

[](#text_editor_code_execution_tool_result_error_param)



TextEditorCodeExecutionViewResultBlockParam object { content, file_type, type, 3 more }



content: string



[](#text_editor_code_execution_view_result_block_param.content)



file_type: "text" or "image" or "pdf"



One of the following:

"text"



[](#text_editor_code_execution_view_result_block_param.file_type%5B0%5D)

"image"



[](#text_editor_code_execution_view_result_block_param.file_type%5B1%5D)

"pdf"



[](#text_editor_code_execution_view_result_block_param.file_type%5B2%5D)

[](#text_editor_code_execution_view_result_block_param.file_type)

type: "text_editor_code_execution_view_result"



[](#text_editor_code_execution_view_result_block_param.type)

num_lines: optional number



[](#text_editor_code_execution_view_result_block_param.num_lines)

start_line: optional number



[](#text_editor_code_execution_view_result_block_param.start_line)

total_lines: optional number



[](#text_editor_code_execution_view_result_block_param.total_lines)

[](#text_editor_code_execution_view_result_block_param)



TextEditorCodeExecutionCreateResultBlockParam object { is_file_update, type }



is_file_update: boolean



[](#text_editor_code_execution_create_result_block_param.is_file_update)

type: "text_editor_code_execution_create_result"



[](#text_editor_code_execution_create_result_block_param.type)

[](#text_editor_code_execution_create_result_block_param)



TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new_lines, 3 more }



type: "text_editor_code_execution_str_replace_result"



[](#text_editor_code_execution_str_replace_result_block_param.type)

lines: optional array of string



[](#text_editor_code_execution_str_replace_result_block_param.lines)

new_lines: optional number



[](#text_editor_code_execution_str_replace_result_block_param.new_lines)

new_start: optional number



[](#text_editor_code_execution_str_replace_result_block_param.new_start)

old_lines: optional number



[](#text_editor_code_execution_str_replace_result_block_param.old_lines)

old_start: optional number



[](#text_editor_code_execution_str_replace_result_block_param.old_start)

[](#text_editor_code_execution_str_replace_result_block_param)

[](#text_editor_code_execution_tool_result_block_param.content)

tool_use_id: string



[](#text_editor_code_execution_tool_result_block_param.tool_use_id)

type: "text_editor_code_execution_tool_result"



[](#text_editor_code_execution_tool_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_editor_code_execution_tool_result_block_param.cache_control)

[](#text_editor_code_execution_tool_result_block_param)



ToolSearchToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [ToolSearchToolResultErrorParam](/docs/en/api/messages#tool_search_tool_result_error_param) { error_code, type, error_message } or [ToolSearchToolSearchResultBlockParam](/docs/en/api/messages#tool_search_tool_search_result_block_param) { tool_references, type }



One of the following:



ToolSearchToolResultErrorParam object { error_code, type, error_message }





error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#tool_search_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#tool_search_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#tool_search_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#tool_search_tool_result_error_param.error_code%20%2B%20(resource)%20messages%5B3%5D)

[](#tool_search_tool_result_error_param.error_code)

type: "tool_search_tool_result_error"



[](#tool_search_tool_result_error_param.type)

error_message: optional string



[](#tool_search_tool_result_error_param.error_message)

[](#tool_search_tool_result_error_param)



ToolSearchToolSearchResultBlockParam object { tool_references, type }





tool_references: array of [ToolReferenceBlockParam](/docs/en/api/messages#tool_reference_block_param) { tool_name, type, cache_control }



tool_name: string



[](#tool_reference_block_param.tool_name)

type: "tool_reference"



[](#tool_reference_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_reference_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_reference_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_reference_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_reference_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_reference_block_param.cache_control)

[](#tool_search_tool_search_result_block_param.tool_references)

type: "tool_search_tool_search_result"



[](#tool_search_tool_search_result_block_param.type)

[](#tool_search_tool_search_result_block_param)

[](#tool_search_tool_result_block_param.content)

tool_use_id: string



[](#tool_search_tool_result_block_param.tool_use_id)

type: "tool_search_tool_result"



[](#tool_search_tool_result_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_search_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_search_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_search_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_search_tool_result_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_search_tool_result_block_param.cache_control)

[](#tool_search_tool_result_block_param)



ContainerUploadBlockParam object { file_id, type, cache_control }



A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string



[](#container_upload_block_param.file_id)

type: "container_upload"



[](#container_upload_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#container_upload_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#container_upload_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#container_upload_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#container_upload_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#container_upload_block_param.cache_control)

[](#container_upload_block_param)



MidConversationSystemBlockParam object { content, type, cache_control }



System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific point in the conversation, rather than only via the top-level `system` parameter.



content: array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }



System instruction text blocks.

text: string



[](#text_block_param.text)

type: "text"



[](#text_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_block_param.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_char_location_param.cited_text)

document_index: number



[](#citation_char_location_param.document_index)

document_title: string



[](#citation_char_location_param.document_title)

end_char_index: number



[](#citation_char_location_param.end_char_index)

start_char_index: number



[](#citation_char_location_param.start_char_index)

type: "char_location"



[](#citation_char_location_param.type)

[](#citation_char_location_param)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_page_location_param.cited_text)

document_index: number



[](#citation_page_location_param.document_index)

document_title: string



[](#citation_page_location_param.document_title)

end_page_number: number



[](#citation_page_location_param.end_page_number)

start_page_number: number



[](#citation_page_location_param.start_page_number)

type: "page_location"



[](#citation_page_location_param.type)

[](#citation_page_location_param)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location_param.cited_text)

document_index: number



[](#citation_content_block_location_param.document_index)

document_title: string



[](#citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#citation_content_block_location_param.type)

[](#citation_content_block_location_param)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#citation_web_search_result_location_param.encrypted_index)

title: string



[](#citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#citation_web_search_result_location_param.type)

url: string



[](#citation_web_search_result_location_param.url)

[](#citation_web_search_result_location_param)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citation_search_result_location_param.search_result_index)

source: string



[](#citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_search_result_location_param.start_block_index)

title: string



[](#citation_search_result_location_param.title)

type: "search_result_location"



[](#citation_search_result_location_param.type)

[](#citation_search_result_location_param)

[](#text_block_param.citations)

[](#mid_conversation_system_block_param.content)

type: "mid_conv_system"



[](#mid_conversation_system_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#mid_conversation_system_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#mid_conversation_system_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#mid_conversation_system_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#mid_conversation_system_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#mid_conversation_system_block_param.cache_control)

[](#mid_conversation_system_block_param)

[](#message_param.content%5B1%5D)

[](#message_param.content)



role: "user" or "assistant" or "system"



One of the following:

"user"



[](#message_param.role%5B0%5D)

"assistant"



[](#message_param.role%5B1%5D)

"system"



[](#message_param.role%5B2%5D)

[](#message_param.role)

[](#create.messages)



model: [Model](/docs/en/api/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 14 more



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#create.model%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#create.model%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#create.model%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#create.model%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#create.model%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#create.model%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#create.model%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#create.model%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#create.model%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B16%5D)

[](#create.model%5B0%5D)

string



[](#create.model%5B1%5D)

[](#create.model)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

type: "ephemeral"



[](#create.cache_control.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#create.cache_control.ttl%5B0%5D)

"1h"



[](#create.cache_control.ttl%5B1%5D)

[](#create.cache_control.ttl)

[](#create.cache_control)

container: optional string



Container identifier for reuse across requests.

[](#create.container)

inference_geo: optional string



Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

[](#create.inference_geo)



metadata: optional [Metadata](/docs/en/api/messages#metadata) { user_id }



An object describing metadata about the request.



user_id: optional string



An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

[](#create.metadata.user_id)

[](#create.metadata)



output_config: optional [OutputConfig](/docs/en/api/messages#output_config) { effort, format }



Configuration options for the model's output, such as the output format.



effort: optional "low" or "medium" or "high" or 2 more



All possible effort levels.

One of the following:

"low"



[](#create.output_config.effort%5B0%5D)

"medium"



[](#create.output_config.effort%5B1%5D)

"high"



[](#create.output_config.effort%5B2%5D)

"xhigh"



[](#create.output_config.effort%5B3%5D)

"max"



[](#create.output_config.effort%5B4%5D)

[](#create.output_config.effort)



format: optional [JSONOutputFormat](/docs/en/api/messages#json_output_format) { schema, type }



A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: map\[unknown\]



The JSON schema of the format

[](#output_config.format%20%2B%20(resource)%20messages.schema)

type: "json_schema"



[](#output_config.format%20%2B%20(resource)%20messages.type)

[](#create.output_config.format)

[](#create.output_config)



service_tier: optional "auto" or "standard_only"



Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

One of the following:

"auto"



[](#create.service_tier%5B0%5D)

"standard_only"



[](#create.service_tier%5B1%5D)

[](#create.service_tier)



stop_sequences: optional array of string



Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

[](#create.stop_sequences)



stream: optional boolean



Whether to incrementally stream the response using server-sent events.

See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

[](#create.stream)



system: optional string or array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }



System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

One of the following:

string



[](#create.system%5B0%5D)



array of [TextBlockParam](/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }



text: string



[](#text_block_param.text)

type: "text"



[](#text_block_param.type)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#text_block_param.cache_control%20%2B%20(resource)%20messages.ttl)

[](#text_block_param.cache_control)



citations: optional array of [TextCitationParam](/docs/en/api/messages#text_citation_param)



One of the following:



CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_char_location_param.cited_text)

document_index: number



[](#citation_char_location_param.document_index)

document_title: string



[](#citation_char_location_param.document_title)

end_char_index: number



[](#citation_char_location_param.end_char_index)

start_char_index: number



[](#citation_char_location_param.start_char_index)

type: "char_location"



[](#citation_char_location_param.type)

[](#citation_char_location_param)



CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#citation_page_location_param.cited_text)

document_index: number



[](#citation_page_location_param.document_index)

document_title: string



[](#citation_page_location_param.document_title)

end_page_number: number



[](#citation_page_location_param.end_page_number)

start_page_number: number



[](#citation_page_location_param.start_page_number)

type: "page_location"



[](#citation_page_location_param.type)

[](#citation_page_location_param)



CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location_param.cited_text)

document_index: number



[](#citation_content_block_location_param.document_index)

document_title: string



[](#citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#citation_content_block_location_param.type)

[](#citation_content_block_location_param)



CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#citation_web_search_result_location_param.encrypted_index)

title: string



[](#citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#citation_web_search_result_location_param.type)

url: string



[](#citation_web_search_result_location_param.url)

[](#citation_web_search_result_location_param)



CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citation_search_result_location_param.search_result_index)

source: string



[](#citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_search_result_location_param.start_block_index)

title: string



[](#citation_search_result_location_param.title)

type: "search_result_location"



[](#citation_search_result_location_param.type)

[](#citation_search_result_location_param)

[](#text_block_param.citations)

[](#create.system%5B1%5D)

[](#create.system)



thinking: optional [ThinkingConfigParam](/docs/en/api/messages#thinking_config_param)



Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

One of the following:



ThinkingConfigEnabled object { budget_tokens, type, display }





budget_tokens: number



Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

minimum1024

[](#create.thinking.budget_tokens)

type: "enabled"



[](#create.thinking.type)



display: optional "summarized" or "omitted"



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



[](#create.thinking.display%5B0%5D)

"omitted"



[](#create.thinking.display%5B1%5D)

[](#create.thinking.display)

[](#create.thinking)



ThinkingConfigDisabled object { type }



type: "disabled"



[](#create.thinking.type)

[](#create.thinking)



ThinkingConfigAdaptive object { type, display }



type: "adaptive"



[](#create.thinking.type)



display: optional "summarized" or "omitted"



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



[](#create.thinking.display%5B0%5D)

"omitted"



[](#create.thinking.display%5B1%5D)

[](#create.thinking.display)

[](#create.thinking)

[](#create.thinking)



tool_choice: optional [ToolChoice](/docs/en/api/messages#tool_choice)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



ToolChoiceAuto object { type, disable_parallel_tool_use }



The model will automatically decide whether to use tools.

type: "auto"



[](#create.tool_choice.type)



disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

[](#create.tool_choice.disable_parallel_tool_use)

[](#create.tool_choice)



ToolChoiceAny object { type, disable_parallel_tool_use }



The model will use any available tools.

type: "any"



[](#create.tool_choice.type)



disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[](#create.tool_choice.disable_parallel_tool_use)

[](#create.tool_choice)



ToolChoiceTool object { name, type, disable_parallel_tool_use }



The model will use the specified tool with `tool_choice.name`.

name: string



The name of the tool to use.

[](#create.tool_choice.name)

type: "tool"



[](#create.tool_choice.type)



disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[](#create.tool_choice.disable_parallel_tool_use)

[](#create.tool_choice)



ToolChoiceNone object { type }



The model will not be allowed to use tools.

type: "none"



[](#create.tool_choice.type)

[](#create.tool_choice)

[](#create.tool_choice)



tools: optional array of [ToolUnion](/docs/en/api/messages#tool_union)



Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)).

Each tool definition includes:

- `name`: Name of the tool.
- `description`: Optional, but strongly-recommended description of the tool.
- `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

For example, if you defined `tools` as:

```python
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



And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

```python
[
  {
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
  }
]
```



You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

```python
[
  {
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
  }
]
```



Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for more details.

One of the following:



Tool object { input_schema, name, allowed_callers, 7 more }





input_schema: object { type, properties, required }



[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"



[](#tool.input_schema.type)

properties: optional map\[unknown\]



[](#tool.input_schema.properties)

required: optional array of string



[](#tool.input_schema.required)

[](#tool.input_schema)



name: string



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

[](#tool.name)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#tool.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#tool.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#tool.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#tool.allowed_callers.items%5B3%5D)

[](#tool.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#tool.defer_loading)



description: optional string



Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

[](#tool.description)

eager_input_streaming: optional boolean



Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

[](#tool.eager_input_streaming)

input_examples: optional array of map\[unknown\]



[](#tool.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#tool.strict)

type: optional "custom"



[](#tool.type)

[](#tool)



ToolBash20250124 object { name, type, allowed_callers, 4 more }





name: "bash"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#tool_bash_20250124.name)

type: "bash_20250124"



[](#tool_bash_20250124.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#tool_bash_20250124.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#tool_bash_20250124.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#tool_bash_20250124.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#tool_bash_20250124.allowed_callers.items%5B3%5D)

[](#tool_bash_20250124.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_bash_20250124.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_bash_20250124.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_bash_20250124.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_bash_20250124.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_bash_20250124.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#tool_bash_20250124.defer_loading)

input_examples: optional array of map\[unknown\]



[](#tool_bash_20250124.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#tool_bash_20250124.strict)

[](#tool_bash_20250124)



CodeExecutionTool20250522 object { name, type, allowed_callers, 3 more }





name: "code_execution"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#code_execution_tool_20250522.name)

type: "code_execution_20250522"



[](#code_execution_tool_20250522.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#code_execution_tool_20250522.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#code_execution_tool_20250522.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#code_execution_tool_20250522.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#code_execution_tool_20250522.allowed_callers.items%5B3%5D)

[](#code_execution_tool_20250522.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#code_execution_tool_20250522.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#code_execution_tool_20250522.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#code_execution_tool_20250522.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#code_execution_tool_20250522.cache_control%20%2B%20(resource)%20messages.ttl)

[](#code_execution_tool_20250522.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#code_execution_tool_20250522.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#code_execution_tool_20250522.strict)

[](#code_execution_tool_20250522)



CodeExecutionTool20250825 object { name, type, allowed_callers, 3 more }





name: "code_execution"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#code_execution_tool_20250825.name)

type: "code_execution_20250825"



[](#code_execution_tool_20250825.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#code_execution_tool_20250825.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#code_execution_tool_20250825.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#code_execution_tool_20250825.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#code_execution_tool_20250825.allowed_callers.items%5B3%5D)

[](#code_execution_tool_20250825.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#code_execution_tool_20250825.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#code_execution_tool_20250825.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#code_execution_tool_20250825.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#code_execution_tool_20250825.cache_control%20%2B%20(resource)%20messages.ttl)

[](#code_execution_tool_20250825.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#code_execution_tool_20250825.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#code_execution_tool_20250825.strict)

[](#code_execution_tool_20250825)



CodeExecutionTool20260120 object { name, type, allowed_callers, 3 more }



Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code_execution"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#code_execution_tool_20260120.name)

type: "code_execution_20260120"



[](#code_execution_tool_20260120.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#code_execution_tool_20260120.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#code_execution_tool_20260120.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#code_execution_tool_20260120.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#code_execution_tool_20260120.allowed_callers.items%5B3%5D)

[](#code_execution_tool_20260120.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#code_execution_tool_20260120.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#code_execution_tool_20260120.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#code_execution_tool_20260120.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#code_execution_tool_20260120.cache_control%20%2B%20(resource)%20messages.ttl)

[](#code_execution_tool_20260120.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#code_execution_tool_20260120.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#code_execution_tool_20260120.strict)

[](#code_execution_tool_20260120)



CodeExecutionTool20260521 object { name, type, allowed_callers, 3 more }



Code execution tool with REPL state persistence.



name: "code_execution"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#code_execution_tool_20260521.name)

type: "code_execution_20260521"



[](#code_execution_tool_20260521.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#code_execution_tool_20260521.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#code_execution_tool_20260521.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#code_execution_tool_20260521.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#code_execution_tool_20260521.allowed_callers.items%5B3%5D)

[](#code_execution_tool_20260521.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#code_execution_tool_20260521.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#code_execution_tool_20260521.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#code_execution_tool_20260521.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#code_execution_tool_20260521.cache_control%20%2B%20(resource)%20messages.ttl)

[](#code_execution_tool_20260521.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#code_execution_tool_20260521.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#code_execution_tool_20260521.strict)

[](#code_execution_tool_20260521)



MemoryTool20250818 object { name, type, allowed_callers, 4 more }





name: "memory"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#memory_tool_20250818.name)

type: "memory_20250818"



[](#memory_tool_20250818.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#memory_tool_20250818.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#memory_tool_20250818.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#memory_tool_20250818.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#memory_tool_20250818.allowed_callers.items%5B3%5D)

[](#memory_tool_20250818.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#memory_tool_20250818.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#memory_tool_20250818.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#memory_tool_20250818.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#memory_tool_20250818.cache_control%20%2B%20(resource)%20messages.ttl)

[](#memory_tool_20250818.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#memory_tool_20250818.defer_loading)

input_examples: optional array of map\[unknown\]



[](#memory_tool_20250818.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#memory_tool_20250818.strict)

[](#memory_tool_20250818)



ToolTextEditor20250124 object { name, type, allowed_callers, 4 more }





name: "str_replace_editor"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#tool_text_editor_20250124.name)

type: "text_editor_20250124"



[](#tool_text_editor_20250124.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#tool_text_editor_20250124.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#tool_text_editor_20250124.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#tool_text_editor_20250124.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#tool_text_editor_20250124.allowed_callers.items%5B3%5D)

[](#tool_text_editor_20250124.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_text_editor_20250124.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_text_editor_20250124.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_text_editor_20250124.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_text_editor_20250124.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_text_editor_20250124.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#tool_text_editor_20250124.defer_loading)

input_examples: optional array of map\[unknown\]



[](#tool_text_editor_20250124.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#tool_text_editor_20250124.strict)

[](#tool_text_editor_20250124)



ToolTextEditor20250429 object { name, type, allowed_callers, 4 more }





name: "str_replace_based_edit_tool"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#tool_text_editor_20250429.name)

type: "text_editor_20250429"



[](#tool_text_editor_20250429.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#tool_text_editor_20250429.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#tool_text_editor_20250429.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#tool_text_editor_20250429.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#tool_text_editor_20250429.allowed_callers.items%5B3%5D)

[](#tool_text_editor_20250429.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_text_editor_20250429.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_text_editor_20250429.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_text_editor_20250429.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_text_editor_20250429.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_text_editor_20250429.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#tool_text_editor_20250429.defer_loading)

input_examples: optional array of map\[unknown\]



[](#tool_text_editor_20250429.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#tool_text_editor_20250429.strict)

[](#tool_text_editor_20250429)



ToolTextEditor20250728 object { name, type, allowed_callers, 5 more }





name: "str_replace_based_edit_tool"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#tool_text_editor_20250728.name)

type: "text_editor_20250728"



[](#tool_text_editor_20250728.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#tool_text_editor_20250728.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#tool_text_editor_20250728.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#tool_text_editor_20250728.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#tool_text_editor_20250728.allowed_callers.items%5B3%5D)

[](#tool_text_editor_20250728.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_text_editor_20250728.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_text_editor_20250728.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_text_editor_20250728.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_text_editor_20250728.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_text_editor_20250728.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#tool_text_editor_20250728.defer_loading)

input_examples: optional array of map\[unknown\]



[](#tool_text_editor_20250728.input_examples)

max_characters: optional number



Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

[](#tool_text_editor_20250728.max_characters)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#tool_text_editor_20250728.strict)

[](#tool_text_editor_20250728)



WebSearchTool20250305 object { name, type, allowed_callers, 7 more }





name: "web_search"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#web_search_tool_20250305.name)

type: "web_search_20250305"



[](#web_search_tool_20250305.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#web_search_tool_20250305.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#web_search_tool_20250305.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#web_search_tool_20250305.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#web_search_tool_20250305.allowed_callers.items%5B3%5D)

[](#web_search_tool_20250305.allowed_callers)

allowed_domains: optional array of string



If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

[](#web_search_tool_20250305.allowed_domains)

blocked_domains: optional array of string



If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[](#web_search_tool_20250305.blocked_domains)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_search_tool_20250305.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_search_tool_20250305.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_search_tool_20250305.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_search_tool_20250305.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_search_tool_20250305.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#web_search_tool_20250305.defer_loading)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#web_search_tool_20250305.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#web_search_tool_20250305.strict)



user_location: optional [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more }



Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"



[](#web_search_tool_20250305.user_location%20%2B%20(resource)%20messages.type)

city: optional string



The city of the user.

[](#web_search_tool_20250305.user_location%20%2B%20(resource)%20messages.city)

country: optional string



The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

[](#web_search_tool_20250305.user_location%20%2B%20(resource)%20messages.country)

region: optional string



The region of the user.

[](#web_search_tool_20250305.user_location%20%2B%20(resource)%20messages.region)

timezone: optional string



The [IANA timezone](https://nodatime.org/TimeZones) of the user.

[](#web_search_tool_20250305.user_location%20%2B%20(resource)%20messages.timezone)

[](#web_search_tool_20250305.user_location)

[](#web_search_tool_20250305)



WebFetchTool20250910 object { name, type, allowed_callers, 8 more }





name: "web_fetch"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#web_fetch_tool_20250910.name)

type: "web_fetch_20250910"



[](#web_fetch_tool_20250910.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#web_fetch_tool_20250910.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#web_fetch_tool_20250910.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#web_fetch_tool_20250910.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#web_fetch_tool_20250910.allowed_callers.items%5B3%5D)

[](#web_fetch_tool_20250910.allowed_callers)

allowed_domains: optional array of string



List of domains to allow fetching from

[](#web_fetch_tool_20250910.allowed_domains)

blocked_domains: optional array of string



List of domains to block fetching from

[](#web_fetch_tool_20250910.blocked_domains)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_fetch_tool_20250910.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_fetch_tool_20250910.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_fetch_tool_20250910.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_fetch_tool_20250910.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_fetch_tool_20250910.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean



[](#web_fetch_tool_20250910.citations%20%2B%20(resource)%20messages.enabled)

[](#web_fetch_tool_20250910.citations)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#web_fetch_tool_20250910.defer_loading)

max_content_tokens: optional number



Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

[](#web_fetch_tool_20250910.max_content_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#web_fetch_tool_20250910.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#web_fetch_tool_20250910.strict)

[](#web_fetch_tool_20250910)



WebSearchTool20260209 object { name, type, allowed_callers, 7 more }





name: "web_search"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#web_search_tool_20260209.name)

type: "web_search_20260209"



[](#web_search_tool_20260209.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#web_search_tool_20260209.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#web_search_tool_20260209.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#web_search_tool_20260209.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#web_search_tool_20260209.allowed_callers.items%5B3%5D)

[](#web_search_tool_20260209.allowed_callers)

allowed_domains: optional array of string



If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

[](#web_search_tool_20260209.allowed_domains)

blocked_domains: optional array of string



If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[](#web_search_tool_20260209.blocked_domains)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_search_tool_20260209.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_search_tool_20260209.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_search_tool_20260209.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_search_tool_20260209.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_search_tool_20260209.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#web_search_tool_20260209.defer_loading)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#web_search_tool_20260209.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#web_search_tool_20260209.strict)



user_location: optional [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more }



Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"



[](#web_search_tool_20260209.user_location%20%2B%20(resource)%20messages.type)

city: optional string



The city of the user.

[](#web_search_tool_20260209.user_location%20%2B%20(resource)%20messages.city)

country: optional string



The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

[](#web_search_tool_20260209.user_location%20%2B%20(resource)%20messages.country)

region: optional string



The region of the user.

[](#web_search_tool_20260209.user_location%20%2B%20(resource)%20messages.region)

timezone: optional string



The [IANA timezone](https://nodatime.org/TimeZones) of the user.

[](#web_search_tool_20260209.user_location%20%2B%20(resource)%20messages.timezone)

[](#web_search_tool_20260209.user_location)

[](#web_search_tool_20260209)



WebFetchTool20260209 object { name, type, allowed_callers, 8 more }





name: "web_fetch"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#web_fetch_tool_20260209.name)

type: "web_fetch_20260209"



[](#web_fetch_tool_20260209.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#web_fetch_tool_20260209.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#web_fetch_tool_20260209.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#web_fetch_tool_20260209.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#web_fetch_tool_20260209.allowed_callers.items%5B3%5D)

[](#web_fetch_tool_20260209.allowed_callers)

allowed_domains: optional array of string



List of domains to allow fetching from

[](#web_fetch_tool_20260209.allowed_domains)

blocked_domains: optional array of string



List of domains to block fetching from

[](#web_fetch_tool_20260209.blocked_domains)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_fetch_tool_20260209.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_fetch_tool_20260209.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_fetch_tool_20260209.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_fetch_tool_20260209.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_fetch_tool_20260209.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean



[](#web_fetch_tool_20260209.citations%20%2B%20(resource)%20messages.enabled)

[](#web_fetch_tool_20260209.citations)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#web_fetch_tool_20260209.defer_loading)

max_content_tokens: optional number



Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

[](#web_fetch_tool_20260209.max_content_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#web_fetch_tool_20260209.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#web_fetch_tool_20260209.strict)

[](#web_fetch_tool_20260209)



WebFetchTool20260309 object { name, type, allowed_callers, 9 more }



Web fetch tool with use_cache parameter for bypassing cached content.



name: "web_fetch"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#web_fetch_tool_20260309.name)

type: "web_fetch_20260309"



[](#web_fetch_tool_20260309.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#web_fetch_tool_20260309.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#web_fetch_tool_20260309.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#web_fetch_tool_20260309.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#web_fetch_tool_20260309.allowed_callers.items%5B3%5D)

[](#web_fetch_tool_20260309.allowed_callers)

allowed_domains: optional array of string



List of domains to allow fetching from

[](#web_fetch_tool_20260309.allowed_domains)

blocked_domains: optional array of string



List of domains to block fetching from

[](#web_fetch_tool_20260309.blocked_domains)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_fetch_tool_20260309.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_fetch_tool_20260309.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_fetch_tool_20260309.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_fetch_tool_20260309.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_fetch_tool_20260309.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean



[](#web_fetch_tool_20260309.citations%20%2B%20(resource)%20messages.enabled)

[](#web_fetch_tool_20260309.citations)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#web_fetch_tool_20260309.defer_loading)

max_content_tokens: optional number



Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

[](#web_fetch_tool_20260309.max_content_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#web_fetch_tool_20260309.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#web_fetch_tool_20260309.strict)

use_cache: optional boolean



Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[](#web_fetch_tool_20260309.use_cache)

[](#web_fetch_tool_20260309)



WebSearchTool20260318 object { name, type, allowed_callers, 8 more }





name: "web_search"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#web_search_tool_20260318.name)

type: "web_search_20260318"



[](#web_search_tool_20260318.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#web_search_tool_20260318.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#web_search_tool_20260318.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#web_search_tool_20260318.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#web_search_tool_20260318.allowed_callers.items%5B3%5D)

[](#web_search_tool_20260318.allowed_callers)

allowed_domains: optional array of string



If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

[](#web_search_tool_20260318.allowed_domains)

blocked_domains: optional array of string



If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[](#web_search_tool_20260318.blocked_domains)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_search_tool_20260318.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_search_tool_20260318.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_search_tool_20260318.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_search_tool_20260318.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_search_tool_20260318.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#web_search_tool_20260318.defer_loading)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#web_search_tool_20260318.max_uses)



response_inclusion: optional "full" or "excluded"



How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"



[](#web_search_tool_20260318.response_inclusion%5B0%5D)

"excluded"



[](#web_search_tool_20260318.response_inclusion%5B1%5D)

[](#web_search_tool_20260318.response_inclusion)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#web_search_tool_20260318.strict)



user_location: optional [UserLocation](/docs/en/api/messages#user_location) { type, city, country, 2 more }



Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"



[](#web_search_tool_20260318.user_location%20%2B%20(resource)%20messages.type)

city: optional string



The city of the user.

[](#web_search_tool_20260318.user_location%20%2B%20(resource)%20messages.city)

country: optional string



The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

[](#web_search_tool_20260318.user_location%20%2B%20(resource)%20messages.country)

region: optional string



The region of the user.

[](#web_search_tool_20260318.user_location%20%2B%20(resource)%20messages.region)

timezone: optional string



The [IANA timezone](https://nodatime.org/TimeZones) of the user.

[](#web_search_tool_20260318.user_location%20%2B%20(resource)%20messages.timezone)

[](#web_search_tool_20260318.user_location)

[](#web_search_tool_20260318)



WebFetchTool20260318 object { name, type, allowed_callers, 10 more }





name: "web_fetch"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#web_fetch_tool_20260318.name)

type: "web_fetch_20260318"



[](#web_fetch_tool_20260318.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#web_fetch_tool_20260318.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#web_fetch_tool_20260318.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#web_fetch_tool_20260318.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#web_fetch_tool_20260318.allowed_callers.items%5B3%5D)

[](#web_fetch_tool_20260318.allowed_callers)

allowed_domains: optional array of string



List of domains to allow fetching from

[](#web_fetch_tool_20260318.allowed_domains)

blocked_domains: optional array of string



List of domains to block fetching from

[](#web_fetch_tool_20260318.blocked_domains)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#web_fetch_tool_20260318.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#web_fetch_tool_20260318.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#web_fetch_tool_20260318.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#web_fetch_tool_20260318.cache_control%20%2B%20(resource)%20messages.ttl)

[](#web_fetch_tool_20260318.cache_control)



citations: optional [CitationsConfigParam](/docs/en/api/messages#citations_config_param) { enabled }



Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean



[](#web_fetch_tool_20260318.citations%20%2B%20(resource)%20messages.enabled)

[](#web_fetch_tool_20260318.citations)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#web_fetch_tool_20260318.defer_loading)

max_content_tokens: optional number



Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

[](#web_fetch_tool_20260318.max_content_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#web_fetch_tool_20260318.max_uses)



response_inclusion: optional "full" or "excluded"



How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"



[](#web_fetch_tool_20260318.response_inclusion%5B0%5D)

"excluded"



[](#web_fetch_tool_20260318.response_inclusion%5B1%5D)

[](#web_fetch_tool_20260318.response_inclusion)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#web_fetch_tool_20260318.strict)

use_cache: optional boolean



Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[](#web_fetch_tool_20260318.use_cache)

[](#web_fetch_tool_20260318)



ToolSearchToolBm25_20251119 object { name, type, allowed_callers, 3 more }





name: "tool_search_tool_bm25"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#tool_search_tool_bm25_20251119.name)



type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"



One of the following:

"tool_search_tool_bm25_20251119"



[](#tool_search_tool_bm25_20251119.type%5B0%5D)

"tool_search_tool_bm25"



[](#tool_search_tool_bm25_20251119.type%5B1%5D)

[](#tool_search_tool_bm25_20251119.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#tool_search_tool_bm25_20251119.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#tool_search_tool_bm25_20251119.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#tool_search_tool_bm25_20251119.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#tool_search_tool_bm25_20251119.allowed_callers.items%5B3%5D)

[](#tool_search_tool_bm25_20251119.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_search_tool_bm25_20251119.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_search_tool_bm25_20251119.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_search_tool_bm25_20251119.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_search_tool_bm25_20251119.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_search_tool_bm25_20251119.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#tool_search_tool_bm25_20251119.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#tool_search_tool_bm25_20251119.strict)

[](#tool_search_tool_bm25_20251119)



ToolSearchToolRegex20251119 object { name, type, allowed_callers, 3 more }





name: "tool_search_tool_regex"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#tool_search_tool_regex_20251119.name)



type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"



One of the following:

"tool_search_tool_regex_20251119"



[](#tool_search_tool_regex_20251119.type%5B0%5D)

"tool_search_tool_regex"



[](#tool_search_tool_regex_20251119.type%5B1%5D)

[](#tool_search_tool_regex_20251119.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#tool_search_tool_regex_20251119.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#tool_search_tool_regex_20251119.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#tool_search_tool_regex_20251119.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#tool_search_tool_regex_20251119.allowed_callers.items%5B3%5D)

[](#tool_search_tool_regex_20251119.allowed_callers)



cache_control: optional [CacheControlEphemeral](/docs/en/api/messages#cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#tool_search_tool_regex_20251119.cache_control%20%2B%20(resource)%20messages.type)



ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



[](#tool_search_tool_regex_20251119.cache_control%20%2B%20(resource)%20messages.ttl%5B0%5D)

"1h"



[](#tool_search_tool_regex_20251119.cache_control%20%2B%20(resource)%20messages.ttl%5B1%5D)

[](#tool_search_tool_regex_20251119.cache_control%20%2B%20(resource)%20messages.ttl)

[](#tool_search_tool_regex_20251119.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#tool_search_tool_regex_20251119.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#tool_search_tool_regex_20251119.strict)

[](#tool_search_tool_regex_20251119)

[](#create.tools)



temperature: optional number⁠Deprecated



Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

[](#create.temperature)



top_k: optional number⁠Deprecated



Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0

[](#create.top_k)



top_p: optional number⁠Deprecated



Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value \>= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

[](#create.top_p)

##### ReturnsExpand Collapse 



Message object { id, container, content, 7 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#message.id)



container: [Container](/docs/en/api/messages#container) { id, expires_at }



Information about the container used in the request (for the code execution tool)

id: string



Identifier for the container used in this request

[](#message.container%20%2B%20(resource)%20messages.id)

expires_at: string



The time at which the container will expire.

[](#message.container%20%2B%20(resource)%20messages.expires_at)

[](#message.container)



content: array of [ContentBlock](/docs/en/api/messages#content_block)



Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```python
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```python
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```python
[{"type": "text", "text": "B)"}]
```



One of the following:



TextBlock object { citations, text, type }





citations: array of [TextCitation](/docs/en/api/messages#text_citation)



Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#citation_char_location.cited_text)

document_index: number



[](#citation_char_location.document_index)

document_title: string



[](#citation_char_location.document_title)

end_char_index: number



[](#citation_char_location.end_char_index)

file_id: string



[](#citation_char_location.file_id)

start_char_index: number



[](#citation_char_location.start_char_index)

type: "char_location"



[](#citation_char_location.type)

[](#citation_char_location)



CitationPageLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#citation_page_location.cited_text)

document_index: number



[](#citation_page_location.document_index)

document_title: string



[](#citation_page_location.document_title)

end_page_number: number



[](#citation_page_location.end_page_number)

file_id: string



[](#citation_page_location.file_id)

start_page_number: number



[](#citation_page_location.start_page_number)

type: "page_location"



[](#citation_page_location.type)

[](#citation_page_location)



CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location.cited_text)

document_index: number



[](#citation_content_block_location.document_index)

document_title: string



[](#citation_content_block_location.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location.end_block_index)

file_id: string



[](#citation_content_block_location.file_id)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location.start_block_index)

type: "content_block_location"



[](#citation_content_block_location.type)

[](#citation_content_block_location)



CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citations_web_search_result_location.cited_text)

encrypted_index: string



[](#citations_web_search_result_location.encrypted_index)

title: string



[](#citations_web_search_result_location.title)

type: "web_search_result_location"



[](#citations_web_search_result_location.type)

url: string



[](#citations_web_search_result_location.url)

[](#citations_web_search_result_location)



CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citations_search_result_location.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citations_search_result_location.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citations_search_result_location.search_result_index)

source: string



[](#citations_search_result_location.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citations_search_result_location.start_block_index)

title: string



[](#citations_search_result_location.title)

type: "search_result_location"



[](#citations_search_result_location.type)

[](#citations_search_result_location)

[](#text_block.citations)

text: string



[](#text_block.text)

type: "text"



[](#text_block.type)

[](#text_block)



ThinkingBlock object { signature, thinking, type }



signature: string



[](#thinking_block.signature)

thinking: string



[](#thinking_block.thinking)

type: "thinking"



[](#thinking_block.type)

[](#thinking_block)



RedactedThinkingBlock object { data, type }



data: string



[](#redacted_thinking_block.data)

type: "redacted_thinking"



[](#redacted_thinking_block.type)

[](#redacted_thinking_block)



ToolUseBlock object { id, caller, input, 2 more }



id: string



[](#tool_use_block.id)



caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#tool_use_block.caller)

input: map\[unknown\]



[](#tool_use_block.input)

name: string



[](#tool_use_block.name)

type: "tool_use"



[](#tool_use_block.type)

[](#tool_use_block)



ServerToolUseBlock object { id, caller, input, 2 more }



id: string



[](#server_tool_use_block.id)



caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#server_tool_use_block.caller)

input: map\[unknown\]



[](#server_tool_use_block.input)



name: "web_search" or "web_fetch" or "code_execution" or 4 more



One of the following:

"web_search"



[](#server_tool_use_block.name%5B0%5D)

"web_fetch"



[](#server_tool_use_block.name%5B1%5D)

"code_execution"



[](#server_tool_use_block.name%5B2%5D)

"bash_code_execution"



[](#server_tool_use_block.name%5B3%5D)

"text_editor_code_execution"



[](#server_tool_use_block.name%5B4%5D)

"tool_search_tool_regex"



[](#server_tool_use_block.name%5B5%5D)

"tool_search_tool_bm25"



[](#server_tool_use_block.name%5B6%5D)

[](#server_tool_use_block.name)

type: "server_tool_use"



[](#server_tool_use_block.type)

[](#server_tool_use_block)



WebSearchToolResultBlock object { caller, content, tool_use_id, type }





caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#web_search_tool_result_block.caller)



content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)



One of the following:



WebSearchToolResultError object { error_code, type }





error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"max_uses_exceeded"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"too_many_requests"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"query_too_long"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

"request_too_large"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B5%5D)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.error_code)

type: "web_search_tool_result_error"



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages)



array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more }



encrypted_content: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.encrypted_content)

page_age: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.page_age)

title: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.title)

type: "web_search_result"



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.type)

url: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.url)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages%5B1%5D)

[](#web_search_tool_result_block.content)

tool_use_id: string



[](#web_search_tool_result_block.tool_use_id)

type: "web_search_tool_result"



[](#web_search_tool_result_block.type)

[](#web_search_tool_result_block)



WebFetchToolResultBlock object { caller, content, tool_use_id, type }





caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#web_fetch_tool_result_block.caller)



content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } or [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }



One of the following:



WebFetchToolResultErrorBlock object { error_code, type }





error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B0%5D)

"url_too_long"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B1%5D)

"url_not_allowed"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B2%5D)

"url_not_in_prior_context"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B3%5D)

"url_not_accessible"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B4%5D)

"unsupported_content_type"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B5%5D)

"too_many_requests"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B6%5D)

"max_uses_exceeded"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B7%5D)

"unavailable"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B8%5D)

[](#web_fetch_tool_result_error_block.error_code)

type: "web_fetch_tool_result_error"



[](#web_fetch_tool_result_error_block.type)

[](#web_fetch_tool_result_error_block)



WebFetchBlock object { content, retrieved_at, type, url }





content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }





citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled }



Citation configuration for the document

enabled: boolean



[](#document_block.citations%20%2B%20(resource)%20messages.enabled)

[](#web_fetch_block.content%20%2B%20(resource)%20messages.citations)



source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }



One of the following:



Base64PDFSource object { data, media_type, type }



data: string



[](#web_fetch_block.content%20%2B%20(resource)%20messages.data)

media_type: "application/pdf"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.media_type)

type: "base64"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block.content%20%2B%20(resource)%20messages)



PlainTextSource object { data, media_type, type }



data: string



[](#web_fetch_block.content%20%2B%20(resource)%20messages.data)

media_type: "text/plain"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.media_type)

type: "text"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block.content%20%2B%20(resource)%20messages)

[](#web_fetch_block.content%20%2B%20(resource)%20messages.source)

title: string



The title of the document

[](#web_fetch_block.content%20%2B%20(resource)%20messages.title)

type: "document"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block.content)

retrieved_at: string



ISO 8601 timestamp when the content was retrieved

[](#web_fetch_block.retrieved_at)

type: "web_fetch_result"



[](#web_fetch_block.type)

url: string



Fetched content URL

[](#web_fetch_block.url)

[](#web_fetch_block)

[](#web_fetch_tool_result_block.content)

tool_use_id: string



[](#web_fetch_tool_result_block.tool_use_id)

type: "web_fetch_tool_result"



[](#web_fetch_tool_result_block.type)

[](#web_fetch_tool_result_block)



CodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)



Code execution result with encrypted stdout for PFC + web_search results.

One of the following:



CodeExecutionToolResultError object { error_code, type }





error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.error_code)

type: "code_execution_tool_result_error"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)



CodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type }



file_id: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.file_id)

type: "code_execution_output"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.content)

return_code: number



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stderr)

stdout: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stdout)

type: "code_execution_result"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)



EncryptedCodeExecutionResultBlock object { content, encrypted_stdout, return_code, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.



content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type }



file_id: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.file_id)

type: "code_execution_output"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.content)

encrypted_stdout: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.encrypted_stdout)

return_code: number



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stderr)

type: "encrypted_code_execution_result"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)

[](#code_execution_tool_result_block.content)

tool_use_id: string



[](#code_execution_tool_result_block.tool_use_id)

type: "code_execution_tool_result"



[](#code_execution_tool_result_block.type)

[](#code_execution_tool_result_block)



BashCodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } or [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }



One of the following:



BashCodeExecutionToolResultError object { error_code, type }





error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"output_file_too_large"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

[](#bash_code_execution_tool_result_error.error_code)

type: "bash_code_execution_tool_result_error"



[](#bash_code_execution_tool_result_error.type)

[](#bash_code_execution_tool_result_error)



BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type }



file_id: string



[](#bash_code_execution_output_block.file_id)

type: "bash_code_execution_output"



[](#bash_code_execution_output_block.type)

[](#bash_code_execution_result_block.content)

return_code: number



[](#bash_code_execution_result_block.return_code)

stderr: string



[](#bash_code_execution_result_block.stderr)

stdout: string



[](#bash_code_execution_result_block.stdout)

type: "bash_code_execution_result"



[](#bash_code_execution_result_block.type)

[](#bash_code_execution_result_block)

[](#bash_code_execution_tool_result_block.content)

tool_use_id: string



[](#bash_code_execution_tool_result_block.tool_use_id)

type: "bash_code_execution_tool_result"



[](#bash_code_execution_tool_result_block.type)

[](#bash_code_execution_tool_result_block)



TextEditorCodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } or [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }



One of the following:



TextEditorCodeExecutionToolResultError object { error_code, error_message, type }





error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"file_not_found"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

[](#text_editor_code_execution_tool_result_error.error_code)

error_message: string



[](#text_editor_code_execution_tool_result_error.error_message)

type: "text_editor_code_execution_tool_result_error"



[](#text_editor_code_execution_tool_result_error.type)

[](#text_editor_code_execution_tool_result_error)



TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more }



content: string



[](#text_editor_code_execution_view_result_block.content)



file_type: "text" or "image" or "pdf"



One of the following:

"text"



[](#text_editor_code_execution_view_result_block.file_type%5B0%5D)

"image"



[](#text_editor_code_execution_view_result_block.file_type%5B1%5D)

"pdf"



[](#text_editor_code_execution_view_result_block.file_type%5B2%5D)

[](#text_editor_code_execution_view_result_block.file_type)

num_lines: number



[](#text_editor_code_execution_view_result_block.num_lines)

start_line: number



[](#text_editor_code_execution_view_result_block.start_line)

total_lines: number



[](#text_editor_code_execution_view_result_block.total_lines)

type: "text_editor_code_execution_view_result"



[](#text_editor_code_execution_view_result_block.type)

[](#text_editor_code_execution_view_result_block)



TextEditorCodeExecutionCreateResultBlock object { is_file_update, type }



is_file_update: boolean



[](#text_editor_code_execution_create_result_block.is_file_update)

type: "text_editor_code_execution_create_result"



[](#text_editor_code_execution_create_result_block.type)

[](#text_editor_code_execution_create_result_block)



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more }



lines: array of string



[](#text_editor_code_execution_str_replace_result_block.lines)

new_lines: number



[](#text_editor_code_execution_str_replace_result_block.new_lines)

new_start: number



[](#text_editor_code_execution_str_replace_result_block.new_start)

old_lines: number



[](#text_editor_code_execution_str_replace_result_block.old_lines)

old_start: number



[](#text_editor_code_execution_str_replace_result_block.old_start)

type: "text_editor_code_execution_str_replace_result"



[](#text_editor_code_execution_str_replace_result_block.type)

[](#text_editor_code_execution_str_replace_result_block)

[](#text_editor_code_execution_tool_result_block.content)

tool_use_id: string



[](#text_editor_code_execution_tool_result_block.tool_use_id)

type: "text_editor_code_execution_tool_result"



[](#text_editor_code_execution_tool_result_block.type)

[](#text_editor_code_execution_tool_result_block)



ToolSearchToolResultBlock object { content, tool_use_id, type }





content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } or [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }



One of the following:



ToolSearchToolResultError object { error_code, error_message, type }





error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

[](#tool_search_tool_result_error.error_code)

error_message: string



[](#tool_search_tool_result_error.error_message)

type: "tool_search_tool_result_error"



[](#tool_search_tool_result_error.type)

[](#tool_search_tool_result_error)



ToolSearchToolSearchResultBlock object { tool_references, type }





tool_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type }



tool_name: string



[](#tool_reference_block.tool_name)

type: "tool_reference"



[](#tool_reference_block.type)

[](#tool_search_tool_search_result_block.tool_references)

type: "tool_search_tool_search_result"



[](#tool_search_tool_search_result_block.type)

[](#tool_search_tool_search_result_block)

[](#tool_search_tool_result_block.content)

tool_use_id: string



[](#tool_search_tool_result_block.tool_use_id)

type: "tool_search_tool_result"



[](#tool_search_tool_result_block.type)

[](#tool_search_tool_result_block)



ContainerUploadBlock object { file_id, type }



Response model for a file uploaded to the container.

file_id: string



[](#container_upload_block.file_id)

type: "container_upload"



[](#container_upload_block.type)

[](#container_upload_block)

[](#message.content)



model: [Model](/docs/en/api/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 14 more



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#message.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#message.model%20%2B%20(resource)%20messages%5B1%5D)

[](#message.model)



role: "assistant"



Conversational role of the generated message.

This will always be `"assistant"`.

[](#message.role)



stop_details: [RefusalStopDetails](/docs/en/api/messages#refusal_stop_details) { category, explanation, type }



Structured information about a refusal.



category: "cyber" or "bio" or "frontier_llm" or 2 more



The policy category that triggered a refusal.

One of the following:

"cyber"



The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B0%5D)

"bio"



The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B1%5D)

"frontier_llm"



The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B2%5D)

"reasoning_extraction"



The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B3%5D)

"general_harms"



The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B4%5D)

[](#message.stop_details%20%2B%20(resource)%20messages.category)



explanation: string



Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

[](#message.stop_details%20%2B%20(resource)%20messages.explanation)

type: "refusal"



[](#message.stop_details%20%2B%20(resource)%20messages.type)

[](#message.stop_details)



stop_reason: [StopReason](/docs/en/api/messages#stop_reason)



The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations
- `"model_context_window_exceeded"`: we exceeded the model's context window

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end_turn"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B0%5D)

"max_tokens"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B1%5D)

"stop_sequence"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B2%5D)

"tool_use"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B3%5D)

"pause_turn"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B4%5D)

"refusal"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B5%5D)

"model_context_window_exceeded"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B6%5D)

[](#message.stop_reason)



stop_sequence: string



Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

[](#message.stop_sequence)



type: "message"



Object type.

For Messages, this is always `"message"`.

[](#message.type)



usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }



Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number



The number of input tokens used to create the 1 hour cache entry.

[](#usage.cache_creation%20%2B%20(resource)%20messages.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: number



The number of input tokens used to create the 5 minute cache entry.

[](#usage.cache_creation%20%2B%20(resource)%20messages.ephemeral_5m_input_tokens)

[](#message.usage%20%2B%20(resource)%20messages.cache_creation)

cache_creation_input_tokens: number



The number of input tokens used to create the cache entry.

[](#message.usage%20%2B%20(resource)%20messages.cache_creation_input_tokens)

cache_read_input_tokens: number



The number of input tokens read from the cache.

[](#message.usage%20%2B%20(resource)%20messages.cache_read_input_tokens)

inference_geo: string



The geographic region where inference was performed for this request.

[](#message.usage%20%2B%20(resource)%20messages.inference_geo)

input_tokens: number



The number of input tokens which were used.

[](#message.usage%20%2B%20(resource)%20messages.input_tokens)

output_tokens: number



The number of output tokens which were used.

[](#message.usage%20%2B%20(resource)%20messages.output_tokens)



output_tokens_details: [OutputTokensDetails](/docs/en/api/messages#output_tokens_details) { thinking_tokens }



Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.



thinking_tokens: number



Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0

[](#usage.output_tokens_details%20%2B%20(resource)%20messages.thinking_tokens)

[](#message.usage%20%2B%20(resource)%20messages.output_tokens_details)



server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests }



The number of server tool requests.

web_fetch_requests: number



The number of web fetch tool requests.

[](#usage.server_tool_use%20%2B%20(resource)%20messages.web_fetch_requests)

web_search_requests: number



The number of web search tool requests.

[](#usage.server_tool_use%20%2B%20(resource)%20messages.web_search_requests)

[](#message.usage%20%2B%20(resource)%20messages.server_tool_use)



service_tier: "standard" or "priority" or "batch"



If the request used the priority, standard, or batch tier.

One of the following:

"standard"



[](#message.usage%20%2B%20(resource)%20messages.service_tier%5B0%5D)

"priority"



[](#message.usage%20%2B%20(resource)%20messages.service_tier%5B1%5D)

"batch"



[](#message.usage%20%2B%20(resource)%20messages.service_tier%5B2%5D)

[](#message.usage%20%2B%20(resource)%20messages.service_tier)

[](#message.usage)

[](#message)



RawMessageStreamEvent = [RawMessageStartEvent](/docs/en/api/messages#raw_message_start_event) { message, type } or [RawMessageDeltaEvent](/docs/en/api/messages#raw_message_delta_event) { delta, type, usage } or [RawMessageStopEvent](/docs/en/api/messages#raw_message_stop_event) { type } or 3 more



One of the following:



RawMessageStartEvent object { message, type }





message: [Message](/docs/en/api/messages#message) { id, container, content, 7 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.id)



container: [Container](/docs/en/api/messages#container) { id, expires_at }



Information about the container used in the request (for the code execution tool)

id: string



Identifier for the container used in this request

[](#message.container%20%2B%20(resource)%20messages.id)

expires_at: string



The time at which the container will expire.

[](#message.container%20%2B%20(resource)%20messages.expires_at)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.container)



content: array of [ContentBlock](/docs/en/api/messages#content_block)



Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```python
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```python
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```python
[{"type": "text", "text": "B)"}]
```



One of the following:



TextBlock object { citations, text, type }





citations: array of [TextCitation](/docs/en/api/messages#text_citation)



Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.document_title)

end_char_index: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.end_char_index)

file_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_id)

start_char_index: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.start_char_index)

type: "char_location"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



CitationPageLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.document_title)

end_page_number: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.end_page_number)

file_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_id)

start_page_number: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.start_page_number)

type: "page_location"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.end_block_index)

file_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_id)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.start_block_index)

type: "content_block_location"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.cited_text)

encrypted_index: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.encrypted_index)

title: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.title)

type: "web_search_result_location"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

url: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.url)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.search_result_index)

source: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.start_block_index)

title: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.title)

type: "search_result_location"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.citations)

text: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.text)

type: "text"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ThinkingBlock object { signature, thinking, type }



signature: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.signature)

thinking: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.thinking)

type: "thinking"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



RedactedThinkingBlock object { data, type }



data: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.data)

type: "redacted_thinking"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ToolUseBlock object { id, caller, input, 2 more }



id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.id)



caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.caller)

input: map\[unknown\]



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.input)

name: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name)

type: "tool_use"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolUseBlock object { id, caller, input, 2 more }



id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.id)



caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.caller)

input: map\[unknown\]



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.input)



name: "web_search" or "web_fetch" or "code_execution" or 4 more



One of the following:

"web_search"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name%5B0%5D)

"web_fetch"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name%5B1%5D)

"code_execution"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name%5B2%5D)

"bash_code_execution"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name%5B3%5D)

"text_editor_code_execution"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name%5B4%5D)

"tool_search_tool_regex"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name%5B5%5D)

"tool_search_tool_bm25"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name%5B6%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.name)

type: "server_tool_use"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



WebSearchToolResultBlock object { caller, content, tool_use_id, type }





caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.caller)



content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)



One of the following:



WebSearchToolResultError object { error_code, type }





error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"max_uses_exceeded"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"too_many_requests"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"query_too_long"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

"request_too_large"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B5%5D)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.error_code)

type: "web_search_tool_result_error"



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages)



array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more }



encrypted_content: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.encrypted_content)

page_age: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.page_age)

title: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.title)

type: "web_search_result"



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.type)

url: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.url)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages%5B1%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_use_id)

type: "web_search_tool_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



WebFetchToolResultBlock object { caller, content, tool_use_id, type }





caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.caller)



content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } or [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }



One of the following:



WebFetchToolResultErrorBlock object { error_code, type }





error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B0%5D)

"url_too_long"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B1%5D)

"url_not_allowed"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B2%5D)

"url_not_in_prior_context"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B3%5D)

"url_not_accessible"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B4%5D)

"unsupported_content_type"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B5%5D)

"too_many_requests"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B6%5D)

"max_uses_exceeded"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B7%5D)

"unavailable"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B8%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.error_code)

type: "web_fetch_tool_result_error"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



WebFetchBlock object { content, retrieved_at, type, url }





content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }





citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled }



Citation configuration for the document

enabled: boolean



[](#document_block.citations%20%2B%20(resource)%20messages.enabled)

[](#web_fetch_block.content%20%2B%20(resource)%20messages.citations)



source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }



One of the following:



Base64PDFSource object { data, media_type, type }



data: string



[](#web_fetch_block.content%20%2B%20(resource)%20messages.data)

media_type: "application/pdf"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.media_type)

type: "base64"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block.content%20%2B%20(resource)%20messages)



PlainTextSource object { data, media_type, type }



data: string



[](#web_fetch_block.content%20%2B%20(resource)%20messages.data)

media_type: "text/plain"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.media_type)

type: "text"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block.content%20%2B%20(resource)%20messages)

[](#web_fetch_block.content%20%2B%20(resource)%20messages.source)

title: string



The title of the document

[](#web_fetch_block.content%20%2B%20(resource)%20messages.title)

type: "document"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)

retrieved_at: string



ISO 8601 timestamp when the content was retrieved

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.retrieved_at)

type: "web_fetch_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

url: string



Fetched content URL

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.url)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_use_id)

type: "web_fetch_tool_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



CodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)



Code execution result with encrypted stdout for PFC + web_search results.

One of the following:



CodeExecutionToolResultError object { error_code, type }





error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.error_code)

type: "code_execution_tool_result_error"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)



CodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type }



file_id: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.file_id)

type: "code_execution_output"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.content)

return_code: number



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stderr)

stdout: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stdout)

type: "code_execution_result"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)



EncryptedCodeExecutionResultBlock object { content, encrypted_stdout, return_code, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.



content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type }



file_id: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.file_id)

type: "code_execution_output"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.content)

encrypted_stdout: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.encrypted_stdout)

return_code: number



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stderr)

type: "encrypted_code_execution_result"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_use_id)

type: "code_execution_tool_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



BashCodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } or [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }



One of the following:



BashCodeExecutionToolResultError object { error_code, type }





error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"output_file_too_large"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.error_code)

type: "bash_code_execution_tool_result_error"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type }



file_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_id)

type: "bash_code_execution_output"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)

return_code: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.stderr)

stdout: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.stdout)

type: "bash_code_execution_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_use_id)

type: "bash_code_execution_tool_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } or [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }



One of the following:



TextEditorCodeExecutionToolResultError object { error_code, error_message, type }





error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"file_not_found"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.error_code)

error_message: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.error_message)

type: "text_editor_code_execution_tool_result_error"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more }



content: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)



file_type: "text" or "image" or "pdf"



One of the following:

"text"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_type%5B0%5D)

"image"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_type%5B1%5D)

"pdf"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_type%5B2%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_type)

num_lines: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.num_lines)

start_line: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.start_line)

total_lines: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.total_lines)

type: "text_editor_code_execution_view_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionCreateResultBlock object { is_file_update, type }



is_file_update: boolean



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.is_file_update)

type: "text_editor_code_execution_create_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more }



lines: array of string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.lines)

new_lines: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.new_lines)

new_start: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.new_start)

old_lines: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.old_lines)

old_start: number



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.old_start)

type: "text_editor_code_execution_str_replace_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_use_id)

type: "text_editor_code_execution_tool_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ToolSearchToolResultBlock object { content, tool_use_id, type }





content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } or [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }



One of the following:



ToolSearchToolResultError object { error_code, error_message, type }





error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.error_code)

error_message: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.error_message)

type: "tool_search_tool_result_error"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ToolSearchToolSearchResultBlock object { tool_references, type }





tool_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type }



tool_name: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_name)

type: "tool_reference"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_references)

type: "tool_search_tool_search_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.tool_use_id)

type: "tool_search_tool_result"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)



ContainerUploadBlock object { file_id, type }



Response model for a file uploaded to the container.

file_id: string



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.file_id)

type: "container_upload"



[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.content)



model: [Model](/docs/en/api/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 14 more



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#message.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#message.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#message.model%20%2B%20(resource)%20messages%5B1%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.model)



role: "assistant"



Conversational role of the generated message.

This will always be `"assistant"`.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.role)



stop_details: [RefusalStopDetails](/docs/en/api/messages#refusal_stop_details) { category, explanation, type }



Structured information about a refusal.



category: "cyber" or "bio" or "frontier_llm" or 2 more



The policy category that triggered a refusal.

One of the following:

"cyber"



The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B0%5D)

"bio"



The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B1%5D)

"frontier_llm"



The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B2%5D)

"reasoning_extraction"



The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B3%5D)

"general_harms"



The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

[](#message.stop_details%20%2B%20(resource)%20messages.category%5B4%5D)

[](#message.stop_details%20%2B%20(resource)%20messages.category)



explanation: string



Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

[](#message.stop_details%20%2B%20(resource)%20messages.explanation)

type: "refusal"



[](#message.stop_details%20%2B%20(resource)%20messages.type)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.stop_details)



stop_reason: [StopReason](/docs/en/api/messages#stop_reason)



The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations
- `"model_context_window_exceeded"`: we exceeded the model's context window

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

"end_turn"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B0%5D)

"max_tokens"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B1%5D)

"stop_sequence"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B2%5D)

"tool_use"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B3%5D)

"pause_turn"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B4%5D)

"refusal"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B5%5D)

"model_context_window_exceeded"



[](#message.stop_reason%20%2B%20(resource)%20messages%5B6%5D)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.stop_reason)



stop_sequence: string



Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.stop_sequence)



type: "message"



Object type.

For Messages, this is always `"message"`.

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.type)



usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }



Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: number



The number of input tokens used to create the 1 hour cache entry.

[](#usage.cache_creation%20%2B%20(resource)%20messages.ephemeral_1h_input_tokens)

ephemeral_5m_input_tokens: number



The number of input tokens used to create the 5 minute cache entry.

[](#usage.cache_creation%20%2B%20(resource)%20messages.ephemeral_5m_input_tokens)

[](#message.usage%20%2B%20(resource)%20messages.cache_creation)

cache_creation_input_tokens: number



The number of input tokens used to create the cache entry.

[](#message.usage%20%2B%20(resource)%20messages.cache_creation_input_tokens)

cache_read_input_tokens: number



The number of input tokens read from the cache.

[](#message.usage%20%2B%20(resource)%20messages.cache_read_input_tokens)

inference_geo: string



The geographic region where inference was performed for this request.

[](#message.usage%20%2B%20(resource)%20messages.inference_geo)

input_tokens: number



The number of input tokens which were used.

[](#message.usage%20%2B%20(resource)%20messages.input_tokens)

output_tokens: number



The number of output tokens which were used.

[](#message.usage%20%2B%20(resource)%20messages.output_tokens)



output_tokens_details: [OutputTokensDetails](/docs/en/api/messages#output_tokens_details) { thinking_tokens }



Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.



thinking_tokens: number



Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0

[](#usage.output_tokens_details%20%2B%20(resource)%20messages.thinking_tokens)

[](#message.usage%20%2B%20(resource)%20messages.output_tokens_details)



server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests }



The number of server tool requests.

web_fetch_requests: number



The number of web fetch tool requests.

[](#usage.server_tool_use%20%2B%20(resource)%20messages.web_fetch_requests)

web_search_requests: number



The number of web search tool requests.

[](#usage.server_tool_use%20%2B%20(resource)%20messages.web_search_requests)

[](#message.usage%20%2B%20(resource)%20messages.server_tool_use)



service_tier: "standard" or "priority" or "batch"



If the request used the priority, standard, or batch tier.

One of the following:

"standard"



[](#message.usage%20%2B%20(resource)%20messages.service_tier%5B0%5D)

"priority"



[](#message.usage%20%2B%20(resource)%20messages.service_tier%5B1%5D)

"batch"



[](#message.usage%20%2B%20(resource)%20messages.service_tier%5B2%5D)

[](#message.usage%20%2B%20(resource)%20messages.service_tier)

[](#raw_message_start_event.message%20%2B%20(resource)%20messages.usage)

[](#raw_message_start_event.message)

type: "message_start"



[](#raw_message_start_event.type)

[](#raw_message_start_event)



RawMessageDeltaEvent object { delta, type, usage }





delta: object { container, stop_details, stop_reason, stop_sequence }





container: [Container](/docs/en/api/messages#container) { id, expires_at }



Information about the container used in the request (for the code execution tool)

id: string



Identifier for the container used in this request

[](#raw_message_delta_event.delta.container%20%2B%20(resource)%20messages.id)

expires_at: string



The time at which the container will expire.

[](#raw_message_delta_event.delta.container%20%2B%20(resource)%20messages.expires_at)

[](#raw_message_delta_event.delta.container)



stop_details: [RefusalStopDetails](/docs/en/api/messages#refusal_stop_details) { category, explanation, type }



Structured information about a refusal.



category: "cyber" or "bio" or "frontier_llm" or 2 more



The policy category that triggered a refusal.

One of the following:

"cyber"



The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

[](#raw_message_delta_event.delta.stop_details%20%2B%20(resource)%20messages.category%5B0%5D)

"bio"



The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

[](#raw_message_delta_event.delta.stop_details%20%2B%20(resource)%20messages.category%5B1%5D)

"frontier_llm"



The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

[](#raw_message_delta_event.delta.stop_details%20%2B%20(resource)%20messages.category%5B2%5D)

"reasoning_extraction"



The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

[](#raw_message_delta_event.delta.stop_details%20%2B%20(resource)%20messages.category%5B3%5D)

"general_harms"



The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

[](#raw_message_delta_event.delta.stop_details%20%2B%20(resource)%20messages.category%5B4%5D)

[](#raw_message_delta_event.delta.stop_details%20%2B%20(resource)%20messages.category)



explanation: string



Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

[](#raw_message_delta_event.delta.stop_details%20%2B%20(resource)%20messages.explanation)

type: "refusal"



[](#raw_message_delta_event.delta.stop_details%20%2B%20(resource)%20messages.type)

[](#raw_message_delta_event.delta.stop_details)



stop_reason: [StopReason](/docs/en/api/messages#stop_reason)



One of the following:

"end_turn"



[](#raw_message_delta_event.delta.stop_reason%20%2B%20(resource)%20messages%5B0%5D)

"max_tokens"



[](#raw_message_delta_event.delta.stop_reason%20%2B%20(resource)%20messages%5B1%5D)

"stop_sequence"



[](#raw_message_delta_event.delta.stop_reason%20%2B%20(resource)%20messages%5B2%5D)

"tool_use"



[](#raw_message_delta_event.delta.stop_reason%20%2B%20(resource)%20messages%5B3%5D)

"pause_turn"



[](#raw_message_delta_event.delta.stop_reason%20%2B%20(resource)%20messages%5B4%5D)

"refusal"



[](#raw_message_delta_event.delta.stop_reason%20%2B%20(resource)%20messages%5B5%5D)

"model_context_window_exceeded"



[](#raw_message_delta_event.delta.stop_reason%20%2B%20(resource)%20messages%5B6%5D)

[](#raw_message_delta_event.delta.stop_reason)

stop_sequence: string



[](#raw_message_delta_event.delta.stop_sequence)

[](#raw_message_delta_event.delta)

type: "message_delta"



[](#raw_message_delta_event.type)



usage: [MessageDeltaUsage](/docs/en/api/messages#message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }



Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: number



The cumulative number of input tokens used to create the cache entry.

[](#raw_message_delta_event.usage%20%2B%20(resource)%20messages.cache_creation_input_tokens)

cache_read_input_tokens: number



The cumulative number of input tokens read from the cache.

[](#raw_message_delta_event.usage%20%2B%20(resource)%20messages.cache_read_input_tokens)

input_tokens: number



The cumulative number of input tokens which were used.

[](#raw_message_delta_event.usage%20%2B%20(resource)%20messages.input_tokens)

output_tokens: number



The cumulative number of output tokens which were used.

[](#raw_message_delta_event.usage%20%2B%20(resource)%20messages.output_tokens)



output_tokens_details: [OutputTokensDetails](/docs/en/api/messages#output_tokens_details) { thinking_tokens }



Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.



thinking_tokens: number



Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0

[](#message_delta_usage.output_tokens_details%20%2B%20(resource)%20messages.thinking_tokens)

[](#raw_message_delta_event.usage%20%2B%20(resource)%20messages.output_tokens_details)



server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests }



The number of server tool requests.

web_fetch_requests: number



The number of web fetch tool requests.

[](#message_delta_usage.server_tool_use%20%2B%20(resource)%20messages.web_fetch_requests)

web_search_requests: number



The number of web search tool requests.

[](#message_delta_usage.server_tool_use%20%2B%20(resource)%20messages.web_search_requests)

[](#raw_message_delta_event.usage%20%2B%20(resource)%20messages.server_tool_use)

[](#raw_message_delta_event.usage)

[](#raw_message_delta_event)



RawMessageStopEvent object { type }



type: "message_stop"



[](#raw_message_stop_event.type)

[](#raw_message_stop_event)



RawContentBlockStartEvent object { content_block, index, type }





content_block: [TextBlock](/docs/en/api/messages#text_block) { citations, text, type } or [ThinkingBlock](/docs/en/api/messages#thinking_block) { signature, thinking, type } or [RedactedThinkingBlock](/docs/en/api/messages#redacted_thinking_block) { data, type } or 9 more



Response model for a file uploaded to the container.

One of the following:



TextBlock object { citations, text, type }





citations: array of [TextCitation](/docs/en/api/messages#text_citation)



Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#citation_char_location.cited_text)

document_index: number



[](#citation_char_location.document_index)

document_title: string



[](#citation_char_location.document_title)

end_char_index: number



[](#citation_char_location.end_char_index)

file_id: string



[](#citation_char_location.file_id)

start_char_index: number



[](#citation_char_location.start_char_index)

type: "char_location"



[](#citation_char_location.type)

[](#citation_char_location)



CitationPageLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#citation_page_location.cited_text)

document_index: number



[](#citation_page_location.document_index)

document_title: string



[](#citation_page_location.document_title)

end_page_number: number



[](#citation_page_location.end_page_number)

file_id: string



[](#citation_page_location.file_id)

start_page_number: number



[](#citation_page_location.start_page_number)

type: "page_location"



[](#citation_page_location.type)

[](#citation_page_location)



CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citation_content_block_location.cited_text)

document_index: number



[](#citation_content_block_location.document_index)

document_title: string



[](#citation_content_block_location.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citation_content_block_location.end_block_index)

file_id: string



[](#citation_content_block_location.file_id)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citation_content_block_location.start_block_index)

type: "content_block_location"



[](#citation_content_block_location.type)

[](#citation_content_block_location)



CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#citations_web_search_result_location.cited_text)

encrypted_index: string



[](#citations_web_search_result_location.encrypted_index)

title: string



[](#citations_web_search_result_location.title)

type: "web_search_result_location"



[](#citations_web_search_result_location.type)

url: string



[](#citations_web_search_result_location.url)

[](#citations_web_search_result_location)



CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#citations_search_result_location.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#citations_search_result_location.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#citations_search_result_location.search_result_index)

source: string



[](#citations_search_result_location.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#citations_search_result_location.start_block_index)

title: string



[](#citations_search_result_location.title)

type: "search_result_location"



[](#citations_search_result_location.type)

[](#citations_search_result_location)

[](#text_block.citations)

text: string



[](#text_block.text)

type: "text"



[](#text_block.type)

[](#text_block)



ThinkingBlock object { signature, thinking, type }



signature: string



[](#thinking_block.signature)

thinking: string



[](#thinking_block.thinking)

type: "thinking"



[](#thinking_block.type)

[](#thinking_block)



RedactedThinkingBlock object { data, type }



data: string



[](#redacted_thinking_block.data)

type: "redacted_thinking"



[](#redacted_thinking_block.type)

[](#redacted_thinking_block)



ToolUseBlock object { id, caller, input, 2 more }



id: string



[](#tool_use_block.id)



caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#tool_use_block.caller)

input: map\[unknown\]



[](#tool_use_block.input)

name: string



[](#tool_use_block.name)

type: "tool_use"



[](#tool_use_block.type)

[](#tool_use_block)



ServerToolUseBlock object { id, caller, input, 2 more }



id: string



[](#server_tool_use_block.id)



caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#server_tool_use_block.caller)

input: map\[unknown\]



[](#server_tool_use_block.input)



name: "web_search" or "web_fetch" or "code_execution" or 4 more



One of the following:

"web_search"



[](#server_tool_use_block.name%5B0%5D)

"web_fetch"



[](#server_tool_use_block.name%5B1%5D)

"code_execution"



[](#server_tool_use_block.name%5B2%5D)

"bash_code_execution"



[](#server_tool_use_block.name%5B3%5D)

"text_editor_code_execution"



[](#server_tool_use_block.name%5B4%5D)

"tool_search_tool_regex"



[](#server_tool_use_block.name%5B5%5D)

"tool_search_tool_bm25"



[](#server_tool_use_block.name%5B6%5D)

[](#server_tool_use_block.name)

type: "server_tool_use"



[](#server_tool_use_block.type)

[](#server_tool_use_block)



WebSearchToolResultBlock object { caller, content, tool_use_id, type }





caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#web_search_tool_result_block.caller)



content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)



One of the following:



WebSearchToolResultError object { error_code, type }





error_code: [WebSearchToolResultErrorCode](/docs/en/api/messages#web_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"max_uses_exceeded"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"too_many_requests"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"query_too_long"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

"request_too_large"



[](#web_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B5%5D)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.error_code)

type: "web_search_tool_result_error"



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages)



array of [WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more }



encrypted_content: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.encrypted_content)

page_age: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.page_age)

title: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.title)

type: "web_search_result"



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.type)

url: string



[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages.url)

[](#web_search_tool_result_block.content%20%2B%20(resource)%20messages%5B1%5D)

[](#web_search_tool_result_block.content)

tool_use_id: string



[](#web_search_tool_result_block.tool_use_id)

type: "web_search_tool_result"



[](#web_search_tool_result_block.type)

[](#web_search_tool_result_block)



WebFetchToolResultBlock object { caller, content, tool_use_id, type }





caller: [DirectCaller](/docs/en/api/messages#direct_caller) { type } or [ServerToolCaller](/docs/en/api/messages#server_tool_caller) { tool_id, type } or [ServerToolCaller20260120](/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



DirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#direct_caller.type)

[](#direct_caller)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#server_tool_caller.type)

[](#server_tool_caller)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#server_tool_caller_20260120.type)

[](#server_tool_caller_20260120)

[](#web_fetch_tool_result_block.caller)



content: [WebFetchToolResultErrorBlock](/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type } or [WebFetchBlock](/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url }



One of the following:



WebFetchToolResultErrorBlock object { error_code, type }





error_code: [WebFetchToolResultErrorCode](/docs/en/api/messages#web_fetch_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B0%5D)

"url_too_long"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B1%5D)

"url_not_allowed"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B2%5D)

"url_not_in_prior_context"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B3%5D)

"url_not_accessible"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B4%5D)

"unsupported_content_type"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B5%5D)

"too_many_requests"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B6%5D)

"max_uses_exceeded"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B7%5D)

"unavailable"



[](#web_fetch_tool_result_error_block.error_code%20%2B%20(resource)%20messages%5B8%5D)

[](#web_fetch_tool_result_error_block.error_code)

type: "web_fetch_tool_result_error"



[](#web_fetch_tool_result_error_block.type)

[](#web_fetch_tool_result_error_block)



WebFetchBlock object { content, retrieved_at, type, url }





content: [DocumentBlock](/docs/en/api/messages#document_block) { citations, source, title, type }





citations: [CitationsConfig](/docs/en/api/messages#citations_config) { enabled }



Citation configuration for the document

enabled: boolean



[](#document_block.citations%20%2B%20(resource)%20messages.enabled)

[](#web_fetch_block.content%20%2B%20(resource)%20messages.citations)



source: [Base64PDFSource](/docs/en/api/messages#base64_pdf_source) { data, media_type, type } or [PlainTextSource](/docs/en/api/messages#plain_text_source) { data, media_type, type }



One of the following:



Base64PDFSource object { data, media_type, type }



data: string



[](#web_fetch_block.content%20%2B%20(resource)%20messages.data)

media_type: "application/pdf"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.media_type)

type: "base64"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block.content%20%2B%20(resource)%20messages)



PlainTextSource object { data, media_type, type }



data: string



[](#web_fetch_block.content%20%2B%20(resource)%20messages.data)

media_type: "text/plain"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.media_type)

type: "text"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block.content%20%2B%20(resource)%20messages)

[](#web_fetch_block.content%20%2B%20(resource)%20messages.source)

title: string



The title of the document

[](#web_fetch_block.content%20%2B%20(resource)%20messages.title)

type: "document"



[](#web_fetch_block.content%20%2B%20(resource)%20messages.type)

[](#web_fetch_block.content)

retrieved_at: string



ISO 8601 timestamp when the content was retrieved

[](#web_fetch_block.retrieved_at)

type: "web_fetch_result"



[](#web_fetch_block.type)

url: string



Fetched content URL

[](#web_fetch_block.url)

[](#web_fetch_block)

[](#web_fetch_tool_result_block.content)

tool_use_id: string



[](#web_fetch_tool_result_block.tool_use_id)

type: "web_fetch_tool_result"



[](#web_fetch_tool_result_block.type)

[](#web_fetch_tool_result_block)



CodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [CodeExecutionToolResultBlockContent](/docs/en/api/messages#code_execution_tool_result_block_content)



Code execution result with encrypted stdout for PFC + web_search results.

One of the following:



CodeExecutionToolResultError object { error_code, type }





error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/messages#code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.error_code)

type: "code_execution_tool_result_error"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)



CodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type }



file_id: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.file_id)

type: "code_execution_output"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.content)

return_code: number



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stderr)

stdout: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stdout)

type: "code_execution_result"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)



EncryptedCodeExecutionResultBlock object { content, encrypted_stdout, return_code, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.



content: array of [CodeExecutionOutputBlock](/docs/en/api/messages#code_execution_output_block) { file_id, type }



file_id: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.file_id)

type: "code_execution_output"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.content)

encrypted_stdout: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.encrypted_stdout)

return_code: number



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.stderr)

type: "encrypted_code_execution_result"



[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages.type)

[](#code_execution_tool_result_block.content%20%2B%20(resource)%20messages)

[](#code_execution_tool_result_block.content)

tool_use_id: string



[](#code_execution_tool_result_block.tool_use_id)

type: "code_execution_tool_result"



[](#code_execution_tool_result_block.type)

[](#code_execution_tool_result_block)



BashCodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [BashCodeExecutionToolResultError](/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type } or [BashCodeExecutionResultBlock](/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more }



One of the following:



BashCodeExecutionToolResultError object { error_code, type }





error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/messages#bash_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"output_file_too_large"



[](#bash_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

[](#bash_code_execution_tool_result_error.error_code)

type: "bash_code_execution_tool_result_error"



[](#bash_code_execution_tool_result_error.type)

[](#bash_code_execution_tool_result_error)



BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type }



file_id: string



[](#bash_code_execution_output_block.file_id)

type: "bash_code_execution_output"



[](#bash_code_execution_output_block.type)

[](#bash_code_execution_result_block.content)

return_code: number



[](#bash_code_execution_result_block.return_code)

stderr: string



[](#bash_code_execution_result_block.stderr)

stdout: string



[](#bash_code_execution_result_block.stdout)

type: "bash_code_execution_result"



[](#bash_code_execution_result_block.type)

[](#bash_code_execution_result_block)

[](#bash_code_execution_tool_result_block.content)

tool_use_id: string



[](#bash_code_execution_tool_result_block.tool_use_id)

type: "bash_code_execution_tool_result"



[](#bash_code_execution_tool_result_block.type)

[](#bash_code_execution_tool_result_block)



TextEditorCodeExecutionToolResultBlock object { content, tool_use_id, type }





content: [TextEditorCodeExecutionToolResultError](/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type } or [TextEditorCodeExecutionViewResultBlock](/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more } or [TextEditorCodeExecutionCreateResultBlock](/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type } or [TextEditorCodeExecutionStrReplaceResultBlock](/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more }



One of the following:



TextEditorCodeExecutionToolResultError object { error_code, error_message, type }





error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

"file_not_found"



[](#text_editor_code_execution_tool_result_error.error_code%20%2B%20(resource)%20messages%5B4%5D)

[](#text_editor_code_execution_tool_result_error.error_code)

error_message: string



[](#text_editor_code_execution_tool_result_error.error_message)

type: "text_editor_code_execution_tool_result_error"



[](#text_editor_code_execution_tool_result_error.type)

[](#text_editor_code_execution_tool_result_error)



TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more }



content: string



[](#text_editor_code_execution_view_result_block.content)



file_type: "text" or "image" or "pdf"



One of the following:

"text"



[](#text_editor_code_execution_view_result_block.file_type%5B0%5D)

"image"



[](#text_editor_code_execution_view_result_block.file_type%5B1%5D)

"pdf"



[](#text_editor_code_execution_view_result_block.file_type%5B2%5D)

[](#text_editor_code_execution_view_result_block.file_type)

num_lines: number



[](#text_editor_code_execution_view_result_block.num_lines)

start_line: number



[](#text_editor_code_execution_view_result_block.start_line)

total_lines: number



[](#text_editor_code_execution_view_result_block.total_lines)

type: "text_editor_code_execution_view_result"



[](#text_editor_code_execution_view_result_block.type)

[](#text_editor_code_execution_view_result_block)



TextEditorCodeExecutionCreateResultBlock object { is_file_update, type }



is_file_update: boolean



[](#text_editor_code_execution_create_result_block.is_file_update)

type: "text_editor_code_execution_create_result"



[](#text_editor_code_execution_create_result_block.type)

[](#text_editor_code_execution_create_result_block)



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more }



lines: array of string



[](#text_editor_code_execution_str_replace_result_block.lines)

new_lines: number



[](#text_editor_code_execution_str_replace_result_block.new_lines)

new_start: number



[](#text_editor_code_execution_str_replace_result_block.new_start)

old_lines: number



[](#text_editor_code_execution_str_replace_result_block.old_lines)

old_start: number



[](#text_editor_code_execution_str_replace_result_block.old_start)

type: "text_editor_code_execution_str_replace_result"



[](#text_editor_code_execution_str_replace_result_block.type)

[](#text_editor_code_execution_str_replace_result_block)

[](#text_editor_code_execution_tool_result_block.content)

tool_use_id: string



[](#text_editor_code_execution_tool_result_block.tool_use_id)

type: "text_editor_code_execution_tool_result"



[](#text_editor_code_execution_tool_result_block.type)

[](#text_editor_code_execution_tool_result_block)



ToolSearchToolResultBlock object { content, tool_use_id, type }





content: [ToolSearchToolResultError](/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type } or [ToolSearchToolSearchResultBlock](/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type }



One of the following:



ToolSearchToolResultError object { error_code, error_message, type }





error_code: [ToolSearchToolResultErrorCode](/docs/en/api/messages#tool_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B0%5D)

"unavailable"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B1%5D)

"too_many_requests"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B2%5D)

"execution_time_exceeded"



[](#tool_search_tool_result_error.error_code%20%2B%20(resource)%20messages%5B3%5D)

[](#tool_search_tool_result_error.error_code)

error_message: string



[](#tool_search_tool_result_error.error_message)

type: "tool_search_tool_result_error"



[](#tool_search_tool_result_error.type)

[](#tool_search_tool_result_error)



ToolSearchToolSearchResultBlock object { tool_references, type }





tool_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type }



tool_name: string



[](#tool_reference_block.tool_name)

type: "tool_reference"



[](#tool_reference_block.type)

[](#tool_search_tool_search_result_block.tool_references)

type: "tool_search_tool_search_result"



[](#tool_search_tool_search_result_block.type)

[](#tool_search_tool_search_result_block)

[](#tool_search_tool_result_block.content)

tool_use_id: string



[](#tool_search_tool_result_block.tool_use_id)

type: "tool_search_tool_result"



[](#tool_search_tool_result_block.type)

[](#tool_search_tool_result_block)



ContainerUploadBlock object { file_id, type }



Response model for a file uploaded to the container.

file_id: string



[](#container_upload_block.file_id)

type: "container_upload"



[](#container_upload_block.type)

[](#container_upload_block)

[](#raw_content_block_start_event.content_block)

index: number



[](#raw_content_block_start_event.index)

type: "content_block_start"



[](#raw_content_block_start_event.type)

[](#raw_content_block_start_event)



RawContentBlockDeltaEvent object { delta, index, type }





delta: [RawContentBlockDelta](/docs/en/api/messages#raw_content_block_delta)



One of the following:



TextDelta object { text, type }



text: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.text)

type: "text_delta"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)



InputJSONDelta object { partial_json, type }



partial_json: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.partial_json)

type: "input_json_delta"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)



CitationsDelta object { citation, type }





citation: [CitationCharLocation](/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more } or [CitationPageLocation](/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more } or [CitationContentBlockLocation](/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more } or 2 more



One of the following:



CitationCharLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.document_title)

end_char_index: number



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.end_char_index)

file_id: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.file_id)

start_char_index: number



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.start_char_index)

type: "char_location"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)



CitationPageLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.document_title)

end_page_number: number



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.end_page_number)

file_id: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.file_id)

start_page_number: number



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.start_page_number)

type: "page_location"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)



CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.end_block_index)

file_id: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.file_id)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.start_block_index)

type: "content_block_location"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)



CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.cited_text)

encrypted_index: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.encrypted_index)

title: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.title)

type: "web_search_result_location"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

url: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.url)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)



CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.search_result_index)

source: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.start_block_index)

title: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.title)

type: "search_result_location"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.citation)

type: "citations_delta"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)



ThinkingDelta object { thinking, type }



thinking: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.thinking)

type: "thinking_delta"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)



SignatureDelta object { signature, type }



signature: string



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.signature)

type: "signature_delta"



[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages.type)

[](#raw_content_block_delta_event.delta%20%2B%20(resource)%20messages)

[](#raw_content_block_delta_event.delta)

index: number



[](#raw_content_block_delta_event.index)

type: "content_block_delta"



[](#raw_content_block_delta_event.type)

[](#raw_content_block_delta_event)



RawContentBlockStopEvent object { index, type }



index: number



[](#raw_content_block_stop_event.index)

type: "content_block_stop"



[](#raw_content_block_stop_event.type)

[](#raw_content_block_stop_event)

[](#raw_message_stream_event)

Create a Message

cURL



```python
curl https://api.anthropic.com/v1/messages \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    --max-time 600 \
    -d "{
          \"max_tokens\": 1024,
          \"messages\": [
            {
              \"content\": \"Hello, world\",
              \"role\": \"user\"
            }
          ],
          \"model\": \"claude-opus-4-6\",
          \"stream\": false,
          \"system\": [
            {
              \"text\": \"Today's date is 2024-06-01.\",
              \"type\": \"text\"
            }
          ],
          \"temperature\": 1,
          \"thinking\": {
            \"type\": \"adaptive\"
          },
          \"tools\": [
            {
              \"input_schema\": {
                \"type\": \"object\",
                \"properties\": {
                  \"location\": \"bar\",
                  \"unit\": \"bar\"
                },
                \"required\": [
                  \"location\"
                ]
              },
              \"name\": \"name\"
            }
          ],
          \"top_k\": 5,
          \"top_p\": 0.7
        }"
```

Response 200



```python
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "container_011CpZohnwH4vuy7gazohgSP",
    "expires_at": "2019-12-27T18:11:19.117Z"
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "The grass is green. The sky is blue.",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 0,
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
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
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
    "type": "refusal"
  },
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
    "inference_geo": "global",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
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



```python
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "container_011CpZohnwH4vuy7gazohgSP",
    "expires_at": "2019-12-27T18:11:19.117Z"
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "The grass is green. The sky is blue.",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 0,
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
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
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
    "type": "refusal"
  },
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
