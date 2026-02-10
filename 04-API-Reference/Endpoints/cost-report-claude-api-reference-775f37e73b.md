---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:11:20Z"
source_url: "https://platform.claude.com/docs/en/api/admin/cost_report"
title: "Cost Report - Claude API Reference"
---

Copy page

# Cost Report

##### [Get Cost Report](/docs/en/api/admin/cost_report/retrieve)

get/v1/organizations/cost_report

##### ModelsExpand Collapse 

CostReport = object { data, has_more, next_page }

data: array of object { ending_at, results, starting_at }

ending_at: string

End of the time bucket (exclusive) in RFC 3339 format.

results: array of object { amount, context_window, cost_type, 7 more }

List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

amount: string

Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.

context_window: "0-200k" or "200k-1M"

Input context window used. `null` if not grouping by description or for non-token costs.

Accepts one of the following:

"0-200k"

"200k-1M"

cost_type: "tokens" or "web_search" or "code_execution"

Type of cost. `null` if not grouping by description.

Accepts one of the following:

"tokens"

"web_search"

"code_execution"

currency: string

Currency code for the cost amount. Currently always `"USD"`.

description: string

Description of the cost item. `null` if not grouping by description.

inference_geo: string

Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`. For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

model: string

Model name used. `null` if not grouping by description or for non-token costs.

service_tier: "standard" or "batch"

Service tier used. `null` if not grouping by description or for non-token costs.

Accepts one of the following:

"standard"

"batch"

token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more

Type of token. `null` if not grouping by description or for non-token costs.

Accepts one of the following:

"uncached_input_tokens"

"output_tokens"

"cache_read_input_tokens"

"cache_creation.ephemeral_1h_input_tokens"

"cache_creation.ephemeral_5m_input_tokens"

workspace_id: string

ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.

starting_at: string

Start of the time bucket (inclusive) in RFC 3339 format.

has_more: boolean

Indicates if there are more results.

next_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

formatdate-time

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
