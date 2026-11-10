---
title: "Set up OpenTelemetry with the Claude SDK - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk"
category: "04-API-Reference/Other"
fetched_at: "2026-11-06T06:33:48Z"
tags: ["agents", "api", "sdk"]
---

# Set up OpenTelemetry with the Claude SDK

Copy page



Trace the Claude SDK’s requests and tool uses in Python, TypeScript, C#, Go, Java, PHP, or Ruby, and send the spans to your observability platform.

Copy page



SDK tracing

Feature of  
[OpenTelemetry](manage-claude-opentelemetry.md)

[Status](#availability-feature-support)  
Beta

[APIs](#feature-availability)  
Messages APIAvailableManaged AgentsAvailable

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableAmazon BedrockAvailableAmazon BedrockInvokeModelAvailableClaude Models on Google CloudGoogle managedAvailableMicrosoft FoundryAvailable

With OpenTelemetry, the Claude SDK can emit a span for each request that it sends and each tool use that the [tool runner](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md) runs. You can view these spans in your observability platform, nested in your own traces.

The SDK emits spans in your application. Your application’s OpenTelemetry exporter sends them to your observability platform.



During the beta, the SDK options and the span schema can change in ways that break your code, your queries, or your dashboards. For example, a new version of the SDK can rename a span, an attribute, an option, or an environment variable. Pin the SDK version in your dependencies to choose when you adopt the changes.

## 1. Install the SDK

Install or upgrade to the latest version of the Claude SDK:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

```python
pip install --upgrade anthropic
```



If your application doesn’t use the OpenTelemetry SDK yet, install it with a console exporter, which you use in the next step to print spans:

```python
pip install opentelemetry-sdk
```



## 2. Register a tracer provider

A *tracer provider* is the OpenTelemetry object that creates spans and passes them to your exporter. The SDK uses the tracer provider that your application registers, so your SDK calls stay the same. Register it before the first call that you want to trace.

The following example registers a tracer provider that prints each span to the console and then makes one call. Use it to see spans before you connect an observability platform:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
from anthropic import Anthropic
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# Register a tracer provider that prints each span to the console.
provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)

client = Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content)
```

The console shows one [`anthropic.messages.create`](../Endpoints/opentelemetry-spans.md#anthropic-messages-create) span.

## 3. Send spans to your observability platform

Replace the console exporter with an OTLP exporter that points to your observability platform. For the setup in your language, see the OpenTelemetry docs on [Python exporters](https://opentelemetry.io/docs/languages/python/exporters/), [TypeScript exporters](https://opentelemetry.io/docs/languages/js/exporters/), [.NET exporters](https://opentelemetry.io/docs/languages/dotnet/exporters/), [Go exporters](https://opentelemetry.io/docs/languages/go/exporters/), [Java SDK configuration](https://opentelemetry.io/docs/languages/java/configuration/), [PHP exporters](https://opentelemetry.io/docs/languages/php/exporters/), or [Ruby exporters](https://opentelemetry.io/docs/languages/ruby/exporters/).

## 4. Configure the SDK

Use the following options to decide what goes into your spans and where they are sent. You can set an option in your code or, if it has one, with the environment variable under its name.



If you pass `open_telemetry` to the client, it overrides that option’s environment variables as a whole, including nested keys. Any nested key that you leave out uses its default from the table, even if its environment variable is set.

[TABLE]

The following example shows how to use each option:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
# Use a specific tracer provider and record content.
# Setting open_telemetry overrides all ANTHROPIC_OPEN_TELEMETRY* environment variables.
client = Anthropic(
    open_telemetry={"tracer_provider": provider, "traces": {"content_mode": "content"}}
)

# Turn spans off for one client.
quiet_client = Anthropic(open_telemetry=False)

# Set a conversation ID with with_options(), which returns a copy of the client.
# with_options() replaces the whole option, so start from client.open_telemetry.
message = client.with_options(
    open_telemetry={**client.open_telemetry, "conversation_id": "conv_42"}
).messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
```

## Next steps



[Set up API tracing](manage-claude-opentelemetry-api.md)

Get observability into the Claude API.

[See example traces](manage-claude-opentelemetry.md#example-traces-and-how-to-read-them)

Follow a request from your client into the Claude API.

## Tracing a stream

A stream’s `anthropic.messages.create` span ends when your code has read the whole stream or closed it, so close a stream that you stop reading early. In content mode, the span has the model response only when you read the stream with `messages.stream()`.

Spans that you start while you read a stream are siblings of the SDK span, not its children. To group them with the request, start your own span around both the call and the read loop.

## Tracing a Managed Agents self-hosted sandbox

In a Managed Agents [self-hosted sandbox](managed-agents-self-hosted-sandboxes.md), your sandbox runs the tools, so the tool spans come from the SDK instead of the API. The environment worker in the Python, TypeScript, and Go SDKs emits a span for each tool that it runs and each request that it sends. It groups them under one [`anthropic.environment.work`](../Endpoints/opentelemetry-spans.md#anthropic-environment-work) span for each work item.

To get these spans:

1.  In the process that runs the worker, [set up SDK tracing](#install-the-sdk) as in steps 1 to 4.
2.  Allow network traffic from the sandbox to your observability platform or OpenTelemetry Collector.

When the worker sends a tool result, that request’s API span is nested under its SDK span.

## Trace context and baggage

With each request, the SDK uses your application’s propagator to send the trace context to the API in headers such as `traceparent`. If that propagator also writes baggage, the SDK sends your baggage too. To send the trace context without baggage, register only the W3C trace context propagator.

To stop the SDK from sending these headers, for example when your HTTP client instrumentation already sends them, turn off the SDK’s propagation:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = Anthropic(open_telemetry={"propagation": False})
```

While the SDK calls an [MCP tool](../Agents-Tools/agents-and-tools-mcp-connector.md#client-side-mcp-helpers), the SDK’s tool span is the current span. Some MCP client libraries send the trace context to the MCP server in `_meta`, so a server that reads it can add its spans to your trace under that tool span. The Python `mcp` package from version 2.0 and the C# `ModelContextProtocol` package do this. The TypeScript, Go, Java, Ruby, and PHP MCP SDKs don’t do it on their own.

## Troubleshooting

| Problem | What to check |
|----|----|
| No spans from the SDK | Register the tracer provider before the first call. Make sure that you installed the SDK as in [Install the SDK](#install-the-sdk) and that `ANTHROPIC_OPEN_TELEMETRY` isn’t `false`. |
| The Java SDK doesn’t send spans to the registered tracer provider, or doesn’t send trace context to the API | Another dependency sets `opentelemetry-api` below 1.57.0. Upgrade `opentelemetry-api` to 1.57.0 or later. |
| The SDK spans don’t nest under your spans, or the spans that your tool creates don’t nest under the tool span | Call the SDK from inside one of your own spans, as the example in [Connect API spans to your own traces](manage-claude-opentelemetry-api.md#connect-api-spans-to-your-own-traces) does. In Go, start the spans that your tool creates from the `ctx` that the tool runner passes to it. |
| Requests from the SDK don’t have a `traceparent` header | Register the W3C trace context propagator with OpenTelemetry. The SDK writes the headers with your application’s propagator. |
| A stream’s SDK span doesn’t end or doesn’t have the response | See [Tracing a stream](#trace-a-stream). |
| Each request appears twice | A request’s SDK span and API span have the same name. Use the span kind or `service.name` to tell them apart. If another library also traces the SDK, turn off one of the two. |

## Availability

SDK tracing is in beta on every model.

### API support

[Messages API](../Guides/build-with-claude-working-with-messages.md)

StatusBeta

Cloud platforms

- Claude API
- [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)
- [Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md)
- [Amazon Bedrock](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)InvokeModel
- [Claude Models on Google Cloud](../Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)Google managed
- [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Managed Agents](managed-agents-overview.md)

Usage

The SDK traces the requests that your code sends, such as the events you send to a session; spans for the agent’s model requests and tool calls come from API tracing. In a self-hosted sandbox, the SDK’s environment worker also traces each tool it runs.

StatusBeta

Cloud platforms

- Claude API
- [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)
