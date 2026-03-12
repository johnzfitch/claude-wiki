---
category: "20-Models"
fetched_at: "2026-03-12T08:16:39Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/models/retrieve"
title: "Get a Model - Claude API Reference"
---

# Get a Model

client.beta.models.retrieve(stringmodelID, ModelRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaModelInfo](/docs/en/api/beta#beta_model_info) { id, created_at, display_name, type }

GET/v1/models/{model_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse 

modelID: string

Model identifier or alias.

params: ModelRetrieveParams { betas }

betas?: Array\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\>

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" \| "prompt-caching-2024-07-31" \| "computer-use-2024-10-22" \| 17 more

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

BetaModelInfo { id, created_at, display_name, type }

id: string

Unique model identifier.

created_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.

Get a Model

TypeScript

``` shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaModelInfo = await client.beta.models.retrieve('model_id');

console.log(betaModelInfo.id);
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
