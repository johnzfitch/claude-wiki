---
category: "20-Models"
fetched_at: "2026-03-12T08:16:40Z"
source_url: "https://platform.claude.com/docs/en/api/python/models/list"
title: "List Models - Claude API Reference"
---

# List Models

models.list(ModelListParams\*\*kwargs) -\> SyncPage\[[ModelInfo](/docs/en/api/models#model_info)\]

GET/v1/models

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

##### ParametersExpand Collapse 

after_id: Optional\[str\]

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: Optional\[str\]

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

limit: Optional\[int\]

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

betas: Optional\[List\[[AnthropicBetaParam](/docs/en/api/beta#anthropic_beta)\]\]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal\["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 17 more\]

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

##### ReturnsExpand Collapse 

class ModelInfo: …

id: str

Unique model identifier.

created_at: datetime

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: str

A human-readable name for the model.

type: Literal\["model"\]

Object type.

For Models, this is always `"model"`.

List Models

Python

``` shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.models.list()
page = page.data[0]
print(page.id)
```

Response 200

``` shiki
{
  "data": [
    {
      "id": "claude-opus-4-6",
      "created_at": "2026-02-04T00:00:00Z",
      "display_name": "Claude Opus 4.6",
      "type": "model"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "data": [
    {
      "id": "claude-opus-4-6",
      "created_at": "2026-02-04T00:00:00Z",
      "display_name": "Claude Opus 4.6",
