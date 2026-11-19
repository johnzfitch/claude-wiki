---
title: "API overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/overview"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:20Z"
tags: ["api", "authentication", "cli", "sdk"]
---

# API overview

Copy page



Understand the Claude API’s available endpoints, authentication headers, client SDKs, pagination, rate limits, and cloud platform access options.

Copy page



The Claude API is a RESTful API at `https://api.anthropic.com` that provides programmatic access to Claude models and Claude Managed Agents.



**New to Claude?** For direct model access, start with [Get started](../../01-Getting-Started/get-started.md) and [Working with Messages](../Guides/build-with-claude-working-with-messages.md). For managed agent infrastructure, see the [Claude Managed Agents quickstart](../Other/managed-agents-quickstart.md).

## Prerequisites

To use the Claude API, you need:

- A [Claude Console account](../Other/playground.md)
- An [API key](../Other/playground.md) from the Console, or a configured [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md) rule

For step-by-step setup instructions, see [Get started](../../01-Getting-Started/get-started.md).

## Available APIs

The Claude API includes the following APIs:

- **[Messages API](messages-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.:** Send messages to Claude for conversational interactions (`POST /v1/messages`)
- **[Message Batches API](messages-batches-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.:** Process large volumes of Messages requests asynchronously with a 50 percent cost reduction (`POST /v1/messages/batches`)
- **[Token Counting API](platform-claude-com-messages-count-tokens.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.:** Count tokens in a message before sending to manage costs and rate limits (`POST /v1/messages/count_tokens`)
- **[Models API](models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.:** List available Claude models and their details (`GET /v1/models`)
- **[Files API](files-upload.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.:** Upload and manage files for use across multiple API calls (`POST /v1/files`, `GET /v1/files`)
- **[Skills API](skills-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.:** Create and manage custom agent skills (`POST /v1/skills`, `GET /v1/skills`)

The following APIs are in beta:

- **[Agents API](../Other/managed-agents-agent-setup.md):** Define reusable, versioned agent configurations for Claude Managed Agents (`POST /v1/agents`, `GET /v1/agents`)
- **[Sessions API](../Other/managed-agents-sessions.md):** Run stateful agent sessions in managed cloud sandboxes (`POST /v1/sessions`, `GET /v1/sessions/{id}/events/stream`)
- **[Environments API](../Other/managed-agents-environments.md):** Configure sandbox templates for agent sessions (`POST /v1/environments`, `GET /v1/environments`)

For the complete API reference with all endpoints, parameters, and response schemas, explore the API reference pages listed in the navigation. To access beta features, see [Beta headers](beta-headers.md).

## Authentication

For details on each authentication method and when to use it, see [Authentication](../Other/manage-claude-authentication.md). Requests to the Claude API include these headers:

| Header | Value | Required |
|----|----|----|
| `Authorization` | `Bearer <token>`, where `<token>` is your API key or a short-lived access token obtained from `POST /v1/oauth/token` through [Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md) | Yes, unless `x-api-key` is set |
| `x-api-key` | Your API key from Console. Legacy fallback for `Authorization`, still supported | No |
| `anthropic-workspace-id` | ID of the [workspace](../Other/manage-claude-workspaces.md) the request runs in (for example, `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`). See [Select a workspace](../Other/manage-claude-authentication.md#select-a-workspace). | Required with an API key that isn’t scoped to a workspace. Optional for other API keys. A key created for a single workspace runs in that workspace when you omit the header. Not used with Workload Identity Federation tokens, which select a workspace at token exchange. |
| `anthropic-version` | API version (for example, `2026-10-21`) | Yes |
| `content-type` | `application/json` | Yes |

If you are using the [Client SDKs](#client-sdks), the SDK sends the authentication, version, and content-type headers automatically; you pass `anthropic-workspace-id` yourself when your key needs it. For API versioning details, see [API versions](versioning.md).

When accessing Claude through a [cloud platform](#claude-api-vs-cloud-platforms), authentication is integrated with the cloud provider’s IAM system. See the platform-specific documentation for supported credential types, required headers, and authentication options.

### Getting API keys

The API is made available through the web [Console](../Other/playground.md). In the Console, you can use [playground](../Other/playground.md) (`platform.claude.com/playground`) to try out the API in the browser and then generate API keys on the [API keys](../Other/playground.md) page (`platform.claude.com/settings/keys`). To learn how, see [Get your Claude API key](../Other/get-api-key.md). You choose each key’s type (see [Key types](../Other/manage-claude-authentication.md#key-types)) and its [expiration](../Other/manage-claude-authentication.md#key-expiration) when you create it. Use [workspaces](../Other/playground.md) in the Console to separate environments and [control spend](rate-limits.md) by use case.

## Client SDKs

Anthropic provides official SDKs that simplify API integration by handling authentication, request formatting, error handling, and more.

**Benefits:**

- Automatic header management (authentication, `anthropic-version`, `content-type`)
- Type-safe request and response handling
- Built-in retry logic and error handling
- Streaming support
- Request timeouts and connection management

For a list of client SDKs, see [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md).

## Claude API versus cloud platforms

Claude is available through the first-party Claude API and through cloud platforms. Choose based on your infrastructure, feature availability, compliance requirements, and pricing preferences.

### Claude API

- **Direct access** to the latest models and features
- **Anthropic billing and support**
- **Best for:** New integrations, full feature access, direct relationship with Anthropic

### Cloud platform APIs

Access Claude through AWS, Google Cloud, or Microsoft Azure:

- **Integrated** with cloud provider billing and IAM
- **Feature availability varies by platform:** Anthropic-operated platforms include [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md), and [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md); partner-operated platforms include Claude Models on Google Cloud (Google managed) and Amazon Bedrock. See each platform’s page for feature availability and timing.
- **Best for:** Existing cloud commitments, specific compliance requirements, consolidated cloud billing

| Platform | Provider | Documentation |
|----|----|----|
| Claude Models on Google Cloud (Google managed) | Google Cloud | [Claude Models on Google Cloud (Google managed)](../Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md) |
| Amazon Bedrock | AWS | [Claude in Amazon Bedrock (`bedrock-mantle`)](../Guides/build-with-claude-claude-in-amazon-bedrock.md) and [Claude on Amazon Bedrock (`bedrock-runtime`)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md) |
| Claude Platform on AWS | AWS (Anthropic-operated) | [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md) |
| Claude Models on Google Cloud (Anthropic managed) | Google Cloud (Anthropic-operated) | [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md) |
| Microsoft Foundry | Microsoft Azure (Anthropic-operated) | [Claude in Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md) |



Claude Managed Agents is available through the first-party Claude API, [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), and [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md). For feature availability across platforms, see the [Features overview](../Guides/build-with-claude-overview.md).

## Request and response format

### Request size limits

The first-party Claude API enforces these request size limits:

| Endpoint | Maximum request size |
|----|----|
| Messages, Token Counting | 128 MB |
| Message Batches API (see [Batch processing](../Guides/build-with-claude-batch-processing.md)) | 256 MB |
| [Files API](../Guides/build-with-claude-files.md) | 500 MB |
| Sessions, Agents, Environments | 32 MB |

If you exceed these limits, you’ll receive a 413 `request_too_large` error.



Partner-operated platforms have their own request size limits: Bedrock limits requests to 20 MB, and Claude Models on Google Cloud (Google managed) limits requests to 30 MB. Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed), and Microsoft Foundry support Messages and Token Counting requests of up to 32 MB. Consult your platform’s documentation for current values.

### Response headers

The Claude API includes the following headers in its responses:

| Header | Description |
|----|----|
| `request-id` | A globally unique identifier for the request, such as `req_018EeWyXxfu5pfWkrYcMdjWG`. Include it when you contact support about a specific request. See [Request ID](errors.md#request-id). |
| `anthropic-organization-id` | The ID of the organization that the API key or access token used in the request belongs to. |
| `anthropic-workspace-id` | The `wrkspc_`-prefixed ID of the [workspace](../Other/manage-claude-workspaces.md) that the API key or access token resolved to, such as `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`, including when that is your organization’s Default Workspace. Absent when the credential doesn’t resolve to a workspace (for example, on Admin API requests) or the request fails before authentication completes. See [Identify the workspace behind an API response](../Other/manage-claude-workspaces.md#identify-the-workspace-behind-an-api-response). |

For the rate limit headers, see [Response headers](rate-limits.md#response-headers) in Rate limits. For examples that read a response header by name with each SDK, see [Identify the workspace behind an API response](../Other/manage-claude-workspaces.md#identify-the-workspace-behind-an-api-response).



Claude Platform on AWS adds an AWS request ID (`x-amzn-requestid`) alongside the standard `request-id` header. See [Request IDs](../Guides/build-with-claude-claude-platform-on-aws.md#request-ids) for the dual-ID handling pattern.

## Pagination

List endpoints return results in pages. Most newer list endpoints use the `page` and `next_page` cursor scheme described in this section. Some use a different scheme; see the note at the end of this section. Use the `limit` query parameter to control the page size and the `page` query parameter to fetch an adjacent page. Each response includes a `data` array alongside cursor fields for navigating between pages.

| Name | Location | Description |
|----|----|----|
| `limit` | Query parameter | Maximum number of items to return per page. |
| `page` | Query parameter | Opaque cursor from a previous response. Pass a `next_page` or `prev_page` value here to fetch the adjacent page. |
| `order` | Query parameter | Sort direction for the results (`asc` or `desc`), on list endpoints that support sorting. A `page` cursor is only valid with the `order` it was created with. |
| `next_page` | Response field | Cursor for the next page, or `null` if there are no more results. |
| `prev_page` | Response field | Cursor for the previous page on endpoints that support backward pagination (currently `GET /v1/sessions`), or `null` if you are on the first page. Other list endpoints omit the field. |

To go back a page, pass `prev_page` as the `page` parameter. `prev_page` is `null` when you’re on the first page. Not all list endpoints support `prev_page`. Only `GET /v1/sessions` returns `prev_page`; on list endpoints that do not support backward pagination, the field is absent from the response rather than `null`. For a request walkthrough, see [Listing sessions](../Other/managed-agents-session-operations.md#listing-sessions).

The SDK provides an auto-paginating iterator that follows `next_page` for you. For example, `for session in client.beta.sessions.list()` walks through every session. SDK auto-pagination is forward-only; to go back a page, read `prev_page` from the response and pass it back as the `page` parameter yourself. See [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md) for details.



Some list endpoints use a different cursor scheme. The Message Batches API (see [Batch processing](../Guides/build-with-claude-batch-processing.md)), the [Models API](models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., and several [Admin API](../Other/manage-claude-admin-api.md) endpoints take `after_id` and `before_id` query parameters instead of `page`. Their responses return `has_more`, `first_id`, and `last_id` instead of `next_page`. See the reference page for each endpoint for its exact pagination fields.

## Rate limits and availability

### Rate limits

The API enforces rate limits and spend limits to prevent misuse and manage capacity. Limits are organized into usage tiers; your organization is placed on a tier automatically and can move to a higher tier over time. Each tier has:

- **Spend limits:** Maximum monthly cost for API usage
- **Rate limits:** Maximum number of requests per minute (RPM) and tokens per minute (TPM)

You can view your rate limits under [Rate limits in the Claude Console](../Other/playground.md). Your spend limits are under [Spend limits in the Claude Console](https://platform.claude.com/settings/spend-limits) (`platform.claude.com/settings/spend-limits`). For higher rate limits or a higher monthly spend cap, use **Request tier increase** on the **Rate limits** page.

For detailed information about limits, tiers, and the token bucket algorithm used for rate limiting, see [Rate limits](rate-limits.md).

### Availability

The Claude API is available in [many countries and regions](supported-regions.md) worldwide. Check the supported regions page to confirm availability in your location.

## Next steps



[Messages API reference](messages-create.md)

Complete API specification for direct model interactions



[Claude Managed Agents reference](../Other/managed-agents-sessions.md)

Agents, Sessions, and Environments endpoints



[Client SDKs](../Other/cli-sdks-libraries-overview.md)

Python, TypeScript, C#, Go, Java, PHP, and Ruby



[Rate limits](rate-limits.md)

Usage tiers, requesting higher limits, and the token bucket algorithm
