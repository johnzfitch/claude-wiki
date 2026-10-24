---
title: "Set up OpenTelemetry with the Claude API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/opentelemetry/api"
category: "04-API-Reference/Other"
fetched_at: "2026-10-22T06:29:43Z"
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fopentelemetry%2Fapi)

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

[OpenTelemetry](manage-claude-opentelemetry.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[ZDR](manage-claude-api-and-data-retention.md)

Eligible

excludes [Covered Models](manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Only for features that are themselves ZDR eligible, such as the Messages API. Claude Managed Agents isn't ZDR eligible.

# Set up OpenTelemetry with the Claude API

Copy page



Add a destination in the Claude Console to send OpenTelemetry traces of your Messages API requests and Managed Agents sessions to your observability platform.

Copy page



With OpenTelemetry, the Claude API can emit a span for each model request and each tool use that it runs. You can view these spans in your observability platform without changing your code.

The API emits spans for your Messages API requests and Managed Agents sessions. To receive them, add a *destination* in the Claude Console. A destination tells the API your observability platform's OTLP endpoint and how to authenticate with it.

## What you need

- **The admin role** in a Claude Console organization, to add and change destinations. With the developer role, you can view them. If your organization is on Claude Platform on AWS, sign in to the Console through the AWS Console, as [Signing in](../Guides/build-with-claude-claude-platform-on-aws.md#signing-in) describes.
- **An OTLP/HTTP endpoint** that accepts protobuf encoding at an HTTPS URL on port 443. If you run your own [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), its OTLP/HTTP receiver listens on port 4318 by default. Configure the receiver to accept HTTPS on port 443, or put a load balancer or reverse proxy in front of the Collector.
- **Credentials for the endpoint**, such as an API key.

## 1. Add a destination



When you add a telemetry destination, Anthropic will send traces of Claude Platform activity in your organization to the third-party provider's OTLP/HTTP endpoint that you specify, in accordance with your provider terms and access controls. After delivery, the data is held by the service that you chose, outside Anthropic, under that service's retention and access controls.

1.  In the Console, open your organization's [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations) and click **Add destination**.

2.  Configure the destination:

    | Field                          | What to enter                                                                                                                                                                                                                                                                                                                                                                            |
    |--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Provider**                   | Your observability platform, or **Custom** if it isn't listed. If you select a listed platform, the Console asks for its details, such as an API key, instead of the **OTLP endpoint URL**, **Request headers**, and **OTLP traces endpoint URL**.                                                                                                                                       |
    | **Name**                       | Optional. For example, "Acme's observability platform."                                                                                                                                                                                                                                                                                                                                  |
    | **OTLP endpoint URL**          | The base HTTPS URL of your observability platform's OTLP/HTTP endpoint, with a hostname, not an IP address. It can have a path prefix, for example `https://gateway.example.com/otlp`. Don't add `/v1/traces`, because the API adds it. If you set an **OTLP traces endpoint URL**, the API uses that URL instead.                                                                       |
    | **Request headers**            | The headers that the API sends with each request, for example your observability platform's API key header. Put credentials only in header values. After you save, the Console doesn't show the values again.                                                                                                                                                                            |
    | **Content mode**               | **Metadata only** or **Full content**. See [how the content modes differ](manage-claude-opentelemetry.md#choose-a-content-mode).                                                                                                                                                                                                                                                   |
    | **Workspaces**                 | The workspaces whose spans the destination receives: **All**, **Selected**, or **All except**. See [Choose workspaces for a destination](#choose-workspaces-for-a-destination).                                                                                                                                                                                                          |
    | **OTLP traces endpoint URL**   | Optional, under **Advanced settings**. The full URL of your observability platform's traces endpoint, for example `https://gateway.example.com/custom/traces`. Set it when the platform receives traces at a URL other than the OTLP endpoint URL plus `/v1/traces`. It must have the same host as the OTLP endpoint URL.                                                                |
    | **Maximum content size in MB** | Optional, under **Advanced settings** when the content mode is **Full content**. The most content that the API sends in each span. The Console fills it in based on the **Provider** you select. Change it to fit what your observability platform accepts. Leave it empty to send as much as the API allows. See [Content limits](manage-claude-opentelemetry.md#content-limits). |

3.  Click **Add destination** to save.

4.  Click **Test** in the destination's **More actions** menu. You will see a message that the test span was delivered to your collector, or how the delivery failed (see [Delivery errors](#delivery-errors)).

5.  Check that the `anthropic.test` span arrived in your observability platform.

### Admin API and CLI

You can also add a destination with the [Admin API](manage-claude-admin-api.md) instead of the Console. Sign in to the CLI as an admin, or use another [Admin API credential](manage-claude-admin-api.md#authentication), such as an [Admin API key](manage-claude-admin-api-keys.md) or a service account key in `ANTHROPIC_API_KEY`. On Claude Platform on AWS, send the requests to `https://aws-external-anthropic.{region}.api.aws` instead, signed with your AWS credentials as in [Making requests](../Guides/build-with-claude-claude-platform-on-aws.md#making-requests). There, your [IAM policy](../Endpoints/claude-platform-on-aws-iam-actions.md) determines who can manage destinations. A request can include only the workspaces of your AWS account in that Region.

CLI

cURL

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
client = anthropic.Anthropic()

destination = client.beta.organization.telemetry_destinations.create(
    endpoint_url="https://gateway.example.com/otlp",
    headers={"authorization": "Bearer YOUR_OBSERVABILITY_API_KEY"},
    traces={"content_mode": "metadata_only"},
    workspaces={"type": "all"},
)

print(destination.id)
```

A create request takes the Console's settings except **Provider**, so enter your observability platform's endpoint URL and headers yourself. Set `traces.max_content_bytes`, in bytes, to fit what your observability platform accepts (see [Content limits](manage-claude-opentelemetry.md#content-limits)). To list, change, or delete destinations, or to add or remove one workspace, use the other methods of the [telemetry destinations API](../Admin/beta-organization-telemetry-destinations.md).

## 2. Choose workspaces for a destination

A destination receives the spans of the workspaces that it covers. Choose them when you add the destination. For **Workspaces**, select one of the following:

- **All:** Every workspace in the organization, including the [Default Workspace](manage-claude-workspaces.md#how-workspaces-work) and workspaces created later.
- **Selected:** Only the workspaces that you select.
- **All except:** Like **All**, but without the workspaces that you select.

For **Selected** or **All except**, select the workspaces in the search box that appears under the options. To change a destination's workspaces later, open its **More actions** menu on the [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations) in the Console while the **Workspace** filter shows **All**. Click **Edit**, then choose another **Workspaces** option or change the workspaces in the search box.

If you have the developer role in the organization and the Workspace Admin role in a workspace, you can add that workspace to a **Selected** destination or remove it. Set the **Workspace** filter to that workspace, then open the destination's **More actions** menu. On Claude Platform on AWS, the Console has no Workspace Admin role. There, your [IAM policy](../Endpoints/claude-platform-on-aws-iam-actions.md) determines who can add a workspace to a destination or remove it.

The API sends spans to every enabled destination that covers the [workspace where the request or session runs](manage-claude-workspaces.md#api-keys-and-resource-scoping).

## 3. Check that spans arrive

1.  In the Console, select a workspace that the destination covers and send a Messages API request in [playground](playground.md). You can also send a Messages API request from your application or start a Managed Agents session in that workspace. To start a session, you can follow the steps in [Get started with Claude Managed Agents](managed-agents-quickstart.md).
2.  In the Console, on the [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations), check that the **Delivery** column shows **Healthy** for the destination. This can take about a minute.
3.  In your observability platform, filter on `service.name` = `claude-platform` to find the request's spans.

If the column shows **Failing**, hover over it to see the last error. To find the likely cause, see [Delivery errors](#delivery-errors).

## 4. Connect API spans to your own traces

By default, the API spans for a Messages API request or a Managed Agents session are in their own traces. Connect them to your application's traces, so that they nest under your own spans.

The API reads each request's trace context from the W3C [`traceparent` header](https://www.w3.org/TR/trace-context/). If the sampled flag in the header is off, the API doesn't emit the request's span or the spans under it.

With the Claude SDK

With other clients

With the Claude SDK

To connect the API spans, [set up SDK tracing](manage-claude-opentelemetry-sdk.md) in your application and call the SDK from inside one of your own spans. Your span then contains the SDK span, which contains the API span. Send all of these spans to the same observability platform, so that it can show them as one trace. See the example traces of [a Messages API request](manage-claude-opentelemetry.md#a-messages-api-request) and [a Managed Agents session](manage-claude-opentelemetry.md#a-managed-agents-session).

The following example sends a user message to a session inside your own span:

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
from opentelemetry import trace

tracer = trace.get_tracer("my-service")

with tracer.start_as_current_span("summarize_issues"):
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "Summarize the open issues"}],
            },
        ],
    )
```

The SDK writes the `traceparent` header with your application's propagator, and the sampled flag in it follows your sampler. If your application uses a propagator other than W3C trace context, such as B3, also add the W3C trace context propagator.

With other clients

Copy the current span's trace context into the request headers, for example when you create a Managed Agents session or send a user message:

cURL

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
import os
import httpx2
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

headers = {
    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
    "anthropic-version": "2023-06-01",
    "anthropic-beta": "managed-agents-2026-04-01",
    "content-type": "application/json",
}
# Copy the active span's trace context into the request headers.
TraceContextTextMapPropagator().inject(headers)

httpx2.post(
    f"https://api.anthropic.com/v1/sessions/{os.environ['SESSION_ID']}/events",
    headers=headers,
    json={
        "events": [
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "Summarize the open issues"}],
            },
        ],
    },
)
```

When you connect your MCP server with the [Messages API's MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md) or the [Managed Agents MCP connector](managed-agents-mcp-connector.md), the API also passes the trace on to your server. The server can then put its own spans under the API spans. In `params._meta` of a `tools/call` request, the API sends a W3C `traceparent` that references the [`anthropic.mcp_tool_use`](../Endpoints/opentelemetry-spans.md#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) span for that tool use. With the Messages API's MCP connector, the other requests and notifications to your MCP server have a `traceparent` too, which references the [`anthropic.messages.create`](../Endpoints/opentelemetry-spans.md#anthropic-messages-create) span. If the API doesn't trace your Messages API request, such as when its `traceparent` header has the sampled flag off, your MCP server gets no `traceparent`.

## Next steps



[Set up SDK tracing](manage-claude-opentelemetry-sdk.md)

Get observability into your client.

[See example traces](manage-claude-opentelemetry.md#example-traces-and-how-to-read-them)

Follow a request from your client into the Claude API.

## Delivery and health

The following rules apply to the spans that the API sends to your destinations.

- **At least once:** A destination can receive the same span more than once. To remove duplicates, use the trace ID and span ID.
- **Best effort:** A span can be lost before delivery. The API can't send a lost span again.
- **Compression:** The API compresses requests with gzip and sets the header `Content-Encoding: gzip`. If your endpoint answers a compressed request with a `400`, `406`, `415`, or `422` response, the API sends the same spans again right away without compression. It then usually sends that destination's later requests without compression for about a day.
- **Retries:** The API retries a delivery later, a limited number of times, after a timeout, a connection, TLS, or DNS failure, an invalid address, or a `408`, `429`, or `5xx` response. It doesn't retry other failures.
- **Timeouts:** For each request, your endpoint must complete the TLS handshake within 5 seconds and send the response headers within 5 seconds. Each delivery times out after 10 seconds in total, including any resend.
- **User agent:** Each request has the header `User-Agent: Claude-Platform`.

The **Delivery** column shows each destination's state. The state can be up to a minute late.

| Delivery state | Meaning                                                                     |
|----------------|-----------------------------------------------------------------------------|
| **Healthy**    | The last delivery succeeded.                                                |
| **Failing**    | The last delivery failed. To see the error, hover over **Failing**.         |
| **No data**    | The API hasn't tried a delivery yet.                                        |
| **Disabled**   | The destination doesn't receive spans. To see why, hover over **Disabled**. |

The API disables a destination when:

- The endpoint sends a `3xx` redirect.
- All deliveries fail for 24 hours.

While a destination is disabled, the API drops the spans for it, and they aren't sent after you enable it again. To resume export, fix the cause and check the fix with **Test** in the destination's **More actions** menu. Then, on the [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations) in the Console, click **Enable** in the same menu while the **Workspace** filter shows **All**. Export starts again within about a minute. Until the next delivery, the **Delivery** column can still show **Failing** with the old error.

To change a destination, open its **More actions** menu while the **Workspace** filter shows **All**. Then click **Edit**, **Disable**, **Enable**, or **Delete**. If you change the host of the **OTLP endpoint URL**, enter the header values again. If the destination has an **OTLP traces endpoint URL**, give it the same new host, or clear it.

## Limits

| Limit                                                       | Value            |
|-------------------------------------------------------------|------------------|
| Destinations for each organization, including disabled ones | 10               |
| Workspaces that you select for a destination                | 1,000            |
| Request headers for each destination                        | 20               |
| Length of a header name                                     | 128 bytes        |
| Length of a header value                                    | 4,096 bytes      |
| Length of all header names and values together              | 16,384 bytes     |
| Length of an endpoint URL                                   | 2,048 characters |

## Troubleshooting

| Problem                                                                            | What to check                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No API spans                                                                       | The workspace needs an enabled destination that covers it. See [Choose workspaces for a destination](#choose-workspaces-for-a-destination). After a destination starts covering a workspace, spans from that workspace can take up to a minute to arrive. The API emits no span for a request whose `traceparent` header has the sampled flag off, or for a request to the [OpenAI-compatible endpoint](cli-sdks-libraries-libraries-openai-sdk.md). |
| The **Delivery** column shows **Failing**                                          | Hover over it to see the last error. To find the likely cause, see [Delivery errors](#delivery-errors).                                                                                                                                                                                                                                                                                                                                                    |
| The **Delivery** column shows **Disabled**                                         | Hover over it to see why. For the reasons, see [when the API disables a destination](#delivery-and-health).                                                                                                                                                                                                                                                                                                                                                |
| Spans have no prompts or responses, but the destination is set to **Full content** | Your organization might have a HIPAA, FERPA, or K-12 data-handling restriction with Anthropic. See [Content modes](manage-claude-opentelemetry.md#choose-a-content-mode).                                                                                                                                                                                                                                                                            |

### Delivery errors

When a delivery fails, the **Delivery** column shows **Failing**. Hover over it to see the error, then find the likely cause:

| Error                                              | Likely cause                                                                                           |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| HTTP error (status 401) or HTTP error (status 403) | A wrong authentication header                                                                          |
| HTTP error (status 404)                            | A wrong path in the **OTLP endpoint URL** or the **OTLP traces endpoint URL**                          |
| Invalid address                                    | The endpoint's hostname doesn't exist or doesn't resolve to a public IP address                        |
| Temporary DNS failure                              | The DNS lookup of the endpoint's hostname failed, for example because its DNS server returned an error |
| TLS failure                                        | A TLS problem, for example with the endpoint's certificate                                             |
| Timeout                                            | The endpoint didn't respond in time. See [the delivery timeouts](#delivery-and-health)                 |
| Connection failure                                 | The API couldn't connect to the endpoint                                                               |
| Redirect (status 3xx)                              | The endpoint redirected the request. The API doesn't follow redirects, so use the URL it redirects to  |
| HTTP error (status 408, 429, or 5xx)               | The endpoint was overloaded, limited the rate of requests, or had an error                             |
| HTTP error (another 4xx status)                    | The endpoint refused the request, for example because of its size or format                            |

## Compatibility

Supported platforms  
- Claude APIBeta
- Claude Platform on AWSBeta

Works with  
Messages API, Claude Managed Agents

- After delivery, the data is held by the service that you chose, outside Anthropic, under that service's retention and access controls.
