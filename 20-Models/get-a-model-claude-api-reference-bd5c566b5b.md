---
category: "20-Models"
fetched_at: "2026-02-22T14:20:38Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/models/retrieve"
title: "Get a Model - Claude API Reference"
---

Copy page

C#

# Get a Model

[ModelInfo](/docs/en/api/models#model_info) Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse 

ModelRetrieveParams parameters

required string modelID

Model identifier or alias.

IReadOnlyList\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\> betas

Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024_09_24

"prompt-caching-2024-07-31"PromptCaching2024_07_31

"computer-use-2024-10-22"ComputerUse2024_10_22

"computer-use-2025-01-24"ComputerUse2025_01_24

"pdfs-2024-09-25"Pdfs2024_09_25

"token-counting-2024-11-01"TokenCounting2024_11_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19

"output-128k-2025-02-19"Output128k2025_02_19

"files-api-2025-04-14"FilesApi2025_04_14

"mcp-client-2025-04-04"McpClient2025_04_04

"mcp-client-2025-11-20"McpClient2025_11_20

"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14

"code-execution-2025-05-22"CodeExecution2025_05_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11

"context-1m-2025-08-07"Context1m2025_08_07

"context-management-2025-06-27"ContextManagement2025_06_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26

"skills-2025-10-02"Skills2025_10_02

"fast-mode-2026-02-01"FastMode2026_02_01

##### ReturnsExpand Collapse 

class ModelInfo:

required string ID

Unique model identifier.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

required string DisplayName

A human-readable name for the model.

JsonElement Type "model"constant

Object type.

For Models, this is always `"model"`.

Get a Model

C#

``` shiki
ModelRetrieveParams parameters = new() { ModelID = "model_id" };

var modelInfo = await client.Models.Retrieve(parameters);

Console.WriteLine(modelInfo);
```

Response 200

``` shiki
{
  "id": "claude-opus-4-6",
  "created_at": "2026-02-04T00:00:00Z",
  "display_name": "Claude Opus 4.6",
  "type": "model"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "claude-opus-4-6",
  "created_at": "2026-02-04T00:00:00Z",
  "display_name": "Claude Opus 4.6",
  "type": "model"
}
```

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
