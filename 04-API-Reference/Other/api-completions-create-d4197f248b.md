---
title: "Create a Text Completion - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/completions/create"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:27Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Create




cURL

# Create a Text Completion

POST/v1/complete

\[Legacy\] Create a Text Completion.

The Text Completions API is a legacy API. We recommend using the [Messages API](https://platform.claude.com/docs/en/api/messages) going forward.

Future models and features will not be compatible with Text Completions. See our [migration guide](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) for guidance in migrating from Text Completions to Messages.

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string



[](#anthropic_beta%5B0%5D)



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more



One of the following:

"message-batches-2024-09-24"



[](#anthropic_beta%5B1%5D%5B0%5D)

"prompt-caching-2024-07-31"



[](#anthropic_beta%5B1%5D%5B1%5D)

"computer-use-2024-10-22"



[](#anthropic_beta%5B1%5D%5B2%5D)

"computer-use-2025-01-24"



[](#anthropic_beta%5B1%5D%5B3%5D)

"pdfs-2024-09-25"



[](#anthropic_beta%5B1%5D%5B4%5D)

"token-counting-2024-11-01"



[](#anthropic_beta%5B1%5D%5B5%5D)

"token-efficient-tools-2025-02-19"



[](#anthropic_beta%5B1%5D%5B6%5D)

"output-128k-2025-02-19"



[](#anthropic_beta%5B1%5D%5B7%5D)

"files-api-2025-04-14"



[](#anthropic_beta%5B1%5D%5B8%5D)

"mcp-client-2025-04-04"



[](#anthropic_beta%5B1%5D%5B9%5D)

"mcp-client-2025-11-20"



[](#anthropic_beta%5B1%5D%5B10%5D)

"dev-full-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B11%5D)

"interleaved-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B12%5D)

"code-execution-2025-05-22"



[](#anthropic_beta%5B1%5D%5B13%5D)

"extended-cache-ttl-2025-04-11"



[](#anthropic_beta%5B1%5D%5B14%5D)

"context-1m-2025-08-07"



[](#anthropic_beta%5B1%5D%5B15%5D)

"context-management-2025-06-27"



[](#anthropic_beta%5B1%5D%5B16%5D)

"model-context-window-exceeded-2025-08-26"



[](#anthropic_beta%5B1%5D%5B17%5D)

"skills-2025-10-02"



[](#anthropic_beta%5B1%5D%5B18%5D)

"fast-mode-2026-02-01"



[](#anthropic_beta%5B1%5D%5B19%5D)

"output-300k-2026-03-24"



[](#anthropic_beta%5B1%5D%5B20%5D)

"user-profiles-2026-03-24"



[](#anthropic_beta%5B1%5D%5B21%5D)

"advisor-tool-2026-03-01"



[](#anthropic_beta%5B1%5D%5B22%5D)

"managed-agents-2026-04-01"



[](#anthropic_beta%5B1%5D%5B23%5D)

"cache-diagnosis-2026-04-07"



[](#anthropic_beta%5B1%5D%5B24%5D)

"dreaming-2026-04-21"



[](#anthropic_beta%5B1%5D%5B25%5D)

"thinking-token-count-2026-05-13"



[](#anthropic_beta%5B1%5D%5B26%5D)

"server-side-fallback-2026-06-01"



[](#anthropic_beta%5B1%5D%5B27%5D)

"server-side-fallback-2026-07-01"



[](#anthropic_beta%5B1%5D%5B28%5D)

"fallback-credit-2026-06-01"



[](#anthropic_beta%5B1%5D%5B29%5D)

"fallback-credit-2026-07-01"



[](#anthropic_beta%5B1%5D%5B30%5D)

"agent-memory-2026-07-22"



[](#anthropic_beta%5B1%5D%5B31%5D)

[](#anthropic_beta%5B1%5D)

[](#create.betas)

##### Body ParametersJSONExpand Collapse 



max_tokens_to_sample: number



The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

minimum1

[](#create.max_tokens_to_sample)



model: [Model](/docs/en/api/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 14 more



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#create.model%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#create.model%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#create.model%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#create.model%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#create.model%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#create.model%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#create.model%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#create.model%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#create.model%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#create.model%5B0%5D%5B16%5D)

[](#create.model%5B0%5D)

string



[](#create.model%5B1%5D)

[](#create.model)



prompt: string



The prompt that you want Claude to complete.

For proper response generation you will need to format your prompt using alternating \`

Human:`and`

Assistant:\` conversational turns. For example:

```
"

Human: {userQuestion}

Assistant:"
```

See [prompt validation](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) and our guide to [prompt design](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) for more details.

minLength1

[](#create.prompt)



metadata: optional [Metadata](/docs/en/api/messages#metadata) { user_id }



An object describing metadata about the request.



user_id: optional string



An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

[](#create.metadata.user_id)

[](#create.metadata)



stop_sequences: optional array of string



Sequences that will cause the model to stop generating.

Our models stop on \`"

Human:"\`, and may include additional built-in stop sequences in the future. By providing the stop_sequences parameter, you may include additional strings that will cause the model to stop generating.

[](#create.stop_sequences)



stream: optional boolean



Whether to incrementally stream the response using server-sent events.

See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

[](#create.stream)



temperature: optional number⁠Deprecated



Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

[](#create.temperature)



top_k: optional number⁠Deprecated



Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0

[](#create.top_k)



top_p: optional number⁠Deprecated



Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value \>= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

[](#create.top_p)

##### ReturnsExpand Collapse 



Completion object { id, completion, model, 2 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#completion.id)

completion: string



The resulting completion up to and excluding the stop sequences.

[](#completion.completion)



model: [Model](/docs/en/api/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 14 more



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#completion.model%20%2B%20(resource)%20messages%5B1%5D)

[](#completion.model)



stop_reason: string



The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

[](#completion.stop_reason)



type: "completion"



Object type.

For Text Completions, this is always `"completion"`.

[](#completion.type)

[](#completion)



Completion object { id, completion, model, 2 more }





id: string



Unique object identifier.

The format and length of IDs may change over time.

[](#completion.id)

completion: string



The resulting completion up to and excluding the stop sequences.

[](#completion.completion)



model: [Model](/docs/en/api/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 14 more



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-sonnet-5"



High-performance model for coding and agents

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B0%5D)

"claude-fable-5"



Next generation of intelligence for the hardest knowledge work and coding problems

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B1%5D)

"claude-mythos-5"



Most capable model for cybersecurity and biology research

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B2%5D)

"claude-opus-5"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B3%5D)

"claude-opus-4-8"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B4%5D)

"claude-opus-4-7"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B5%5D)

"claude-mythos-preview"



New class of intelligence, strongest in coding and cybersecurity

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B6%5D)

"claude-opus-4-6"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B7%5D)

"claude-sonnet-4-6"



Best combination of speed and intelligence

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B8%5D)

"claude-haiku-4-5"



Fastest model with near-frontier intelligence

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B9%5D)

"claude-haiku-4-5-20251001"



Fastest model with near-frontier intelligence

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B10%5D)

"claude-opus-4-5"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B11%5D)

"claude-opus-4-5-20251101"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B12%5D)

"claude-sonnet-4-5"



High-performance model for agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B13%5D)

"claude-sonnet-4-5-20250929"



High-performance model for agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B14%5D)

"claude-opus-4-1"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B15%5D)

"claude-opus-4-1-20250805"



Powerful intelligence for long-running agents and coding

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D%5B16%5D)

[](#completion.model%20%2B%20(resource)%20messages%5B0%5D)

string



[](#completion.model%20%2B%20(resource)%20messages%5B1%5D)

[](#completion.model)



stop_reason: string



The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

[](#completion.stop_reason)



type: "completion"



Object type.

For Text Completions, this is always `"completion"`.

[](#completion.type)

[](#completion)

Create a Text Completion

cURL



```python
curl https://api.anthropic.com/v1/complete \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    --max-time 600 \
    -d '{
          "max_tokens_to_sample": 256,
          "model": "claude-2.1",
          "prompt": "\\n\\nHuman: Hello, world!\\n\\nAssistant:",
          "temperature": 1,
          "top_k": 5,
          "top_p": 0.7
        }'
```

Response 200



```python
{
  "id": "compl_018CKm6gsux7P8yMcwZbeCPw",
  "completion": " Hello! My name is Claude.",
  "model": "claude-2.1",
  "stop_reason": "stop_sequence",
  "type": "completion"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "compl_018CKm6gsux7P8yMcwZbeCPw",
  "completion": " Hello! My name is Claude.",
  "model": "claude-2.1",
  "stop_reason": "stop_sequence",
