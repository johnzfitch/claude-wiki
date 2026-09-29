---
title: "List Events - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/events/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:42Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fsessions%2Fevents%2Flist)

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
4.  [Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events)

# List Events

GET/v1/sessions/{session_id}/events

List Events

##### Path parameters

session_id: string



##### Query parameters



"created_at\[gt\]": optional string



Return events created after this time (exclusive). Compared against the event's `processed_at` value.

formatdate-time



"created_at\[gte\]": optional string



Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

formatdate-time



"created_at\[lt\]": optional string



Return events created before this time (exclusive). Compared against the event's `processed_at` value.

formatdate-time



"created_at\[lte\]": optional string



Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

formatdate-time



limit: optional number



formatint32



order: optional "asc" or "desc"



Sort direction for results, ordered by the event's `processed_at`. Defaults to `asc` (chronological).

One of the following:

"asc"



"desc"



page: optional string



Opaque pagination cursor from a previous response's `next_page`.

types: optional array of string



Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](http-beta.md#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string





"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more



One of the following:

"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"





"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



data: optional array of [BetaManagedAgentsSessionEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_session_event)



Events for the session, ordered by `processed_at`.

One of the following:



BetaManagedAgentsUserMessageEvent object{ type: "user.message", id, content, processed_at }



A user message event in the session conversation.

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

BetaManagedAgentsUserToolConfirmationEvent object{ type: "user.tool_confirmation", id, result, 4 more }



A tool confirmation event that approves or denies a pending tool execution.



BetaManagedAgentsUserCustomToolResultEvent object{ type: "user.custom_tool_result", id, custom_tool_use_id, 4 more }



Event sent by the client providing the result of a custom tool execution.

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

BetaManagedAgentsAgentMCPToolUseEvent object{ type: "agent.mcp_tool_use", id, input, 6 more }



Event emitted when the agent invokes a tool provided by an MCP server.



BetaManagedAgentsAgentMCPToolResultEvent object{ type: "agent.mcp_tool_result", id, mcp_tool_use_id, 3 more }



Event representing the result of an MCP tool execution.



BetaManagedAgentsAgentToolUseEvent object{ type: "agent.tool_use", id, input, 5 more }



Event emitted when the agent invokes a built-in agent tool.



BetaManagedAgentsAgentToolResultEvent object{ type: "agent.tool_result", id, processed_at, 3 more }



Event representing the result of an agent tool execution.



BetaManagedAgentsAgentThreadMessageReceivedEvent object{ type: "agent.thread_message_received", id, content, 3 more }



Delivery event written to the target thread's input stream when an agent-to-agent message arrives.



BetaManagedAgentsAgentThreadMessageSentEvent object{ type: "agent.thread_message_sent", id, content, 3 more }



Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

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

BetaManagedAgentsSessionErrorEvent object{ type: "session.error", id, error, processed_at }



An error event indicating a problem occurred during session execution.

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

BetaManagedAgentsSessionStatusIdleEvent object{ type: "session.status_idle", id, processed_at, stop_reason }



Indicates the agent has paused and is awaiting user input.

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

BetaManagedAgentsSpanOutcomeEvaluationEndEvent object{ type: "span.outcome_evaluation_end", id, explanation, 6 more }



Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

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

BetaManagedAgentsSpanModelRequestEndEvent object{ type: "span.model_request_end", id, is_error, 3 more }



Emitted when a model request completes.

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

BetaManagedAgentsUserDefineOutcomeEvent object{ type: "user.define_outcome", id, description, 4 more }



Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

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

BetaManagedAgentsSessionThreadStatusIdleEvent object{ type: "session.thread_status_idle", id, agent_name, 3 more }



A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

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

BetaManagedAgentsUserToolResultEvent object{ type: "user.tool_result", id, tool_use_id, 4 more }



Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

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

BetaManagedAgentsSessionUpdatedEvent object{ type: "session.updated", id, processed_at, 4 more }



Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.



BetaManagedAgentsSystemMessageEvent object{ type: "system.message", id, content, processed_at }



A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

type: "system.message"



id: string



Unique identifier for this event.



content: array of [BetaManagedAgentsSystemContentBlock](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_system_content_block) { type: "text", text }



System content blocks. Text-only.

type: "text"





text: string



The text content.

minLength1



processed_at: optional string or null



Timestamp when this system message was processed.

formatdate-time



BetaManagedAgentsSessionUsageEvent object{ type: "session.usage", id, processed_at, 2 more }



Periodic snapshot of the session's cumulative usage and tracked list cost.

next_page: optional string or null



Opaque cursor for the next page. Null when no more results.

List Events

cURL



```python
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
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
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
