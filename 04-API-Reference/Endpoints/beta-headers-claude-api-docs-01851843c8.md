---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:05:08Z"
source_url: "https://platform.claude.com/docs/en/api/beta-headers"
title: "Beta headers - Claude API Docs"
---

Using the API

# Beta headers

Copy page

Documentation for using beta headers with the Claude API

Copy page

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

These features are subject to change and may be modified or removed in future releases.

Beta headers are often used in conjunction with the [beta namespace in the client SDKs](/docs/en/api/client-sdks#beta-namespace-in-client-sdks)

## 

How to use beta headers

To access beta features, include the `anthropic-beta` header in your API requests:

``` shiki
POST /v1/messages
Content-Type: application/json
X-API-Key: YOUR_API_KEY
anthropic-beta: BETA_FEATURE_NAME
```

When using the SDK, you can specify beta headers in the request options:

Python

``` shiki
from anthropic import Anthropic

client = Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ],
    betas=["code-execution-2025-08-25"]
)
```

Beta features are experimental and may:

- Have breaking changes without notice
- Be deprecated or removed
- Have different rate limits or pricing
- Not be available in all regions

### 

Multiple beta features

To use multiple beta features in a single request, include all feature names in the header separated by commas:

``` shiki
anthropic-beta: feature1,feature2,feature3
```

### 

Version naming conventions

Beta feature names typically follow the pattern: `feature-name-YYYY-MM-DD`, where the date indicates when the beta version was released. Always use the exact beta feature name as documented.

## 

Error handling

If you use an invalid or unavailable beta header, you'll receive an error response:

``` shiki
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Unsupported beta header: invalid-beta-name"
  }
}
```

## 

Getting help

For questions about beta features:

1.  Check the documentation for the specific feature
2.  Review the [API changelog](/docs/en/api/versioning) for updates
3.  Contact support for assistance with production usage

Remember that beta features are provided "as-is" and may not have the same SLA guarantees as stable API features.

Was this page helpful?

- 

- [How to use beta headers](#how-to-use-beta-headers)

- [Multiple beta features](#multiple-beta-features)

- [Version naming conventions](#version-naming-conventions)

- [Error handling](#error-handling)

- [Getting help](#getting-help)

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
