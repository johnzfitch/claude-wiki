---
title: "OpenTelemetry span reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/opentelemetry/spans"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-22T06:28:19Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fopentelemetry%2Fspans)

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


Organization


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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations

Webhooks


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


Compliance API

Activities

Organizations

Groups

Apps


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[AWS IAM actions](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[Migrating to API version 2026-10-21](migration-2026-10-21.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

[API reference](overview.md)OpenTelemetry

[OpenTelemetry](../Other/manage-claude-opentelemetry.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

# OpenTelemetry span reference

Copy page



The OpenTelemetry spans and span attributes that the Claude API and the Claude SDK emit.

Copy page





OpenTelemetry export is in beta. It's provided under your agreement with Anthropic, including the Beta Services section of the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Span names and attributes can change during the beta.

To get spans, see [Set up OpenTelemetry with the Claude SDK](../Other/manage-claude-opentelemetry-sdk.md) and [Set up OpenTelemetry with the Claude API](../Other/manage-claude-opentelemetry-api.md).

## Span names and kinds

| Property              | SDK spans                                                                                                                              | API spans                                                |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `service.name`        | The application's `service.name`                                                                                                       | `claude-platform`                                        |
| Instrumentation scope | `com.anthropic.sdk.<language>` or `com.anthropic.sdk.cli`, plus `.<platform>` on a cloud platform's client, with the package's version | `com.anthropic.claude-platform`                          |
| Span kind             | `CLIENT` on the span for a request, `INTERNAL` otherwise                                                                               | `SERVER` on the span for a request, `INTERNAL` otherwise |

- **Spans for requests** have the name of the request's API method: `anthropic.` followed by the method's path in the API reference, with dots instead of slashes and without `beta`. For example, `client.beta.sessions.events.send()` sends a request to [send session events](beta-sessions-events-send.md), and its spans have the name [`anthropic.sessions.events.send`](#anthropic-sessions-events-send).
- **Tool spans** have a fixed name, a space, and the tool name, for example [`anthropic.tool_use bash`](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use).

## Span status

- **`OK`:** The step completed.
- **`ERROR`:** The step failed.
- **Unset:** The application canceled the step, for example when it sent a [`user.interrupt`](beta-sessions-events.md#beta_managed_agents_user_interrupt_event) event.

A stream's span ends when the stream ends. If the application closes the stream early, the SDK span has the status unset, so the SDK span for a stream that never completes, such as [`anthropic.sessions.events.stream`](#anthropic-sessions-method), has the status unset or `ERROR`.

## Attributes

Attributes use the [OpenTelemetry semantic conventions for generative AI](https://github.com/open-telemetry/semantic-conventions-genai) (`gen_ai.*`) where one exists. Anthropic attributes start with `anthropic.`. The spans follow the conventions at commit [`e57c543b`](https://github.com/open-telemetry/semantic-conventions-genai/tree/e57c543b4889619eb2a05702471937db5119165d) of September 24, 2026. The conventions are still in development.

### Common attributes

Every span for a request has the following attributes, except where a description says otherwise. Other spans can have only the first three:

[TABLE]

On Claude Platform on AWS, API spans don't have `server.address`, `server.port`, or `url.full`.

### Session attributes

In a Managed Agents session, spans have the following attributes. A session's spans can be in more than one trace, so to assemble a view of the session, such as a transcript, [group its spans by these IDs](../Other/manage-claude-opentelemetry.md#a-managed-agents-session).

| Attribute                | Type     | Description                                                                                                                                                                                                                                                                                                                                    |
|--------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `anthropic.session.id`   | `string` | The session ID. Absent on the spans for methods that don't act on one session, such as [`anthropic.sessions.list`](#anthropic-sessions-method).                                                                                                                                                                                                |
| `gen_ai.conversation.id` | `string` | The ID of the session thread that the span belongs to. The SDK's [`conversation_id` option](../Other/manage-claude-opentelemetry-sdk.md#configure-the-sdk) replaces it with your own conversation ID. Absent on SDK spans with no thread unless you set the option, and on API spans for Sessions API requests other than requests to one thread. |

### Content attributes

Attributes tagged with Content are only on spans in content mode, from the SDK and the API alike. See [how the content modes differ in the guide](../Other/manage-claude-opentelemetry.md#choose-a-content-mode). When this content is too large, the SDK and the API shorten it to fit the [content limits](../Other/manage-claude-opentelemetry.md#content-limits) and set `anthropic.content.truncated` to `true`. If Anthropic's safeguards withhold content from a response, the API's spans don't include that content either.

The message attributes are JSON strings in the message format of the OpenTelemetry GenAI conventions. Each Anthropic content block becomes one GenAI conventions message part, on the Messages API and in Managed Agents message events such as `agent.message`:

| Anthropic content block                                                                         | GenAI conventions message part                                                                                                                               |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `text`                                                                                          | `text`                                                                                                                                                       |
| `tool_use`, `server_tool_use`                                                                   | `tool_call`, with `anthropic_toolset_name` for a `tool_use` block that has a `toolset_name`, such as `computer`                                              |
| `mcp_tool_use`                                                                                  | `tool_call` with `anthropic_mcp_server_name`                                                                                                                 |
| `tool_result`, `mcp_tool_result`, a server tool's result block such as `web_search_tool_result` | `tool_call_response`                                                                                                                                         |
| `thinking`                                                                                      | `reasoning`, without the `thinking` block's signature. Not in Managed Agents spans, because the `agent.thinking` event doesn't include the thinking content. |
| Any other block, such as `image`                                                                | The block's `type` with the prefix `anthropic_`, such as `anthropic_image`. The part has no other fields.                                                    |

Each Managed Agents tool use or tool result event also becomes one GenAI conventions message part:

| Managed Agents event                                                                        | GenAI conventions message part               |
|---------------------------------------------------------------------------------------------|----------------------------------------------|
| `agent.tool_use`, `agent.custom_tool_use`                                                   | `tool_call`                                  |
| `agent.mcp_tool_use`                                                                        | `tool_call` with `anthropic_mcp_server_name` |
| `user.tool_result`, `user.custom_tool_result`, `agent.tool_result`, `agent.mcp_tool_result` | `tool_call_response`                         |

### Token usage

The following spans have token usage attributes: [`anthropic.messages.create`](#anthropic-messages-create), [`anthropic.model_request`](#anthropic-model-request), [`anthropic.compaction`](#anthropic-compaction), and [`anthropic.session.outcome_evaluation`](#anthropic-session-outcome-evaluation). The values are for each span's step, for example the request, the model request, or the compaction. To count each token once, see [how to count tokens in the guide](../Other/manage-claude-opentelemetry.md#count-tokens).

| Attribute                                                  | Type  | Description                                                                                                                                                                       |
|------------------------------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `gen_ai.usage.input_tokens`                                | `int` | The input tokens, cache reads and writes included.                                                                                                                                |
| `gen_ai.usage.output_tokens`                               | `int` | The output tokens.                                                                                                                                                                |
| `gen_ai.usage.cache_write.input_tokens`                    | `int` | The tokens written to the prompt cache. Absent on [`anthropic.session.outcome_evaluation`](#anthropic-session-outcome-evaluation) spans.                                          |
| `anthropic.usage.cache_creation.ephemeral_5m_input_tokens` | `int` | The tokens written to the 5-minute cache. Only on the spans for Messages API requests. On a streaming response's SDK span, only the tokens written before the first output token. |
| `anthropic.usage.cache_creation.ephemeral_1h_input_tokens` | `int` | The tokens written to the 1-hour cache. Only on the spans for Messages API requests. On a streaming response's SDK span, only the tokens written before the first output token.   |
| `gen_ai.usage.cache_read.input_tokens`                     | `int` | The tokens read from the prompt cache. Absent on [`anthropic.session.outcome_evaluation`](#anthropic-session-outcome-evaluation) spans.                                           |

## Spans

A span can come from the SDK in the application or from the API, so each span in this reference lists its sources. Descriptions that start with **Messages API:** or **Managed Agents:** are for that product's spans. Attribute descriptions that start with a source, such as **SDK:** or **API:**, are for that source's spans.

### `anthropic.messages.create`

- **Source:** The SDK and the API.
- **Kind:** `CLIENT` from the SDK, `SERVER` from the API.
- **Parent of the SDK span:** The span that is current in the application when it calls the method. If no span is current, there's no parent.
- **Parent of the API span:** The span in the request's `traceparent` header, which is the SDK span when the request comes from the SDK. Without the header, the API span has no parent. See [how to send the `traceparent` header](../Other/manage-claude-opentelemetry-api.md#connect-api-spans-to-your-own-traces).
- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** An [`anthropic.model_request`](#anthropic-model-request) span for each model request, a [tool span](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) for each use of a server tool or an MCP connector tool that the API runs in the request, and an [`anthropic.compaction`](#anthropic-compaction) span for each compaction.

The SDK emits this span for each Messages request, streamed or not.

The API emits this span for each [`POST /v1/messages`](messages-create.md) request that it authenticates. It doesn't emit the span for a request to the [OpenAI-compatible endpoint](../Other/cli-sdks-libraries-libraries-openai-sdk.md), `POST /v1/chat/completions`.

The API emits one span for a request, even when a [fallback model](../Guides/build-with-claude-refusals-and-fallback.md) serves it.

The span has the [token usage attributes](#token-usage). The SDK span also has the attributes of every [SDK span for a request](#anthropic-resources-method).

[TABLE]

A request's spans don't have the response's server tool usage counts, such as `web_search_requests`. Instead, the API emits a [tool span](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) for each use of a server tool.

### `anthropic.messages.count_tokens`

- **Source:** The SDK. The API doesn't emit a span for [`POST /v1/messages/count_tokens`](platform-claude-com-messages-count-tokens.md).
- **Kind:** `CLIENT`.
- **Parent:** The span that is current in the application when it calls the method, or none if no span is current.
- **Children:** None.

| Attribute                                     | Type     | Description                                                                                         |
|-----------------------------------------------|----------|-----------------------------------------------------------------------------------------------------|
| `gen_ai.request.model`                        | `string` | The request's model.                                                                                |
| `anthropic.message.count_tokens.input_tokens` | `int`    | The token count in the response. This count isn't usage. Don't include it when you sum token usage. |

### `anthropic.sessions.create`

The same as [`anthropic.sessions.<method>`](#anthropic-sessions-method), except for the following children and attributes:

- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** The first turn's [`anthropic.session.turn`](#anthropic-session-turn) span, when the request has non-empty [`initial_events`](beta-sessions-create.md#create.initial_events).

[TABLE]

### `anthropic.sessions.events.send`

The same as [`anthropic.sessions.<method>`](#anthropic-sessions-method), except for the API span's children.

- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** The [`anthropic.session.turn`](#anthropic-session-turn) span for each turn that starts because of the request's events.

### `anthropic.sessions.update`

The same as [`anthropic.sessions.<method>`](#anthropic-sessions-method), except for the API span's children.

- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** The [`anthropic.session.turn`](#anthropic-session-turn) span for each turn that resumes because the request raises or removes the [session budget](../Other/managed-agents-budgets.md#resume-a-session-at-its-budget).

### `anthropic.session.turn`

- **Source:** The API, for Managed Agents sessions.
- **Kind:** `INTERNAL`.
- **Parent:** It depends on why the turn started:
  - The [`anthropic.sessions.create`](#anthropic-sessions-create) span, for the first turn of a session that was created with non-empty [`initial_events`](beta-sessions-create.md#create.initial_events).
  - The [`anthropic.sessions.events.send`](#anthropic-sessions-events-send) span for the request in which the event was sent, for a turn that started because of an event, for example a [`user.message`](beta-sessions-events.md#beta_managed_agents_user_message_event) event.
  - The [`anthropic.sessions.update`](#anthropic-sessions-update) span, for a turn that resumes because the request raises or removes the session budget.
  - The `anthropic.session.turn` span for the turn of [the agent that the session runs](../Other/managed-agents-multiagent-orchestration.md) during which that agent started this turn, for a turn on another thread.
  - The `anthropic.session.turn` span for the turn that produced the reply, for a turn that starts because an agent on another thread replied, such as an agent that the primary agent called.
  - None, for any other turn, such as a turn that starts because a [workflow run](../Other/managed-agents-workflow-runs.md) ended.
- **Children:**
  - An [`anthropic.model_request`](#anthropic-model-request) span for each model request in the turn.
  - A tool span each time the API runs a tool in the turn, except in the [cases listed in the tool span section](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use).
  - An `anthropic.session.turn` span for each turn on another thread that was started during this turn by the agent that the session runs, or by this turn's reply.
  - An [`anthropic.session.outcome_evaluation`](#anthropic-session-outcome-evaluation) span for each iteration of an outcome evaluation that this turn starts.

A turn starts when its thread enters the `running` state and ends when the thread leaves it.

| Attribute                            | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `gen_ai.operation.name`              | `string` | `invoke_agent`                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `gen_ai.agent.id`                    | `string` | The ID of the agent that runs the turn's thread. Absent on an [advisor](../Other/managed-agents-multiagent-orchestration.md#advisor-threads) thread.                                                                                                                                                                                                                                                                                                                       |
| `gen_ai.agent.name`                  | `string` | That agent's name. `anthropic.advisor` on an advisor thread.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `gen_ai.request.model`               | `string` | That agent's model. On an advisor thread, the advisor's model.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `anthropic.session.turn.stop_reason` | `string` | Why the turn ended: the [`session.thread_status_idle`](beta-sessions-events.md#beta_managed_agents_session_thread_status_idle_event) event's [`stop_reason.type`](beta-sessions-events.md#beta_managed_agents_session_thread_status_idle_event), for example `requires_action`. Absent when the thread didn't go idle.                                                                                                                              |
| `error.type`                         | `string` | The [`error.type`](beta-sessions-events.md#beta_managed_agents_session_error_event) of the [`session.error`](beta-sessions-events.md#beta_managed_agents_session_error_event) event that ended the turn, if the turn failed.                                                                                                                                                                                                                        |
| `gen_ai.agent.description`           | `string` | That agent's description. Absent on an advisor thread or when the agent doesn't have one.                                                                                                                                                                                                                                                                                                                                                                               |
| `gen_ai.system_instructions`         | `string` | Content A JSON string that follows the OpenTelemetry [`SystemInstructions`](https://github.com/open-telemetry/semantic-conventions-genai/blob/e57c543b4889619eb2a05702471937db5119165d/model/gen-ai/gen-ai-system-instructions.json) schema. The system prompt in effect for the turn. Only on a thread's first turn. Absent on an advisor thread.                                                                                                                      |
| `gen_ai.input.messages`              | `string` | Content A JSON string that follows the OpenTelemetry [`InputMessages`](https://github.com/open-telemetry/semantic-conventions-genai/blob/e57c543b4889619eb2a05702471937db5119165d/model/gen-ai/gen-ai-input-messages.json) schema. The turn's input events: user messages and tool results, [`system.message`](beta-sessions-events.md#beta_managed_agents_system_message_event_params) events, and messages from other threads. Absent on an advisor thread. |
| `gen_ai.output.messages`             | `string` | Content A JSON string that follows the OpenTelemetry [`OutputMessages`](https://github.com/open-telemetry/semantic-conventions-genai/blob/e57c543b4889619eb2a05702471937db5119165d/model/gen-ai/gen-ai-output-messages.json) schema. The turn's output events: the agent's messages, tool uses, and tool results.                                                                                                                                                       |

### `anthropic.model_request`

- **Source:** The API, for Messages API requests and Managed Agents sessions.
- **Kind:** `INTERNAL`.
- **Parent:**
  - **Messages API:** The [`anthropic.messages.create`](#anthropic-messages-create) span for the request.
  - **Managed Agents:** The [`anthropic.session.turn`](#anthropic-session-turn) span for the turn that makes the request.
- **Children:** None.

On the Messages API, each span is one model request within the API request.

The span has the [token usage attributes](#token-usage).

[TABLE]

### `anthropic.tool_use`, `anthropic.mcp_tool_use`, and `anthropic.custom_tool_use`

- **Source:** The SDK and the API.
- **Name:** `anthropic.tool_use <tool>`, `anthropic.mcp_tool_use <tool>`, or `anthropic.custom_tool_use <tool>`, where `<tool>` is the tool's name.
- **Kind:** `INTERNAL`.
- **Parent of the SDK span:** The span that is current in the application when the tool starts, which in the Messages tool runner is the [`anthropic.messages.tool_runner`](#anthropic-messages-tool-runner) span. If no span is current, there's no parent.
- **Parent of the API span:**
  - **Messages API:** The [`anthropic.messages.create`](#anthropic-messages-create) span for the request in which the API runs the tool.
  - **Managed Agents:** The [`anthropic.session.turn`](#anthropic-session-turn) span for the turn in which the tool runs. For a tool use that waits for a [`user.tool_confirmation`](beta-sessions-events.md#beta_managed_agents_user_tool_confirmation_event) event, that is the turn that starts because of the confirmation.
  - For a tool use from code that another tool runs, the tool span for that tool. On the Messages API, that tool is the [code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md).
- **Children of the SDK span:** The spans that the tool's code starts.
- **Children of the API span:** A tool span for each tool use from the code that this tool runs. For example, code that the code execution tool runs might use `web_search`.

The span name prefix depends on the type of tool:

- `anthropic.tool_use <tool>` is the span for each use of a [server tool](../Agents-Tools/agents-and-tools-tool-use-server-tools.md) on the Messages API or of a tool from the agent toolset of Managed Agents. The API runs the agent toolset tools, except in a [self-hosted sandbox](../Other/manage-claude-opentelemetry-sdk.md#trace-a-self-hosted-sandbox), where the environment worker runs them.
- `anthropic.mcp_tool_use <tool>` is the span for each use of an MCP tool, in the SDK, on the Messages API, and on Managed Agents. In the SDK, it's a tool from an MCP helper that the [Messages tool runner](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md) or the [session tool runner](../Other/managed-agents-self-hosted-sandboxes-reference.md#session-tool-runner) runs. On the Messages API, the tool comes from the [MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md). On Managed Agents, if the [connection to the MCP server fails](../Other/managed-agents-mcp-connector.md#handle-connection-and-authentication-failures), the span name doesn't include the tool name.
- `anthropic.custom_tool_use <tool>` is the span for each use of a tool that the application defines and a tool runner runs. Only the SDK emits this span.

The API doesn't emit a tool span in the following cases:

- The model asks to use a tool that the application runs, such as a [custom tool](../Other/managed-agents-tools.md). If a tool runner in the SDK runs the tool, the tool runner emits its span.
- **Managed Agents:** The agent uses a tool that runs in a self-hosted sandbox. The worker in the SDK, which runs the tool, emits its span. See [how to trace a self-hosted sandbox](../Other/manage-claude-opentelemetry-sdk.md#trace-a-self-hosted-sandbox).
- **Managed Agents:** The agent uses a [multiagent](../Other/managed-agents-multiagent-orchestration.md) tool or the [advisor tool](../Other/managed-agents-multiagent-orchestration.md#give-the-session-an-advisor).
- **Managed Agents:** The agent asks to use a tool, but the server denies the use under the [`auto` permission policy](../Other/managed-agents-permission-policies.md#let-the-server-evaluate-each-call-with-auto), or the application denies it in a [`user.tool_confirmation`](beta-sessions-events.md#beta_managed_agents_user_tool_confirmation_event) event.

[TABLE]

### `anthropic.compaction`

- **Source:** The API, for Messages API requests.
- **Kind:** `INTERNAL`.
- **Parent:** The [`anthropic.messages.create`](#anthropic-messages-create) span for the request.
- **Children:** None.

The span has the compaction's [token usage attributes](#token-usage). On [`anthropic.messages.create`](#anthropic-messages-create), a compaction's usage is in the `anthropic.usage.compaction.*` attributes instead of the `gen_ai.usage.*` totals.

| Attribute    | Type     | Description                                                                                               |
|--------------|----------|-----------------------------------------------------------------------------------------------------------|
| `error.type` | `string` | The request's [error type](errors.md#http-errors), if the request failed during the compaction. |

### `anthropic.session.outcome_evaluation`

- **Source:** The API, for Managed Agents sessions.
- **Kind:** `INTERNAL`.
- **Parent:** The [`anthropic.session.turn`](#anthropic-session-turn) span for the turn that started the iteration, even if that turn ends before the iteration.
- **Children:** None.

The status is unset when the result is `interrupted` and `OK` for any other result.

The span has two of the [token usage attributes](#token-usage): `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens`.

| Attribute                                          | Type     | Description                                                                                                  |
|----------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------|
| `anthropic.session.outcome.id`                     | `string` | The ID of the outcome that the iteration evaluates.                                                          |
| `anthropic.session.outcome_evaluation.result`      | `string` | The iteration's result: `satisfied`, `needs_revision`, `max_iterations_reached`, `failed`, or `interrupted`. |
| `anthropic.session.outcome_evaluation.iteration`   | `int`    | The iteration number.                                                                                        |
| `anthropic.session.outcome_evaluation.explanation` | `string` | Content The grader's explanation of the result, as plain text.                                               |

### `anthropic.messages.tool_runner`

- **Source:** The SDK.
- **Kind:** `INTERNAL`.
- **Parent:** The span that is current in the application when the loop starts, or none if no span is current.
- **Children:** The [`anthropic.messages.create`](#anthropic-messages-create) span for each request in the loop and the [tool span](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) for each tool use that the runner runs.

The span ends with the loop. If the application stops the runner, the status is unset. If a tool's code raises an error, its tool span has the status `ERROR` and the loop continues. The span doesn't have usage attributes, so read the usage from its [`anthropic.messages.create`](#anthropic-messages-create) children.

| Attribute                | Type     | Description                                                                                                                                             |
|--------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `gen_ai.operation.name`  | `string` | `invoke_agent`                                                                                                                                          |
| `gen_ai.request.model`   | `string` | The model of the loop's first request.                                                                                                                  |
| `gen_ai.conversation.id` | `string` | The conversation ID passed with the [`conversation_id` option](../Other/manage-claude-opentelemetry-sdk.md#configure-the-sdk). Absent without one.         |
| `error.type`             | `string` | The [error type](errors.md#http-errors) of the request that ended the loop, if the loop failed. `client_error` when the runner itself failed. |
| `gen_ai.output.type`     | `string` | `json` when the requests set the output format to JSON. Absent otherwise.                                                                               |

### `anthropic.messages.batches.<method>`

- **Source:** The SDK, for every Message Batches method.
- **Kind:** `CLIENT`.
- **Parent:** The span that is current in the application when it calls the method, or none if no span is current.
- **Children:** None.

The spans also have the attributes of every [SDK span for a request](#anthropic-resources-method).

| Attribute                               | Type     | Description                                                                                                               |
|-----------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------|
| `anthropic.message.batch.id`            | `string` | The ID of the batch that the method acts on, or of the new batch for `create`. Absent on `list` and on a failed `create`. |
| `anthropic.message.batch.request_count` | `int`    | Only on `create`. The number of items in the [`requests`](messages-batches-create.md#create.requests) array.    |

### `anthropic.sessions.<method>`

- **Source:** The SDK and the API.
- **Kind:** `CLIENT` from the SDK, `SERVER` from the API.
- **Parent of the SDK span:** The span that is current in the application when it calls the method, or none if no span is current.
- **Parent of the API span:** The span in the request's [`traceparent` header](../Other/manage-claude-opentelemetry-api.md#connect-api-spans-to-your-own-traces), which is the SDK span when the request comes from the SDK, or none without the header.
- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** None.

The API emits an `anthropic.sessions.<method>` span for each authenticated request to an endpoint of the [Sessions API](../Other/managed-agents-sessions.md). Requests that the platform sends on a user's behalf, such as a message sent in the Claude Console or a session that a [scheduled deployment](../Other/managed-agents-scheduled-deployments.md) starts, also have one, each in a new trace.

### Span names and endpoints

| Span                                       | Endpoint                                                                                                       |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `anthropic.sessions.create`                | [`POST /v1/sessions`](beta-sessions-create.md)                                                       |
| `anthropic.sessions.list`                  | [`GET /v1/sessions`](beta-sessions-list.md)                                                          |
| `anthropic.sessions.retrieve`              | [`GET /v1/sessions/{session_id}`](beta-sessions-retrieve.md)                                         |
| `anthropic.sessions.update`                | [`POST /v1/sessions/{session_id}`](beta-sessions-update.md)                                          |
| `anthropic.sessions.delete`                | [`DELETE /v1/sessions/{session_id}`](beta-sessions-delete.md)                                        |
| `anthropic.sessions.archive`               | [`POST /v1/sessions/{session_id}/archive`](beta-sessions-archive.md)                                 |
| `anthropic.sessions.events.send`           | [`POST /v1/sessions/{session_id}/events`](beta-sessions-events-send.md)                              |
| `anthropic.sessions.events.list`           | [`GET /v1/sessions/{session_id}/events`](beta-sessions-events-list.md)                               |
| `anthropic.sessions.events.stream`         | [`GET /v1/sessions/{session_id}/events/stream`](beta-sessions-events-stream.md)                      |
| `anthropic.sessions.resources.add`         | [`POST /v1/sessions/{session_id}/resources`](beta-sessions-resources-add.md)                         |
| `anthropic.sessions.resources.list`        | [`GET /v1/sessions/{session_id}/resources`](beta-sessions-resources-list.md)                         |
| `anthropic.sessions.resources.retrieve`    | [`GET /v1/sessions/{session_id}/resources/{resource_id}`](beta-sessions-resources-retrieve.md)       |
| `anthropic.sessions.resources.update`      | [`POST /v1/sessions/{session_id}/resources/{resource_id}`](beta-sessions-resources-update.md)        |
| `anthropic.sessions.resources.delete`      | [`DELETE /v1/sessions/{session_id}/resources/{resource_id}`](beta-sessions-resources-delete.md)      |
| `anthropic.sessions.threads.list`          | [`GET /v1/sessions/{session_id}/threads`](beta-sessions-threads-list.md)                             |
| `anthropic.sessions.threads.retrieve`      | [`GET /v1/sessions/{session_id}/threads/{thread_id}`](beta-sessions-threads-retrieve.md)             |
| `anthropic.sessions.threads.archive`       | [`POST /v1/sessions/{session_id}/threads/{thread_id}/archive`](beta-sessions-threads-archive.md)     |
| `anthropic.sessions.threads.events.list`   | [`GET /v1/sessions/{session_id}/threads/{thread_id}/events`](beta-sessions-threads-events-list.md)   |
| `anthropic.sessions.threads.events.stream` | [`GET /v1/sessions/{session_id}/threads/{thread_id}/stream`](beta-sessions-threads-events-stream.md) |

The span has the [session attributes](#session-attributes). The SDK span also has the attributes of every [SDK span for a request](#anthropic-resources-method).

[TABLE]

### `anthropic.environment.work`

- **Source:** The CLI and the SDK in Python, TypeScript, and Go.
- **Kind:** `INTERNAL`.
- **Parent:** The span that is current in the application when the environment worker or the work poller gets the work item, or none if no span is current. In `ant beta:worker poll`, the span is a root span.
- **Children:** The spans for the requests that the environment worker sends while it handles the work item and the [tool span](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) for each tool that it runs for the work item.

The environment worker and the work poller are the [SDK helpers](../Other/managed-agents-self-hosted-sandboxes.md#sdk-helpers) that claim work items in a self-hosted sandbox. They emit one `anthropic.environment.work` span for each work item, from when a poll returns the work item until its handling ends.

| Attribute                       | Type     | Description                                                                                                                 |
|---------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| `anthropic.environment.id`      | `string` | The environment ID.                                                                                                         |
| `anthropic.environment.work.id` | `string` | The work item ID.                                                                                                           |
| `anthropic.session.id`          | `string` | The ID of the session that the work item belongs to.                                                                        |
| `error.type`                    | `string` | The `error.type` of the span for the failed request, if a request ended the handling. `client_error` for any other failure. |

### `anthropic.<resources>.<method>`

- **Source:** The SDK.
- **Kind:** `CLIENT`.
- **Parent:** The span that is current in the application when it calls the method, or none if no span is current.
- **Children:** None.

Each SDK method that sends a request and doesn't have a section on this page emits an `anthropic.<resources>.<method>` span, for example `anthropic.models.list` or `anthropic.files.upload`. The request for each later page of a list has its own span.

A span covers its whole request, retries included, and has each attribute of the same-named API span when the SDK has the value. The SDK sets `http.request.method` and `http.route` when it starts the span, so a sampler can use them.

Every SDK span for a request, including [`anthropic.messages.create`](#anthropic-messages-create), [`anthropic.messages.count_tokens`](#anthropic-messages-count-tokens), and [`anthropic.messages.batches.<method>`](#anthropic-messages-batches-method), has the following attributes:

| Attribute                   | Type     | Description                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `gen_ai.conversation.id`    | `string` | The conversation ID passed with the [`conversation_id` option](../Other/manage-claude-opentelemetry-sdk.md#configure-the-sdk). Without one, the session thread ID on requests to one session thread, and on the request in which the session tool runner sends a tool's result. Absent on other requests.                                       |
| `anthropic.<resource>.id`   | `string` | One attribute for each ID in the request's path and one for the ID of an object that the method creates. The name comes from the path, in the singular, for example `anthropic.session.id` or `anthropic.session.thread.id`.                                                                                                                 |
| `gen_ai.agent.id`           | `string` | The agent ID, on the agent methods.                                                                                                                                                                                                                                                                                                          |
| `gen_ai.memory.store.id`    | `string` | The memory store ID, on the memory store methods.                                                                                                                                                                                                                                                                                            |
| `gen_ai.memory.record.id`   | `string` | The memory ID, on the memory methods.                                                                                                                                                                                                                                                                                                        |
| `http.request.resend_count` | `int`    | The number of times that the SDK resent the request, for any reason, such as a retry. Absent when the SDK didn't resend it.                                                                                                                                                                                                                  |
| `error.type`                | `string` | A failed call's [error type](errors.md#http-errors), for example `rate_limit_error`. The HTTP status code, for example `502`, when the error response doesn't have an error type. `connection_error`, `client_timeout_error`, or `client_error` when the call failed in the SDK. `api_error` when the server ended a stream early. |
| `server.address`            | `string` | The host of the client's base URL, `api.anthropic.com` by default. On a cloud platform's client, that platform's host.                                                                                                                                                                                                                       |
| `url.query`                 | `string` | The URL's query string, with only the query parameters that the endpoint defines. Absent when there are none. In metadata-only mode, absent when the query has a sensitive parameter, such as `email`.                                                                                                                                       |
| `url.full`                  | `string` | The URL, made of `url.scheme`, `server.address`, the port when the base URL has one, `url.path`, and `url.query`. In metadata-only mode, absent whenever that mode leaves out `url.query`.                                                                                                                                                   |
