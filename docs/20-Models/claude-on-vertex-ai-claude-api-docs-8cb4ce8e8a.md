---
category: "20-Models"
fetched_at: "2026-02-07T10:04:51Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai"
title: "Claude on Vertex AI - Claude API Docs"
---

Claude on 3rd-party platforms

# Claude on Vertex AI

Copy page

Anthropic's Claude models are now generally available through [Vertex AI](https://cloud.google.com/vertex-ai).

Copy page

The Vertex API for accessing Claude is nearly-identical to the [Messages API](/docs/en/api/messages) and supports all of the same options, with two key differences:

- In Vertex, `model` is not passed in the request body. Instead, it is specified in the Google Cloud endpoint URL.
- In Vertex, `anthropic_version` is passed in the request body (rather than as a header), and must be set to the value `vertex-2023-10-16`.

Vertex is also supported by Anthropic's official [client SDKs](/docs/en/api/client-sdks). This guide will walk you through the process of making a request to Claude on Vertex AI in either Python or TypeScript.

Note that this guide assumes you have already have a GCP project that is able to use Vertex AI. See [using the Claude 3 models from Anthropic](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) for more information on the setup required, as well as a full walkthrough.

## 

Install an SDK for accessing Vertex AI

First, install Anthropic's [client SDK](/docs/en/api/client-sdks) for your language of choice.

Python

Python

TypeScript

TypeScript

Java

Java

Go

Go

``` shiki
pip install -U google-cloud-aiplatform "anthropic[vertex]"
```

## 

Accessing Vertex AI

### 

Model Availability

Note that Anthropic model availability varies by region. Search for "Claude" in the [Vertex AI Model Garden](https://cloud.google.com/model-garden) or go to [Use Claude 3](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude) for the latest information.

#### 

API model IDs

| Model                | Vertex AI API model ID     |
|----------------------|----------------------------|
| Claude Opus 4.6      | claude-opus-4-6            |
| Claude Sonnet 4.5    | claude-sonnet-4-5@20250929 |
| Claude Sonnet 4      | claude-sonnet-4@20250514   |
| Claude Sonnet 3.7 ⚠️ | claude-3-7-sonnet@20250219 |
| Claude Opus 4.5      | claude-opus-4-5@20251101   |
| Claude Opus 4.1      | claude-opus-4-1@20250805   |
| Claude Opus 4        | claude-opus-4@20250514     |
| Claude Haiku 4.5     | claude-haiku-4-5@20251001  |
| Claude Haiku 3.5 ⚠️  | claude-3-5-haiku@20241022  |
| Claude Haiku 3       | claude-3-haiku@20240307    |

### 

Making requests

Before running requests you may need to run `gcloud auth application-default login` to authenticate with GCP.

The following examples shows how to generate text from Claude on Vertex AI:

Python

``` shiki
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "global"

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

See our [client SDKs](/docs/en/api/client-sdks) and the official [Vertex AI docs](https://cloud.google.com/vertex-ai/docs) for more details.

Claude is also available through [Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock) and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry).

## 

Activity logging

Vertex provides a [request-response logging service](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/request-response-logging) that allows customers to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis in order to understand your activity and investigate any potential misuse.

Turning on this service does not give Google or Anthropic any access to your content.

## 

Feature support

You can find all the features currently supported on Vertex [here](/docs/en/api/overview).

## 

Global vs regional endpoints

Starting with **Claude Sonnet 4.5 and all future models**, Google Vertex AI offers two endpoint types:

- **Global endpoints**: Dynamic routing for maximum availability
- **Regional endpoints**: Guaranteed data routing through specific geographic regions

Regional endpoints include a 10% pricing premium over global endpoints.

This applies to Claude Sonnet 4.5 and future models only. Older models (Claude Sonnet 4, Opus 4, and earlier) maintain their existing pricing structures.

### 

When to use each option

**Global endpoints (recommended):**

- Provide maximum availability and uptime
- Dynamically route requests to regions with available capacity
- No pricing premium
- Best for applications where data residency is flexible
- Only supports pay-as-you-go traffic (provisioned throughput requires regional endpoints)

**Regional endpoints:**

- Route traffic through specific geographic regions
- Required for data residency and compliance requirements
- Support both pay-as-you-go and provisioned throughput
- 10% pricing premium reflects infrastructure costs for dedicated regional capacity

### 

Implementation

**Using global endpoints (recommended):**

Set the `region` parameter to `"global"` when initializing the client:

Python

``` shiki
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "global"

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

**Using regional endpoints:**

Specify a specific region like `"us-east1"` or `"europe-west1"`:

Python

``` shiki
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "us-east1"  # Specify a specific region

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

### 

Additional resources

- **Google Vertex AI pricing:** [cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)
- **Claude models documentation:** [Claude on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude)
- **Google blog post:** [Global endpoint for Claude models](https://cloud.google.com/blog/products/ai-machine-learning/global-endpoint-for-claude-models-generally-available-on-vertex-ai)
- **Anthropic pricing details:** [Pricing documentation](/docs/en/about-claude/pricing#third-party-platform-pricing)

Was this page helpful?

- 

- [Install an SDK for accessing Vertex AI](#install-an-sdk-for-accessing-vertex-ai)

- [Accessing Vertex AI](#accessing-vertex-ai)

- [Model Availability](#model-availability)

- [Making requests](#making-requests)

- [Activity logging](#activity-logging)

- [Feature support](#feature-support)

- [Global vs regional endpoints](#global-vs-regional-endpoints)

- [When to use each option](#when-to-use-each-option)

- [Implementation](#implementation)

- [Additional resources](#additional-resources)

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
