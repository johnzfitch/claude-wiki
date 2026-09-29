---
title: "Events - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/events"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:47Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fsessions%2Fevents)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions


Create Session


List Sessions


Get Session


Update Session


Delete Session


Archive Session

Events


List Events


Send Events


Stream Events

Resources

Threads

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)
3.  [Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions)

# Events

##### [List Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/list)

GET/v1/sessions/{session_id}/events

##### [Send Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/send)

POST/v1/sessions/{session_id}/events

##### [Stream Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/stream)

GET/v1/sessions/{session_id}/events/stream

##### Models



BetaManagedAgentsAgentAutoEvaluatedPermission = [BetaManagedAgentsAgentAutoEvaluatedPermissionAllow](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_agent_auto_evaluated_permission_allow) or [BetaManagedAgentsAgentAutoEvaluatedPermissionAsk](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_agent_auto_evaluated_permission_ask) or [BetaManagedAgentsAgentAutoEvaluatedPermissionDeny](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_agent_auto_evaluated_permission_deny)



The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

One of the following:



BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object{ type: "allow" }



The server judged the invocation safe to execute without client approval.

type: "allow"





BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object{ type: "ask", reason_code }



The server reached no judgement; the invocation is held for client approval.

type: "ask"





reason_code: string



The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

maxLength64



BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object{ type: "deny", reason_code }



The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

type: "deny"





reason_code: string



The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

maxLength64



BetaManagedAgentsAgentCustomToolUseEvent object{ type: "agent.custom_tool_use", id, input, 3 more }



Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

type: "agent.custom_tool_use"



id: string



Unique identifier for this event.

input: map\[unknown\]



Input parameters for the tool call.

name: string



Name of the custom tool being called.



processed_at: string



Timestamp when this tool use was processed.

formatdate-time

session_thread_id: optional string or null



When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.



BetaManagedAgentsAgentEvaluatedPermission = "allow" or "ask" or "deny"



AgentEvaluatedPermission enum

One of the following:

"allow"



"ask"



"deny"





BetaManagedAgentsAgentMCPToolResultEvent object{ type: "agent.mcp_tool_result", id, mcp_tool_use_id, 3 more }



Event representing the result of an MCP tool execution.



BetaManagedAgentsAgentMCPToolUseEvent object{ type: "agent.mcp_tool_use", id, input, 6 more }



Event emitted when the agent invokes a tool provided by an MCP server.



BetaManagedAgentsAgentMessageEvent object{ type: "agent.message", id, content, processed_at }



An agent response event in the session conversation.



BetaManagedAgentsAgentThinkingEvent object{ type: "agent.thinking", id, processed_at }



Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

type: "agent.thinking"



id: string



Unique identifier for this event.



processed_at: string



Timestamp when this thinking was produced.

formatdate-time



BetaManagedAgentsAgentThreadContextCompactedEvent object{ type: "agent.thread_context_compacted", id, processed_at }



Indicates that context compaction (summarization) occurred during the session.

type: "agent.thread_context_compacted"



id: string



Unique identifier for this event.



processed_at: string



Timestamp when compaction was processed.

formatdate-time



BetaManagedAgentsAgentThreadMessageReceivedEvent object{ type: "agent.thread_message_received", id, content, 3 more }



Delivery event written to the target thread's input stream when an agent-to-agent message arrives.



BetaManagedAgentsAgentThreadMessageSentEvent object{ type: "agent.thread_message_sent", id, content, 3 more }



Observability event emitted to the sender's output stream when an agent-to-agent message is sent.



BetaManagedAgentsAgentToolEvaluation = [BetaManagedAgentsAgentToolEvaluationAlwaysAllow](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_agent_tool_evaluation_always_allow) or [BetaManagedAgentsAgentToolEvaluationAlwaysAsk](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_agent_tool_evaluation_always_ask) or [BetaManagedAgentsAgentToolEvaluationAuto](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_agent_tool_evaluation_auto)



Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

One of the following:



BetaManagedAgentsAgentToolEvaluationAlwaysAllow object{ type: "always_allow" }



The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

type: "always_allow"





BetaManagedAgentsAgentToolEvaluationAlwaysAsk object{ type: "always_ask" }



The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

type: "always_ask"





BetaManagedAgentsAgentToolEvaluationAuto object{ type: "auto", evaluated_permission }



The resolved permission_policy was auto: the server judged this invocation individually.

type: "auto"





evaluated_permission: [BetaManagedAgentsAgentAutoEvaluatedPermission](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_agent_auto_evaluated_permission)



The server's judgement for this invocation.

One of the following:



BetaManagedAgentsAgentToolResultEvent object{ type: "agent.tool_result", id, processed_at, 3 more }



Event representing the result of an agent tool execution.



BetaManagedAgentsAgentToolUseEvent object{ type: "agent.tool_use", id, input, 5 more }



Event emitted when the agent invokes a built-in agent tool.



BetaManagedAgentsBase64DocumentSource object{ type: "base64", data, media_type }



Base64-encoded document data.

type: "base64"





data: string



Base64-encoded document data.

minLength1



media_type: string



MIME type of the document (e.g., "application/pdf").

minLength1



BetaManagedAgentsBase64ImageSource object{ type: "base64", data, media_type }



Base64-encoded image data.

type: "base64"





data: string



Base64-encoded image data.

minLength1



media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

minLength1



BetaManagedAgentsBillingError object{ type: "billing_error", message, retry_status }



The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.



BetaManagedAgentsCredentialHostUnreachableError object{ type: "credential_host_unreachable_error", credential_id, message, 2 more }



An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.



BetaManagedAgentsDocumentBlock object{ type: "document", source, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



BetaManagedAgentsEventParams = [BetaManagedAgentsUserMessageEventParams](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_message_event_params) or [BetaManagedAgentsUserInterruptEventParams](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_interrupt_event_params) or [BetaManagedAgentsUserToolConfirmationEventParams](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_tool_confirmation_event_params) or 4 more



Union type for event parameters that can be sent to a session.

One of the following:



BetaManagedAgentsFileDocumentSource object{ type: "file", file_id }



Document referenced by file ID.

type: "file"





file_id: string



ID of a previously uploaded file.

minLength1



BetaManagedAgentsFileImageSource object{ type: "file", file_id }



Image referenced by file ID.

type: "file"





file_id: string



ID of a previously uploaded file.

minLength1



BetaManagedAgentsFileRubric object{ type: "file", file_id }



Rubric referenced by a file uploaded via the Files API.

type: "file"



file_id: string



ID of the rubric file.



BetaManagedAgentsFileRubricParams object{ type: "file", file_id }



Rubric referenced by a file uploaded via the Files API.

type: "file"



file_id: string



ID of the rubric file.



BetaManagedAgentsImageBlock object{ type: "image", source }



Image content specified directly as base64 data or as a reference via a URL.



BetaManagedAgentsMCPAuthenticationFailedError object{ type: "mcp_authentication_failed_error", mcp_server_name, message, retry_status }



Authentication to an MCP server failed.



BetaManagedAgentsMCPConnectionFailedError object{ type: "mcp_connection_failed_error", mcp_server_name, message, retry_status }



Failed to connect to an MCP server.



BetaManagedAgentsModelOverloadedError object{ type: "model_overloaded_error", message, retry_status }



The model is currently overloaded. Emitted after automatic retries are exhausted.



BetaManagedAgentsModelRateLimitedError object{ type: "model_rate_limited_error", message, retry_status }



The model request was rate-limited.



BetaManagedAgentsModelRequestFailedError object{ type: "model_request_failed_error", message, retry_status }



A model request failed for a reason other than overload or rate-limiting.



BetaManagedAgentsPlainTextDocumentSource object{ type: "text", data, media_type }



Plain text document content.

type: "text"





data: string



The plain text content.

minLength1

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".



BetaManagedAgentsRedactedBlock object{ type: "redacted" }



Placeholder for content withheld by Anthropic model policy.

type: "redacted"





BetaManagedAgentsRetryStatusExhausted object{ type: "exhausted" }



This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"





BetaManagedAgentsRetryStatusRetrying object{ type: "retrying" }



The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"





BetaManagedAgentsRetryStatusTerminal object{ type: "terminal" }



The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"





BetaManagedAgentsSearchResultBlock object{ type: "search_result", citations, content, 2 more }



A block containing a web search result.

type: "search_result"





citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_search_result_citations) { enabled }



Citation settings for this search result.

enabled: boolean



Whether citations are enabled for this search result.



content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_search_result_content) { type: "text", text }



Array of text content blocks from the search result.

type: "text"





text: string



The text content.

minLength1



source: string



The URL source of the search result.

minLength1



title: string



The title of the search result.

minLength1



BetaManagedAgentsSearchResultCitations object{ enabled }



Citation settings for a search result.

enabled: boolean



Whether citations are enabled for this search result.



BetaManagedAgentsSearchResultContent object{ type: "text", text }



Text content within a search result.

type: "text"





text: string



The text content.

minLength1



BetaManagedAgentsSendSessionEvents object{ data }



Events that were successfully sent to the session.



BetaManagedAgentsSessionBudgetReached object{ type: "budget_reached" }



The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

type: "budget_reached"





BetaManagedAgentsSessionDeletedEvent object{ type: "session.deleted", id, processed_at }



Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

type: "session.deleted"



id: string



Unique identifier for this event.



processed_at: string



Timestamp when the session was deleted.

formatdate-time



BetaManagedAgentsSessionEndTurn object{ type: "end_turn" }



The agent completed its turn naturally and is ready for the next user message.

type: "end_turn"





BetaManagedAgentsSessionErrorEvent object{ type: "session.error", id, error, processed_at }



An error event indicating a problem occurred during session execution.



BetaManagedAgentsSessionEvent = [BetaManagedAgentsUserMessageEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_message_event) or [BetaManagedAgentsUserInterruptEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_interrupt_event) or [BetaManagedAgentsUserToolConfirmationEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_tool_confirmation_event) or 32 more



Union type for all event types in a session.

One of the following:



BetaManagedAgentsSessionRequiresAction object{ type: "requires_action", event_ids }



The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

type: "requires_action"



event_ids: array of string



The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.



BetaManagedAgentsSessionRetriesExhausted object{ type: "retries_exhausted" }



The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

type: "retries_exhausted"





BetaManagedAgentsSessionStatusIdleEvent object{ type: "session.status_idle", id, processed_at, stop_reason }



Indicates the agent has paused and is awaiting user input.



BetaManagedAgentsSessionStatusRescheduledEvent object{ type: "session.status_rescheduled", id, processed_at }



Indicates the session is recovering from an error state and is rescheduled for execution.

type: "session.status_rescheduled"



id: string



Unique identifier for this event.



processed_at: string



Timestamp of status change.

formatdate-time



BetaManagedAgentsSessionStatusRunningEvent object{ type: "session.status_running", id, processed_at }



Indicates the session is actively running and the agent is working.

type: "session.status_running"



id: string



Unique identifier for this event.



processed_at: string



Timestamp of status change.

formatdate-time



BetaManagedAgentsSessionStatusTerminatedEvent object{ type: "session.status_terminated", id, processed_at }



Indicates the session has terminated, either due to an error or completion.

type: "session.status_terminated"



id: string



Unique identifier for this event.



processed_at: string



Timestamp of status change.

formatdate-time



BetaManagedAgentsSessionThreadCreatedEvent object{ type: "session.thread_created", id, agent_name, 2 more }



Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

type: "session.thread_created"



id: string



Unique identifier for this event.

agent_name: string



Name of the callable agent the thread runs.



processed_at: string



Timestamp when the thread was created.

formatdate-time

session_thread_id: string



Public `sthr_` ID of the newly created thread.



BetaManagedAgentsSessionThreadStatusIdleEvent object{ type: "session.thread_status_idle", id, agent_name, 3 more }



A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.



BetaManagedAgentsSessionThreadStatusRescheduledEvent object{ type: "session.thread_status_rescheduled", id, agent_name, 2 more }



A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

type: "session.thread_status_rescheduled"



id: string



Unique identifier for this event.

agent_name: string



Name of the agent the thread runs.



processed_at: string



Timestamp of the status transition.

formatdate-time

session_thread_id: string



Public sthr\_ ID of the thread that is retrying.



BetaManagedAgentsSessionThreadStatusRunningEvent object{ type: "session.thread_status_running", id, agent_name, 2 more }



A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

type: "session.thread_status_running"



id: string



Unique identifier for this event.

agent_name: string



Name of the agent the thread runs.



processed_at: string



Timestamp of the status transition.

formatdate-time

session_thread_id: string



Public sthr\_ ID of the thread that started running.



BetaManagedAgentsSessionThreadStatusTerminatedEvent object{ type: "session.thread_status_terminated", id, agent_name, 2 more }



A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

type: "session.thread_status_terminated"



id: string



Unique identifier for this event.

agent_name: string



Name of the agent the thread runs.



processed_at: string



Timestamp of the status transition.

formatdate-time

session_thread_id: string



Public sthr\_ ID of the thread that terminated.



BetaManagedAgentsSessionUsageSnapshot object{ active_seconds, cache_creation, cache_read_input_tokens, 4 more }



Point-in-time snapshot of a session's cumulative usage.



BetaManagedAgentsSpanModelRequestEndEvent object{ type: "span.model_request_end", id, is_error, 3 more }



Emitted when a model request completes.



BetaManagedAgentsSpanModelRequestStartEvent object{ type: "span.model_request_start", id, processed_at }



Emitted when a model request is initiated by the agent.

type: "span.model_request_start"



id: string



Unique identifier for this event.



processed_at: string



Timestamp when the model request started.

formatdate-time



BetaManagedAgentsSpanModelUsage object{ cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }



Token usage for a single model request.



cache_creation_input_tokens: number



Tokens used to create prompt cache in this request.

formatint32



cache_read_input_tokens: number



Tokens read from prompt cache in this request.

formatint32



input_tokens: number



Input tokens consumed by this request.

formatint32



output_tokens: number



Output tokens generated by this request.

formatint32



speed: optional "standard" or "fast" or null



Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active.

One of the following:

"standard"



"fast"





BetaManagedAgentsSpanOutcomeEvaluationEndEvent object{ type: "span.outcome_evaluation_end", id, explanation, 6 more }



Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.



BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object{ type: "span.outcome_evaluation_ongoing", id, iteration, 2 more }



Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

type: "span.outcome_evaluation_ongoing"



id: string



Unique identifier for this event.



iteration: number



0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

formatint32

outcome_id: string



The `outc_` ID of the outcome being evaluated.



processed_at: string



Timestamp when this heartbeat was emitted.

formatdate-time



BetaManagedAgentsSpanOutcomeEvaluationStartEvent object{ type: "span.outcome_evaluation_start", id, iteration, 2 more }



Emitted when an outcome evaluation cycle begins.

type: "span.outcome_evaluation_start"



id: string



Unique identifier for this event.



iteration: number



0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

formatint32

outcome_id: string



The `outc_` ID of the outcome being evaluated.



processed_at: string



Timestamp when outcome evaluation started.

formatdate-time



BetaManagedAgentsStreamSessionEvents = [BetaManagedAgentsUserMessageEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_message_event) or [BetaManagedAgentsUserInterruptEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_interrupt_event) or [BetaManagedAgentsUserToolConfirmationEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_tool_confirmation_event) or 34 more



Server-sent event in the session stream.

One of the following:



BetaManagedAgentsSystemMessageEventParams object{ type: "system.message", content }



Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

type: "system.message"





content: array of [BetaManagedAgentsSystemContentBlock](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_system_content_block) { type: "text", text }



System content blocks to append. Text-only.

type: "text"





text: string



The text content.

minLength1



BetaManagedAgentsTextBlock object{ type: "text", text }



Regular text content.

type: "text"





text: string



The text content.

minLength1



BetaManagedAgentsTextRubric object{ type: "text", content }



Rubric content provided inline as text.

type: "text"



content: string



Rubric content. Plain text or markdown — the grader treats it as freeform text.



BetaManagedAgentsTextRubricParams object{ type: "text", content }



Rubric content provided inline as text.

type: "text"





content: string



Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

maxLength262144



BetaManagedAgentsUnknownError object{ type: "unknown_error", message, retry_status }



An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.



BetaManagedAgentsURLDocumentSource object{ type: "url", url }



Document referenced by URL.

type: "url"





url: string



URL of the document to fetch.

minLength1



BetaManagedAgentsURLImageSource object{ type: "url", url }



Image referenced by URL.

type: "url"





url: string



URL of the image to fetch.

minLength1



BetaManagedAgentsUserCustomToolResultEvent object{ type: "user.custom_tool_result", id, custom_tool_use_id, 4 more }



Event sent by the client providing the result of a custom tool execution.



BetaManagedAgentsUserCustomToolResultEventParams object{ type: "user.custom_tool_result", custom_tool_use_id, content, is_error }



Parameters for providing the result of a custom tool execution.



BetaManagedAgentsUserDefineOutcomeEvent object{ type: "user.define_outcome", id, description, 4 more }



Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.



BetaManagedAgentsUserDefineOutcomeEventParams object{ type: "user.define_outcome", description, rubric, max_iterations }



Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.



BetaManagedAgentsUserInterruptEvent object{ type: "user.interrupt", id, processed_at, session_thread_id }



An interrupt event that pauses agent execution and returns control to the user.

type: "user.interrupt"



id: string



Unique identifier for this event.



processed_at: optional string or null



Timestamp when the interrupt was processed.

formatdate-time

session_thread_id: optional string or null



If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



BetaManagedAgentsUserInterruptEventParams object{ type: "user.interrupt", session_thread_id }



Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"



session_thread_id: optional string or null



If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



BetaManagedAgentsUserMessageEvent object{ type: "user.message", id, content, processed_at }



A user message event in the session conversation.



BetaManagedAgentsUserMessageEventParams object{ type: "user.message", content }



Parameters for sending a user message to the session.



BetaManagedAgentsUserToolConfirmationEvent object{ type: "user.tool_confirmation", id, result, 4 more }



A tool confirmation event that approves or denies a pending tool execution.



BetaManagedAgentsUserToolConfirmationEventParams object{ type: "user.tool_confirmation", result, tool_use_id, deny_message }



Parameters for confirming or denying a tool execution request.

type: "user.tool_confirmation"





result: "allow" or "deny"



The confirmation result: 'allow' or 'deny'.

One of the following:

"allow"



"deny"





tool_use_id: string



The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](beta-sessions-events-list.md#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

minLength1

maxLength128



deny_message: optional string or null



Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

maxLength10000



BetaManagedAgentsUserToolResultEventParams object{ type: "user.tool_result", tool_use_id, content, is_error }



Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.
