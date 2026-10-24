---
title: "OpenTelemetry for the Claude API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/opentelemetry"
category: "04-API-Reference/Other"
fetched_at: "2026-10-23T06:28:52Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fopentelemetry)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Plugins API](manage-claude-plugins-api.md)[Workspaces](manage-claude-workspaces.md)[Organization webhooks (beta)](manage-claude-organization-webhooks.md)[User profiles](manage-claude-user-profiles.md)[Verification Portal links](manage-claude-user-profiles-verification-portal.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF with the Admin API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

[OpenTelemetry](manage-claude-opentelemetry.md)

[Overview](manage-claude-opentelemetry.md)[Get Claude SDK spans](manage-claude-opentelemetry-sdk.md)[Get Claude API spans](manage-claude-opentelemetry-api.md)

Data & compliance

[Data residency](manage-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys (CMEK)](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)OpenTelemetry

OpenTelemetry

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

# OpenTelemetry for the Claude API

Copy page



Trace your Messages API requests, tool uses, and Managed Agents sessions with OpenTelemetry spans from the Claude SDK and the Claude API.

Copy page





OpenTelemetry export is in beta. It's provided under your agreement with Anthropic, including the Beta Services section of the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms).

The Claude API and the SDK can trace your Messages API requests, tool uses, and Managed Agents sessions with [OpenTelemetry](https://opentelemetry.io/). You can view these traces in the observability platform you already have. Use them to debug failed or slow requests, track token spend and latency, and build evals from real traffic. You can also see each request inside your application's own traces, linked to the user or feature that sent it.

OpenTelemetry is a vendor-neutral standard that most observability platforms support. A *trace* is the full record of one request through your system. A *span* is one step in a trace, such as a model request or a tool use. The API and the SDK use attributes from the [GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai), so platforms that support the conventions can recognize the spans without extra setup.

## Get started

You can set up SDK tracing, API tracing, or both. Set up both to see a request's SDK and API spans in one trace, as in the [example traces](#example-traces-and-how-to-read-them).

Claude Code

Let Claude Code set up this feature for you

Run in

`❯``Set up OpenTelemetry tracing with the Claude API and Claude SDK`



[Set up SDK tracing](manage-claude-opentelemetry-sdk.md)

Install the SDK and register a tracer provider.



[Set up API tracing](manage-claude-opentelemetry-api.md)

Add a destination in the Claude Console.



[Span reference](../Endpoints/opentelemetry-spans.md)

Look up spans and their attributes.



[TABLE]

For Claude Code, the Agent SDK, or Cowork, see [Claude Code monitoring](../../13-Enterprise-Admin/monitoring-usage.md), [Agent SDK observability](../../05-Agent-SDK/agent-sdk-observability.md), or [Cowork activity monitoring](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry).

## Send traces to a partner platform

Send traces to any observability platform that accepts OTLP, including these partners:

[Arize AI](https://arize.com/docs/ax/integrations/platforms/claude-managed-agents/claude-managed-agents-tracing)

Unified observability and evaluation platform for AI.

[Braintrust](https://www.braintrust.dev/docs/integrations/ai-providers/anthropic#export-opentelemetry-traces-from-the-claude-api)

Active observability platform for agents.

[Databricks](https://docs.databricks.com/aws/en/ai-gateway/unified-trace-table)

Unified AI control plane for observability and evaluation.

[Datadog](https://docs.datadoghq.com/llm_observability/instrument/otel_instrumentation/?tab=python#using-claude-managed-agents)

AI-powered observability and security.

[Dynatrace](https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability/integrations/claude-platform)

Observability built for the age of AI.

[Elastic](https://www.elastic.co/docs/reference/opentelemetry/motlp)

Observability built on open source.

[Grafana Cloud](https://grafana.com/docs/grafana-cloud/observe-and-act/agent-observability/guides/send-claude-platform-traces/)

Fully managed open observability platform.

[Honeycomb](https://docs.honeycomb.io/send-data/use-cases/claude-platform)

Observability platform for the new shape of software.

[Langfuse](https://langfuse.com/integrations/model-providers/claude-platform)

Open-source agent observability and evaluation platform.

[LangSmith](https://docs.langchain.com/langsmith/trace-anthropic)

LangSmith agent engineering platform.

[New Relic](https://docs.newrelic.com/docs/ai-monitoring/opentelemetry-ai-monitoring/#anthropic)

Intelligent observability platform.

[PostHog](https://posthog.com/docs/ai-observability/installation/anthropic?tab=Claude+Platform&utm_source=anthropic&utm_campaign=anthropic-otel)

All-in-one platform for building successful products.

[Pydantic Logfire](https://pydantic.dev/docs/logfire/integrations/llms/claude-platform/)

Production-grade AI & general observability.

[Sentry](https://sentry.io/cookbook/trace-claude-platform-with-opentelemetry/)

Debug your broken code and misbehaving agents.

[Snowflake](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-ai-gateway/observability#trace-claude-requests)

AI Data Cloud.

[Splunk](https://agent-observability-docs.splunk.com/sdk-api/third-party-integrations/claude)

Observe, evaluate, and secure agents.

## Content modes

Each destination and each SDK client has a content mode, which sets whether spans include model prompts and responses. Set it when you [add a destination](manage-claude-opentelemetry-api.md#add-a-destination) or [configure the SDK](manage-claude-opentelemetry-sdk.md#configure-the-sdk).

- **Metadata only** (`metadata_only` in the SDK): The default. Spans include identifiers, timing, status, token counts, and text that you choose, such as the names and descriptions of your agents and tools and the names of your MCP servers.
- **Full content** (`content` in the SDK): Most visibility. Spans include model prompts and responses, and everything in Metadata only.

With Full content, you can also see why a run failed or was slow, read full conversations, and build evals from real traces. In the [OpenTelemetry span reference](../Endpoints/opentelemetry-spans.md), attributes that hold prompts and responses are tagged Content.



Your observability platform stores this content under its own access and retention settings, so check that they meet your organization's requirements.

If your organization has a HIPAA, FERPA, or K-12 data-handling restriction with Anthropic, destinations export only metadata regardless of their content mode. SDK spans aren't affected.

With [zero data retention](manage-claude-api-and-data-retention.md), you can still use Full content. For Messages API requests, the API holds the exported content only in memory until it delivers it to the destination. [Claude Managed Agents](managed-agents-overview.md) isn't eligible for zero data retention, and its data retention stays the same when you use OpenTelemetry.

### Content limits

With Full content, each span holds up to 0.75 MB of content by default. That fits a 200k-token context window of English text and stays below the 1 MB request limit of many observability platforms and proxies. If you select a partner platform as the **Provider**, the Console sets a limit that the platform accepts.

When content is over the limit, the SDK or the API shortens it and sets `anthropic.content.truncated` to `true`. Request spans drop the system prompt and the earliest messages first, and tool spans drop blocks from the end of the result. Images and documents appear only as their type.

Change the limit in these cases:

- **Your observability platform accepts larger payloads:** Raise or remove the limit to keep long prompts and responses whole. A full 1M-token context window needs about 4 MB.
- **Your observability platform or a proxy in front of it rejects large requests:** Lower the limit.

In the SDK, set `traces.max_content_bytes`. In the Console, set **Content mode** to **Full content** when you [add a destination](manage-claude-opentelemetry-api.md#add-a-destination), then set **Maximum content size in MB** under **Advanced settings**.

## Example traces and how to read them

### A Messages API request

Under the API span for a request that [creates a message](../Endpoints/messages-create.md), the API adds a span for each model request and a tool span for each use of a server tool or an MCP connector tool that the API runs.

In this example, your application calls the [tool runner](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md), the SDK helper that runs your tools and sends their results back to Claude. Each request that the tool runner sends has a client span from the SDK and a server span from the API. The spans appear in the following order:

1.  Your application starts the `answer_question` span and calls the Messages tool runner inside it (shown as the [`anthropic.messages.tool_runner`](../Endpoints/opentelemetry-spans.md#anthropic-messages-tool-runner) span).
2.  The tool runner sends the first request (shown as the first [`anthropic.messages.create`](../Endpoints/opentelemetry-spans.md#anthropic-messages-create) client span and the spans under it). In this request, the API runs the web search tool between two model requests.
3.  In the second model request, the model asks to use the custom `get_weather` tool, so the first request ends.
4.  The tool runner runs `get_weather` (shown as the `anthropic.custom_tool_use get_weather` span).
5.  The tool runner sends the second request with the tool result (shown as the second `anthropic.messages.create` client span and the spans under it).
6.  In the second request, the model gives the final answer.

The SDK in your application emits the [`anthropic.messages.tool_runner`](../Endpoints/opentelemetry-spans.md#anthropic-messages-tool-runner) span, the [`anthropic.custom_tool_use`](../Endpoints/opentelemetry-spans.md#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) span, and each request's client span. To get these spans, [set up SDK tracing](manage-claude-opentelemetry-sdk.md).

Each request has its token usage on several of its spans. To count each token once, see [Counting tokens](#count-tokens).

With [Full content](#choose-a-content-mode), the `anthropic.messages.create` server span has the prompt and the response. The system prompt is in `gen_ai.system_instructions`, the request's messages in `gen_ai.input.messages`, and the response in `gen_ai.output.messages`.

For each span and its attributes, see the [OpenTelemetry span reference](../Endpoints/opentelemetry-spans.md).

### A Managed Agents session

A session has a span for each Sessions API request and a turn span for each agent turn. A turn that a request starts is a child of that request's span. A turn contains a span for each model request and each tool that the API runs, except in the [cases listed in the tool span reference](../Endpoints/opentelemetry-spans.md#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use). It also contains a span for each outcome evaluation.

This example follows one chat request, in which your application sends a message to a session and runs a custom tool. The trace has spans from both your application and the API, in the following order:

1.  Your application receives a `POST /chat` request from a user.
2.  Your application starts the SDK's session tool runner, which lists and streams the session's events (shown as the `anthropic.sessions.events.stream` and `anthropic.sessions.events.list` spans).
3.  Your application sends the user's message to the session by calling `sessions.events.send`.
4.  A turn starts and includes model requests, a `bash` tool use, and a turn on another thread (shown as the first `anthropic.session.turn` span and the spans under it).
5.  The model asks to use the [custom tool](managed-agents-tools.md) `list_issues`, so the turn ends with the stop reason `requires_action`.
6.  The session tool runner runs `list_issues` (shown as the `anthropic.custom_tool_use list_issues` span) and sends its result by calling `sessions.events.send`.
7.  A second turn starts with the tool result (shown as the last `anthropic.session.turn` span).

The SDK in your application emits the [`anthropic.custom_tool_use`](../Endpoints/opentelemetry-spans.md#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) span and each request's client span. To get these spans, [set up SDK tracing](manage-claude-opentelemetry-sdk.md).

A session's spans can be in several traces, for example when you send a later request from a new root trace. With [multiagent](managed-agents-multiagent-orchestration.md) on, a session can also have several threads. To find the spans you need, group them by an ID.

- **One thread:** Group spans by `gen_ai.conversation.id`, which holds the session thread ID. Sort them by start time to read the thread as a transcript.
- **A whole session, with all its threads:** Group spans by `anthropic.session.id`, across traces.

With [Full content](#choose-a-content-mode), you can read a session's content from its spans.

- To read a turn's content, use its [turn span](../Endpoints/opentelemetry-spans.md#anthropic-session-turn). The system prompt is in `gen_ai.system_instructions` on a thread's first turn span, the input in `gen_ai.input.messages` (your messages and tool results, `system.message` events, and messages from other threads), and the output in `gen_ai.output.messages` (the agent's messages, tool uses, and tool results).
- To see the arguments and result of a tool use, read its [tool span](../Endpoints/opentelemetry-spans.md#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use). The arguments are in `gen_ai.tool.call.arguments`, and the result is in `anthropic.tool_result.content`.

For each span and its attributes, see the [OpenTelemetry span reference](../Endpoints/opentelemetry-spans.md).

## Counting tokens

To count each token once, sum the spans of only one source for each request. When a Messages API request has both an SDK span and an API span, sum its API spans. Both are named `anthropic.messages.create`, so tell them apart by kind: the SDK span is `CLIENT` and its child, the API span, is `SERVER`.

For each source, sum only the following spans, because some usage attributes repeat on more than one level of the API spans:

- **SDK spans:** Sum the [`anthropic.messages.create`](../Endpoints/opentelemetry-spans.md#anthropic-messages-create) spans. If a request has [compactions](../Guides/build-with-claude-compaction.md), also add the span's `anthropic.usage.compaction.input_tokens` and `anthropic.usage.compaction.output_tokens`, because the `gen_ai.usage.*` attributes don't include compaction tokens. If a [fallback model](../Guides/build-with-claude-refusals-and-fallback.md) served a request, its span has the usage of only the model that served the response.
- **API spans for a Messages API request:** Sum either the [`anthropic.messages.create`](../Endpoints/opentelemetry-spans.md#anthropic-messages-create) spans or their [`anthropic.model_request`](../Endpoints/opentelemetry-spans.md#anthropic-model-request) spans, not both. If a request has compactions, also add its [`anthropic.compaction`](../Endpoints/opentelemetry-spans.md#anthropic-compaction) spans. Don't add the `anthropic.usage.compaction.*` attributes of the `anthropic.messages.create` span as well, because they hold the same tokens.
- **API spans for a Managed Agents session:** Sum the `anthropic.model_request` and [`anthropic.session.outcome_evaluation`](../Endpoints/opentelemetry-spans.md#anthropic-session-outcome-evaluation) spans.

Spans can arrive more than once, for example when a delivery is retried. If your observability platform doesn't remove duplicates, count each span once by its trace ID and span ID.

`gen_ai.usage.input_tokens` already includes the tokens read from and written to the prompt cache, so don't add the cache attributes to it. For all usage attributes, see [Token usage](../Endpoints/opentelemetry-spans.md#token-usage).



Exported spans aren't guaranteed to be a complete record of your API usage. Their delivery is [best effort](manage-claude-opentelemetry-api.md#delivery-and-health), so a span can be lost. A caller can also leave out a request's spans by turning off the sampled flag in the request's [`traceparent` header](manage-claude-opentelemetry-api.md#connect-api-spans-to-your-own-traces). To track each API key's usage, for example to spot a leaked key, use the [Usage API](manage-claude-usage-cost-api.md#usage-api), which also counts the usage of requests without spans.
