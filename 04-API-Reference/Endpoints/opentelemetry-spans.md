---
title: "OpenTelemetry span reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/opentelemetry/spans"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:33:42Z"
tags: ["api"]
---

# OpenTelemetry span reference

Copy page



The OpenTelemetry spans and span attributes that the Claude API and the Claude SDK emit.

Copy page



[OpenTelemetry](../Other/manage-claude-opentelemetry.md)

[Status](../Other/manage-claude-opentelemetry.md#availability-feature-support)  
Beta

[APIs](../Other/manage-claude-opentelemetry.md#feature-availability)  
Messages APIAvailableManaged AgentsAvailable

[Cloud platforms](../Other/manage-claude-opentelemetry.md#availability-feature-support)  
All platforms



OpenTelemetry export is in beta. It’s provided under your agreement with Anthropic, including the Beta Services section of the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Span names and attributes can change during the beta.

To get spans, see [Set up OpenTelemetry with the Claude SDK](../Other/manage-claude-opentelemetry-sdk.md) and [Set up OpenTelemetry with the Claude API](../Other/manage-claude-opentelemetry-api.md).

## Span names and kinds

[TABLE]

- **Spans for requests** have the name of the request’s API method: `anthropic.` followed by the method’s path in the API reference, with dots instead of slashes and without `beta`. For example, `client.beta.sessions.events.send()` sends a request to [send session events](beta-sessions-events-send.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., and its spans have the name [`anthropic.sessions.events.send`](#anthropic-sessions-events-send).
- **Tool spans** have a fixed name, a space, and the tool name, for example [`anthropic.tool_use bash`](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use).

## Span status

- **`OK`:** The step completed.
- **`ERROR`:** The step failed.
- **Unset:** The application canceled the step, for example when it sent a [`user.interrupt`](beta-sessions-events.md#beta_managed_agents_user_interrupt_event)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. event.

A stream’s span ends when the stream ends. If the application closes the stream early, the SDK span has the status unset, so the SDK span for a stream that never completes, such as [`anthropic.sessions.events.stream`](#anthropic-sessions-method), has the status unset or `ERROR`.

## Attributes

Attributes use the [OpenTelemetry semantic conventions for generative AI](https://github.com/open-telemetry/semantic-conventions-genai) (`gen_ai.*`) where one exists. Anthropic attributes start with `anthropic.`. The spans follow the conventions at commit [`e57c543b`](https://github.com/open-telemetry/semantic-conventions-genai/tree/e57c543b4889619eb2a05702471937db5119165d) of September 24, 2026. The conventions are still in development.

### Common attributes

Every span for a request has the following attributes, except where a description says otherwise. Other spans can have only the first three:

[TABLE]

API spans for requests sent through a cloud platform, such as Claude Platform on AWS, don’t have `server.address`, `server.port`, or `url.full`.

### Session attributes

In a Managed Agents session, spans have the following attributes. A session’s spans can be in more than one trace, so to assemble a view of the session, such as a transcript, [group its spans by these IDs](../Other/manage-claude-opentelemetry.md#a-managed-agents-session).

[TABLE]

### Content attributes

Attributes tagged with Content are only on spans in content mode, from the SDK and the API alike. See [how the content modes differ in the guide](../Other/manage-claude-opentelemetry.md#choose-a-content-mode). When this content is too large, the SDK and the API shorten it to fit the [content limits](../Other/manage-claude-opentelemetry.md#content-limits) and set `anthropic.content.truncated` to `true`. If Anthropic’s safeguards withhold content from a response, the API’s spans don’t include that content either.

The message attributes are JSON strings in the message format of the OpenTelemetry GenAI conventions. Each Anthropic content block becomes one GenAI conventions message part, on the Messages API and in Managed Agents message events such as `agent.message`:

[TABLE]

Each Managed Agents tool use or tool result event also becomes one GenAI conventions message part:

[TABLE]

### Token usage

The following spans have token usage attributes: [`anthropic.messages.create`](#anthropic-messages-create), [`anthropic.model_request`](#anthropic-model-request), [`anthropic.compaction`](#anthropic-compaction), and [`anthropic.session.outcome_evaluation`](#anthropic-session-outcome-evaluation). The values are for each span’s step, for example the request, the model request, or the compaction. On the API spans for a Messages API request, the token counts are the tokens that your organization is billed for, even when the request fails or the application cancels it. The SDK’s `anthropic.messages.create` span has the counts that the response reports instead, so for a failed or canceled request they can be lower than on the API span, or absent. To count each token once, see [how to count tokens in the guide](../Other/manage-claude-opentelemetry.md#count-tokens).

[TABLE]

## Spans

A span can come from the SDK in the application or from the API, so each span in this reference lists its sources. Descriptions that start with **Messages API:** or **Managed Agents:** are for that product’s spans. Attribute descriptions that start with a source, such as **SDK:** or **API:**, are for that source’s spans.

### `anthropic.messages.create`

- **Source:** The SDK and the API.
- **Kind:** `CLIENT` from the SDK, `SERVER` from the API.
- **Parent of the SDK span:** The span that is current in the application when it calls the method. If no span is current, there’s no parent.
- **Parent of the API span:** The span in the request’s `traceparent` header, which is the SDK span when the request comes from the SDK. Without the header, the API span has no parent. See [how to send the `traceparent` header](../Other/manage-claude-opentelemetry-api.md#connect-api-spans-to-your-own-traces).
- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** An [`anthropic.model_request`](#anthropic-model-request) span for each model request, a [tool span](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) for each use of a server tool or an MCP connector tool that the API runs in the request, and an [`anthropic.compaction`](#anthropic-compaction) span for each compaction.

The SDK emits this span for each Messages request, streamed or not.

The API emits this span for each [`POST /v1/messages`](messages-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. request that it authenticates. It doesn’t emit the span for a request to the [OpenAI-compatible endpoint](../Other/cli-sdks-libraries-libraries-openai-sdk.md), `POST /v1/chat/completions`.

The API emits one span for a request, even when a [fallback model](../Guides/build-with-claude-refusals-and-fallback.md) serves it.

The span has the [token usage attributes](#token-usage). The SDK span also has the attributes of every [SDK span for a request](#anthropic-resources-method).

[TABLE]

A request’s spans don’t have the response’s server tool usage counts, such as `web_search_requests`. Instead, the API emits a [tool span](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) for each use of a server tool.

### `anthropic.messages.count_tokens`

- **Source:** The SDK. The API doesn’t emit a span for [`POST /v1/messages/count_tokens`](platform-claude-com-messages-count-tokens.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return..
- **Kind:** `CLIENT`.
- **Parent:** The span that is current in the application when it calls the method, or none if no span is current.
- **Children:** None.

[TABLE]

### `anthropic.sessions.create`

The same as [`anthropic.sessions.<method>`](#anthropic-sessions-method), except for the following children and attributes:

- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** The first turn’s [`anthropic.session.turn`](#anthropic-session-turn) span, when the request has non-empty [`initial_events`](beta-sessions-create.md#create.initial_events)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return..

[TABLE]

### `anthropic.sessions.events.send`

The same as [`anthropic.sessions.<method>`](#anthropic-sessions-method), except for the API span’s children.

- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** The [`anthropic.session.turn`](#anthropic-session-turn) span for each turn that starts because of the request’s events.

### `anthropic.sessions.update`

The same as [`anthropic.sessions.<method>`](#anthropic-sessions-method), except for the API span’s children.

- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** The [`anthropic.session.turn`](#anthropic-session-turn) span for each turn that resumes because the request raises or removes the [session budget](../Other/managed-agents-budgets.md#resume-a-session-at-its-budget).

### `anthropic.session.turn`

- **Source:** The API, for Managed Agents sessions.
- **Kind:** `INTERNAL`.
- **Parent:** It depends on why the turn started:
  - The [`anthropic.sessions.create`](#anthropic-sessions-create) span, for the first turn of a session that was created with non-empty [`initial_events`](beta-sessions-create.md#create.initial_events)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return..
  - The [`anthropic.sessions.events.send`](#anthropic-sessions-events-send) span for the request in which the event was sent, for a turn that started because of an event, for example a [`user.message`](beta-sessions-events.md#beta_managed_agents_user_message_event)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. event.
  - The [`anthropic.sessions.update`](#anthropic-sessions-update) span, for a turn that resumes because the request raises or removes the session budget.
  - The `anthropic.session.turn` span for the turn of [the agent that the session runs](../Other/managed-agents-multiagent-orchestration.md) during which that agent started this turn, for a turn on another thread.
  - The `anthropic.session.turn` span for the turn that produced the reply, for a turn that starts because an agent on another thread replied, such as an agent that the primary agent called.
  - None, for any other turn, such as a turn that starts because a [workflow run](../Other/managed-agents-workflow-runs.md) ended.
- **Children:**
  - An [`anthropic.model_request`](#anthropic-model-request) span for each model request in the turn.
  - A tool span each time the API runs a tool in the turn, except in the [cases listed in the tool span section](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use).
  - An `anthropic.session.turn` span for each turn on another thread that was started during this turn by the agent that the session runs, or by this turn’s reply.
  - An [`anthropic.session.outcome_evaluation`](#anthropic-session-outcome-evaluation) span for each iteration of an outcome evaluation that this turn starts.

A turn starts when its thread enters the `running` state and ends when the thread leaves it.

[TABLE]

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
- **Name:** `anthropic.tool_use <tool>`, `anthropic.mcp_tool_use <tool>`, or `anthropic.custom_tool_use <tool>`, where `<tool>` is the tool’s name.
- **Kind:** `INTERNAL`.
- **Parent of the SDK span:** The span that is current in the application when the tool starts, which in the Messages tool runner is the [`anthropic.messages.tool_runner`](#anthropic-messages-tool-runner) span. If no span is current, there’s no parent.
- **Parent of the API span:**
  - **Messages API:** The [`anthropic.messages.create`](#anthropic-messages-create) span for the request in which the API runs the tool.
  - **Managed Agents:** The [`anthropic.session.turn`](#anthropic-session-turn) span for the turn in which the tool runs. For a tool use that waits for a [`user.tool_confirmation`](beta-sessions-events.md#beta_managed_agents_user_tool_confirmation_event)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. event, that is the turn that starts because of the confirmation.
  - For a tool use from code that another tool runs, the tool span for that tool. On the Messages API, that tool is the [code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md).
- **Children of the SDK span:** The spans that the tool’s code starts.
- **Children of the API span:** A tool span for each tool use from the code that this tool runs. For example, code that the code execution tool runs might use `web_search`.

The span name prefix depends on the type of tool:

- `anthropic.tool_use <tool>` is the span for each use of a [server tool](../Agents-Tools/agents-and-tools-tool-use-server-tools.md) on the Messages API or of a tool from the agent toolset of Managed Agents. The API runs the agent toolset tools, except in a [self-hosted sandbox](../Other/manage-claude-opentelemetry-sdk.md#trace-a-self-hosted-sandbox), where the environment worker runs them.
- `anthropic.mcp_tool_use <tool>` is the span for each use of an MCP tool, in the SDK, on the Messages API, and on Managed Agents. In the SDK, it’s a tool from an MCP helper that the [Messages tool runner](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md) or the [session tool runner](../Other/managed-agents-self-hosted-sandboxes-reference.md#session-tool-runner) runs. On the Messages API, the tool comes from the [MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md). On Managed Agents, if the [connection to the MCP server fails](../Other/managed-agents-mcp-connector.md#handle-connection-and-authentication-failures), the span name doesn’t include the tool name.
- `anthropic.custom_tool_use <tool>` is the span for each use of a tool that the application defines and a tool runner runs. Only the SDK emits this span.

The API doesn’t emit a tool span in the following cases:

- The model asks to use a tool that the application runs, such as a [custom tool](../Other/managed-agents-tools.md). If a tool runner in the SDK runs the tool, the tool runner emits its span.
- **Managed Agents:** The agent uses a tool that runs in a self-hosted sandbox. The worker in the SDK, which runs the tool, emits its span. See [how to trace a self-hosted sandbox](../Other/manage-claude-opentelemetry-sdk.md#trace-a-self-hosted-sandbox).
- **Managed Agents:** The agent uses a [multiagent](../Other/managed-agents-multiagent-orchestration.md) tool or the [advisor tool](../Other/managed-agents-multiagent-orchestration.md#give-the-session-an-advisor).
- **Managed Agents:** The agent asks to use a tool, but the server denies the use under the [`auto` permission policy](../Other/managed-agents-permission-policies.md#let-the-server-evaluate-each-call-with-auto), or the application denies it in a [`user.tool_confirmation`](beta-sessions-events.md#beta_managed_agents_user_tool_confirmation_event)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. event.

[TABLE]

### `anthropic.compaction`

- **Source:** The API, for Messages API requests.
- **Kind:** `INTERNAL`.
- **Parent:** The [`anthropic.messages.create`](#anthropic-messages-create) span for the request.
- **Children:** None.

The span has the compaction’s [token usage attributes](#token-usage). On [`anthropic.messages.create`](#anthropic-messages-create), a compaction’s usage is in the `anthropic.usage.compaction.*` attributes instead of the `gen_ai.usage.*` totals.

[TABLE]

### `anthropic.session.outcome_evaluation`

- **Source:** The API, for Managed Agents sessions.
- **Kind:** `INTERNAL`.
- **Parent:** The [`anthropic.session.turn`](#anthropic-session-turn) span for the turn that started the iteration, even if that turn ends before the iteration.
- **Children:** None.

The status is unset when the result is `interrupted` and `OK` for any other result.

The span has two of the [token usage attributes](#token-usage): `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens`.

[TABLE]

### `anthropic.messages.tool_runner`

- **Source:** The SDK.
- **Kind:** `INTERNAL`.
- **Parent:** The span that is current in the application when the loop starts, or none if no span is current.
- **Children:** The [`anthropic.messages.create`](#anthropic-messages-create) span for each request in the loop and the [tool span](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) for each tool use that the runner runs.

The span ends with the loop. If the application stops the runner, the status is unset. If a tool’s code raises an error, its tool span has the status `ERROR` and the loop continues. The span doesn’t have usage attributes, so read the usage from its [`anthropic.messages.create`](#anthropic-messages-create) children.

[TABLE]

### `anthropic.messages.batches.<method>`

- **Source:** The SDK, for every Message Batches method.
- **Kind:** `CLIENT`.
- **Parent:** The span that is current in the application when it calls the method, or none if no span is current.
- **Children:** None.

The spans also have the attributes of every [SDK span for a request](#anthropic-resources-method).

[TABLE]

### `anthropic.sessions.<method>`

- **Source:** The SDK and the API.
- **Kind:** `CLIENT` from the SDK, `SERVER` from the API.
- **Parent of the SDK span:** The span that is current in the application when it calls the method, or none if no span is current.
- **Parent of the API span:** The span in the request’s [`traceparent` header](../Other/manage-claude-opentelemetry-api.md#connect-api-spans-to-your-own-traces), which is the SDK span when the request comes from the SDK, or none without the header.
- **Children of the SDK span:** The API span for that request.
- **Children of the API span:** None.

The API emits an `anthropic.sessions.<method>` span for each authenticated request to an endpoint of the [Sessions API](../Other/managed-agents-sessions.md). Requests that the platform sends on a user’s behalf, such as a message sent in the Claude Console or a session that a [scheduled deployment](../Other/managed-agents-scheduled-deployments.md) starts, also have one, each in a new trace.

### Span names and endpoints

[TABLE]

The span has the [session attributes](#session-attributes). The SDK span also has the attributes of every [SDK span for a request](#anthropic-resources-method).

[TABLE]

### `anthropic.environment.work`

- **Source:** The CLI and the SDK in Python, TypeScript, and Go.
- **Kind:** `INTERNAL`.
- **Parent:** The span that is current in the application when the environment worker or the work poller gets the work item, or none if no span is current. In `ant beta:worker poll`, the span is a root span.
- **Children:** The spans for the requests that the environment worker sends while it handles the work item and the [tool span](#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) for each tool that it runs for the work item.

The environment worker and the work poller are the [SDK helpers](../Other/managed-agents-self-hosted-sandboxes.md#sdk-helpers) that claim work items in a self-hosted sandbox. They emit one `anthropic.environment.work` span for each work item, from when a poll returns the work item until its handling ends.

[TABLE]

### `anthropic.<resources>.<method>`

- **Source:** The SDK.
- **Kind:** `CLIENT`.
- **Parent:** The span that is current in the application when it calls the method, or none if no span is current.
- **Children:** None.

Each SDK method that sends a request and doesn’t have a section on this page emits an `anthropic.<resources>.<method>` span, for example `anthropic.models.list` or `anthropic.files.upload`. The request for each later page of a list has its own span.

A span covers its whole request, retries included, and has each attribute of the same-named API span when the SDK has the value. The SDK sets `http.request.method` and `http.route` when it starts the span, so a sampler can use them.

Every SDK span for a request, including [`anthropic.messages.create`](#anthropic-messages-create), [`anthropic.messages.count_tokens`](#anthropic-messages-count-tokens), and [`anthropic.messages.batches.<method>`](#anthropic-messages-batches-method), has the following attributes:

[TABLE]
