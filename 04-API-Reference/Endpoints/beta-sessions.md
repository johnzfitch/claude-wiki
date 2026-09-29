---
title: "Sessions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:46Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fsessions)

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

# Sessions

##### [Create Session](https://platform.claude.com/docs/en/api/http/beta/sessions/create)

POST/v1/sessions

##### [List Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions/list)

GET/v1/sessions

##### [Get Session](https://platform.claude.com/docs/en/api/http/beta/sessions/retrieve)

GET/v1/sessions/{session_id}

##### [Update Session](https://platform.claude.com/docs/en/api/http/beta/sessions/update)

POST/v1/sessions/{session_id}

##### [Delete Session](https://platform.claude.com/docs/en/api/http/beta/sessions/delete)

DELETE/v1/sessions/{session_id}

##### [Archive Session](https://platform.claude.com/docs/en/api/http/beta/sessions/archive)

POST/v1/sessions/{session_id}/archive

##### Models



BetaManagedAgentsAdvisorParams object{ type: "advisor", model }



Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

type: "advisor"





model: string



A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

minLength1

maxLength256



BetaManagedAgentsAgentMessagePreview object{ type: "agent.message", id }



type: "agent.message"



id: string



The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.



BetaManagedAgentsAgentParams object{ type: "agent", id, version }



Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

type: "agent"





id: string



The `agent` ID.

minLength1

maxLength128



version: optional number



The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

formatint32



BetaManagedAgentsAgentThinkingPreview object{ type: "agent.thinking", id }



type: "agent.thinking"



id: string



The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.



BetaManagedAgentsAgentWithOverridesParams object{ type: "agent_with_overrides", id, mcp_servers, 5 more }



Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.



BetaManagedAgentsBranchCheckout object{ type: "branch", name }



type: "branch"





name: string



Branch name to check out.

minLength1

maxLength255



BetaManagedAgentsBudgetLimit object{ type: "limit", max_list_cost }



A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

type: "limit"





max_list_cost: [BetaMonetaryAmount](http-beta.md#beta_monetary_amount) { amount, currency }



Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

amount: string



Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is \$25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

currency: [BetaCurrency](http-beta.md#beta_currency)



Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.



BetaManagedAgentsCacheCreationUsage object{ ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }



Prompt-cache creation token usage broken down by cache lifetime.



ephemeral_1h_input_tokens: optional number



Tokens used to create 1-hour ephemeral cache entries.

formatint32



ephemeral_5m_input_tokens: optional number



Tokens used to create 5-minute ephemeral cache entries.

formatint32



BetaManagedAgentsCommitCheckout object{ type: "commit", sha }



type: "commit"





sha: string



Full commit SHA to check out.

minLength7

maxLength64



BetaManagedAgentsDeletedSession object{ type: "session_deleted", id }



Confirmation that a `session` has been permanently deleted.

type: "session_deleted"



id: string





BetaManagedAgentsDeltaContent object{ type: "content_delta", content, index }



type: "content_delta"





content: [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_text_block) { type: "text", text }



A partial element of the content array at index, typed like the element itself — the same shape the buffered agent.message carries in content.

type: "text"





text: string



The text content.

minLength1

index: optional number



Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.



BetaManagedAgentsDeltaEvent object{ type: "event_delta", delta, event_id }



An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.



BetaManagedAgentsDeltaType = "agent.message" or "agent.thinking"



EventDeltaType enum

One of the following:

"agent.message"



"agent.thinking"





BetaManagedAgentsFileResourceParams object{ type: "file", file_id, mount_path }



Mount a file uploaded via the Files API into the session.

type: "file"





file_id: string



ID of a previously uploaded file.

minLength1

maxLength128



mount_path: optional string or null



Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

minLength1

maxLength4096



BetaManagedAgentsGitHubRepositoryResourceParams object{ type: "github_repository", url, authorization_token, 2 more }



Mount a GitHub repository into the session's container.



BetaManagedAgentsMemoryStoreResourceParam object{ type: "memory_store", memory_store_id, access, instructions }



Parameters for attaching a memory store to an agent session.

type: "memory_store"



memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.



access: optional "read_write" or "read_only" or null



Access mode for the mounted store. Defaults to read_write. read_only mounts the store as a read-only filesystem.

One of the following:

"read_write"



"read_only"





instructions: optional string or null



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

maxLength4096



BetaManagedAgentsMultiagent object{ type: "coordinator", agents }



Resolved multiagent orchestration configuration as returned in API responses.



BetaManagedAgentsMultiagentParams object{ type: "coordinator", agents }



Multiagent orchestration configuration. Currently supports the `coordinator` topology.



BetaManagedAgentsMultiagentRosterEntryParams = string or [BetaManagedAgentsAgentParams](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_agent_params) or [BetaManagedAgentsMultiagentSelfParams](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_multiagent_self_params) or [BetaManagedAgentsAdvisorParams](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_advisor_params)



An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

One of the following:



BetaManagedAgentsOutcomeEvaluationResource object{ type: "outcome_evaluation", completed_at, description, 4 more }



Evaluation state for a single outcome defined via a `define_outcome` event.

type: "outcome_evaluation"





completed_at: string or null



When the outcome reached a terminal result. Null while `pending`/`running`/`evaluating`.

formatdate-time

description: string



What the agent should produce.

explanation: string or null



Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.



iteration: number



0-indexed revision cycle the outcome is currently on.

formatint32

outcome_id: string



Server-generated outc\_ ID for this outcome.

result: string



Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.



BetaManagedAgentsServerToolUsage object{ web_fetch_requests, web_search_requests }



Cumulative count of server-executed tool invocations, broken down by tool.



web_fetch_requests: optional number



Number of server-executed web fetch requests.

formatint32



web_search_requests: optional number



Number of server-executed web search requests.

formatint32



BetaManagedAgentsSession object{ type: "session", id, agent, 14 more }



A Managed Agents `session`.



BetaManagedAgentsSessionAgent object{ type: "agent", id, description, 8 more }



Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.



BetaManagedAgentsSessionAgentUpdate object{ mcp_servers, tools }



Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.



BetaManagedAgentsSessionMultiagentCoordinator object{ type: "coordinator", agents }



Resolved coordinator topology with full agent definitions for each roster member.

type: "coordinator"





agents: array of [BetaManagedAgentsSessionThreadAgent](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_session_thread_agent) or [BetaManagedAgentsAdvisor](https://platform.claude.com/docs/en/api/http/beta/agents#beta_managed_agents_advisor)



Full `agent` definitions the coordinator may spawn as session threads.

One of the following:



BetaManagedAgentsSessionThreadAgent object{ type: "agent", id, description, 7 more }



Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.



BetaManagedAgentsAdvisor object{ type: "advisor", model }



Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

type: "advisor"



model: string



The advisor model id.



BetaManagedAgentsSessionStats object{ active_seconds, duration_seconds }



Timing statistics for a session.



active_seconds: optional number



Cumulative time in seconds the session spent in `running` status. Excludes idle time.

formatdouble



duration_seconds: optional number



Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

formatdouble



BetaManagedAgentsSessionUpdatedEvent object{ type: "session.updated", id, processed_at, 4 more }



Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.



BetaManagedAgentsSessionUsage object{ active_seconds, cache_creation, cache_read_input_tokens, 4 more }



Cumulative token usage for a session across all turns.



BetaManagedAgentsSessionUsageEvent object{ type: "session.usage", id, processed_at, 2 more }



Periodic snapshot of the session's cumulative usage and tracked list cost.



BetaManagedAgentsStartEvent object{ type: "event_start", event }



Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.



BetaManagedAgentsStartEventPreview = [BetaManagedAgentsAgentMessagePreview](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_agent_message_preview) or [BetaManagedAgentsAgentThinkingPreview](https://platform.claude.com/docs/en/api/http/beta/sessions#beta_managed_agents_agent_thinking_preview)



One of the following:



BetaManagedAgentsAgentMessagePreview object{ type: "agent.message", id }



type: "agent.message"



id: string



The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.



BetaManagedAgentsAgentThinkingPreview object{ type: "agent.thinking", id }



type: "agent.thinking"



id: string



The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.



BetaManagedAgentsSystemContentBlock object{ type: "text", text }



Content block in a mid-conversation system message. Text-only.

type: "text"





text: string



The text content.

minLength1

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

BetaManagedAgentsUserToolResultEvent object{ type: "user.tool_result", id, tool_use_id, 4 more }



Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

#### Sessions[Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events)

##### [List Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/list)

GET/v1/sessions/{session_id}/events

##### [Send Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/send)

POST/v1/sessions/{session_id}/events

##### [Stream Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/stream)

GET/v1/sessions/{session_id}/events/stream

#### Sessions[Resources](https://platform.claude.com/docs/en/api/http/beta/sessions/resources)

##### [Add Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

##### [List Session Resources](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

##### [Get Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

##### [Update Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

##### [Delete Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

#### Sessions[Threads](https://platform.claude.com/docs/en/api/http/beta/sessions/threads)

##### [List Session Threads](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/list)

GET/v1/sessions/{session_id}/threads

##### [Get Session Thread](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/retrieve)

GET/v1/sessions/{session_id}/threads/{thread_id}

##### [Archive Session Thread](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/archive)

POST/v1/sessions/{session_id}/threads/{thread_id}/archive

#### SessionsThreads[Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events)

##### [List Session Thread Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events/list)

GET/v1/sessions/{session_id}/threads/{thread_id}/events

##### [Stream Session Thread Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events/stream)

GET/v1/sessions/{session_id}/threads/{thread_id}/stream
