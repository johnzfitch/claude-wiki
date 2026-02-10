---
category: "20-Models"
fetched_at: "2026-02-07T10:04:50Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry"
title: "Claude in Microsoft Foundry - Claude API Docs"
---

Claude on 3rd-party platforms

# Claude in Microsoft Foundry

Copy page

Access Claude models through Microsoft Foundry with Azure-native endpoints and authentication.

Copy page

This guide will walk you through the process of setting up and making API calls to Claude in Foundry in Python, TypeScript, or using direct HTTP requests. When you can access Claude in Foundry, you will be billed for Claude usage in the Microsoft Marketplace with your Azure subscription, allowing you to access Claude's latest capabilities while managing costs through your Azure subscription.

Regional availability: At launch, Claude is available as a Global Standard deployment type in Foundry resources (US DataZone coming soon). Pricing for Claude in the Microsoft Marketplace uses Anthropic's standard API pricing. Visit the [pricing page](https://claude.com/pricing#api) for details.

## 

Preview

In this preview platform integration, Claude models run on Anthropic's infrastructure. This is a commercial integration for billing and access through Azure. As an independent processor for Microsoft, customers using Claude through Microsoft Foundry are subject to Anthropic's data use terms. Anthropic continues to provide its industry-leading safety and data commitments, including zero data retention availability.

## 

Prerequisites

Before you begin, ensure you have:

- An active Azure subscription
- Access to [Foundry](https://ai.azure.com/)
- The [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed (optional, for resource management)

## 

Install an SDK

Anthropic's [client SDKs](/docs/en/api/client-sdks) support Foundry through platform-specific packages.

Python

Python

TypeScript

TypeScript

C#

C#

``` shiki
pip install -U "anthropic"
```

## 

Provisioning

Foundry uses a two-level hierarchy: **resources** contain your security and billing configuration, while **deployments** are the model instances you call via API. You'll first create a Foundry resource, then create one or more Claude deployments within it.

### 

Provisioning Foundry resources

Create a Foundry resource, which is required to use and manage services in Azure. You can follow these instructions to create a [Foundry resource](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource?pivots=azportal#create-a-new-azure-ai-foundry-resource). Alternatively, you can start by creating a [Foundry project](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry), which involves creating a Foundry resource.

To provision your resource:

1.  Navigate to the [Foundry portal](https://ai.azure.com/)
2.  Create a new Foundry resource or select an existing one
3.  Configure access management using Azure-issued API keys or Entra ID for role-based access control
4.  Optionally configure the resource to be part of a private network (Azure Virtual Network) for enhanced security
5.  Note your resource name—you'll use this as `{resource}` in API endpoints (e.g., `https://{resource}.services.ai.azure.com/anthropic/v1/*`)

### 

Creating Foundry deployments

After creating your resource, deploy a Claude model to make it available for API calls:

1.  In the Foundry portal, navigate to your resource
2.  Go to **Models + endpoints** and select **+ Deploy model** \> **Deploy base model**
3.  Search for and select a Claude model (e.g., `claude-sonnet-4-5`)
4.  Configure deployment settings:
    - **Deployment name**: Defaults to the model ID, but you can customize it (e.g., `my-claude-deployment`). The deployment name cannot be changed after it has been created.
    - **Deployment type**: Select Global Standard (recommended for Claude)
5.  Select **Deploy** and wait for provisioning to complete
6.  Once deployed, you can find your endpoint URL and keys under **Keys and Endpoint**

The deployment name you choose becomes the value you pass in the `model` parameter of your API requests. You can create multiple deployments of the same model with different names to manage separate configurations or rate limits.

## 

Authentication

Claude on Foundry supports two authentication methods: API keys and Entra ID tokens. Both methods use Azure-hosted endpoints in the format `https://{resource}.services.ai.azure.com/anthropic/v1/*`.

### 

API key authentication

After provisioning your Foundry Claude resource, you can obtain an API key from the Foundry portal:

1.  Navigate to your resource in the Foundry portal
2.  Go to **Keys and Endpoint** section
3.  Copy one of the provided API keys
4.  Use either the `api-key` or `x-api-key` header in your requests, or provide it to the SDK

The Python and TypeScript SDKs require an API key and either a resource name or base URL. The SDKs will automatically read these from the following environment variables if they are defined:

- `ANTHROPIC_FOUNDRY_API_KEY` - Your API key
- `ANTHROPIC_FOUNDRY_RESOURCE` - Your resource name (e.g., `example-resource`)
- `ANTHROPIC_FOUNDRY_BASE_URL` - Alternative to resource name; the full base URL (e.g., `https://example-resource.services.ai.azure.com/anthropic/`)

The `resource` and `base_url` parameters are mutually exclusive. Provide either the resource name (which the SDK uses to construct the URL as `https://{resource}.services.ai.azure.com/anthropic/`) or the full base URL directly.

**Example using API key:**

Python

``` shiki
import os
from anthropic import AnthropicFoundry

client = AnthropicFoundry(
    api_key=os.environ.get("ANTHROPIC_FOUNDRY_API_KEY"),
    resource='example-resource', # your resource name
)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(message.content)
```

Keep your API keys secure. Never commit them to version control or share them publicly. Anyone with access to your API key can make requests to Claude through your Foundry resource.

## 

Microsoft Entra authentication

For enhanced security and centralized access management, you can use Entra ID (formerly Azure Active Directory) tokens:

1.  Enable Entra authentication for your Foundry resource
2.  Obtain an access token from Entra ID
3.  Use the token in the `Authorization: Bearer {TOKEN}` header

**Example using Entra ID:**

Python

``` shiki
import os
from anthropic import AnthropicFoundry
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Get Azure Entra ID token using token provider pattern
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

# Create client with Entra ID authentication
client = AnthropicFoundry(
    resource='example-resource', # your resource name
    azure_ad_token_provider=token_provider  # Use token provider for Entra ID auth
)

# Make request
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(message.content)
```

Azure Entra ID authentication allows you to manage access using Azure RBAC, integrate with your organization's identity management, and avoid managing API keys manually.

## 

Correlation request IDs

Foundry includes request identifiers in HTTP response headers for debugging and tracing. When contacting support, provide both the `request-id` and `apim-request-id` values to help teams quickly locate and investigate your request across both Anthropic and Azure systems.

## 

Supported features

Claude on Foundry supports most of Claude's powerful features. You can find all the features currently supported in the [overview documentation](/docs/en/build-with-claude/overview).

### 

Features not supported

- Admin API (`/v1/organizations/*` endpoints)
- Models API (`/v1/models`)
- Message Batch API (`/v1/messages/batches`)

## 

API responses

API responses from Claude on Foundry follow the standard [Claude API response format](/docs/en/api/messages). This includes the `usage` object in response bodies, which provides detailed token consumption information for your requests. The `usage` object is consistent across all platforms (first-party API, Foundry, Amazon Bedrock, and Google Vertex AI).

For details on response headers specific to Foundry, see the [correlation request IDs section](#correlation-request-ids).

## 

API model IDs and deployments

The following Claude models are available through Foundry. The latest generation models (Opus 4.6, Sonnet 4.5, and Haiku 4.5) offer the most advanced capabilities:

| Model             | Default Deployment Name |
|-------------------|-------------------------|
| Claude Opus 4.6   | `claude-opus-4-6`       |
| Claude Opus 4.5   | `claude-opus-4-5`       |
| Claude Sonnet 4.5 | `claude-sonnet-4-5`     |
| Claude Opus 4.1   | `claude-opus-4-1`       |
| Claude Haiku 4.5  | `claude-haiku-4-5`      |

By default, deployment names match the model IDs shown above. However, you can create custom deployments with different names in the Foundry portal to manage different configurations, versions, or rate limits. Use the deployment name (not necessarily the model ID) in your API requests.

## 

Monitoring and logging

Azure provides comprehensive monitoring and logging capabilities for your Claude usage through standard Azure patterns:

- **Azure Monitor**: Track API usage, latency, and error rates
- **Azure Log Analytics**: Query and analyze request/response logs
- **Cost Management**: Monitor and forecast costs associated with Claude usage

Anthropic recommends logging your activity on at least a 30-day rolling basis to understand usage patterns and investigate any potential issues.

Azure's logging services are configured within your Azure subscription. Enabling logging does not provide Microsoft or Anthropic access to your content beyond what's necessary for billing and service operation.

## 

Troubleshooting

### 

Authentication errors

**Error**: `401 Unauthorized` or `Invalid API key`

- **Solution**: Verify your API key is correct. You can obtain a new API key from the Azure portal under **Keys and Endpoint** for your Claude resource.
- **Solution**: If using Azure Entra ID, ensure your access token is valid and hasn't expired. Tokens typically expire after 1 hour.

**Error**: `403 Forbidden`

- **Solution**: Your Azure account may lack the necessary permissions. Ensure you have the appropriate Azure RBAC role assigned (e.g., "Cognitive Services OpenAI User").

### 

Rate limiting

**Error**: `429 Too Many Requests`

- **Solution**: You've exceeded your rate limit. Implement exponential backoff and retry logic in your application.
- **Solution**: Consider requesting rate limit increases through the Azure portal or Azure support.

#### 

Rate limit headers

Foundry does not include Anthropic's standard rate limit headers (`anthropic-ratelimit-tokens-limit`, `anthropic-ratelimit-tokens-remaining`, `anthropic-ratelimit-tokens-reset`, `anthropic-ratelimit-input-tokens-limit`, `anthropic-ratelimit-input-tokens-remaining`, `anthropic-ratelimit-input-tokens-reset`, `anthropic-ratelimit-output-tokens-limit`, `anthropic-ratelimit-output-tokens-remaining`, and `anthropic-ratelimit-output-tokens-reset`) in responses. Manage rate limiting through Azure's monitoring tools instead.

### 

Model and deployment errors

**Error**: `Model not found` or `Deployment not found`

- **Solution**: Verify you're using the correct deployment name. If you haven't created a custom deployment, use the default model ID (e.g., `claude-sonnet-4-5`).
- **Solution**: Ensure the model/deployment is available in your Azure region.

**Error**: `Invalid model parameter`

- **Solution**: The model parameter should contain your deployment name, which can be customized in the Foundry portal. Verify the deployment exists and is properly configured.

## 

Additional resources

- **Foundry documentation**: [ai.azure.com/catalog](https://ai.azure.com/catalog/publishers/anthropic)
- **Azure pricing**: [azure.microsoft.com/en-us/pricing](https://azure.microsoft.com/en-us/pricing/)
- **Anthropic pricing details**: [Pricing documentation](/docs/en/about-claude/pricing#third-party-platform-pricing)
- **Authentication guide**: See the [authentication section](#authentication) above
- **Azure portal**: [portal.azure.com](https://portal.azure.com/)

Was this page helpful?

- 

- [Preview](#preview)

- [Prerequisites](#prerequisites)

- [Install an SDK](#install-an-sdk)

- [Provisioning](#provisioning)

- [Provisioning Foundry resources](#provisioning-foundry-resources)

- [Creating Foundry deployments](#creating-foundry-deployments)

- [Authentication](#authentication)

- [API key authentication](#api-key-authentication)

- [Microsoft Entra authentication](#microsoft-entra-authentication)

- [Correlation request IDs](#correlation-request-ids)

- [Supported features](#supported-features)

- [Features not supported](#features-not-supported)

- [API responses](#api-responses)

- [API model IDs and deployments](#api-model-ids-and-deployments)

- [Monitoring and logging](#monitoring-and-logging)

- [Troubleshooting](#troubleshooting)

- [Authentication errors](#authentication-errors)

- [Rate limiting](#rate-limiting)

- [Model and deployment errors](#model-and-deployment-errors)

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
