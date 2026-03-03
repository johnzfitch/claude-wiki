---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:07:16Z"
source_url: "https://platform.claude.com/docs/en/api/admin/cost_report"
title: "Cost Report - Claude API Reference"
---

# Cost Report

##### [Get Cost Report](/docs/en/api/admin/cost_report/retrieve)

GET/v1/organizations/cost_report

##### ModelsExpand Collapse 

CostReport = object { data, has_more, next_page }

data: array of object { ending_at, results, starting_at }

ending_at: string

End of the time bucket (exclusive) in RFC 3339 format.

results: array of object { amount, context_window, cost_type, 8 more }

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

speed: "standard" or "fast"

Speed used (research preview). `null` if not grouping by speed, or for non-token costs. Only returned when the `fast-mode-2026-02-01` beta header is provided.

Accepts one of the following:

"standard"

"fast"

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
