---
title: "Batches - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/messages/batches"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:41Z"
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

Batches




cURL



A beta version of this API exists and may have additional functionality. [View the beta version](/docs/en/api/beta/messages/batches).

# Batches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 



DeletedMessageBatch object { id, type }



id: string



ID of the Message Batch.

[](#deleted_message_batch.id)



type: "message_batch_deleted"



Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

[](#deleted_message_batch.type)

[](#deleted_message_batch)



MessageBatch object { id, archived_at, cancel_initiated_at, 7 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#message_batch.id)

archived_at: string



RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

[](#message_batch.archived_at)

cancel_initiated_at: string



RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

[](#message_batch.cancel_initiated_at)

created_at: string



RFC 3339 datetime string representing the time at which the Message Batch was created.

[](#message_batch.created_at)



ended_at: string



RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

[](#message_batch.ended_at)

expires_at: string



RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

[](#message_batch.expires_at)



processing_status: "in_progress" or "canceling" or "ended"



Processing status of the Message Batch.

One of the following:

"in_progress"



[](#message_batch.processing_status%5B0%5D)

"canceling"



[](#message_batch.processing_status%5B1%5D)

"ended"



[](#message_batch.processing_status%5B2%5D)

[](#message_batch.processing_status)



request_counts: [MessageBatchRequestCounts](/docs/en/api/messages/batches#message_batch_request_counts) { canceled, errored, expired, 2 more }



Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: number



Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

[](#message_batch.request_counts%20%2B%20(resource)%20messages.batches.canceled)



errored: number



Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

[](#message_batch.request_counts%20%2B%20(resource)%20messages.batches.errored)



expired: number



Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

[](#message_batch.request_counts%20%2B%20(resource)%20messages.batches.expired)

processing: number



Number of requests in the Message Batch that are processing.

[](#message_batch.request_counts%20%2B%20(resource)%20messages.batches.processing)



succeeded: number



Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

[](#message_batch.request_counts%20%2B%20(resource)%20messages.batches.succeeded)

[](#message_batch.request_counts)



results_url: string



URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

[](#message_batch.results_url)



type: "message_batch"



Object type.

For Message Batches, this is always `"message_batch"`.

[](#message_batch.type)

[](#message_batch)



MessageBatchCanceledResult object { type }



type: "canceled"



[](#message_batch_canceled_result.type)

[](#message_batch_canceled_result)



MessageBatchErroredResult object { error, type }





error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }





error: [ErrorObject](/docs/en/api/$shared#error_object)



One of the following:



InvalidRequestError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "invalid_request_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



AuthenticationError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "authentication_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



BillingError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "billing_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



PermissionError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "permission_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



NotFoundError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "not_found_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



RateLimitError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "rate_limit_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



GatewayTimeoutError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "timeout_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



APIErrorObject object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "api_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



OverloadedError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "overloaded_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)

[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.error)

request_id: string



[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.request_id)

type: "error"



[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.type)

[](#message_batch_errored_result.error)

type: "errored"



[](#message_batch_errored_result.type)

[](#message_batch_errored_result)



MessageBatchExpiredResult object { type }



type: "expired"



[](#message_batch_expired_result.type)

[](#message_batch_expired_result)



MessageBatchIndividualResponse object { custom_id, result }



This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom_id: string



Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[](#message_batch_individual_response.custom_id)



result: [MessageBatchResult](/docs/en/api/messages/batches#message_batch_result)



Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchSucceededResult object { message, type }





message: [Message](/docs/en/api/messages#message) { id, container, content, 7 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.container)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)

end_char_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_char_index)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_char_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_char_index)

type: "char_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationPageLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)

end_page_number: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_page_number)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_page_number: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_page_number)

type: "page_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_block_index)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_block_index)

type: "content_block_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

encrypted_index: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.encrypted_index)

title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.title)

type: "web_search_result_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

url: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.url)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.search_result_index)

source: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_block_index)

title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.title)

type: "search_result_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.citations)

text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.text)

type: "text"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ThinkingBlock object { signature, thinking, type }



signature: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.signature)

thinking: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.thinking)

type: "thinking"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



RedactedThinkingBlock object { data, type }



data: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.data)

type: "redacted_thinking"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ToolUseBlock object { id, caller, input, 2 more }



id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

input: map\[unknown\]



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.input)

name: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name)

type: "tool_use"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolUseBlock object { id, caller, input, 2 more }



id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

input: map\[unknown\]



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.input)



name: "web_search" or "web_fetch" or "code_execution" or 4 more



One of the following:

"web_search"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B0%5D)

"web_fetch"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B1%5D)

"code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B2%5D)

"bash_code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B3%5D)

"text_editor_code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B4%5D)

"tool_search_tool_regex"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B5%5D)

"tool_search_tool_bm25"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B6%5D)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name)

type: "server_tool_use"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "web_search_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

type: "web_fetch_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

retrieved_at: string



ISO 8601 timestamp when the content was retrieved

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.retrieved_at)

type: "web_fetch_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

url: string



Fetched content URL

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.url)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "web_fetch_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

type: "bash_code_execution_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type }



file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

type: "bash_code_execution_output"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

return_code: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stderr)

stdout: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stdout)

type: "bash_code_execution_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "bash_code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

error_message: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_message)

type: "text_editor_code_execution_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more }



content: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)



file_type: "text" or "image" or "pdf"



One of the following:

"text"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B0%5D)

"image"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B1%5D)

"pdf"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B2%5D)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type)

num_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.num_lines)

start_line: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_line)

total_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.total_lines)

type: "text_editor_code_execution_view_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionCreateResultBlock object { is_file_update, type }



is_file_update: boolean



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.is_file_update)

type: "text_editor_code_execution_create_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more }



lines: array of string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.lines)

new_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.new_lines)

new_start: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.new_start)

old_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.old_lines)

old_start: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.old_start)

type: "text_editor_code_execution_str_replace_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "text_editor_code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

error_message: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_message)

type: "tool_search_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ToolSearchToolSearchResultBlock object { tool_references, type }





tool_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type }



tool_name: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_name)

type: "tool_reference"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_references)

type: "tool_search_tool_search_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "tool_search_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ContainerUploadBlock object { file_id, type }



Response model for a file uploaded to the container.

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

type: "container_upload"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.model)



role: "assistant"



Conversational role of the generated message.

This will always be `"assistant"`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.role)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_details)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_reason)



stop_sequence: string



Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_sequence)



type: "message"



Object type.

For Messages, this is always `"message"`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.usage)

[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches.message)

type: "succeeded"



[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches.type)

[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches)



MessageBatchErroredResult object { error, type }





error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }





error: [ErrorObject](/docs/en/api/$shared#error_object)



One of the following:



InvalidRequestError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "invalid_request_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



AuthenticationError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "authentication_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



BillingError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "billing_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



PermissionError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "permission_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



NotFoundError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "not_found_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



RateLimitError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "rate_limit_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



GatewayTimeoutError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "timeout_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



APIErrorObject object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "api_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



OverloadedError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "overloaded_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)

[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.error)

request_id: string



[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.request_id)

type: "error"



[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.type)

[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches.error)

type: "errored"



[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches.type)

[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches)



MessageBatchCanceledResult object { type }



type: "canceled"



[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches.type)

[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches)



MessageBatchExpiredResult object { type }



type: "expired"



[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches.type)

[](#message_batch_individual_response.result%20%2B%20(resource)%20messages.batches)

[](#message_batch_individual_response.result)

[](#message_batch_individual_response)



MessageBatchRequestCounts object { canceled, errored, expired, 2 more }





canceled: number



Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

[](#message_batch_request_counts.canceled)



errored: number



Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

[](#message_batch_request_counts.errored)



expired: number



Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

[](#message_batch_request_counts.expired)

processing: number



Number of requests in the Message Batch that are processing.

[](#message_batch_request_counts.processing)



succeeded: number



Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

[](#message_batch_request_counts.succeeded)

[](#message_batch_request_counts)



MessageBatchResult = [MessageBatchSucceededResult](/docs/en/api/messages/batches#message_batch_succeeded_result) { message, type } or [MessageBatchErroredResult](/docs/en/api/messages/batches#message_batch_errored_result) { error, type } or [MessageBatchCanceledResult](/docs/en/api/messages/batches#message_batch_canceled_result) { type } or [MessageBatchExpiredResult](/docs/en/api/messages/batches#message_batch_expired_result) { type }



Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchSucceededResult object { message, type }





message: [Message](/docs/en/api/messages#message) { id, container, content, 7 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.container)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)

end_char_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_char_index)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_char_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_char_index)

type: "char_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationPageLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)

end_page_number: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_page_number)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_page_number: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_page_number)

type: "page_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_block_index)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_block_index)

type: "content_block_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

encrypted_index: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.encrypted_index)

title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.title)

type: "web_search_result_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

url: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.url)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.search_result_index)

source: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_block_index)

title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.title)

type: "search_result_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.citations)

text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.text)

type: "text"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ThinkingBlock object { signature, thinking, type }



signature: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.signature)

thinking: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.thinking)

type: "thinking"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



RedactedThinkingBlock object { data, type }



data: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.data)

type: "redacted_thinking"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ToolUseBlock object { id, caller, input, 2 more }



id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

input: map\[unknown\]



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.input)

name: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name)

type: "tool_use"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolUseBlock object { id, caller, input, 2 more }



id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

input: map\[unknown\]



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.input)



name: "web_search" or "web_fetch" or "code_execution" or 4 more



One of the following:

"web_search"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B0%5D)

"web_fetch"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B1%5D)

"code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B2%5D)

"bash_code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B3%5D)

"text_editor_code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B4%5D)

"tool_search_tool_regex"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B5%5D)

"tool_search_tool_bm25"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B6%5D)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name)

type: "server_tool_use"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "web_search_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

type: "web_fetch_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

retrieved_at: string



ISO 8601 timestamp when the content was retrieved

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.retrieved_at)

type: "web_fetch_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

url: string



Fetched content URL

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.url)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "web_fetch_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

type: "bash_code_execution_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type }



file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

type: "bash_code_execution_output"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

return_code: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stderr)

stdout: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stdout)

type: "bash_code_execution_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "bash_code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

error_message: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_message)

type: "text_editor_code_execution_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more }



content: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)



file_type: "text" or "image" or "pdf"



One of the following:

"text"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B0%5D)

"image"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B1%5D)

"pdf"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B2%5D)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type)

num_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.num_lines)

start_line: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_line)

total_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.total_lines)

type: "text_editor_code_execution_view_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionCreateResultBlock object { is_file_update, type }



is_file_update: boolean



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.is_file_update)

type: "text_editor_code_execution_create_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more }



lines: array of string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.lines)

new_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.new_lines)

new_start: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.new_start)

old_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.old_lines)

old_start: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.old_start)

type: "text_editor_code_execution_str_replace_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "text_editor_code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

error_message: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_message)

type: "tool_search_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ToolSearchToolSearchResultBlock object { tool_references, type }





tool_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type }



tool_name: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_name)

type: "tool_reference"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_references)

type: "tool_search_tool_search_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "tool_search_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ContainerUploadBlock object { file_id, type }



Response model for a file uploaded to the container.

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

type: "container_upload"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.model)



role: "assistant"



Conversational role of the generated message.

This will always be `"assistant"`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.role)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_details)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_reason)



stop_sequence: string



Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_sequence)



type: "message"



Object type.

For Messages, this is always `"message"`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.usage)

[](#message_batch_succeeded_result.message)

type: "succeeded"



[](#message_batch_succeeded_result.type)

[](#message_batch_succeeded_result)



MessageBatchErroredResult object { error, type }





error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }





error: [ErrorObject](/docs/en/api/$shared#error_object)



One of the following:



InvalidRequestError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "invalid_request_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



AuthenticationError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "authentication_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



BillingError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "billing_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



PermissionError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "permission_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



NotFoundError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "not_found_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



RateLimitError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "rate_limit_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



GatewayTimeoutError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "timeout_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



APIErrorObject object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "api_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)



OverloadedError object { message, type }



message: string



[](#error_response.error%20%2B%20(resource)%20%24shared.message)

type: "overloaded_error"



[](#error_response.error%20%2B%20(resource)%20%24shared.type)

[](#error_response.error%20%2B%20(resource)%20%24shared)

[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.error)

request_id: string



[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.request_id)

type: "error"



[](#message_batch_errored_result.error%20%2B%20(resource)%20%24shared.type)

[](#message_batch_errored_result.error)

type: "errored"



[](#message_batch_errored_result.type)

[](#message_batch_errored_result)



MessageBatchCanceledResult object { type }



type: "canceled"



[](#message_batch_canceled_result.type)

[](#message_batch_canceled_result)



MessageBatchExpiredResult object { type }



type: "expired"



[](#message_batch_expired_result.type)

[](#message_batch_expired_result)

[](#message_batch_result)



MessageBatchSucceededResult object { message, type }





message: [Message](/docs/en/api/messages#message) { id, container, content, 7 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.container)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)

end_char_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_char_index)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_char_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_char_index)

type: "char_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationPageLocation object { cited_text, document_index, document_title, 4 more }



cited_text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)

end_page_number: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_page_number)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_page_number: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_page_number)

type: "page_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

document_index: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_index)

document_title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.document_title)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_block_index)

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_block_index)

type: "content_block_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more }



cited_text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)

encrypted_index: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.encrypted_index)

title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.title)

type: "web_search_result_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

url: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.url)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more }





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.cited_text)



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.end_block_index)



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.search_result_index)

source: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.source)

start_block_index: number



0-based index of the first cited block in the source's `content` array.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_block_index)

title: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.title)

type: "search_result_location"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.citations)

text: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.text)

type: "text"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ThinkingBlock object { signature, thinking, type }



signature: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.signature)

thinking: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.thinking)

type: "thinking"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



RedactedThinkingBlock object { data, type }



data: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.data)

type: "redacted_thinking"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ToolUseBlock object { id, caller, input, 2 more }



id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

input: map\[unknown\]



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.input)

name: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name)

type: "tool_use"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolUseBlock object { id, caller, input, 2 more }



id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.id)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

input: map\[unknown\]



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.input)



name: "web_search" or "web_fetch" or "code_execution" or 4 more



One of the following:

"web_search"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B0%5D)

"web_fetch"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B1%5D)

"code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B2%5D)

"bash_code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B3%5D)

"text_editor_code_execution"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B4%5D)

"tool_search_tool_regex"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B5%5D)

"tool_search_tool_bm25"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name%5B6%5D)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.name)

type: "server_tool_use"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "web_search_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller object { tool_id, type }



Tool invocation generated by a server-side tool.

tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20250825"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ServerToolCaller20260120 object { tool_id, type }



tool_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_id)

type: "code_execution_20260120"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.caller)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

type: "web_fetch_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

retrieved_at: string



ISO 8601 timestamp when the content was retrieved

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.retrieved_at)

type: "web_fetch_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

url: string



Fetched content URL

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.url)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "web_fetch_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

type: "bash_code_execution_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more }





content: array of [BashCodeExecutionOutputBlock](/docs/en/api/messages#bash_code_execution_output_block) { file_id, type }



file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

type: "bash_code_execution_output"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

return_code: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.return_code)

stderr: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stderr)

stdout: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stdout)

type: "bash_code_execution_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "bash_code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

error_message: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_message)

type: "text_editor_code_execution_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more }



content: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)



file_type: "text" or "image" or "pdf"



One of the following:

"text"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B0%5D)

"image"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B1%5D)

"pdf"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type%5B2%5D)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_type)

num_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.num_lines)

start_line: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.start_line)

total_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.total_lines)

type: "text_editor_code_execution_view_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionCreateResultBlock object { is_file_update, type }



is_file_update: boolean



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.is_file_update)

type: "text_editor_code_execution_create_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more }



lines: array of string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.lines)

new_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.new_lines)

new_start: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.new_start)

old_lines: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.old_lines)

old_start: number



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.old_start)

type: "text_editor_code_execution_str_replace_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "text_editor_code_execution_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_code)

error_message: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.error_message)

type: "tool_search_tool_result_error"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ToolSearchToolSearchResultBlock object { tool_references, type }





tool_references: array of [ToolReferenceBlock](/docs/en/api/messages#tool_reference_block) { tool_name, type }



tool_name: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_name)

type: "tool_reference"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_references)

type: "tool_search_tool_search_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

tool_use_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.tool_use_id)

type: "tool_search_tool_result"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)



ContainerUploadBlock object { file_id, type }



Response model for a file uploaded to the container.

file_id: string



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.file_id)

type: "container_upload"



[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages)

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.content)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.model)



role: "assistant"



Conversational role of the generated message.

This will always be `"assistant"`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.role)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_details)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_reason)



stop_sequence: string



Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.stop_sequence)



type: "message"



Object type.

For Messages, this is always `"message"`.

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.type)

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

[](#message_batch_succeeded_result.message%20%2B%20(resource)%20messages.usage)

[](#message_batch_succeeded_result.message)

type: "succeeded"



[](#message_batch_succeeded_result.type)

[](#message_batch_succeeded_result)
