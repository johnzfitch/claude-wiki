---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:05:07Z"
source_url: "https://platform.claude.com/docs/en/api/overview"
title: "API Overview - Claude API Docs"
---

Using the API

# API Overview

Copy page

Copy page

The Claude API is a RESTful API at `https://api.anthropic.com` that provides programmatic access to Claude models. The primary API is the Messages API (`POST /v1/messages`) for conversational interactions.

**New to Claude?** Start with [Get started](/docs/en/get-started) for prerequisites and your first API call, or see [Working with Messages](/docs/en/build-with-claude/working-with-messages) for request/response patterns and examples.

## 

Prerequisites

To use the Claude API, you'll need:

- An [Anthropic Console account](https://platform.claude.com)
- An [API key](/settings/keys)

For step-by-step setup instructions, see [Get started](/docs/en/get-started).

## 

Available APIs

The Claude API includes the following APIs:

**General Availability:**

- **[Messages API](/docs/en/api/messages)**: Send messages to Claude for conversational interactions (`POST /v1/messages`)
- **[Message Batches API](/docs/en/api/creating-message-batches)**: Process large volumes of Messages requests asynchronously with 50% cost reduction (`POST /v1/messages/batches`)
- **[Token Counting API](/docs/en/api/messages-count-tokens)**: Count tokens in a message before sending to manage costs and rate limits (`POST /v1/messages/count_tokens`)
- **[Models API](/docs/en/api/models-list)**: List available Claude models and their details (`GET /v1/models`)

**Beta:**

- **[Files API](/docs/en/api/files-create)**: Upload and manage files for use across multiple API calls (`POST /v1/files`, `GET /v1/files`)
- **[Skills API](/docs/en/api/skills/create-skill)**: Create and manage custom agent skills (`POST /v1/skills`, `GET /v1/skills`)

For the complete API reference with all endpoints, parameters, and response schemas, explore the API reference pages listed in the navigation. To access beta features, see [Beta headers](/docs/en/api/beta-headers).

The Messages API supports an optional `inference_geo` parameter for [data residency controls](/docs/en/build-with-claude/data-residency), allowing you to specify where model inference runs.

## 

Authentication

All requests to the Claude API must include these headers:

| Header              | Value                            | Required |
|---------------------|----------------------------------|----------|
| `x-api-key`         | Your API key from Console        | Yes      |
| `anthropic-version` | API version (e.g., `2023-06-01`) | Yes      |
| `content-type`      | `application/json`               | Yes      |

If you are using the [Client SDKs](#client-sdks), the SDK will send these headers automatically. For API versioning details, see [API versions](/docs/en/api/versioning).

### 

Getting API Keys

The API is made available via the web [Console](https://platform.claude.com/). You can use the [Workbench](https://platform.claude.com/workbench) to try out the API in the browser and then generate API keys in [Account Settings](https://platform.claude.com/settings/keys). Use [workspaces](https://platform.claude.com/settings/workspaces) to segment your API keys and [control spend](/docs/en/api/rate-limits) by use case.

## 

Client SDKs

Anthropic provides official SDKs that simplify API integration by handling authentication, request formatting, error handling, and more.

**Benefits**:

- Automatic header management (x-api-key, anthropic-version, content-type)
- Type-safe request and response handling
- Built-in retry logic and error handling
- Streaming support
- Request timeouts and connection management

**Example** (Python):

``` shiki
from anthropic import Anthropic

client = Anthropic()  # Reads ANTHROPIC_API_KEY from environment
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}]
)
```

For a list of client SDKs and their respective installation instructions, see [Client SDKs](/docs/en/api/client-sdks).

## 

Claude API vs Third-Party Platforms

Claude is available through Anthropic's direct API and through partner platforms. Choose based on your infrastructure, compliance requirements, and pricing preferences.

### 

Claude API

- **Direct access** to the latest models and features first
- **Anthropic billing and support**
- **Best for**: New integrations, full feature access, direct relationship with Anthropic

### 

Third-Party Platform APIs

Access Claude through AWS, Google Cloud, or Microsoft Azure:

- **Integrated** with cloud provider billing and IAM
- **May have feature delays** or differences from the direct API
- **Best for**: Existing cloud commitments, specific compliance requirements, consolidated cloud billing

| Platform | Provider | Documentation |
|----|----|----|
| Amazon Bedrock | AWS | [Claude on Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock) |
| Vertex AI | Google Cloud | [Claude on Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai) |
| Azure AI | Microsoft Azure | [Claude on Azure AI](/docs/en/build-with-claude/claude-in-microsoft-foundry) |

For feature availability across platforms, see the [Features overview](/docs/en/build-with-claude/overview).

## 

Request and Response Format

### 

Request Size Limits

The API has different maximum request sizes depending on the endpoint:

| Endpoint                                                 | Maximum Size |
|----------------------------------------------------------|--------------|
| Standard endpoints (Messages, Token Counting)            | 32 MB        |
| [Batch API](/docs/en/build-with-claude/batch-processing) | 256 MB       |
| [Files API](/docs/en/build-with-claude/files)            | 500 MB       |

If you exceed these limits, you'll receive a 413 `request_too_large` error.

### 

Response Headers

The Claude API includes the following headers in every response:

- `request-id`: A globally unique identifier for the request
- `anthropic-organization-id`: The organization ID associated with the API key used in the request

## 

Rate Limits and Availability

### 

Rate Limits

The API enforces rate limits and spend limits to prevent misuse and manage capacity. Limits are organized into usage tiers that increase automatically as you use the API. Each tier has:

- **Spend limits**: Maximum monthly cost for API usage
- **Rate limits**: Maximum number of requests per minute (RPM) and tokens per minute (TPM)

You can view your organization's current limits in the [Console](/settings/limits). For higher limits or Priority Tier (enhanced service levels with committed spend), contact sales through the Console.

For detailed information about limits, tiers, and the token bucket algorithm used for rate limiting, see [Rate limits](/docs/en/api/rate-limits).

### 

Availability

The Claude API is available in [many countries and regions](/docs/en/api/supported-regions) worldwide. Check the supported regions page to confirm availability in your location.

## 

Basic Example

Here's a minimal request using the Messages API:

``` shiki
curl https://api.anthropic.com/v1/messages \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Hello, Claude"}
    ]
  }'
```

**Response:**

``` shiki
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello! How can I assist you today?"
    }
  ],
  "model": "claude-opus-4-6",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 12,
    "output_tokens": 8
  }
}
```

For complete examples and tutorials, see [Get started](/docs/en/get-started) and [Working with Messages](/docs/en/build-with-claude/working-with-messages).

## 

Next Steps

[](/docs/en/get-started)

Get started

Prerequisites, step-by-step tutorial, and examples in multiple languages

[](/docs/en/build-with-claude/working-with-messages)

Working with Messages

Request/response patterns, multi-turn conversations, and best practices

[](/docs/en/api/messages)

Messages API Reference

Complete API specification: parameters, responses, and error codes

[](/docs/en/api/client-sdks)

Client SDKs

Installation guides for Python, TypeScript, Java, Go, C#, Ruby, and PHP

[](/docs/en/build-with-claude/overview)

Features overview

Explore capabilities: caching, vision, tool use, streaming, and more

[](/docs/en/api/rate-limits)

Rate limits

Usage tiers, spend limits, and rate limiting with token bucket algorithm

Was this page helpful?

- 

- [Prerequisites](#prerequisites)

- [Available APIs](#available-apis)

- [Authentication](#authentication)

- [Getting API Keys](#getting-api-keys)

- [Client SDKs](#client-sdks)

- [Claude API vs Third-Party Platforms](#claude-api-vs-third-party-platforms)

- [Claude API](#claude-api)

- [Third-Party Platform APIs](#third-party-platform-apis)

- [Request and Response Format](#request-and-response-format)

- [Request Size Limits](#request-size-limits)

- [Response Headers](#response-headers)

- [Rate Limits and Availability](#rate-limits-and-availability)

- [Rate Limits](#rate-limits)

- [Availability](#availability)

- [Basic Example](#basic-example)

- [Next Steps](#next-steps)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
