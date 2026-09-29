---
title: "Token counting - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/token-counting"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:28Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Ftoken-counting)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode (research preview)](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Google Cloud](build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Context management

# Token counting

Copy page



Count the tokens in a message before you send it to Claude. Use token counts to manage rate limits and costs, make model routing decisions, and fit prompts to a target length.

Copy page



Token counting

[ZDR](../Other/manage-claude-api-and-data-retention.md)

Eligible

excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Token counting lets you determine the number of tokens in a message before you send it to Claude. This helps you make informed decisions about your prompts and usage. With token counting, you can:

- Proactively manage rate limits and costs
- Make smart model routing decisions
- Optimize prompts to a specific length

------------------------------------------------------------------------

## How to count message tokens

The [token counting](../Endpoints/platform-claude-com-messages-count-tokens.md) endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](../Agents-Tools/agents-and-tools-tool-use-overview.md), [images](build-with-claude-vision.md), and [PDFs](build-with-claude-pdf-support.md). The response contains the total number of input tokens.

This endpoint returns an `invalid_request_error` for a few inputs that the Messages API accepts: [server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md) such as web search, web fetch, code execution, and tool search (every server tool except the [advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)), the [MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md), and `image` or `document` blocks with a `url` or `file` source. Send images and PDFs as base64 to count them. For requests that use server tools or MCP servers, the Messages API response reports the tokens used in its `usage` object.



The token count is an **estimate**. In some cases, the actual number of input tokens used when creating a message might differ by a small amount.

Token counts may include tokens added automatically by Anthropic for system optimizations. **You are not billed for system-added tokens**. Billing reflects only your content.

### Supported models

All [active models](../../20-Models/about-claude-models-overview.md) support token counting.



Claude 4.7 and later models and Claude Mythos Preview use a newer tokenizer. The same input text produces approximately 30 percent more tokens than on earlier models. The exact increase depends on the content and workload shape. Recount prompts against the model you plan to use rather than reusing counts measured against earlier models.

### Count tokens in basic messages

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    system="You are a scientist",
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(response.json())
```

Output



```python
{ "input_tokens": 14 }
```

### Count tokens in messages with tools



Token counting supports client tools and the [advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md). Requests that include other [server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md) return an error. For the advisor tool, the count covers the executor's first sampling call only.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"],
            },
        }
    ],
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
)

print(response.json())
```

Output



```python
{ "input_tokens": 403 }
```

### Count tokens in messages with images

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import base64
import httpx2

image_url = "https://platform.claude.com/docs/images/vision-example.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx2.get(image_url).content).decode("utf-8")

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                    },
                },
                {"type": "text", "text": "Describe this image"},
            ],
        }
    ],
)
print(response.json())
```

Output



```python
{ "input_tokens": 1028 }
```

An embedded image block that sets [`"oversized_image": "error"`](build-with-claude-vision-coordinates.md#oversized-image-error) is rejected at count time exactly as the Messages API would reject it.

### Count tokens in messages with thinking



See [Thinking and the context window](build-with-claude-thinking.md#thinking-and-the-context-window) for more details.

- Thinking blocks from **previous** assistant turns count toward your input tokens on models that [keep all prior turns](build-with-claude-thinking.md#thinking-block-preservation-by-model); on models that keep only the last turn, the API strips them and they do **not** count
- **Current** assistant turn thinking **does** count toward your input tokens

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    thinking={"type": "adaptive"},
    messages=[
        {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "thinking",
                    "thinking": "This is a nice number theory question. Let's think about it step by step...",
                    "signature": "EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV...",
                },
                {
                    "type": "text",
                    "text": "Yes, there are infinitely many prime numbers p such that p mod 4 = 3...",
                },
            ],
        },
        {"role": "user", "content": "Can you write a formal proof?"},
    ],
)

print(response.json())
```

Output



```python
{ "input_tokens": 88 }
```

### Count tokens in messages with PDFs



Token counting supports base64-encoded PDFs with the same [PDF requirements](build-with-claude-pdf-support.md#check-pdf-requirements) as the Messages API. This endpoint doesn't support `url` or `file` document sources.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import base64
import anthropic

client = anthropic.Anthropic()

with open("/path/to/document.pdf", "rb") as pdf_file:
    pdf_base64 = base64.standard_b64encode(pdf_file.read()).decode("utf-8")

response = client.messages.count_tokens(
    model="claude-opus-5-5",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_base64,
                    },
                },
                {"type": "text", "text": "Please summarize this document."},
            ],
        }
    ],
)

print(response.json())
```

Output



```python
{ "input_tokens": 2188 }
```

------------------------------------------------------------------------

## Token counts on Claude Fable and Claude Mythos models

Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, and Claude Mythos 5 share the tokenizer introduced with Claude Opus 4.7. A prompt counts the same on all four, and roughly 30 percent higher than on models before Claude Opus 4.7 (the exact increase depends on the content). The token counting endpoint counts under the tokenizer of the `model` you pass. To measure the difference for your workload, count the same request twice, once with your current model and once with the model you plan to move to, and compare the two `input_tokens` values.



**Billing and migration:** Usage and billing on these models reflect this tokenizer's counts. When migrating from a model before Claude Opus 4.7, don't reuse token counts measured on the older model to estimate costs or context window fit. Count your prompts with the `model` ID you plan to use (for example, `"claude-fable-5-1"`).

------------------------------------------------------------------------

## Pricing and rate limits

Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](../Endpoints/rate-limits.md#rate-limits). If you need higher limits, use **Request rate limit increase** on the [Rate limits](../Other/usage-limits.md) page.

| Usage tier | Requests per minute (RPM) |
|------------|---------------------------|
| Start      | 5,000                     |
| Build      | 10,000                    |
| Scale      | 20,000                    |



Token counting and message creation have separate and independent rate limits. Usage of one does not count against the limits of the other.

------------------------------------------------------------------------

## FAQ

### Does token counting use prompt caching?

No, token counting provides an estimate without using caching logic. Although you may provide `cache_control` blocks in your token counting request, prompt caching only occurs during actual message creation.

------------------------------------------------------------------------

## Next steps



[Count message tokens](../Endpoints/platform-claude-com-messages-count-tokens.md)

Read the full API reference for the token counting endpoint.



[Context windows](build-with-claude-context-windows.md)

Use token counts to keep prompts within a model's context window.



[Rate limits](../Endpoints/rate-limits.md)

Check token counts before you send a request to stay within your usage tier.



[Prompt caching](build-with-claude-prompt-caching.md)

Reduce cost and latency on repeated prompts by caching prompt prefixes.

## Compatibility

Supported platforms  
- Claude API
- Claude Platform on AWS
- Amazon Bedrock
- Google Cloud
- Microsoft Foundry
