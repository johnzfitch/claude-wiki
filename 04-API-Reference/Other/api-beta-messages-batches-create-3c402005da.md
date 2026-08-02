---
title: "Create a Message Batch - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/messages/batches/create"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:44Z"
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


Create a Message Batch


Retrieve a Message Batch


List Message Batches


Cancel a Message Batch


Delete a Message Batch


Retrieve Message Batch results

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

# Create a Message Batch

POST/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string



[](#anthropic_beta%5B0%5D)



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more



One of the following:

"message-batches-2024-09-24"



[](#anthropic_beta%5B1%5D%5B0%5D)

"prompt-caching-2024-07-31"



[](#anthropic_beta%5B1%5D%5B1%5D)

"computer-use-2024-10-22"



[](#anthropic_beta%5B1%5D%5B2%5D)

"computer-use-2025-01-24"



[](#anthropic_beta%5B1%5D%5B3%5D)

"pdfs-2024-09-25"



[](#anthropic_beta%5B1%5D%5B4%5D)

"token-counting-2024-11-01"



[](#anthropic_beta%5B1%5D%5B5%5D)

"token-efficient-tools-2025-02-19"



[](#anthropic_beta%5B1%5D%5B6%5D)

"output-128k-2025-02-19"



[](#anthropic_beta%5B1%5D%5B7%5D)

"files-api-2025-04-14"



[](#anthropic_beta%5B1%5D%5B8%5D)

"mcp-client-2025-04-04"



[](#anthropic_beta%5B1%5D%5B9%5D)

"mcp-client-2025-11-20"



[](#anthropic_beta%5B1%5D%5B10%5D)

"dev-full-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B11%5D)

"interleaved-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B12%5D)

"code-execution-2025-05-22"



[](#anthropic_beta%5B1%5D%5B13%5D)

"extended-cache-ttl-2025-04-11"



[](#anthropic_beta%5B1%5D%5B14%5D)

"context-1m-2025-08-07"



[](#anthropic_beta%5B1%5D%5B15%5D)

"context-management-2025-06-27"



[](#anthropic_beta%5B1%5D%5B16%5D)

"model-context-window-exceeded-2025-08-26"



[](#anthropic_beta%5B1%5D%5B17%5D)

"skills-2025-10-02"



[](#anthropic_beta%5B1%5D%5B18%5D)

"fast-mode-2026-02-01"



[](#anthropic_beta%5B1%5D%5B19%5D)

"output-300k-2026-03-24"



[](#anthropic_beta%5B1%5D%5B20%5D)

"user-profiles-2026-03-24"



[](#anthropic_beta%5B1%5D%5B21%5D)

"advisor-tool-2026-03-01"



[](#anthropic_beta%5B1%5D%5B22%5D)

"managed-agents-2026-04-01"



[](#anthropic_beta%5B1%5D%5B23%5D)

"cache-diagnosis-2026-04-07"



[](#anthropic_beta%5B1%5D%5B24%5D)

"dreaming-2026-04-21"



[](#anthropic_beta%5B1%5D%5B25%5D)

"thinking-token-count-2026-05-13"



[](#anthropic_beta%5B1%5D%5B26%5D)

"server-side-fallback-2026-06-01"



[](#anthropic_beta%5B1%5D%5B27%5D)

"server-side-fallback-2026-07-01"



[](#anthropic_beta%5B1%5D%5B28%5D)

"fallback-credit-2026-06-01"



[](#anthropic_beta%5B1%5D%5B29%5D)

"fallback-credit-2026-07-01"



[](#anthropic_beta%5B1%5D%5B30%5D)

"agent-memory-2026-07-22"



[](#anthropic_beta%5B1%5D%5B31%5D)

[](#anthropic_beta%5B1%5D)

[](#create.betas)

"anthropic-user-profile-id": optional string



The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

[](#create.user_profile_id)

##### Body ParametersJSONExpand Collapse 



requests: array of object { custom_id, params }



List of requests for prompt completion. Each is an individual request to create a Message.



custom_id: string



Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1

[](#create.requests.items.custom_id)



params: object { max_tokens, messages, model, 22 more }



Messages API creation parameters for the individual request.

See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.



max_tokens: number



The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

minimum0

[](#create.requests.items.params.max_tokens)



messages: array of [BetaMessageParam](/docs/en/api/beta/messages#beta_message_param) { content, role }

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

content: string or array of [BetaContentBlockParam](/docs/en/api/beta/messages#beta_content_block_param)



One of the following:

string



[](#beta_message_param.content%5B0%5D)



array of [BetaContentBlockParam](/docs/en/api/beta/messages#beta_content_block_param)



One of the following:



BetaTextBlockParam object { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#beta_text_block_param)



BetaImageBlockParam object { source, type, cache_control }





source: [BetaBase64ImageSource](/docs/en/api/beta/messages#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta/messages#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta/messages#beta_file_image_source) { file_id, type }



One of the following:



BetaBase64ImageSource object { data, media_type, type }



data: string



[](#beta_base64_image_source.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#beta_base64_image_source.media_type%5B0%5D)

"image/png"



[](#beta_base64_image_source.media_type%5B1%5D)

"image/gif"



[](#beta_base64_image_source.media_type%5B2%5D)

"image/webp"



[](#beta_base64_image_source.media_type%5B3%5D)

[](#beta_base64_image_source.media_type)

type: "base64"



[](#beta_base64_image_source.type)

[](#beta_base64_image_source)



BetaURLImageSource object { type, url }



type: "url"



[](#beta_url_image_source.type)

url: string



[](#beta_url_image_source.url)

[](#beta_url_image_source)



BetaFileImageSource object { file_id, type }



file_id: string



[](#beta_file_image_source.file_id)

type: "file"



[](#beta_file_image_source.type)

[](#beta_file_image_source)

[](#beta_image_block_param.source)

type: "image"



[](#beta_image_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_image_block_param.cache_control)

[](#beta_image_block_param)



BetaRequestDocumentBlock object { source, type, cache_control, 3 more }





source: [BetaBase64PDFSource](/docs/en/api/beta/messages#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta/messages#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta/messages#beta_content_block_source) { content, type } or 2 more



One of the following:



BetaBase64PDFSource object { data, media_type, type }



data: string



[](#beta_base64_pdf_source.data)

media_type: "application/pdf"



[](#beta_base64_pdf_source.media_type)

type: "base64"



[](#beta_base64_pdf_source.type)

[](#beta_base64_pdf_source)



BetaPlainTextSource object { data, media_type, type }



data: string



[](#beta_plain_text_source.data)

media_type: "text/plain"



[](#beta_plain_text_source.media_type)

type: "text"



[](#beta_plain_text_source.type)

[](#beta_plain_text_source)



BetaContentBlockSource object { content, type }





content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta/messages#beta_content_block_source_content)



One of the following:

string



[](#beta_content_block_source.content%5B0%5D)



BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta/messages#beta_content_block_source_content)



One of the following:



BetaTextBlockParam object { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#beta_text_block_param)



BetaImageBlockParam object { source, type, cache_control }





source: [BetaBase64ImageSource](/docs/en/api/beta/messages#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta/messages#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta/messages#beta_file_image_source) { file_id, type }



One of the following:



BetaBase64ImageSource object { data, media_type, type }



data: string



[](#beta_base64_image_source.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#beta_base64_image_source.media_type%5B0%5D)

"image/png"



[](#beta_base64_image_source.media_type%5B1%5D)

"image/gif"



[](#beta_base64_image_source.media_type%5B2%5D)

"image/webp"



[](#beta_base64_image_source.media_type%5B3%5D)

[](#beta_base64_image_source.media_type)

type: "base64"



[](#beta_base64_image_source.type)

[](#beta_base64_image_source)



BetaURLImageSource object { type, url }



type: "url"



[](#beta_url_image_source.type)

url: string



[](#beta_url_image_source.url)

[](#beta_url_image_source)



BetaFileImageSource object { file_id, type }



file_id: string



[](#beta_file_image_source.file_id)

type: "file"



[](#beta_file_image_source.type)

[](#beta_file_image_source)

[](#beta_image_block_param.source)

type: "image"



[](#beta_image_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_image_block_param.cache_control)

[](#beta_image_block_param)

[](#beta_content_block_source.content%5B1%5D)

[](#beta_content_block_source.content)

type: "content"



[](#beta_content_block_source.type)

[](#beta_content_block_source)



BetaURLPDFSource object { type, url }



type: "url"



[](#beta_url_pdf_source.type)

url: string



[](#beta_url_pdf_source.url)

[](#beta_url_pdf_source)



BetaFileDocumentSource object { file_id, type }



file_id: string



[](#beta_file_document_source.file_id)

type: "file"



[](#beta_file_document_source.type)

[](#beta_file_document_source)

[](#beta_request_document_block.source)

type: "document"



[](#beta_request_document_block.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_request_document_block.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



enabled: optional boolean



[](#beta_request_document_block.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_request_document_block.citations)

context: optional string



[](#beta_request_document_block.context)

title: optional string



[](#beta_request_document_block.title)

[](#beta_request_document_block)



BetaSearchResultBlockParam object { content, source, title, 3 more }





content: array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#beta_search_result_block_param.content)

source: string



[](#beta_search_result_block_param.source)

title: string



[](#beta_search_result_block_param.title)

type: "search_result"



[](#beta_search_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_search_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_search_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_search_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_search_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_search_result_block_param.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



enabled: optional boolean



[](#beta_search_result_block_param.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_search_result_block_param.citations)

[](#beta_search_result_block_param)



BetaThinkingBlockParam object { signature, thinking, type }



signature: string



[](#beta_thinking_block_param.signature)

thinking: string



[](#beta_thinking_block_param.thinking)

type: "thinking"



[](#beta_thinking_block_param.type)

[](#beta_thinking_block_param)



BetaRedactedThinkingBlockParam object { data, type }



data: string



[](#beta_redacted_thinking_block_param.data)

type: "redacted_thinking"



[](#beta_redacted_thinking_block_param.type)

[](#beta_redacted_thinking_block_param)



BetaToolUseBlockParam object { id, input, name, 3 more }



id: string



[](#beta_tool_use_block_param.id)

input: map\[unknown\]



[](#beta_tool_use_block_param.input)

name: string



[](#beta_tool_use_block_param.name)

type: "tool_use"



[](#beta_tool_use_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_use_block_param.cache_control)



caller: optional [BetaDirectCaller](/docs/en/api/beta/messages#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta/messages#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta/messages#beta_server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



BetaDirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#beta_direct_caller.type)

[](#beta_direct_caller)



BetaServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#beta_server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#beta_server_tool_caller.type)

[](#beta_server_tool_caller)



BetaServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#beta_server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#beta_server_tool_caller_20260120.type)

[](#beta_server_tool_caller_20260120)

[](#beta_tool_use_block_param.caller)

[](#beta_tool_use_block_param)



BetaToolResultBlockParam object { tool_use_id, type, cache_control, 2 more }



tool_use_id: string



[](#beta_tool_result_block_param.tool_use_id)

type: "tool_result"



[](#beta_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_result_block_param.cache_control)



content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta/messages#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta/messages#beta_search_result_block_param) { content, source, title, 3 more } or 2 more



One of the following:

string



[](#beta_tool_result_block_param.content%5B0%5D)



array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations } or [BetaImageBlockParam](/docs/en/api/beta/messages#beta_image_block_param) { source, type, cache_control } or [BetaSearchResultBlockParam](/docs/en/api/beta/messages#beta_search_result_block_param) { content, source, title, 3 more } or 2 more



One of the following:



BetaTextBlockParam object { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#beta_text_block_param)



BetaImageBlockParam object { source, type, cache_control }





source: [BetaBase64ImageSource](/docs/en/api/beta/messages#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta/messages#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta/messages#beta_file_image_source) { file_id, type }



One of the following:



BetaBase64ImageSource object { data, media_type, type }



data: string



[](#beta_base64_image_source.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#beta_base64_image_source.media_type%5B0%5D)

"image/png"



[](#beta_base64_image_source.media_type%5B1%5D)

"image/gif"



[](#beta_base64_image_source.media_type%5B2%5D)

"image/webp"



[](#beta_base64_image_source.media_type%5B3%5D)

[](#beta_base64_image_source.media_type)

type: "base64"



[](#beta_base64_image_source.type)

[](#beta_base64_image_source)



BetaURLImageSource object { type, url }



type: "url"



[](#beta_url_image_source.type)

url: string



[](#beta_url_image_source.url)

[](#beta_url_image_source)



BetaFileImageSource object { file_id, type }



file_id: string



[](#beta_file_image_source.file_id)

type: "file"



[](#beta_file_image_source.type)

[](#beta_file_image_source)

[](#beta_image_block_param.source)

type: "image"



[](#beta_image_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_image_block_param.cache_control)

[](#beta_image_block_param)



BetaSearchResultBlockParam object { content, source, title, 3 more }





content: array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#beta_search_result_block_param.content)

source: string



[](#beta_search_result_block_param.source)

title: string



[](#beta_search_result_block_param.title)

type: "search_result"



[](#beta_search_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_search_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_search_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_search_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_search_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_search_result_block_param.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



enabled: optional boolean



[](#beta_search_result_block_param.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_search_result_block_param.citations)

[](#beta_search_result_block_param)



BetaRequestDocumentBlock object { source, type, cache_control, 3 more }





source: [BetaBase64PDFSource](/docs/en/api/beta/messages#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta/messages#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta/messages#beta_content_block_source) { content, type } or 2 more



One of the following:



BetaBase64PDFSource object { data, media_type, type }



data: string



[](#beta_base64_pdf_source.data)

media_type: "application/pdf"



[](#beta_base64_pdf_source.media_type)

type: "base64"



[](#beta_base64_pdf_source.type)

[](#beta_base64_pdf_source)



BetaPlainTextSource object { data, media_type, type }



data: string



[](#beta_plain_text_source.data)

media_type: "text/plain"



[](#beta_plain_text_source.media_type)

type: "text"



[](#beta_plain_text_source.type)

[](#beta_plain_text_source)



BetaContentBlockSource object { content, type }





content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta/messages#beta_content_block_source_content)



One of the following:

string



[](#beta_content_block_source.content%5B0%5D)



BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta/messages#beta_content_block_source_content)



One of the following:



BetaTextBlockParam object { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#beta_text_block_param)



BetaImageBlockParam object { source, type, cache_control }





source: [BetaBase64ImageSource](/docs/en/api/beta/messages#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta/messages#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta/messages#beta_file_image_source) { file_id, type }



One of the following:



BetaBase64ImageSource object { data, media_type, type }



data: string



[](#beta_base64_image_source.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#beta_base64_image_source.media_type%5B0%5D)

"image/png"



[](#beta_base64_image_source.media_type%5B1%5D)

"image/gif"



[](#beta_base64_image_source.media_type%5B2%5D)

"image/webp"



[](#beta_base64_image_source.media_type%5B3%5D)

[](#beta_base64_image_source.media_type)

type: "base64"



[](#beta_base64_image_source.type)

[](#beta_base64_image_source)



BetaURLImageSource object { type, url }



type: "url"



[](#beta_url_image_source.type)

url: string



[](#beta_url_image_source.url)

[](#beta_url_image_source)



BetaFileImageSource object { file_id, type }



file_id: string



[](#beta_file_image_source.file_id)

type: "file"



[](#beta_file_image_source.type)

[](#beta_file_image_source)

[](#beta_image_block_param.source)

type: "image"



[](#beta_image_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_image_block_param.cache_control)

[](#beta_image_block_param)

[](#beta_content_block_source.content%5B1%5D)

[](#beta_content_block_source.content)

type: "content"



[](#beta_content_block_source.type)

[](#beta_content_block_source)



BetaURLPDFSource object { type, url }



type: "url"



[](#beta_url_pdf_source.type)

url: string



[](#beta_url_pdf_source.url)

[](#beta_url_pdf_source)



BetaFileDocumentSource object { file_id, type }



file_id: string



[](#beta_file_document_source.file_id)

type: "file"



[](#beta_file_document_source.type)

[](#beta_file_document_source)

[](#beta_request_document_block.source)

type: "document"



[](#beta_request_document_block.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_request_document_block.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



enabled: optional boolean



[](#beta_request_document_block.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_request_document_block.citations)

context: optional string



[](#beta_request_document_block.context)

title: optional string



[](#beta_request_document_block.title)

[](#beta_request_document_block)



BetaToolReferenceBlockParam object { tool_name, type, cache_control }



Tool reference block that can be included in tool_result content.

tool_name: string



[](#beta_tool_reference_block_param.tool_name)

type: "tool_reference"



[](#beta_tool_reference_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_reference_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_reference_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_reference_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_reference_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_reference_block_param.cache_control)

[](#beta_tool_reference_block_param)

[](#beta_tool_result_block_param.content%5B1%5D)

[](#beta_tool_result_block_param.content)

is_error: optional boolean



[](#beta_tool_result_block_param.is_error)

[](#beta_tool_result_block_param)



BetaServerToolUseBlockParam object { id, input, name, 3 more }



id: string



[](#beta_server_tool_use_block_param.id)

input: map\[unknown\]



[](#beta_server_tool_use_block_param.input)



name: "advisor" or "web_search" or "web_fetch" or 5 more



One of the following:

"advisor"



[](#beta_server_tool_use_block_param.name%5B0%5D)

"web_search"



[](#beta_server_tool_use_block_param.name%5B1%5D)

"web_fetch"



[](#beta_server_tool_use_block_param.name%5B2%5D)

"code_execution"



[](#beta_server_tool_use_block_param.name%5B3%5D)

"bash_code_execution"



[](#beta_server_tool_use_block_param.name%5B4%5D)

"text_editor_code_execution"



[](#beta_server_tool_use_block_param.name%5B5%5D)

"tool_search_tool_regex"



[](#beta_server_tool_use_block_param.name%5B6%5D)

"tool_search_tool_bm25"



[](#beta_server_tool_use_block_param.name%5B7%5D)

[](#beta_server_tool_use_block_param.name)

type: "server_tool_use"



[](#beta_server_tool_use_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_server_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_server_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_server_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_server_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_server_tool_use_block_param.cache_control)



caller: optional [BetaDirectCaller](/docs/en/api/beta/messages#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta/messages#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta/messages#beta_server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



BetaDirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#beta_direct_caller.type)

[](#beta_direct_caller)



BetaServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#beta_server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#beta_server_tool_caller.type)

[](#beta_server_tool_caller)



BetaServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#beta_server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#beta_server_tool_caller_20260120.type)

[](#beta_server_tool_caller_20260120)

[](#beta_server_tool_use_block_param.caller)

[](#beta_server_tool_use_block_param)



BetaWebSearchToolResultBlockParam object { content, tool_use_id, type, 2 more }





content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta/messages#beta_web_search_tool_result_block_param_content)



One of the following:



ResultBlock = array of [BetaWebSearchResultBlockParam](/docs/en/api/beta/messages#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more }



encrypted_content: string



[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.encrypted_content)

title: string



[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.title)

type: "web_search_result"



[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.type)

url: string



[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.url)

page_age: optional string



[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.page_age)

[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages%5B0%5D)



BetaWebSearchToolRequestError object { error_code, type }





error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta/messages#beta_web_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#beta_web_search_tool_request_error.error_code%20%2B%20(resource)%20beta.messages%5B0%5D)

"unavailable"



[](#beta_web_search_tool_request_error.error_code%20%2B%20(resource)%20beta.messages%5B1%5D)

"max_uses_exceeded"



[](#beta_web_search_tool_request_error.error_code%20%2B%20(resource)%20beta.messages%5B2%5D)

"too_many_requests"



[](#beta_web_search_tool_request_error.error_code%20%2B%20(resource)%20beta.messages%5B3%5D)

"query_too_long"



[](#beta_web_search_tool_request_error.error_code%20%2B%20(resource)%20beta.messages%5B4%5D)

"request_too_large"



[](#beta_web_search_tool_request_error.error_code%20%2B%20(resource)%20beta.messages%5B5%5D)

[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.error_code)

type: "web_search_tool_result_error"



[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_search_tool_result_block_param.content%20%2B%20(resource)%20beta.messages)

[](#beta_web_search_tool_result_block_param.content)

tool_use_id: string



[](#beta_web_search_tool_result_block_param.tool_use_id)

type: "web_search_tool_result"



[](#beta_web_search_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_search_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_search_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_search_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_search_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_search_tool_result_block_param.cache_control)



caller: optional [BetaDirectCaller](/docs/en/api/beta/messages#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta/messages#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta/messages#beta_server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



BetaDirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#beta_direct_caller.type)

[](#beta_direct_caller)



BetaServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#beta_server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#beta_server_tool_caller.type)

[](#beta_server_tool_caller)



BetaServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#beta_server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#beta_server_tool_caller_20260120.type)

[](#beta_server_tool_caller_20260120)

[](#beta_web_search_tool_result_block_param.caller)

[](#beta_web_search_tool_result_block_param)



BetaWebFetchToolResultBlockParam object { content, tool_use_id, type, 2 more }





content: [BetaWebFetchToolResultErrorBlockParam](/docs/en/api/beta/messages#beta_web_fetch_tool_result_error_block_param) { error_code, type } or [BetaWebFetchBlockParam](/docs/en/api/beta/messages#beta_web_fetch_block_param) { content, type, url, retrieved_at }



One of the following:



BetaWebFetchToolResultErrorBlockParam object { error_code, type }





error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta/messages#beta_web_fetch_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B0%5D)

"url_too_long"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B1%5D)

"url_not_allowed"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B2%5D)

"url_not_in_prior_context"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B3%5D)

"url_not_accessible"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B4%5D)

"unsupported_content_type"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B5%5D)

"too_many_requests"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B6%5D)

"max_uses_exceeded"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B7%5D)

"unavailable"



[](#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20(resource)%20beta.messages%5B8%5D)

[](#beta_web_fetch_tool_result_error_block_param.error_code)

type: "web_fetch_tool_result_error"



[](#beta_web_fetch_tool_result_error_block_param.type)

[](#beta_web_fetch_tool_result_error_block_param)



BetaWebFetchBlockParam object { content, type, url, retrieved_at }





content: [BetaRequestDocumentBlock](/docs/en/api/beta/messages#beta_request_document_block) { source, type, cache_control, 3 more }





source: [BetaBase64PDFSource](/docs/en/api/beta/messages#beta_base64_pdf_source) { data, media_type, type } or [BetaPlainTextSource](/docs/en/api/beta/messages#beta_plain_text_source) { data, media_type, type } or [BetaContentBlockSource](/docs/en/api/beta/messages#beta_content_block_source) { content, type } or 2 more



One of the following:



BetaBase64PDFSource object { data, media_type, type }



data: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.data)

media_type: "application/pdf"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.media_type)

type: "base64"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaPlainTextSource object { data, media_type, type }



data: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.data)

media_type: "text/plain"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.media_type)

type: "text"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaContentBlockSource object { content, type }





content: string or array of [BetaContentBlockSourceContent](/docs/en/api/beta/messages#beta_content_block_source_content)



One of the following:

string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.content%5B0%5D)



BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/beta/messages#beta_content_block_source_content)



One of the following:



BetaTextBlockParam object { text, type, cache_control, citations }



text: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.text)

type: "text"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.cited_text)

document_index: number



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.document_index)

document_title: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.document_title)

end_char_index: number



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.end_char_index)

start_char_index: number



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.start_char_index)

type: "char_location"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.cited_text)

document_index: number



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.document_index)

document_title: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.document_title)

end_page_number: number



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.end_page_number)

start_page_number: number



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.start_page_number)

type: "page_location"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.cited_text)

document_index: number



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.document_index)

document_title: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.start_block_index)

type: "content_block_location"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.cited_text)

encrypted_index: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.encrypted_index)

title: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.title)

type: "web_search_result_location"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

url: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.url)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.search_result_index)

source: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.start_block_index)

title: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.title)

type: "search_result_location"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.citations)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaImageBlockParam object { source, type, cache_control }





source: [BetaBase64ImageSource](/docs/en/api/beta/messages#beta_base64_image_source) { data, media_type, type } or [BetaURLImageSource](/docs/en/api/beta/messages#beta_url_image_source) { type, url } or [BetaFileImageSource](/docs/en/api/beta/messages#beta_file_image_source) { file_id, type }



One of the following:



BetaBase64ImageSource object { data, media_type, type }



data: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.data)



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.media_type%5B0%5D)

"image/png"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.media_type%5B1%5D)

"image/gif"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.media_type%5B2%5D)

"image/webp"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.media_type%5B3%5D)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.media_type)

type: "base64"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaURLImageSource object { type, url }



type: "url"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

url: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.url)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaFileImageSource object { file_id, type }



file_id: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.file_id)

type: "file"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.source)

type: "image"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_image_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.cache_control)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.content%5B1%5D)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.content)

type: "content"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaURLPDFSource object { type, url }



type: "url"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

url: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.url)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)



BetaFileDocumentSource object { file_id, type }



file_id: string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.file_id)

type: "file"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.source)

type: "document"



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_request_document_block.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



enabled: optional boolean



[](#beta_request_document_block.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.citations)

context: optional string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.context)

title: optional string



[](#beta_web_fetch_block_param.content%20%2B%20(resource)%20beta.messages.title)

[](#beta_web_fetch_block_param.content)

type: "web_fetch_result"



[](#beta_web_fetch_block_param.type)

url: string



Fetched content URL

[](#beta_web_fetch_block_param.url)

retrieved_at: optional string



ISO 8601 timestamp when the content was retrieved

[](#beta_web_fetch_block_param.retrieved_at)

[](#beta_web_fetch_block_param)

[](#beta_web_fetch_tool_result_block_param.content)

tool_use_id: string



[](#beta_web_fetch_tool_result_block_param.tool_use_id)

type: "web_fetch_tool_result"



[](#beta_web_fetch_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_fetch_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_fetch_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_fetch_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_fetch_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_fetch_tool_result_block_param.cache_control)



caller: optional [BetaDirectCaller](/docs/en/api/beta/messages#beta_direct_caller) { type } or [BetaServerToolCaller](/docs/en/api/beta/messages#beta_server_tool_caller) { tool_id, type } or [BetaServerToolCaller20260120](/docs/en/api/beta/messages#beta_server_tool_caller_20260120) { tool_id, type }



Tool invocation directly from the model.

One of the following:



BetaDirectCaller object { type }



Tool invocation directly from the model.

type: "direct"



[](#beta_direct_caller.type)

[](#beta_direct_caller)



BetaServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#beta_server_tool_caller.tool_id)

type: "code_execution_20250825"



[](#beta_server_tool_caller.type)

[](#beta_server_tool_caller)



BetaServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#beta_server_tool_caller_20260120.tool_id)

type: "code_execution_20260120"



[](#beta_server_tool_caller_20260120.type)

[](#beta_server_tool_caller_20260120)

[](#beta_web_fetch_tool_result_block_param.caller)

[](#beta_web_fetch_tool_result_block_param)



BetaAdvisorToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [BetaAdvisorToolResultErrorParam](/docs/en/api/beta/messages#beta_advisor_tool_result_error_param) { error_code, type } or [BetaAdvisorResultBlockParam](/docs/en/api/beta/messages#beta_advisor_result_block_param) { text, type, stop_reason } or [BetaAdvisorRedactedResultBlockParam](/docs/en/api/beta/messages#beta_advisor_redacted_result_block_param) { encrypted_content, type, stop_reason }



One of the following:



BetaAdvisorToolResultErrorParam object { error_code, type }





error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more



One of the following:

"max_uses_exceeded"



[](#beta_advisor_tool_result_error_param.error_code%5B0%5D)

"prompt_too_long"



[](#beta_advisor_tool_result_error_param.error_code%5B1%5D)

"too_many_requests"



[](#beta_advisor_tool_result_error_param.error_code%5B2%5D)

"overloaded"



[](#beta_advisor_tool_result_error_param.error_code%5B3%5D)

"unavailable"



[](#beta_advisor_tool_result_error_param.error_code%5B4%5D)

"execution_time_exceeded"



[](#beta_advisor_tool_result_error_param.error_code%5B5%5D)

"model_not_found"



[](#beta_advisor_tool_result_error_param.error_code%5B6%5D)

[](#beta_advisor_tool_result_error_param.error_code)

type: "advisor_tool_result_error"



[](#beta_advisor_tool_result_error_param.type)

[](#beta_advisor_tool_result_error_param)



BetaAdvisorResultBlockParam object { text, type, stop_reason }



text: string



[](#beta_advisor_result_block_param.text)

type: "advisor_result"



[](#beta_advisor_result_block_param.type)

stop_reason: optional string



[](#beta_advisor_result_block_param.stop_reason)

[](#beta_advisor_result_block_param)



BetaAdvisorRedactedResultBlockParam object { encrypted_content, type, stop_reason }



encrypted_content: string



Opaque blob produced by a prior response; must be round-tripped verbatim.

[](#beta_advisor_redacted_result_block_param.encrypted_content)

type: "advisor_redacted_result"



[](#beta_advisor_redacted_result_block_param.type)

stop_reason: optional string



[](#beta_advisor_redacted_result_block_param.stop_reason)

[](#beta_advisor_redacted_result_block_param)

[](#beta_advisor_tool_result_block_param.content)

tool_use_id: string



[](#beta_advisor_tool_result_block_param.tool_use_id)

type: "advisor_tool_result"



[](#beta_advisor_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_advisor_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_advisor_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_advisor_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_advisor_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_advisor_tool_result_block_param.cache_control)

[](#beta_advisor_tool_result_block_param)



BetaCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta/messages#beta_code_execution_tool_result_block_param_content)



Code execution result with encrypted stdout for PFC + web_search results.

One of the following:



BetaCodeExecutionToolResultErrorParam object { error_code, type }





error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta/messages#beta_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



[](#beta_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20beta.messages%5B0%5D)

"unavailable"



[](#beta_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20beta.messages%5B1%5D)

"too_many_requests"



[](#beta_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20beta.messages%5B2%5D)

"execution_time_exceeded"



[](#beta_code_execution_tool_result_error_param.error_code%20%2B%20(resource)%20beta.messages%5B3%5D)

[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.error_code)

type: "code_execution_tool_result_error"



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages)



BetaCodeExecutionResultBlockParam object { content, return_code, stderr, 2 more }





content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta/messages#beta_code_execution_output_block_param) { file_id, type }



file_id: string



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.file_id)

type: "code_execution_output"



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.content)

return_code: number



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.return_code)

stderr: string



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.stderr)

stdout: string



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.stdout)

type: "code_execution_result"



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages)



BetaEncryptedCodeExecutionResultBlockParam object { content, encrypted_stdout, return_code, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.



content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/beta/messages#beta_code_execution_output_block_param) { file_id, type }



file_id: string



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.file_id)

type: "code_execution_output"



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.content)

encrypted_stdout: string



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.encrypted_stdout)

return_code: number



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.return_code)

stderr: string



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.stderr)

type: "encrypted_code_execution_result"



[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages.type)

[](#beta_code_execution_tool_result_block_param.content%20%2B%20(resource)%20beta.messages)

[](#beta_code_execution_tool_result_block_param.content)

tool_use_id: string



[](#beta_code_execution_tool_result_block_param.tool_use_id)

type: "code_execution_tool_result"



[](#beta_code_execution_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_code_execution_tool_result_block_param.cache_control)

[](#beta_code_execution_tool_result_block_param)



BetaBashCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [BetaBashCodeExecutionToolResultErrorParam](/docs/en/api/beta/messages#beta_bash_code_execution_tool_result_error_param) { error_code, type } or [BetaBashCodeExecutionResultBlockParam](/docs/en/api/beta/messages#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more }



One of the following:



BetaBashCodeExecutionToolResultErrorParam object { error_code, type }





error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more



One of the following:

"invalid_tool_input"



[](#beta_bash_code_execution_tool_result_error_param.error_code%5B0%5D)

"unavailable"



[](#beta_bash_code_execution_tool_result_error_param.error_code%5B1%5D)

"too_many_requests"



[](#beta_bash_code_execution_tool_result_error_param.error_code%5B2%5D)

"execution_time_exceeded"



[](#beta_bash_code_execution_tool_result_error_param.error_code%5B3%5D)

"output_file_too_large"



[](#beta_bash_code_execution_tool_result_error_param.error_code%5B4%5D)

[](#beta_bash_code_execution_tool_result_error_param.error_code)

type: "bash_code_execution_tool_result_error"



[](#beta_bash_code_execution_tool_result_error_param.type)

[](#beta_bash_code_execution_tool_result_error_param)



BetaBashCodeExecutionResultBlockParam object { content, return_code, stderr, 2 more }





content: array of [BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta/messages#beta_bash_code_execution_output_block_param) { file_id, type }



file_id: string



[](#beta_bash_code_execution_output_block_param.file_id)

type: "bash_code_execution_output"



[](#beta_bash_code_execution_output_block_param.type)

[](#beta_bash_code_execution_result_block_param.content)

return_code: number



[](#beta_bash_code_execution_result_block_param.return_code)

stderr: string



[](#beta_bash_code_execution_result_block_param.stderr)

stdout: string



[](#beta_bash_code_execution_result_block_param.stdout)

type: "bash_code_execution_result"



[](#beta_bash_code_execution_result_block_param.type)

[](#beta_bash_code_execution_result_block_param)

[](#beta_bash_code_execution_tool_result_block_param.content)

tool_use_id: string



[](#beta_bash_code_execution_tool_result_block_param.tool_use_id)

type: "bash_code_execution_tool_result"



[](#beta_bash_code_execution_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_bash_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_bash_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_bash_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_bash_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_bash_code_execution_tool_result_block_param.cache_control)

[](#beta_bash_code_execution_tool_result_block_param)



BetaTextEditorCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [BetaTextEditorCodeExecutionToolResultErrorParam](/docs/en/api/beta/messages#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message } or [BetaTextEditorCodeExecutionViewResultBlockParam](/docs/en/api/beta/messages#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more } or [BetaTextEditorCodeExecutionCreateResultBlockParam](/docs/en/api/beta/messages#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type } or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](/docs/en/api/beta/messages#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more }



One of the following:



BetaTextEditorCodeExecutionToolResultErrorParam object { error_code, type, error_message }





error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more



One of the following:

"invalid_tool_input"



[](#beta_text_editor_code_execution_tool_result_error_param.error_code%5B0%5D)

"unavailable"



[](#beta_text_editor_code_execution_tool_result_error_param.error_code%5B1%5D)

"too_many_requests"



[](#beta_text_editor_code_execution_tool_result_error_param.error_code%5B2%5D)

"execution_time_exceeded"



[](#beta_text_editor_code_execution_tool_result_error_param.error_code%5B3%5D)

"file_not_found"



[](#beta_text_editor_code_execution_tool_result_error_param.error_code%5B4%5D)

[](#beta_text_editor_code_execution_tool_result_error_param.error_code)

type: "text_editor_code_execution_tool_result_error"



[](#beta_text_editor_code_execution_tool_result_error_param.type)

error_message: optional string



[](#beta_text_editor_code_execution_tool_result_error_param.error_message)

[](#beta_text_editor_code_execution_tool_result_error_param)



BetaTextEditorCodeExecutionViewResultBlockParam object { content, file_type, type, 3 more }



content: string



[](#beta_text_editor_code_execution_view_result_block_param.content)



file_type: "text" or "image" or "pdf"



One of the following:

"text"



[](#beta_text_editor_code_execution_view_result_block_param.file_type%5B0%5D)

"image"



[](#beta_text_editor_code_execution_view_result_block_param.file_type%5B1%5D)

"pdf"



[](#beta_text_editor_code_execution_view_result_block_param.file_type%5B2%5D)

[](#beta_text_editor_code_execution_view_result_block_param.file_type)

type: "text_editor_code_execution_view_result"



[](#beta_text_editor_code_execution_view_result_block_param.type)

num_lines: optional number



[](#beta_text_editor_code_execution_view_result_block_param.num_lines)

start_line: optional number



[](#beta_text_editor_code_execution_view_result_block_param.start_line)

total_lines: optional number



[](#beta_text_editor_code_execution_view_result_block_param.total_lines)

[](#beta_text_editor_code_execution_view_result_block_param)



BetaTextEditorCodeExecutionCreateResultBlockParam object { is_file_update, type }



is_file_update: boolean



[](#beta_text_editor_code_execution_create_result_block_param.is_file_update)

type: "text_editor_code_execution_create_result"



[](#beta_text_editor_code_execution_create_result_block_param.type)

[](#beta_text_editor_code_execution_create_result_block_param)



BetaTextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new_lines, 3 more }



type: "text_editor_code_execution_str_replace_result"



[](#beta_text_editor_code_execution_str_replace_result_block_param.type)

lines: optional array of string



[](#beta_text_editor_code_execution_str_replace_result_block_param.lines)

new_lines: optional number



[](#beta_text_editor_code_execution_str_replace_result_block_param.new_lines)

new_start: optional number



[](#beta_text_editor_code_execution_str_replace_result_block_param.new_start)

old_lines: optional number



[](#beta_text_editor_code_execution_str_replace_result_block_param.old_lines)

old_start: optional number



[](#beta_text_editor_code_execution_str_replace_result_block_param.old_start)

[](#beta_text_editor_code_execution_str_replace_result_block_param)

[](#beta_text_editor_code_execution_tool_result_block_param.content)

tool_use_id: string



[](#beta_text_editor_code_execution_tool_result_block_param.tool_use_id)

type: "text_editor_code_execution_tool_result"



[](#beta_text_editor_code_execution_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_editor_code_execution_tool_result_block_param.cache_control)

[](#beta_text_editor_code_execution_tool_result_block_param)



BetaToolSearchToolResultBlockParam object { content, tool_use_id, type, cache_control }





content: [BetaToolSearchToolResultErrorParam](/docs/en/api/beta/messages#beta_tool_search_tool_result_error_param) { error_code, type, error_message } or [BetaToolSearchToolSearchResultBlockParam](/docs/en/api/beta/messages#beta_tool_search_tool_search_result_block_param) { tool_references, type }



One of the following:



BetaToolSearchToolResultErrorParam object { error_code, type, error_message }





error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"



One of the following:

"invalid_tool_input"



[](#beta_tool_search_tool_result_error_param.error_code%5B0%5D)

"unavailable"



[](#beta_tool_search_tool_result_error_param.error_code%5B1%5D)

"too_many_requests"



[](#beta_tool_search_tool_result_error_param.error_code%5B2%5D)

"execution_time_exceeded"



[](#beta_tool_search_tool_result_error_param.error_code%5B3%5D)

[](#beta_tool_search_tool_result_error_param.error_code)

type: "tool_search_tool_result_error"



[](#beta_tool_search_tool_result_error_param.type)

error_message: optional string



[](#beta_tool_search_tool_result_error_param.error_message)

[](#beta_tool_search_tool_result_error_param)



BetaToolSearchToolSearchResultBlockParam object { tool_references, type }





tool_references: array of [BetaToolReferenceBlockParam](/docs/en/api/beta/messages#beta_tool_reference_block_param) { tool_name, type, cache_control }



tool_name: string



[](#beta_tool_reference_block_param.tool_name)

type: "tool_reference"



[](#beta_tool_reference_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_reference_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_reference_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_reference_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_reference_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_reference_block_param.cache_control)

[](#beta_tool_search_tool_search_result_block_param.tool_references)

type: "tool_search_tool_search_result"



[](#beta_tool_search_tool_search_result_block_param.type)

[](#beta_tool_search_tool_search_result_block_param)

[](#beta_tool_search_tool_result_block_param.content)

tool_use_id: string



[](#beta_tool_search_tool_result_block_param.tool_use_id)

type: "tool_search_tool_result"



[](#beta_tool_search_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_search_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_search_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_search_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_search_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_search_tool_result_block_param.cache_control)

[](#beta_tool_search_tool_result_block_param)



BetaMCPToolUseBlockParam object { id, input, name, 3 more }



id: string



[](#beta_mcp_tool_use_block_param.id)

input: map\[unknown\]



[](#beta_mcp_tool_use_block_param.input)

name: string



[](#beta_mcp_tool_use_block_param.name)

server_name: string



The name of the MCP server

[](#beta_mcp_tool_use_block_param.server_name)

type: "mcp_tool_use"



[](#beta_mcp_tool_use_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_mcp_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_mcp_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_mcp_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_mcp_tool_use_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_mcp_tool_use_block_param.cache_control)

[](#beta_mcp_tool_use_block_param)



BetaRequestMCPToolResultBlockParam object { tool_use_id, type, cache_control, 2 more }



tool_use_id: string



[](#beta_request_mcp_tool_result_block_param.tool_use_id)

type: "mcp_tool_result"



[](#beta_request_mcp_tool_result_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_request_mcp_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_request_mcp_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_request_mcp_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_request_mcp_tool_result_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_request_mcp_tool_result_block_param.cache_control)



content: optional string or array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations }



One of the following:

string



[](#beta_request_mcp_tool_result_block_param.content%5B0%5D)



BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#beta_request_mcp_tool_result_block_param.content%5B1%5D)

[](#beta_request_mcp_tool_result_block_param.content)

is_error: optional boolean



[](#beta_request_mcp_tool_result_block_param.is_error)

[](#beta_request_mcp_tool_result_block_param)



BetaContainerUploadBlockParam object { file_id, type, cache_control }



A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: string



[](#beta_container_upload_block_param.file_id)

type: "container_upload"



[](#beta_container_upload_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_container_upload_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_container_upload_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_container_upload_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_container_upload_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_container_upload_block_param.cache_control)

[](#beta_container_upload_block_param)



BetaCompactionBlockParam object { type, cache_control, content, encrypted_content }



A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

type: "compaction"



[](#beta_compaction_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_compaction_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_compaction_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_compaction_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_compaction_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_compaction_block_param.cache_control)

content: optional string



Summary of previously compacted content, or null if compaction failed

[](#beta_compaction_block_param.content)

encrypted_content: optional string



Opaque metadata from prior compaction, to be round-tripped verbatim

[](#beta_compaction_block_param.encrypted_content)

[](#beta_compaction_block_param)



BetaMidConversationSystemBlockParam object { content, type, cache_control }



System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific point in the conversation, rather than only via the top-level `system` parameter.



content: array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations } or [BetaRequestToolAdditionBlock](/docs/en/api/beta/messages#beta_request_tool_addition_block) { tool, type, cache_control } or [BetaRequestToolRemovalBlock](/docs/en/api/beta/messages#beta_request_tool_removal_block) { tool, type, cache_control }



System instruction text blocks.

One of the following:



BetaTextBlockParam object { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#beta_text_block_param)



BetaRequestToolAdditionBlock object { tool, type, cache_control }



Mid-conversation directive to surface a declared tool.

`tool` references a tool (or MCP toolset) by name from the request's `tools`; it is offered to the model from this point in the conversation onward.



tool: [BetaToolChangeToolReference](/docs/en/api/beta/messages#beta_tool_change_tool_reference) { name, type } or [BetaToolChangeMCPToolReference](/docs/en/api/beta/messages#beta_tool_change_mcp_tool_reference) { name, server_name, type } or [BetaToolChangeMCPToolsetReference](/docs/en/api/beta/messages#beta_tool_change_mcp_toolset_reference) { server_name, type }



Reference to a single tool the caller declared directly in `tools[]`. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools — use `mcp_tool_reference` or `mcp_toolset_reference` for those.

One of the following:



BetaToolChangeToolReference object { name, type }



Reference to a single tool the caller declared directly in `tools[]`. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools — use `mcp_tool_reference` or `mcp_toolset_reference` for those.

name: string



[](#beta_tool_change_tool_reference.name)

type: "tool_reference"



[](#beta_tool_change_tool_reference.type)

[](#beta_tool_change_tool_reference)



BetaToolChangeMCPToolReference object { name, server_name, type }



Reference to a single MCP tool by its server and remote name — the same `server_name`/`name` pair `mcp_tool_use` carries.

name: string



[](#beta_tool_change_mcp_tool_reference.name)

server_name: string



[](#beta_tool_change_mcp_tool_reference.server_name)

type: "mcp_tool_reference"



[](#beta_tool_change_mcp_tool_reference.type)

[](#beta_tool_change_mcp_tool_reference)



BetaToolChangeMCPToolsetReference object { server_name, type }



Reference to every tool in the named MCP server's toolset.

server_name: string



[](#beta_tool_change_mcp_toolset_reference.server_name)

type: "mcp_toolset_reference"



[](#beta_tool_change_mcp_toolset_reference.type)

[](#beta_tool_change_mcp_toolset_reference)

[](#beta_request_tool_addition_block.tool)

type: "tool_addition"



[](#beta_request_tool_addition_block.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_request_tool_addition_block.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_request_tool_addition_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_request_tool_addition_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_request_tool_addition_block.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_request_tool_addition_block.cache_control)

[](#beta_request_tool_addition_block)



BetaRequestToolRemovalBlock object { tool, type, cache_control }



Mid-conversation directive to withdraw a tool.

`tool` references a tool (or MCP toolset) by name from the request's `tools`; it is no longer offered to the model from this point in the conversation onward.



tool: [BetaToolChangeToolReference](/docs/en/api/beta/messages#beta_tool_change_tool_reference) { name, type } or [BetaToolChangeMCPToolReference](/docs/en/api/beta/messages#beta_tool_change_mcp_tool_reference) { name, server_name, type } or [BetaToolChangeMCPToolsetReference](/docs/en/api/beta/messages#beta_tool_change_mcp_toolset_reference) { server_name, type }



Reference to a single tool the caller declared directly in `tools[]`. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools — use `mcp_tool_reference` or `mcp_toolset_reference` for those.

One of the following:



BetaToolChangeToolReference object { name, type }



Reference to a single tool the caller declared directly in `tools[]`. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools — use `mcp_tool_reference` or `mcp_toolset_reference` for those.

name: string



[](#beta_tool_change_tool_reference.name)

type: "tool_reference"



[](#beta_tool_change_tool_reference.type)

[](#beta_tool_change_tool_reference)



BetaToolChangeMCPToolReference object { name, server_name, type }



Reference to a single MCP tool by its server and remote name — the same `server_name`/`name` pair `mcp_tool_use` carries.

name: string



[](#beta_tool_change_mcp_tool_reference.name)

server_name: string



[](#beta_tool_change_mcp_tool_reference.server_name)

type: "mcp_tool_reference"



[](#beta_tool_change_mcp_tool_reference.type)

[](#beta_tool_change_mcp_tool_reference)



BetaToolChangeMCPToolsetReference object { server_name, type }



Reference to every tool in the named MCP server's toolset.

server_name: string



[](#beta_tool_change_mcp_toolset_reference.server_name)

type: "mcp_toolset_reference"



[](#beta_tool_change_mcp_toolset_reference.type)

[](#beta_tool_change_mcp_toolset_reference)

[](#beta_request_tool_removal_block.tool)

type: "tool_removal"



[](#beta_request_tool_removal_block.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_request_tool_removal_block.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_request_tool_removal_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_request_tool_removal_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_request_tool_removal_block.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_request_tool_removal_block.cache_control)

[](#beta_request_tool_removal_block)

[](#beta_mid_conversation_system_block_param.content)

type: "mid_conv_system"



[](#beta_mid_conversation_system_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_mid_conversation_system_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_mid_conversation_system_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_mid_conversation_system_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_mid_conversation_system_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_mid_conversation_system_block_param.cache_control)

[](#beta_mid_conversation_system_block_param)



BetaRequestToolAdditionBlock object { tool, type, cache_control }



Mid-conversation directive to surface a declared tool.

`tool` references a tool (or MCP toolset) by name from the request's `tools`; it is offered to the model from this point in the conversation onward.



tool: [BetaToolChangeToolReference](/docs/en/api/beta/messages#beta_tool_change_tool_reference) { name, type } or [BetaToolChangeMCPToolReference](/docs/en/api/beta/messages#beta_tool_change_mcp_tool_reference) { name, server_name, type } or [BetaToolChangeMCPToolsetReference](/docs/en/api/beta/messages#beta_tool_change_mcp_toolset_reference) { server_name, type }



Reference to a single tool the caller declared directly in `tools[]`. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools — use `mcp_tool_reference` or `mcp_toolset_reference` for those.

One of the following:



BetaToolChangeToolReference object { name, type }



Reference to a single tool the caller declared directly in `tools[]`. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools — use `mcp_tool_reference` or `mcp_toolset_reference` for those.

name: string



[](#beta_tool_change_tool_reference.name)

type: "tool_reference"



[](#beta_tool_change_tool_reference.type)

[](#beta_tool_change_tool_reference)



BetaToolChangeMCPToolReference object { name, server_name, type }



Reference to a single MCP tool by its server and remote name — the same `server_name`/`name` pair `mcp_tool_use` carries.

name: string



[](#beta_tool_change_mcp_tool_reference.name)

server_name: string



[](#beta_tool_change_mcp_tool_reference.server_name)

type: "mcp_tool_reference"



[](#beta_tool_change_mcp_tool_reference.type)

[](#beta_tool_change_mcp_tool_reference)



BetaToolChangeMCPToolsetReference object { server_name, type }



Reference to every tool in the named MCP server's toolset.

server_name: string



[](#beta_tool_change_mcp_toolset_reference.server_name)

type: "mcp_toolset_reference"



[](#beta_tool_change_mcp_toolset_reference.type)

[](#beta_tool_change_mcp_toolset_reference)

[](#beta_request_tool_addition_block.tool)

type: "tool_addition"



[](#beta_request_tool_addition_block.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_request_tool_addition_block.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_request_tool_addition_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_request_tool_addition_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_request_tool_addition_block.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_request_tool_addition_block.cache_control)

[](#beta_request_tool_addition_block)



BetaRequestToolRemovalBlock object { tool, type, cache_control }



Mid-conversation directive to withdraw a tool.

`tool` references a tool (or MCP toolset) by name from the request's `tools`; it is no longer offered to the model from this point in the conversation onward.



tool: [BetaToolChangeToolReference](/docs/en/api/beta/messages#beta_tool_change_tool_reference) { name, type } or [BetaToolChangeMCPToolReference](/docs/en/api/beta/messages#beta_tool_change_mcp_tool_reference) { name, server_name, type } or [BetaToolChangeMCPToolsetReference](/docs/en/api/beta/messages#beta_tool_change_mcp_toolset_reference) { server_name, type }



Reference to a single tool the caller declared directly in `tools[]`. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools — use `mcp_tool_reference` or `mcp_toolset_reference` for those.

One of the following:



BetaToolChangeToolReference object { name, type }



Reference to a single tool the caller declared directly in `tools[]`. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools — use `mcp_tool_reference` or `mcp_toolset_reference` for those.

name: string



[](#beta_tool_change_tool_reference.name)

type: "tool_reference"



[](#beta_tool_change_tool_reference.type)

[](#beta_tool_change_tool_reference)



BetaToolChangeMCPToolReference object { name, server_name, type }



Reference to a single MCP tool by its server and remote name — the same `server_name`/`name` pair `mcp_tool_use` carries.

name: string



[](#beta_tool_change_mcp_tool_reference.name)

server_name: string



[](#beta_tool_change_mcp_tool_reference.server_name)

type: "mcp_tool_reference"



[](#beta_tool_change_mcp_tool_reference.type)

[](#beta_tool_change_mcp_tool_reference)



BetaToolChangeMCPToolsetReference object { server_name, type }



Reference to every tool in the named MCP server's toolset.

server_name: string



[](#beta_tool_change_mcp_toolset_reference.server_name)

type: "mcp_toolset_reference"



[](#beta_tool_change_mcp_toolset_reference.type)

[](#beta_tool_change_mcp_toolset_reference)

[](#beta_request_tool_removal_block.tool)

type: "tool_removal"



[](#beta_request_tool_removal_block.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_request_tool_removal_block.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_request_tool_removal_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_request_tool_removal_block.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_request_tool_removal_block.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_request_tool_removal_block.cache_control)

[](#beta_request_tool_removal_block)



BetaFallbackBlockParam object { from, to, type, trigger }



A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its original position. The block marks the boundary between content produced before and after a fallback hop, and the server relies on that boundary to validate the turn: when thinking runs flank the boundary, omitting the block merges them into one span the server cannot validate (the request is rejected), and moving it into the middle of a single run is likewise rejected; between non-thinking blocks the block's placement has no validation effect.



from: [BetaFallbackInfoParam](/docs/en/api/beta/messages#beta_fallback_info_param) { model }



Identifies one hop of a fallback transition.

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

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B1%5D)

[](#beta_fallback_block_param.from%20%2B%20(resource)%20beta.messages.model)

[](#beta_fallback_block_param.from)



to: [BetaFallbackInfoParam](/docs/en/api/beta/messages#beta_fallback_info_param) { model }



Identifies one hop of a fallback transition.

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

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#beta_fallback_info_param.model%20%2B%20(resource)%20messages%5B1%5D)

[](#beta_fallback_block_param.to%20%2B%20(resource)%20beta.messages.model)

[](#beta_fallback_block_param.to)

type: "fallback"



[](#beta_fallback_block_param.type)

trigger: optional unknown



The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

[](#beta_fallback_block_param.trigger)

[](#beta_fallback_block_param)

[](#beta_message_param.content%5B1%5D)

[](#beta_message_param.content)



role: "user" or "assistant" or "system"



One of the following:

"user"



[](#beta_message_param.role%5B0%5D)

"assistant"



[](#beta_message_param.role%5B1%5D)

"system"



[](#beta_message_param.role%5B2%5D)

[](#beta_message_param.role)

[](#create.requests.items.params.messages)

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

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#create.requests.items.params.model%20%2B%20(resource)%20messages%5B1%5D)

[](#create.requests.items.params.model)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

type: "ephemeral"



[](#create.requests.items.params.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#create.requests.items.params.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#create.requests.items.params.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#create.requests.items.params.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#create.requests.items.params.cache_control)



container: optional [BetaContainerParams](/docs/en/api/beta/messages#beta_container_params) { id, skills } or string



Container identifier for reuse across requests.

One of the following:



BetaContainerParams object { id, skills }



Container parameters with skills to be loaded.

id: optional string



Container id

[](#beta_container_params.id)



skills: optional array of [BetaSkillParams](/docs/en/api/beta/messages#beta_skill_params) { skill_id, type, version }



List of skills to load in the container

skill_id: string



Skill ID

[](#beta_skill_params.skill_id)



type: "anthropic" or "custom"



Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"



[](#beta_skill_params.type%5B0%5D)

"custom"



[](#beta_skill_params.type%5B1%5D)

[](#beta_skill_params.type)

version: optional string



Skill version or 'latest' for most recent version

[](#beta_skill_params.version)

[](#beta_container_params.skills)

[](#beta_container_params)

string



[](#create.requests.items.params.container%5B1%5D)

[](#create.requests.items.params.container)



context_management: optional [BetaContextManagementConfig](/docs/en/api/beta/messages#beta_context_management_config) { edits }



Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



edits: optional array of [BetaClearToolUses20250919Edit](/docs/en/api/beta/messages#beta_clear_tool_uses_20250919_edit) { type, clear_at_least, clear_tool_inputs, 3 more } or [BetaClearThinking20251015Edit](/docs/en/api/beta/messages#beta_clear_thinking_20251015_edit) { type, keep } or [BetaCompact20260112Edit](/docs/en/api/beta/messages#beta_compact_20260112_edit) { type, instructions, pause_after_compaction, trigger }



List of context management edits to apply

One of the following:



BetaClearToolUses20250919Edit object { type, clear_at_least, clear_tool_inputs, 3 more }



type: "clear_tool_uses_20250919"



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.type)



clear_at_least: optional [BetaInputTokensClearAtLeast](/docs/en/api/beta/messages#beta_input_tokens_clear_at_least) { type, value }



Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input_tokens"



[](#beta_clear_tool_uses_20250919_edit.clear_at_least%20%2B%20(resource)%20beta.messages.type)

value: number



[](#beta_clear_tool_uses_20250919_edit.clear_at_least%20%2B%20(resource)%20beta.messages.value)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.clear_at_least)



clear_tool_inputs: optional boolean or array of string



Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

boolean



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.clear_tool_inputs%5B0%5D)

array of string



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.clear_tool_inputs%5B1%5D)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.clear_tool_inputs)

exclude_tools: optional array of string



Tool names whose uses are preserved from clearing

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.exclude_tools)



keep: optional [BetaToolUsesKeep](/docs/en/api/beta/messages#beta_tool_uses_keep) { type, value }



Number of tool uses to retain in the conversation

type: "tool_uses"



[](#beta_clear_tool_uses_20250919_edit.keep%20%2B%20(resource)%20beta.messages.type)

value: number



[](#beta_clear_tool_uses_20250919_edit.keep%20%2B%20(resource)%20beta.messages.value)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.keep)



trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta/messages#beta_input_tokens_trigger) { type, value } or [BetaToolUsesTrigger](/docs/en/api/beta/messages#beta_tool_uses_trigger) { type, value }



Condition that triggers the context management strategy

One of the following:



BetaInputTokensTrigger object { type, value }



type: "input_tokens"



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.type)

value: number



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.value)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages)



BetaToolUsesTrigger object { type, value }



type: "tool_uses"



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.type)

value: number



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.value)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.trigger)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages)



BetaClearThinking20251015Edit object { type, keep }



type: "clear_thinking_20251015"



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.type)



keep: optional [BetaThinkingTurns](/docs/en/api/beta/messages#beta_thinking_turns) { type, value } or [BetaAllThinkingTurns](/docs/en/api/beta/messages#beta_all_thinking_turns) { type } or "all"



Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



BetaThinkingTurns object { type, value }



type: "thinking_turns"



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.type)

value: number



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.value)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages)



BetaAllThinkingTurns object { type }



type: "all"



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.type)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages)

"all"



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.keep%5B2%5D)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.keep)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages)



BetaCompact20260112Edit object { type, instructions, pause_after_compaction, trigger }



Automatically compact older context when reaching the configured trigger threshold.

type: "compact_20260112"



[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.type)

instructions: optional string



Additional instructions for summarization.

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.instructions)

pause_after_compaction: optional boolean



Whether to pause after compaction and return the compaction block to the user.

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.pause_after_compaction)



trigger: optional [BetaInputTokensTrigger](/docs/en/api/beta/messages#beta_input_tokens_trigger) { type, value }



When to trigger compaction. Defaults to 150000 input tokens.

type: "input_tokens"



[](#beta_compact_20260112_edit.trigger%20%2B%20(resource)%20beta.messages.type)

value: number



[](#beta_compact_20260112_edit.trigger%20%2B%20(resource)%20beta.messages.value)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.trigger)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages)

[](#create.requests.items.params.context_management%20%2B%20(resource)%20beta.messages.edits)

[](#create.requests.items.params.context_management)



diagnostics: optional [BetaDiagnosticsParam](/docs/en/api/beta/messages#beta_diagnostics_param) { previous_message_id }



Request-level diagnostics. Currently carries the previous response id for prompt-cache divergence reporting.

previous_message_id: optional string



The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

[](#create.requests.items.params.diagnostics%20%2B%20(resource)%20beta.messages.previous_message_id)

[](#create.requests.items.params.diagnostics)



fallback_credit_token: optional string or [BetaFallbackCreditTokenParam](/docs/en/api/beta/messages#beta_fallback_credit_token_param) { token, mode }



The `fallback_credit_token` from a prior refusal's `stop_details`.

When a preceding request was refused and returned a `fallback_credit_token`, pass that code here on the retry to have the retry's cache-creation tokens for the prefix that was warm on the refused model billed at the cache-read rate. Must be redeemed by the same organization and workspace, with the same request body (optionally extended by one appended `assistant` message whose content is the partial text — with any trailing whitespace stripped from the final text block — and paired server-tool blocks streamed before the refusal; the appended-assistant form is not available for requests with `output_format` set or forced `tool_choice`), on an eligible fallback model, on the same platform, and within 5 minutes of the refusal; a mismatch is a 400. A token minted mid-server-tool-loop whose partial content was continuable may only be redeemed with the appended-assistant form — if an exact-body retry is rejected with a 400 saying the token must be redeemed by continuing the partial response, retry with the appended-assistant form instead.

When the appended-assistant form is used on a model that otherwise disallows assistant-turn prefill, this token also authorizes that one prefill.

One of the following:

string



[](#create.requests.items.params.fallback_credit_token%5B0%5D)



BetaFallbackCreditTokenParam object { token, mode }



Object form of `fallback_credit_token`: the token plus a redemption mode.

Requires `anthropic-beta: fallback-credit-2026-07-01`; without that header the field accepts the bare string only. The bare string and the mode-less object are equivalent (both select `strict`), so wrapping an existing token changes nothing by itself.

token: string



The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

[](#beta_fallback_credit_token_param.token)



mode: optional "strict" or "best_effort"



How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

One of the following:

"strict"



[](#beta_fallback_credit_token_param.mode%5B0%5D)

"best_effort"



[](#beta_fallback_credit_token_param.mode%5B1%5D)

[](#beta_fallback_credit_token_param.mode)

[](#beta_fallback_credit_token_param)

[](#create.requests.items.params.fallback_credit_token)



fallbacks: optional [BetaFallbacksParam](/docs/en/api/beta/messages#beta_fallbacks_param)



Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

One of the following:



array of [BetaFallbackParam](/docs/en/api/beta/messages#beta_fallback_param) { model, max_tokens, output_config, 2 more }



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

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#beta_fallback_param.model%20%2B%20(resource)%20messages%5B1%5D)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.model)

max_tokens: optional number



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.max_tokens)



output_config: optional [BetaOutputConfig](/docs/en/api/beta/messages#beta_output_config) { effort, format, task_budget }





effort: optional "low" or "medium" or "high" or 2 more



All possible effort levels.

One of the following:

"low"



[](#beta_fallback_param.output_config%20%2B%20(resource)%20beta.messages.effort%5B0%5D)

"medium"



[](#beta_fallback_param.output_config%20%2B%20(resource)%20beta.messages.effort%5B1%5D)

"high"



[](#beta_fallback_param.output_config%20%2B%20(resource)%20beta.messages.effort%5B2%5D)

"xhigh"



[](#beta_fallback_param.output_config%20%2B%20(resource)%20beta.messages.effort%5B3%5D)

"max"



[](#beta_fallback_param.output_config%20%2B%20(resource)%20beta.messages.effort%5B4%5D)

[](#beta_fallback_param.output_config%20%2B%20(resource)%20beta.messages.effort)



format: optional [BetaJSONOutputFormat](/docs/en/api/beta/messages#beta_json_output_format) { schema, type }



A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: map\[unknown\]



The JSON schema of the format

[](#beta_output_config.format%20%2B%20(resource)%20beta.messages.schema)

type: "json_schema"



[](#beta_output_config.format%20%2B%20(resource)%20beta.messages.type)

[](#beta_fallback_param.output_config%20%2B%20(resource)%20beta.messages.format)



task_budget: optional [BetaTokenTaskBudget](/docs/en/api/beta/messages#beta_token_task_budget) { total, type, remaining }



User-configurable total token budget across contexts.

total: number



Total token budget across all contexts in the session.

[](#beta_output_config.task_budget%20%2B%20(resource)%20beta.messages.total)

type: "tokens"



The budget type. Currently only 'tokens' is supported.

[](#beta_output_config.task_budget%20%2B%20(resource)%20beta.messages.type)

remaining: optional number



Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

[](#beta_output_config.task_budget%20%2B%20(resource)%20beta.messages.remaining)

[](#beta_fallback_param.output_config%20%2B%20(resource)%20beta.messages.task_budget)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.output_config)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.speed%5B0%5D)

"fast"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.speed%5B1%5D)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.speed)



thinking: optional [BetaThinkingConfigEnabled](/docs/en/api/beta/messages#beta_thinking_config_enabled) { budget_tokens, type, display } or [BetaThinkingConfigDisabled](/docs/en/api/beta/messages#beta_thinking_config_disabled) { type } or [BetaThinkingConfigAdaptive](/docs/en/api/beta/messages#beta_thinking_config_adaptive) { type, display }



One of the following:



BetaThinkingConfigEnabled object { budget_tokens, type, display }





budget_tokens: number



Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

minimum1024

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.budget_tokens)

type: "enabled"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.type)



display: optional "summarized" or "omitted"



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.display%5B0%5D)

"omitted"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.display%5B1%5D)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.display)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages)



BetaThinkingConfigDisabled object { type }



type: "disabled"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.type)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages)



BetaThinkingConfigAdaptive object { type, display }



type: "adaptive"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.type)



display: optional "summarized" or "omitted"



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.display%5B0%5D)

"omitted"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.display%5B1%5D)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.display)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages.thinking)

[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages%5B0%5D)

Default = "default"



[](#create.requests.items.params.fallbacks%20%2B%20(resource)%20beta.messages%5B1%5D)

[](#create.requests.items.params.fallbacks)

inference_geo: optional string



Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

[](#create.requests.items.params.inference_geo)



mcp_servers: optional array of [BetaRequestMCPServerURLDefinition](/docs/en/api/beta/messages#beta_request_mcp_server_url_definition) { name, type, url, 2 more }



MCP servers to be utilized in this request

name: string



[](#beta_request_mcp_server_url_definition.name)

type: "url"



[](#beta_request_mcp_server_url_definition.type)

url: string



[](#beta_request_mcp_server_url_definition.url)

authorization_token: optional string



[](#beta_request_mcp_server_url_definition.authorization_token)



tool_configuration: optional [BetaRequestMCPServerToolConfiguration](/docs/en/api/beta/messages#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled }



allowed_tools: optional array of string



[](#beta_request_mcp_server_url_definition.tool_configuration%20%2B%20(resource)%20beta.messages.allowed_tools)

enabled: optional boolean



[](#beta_request_mcp_server_url_definition.tool_configuration%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_request_mcp_server_url_definition.tool_configuration)

[](#create.requests.items.params.mcp_servers)



metadata: optional [BetaMetadata](/docs/en/api/beta/messages#beta_metadata) { user_id }



An object describing metadata about the request.



user_id: optional string



An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

[](#create.requests.items.params.metadata%20%2B%20(resource)%20beta.messages.user_id)

[](#create.requests.items.params.metadata)



output_config: optional [BetaOutputConfig](/docs/en/api/beta/messages#beta_output_config) { effort, format, task_budget }



Configuration options for the model's output, such as the output format.



effort: optional "low" or "medium" or "high" or 2 more



All possible effort levels.

One of the following:

"low"



[](#create.requests.items.params.output_config%20%2B%20(resource)%20beta.messages.effort%5B0%5D)

"medium"



[](#create.requests.items.params.output_config%20%2B%20(resource)%20beta.messages.effort%5B1%5D)

"high"



[](#create.requests.items.params.output_config%20%2B%20(resource)%20beta.messages.effort%5B2%5D)

"xhigh"



[](#create.requests.items.params.output_config%20%2B%20(resource)%20beta.messages.effort%5B3%5D)

"max"



[](#create.requests.items.params.output_config%20%2B%20(resource)%20beta.messages.effort%5B4%5D)

[](#create.requests.items.params.output_config%20%2B%20(resource)%20beta.messages.effort)



format: optional [BetaJSONOutputFormat](/docs/en/api/beta/messages#beta_json_output_format) { schema, type }



A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: map\[unknown\]



The JSON schema of the format

[](#beta_output_config.format%20%2B%20(resource)%20beta.messages.schema)

type: "json_schema"



[](#beta_output_config.format%20%2B%20(resource)%20beta.messages.type)

[](#create.requests.items.params.output_config%20%2B%20(resource)%20beta.messages.format)



task_budget: optional [BetaTokenTaskBudget](/docs/en/api/beta/messages#beta_token_task_budget) { total, type, remaining }



User-configurable total token budget across contexts.

total: number



Total token budget across all contexts in the session.

[](#beta_output_config.task_budget%20%2B%20(resource)%20beta.messages.total)

type: "tokens"



The budget type. Currently only 'tokens' is supported.

[](#beta_output_config.task_budget%20%2B%20(resource)%20beta.messages.type)

remaining: optional number



Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

[](#beta_output_config.task_budget%20%2B%20(resource)%20beta.messages.remaining)

[](#create.requests.items.params.output_config%20%2B%20(resource)%20beta.messages.task_budget)

[](#create.requests.items.params.output_config)



service_tier: optional "auto" or "standard_only"



Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

One of the following:

"auto"



[](#create.requests.items.params.service_tier%5B0%5D)

"standard_only"



[](#create.requests.items.params.service_tier%5B1%5D)

[](#create.requests.items.params.service_tier)



speed: optional "standard" or "fast"



Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"



[](#create.requests.items.params.speed%5B0%5D)

"fast"



[](#create.requests.items.params.speed%5B1%5D)

[](#create.requests.items.params.speed)



stop_sequences: optional array of string



Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

[](#create.requests.items.params.stop_sequences)



stream: optional boolean



Whether to incrementally stream the response using server-sent events.

See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

[](#create.requests.items.params.stream)



system: optional string or array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations }



System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

One of the following:

string



[](#create.requests.items.params.system%5B0%5D)



array of [BetaTextBlockParam](/docs/en/api/beta/messages#beta_text_block_param) { text, type, cache_control, citations }



text: string



[](#beta_text_block_param.text)

type: "text"



[](#beta_text_block_param.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_text_block_param.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_text_block_param.cache_control)



citations: optional array of [BetaTextCitationParam](/docs/en/api/beta/messages#beta_text_citation_param)



One of the following:



BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_char_location_param.cited_text)

document_index: number



[](#beta_citation_char_location_param.document_index)

document_title: string



[](#beta_citation_char_location_param.document_title)

end_char_index: number



[](#beta_citation_char_location_param.end_char_index)

start_char_index: number



[](#beta_citation_char_location_param.start_char_index)

type: "char_location"



[](#beta_citation_char_location_param.type)

[](#beta_citation_char_location_param)



BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more }



cited_text: string



[](#beta_citation_page_location_param.cited_text)

document_index: number



[](#beta_citation_page_location_param.document_index)

document_title: string



[](#beta_citation_page_location_param.document_title)

end_page_number: number



[](#beta_citation_page_location_param.end_page_number)

start_page_number: number



[](#beta_citation_page_location_param.start_page_number)

type: "page_location"



[](#beta_citation_page_location_param.type)

[](#beta_citation_page_location_param)



BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_content_block_location_param.cited_text)

document_index: number



[](#beta_citation_content_block_location_param.document_index)

document_title: string



[](#beta_citation_content_block_location_param.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_content_block_location_param.end_block_index)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_content_block_location_param.start_block_index)

type: "content_block_location"



[](#beta_citation_content_block_location_param.type)

[](#beta_citation_content_block_location_param)



BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#beta_citation_web_search_result_location_param.cited_text)

encrypted_index: string



[](#beta_citation_web_search_result_location_param.encrypted_index)

title: string



[](#beta_citation_web_search_result_location_param.title)

type: "web_search_result_location"



[](#beta_citation_web_search_result_location_param.type)

url: string



[](#beta_citation_web_search_result_location_param.url)

[](#beta_citation_web_search_result_location_param)



BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#beta_citation_search_result_location_param.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#beta_citation_search_result_location_param.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#beta_citation_search_result_location_param.search_result_index)

source: string



[](#beta_citation_search_result_location_param.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#beta_citation_search_result_location_param.start_block_index)

title: string



[](#beta_citation_search_result_location_param.title)

type: "search_result_location"



[](#beta_citation_search_result_location_param.type)

[](#beta_citation_search_result_location_param)

[](#beta_text_block_param.citations)

[](#create.requests.items.params.system%5B1%5D)

[](#create.requests.items.params.system)



thinking: optional [BetaThinkingConfigParam](/docs/en/api/beta/messages#beta_thinking_config_param)



Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

One of the following:



BetaThinkingConfigEnabled object { budget_tokens, type, display }





budget_tokens: number



Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

minimum1024

[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.budget_tokens)

type: "enabled"



[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.type)



display: optional "summarized" or "omitted"



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.display%5B0%5D)

"omitted"



[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.display%5B1%5D)

[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.display)

[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages)



BetaThinkingConfigDisabled object { type }



type: "disabled"



[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.type)

[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages)



BetaThinkingConfigAdaptive object { type, display }



type: "adaptive"



[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.type)



display: optional "summarized" or "omitted"



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.display%5B0%5D)

"omitted"



[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.display%5B1%5D)

[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages.display)

[](#create.requests.items.params.thinking%20%2B%20(resource)%20beta.messages)

[](#create.requests.items.params.thinking)



tool_choice: optional [BetaToolChoice](/docs/en/api/beta/messages#beta_tool_choice)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



BetaToolChoiceAuto object { type, disable_parallel_tool_use }



The model will automatically decide whether to use tools.

type: "auto"



[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages.type)



disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages.disable_parallel_tool_use)

[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages)



BetaToolChoiceAny object { type, disable_parallel_tool_use }



The model will use any available tools.

type: "any"



[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages.type)



disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages.disable_parallel_tool_use)

[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages)



BetaToolChoiceTool object { name, type, disable_parallel_tool_use }



The model will use the specified tool with `tool_choice.name`.

name: string



The name of the tool to use.

[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages.name)

type: "tool"



[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages.type)



disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages.disable_parallel_tool_use)

[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages)



BetaToolChoiceNone object { type }



The model will not be allowed to use tools.

type: "none"



[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages.type)

[](#create.requests.items.params.tool_choice%20%2B%20(resource)%20beta.messages)

[](#create.requests.items.params.tool_choice)



tools: optional array of [BetaToolUnion](/docs/en/api/beta/messages#beta_tool_union)

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

BetaTool object { input_schema, name, allowed_callers, 7 more }





input_schema: object { type, properties, required }



[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"



[](#beta_tool.input_schema.type)

properties: optional map\[unknown\]



[](#beta_tool.input_schema.properties)

required: optional array of string



[](#beta_tool.input_schema.required)

[](#beta_tool.input_schema)



name: string



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

[](#beta_tool.name)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool.allowed_callers.items%5B3%5D)

[](#beta_tool.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool.defer_loading)



description: optional string



Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

[](#beta_tool.description)

eager_input_streaming: optional boolean



Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

[](#beta_tool.eager_input_streaming)

input_examples: optional array of map\[unknown\]



[](#beta_tool.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool.strict)

type: optional "custom"



[](#beta_tool.type)

[](#beta_tool)



BetaToolBash20241022 object { name, type, allowed_callers, 4 more }





name: "bash"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_bash_20241022.name)

type: "bash_20241022"



[](#beta_tool_bash_20241022.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_bash_20241022.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_bash_20241022.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_bash_20241022.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_bash_20241022.allowed_callers.items%5B3%5D)

[](#beta_tool_bash_20241022.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_bash_20241022.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_bash_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_bash_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_bash_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_bash_20241022.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_bash_20241022.defer_loading)

input_examples: optional array of map\[unknown\]



[](#beta_tool_bash_20241022.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_bash_20241022.strict)

[](#beta_tool_bash_20241022)



BetaToolBash20250124 object { name, type, allowed_callers, 4 more }





name: "bash"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_bash_20250124.name)

type: "bash_20250124"



[](#beta_tool_bash_20250124.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_bash_20250124.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_bash_20250124.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_bash_20250124.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_bash_20250124.allowed_callers.items%5B3%5D)

[](#beta_tool_bash_20250124.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_bash_20250124.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_bash_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_bash_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_bash_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_bash_20250124.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_bash_20250124.defer_loading)

input_examples: optional array of map\[unknown\]



[](#beta_tool_bash_20250124.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_bash_20250124.strict)

[](#beta_tool_bash_20250124)



BetaCodeExecutionTool20250522 object { name, type, allowed_callers, 3 more }





name: "code_execution"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_code_execution_tool_20250522.name)

type: "code_execution_20250522"



[](#beta_code_execution_tool_20250522.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_code_execution_tool_20250522.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_code_execution_tool_20250522.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_code_execution_tool_20250522.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_code_execution_tool_20250522.allowed_callers.items%5B3%5D)

[](#beta_code_execution_tool_20250522.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_code_execution_tool_20250522.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_code_execution_tool_20250522.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_code_execution_tool_20250522.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_code_execution_tool_20250522.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_code_execution_tool_20250522.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_code_execution_tool_20250522.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_code_execution_tool_20250522.strict)

[](#beta_code_execution_tool_20250522)



BetaCodeExecutionTool20250825 object { name, type, allowed_callers, 3 more }





name: "code_execution"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_code_execution_tool_20250825.name)

type: "code_execution_20250825"



[](#beta_code_execution_tool_20250825.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_code_execution_tool_20250825.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_code_execution_tool_20250825.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_code_execution_tool_20250825.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_code_execution_tool_20250825.allowed_callers.items%5B3%5D)

[](#beta_code_execution_tool_20250825.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_code_execution_tool_20250825.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_code_execution_tool_20250825.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_code_execution_tool_20250825.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_code_execution_tool_20250825.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_code_execution_tool_20250825.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_code_execution_tool_20250825.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_code_execution_tool_20250825.strict)

[](#beta_code_execution_tool_20250825)



BetaCodeExecutionTool20260120 object { name, type, allowed_callers, 3 more }



Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code_execution"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_code_execution_tool_20260120.name)

type: "code_execution_20260120"



[](#beta_code_execution_tool_20260120.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_code_execution_tool_20260120.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_code_execution_tool_20260120.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_code_execution_tool_20260120.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_code_execution_tool_20260120.allowed_callers.items%5B3%5D)

[](#beta_code_execution_tool_20260120.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_code_execution_tool_20260120.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_code_execution_tool_20260120.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_code_execution_tool_20260120.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_code_execution_tool_20260120.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_code_execution_tool_20260120.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_code_execution_tool_20260120.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_code_execution_tool_20260120.strict)

[](#beta_code_execution_tool_20260120)



BetaCodeExecutionTool20260521 object { name, type, allowed_callers, 3 more }



Code execution tool with REPL state persistence.



name: "code_execution"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_code_execution_tool_20260521.name)

type: "code_execution_20260521"



[](#beta_code_execution_tool_20260521.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_code_execution_tool_20260521.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_code_execution_tool_20260521.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_code_execution_tool_20260521.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_code_execution_tool_20260521.allowed_callers.items%5B3%5D)

[](#beta_code_execution_tool_20260521.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_code_execution_tool_20260521.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_code_execution_tool_20260521.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_code_execution_tool_20260521.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_code_execution_tool_20260521.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_code_execution_tool_20260521.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_code_execution_tool_20260521.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_code_execution_tool_20260521.strict)

[](#beta_code_execution_tool_20260521)



BetaToolComputerUse20241022 object { display_height_px, display_width_px, name, 7 more }



display_height_px: number



The height of the display in pixels.

[](#beta_tool_computer_use_20241022.display_height_px)

display_width_px: number



The width of the display in pixels.

[](#beta_tool_computer_use_20241022.display_width_px)



name: "computer"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_computer_use_20241022.name)

type: "computer_20241022"



[](#beta_tool_computer_use_20241022.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_computer_use_20241022.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_computer_use_20241022.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_computer_use_20241022.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_computer_use_20241022.allowed_callers.items%5B3%5D)

[](#beta_tool_computer_use_20241022.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_computer_use_20241022.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_computer_use_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_computer_use_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_computer_use_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_computer_use_20241022.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_computer_use_20241022.defer_loading)

display_number: optional number



The X11 display number (e.g. 0, 1) for the display.

[](#beta_tool_computer_use_20241022.display_number)

input_examples: optional array of map\[unknown\]



[](#beta_tool_computer_use_20241022.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_computer_use_20241022.strict)

[](#beta_tool_computer_use_20241022)



BetaMemoryTool20250818 object { name, type, allowed_callers, 4 more }





name: "memory"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_memory_tool_20250818.name)

type: "memory_20250818"



[](#beta_memory_tool_20250818.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_memory_tool_20250818.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_memory_tool_20250818.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_memory_tool_20250818.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_memory_tool_20250818.allowed_callers.items%5B3%5D)

[](#beta_memory_tool_20250818.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_memory_tool_20250818.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_memory_tool_20250818.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_memory_tool_20250818.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_memory_tool_20250818.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_memory_tool_20250818.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_memory_tool_20250818.defer_loading)

input_examples: optional array of map\[unknown\]



[](#beta_memory_tool_20250818.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_memory_tool_20250818.strict)

[](#beta_memory_tool_20250818)



BetaToolComputerUse20250124 object { display_height_px, display_width_px, name, 7 more }



display_height_px: number



The height of the display in pixels.

[](#beta_tool_computer_use_20250124.display_height_px)

display_width_px: number



The width of the display in pixels.

[](#beta_tool_computer_use_20250124.display_width_px)



name: "computer"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_computer_use_20250124.name)

type: "computer_20250124"



[](#beta_tool_computer_use_20250124.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_computer_use_20250124.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_computer_use_20250124.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_computer_use_20250124.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_computer_use_20250124.allowed_callers.items%5B3%5D)

[](#beta_tool_computer_use_20250124.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_computer_use_20250124.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_computer_use_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_computer_use_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_computer_use_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_computer_use_20250124.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_computer_use_20250124.defer_loading)

display_number: optional number



The X11 display number (e.g. 0, 1) for the display.

[](#beta_tool_computer_use_20250124.display_number)

input_examples: optional array of map\[unknown\]



[](#beta_tool_computer_use_20250124.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_computer_use_20250124.strict)

[](#beta_tool_computer_use_20250124)



BetaToolTextEditor20241022 object { name, type, allowed_callers, 4 more }





name: "str_replace_editor"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_text_editor_20241022.name)

type: "text_editor_20241022"



[](#beta_tool_text_editor_20241022.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_text_editor_20241022.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_text_editor_20241022.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_text_editor_20241022.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_text_editor_20241022.allowed_callers.items%5B3%5D)

[](#beta_tool_text_editor_20241022.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_text_editor_20241022.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_text_editor_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_text_editor_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_text_editor_20241022.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_text_editor_20241022.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_text_editor_20241022.defer_loading)

input_examples: optional array of map\[unknown\]



[](#beta_tool_text_editor_20241022.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_text_editor_20241022.strict)

[](#beta_tool_text_editor_20241022)



BetaToolComputerUse20251124 object { display_height_px, display_width_px, name, 8 more }



display_height_px: number



The height of the display in pixels.

[](#beta_tool_computer_use_20251124.display_height_px)

display_width_px: number



The width of the display in pixels.

[](#beta_tool_computer_use_20251124.display_width_px)



name: "computer"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_computer_use_20251124.name)

type: "computer_20251124"



[](#beta_tool_computer_use_20251124.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_computer_use_20251124.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_computer_use_20251124.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_computer_use_20251124.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_computer_use_20251124.allowed_callers.items%5B3%5D)

[](#beta_tool_computer_use_20251124.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_computer_use_20251124.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_computer_use_20251124.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_computer_use_20251124.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_computer_use_20251124.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_computer_use_20251124.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_computer_use_20251124.defer_loading)

display_number: optional number



The X11 display number (e.g. 0, 1) for the display.

[](#beta_tool_computer_use_20251124.display_number)

enable_zoom: optional boolean



Whether to enable an action to take a zoomed-in screenshot of the screen.

[](#beta_tool_computer_use_20251124.enable_zoom)

input_examples: optional array of map\[unknown\]



[](#beta_tool_computer_use_20251124.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_computer_use_20251124.strict)

[](#beta_tool_computer_use_20251124)



BetaToolTextEditor20250124 object { name, type, allowed_callers, 4 more }





name: "str_replace_editor"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_text_editor_20250124.name)

type: "text_editor_20250124"



[](#beta_tool_text_editor_20250124.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_text_editor_20250124.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_text_editor_20250124.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_text_editor_20250124.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_text_editor_20250124.allowed_callers.items%5B3%5D)

[](#beta_tool_text_editor_20250124.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_text_editor_20250124.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_text_editor_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_text_editor_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_text_editor_20250124.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_text_editor_20250124.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_text_editor_20250124.defer_loading)

input_examples: optional array of map\[unknown\]



[](#beta_tool_text_editor_20250124.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_text_editor_20250124.strict)

[](#beta_tool_text_editor_20250124)



BetaToolTextEditor20250429 object { name, type, allowed_callers, 4 more }





name: "str_replace_based_edit_tool"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_text_editor_20250429.name)

type: "text_editor_20250429"



[](#beta_tool_text_editor_20250429.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_text_editor_20250429.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_text_editor_20250429.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_text_editor_20250429.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_text_editor_20250429.allowed_callers.items%5B3%5D)

[](#beta_tool_text_editor_20250429.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_text_editor_20250429.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_text_editor_20250429.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_text_editor_20250429.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_text_editor_20250429.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_text_editor_20250429.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_text_editor_20250429.defer_loading)

input_examples: optional array of map\[unknown\]



[](#beta_tool_text_editor_20250429.input_examples)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_text_editor_20250429.strict)

[](#beta_tool_text_editor_20250429)



BetaToolTextEditor20250728 object { name, type, allowed_callers, 5 more }





name: "str_replace_based_edit_tool"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_text_editor_20250728.name)

type: "text_editor_20250728"



[](#beta_tool_text_editor_20250728.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_text_editor_20250728.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_text_editor_20250728.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_text_editor_20250728.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_text_editor_20250728.allowed_callers.items%5B3%5D)

[](#beta_tool_text_editor_20250728.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_text_editor_20250728.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_text_editor_20250728.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_text_editor_20250728.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_text_editor_20250728.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_text_editor_20250728.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_text_editor_20250728.defer_loading)

input_examples: optional array of map\[unknown\]



[](#beta_tool_text_editor_20250728.input_examples)

max_characters: optional number



Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

[](#beta_tool_text_editor_20250728.max_characters)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_text_editor_20250728.strict)

[](#beta_tool_text_editor_20250728)



BetaWebSearchTool20250305 object { name, type, allowed_callers, 7 more }





name: "web_search"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_web_search_tool_20250305.name)

type: "web_search_20250305"



[](#beta_web_search_tool_20250305.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_web_search_tool_20250305.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_web_search_tool_20250305.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_web_search_tool_20250305.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_web_search_tool_20250305.allowed_callers.items%5B3%5D)

[](#beta_web_search_tool_20250305.allowed_callers)

allowed_domains: optional array of string



If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

[](#beta_web_search_tool_20250305.allowed_domains)

blocked_domains: optional array of string



If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[](#beta_web_search_tool_20250305.blocked_domains)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_search_tool_20250305.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_search_tool_20250305.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_search_tool_20250305.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_search_tool_20250305.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_search_tool_20250305.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_web_search_tool_20250305.defer_loading)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#beta_web_search_tool_20250305.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_web_search_tool_20250305.strict)



user_location: optional [BetaUserLocation](/docs/en/api/beta/messages#beta_user_location) { type, city, country, 2 more }



Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"



[](#beta_web_search_tool_20250305.user_location%20%2B%20(resource)%20beta.messages.type)

city: optional string



The city of the user.

[](#beta_web_search_tool_20250305.user_location%20%2B%20(resource)%20beta.messages.city)

country: optional string



The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

[](#beta_web_search_tool_20250305.user_location%20%2B%20(resource)%20beta.messages.country)

region: optional string



The region of the user.

[](#beta_web_search_tool_20250305.user_location%20%2B%20(resource)%20beta.messages.region)

timezone: optional string



The [IANA timezone](https://nodatime.org/TimeZones) of the user.

[](#beta_web_search_tool_20250305.user_location%20%2B%20(resource)%20beta.messages.timezone)

[](#beta_web_search_tool_20250305.user_location)

[](#beta_web_search_tool_20250305)



BetaWebFetchTool20250910 object { name, type, allowed_callers, 8 more }





name: "web_fetch"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_web_fetch_tool_20250910.name)

type: "web_fetch_20250910"



[](#beta_web_fetch_tool_20250910.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_web_fetch_tool_20250910.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_web_fetch_tool_20250910.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_web_fetch_tool_20250910.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_web_fetch_tool_20250910.allowed_callers.items%5B3%5D)

[](#beta_web_fetch_tool_20250910.allowed_callers)

allowed_domains: optional array of string



List of domains to allow fetching from

[](#beta_web_fetch_tool_20250910.allowed_domains)

blocked_domains: optional array of string



List of domains to block fetching from

[](#beta_web_fetch_tool_20250910.blocked_domains)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_fetch_tool_20250910.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_fetch_tool_20250910.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_fetch_tool_20250910.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_fetch_tool_20250910.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_fetch_tool_20250910.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean



[](#beta_web_fetch_tool_20250910.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_web_fetch_tool_20250910.citations)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_web_fetch_tool_20250910.defer_loading)

max_content_tokens: optional number



Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

[](#beta_web_fetch_tool_20250910.max_content_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#beta_web_fetch_tool_20250910.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_web_fetch_tool_20250910.strict)

[](#beta_web_fetch_tool_20250910)



BetaWebSearchTool20260209 object { name, type, allowed_callers, 7 more }





name: "web_search"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_web_search_tool_20260209.name)

type: "web_search_20260209"



[](#beta_web_search_tool_20260209.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_web_search_tool_20260209.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_web_search_tool_20260209.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_web_search_tool_20260209.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_web_search_tool_20260209.allowed_callers.items%5B3%5D)

[](#beta_web_search_tool_20260209.allowed_callers)

allowed_domains: optional array of string



If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

[](#beta_web_search_tool_20260209.allowed_domains)

blocked_domains: optional array of string



If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[](#beta_web_search_tool_20260209.blocked_domains)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_search_tool_20260209.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_search_tool_20260209.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_search_tool_20260209.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_search_tool_20260209.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_search_tool_20260209.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_web_search_tool_20260209.defer_loading)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#beta_web_search_tool_20260209.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_web_search_tool_20260209.strict)



user_location: optional [BetaUserLocation](/docs/en/api/beta/messages#beta_user_location) { type, city, country, 2 more }



Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"



[](#beta_web_search_tool_20260209.user_location%20%2B%20(resource)%20beta.messages.type)

city: optional string



The city of the user.

[](#beta_web_search_tool_20260209.user_location%20%2B%20(resource)%20beta.messages.city)

country: optional string



The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

[](#beta_web_search_tool_20260209.user_location%20%2B%20(resource)%20beta.messages.country)

region: optional string



The region of the user.

[](#beta_web_search_tool_20260209.user_location%20%2B%20(resource)%20beta.messages.region)

timezone: optional string



The [IANA timezone](https://nodatime.org/TimeZones) of the user.

[](#beta_web_search_tool_20260209.user_location%20%2B%20(resource)%20beta.messages.timezone)

[](#beta_web_search_tool_20260209.user_location)

[](#beta_web_search_tool_20260209)



BetaWebFetchTool20260209 object { name, type, allowed_callers, 8 more }





name: "web_fetch"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_web_fetch_tool_20260209.name)

type: "web_fetch_20260209"



[](#beta_web_fetch_tool_20260209.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_web_fetch_tool_20260209.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_web_fetch_tool_20260209.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_web_fetch_tool_20260209.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_web_fetch_tool_20260209.allowed_callers.items%5B3%5D)

[](#beta_web_fetch_tool_20260209.allowed_callers)

allowed_domains: optional array of string



List of domains to allow fetching from

[](#beta_web_fetch_tool_20260209.allowed_domains)

blocked_domains: optional array of string



List of domains to block fetching from

[](#beta_web_fetch_tool_20260209.blocked_domains)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_fetch_tool_20260209.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_fetch_tool_20260209.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_fetch_tool_20260209.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_fetch_tool_20260209.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_fetch_tool_20260209.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean



[](#beta_web_fetch_tool_20260209.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_web_fetch_tool_20260209.citations)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_web_fetch_tool_20260209.defer_loading)

max_content_tokens: optional number



Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

[](#beta_web_fetch_tool_20260209.max_content_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#beta_web_fetch_tool_20260209.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_web_fetch_tool_20260209.strict)

[](#beta_web_fetch_tool_20260209)



BetaWebFetchTool20260309 object { name, type, allowed_callers, 9 more }



Web fetch tool with use_cache parameter for bypassing cached content.



name: "web_fetch"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_web_fetch_tool_20260309.name)

type: "web_fetch_20260309"



[](#beta_web_fetch_tool_20260309.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_web_fetch_tool_20260309.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_web_fetch_tool_20260309.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_web_fetch_tool_20260309.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_web_fetch_tool_20260309.allowed_callers.items%5B3%5D)

[](#beta_web_fetch_tool_20260309.allowed_callers)

allowed_domains: optional array of string



List of domains to allow fetching from

[](#beta_web_fetch_tool_20260309.allowed_domains)

blocked_domains: optional array of string



List of domains to block fetching from

[](#beta_web_fetch_tool_20260309.blocked_domains)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_fetch_tool_20260309.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_fetch_tool_20260309.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_fetch_tool_20260309.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_fetch_tool_20260309.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_fetch_tool_20260309.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean



[](#beta_web_fetch_tool_20260309.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_web_fetch_tool_20260309.citations)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_web_fetch_tool_20260309.defer_loading)

max_content_tokens: optional number



Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

[](#beta_web_fetch_tool_20260309.max_content_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#beta_web_fetch_tool_20260309.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_web_fetch_tool_20260309.strict)

use_cache: optional boolean



Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[](#beta_web_fetch_tool_20260309.use_cache)

[](#beta_web_fetch_tool_20260309)



BetaWebSearchTool20260318 object { name, type, allowed_callers, 8 more }





name: "web_search"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_web_search_tool_20260318.name)

type: "web_search_20260318"



[](#beta_web_search_tool_20260318.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_web_search_tool_20260318.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_web_search_tool_20260318.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_web_search_tool_20260318.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_web_search_tool_20260318.allowed_callers.items%5B3%5D)

[](#beta_web_search_tool_20260318.allowed_callers)

allowed_domains: optional array of string



If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

[](#beta_web_search_tool_20260318.allowed_domains)

blocked_domains: optional array of string



If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[](#beta_web_search_tool_20260318.blocked_domains)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_search_tool_20260318.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_search_tool_20260318.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_search_tool_20260318.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_search_tool_20260318.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_search_tool_20260318.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_web_search_tool_20260318.defer_loading)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#beta_web_search_tool_20260318.max_uses)



response_inclusion: optional "full" or "excluded"



How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"



[](#beta_web_search_tool_20260318.response_inclusion%5B0%5D)

"excluded"



[](#beta_web_search_tool_20260318.response_inclusion%5B1%5D)

[](#beta_web_search_tool_20260318.response_inclusion)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_web_search_tool_20260318.strict)



user_location: optional [BetaUserLocation](/docs/en/api/beta/messages#beta_user_location) { type, city, country, 2 more }



Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"



[](#beta_web_search_tool_20260318.user_location%20%2B%20(resource)%20beta.messages.type)

city: optional string



The city of the user.

[](#beta_web_search_tool_20260318.user_location%20%2B%20(resource)%20beta.messages.city)

country: optional string



The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

[](#beta_web_search_tool_20260318.user_location%20%2B%20(resource)%20beta.messages.country)

region: optional string



The region of the user.

[](#beta_web_search_tool_20260318.user_location%20%2B%20(resource)%20beta.messages.region)

timezone: optional string



The [IANA timezone](https://nodatime.org/TimeZones) of the user.

[](#beta_web_search_tool_20260318.user_location%20%2B%20(resource)%20beta.messages.timezone)

[](#beta_web_search_tool_20260318.user_location)

[](#beta_web_search_tool_20260318)



BetaWebFetchTool20260318 object { name, type, allowed_callers, 10 more }





name: "web_fetch"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_web_fetch_tool_20260318.name)

type: "web_fetch_20260318"



[](#beta_web_fetch_tool_20260318.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_web_fetch_tool_20260318.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_web_fetch_tool_20260318.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_web_fetch_tool_20260318.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_web_fetch_tool_20260318.allowed_callers.items%5B3%5D)

[](#beta_web_fetch_tool_20260318.allowed_callers)

allowed_domains: optional array of string



List of domains to allow fetching from

[](#beta_web_fetch_tool_20260318.allowed_domains)

blocked_domains: optional array of string



List of domains to block fetching from

[](#beta_web_fetch_tool_20260318.blocked_domains)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_web_fetch_tool_20260318.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_web_fetch_tool_20260318.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_web_fetch_tool_20260318.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_web_fetch_tool_20260318.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_web_fetch_tool_20260318.cache_control)



citations: optional [BetaCitationsConfigParam](/docs/en/api/beta/messages#beta_citations_config_param) { enabled }



Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean



[](#beta_web_fetch_tool_20260318.citations%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_web_fetch_tool_20260318.citations)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_web_fetch_tool_20260318.defer_loading)

max_content_tokens: optional number



Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

[](#beta_web_fetch_tool_20260318.max_content_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#beta_web_fetch_tool_20260318.max_uses)



response_inclusion: optional "full" or "excluded"



How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"



[](#beta_web_fetch_tool_20260318.response_inclusion%5B0%5D)

"excluded"



[](#beta_web_fetch_tool_20260318.response_inclusion%5B1%5D)

[](#beta_web_fetch_tool_20260318.response_inclusion)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_web_fetch_tool_20260318.strict)

use_cache: optional boolean



Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[](#beta_web_fetch_tool_20260318.use_cache)

[](#beta_web_fetch_tool_20260318)



BetaAdvisorTool20260301 object { model, name, type, 7 more }



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

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#beta_advisor_tool_20260301.model%20%2B%20(resource)%20messages%5B1%5D)

[](#beta_advisor_tool_20260301.model)



name: "advisor"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_advisor_tool_20260301.name)

type: "advisor_20260301"



[](#beta_advisor_tool_20260301.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_advisor_tool_20260301.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_advisor_tool_20260301.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_advisor_tool_20260301.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_advisor_tool_20260301.allowed_callers.items%5B3%5D)

[](#beta_advisor_tool_20260301.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_advisor_tool_20260301.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_advisor_tool_20260301.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_advisor_tool_20260301.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_advisor_tool_20260301.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_advisor_tool_20260301.cache_control)



caching: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: "ephemeral"



[](#beta_advisor_tool_20260301.caching%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_advisor_tool_20260301.caching%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_advisor_tool_20260301.caching%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_advisor_tool_20260301.caching%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_advisor_tool_20260301.caching)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_advisor_tool_20260301.defer_loading)

max_tokens: optional number



Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

[](#beta_advisor_tool_20260301.max_tokens)

max_uses: optional number



Maximum number of times the tool can be used in the API request.

[](#beta_advisor_tool_20260301.max_uses)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_advisor_tool_20260301.strict)

[](#beta_advisor_tool_20260301)



BetaToolSearchToolBm25_20251119 object { name, type, allowed_callers, 3 more }





name: "tool_search_tool_bm25"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_search_tool_bm25_20251119.name)



type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"



One of the following:

"tool_search_tool_bm25_20251119"



[](#beta_tool_search_tool_bm25_20251119.type%5B0%5D)

"tool_search_tool_bm25"



[](#beta_tool_search_tool_bm25_20251119.type%5B1%5D)

[](#beta_tool_search_tool_bm25_20251119.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_search_tool_bm25_20251119.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_search_tool_bm25_20251119.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_search_tool_bm25_20251119.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_search_tool_bm25_20251119.allowed_callers.items%5B3%5D)

[](#beta_tool_search_tool_bm25_20251119.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_search_tool_bm25_20251119.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_search_tool_bm25_20251119.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_search_tool_bm25_20251119.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_search_tool_bm25_20251119.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_search_tool_bm25_20251119.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_search_tool_bm25_20251119.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_search_tool_bm25_20251119.strict)

[](#beta_tool_search_tool_bm25_20251119)



BetaToolSearchToolRegex20251119 object { name, type, allowed_callers, 3 more }





name: "tool_search_tool_regex"



Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

[](#beta_tool_search_tool_regex_20251119.name)



type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"



One of the following:

"tool_search_tool_regex_20251119"



[](#beta_tool_search_tool_regex_20251119.type%5B0%5D)

"tool_search_tool_regex"



[](#beta_tool_search_tool_regex_20251119.type%5B1%5D)

[](#beta_tool_search_tool_regex_20251119.type)



allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"



One of the following:

"direct"



[](#beta_tool_search_tool_regex_20251119.allowed_callers.items%5B0%5D)

"code_execution_20250825"



[](#beta_tool_search_tool_regex_20251119.allowed_callers.items%5B1%5D)

"code_execution_20260120"



[](#beta_tool_search_tool_regex_20251119.allowed_callers.items%5B2%5D)

"code_execution_20260521"



[](#beta_tool_search_tool_regex_20251119.allowed_callers.items%5B3%5D)

[](#beta_tool_search_tool_regex_20251119.allowed_callers)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_tool_search_tool_regex_20251119.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_tool_search_tool_regex_20251119.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_tool_search_tool_regex_20251119.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_tool_search_tool_regex_20251119.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_tool_search_tool_regex_20251119.cache_control)

defer_loading: optional boolean



If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

[](#beta_tool_search_tool_regex_20251119.defer_loading)

strict: optional boolean



When true, guarantees schema validation on tool names and inputs

[](#beta_tool_search_tool_regex_20251119.strict)

[](#beta_tool_search_tool_regex_20251119)



BetaMCPToolset object { mcp_server_name, type, cache_control, 2 more }



Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: string



Name of the MCP server to configure tools for

[](#beta_mcp_toolset.mcp_server_name)

type: "mcp_toolset"



[](#beta_mcp_toolset.type)



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/beta/messages#beta_cache_control_ephemeral) { type, ttl }



Create a cache control breakpoint at this content block.

type: "ephemeral"



[](#beta_mcp_toolset.cache_control%20%2B%20(resource)%20beta.messages.type)

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

[](#beta_mcp_toolset.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B0%5D)

"1h"



[](#beta_mcp_toolset.cache_control%20%2B%20(resource)%20beta.messages.ttl%5B1%5D)

[](#beta_mcp_toolset.cache_control%20%2B%20(resource)%20beta.messages.ttl)

[](#beta_mcp_toolset.cache_control)



configs: optional map\[[BetaMCPToolConfig](/docs/en/api/beta/messages#beta_mcp_tool_config) { defer_loading, enabled } \]



Configuration overrides for specific tools, keyed by tool name

defer_loading: optional boolean



[](#beta_mcp_tool_config.defer_loading)

enabled: optional boolean



[](#beta_mcp_tool_config.enabled)

[](#beta_mcp_toolset.configs)



default_config: optional [BetaMCPToolDefaultConfig](/docs/en/api/beta/messages#beta_mcp_tool_default_config) { defer_loading, enabled }



Default configuration applied to all tools from this server

defer_loading: optional boolean



[](#beta_mcp_toolset.default_config%20%2B%20(resource)%20beta.messages.defer_loading)

enabled: optional boolean



[](#beta_mcp_toolset.default_config%20%2B%20(resource)%20beta.messages.enabled)

[](#beta_mcp_toolset.default_config)

[](#beta_mcp_toolset)

[](#create.requests.items.params.tools)



output_format: optional [BetaJSONOutputFormat](/docs/en/api/beta/messages#beta_json_output_format) { schema, type } ⁠Deprecated



Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

schema: map\[unknown\]



The JSON schema of the format

[](#create.requests.items.params.output_format%20%2B%20(resource)%20beta.messages.schema)

type: "json_schema"



[](#create.requests.items.params.output_format%20%2B%20(resource)%20beta.messages.type)

[](#create.requests.items.params.output_format)



temperature: optional number⁠Deprecated



Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

[](#create.requests.items.params.temperature)



top_k: optional number⁠Deprecated



Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0

[](#create.requests.items.params.top_k)



top_p: optional number⁠Deprecated



Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value \>= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

[](#create.requests.items.params.top_p)

[](#create.requests.items.params)

[](#create.requests)

##### ReturnsExpand Collapse 



BetaMessageBatch object { id, archived_at, cancel_initiated_at, 7 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#beta_message_batch.id)

archived_at: string



RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

[](#beta_message_batch.archived_at)

cancel_initiated_at: string



RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

[](#beta_message_batch.cancel_initiated_at)

created_at: string



RFC 3339 datetime string representing the time at which the Message Batch was created.

[](#beta_message_batch.created_at)



ended_at: string



RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

[](#beta_message_batch.ended_at)

expires_at: string



RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

[](#beta_message_batch.expires_at)



processing_status: "in_progress" or "canceling" or "ended"



Processing status of the Message Batch.

One of the following:

"in_progress"



[](#beta_message_batch.processing_status%5B0%5D)

"canceling"



[](#beta_message_batch.processing_status%5B1%5D)

"ended"



[](#beta_message_batch.processing_status%5B2%5D)

[](#beta_message_batch.processing_status)



request_counts: [BetaMessageBatchRequestCounts](/docs/en/api/beta/messages/batches#beta_message_batch_request_counts) { canceled, errored, expired, 2 more }



Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: number



Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

[](#beta_message_batch.request_counts%20%2B%20(resource)%20beta.messages.batches.canceled)



errored: number



Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

[](#beta_message_batch.request_counts%20%2B%20(resource)%20beta.messages.batches.errored)



expired: number



Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

[](#beta_message_batch.request_counts%20%2B%20(resource)%20beta.messages.batches.expired)

processing: number



Number of requests in the Message Batch that are processing.

[](#beta_message_batch.request_counts%20%2B%20(resource)%20beta.messages.batches.processing)



succeeded: number



Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

[](#beta_message_batch.request_counts%20%2B%20(resource)%20beta.messages.batches.succeeded)

[](#beta_message_batch.request_counts)



results_url: string



URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

[](#beta_message_batch.results_url)



type: "message_batch"



Object type.

For Message Batches, this is always `"message_batch"`.

[](#beta_message_batch.type)

[](#beta_message_batch)

Create a Message Batch

cURL



```python
curl https://api.anthropic.com/v1/messages/batches \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: message-batches-2024-09-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "requests": [
            {
              "custom_id": "my-custom-id-1",
              "params": {
                "max_tokens": 1024,
                "messages": [
                  {
                    "content": "Hello, world",
                    "role": "user"
                  }
                ],
                "model": "claude-opus-4-6"
              }
            }
          ]
        }'
```

Response 200



```python
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
