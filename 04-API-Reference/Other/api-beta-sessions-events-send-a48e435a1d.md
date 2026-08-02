---
title: "Send Events - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/events/send"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:51Z"
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


Create Session


List Sessions


Get Session


Update Session


Delete Session


Archive Session

Events


List Events


Send Events


Stream Events

Resources

Threads

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

Send




cURL

# Send Events

POST/v1/sessions/{session_id}/events

Send Events

##### Path ParametersExpand Collapse 

session_id: string



[](#send.session_id)

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

[](#send.betas)

##### Body ParametersJSONExpand Collapse 



events: array of [BetaManagedAgentsEventParams](/docs/en/api/beta/sessions/events#beta_managed_agents_event_params)



Events to send to the `session`.

One of the following:



BetaManagedAgentsUserMessageEventParams object { content, type }



Parameters for sending a user message to the session.



content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type } or [BetaManagedAgentsImageBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_image_block) { source, type } or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_document_block) { source, type, context, title }



Array of content blocks for the user message.

One of the following:



BetaManagedAgentsTextBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_text_block.text)

type: "text"



[](#beta_managed_agents_text_block.type)

[](#beta_managed_agents_text_block)



BetaManagedAgentsImageBlock object { source, type }



Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_image_source) { data, media_type, type } or [BetaManagedAgentsURLImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_image_source) { type, url } or [BetaManagedAgentsFileImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_image_source) { file_id, type }



Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media_type, type }



Base64-encoded image data.

data: string



Base64-encoded image data.

[](#beta_managed_agents_base64_image_source.data)

media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

[](#beta_managed_agents_base64_image_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_image_source.type)

[](#beta_managed_agents_base64_image_source)



BetaManagedAgentsURLImageSource object { type, url }



Image referenced by URL.

type: "url"



[](#beta_managed_agents_url_image_source.type)

url: string



URL of the image to fetch.

[](#beta_managed_agents_url_image_source.url)

[](#beta_managed_agents_url_image_source)



BetaManagedAgentsFileImageSource object { file_id, type }



Image referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_image_source.file_id)

type: "file"



[](#beta_managed_agents_file_image_source.type)

[](#beta_managed_agents_file_image_source)

[](#beta_managed_agents_image_block.source)

type: "image"



[](#beta_managed_agents_image_block.type)

[](#beta_managed_agents_image_block)



BetaManagedAgentsDocumentBlock object { source, type, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_document_source) { data, media_type, type } or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_plain_text_document_source) { data, media_type, type } or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_document_source) { type, url } or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_document_source) { file_id, type }



Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media_type, type }



Base64-encoded document data.

data: string



Base64-encoded document data.

[](#beta_managed_agents_base64_document_source.data)

media_type: string



MIME type of the document (e.g., "application/pdf").

[](#beta_managed_agents_base64_document_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_document_source.type)

[](#beta_managed_agents_base64_document_source)



BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }



Plain text document content.

data: string



The plain text content.

[](#beta_managed_agents_plain_text_document_source.data)

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".

[](#beta_managed_agents_plain_text_document_source.media_type)

type: "text"



[](#beta_managed_agents_plain_text_document_source.type)

[](#beta_managed_agents_plain_text_document_source)



BetaManagedAgentsURLDocumentSource object { type, url }



Document referenced by URL.

type: "url"



[](#beta_managed_agents_url_document_source.type)

url: string



URL of the document to fetch.

[](#beta_managed_agents_url_document_source.url)

[](#beta_managed_agents_url_document_source)



BetaManagedAgentsFileDocumentSource object { file_id, type }



Document referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_document_source.file_id)

type: "file"



[](#beta_managed_agents_file_document_source.type)

[](#beta_managed_agents_file_document_source)

[](#beta_managed_agents_document_block.source)

type: "document"



[](#beta_managed_agents_document_block.type)

context: optional string



Additional context about the document for the model.

[](#beta_managed_agents_document_block.context)

title: optional string



The title of the document.

[](#beta_managed_agents_document_block.title)

[](#beta_managed_agents_document_block)

[](#beta_managed_agents_user_message_event_params.content)

type: "user.message"



[](#beta_managed_agents_user_message_event_params.type)

[](#beta_managed_agents_user_message_event_params)



BetaManagedAgentsUserInterruptEventParams object { type, session_thread_id }



Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"



[](#beta_managed_agents_user_interrupt_event_params.type)

session_thread_id: optional string



If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

[](#beta_managed_agents_user_interrupt_event_params.session_thread_id)

[](#beta_managed_agents_user_interrupt_event_params)



BetaManagedAgentsUserToolConfirmationEventParams object { result, tool_use_id, type, deny_message }



Parameters for confirming or denying a tool execution request.



result: "allow" or "deny"



UserToolConfirmationResult enum

One of the following:

"allow"



[](#beta_managed_agents_user_tool_confirmation_event_params.result%5B0%5D)

"deny"



[](#beta_managed_agents_user_tool_confirmation_event_params.result%5B1%5D)

[](#beta_managed_agents_user_tool_confirmation_event_params.result)

tool_use_id: string



The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

[](#beta_managed_agents_user_tool_confirmation_event_params.tool_use_id)

type: "user.tool_confirmation"



[](#beta_managed_agents_user_tool_confirmation_event_params.type)

deny_message: optional string



Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

[](#beta_managed_agents_user_tool_confirmation_event_params.deny_message)

[](#beta_managed_agents_user_tool_confirmation_event_params)



BetaManagedAgentsUserCustomToolResultEventParams object { custom_tool_use_id, type, content, is_error }



Parameters for providing the result of a custom tool execution.

custom_tool_use_id: string



The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

[](#beta_managed_agents_user_custom_tool_result_event_params.custom_tool_use_id)

type: "user.custom_tool_result"



[](#beta_managed_agents_user_custom_tool_result_event_params.type)



content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type } or [BetaManagedAgentsImageBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_image_block) { source, type } or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_document_block) { source, type, context, title } or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_block) { citations, content, source, 2 more }



The result content returned by the tool.

One of the following:



BetaManagedAgentsTextBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_text_block.text)

type: "text"



[](#beta_managed_agents_text_block.type)

[](#beta_managed_agents_text_block)



BetaManagedAgentsImageBlock object { source, type }



Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_image_source) { data, media_type, type } or [BetaManagedAgentsURLImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_image_source) { type, url } or [BetaManagedAgentsFileImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_image_source) { file_id, type }



Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media_type, type }



Base64-encoded image data.

data: string



Base64-encoded image data.

[](#beta_managed_agents_base64_image_source.data)

media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

[](#beta_managed_agents_base64_image_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_image_source.type)

[](#beta_managed_agents_base64_image_source)



BetaManagedAgentsURLImageSource object { type, url }



Image referenced by URL.

type: "url"



[](#beta_managed_agents_url_image_source.type)

url: string



URL of the image to fetch.

[](#beta_managed_agents_url_image_source.url)

[](#beta_managed_agents_url_image_source)



BetaManagedAgentsFileImageSource object { file_id, type }



Image referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_image_source.file_id)

type: "file"



[](#beta_managed_agents_file_image_source.type)

[](#beta_managed_agents_file_image_source)

[](#beta_managed_agents_image_block.source)

type: "image"



[](#beta_managed_agents_image_block.type)

[](#beta_managed_agents_image_block)



BetaManagedAgentsDocumentBlock object { source, type, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_document_source) { data, media_type, type } or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_plain_text_document_source) { data, media_type, type } or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_document_source) { type, url } or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_document_source) { file_id, type }



Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media_type, type }



Base64-encoded document data.

data: string



Base64-encoded document data.

[](#beta_managed_agents_base64_document_source.data)

media_type: string



MIME type of the document (e.g., "application/pdf").

[](#beta_managed_agents_base64_document_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_document_source.type)

[](#beta_managed_agents_base64_document_source)



BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }



Plain text document content.

data: string



The plain text content.

[](#beta_managed_agents_plain_text_document_source.data)

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".

[](#beta_managed_agents_plain_text_document_source.media_type)

type: "text"



[](#beta_managed_agents_plain_text_document_source.type)

[](#beta_managed_agents_plain_text_document_source)



BetaManagedAgentsURLDocumentSource object { type, url }



Document referenced by URL.

type: "url"



[](#beta_managed_agents_url_document_source.type)

url: string



URL of the document to fetch.

[](#beta_managed_agents_url_document_source.url)

[](#beta_managed_agents_url_document_source)



BetaManagedAgentsFileDocumentSource object { file_id, type }



Document referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_document_source.file_id)

type: "file"



[](#beta_managed_agents_file_document_source.type)

[](#beta_managed_agents_file_document_source)

[](#beta_managed_agents_document_block.source)

type: "document"



[](#beta_managed_agents_document_block.type)

context: optional string



Additional context about the document for the model.

[](#beta_managed_agents_document_block.context)

title: optional string



The title of the document.

[](#beta_managed_agents_document_block.title)

[](#beta_managed_agents_document_block)



BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }



A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_citations) { enabled }



Citation settings for a search result.

enabled: boolean



Whether citations are enabled for this search result.

[](#beta_managed_agents_search_result_block.citations%20%2B%20(resource)%20beta.sessions.events.enabled)

[](#beta_managed_agents_search_result_block.citations)



content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_content) { text, type }



Array of text content blocks from the search result.

text: string



The text content.

[](#beta_managed_agents_search_result_content.text)

type: "text"



[](#beta_managed_agents_search_result_content.type)

[](#beta_managed_agents_search_result_block.content)

source: string



The URL source of the search result.

[](#beta_managed_agents_search_result_block.source)

title: string



The title of the search result.

[](#beta_managed_agents_search_result_block.title)

type: "search_result"



[](#beta_managed_agents_search_result_block.type)

[](#beta_managed_agents_search_result_block)

[](#beta_managed_agents_user_custom_tool_result_event_params.content)

is_error: optional boolean



Whether the tool execution resulted in an error.

[](#beta_managed_agents_user_custom_tool_result_event_params.is_error)

[](#beta_managed_agents_user_custom_tool_result_event_params)



BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max_iterations }



Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: string



What the agent should produce. This is the task specification.

[](#beta_managed_agents_user_define_outcome_event_params.description)



rubric: [BetaManagedAgentsFileRubricParams](/docs/en/api/beta/sessions/events#beta_managed_agents_file_rubric_params) { file_id, type } or [BetaManagedAgentsTextRubricParams](/docs/en/api/beta/sessions/events#beta_managed_agents_text_rubric_params) { content, type }



Rubric for grading the quality of an outcome.

One of the following:



BetaManagedAgentsFileRubricParams object { file_id, type }



Rubric referenced by a file uploaded via the Files API.

file_id: string



ID of the rubric file.

[](#beta_managed_agents_file_rubric_params.file_id)

type: "file"



[](#beta_managed_agents_file_rubric_params.type)

[](#beta_managed_agents_file_rubric_params)



BetaManagedAgentsTextRubricParams object { content, type }



Rubric content provided inline as text.

content: string



Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

[](#beta_managed_agents_text_rubric_params.content)

type: "text"



[](#beta_managed_agents_text_rubric_params.type)

[](#beta_managed_agents_text_rubric_params)

[](#beta_managed_agents_user_define_outcome_event_params.rubric)

type: "user.define_outcome"



[](#beta_managed_agents_user_define_outcome_event_params.type)

max_iterations: optional number



Eval→revision cycles before giving up. Default 3, max 20.

[](#beta_managed_agents_user_define_outcome_event_params.max_iterations)

[](#beta_managed_agents_user_define_outcome_event_params)



BetaManagedAgentsUserToolResultEventParams object { tool_use_id, type, content, is_error }



Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

tool_use_id: string



The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

[](#beta_managed_agents_user_tool_result_event_params.tool_use_id)

type: "user.tool_result"



[](#beta_managed_agents_user_tool_result_event_params.type)



content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type } or [BetaManagedAgentsImageBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_image_block) { source, type } or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_document_block) { source, type, context, title } or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_block) { citations, content, source, 2 more }



The result content returned by the tool.

One of the following:



BetaManagedAgentsTextBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_text_block.text)

type: "text"



[](#beta_managed_agents_text_block.type)

[](#beta_managed_agents_text_block)



BetaManagedAgentsImageBlock object { source, type }



Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_image_source) { data, media_type, type } or [BetaManagedAgentsURLImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_image_source) { type, url } or [BetaManagedAgentsFileImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_image_source) { file_id, type }



Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media_type, type }



Base64-encoded image data.

data: string



Base64-encoded image data.

[](#beta_managed_agents_base64_image_source.data)

media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

[](#beta_managed_agents_base64_image_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_image_source.type)

[](#beta_managed_agents_base64_image_source)



BetaManagedAgentsURLImageSource object { type, url }



Image referenced by URL.

type: "url"



[](#beta_managed_agents_url_image_source.type)

url: string



URL of the image to fetch.

[](#beta_managed_agents_url_image_source.url)

[](#beta_managed_agents_url_image_source)



BetaManagedAgentsFileImageSource object { file_id, type }



Image referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_image_source.file_id)

type: "file"



[](#beta_managed_agents_file_image_source.type)

[](#beta_managed_agents_file_image_source)

[](#beta_managed_agents_image_block.source)

type: "image"



[](#beta_managed_agents_image_block.type)

[](#beta_managed_agents_image_block)



BetaManagedAgentsDocumentBlock object { source, type, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_document_source) { data, media_type, type } or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_plain_text_document_source) { data, media_type, type } or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_document_source) { type, url } or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_document_source) { file_id, type }



Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media_type, type }



Base64-encoded document data.

data: string



Base64-encoded document data.

[](#beta_managed_agents_base64_document_source.data)

media_type: string



MIME type of the document (e.g., "application/pdf").

[](#beta_managed_agents_base64_document_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_document_source.type)

[](#beta_managed_agents_base64_document_source)



BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }



Plain text document content.

data: string



The plain text content.

[](#beta_managed_agents_plain_text_document_source.data)

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".

[](#beta_managed_agents_plain_text_document_source.media_type)

type: "text"



[](#beta_managed_agents_plain_text_document_source.type)

[](#beta_managed_agents_plain_text_document_source)



BetaManagedAgentsURLDocumentSource object { type, url }



Document referenced by URL.

type: "url"



[](#beta_managed_agents_url_document_source.type)

url: string



URL of the document to fetch.

[](#beta_managed_agents_url_document_source.url)

[](#beta_managed_agents_url_document_source)



BetaManagedAgentsFileDocumentSource object { file_id, type }



Document referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_document_source.file_id)

type: "file"



[](#beta_managed_agents_file_document_source.type)

[](#beta_managed_agents_file_document_source)

[](#beta_managed_agents_document_block.source)

type: "document"



[](#beta_managed_agents_document_block.type)

context: optional string



Additional context about the document for the model.

[](#beta_managed_agents_document_block.context)

title: optional string



The title of the document.

[](#beta_managed_agents_document_block.title)

[](#beta_managed_agents_document_block)



BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }



A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_citations) { enabled }



Citation settings for a search result.

enabled: boolean



Whether citations are enabled for this search result.

[](#beta_managed_agents_search_result_block.citations%20%2B%20(resource)%20beta.sessions.events.enabled)

[](#beta_managed_agents_search_result_block.citations)



content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_content) { text, type }



Array of text content blocks from the search result.

text: string



The text content.

[](#beta_managed_agents_search_result_content.text)

type: "text"



[](#beta_managed_agents_search_result_content.type)

[](#beta_managed_agents_search_result_block.content)

source: string



The URL source of the search result.

[](#beta_managed_agents_search_result_block.source)

title: string



The title of the search result.

[](#beta_managed_agents_search_result_block.title)

type: "search_result"



[](#beta_managed_agents_search_result_block.type)

[](#beta_managed_agents_search_result_block)

[](#beta_managed_agents_user_tool_result_event_params.content)

is_error: optional boolean



Whether the tool execution resulted in an error.

[](#beta_managed_agents_user_tool_result_event_params.is_error)

[](#beta_managed_agents_user_tool_result_event_params)



BetaManagedAgentsSystemMessageEventParams object { content, type }



Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



content: array of [BetaManagedAgentsSystemContentBlock](/docs/en/api/beta/sessions#beta_managed_agents_system_content_block) { text, type }



System content blocks to append. Text-only.

text: string



The text content.

[](#beta_managed_agents_system_content_block.text)

type: "text"



[](#beta_managed_agents_system_content_block.type)

[](#beta_managed_agents_system_message_event_params.content)

type: "system.message"



[](#beta_managed_agents_system_message_event_params.type)

[](#beta_managed_agents_system_message_event_params)

[](#send.events)

##### ReturnsExpand Collapse 



BetaManagedAgentsSendSessionEvents object { data }



Events that were successfully sent to the session.



data: optional array of [BetaManagedAgentsUserMessageEvent](/docs/en/api/beta/sessions/events#beta_managed_agents_user_message_event) { id, content, type, processed_at } or [BetaManagedAgentsUserInterruptEvent](/docs/en/api/beta/sessions/events#beta_managed_agents_user_interrupt_event) { id, type, processed_at, session_thread_id } or [BetaManagedAgentsUserToolConfirmationEvent](/docs/en/api/beta/sessions/events#beta_managed_agents_user_tool_confirmation_event) { id, result, tool_use_id, 4 more } or 4 more



Sent events

One of the following:



BetaManagedAgentsUserMessageEvent object { id, content, type, processed_at }



A user message event in the session conversation.

id: string



Unique identifier for this event.

[](#beta_managed_agents_user_message_event.id)



content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type } or [BetaManagedAgentsImageBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_image_block) { source, type } or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_document_block) { source, type, context, title }



Array of content blocks comprising the user message.

One of the following:



BetaManagedAgentsTextBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_text_block.text)

type: "text"



[](#beta_managed_agents_text_block.type)

[](#beta_managed_agents_text_block)



BetaManagedAgentsImageBlock object { source, type }



Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_image_source) { data, media_type, type } or [BetaManagedAgentsURLImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_image_source) { type, url } or [BetaManagedAgentsFileImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_image_source) { file_id, type }



Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media_type, type }



Base64-encoded image data.

data: string



Base64-encoded image data.

[](#beta_managed_agents_base64_image_source.data)

media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

[](#beta_managed_agents_base64_image_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_image_source.type)

[](#beta_managed_agents_base64_image_source)



BetaManagedAgentsURLImageSource object { type, url }



Image referenced by URL.

type: "url"



[](#beta_managed_agents_url_image_source.type)

url: string



URL of the image to fetch.

[](#beta_managed_agents_url_image_source.url)

[](#beta_managed_agents_url_image_source)



BetaManagedAgentsFileImageSource object { file_id, type }



Image referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_image_source.file_id)

type: "file"



[](#beta_managed_agents_file_image_source.type)

[](#beta_managed_agents_file_image_source)

[](#beta_managed_agents_image_block.source)

type: "image"



[](#beta_managed_agents_image_block.type)

[](#beta_managed_agents_image_block)



BetaManagedAgentsDocumentBlock object { source, type, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_document_source) { data, media_type, type } or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_plain_text_document_source) { data, media_type, type } or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_document_source) { type, url } or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_document_source) { file_id, type }



Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media_type, type }



Base64-encoded document data.

data: string



Base64-encoded document data.

[](#beta_managed_agents_base64_document_source.data)

media_type: string



MIME type of the document (e.g., "application/pdf").

[](#beta_managed_agents_base64_document_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_document_source.type)

[](#beta_managed_agents_base64_document_source)



BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }



Plain text document content.

data: string



The plain text content.

[](#beta_managed_agents_plain_text_document_source.data)

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".

[](#beta_managed_agents_plain_text_document_source.media_type)

type: "text"



[](#beta_managed_agents_plain_text_document_source.type)

[](#beta_managed_agents_plain_text_document_source)



BetaManagedAgentsURLDocumentSource object { type, url }



Document referenced by URL.

type: "url"



[](#beta_managed_agents_url_document_source.type)

url: string



URL of the document to fetch.

[](#beta_managed_agents_url_document_source.url)

[](#beta_managed_agents_url_document_source)



BetaManagedAgentsFileDocumentSource object { file_id, type }



Document referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_document_source.file_id)

type: "file"



[](#beta_managed_agents_file_document_source.type)

[](#beta_managed_agents_file_document_source)

[](#beta_managed_agents_document_block.source)

type: "document"



[](#beta_managed_agents_document_block.type)

context: optional string



Additional context about the document for the model.

[](#beta_managed_agents_document_block.context)

title: optional string



The title of the document.

[](#beta_managed_agents_document_block.title)

[](#beta_managed_agents_document_block)

[](#beta_managed_agents_user_message_event.content)

type: "user.message"



[](#beta_managed_agents_user_message_event.type)

processed_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_user_message_event.processed_at)

[](#beta_managed_agents_user_message_event)



BetaManagedAgentsUserInterruptEvent object { id, type, processed_at, session_thread_id }



An interrupt event that pauses agent execution and returns control to the user.

id: string



Unique identifier for this event.

[](#beta_managed_agents_user_interrupt_event.id)

type: "user.interrupt"



[](#beta_managed_agents_user_interrupt_event.type)

processed_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_user_interrupt_event.processed_at)

session_thread_id: optional string



If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

[](#beta_managed_agents_user_interrupt_event.session_thread_id)

[](#beta_managed_agents_user_interrupt_event)



BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool_use_id, 4 more }



A tool confirmation event that approves or denies a pending tool execution.

id: string



Unique identifier for this event.

[](#beta_managed_agents_user_tool_confirmation_event.id)



result: "allow" or "deny"



UserToolConfirmationResult enum

One of the following:

"allow"



[](#beta_managed_agents_user_tool_confirmation_event.result%5B0%5D)

"deny"



[](#beta_managed_agents_user_tool_confirmation_event.result%5B1%5D)

[](#beta_managed_agents_user_tool_confirmation_event.result)

tool_use_id: string



The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

[](#beta_managed_agents_user_tool_confirmation_event.tool_use_id)

type: "user.tool_confirmation"



[](#beta_managed_agents_user_tool_confirmation_event.type)

deny_message: optional string



Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

[](#beta_managed_agents_user_tool_confirmation_event.deny_message)

processed_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_user_tool_confirmation_event.processed_at)

session_thread_id: optional string



When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

[](#beta_managed_agents_user_tool_confirmation_event.session_thread_id)

[](#beta_managed_agents_user_tool_confirmation_event)



BetaManagedAgentsUserCustomToolResultEvent object { id, custom_tool_use_id, type, 4 more }



Event sent by the client providing the result of a custom tool execution.

id: string



Unique identifier for this event.

[](#beta_managed_agents_user_custom_tool_result_event.id)

custom_tool_use_id: string



The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

[](#beta_managed_agents_user_custom_tool_result_event.custom_tool_use_id)

type: "user.custom_tool_result"



[](#beta_managed_agents_user_custom_tool_result_event.type)



content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type } or [BetaManagedAgentsImageBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_image_block) { source, type } or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_document_block) { source, type, context, title } or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_block) { citations, content, source, 2 more }



The result content returned by the tool.

One of the following:



BetaManagedAgentsTextBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_text_block.text)

type: "text"



[](#beta_managed_agents_text_block.type)

[](#beta_managed_agents_text_block)



BetaManagedAgentsImageBlock object { source, type }



Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_image_source) { data, media_type, type } or [BetaManagedAgentsURLImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_image_source) { type, url } or [BetaManagedAgentsFileImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_image_source) { file_id, type }



Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media_type, type }



Base64-encoded image data.

data: string



Base64-encoded image data.

[](#beta_managed_agents_base64_image_source.data)

media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

[](#beta_managed_agents_base64_image_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_image_source.type)

[](#beta_managed_agents_base64_image_source)



BetaManagedAgentsURLImageSource object { type, url }



Image referenced by URL.

type: "url"



[](#beta_managed_agents_url_image_source.type)

url: string



URL of the image to fetch.

[](#beta_managed_agents_url_image_source.url)

[](#beta_managed_agents_url_image_source)



BetaManagedAgentsFileImageSource object { file_id, type }



Image referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_image_source.file_id)

type: "file"



[](#beta_managed_agents_file_image_source.type)

[](#beta_managed_agents_file_image_source)

[](#beta_managed_agents_image_block.source)

type: "image"



[](#beta_managed_agents_image_block.type)

[](#beta_managed_agents_image_block)



BetaManagedAgentsDocumentBlock object { source, type, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_document_source) { data, media_type, type } or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_plain_text_document_source) { data, media_type, type } or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_document_source) { type, url } or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_document_source) { file_id, type }



Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media_type, type }



Base64-encoded document data.

data: string



Base64-encoded document data.

[](#beta_managed_agents_base64_document_source.data)

media_type: string



MIME type of the document (e.g., "application/pdf").

[](#beta_managed_agents_base64_document_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_document_source.type)

[](#beta_managed_agents_base64_document_source)



BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }



Plain text document content.

data: string



The plain text content.

[](#beta_managed_agents_plain_text_document_source.data)

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".

[](#beta_managed_agents_plain_text_document_source.media_type)

type: "text"



[](#beta_managed_agents_plain_text_document_source.type)

[](#beta_managed_agents_plain_text_document_source)



BetaManagedAgentsURLDocumentSource object { type, url }



Document referenced by URL.

type: "url"



[](#beta_managed_agents_url_document_source.type)

url: string



URL of the document to fetch.

[](#beta_managed_agents_url_document_source.url)

[](#beta_managed_agents_url_document_source)



BetaManagedAgentsFileDocumentSource object { file_id, type }



Document referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_document_source.file_id)

type: "file"



[](#beta_managed_agents_file_document_source.type)

[](#beta_managed_agents_file_document_source)

[](#beta_managed_agents_document_block.source)

type: "document"



[](#beta_managed_agents_document_block.type)

context: optional string



Additional context about the document for the model.

[](#beta_managed_agents_document_block.context)

title: optional string



The title of the document.

[](#beta_managed_agents_document_block.title)

[](#beta_managed_agents_document_block)



BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }



A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_citations) { enabled }



Citation settings for a search result.

enabled: boolean



Whether citations are enabled for this search result.

[](#beta_managed_agents_search_result_block.citations%20%2B%20(resource)%20beta.sessions.events.enabled)

[](#beta_managed_agents_search_result_block.citations)



content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_content) { text, type }



Array of text content blocks from the search result.

text: string



The text content.

[](#beta_managed_agents_search_result_content.text)

type: "text"



[](#beta_managed_agents_search_result_content.type)

[](#beta_managed_agents_search_result_block.content)

source: string



The URL source of the search result.

[](#beta_managed_agents_search_result_block.source)

title: string



The title of the search result.

[](#beta_managed_agents_search_result_block.title)

type: "search_result"



[](#beta_managed_agents_search_result_block.type)

[](#beta_managed_agents_search_result_block)

[](#beta_managed_agents_user_custom_tool_result_event.content)

is_error: optional boolean



Whether the tool execution resulted in an error.

[](#beta_managed_agents_user_custom_tool_result_event.is_error)

processed_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_user_custom_tool_result_event.processed_at)

session_thread_id: optional string



Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

[](#beta_managed_agents_user_custom_tool_result_event.session_thread_id)

[](#beta_managed_agents_user_custom_tool_result_event)



BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max_iterations, 4 more }



Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: string



Unique identifier for this event.

[](#beta_managed_agents_user_define_outcome_event.id)

description: string



What the agent should produce. Copied from the input event.

[](#beta_managed_agents_user_define_outcome_event.description)

max_iterations: number



Evaluate-then-revise cycles before giving up. Default 3, max 20.

[](#beta_managed_agents_user_define_outcome_event.max_iterations)

outcome_id: string



Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

[](#beta_managed_agents_user_define_outcome_event.outcome_id)

processed_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_user_define_outcome_event.processed_at)



rubric: [BetaManagedAgentsFileRubric](/docs/en/api/beta/sessions/events#beta_managed_agents_file_rubric) { file_id, type } or [BetaManagedAgentsTextRubric](/docs/en/api/beta/sessions/events#beta_managed_agents_text_rubric) { content, type }



Rubric for grading the quality of an outcome.

One of the following:



BetaManagedAgentsFileRubric object { file_id, type }



Rubric referenced by a file uploaded via the Files API.

file_id: string



ID of the rubric file.

[](#beta_managed_agents_file_rubric.file_id)

type: "file"



[](#beta_managed_agents_file_rubric.type)

[](#beta_managed_agents_file_rubric)



BetaManagedAgentsTextRubric object { content, type }



Rubric content provided inline as text.

content: string



Rubric content. Plain text or markdown — the grader treats it as freeform text.

[](#beta_managed_agents_text_rubric.content)

type: "text"



[](#beta_managed_agents_text_rubric.type)

[](#beta_managed_agents_text_rubric)

[](#beta_managed_agents_user_define_outcome_event.rubric)

type: "user.define_outcome"



[](#beta_managed_agents_user_define_outcome_event.type)

[](#beta_managed_agents_user_define_outcome_event)



BetaManagedAgentsUserToolResultEvent object { id, tool_use_id, type, 4 more }



Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

id: string



Unique identifier for this event.

[](#beta_managed_agents_user_tool_result_event.id)

tool_use_id: string



The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

[](#beta_managed_agents_user_tool_result_event.tool_use_id)

type: "user.tool_result"



[](#beta_managed_agents_user_tool_result_event.type)



content: optional array of [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type } or [BetaManagedAgentsImageBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_image_block) { source, type } or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_document_block) { source, type, context, title } or [BetaManagedAgentsSearchResultBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_block) { citations, content, source, 2 more }



The result content returned by the tool.

One of the following:



BetaManagedAgentsTextBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_text_block.text)

type: "text"



[](#beta_managed_agents_text_block.type)

[](#beta_managed_agents_text_block)



BetaManagedAgentsImageBlock object { source, type }



Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_image_source) { data, media_type, type } or [BetaManagedAgentsURLImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_image_source) { type, url } or [BetaManagedAgentsFileImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_image_source) { file_id, type }



Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media_type, type }



Base64-encoded image data.

data: string



Base64-encoded image data.

[](#beta_managed_agents_base64_image_source.data)

media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

[](#beta_managed_agents_base64_image_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_image_source.type)

[](#beta_managed_agents_base64_image_source)



BetaManagedAgentsURLImageSource object { type, url }



Image referenced by URL.

type: "url"



[](#beta_managed_agents_url_image_source.type)

url: string



URL of the image to fetch.

[](#beta_managed_agents_url_image_source.url)

[](#beta_managed_agents_url_image_source)



BetaManagedAgentsFileImageSource object { file_id, type }



Image referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_image_source.file_id)

type: "file"



[](#beta_managed_agents_file_image_source.type)

[](#beta_managed_agents_file_image_source)

[](#beta_managed_agents_image_block.source)

type: "image"



[](#beta_managed_agents_image_block.type)

[](#beta_managed_agents_image_block)



BetaManagedAgentsDocumentBlock object { source, type, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_document_source) { data, media_type, type } or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_plain_text_document_source) { data, media_type, type } or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_document_source) { type, url } or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_document_source) { file_id, type }



Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media_type, type }



Base64-encoded document data.

data: string



Base64-encoded document data.

[](#beta_managed_agents_base64_document_source.data)

media_type: string



MIME type of the document (e.g., "application/pdf").

[](#beta_managed_agents_base64_document_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_document_source.type)

[](#beta_managed_agents_base64_document_source)



BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }



Plain text document content.

data: string



The plain text content.

[](#beta_managed_agents_plain_text_document_source.data)

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".

[](#beta_managed_agents_plain_text_document_source.media_type)

type: "text"



[](#beta_managed_agents_plain_text_document_source.type)

[](#beta_managed_agents_plain_text_document_source)



BetaManagedAgentsURLDocumentSource object { type, url }



Document referenced by URL.

type: "url"



[](#beta_managed_agents_url_document_source.type)

url: string



URL of the document to fetch.

[](#beta_managed_agents_url_document_source.url)

[](#beta_managed_agents_url_document_source)



BetaManagedAgentsFileDocumentSource object { file_id, type }



Document referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_document_source.file_id)

type: "file"



[](#beta_managed_agents_file_document_source.type)

[](#beta_managed_agents_file_document_source)

[](#beta_managed_agents_document_block.source)

type: "document"



[](#beta_managed_agents_document_block.type)

context: optional string



Additional context about the document for the model.

[](#beta_managed_agents_document_block.context)

title: optional string



The title of the document.

[](#beta_managed_agents_document_block.title)

[](#beta_managed_agents_document_block)



BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more }



A block containing a web search result.



citations: [BetaManagedAgentsSearchResultCitations](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_citations) { enabled }



Citation settings for a search result.

enabled: boolean



Whether citations are enabled for this search result.

[](#beta_managed_agents_search_result_block.citations%20%2B%20(resource)%20beta.sessions.events.enabled)

[](#beta_managed_agents_search_result_block.citations)



content: array of [BetaManagedAgentsSearchResultContent](/docs/en/api/beta/sessions/events#beta_managed_agents_search_result_content) { text, type }



Array of text content blocks from the search result.

text: string



The text content.

[](#beta_managed_agents_search_result_content.text)

type: "text"



[](#beta_managed_agents_search_result_content.type)

[](#beta_managed_agents_search_result_block.content)

source: string



The URL source of the search result.

[](#beta_managed_agents_search_result_block.source)

title: string



The title of the search result.

[](#beta_managed_agents_search_result_block.title)

type: "search_result"



[](#beta_managed_agents_search_result_block.type)

[](#beta_managed_agents_search_result_block)

[](#beta_managed_agents_user_tool_result_event.content)

is_error: optional boolean



Whether the tool execution resulted in an error.

[](#beta_managed_agents_user_tool_result_event.is_error)

processed_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_user_tool_result_event.processed_at)

session_thread_id: optional string



Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

[](#beta_managed_agents_user_tool_result_event.session_thread_id)

[](#beta_managed_agents_user_tool_result_event)



BetaManagedAgentsSystemMessageEvent object { id, content, type, processed_at }



A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

id: string



Unique identifier for this event.

[](#beta_managed_agents_system_message_event.id)



content: array of [BetaManagedAgentsSystemContentBlock](/docs/en/api/beta/sessions#beta_managed_agents_system_content_block) { text, type }



System content blocks. Text-only.

text: string



The text content.

[](#beta_managed_agents_system_content_block.text)

type: "text"



[](#beta_managed_agents_system_content_block.type)

[](#beta_managed_agents_system_message_event.content)

type: "system.message"



[](#beta_managed_agents_system_message_event.type)

processed_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_system_message_event.processed_at)

[](#beta_managed_agents_system_message_event)

[](#beta_managed_agents_send_session_events.data)

[](#beta_managed_agents_send_session_events)

Send Events

cURL



```python
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "events": [
            {
              "content": [
                {
                  "text": "Where is my order #1234?",
                  "type": "text"
                }
              ],
              "type": "user.message"
            }
          ]
        }'
```

Response 200



```python
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
