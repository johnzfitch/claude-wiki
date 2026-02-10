---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:11:18Z"
source_url: "https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages"
title: "Get Messages Usage Report - Claude API Reference"
---

Copy page

# Get Messages Usage Report

get/v1/organizations/usage_report/messages

Get Messages Usage Report

##### Query ParametersExpand Collapse 

starting_at: string

Time buckets that start on or after this RFC 3339 timestamp will be returned. Each time bucket will be snapped to the start of the minute/hour/day in UTC.

formatdate-time

api_key_ids: optional array of string

Restrict usage returned to the specified API key ID(s).

bucket_width: optional "1d" or "1m" or "1h"

Time granularity of the response data.

Accepts one of the following:

"1d"

"1m"

"1h"

context_window: optional array of "0-200k" or "200k-1M"

Restrict usage returned to the specified context window(s).

Accepts one of the following:

"0-200k"

"200k-1M"

ending_at: optional string

Time buckets that end before this RFC 3339 timestamp will be returned.

formatdate-time

group_by: optional array of "api_key_id" or "workspace_id" or "model" or 3 more

Group by any subset of the available options.

Accepts one of the following:

"api_key_id"

"workspace_id"

"model"

"service_tier"

"context_window"

"inference_geo"

inference_geos: optional array of "global" or "us" or "not_available"

Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.

Accepts one of the following:

"global"

"us"

"not_available"

limit: optional number

Maximum number of time buckets to return in the response.

The default and max limits depend on `bucket_width`: • `"1d"`: Default of 7 days, maximum of 31 days • `"1h"`: Default of 24 hours, maximum of 168 hours • `"1m"`: Default of 60 minutes, maximum of 1440 minutes

models: optional array of string

Restrict usage returned to the specified model(s).

page: optional string

Optionally set to the `next_page` token from the previous response.

formatdate-time

service_tiers: optional array of "standard" or "batch" or "priority" or 3 more

Restrict usage returned to the specified service tier(s).

Accepts one of the following:

"standard"

"batch"

"priority"

"priority_on_demand"

"flex"

"flex_discount"

workspace_ids: optional array of string

Restrict usage returned to the specified workspace ID(s).

##### Header ParametersExpand Collapse 

"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### ReturnsExpand Collapse 

MessagesUsageReport = object { data, has_more, next_page }

data: array of object { ending_at, results, starting_at }

ending_at: string

End of the time bucket (exclusive) in RFC 3339 format.

formatdate-time

results: array of object { api_key_id, cache_creation, cache_read_input_tokens, 8 more }

List of usage items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

api_key_id: string

ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.

cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

The number of input tokens for cache creation.

ephemeral_1h_input_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral_5m_input_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache_read_input_tokens: number

The number of input tokens read from the cache.

context_window: "0-200k" or "200k-1M"

Context window used. `null` if not grouping by context window.

Accepts one of the following:

"0-200k"

"200k-1M"

inference_geo: string

Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`. For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

model: string

Model used. `null` if not grouping by model.

output_tokens: number

The number of output tokens generated.

server_tool_use: object { web_search_requests }

Server-side tool usage metrics.

web_search_requests: number

The number of web search requests made.

service_tier: "standard" or "batch" or "priority" or 3 more

Service tier used. `null` if not grouping by service tier.

Accepts one of the following:

"standard"

"batch"

"priority"

"priority_on_demand"

"flex"

"flex_discount"

uncached_input_tokens: number

The number of uncached input tokens processed.

workspace_id: string

ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.

starting_at: string

Start of the time bucket (inclusive) in RFC 3339 format.

formatdate-time

has_more: boolean

Indicates if there are more results.

next_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

formatdate-time

Get Messages Usage Report

``` shiki
curl https://api.anthropic.com/v1/organizations/usage_report/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

``` shiki
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
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
