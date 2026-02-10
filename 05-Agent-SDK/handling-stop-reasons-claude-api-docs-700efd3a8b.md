---
category: "05-Agent-SDK"
fetched_at: "2026-02-07T10:04:38Z"
source_url: "https://platform.claude.com/docs/en/agent-sdk/stop-reasons"
title: "Handling stop reasons - Claude API Docs"
---

Guides

# Handling stop reasons

Copy page

Detect refusals and other stop reasons directly from result messages in the Agent SDK

Copy page

The `stop_reason` field on result messages tells you why the model stopped generating. This is the recommended way to detect refusals, max-token limits, and other termination conditions (no stream parsing required).

`stop_reason` is available on every `ResultMessage`, regardless of whether streaming is enabled. You don't need to set `include_partial_messages` (Python) or `includePartialMessages` (TypeScript).

## 

Reading stop_reason

The `stop_reason` field is present on both success and error result messages. Check it after iterating through the message stream:

Python

``` shiki
from claude_agent_sdk import query, ResultMessage
import asyncio

async def check_stop_reason():
    async for message in query(prompt="Write a poem about the ocean"):
        if isinstance(message, ResultMessage):
            print(f"Stop reason: {message.stop_reason}")
            if message.stop_reason == "refusal":
                print("The model declined this request.")

asyncio.run(check_stop_reason())
```

## 

Available stop reasons

| Stop reason | Meaning |
|----|----|
| `end_turn` | The model finished generating its response normally. |
| `max_tokens` | The response reached the maximum output token limit. |
| `stop_sequence` | The model generated a configured stop sequence. |
| `refusal` | The model declined to fulfill the request. |
| `tool_use` | The model's final output was a tool call. This is uncommon in SDK results because tool calls are normally executed before the result is returned. |
| `null` | No API response was received; for example, an error occurred before the first request, or the result was replayed from a cached session. |

## 

Stop reasons on error results

Error results (such as `error_max_turns` or `error_during_execution`) also carry `stop_reason`. The value reflects the last assistant message received before the error occurred:

| Result variant | `stop_reason` value |
|----|----|
| `success` | The stop reason from the final assistant message. |
| `error_max_turns` | The stop reason from the last assistant message before the turn limit was hit. |
| `error_max_budget_usd` | The stop reason from the last assistant message before the budget was exceeded. |
| `error_max_structured_output_retries` | The stop reason from the last assistant message before the retry limit was hit. |
| `error_during_execution` | The last stop reason seen, or `null` if the error occurred before any API response. |

Python

``` shiki
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage
import asyncio

async def handle_max_turns():
    options = ClaudeAgentOptions(max_turns=3)

    async for message in query(prompt="Refactor this module", options=options):
        if isinstance(message, ResultMessage):
            if message.subtype == "error_max_turns":
                print(f"Hit turn limit. Last stop reason: {message.stop_reason}")
                # stop_reason might be "end_turn" or "tool_use"
                # depending on what the model was doing when the limit hit

asyncio.run(handle_max_turns())
```

## 

Detecting refusals

`stop_reason === "refusal"` is the simplest way to detect when the model declines a request. Previously, detecting refusals required enabling partial message streaming and manually scanning `StreamEvent` messages for `message_delta` events. With `stop_reason` on the result message, you can check directly:

Python

``` shiki
from claude_agent_sdk import query, ResultMessage
import asyncio

async def safe_query(prompt: str):
    async for message in query(prompt=prompt):
        if isinstance(message, ResultMessage):
            if message.stop_reason == "refusal":
                print("Request was declined. Please revise your prompt.")
                return None
            return message.result
    return None

asyncio.run(safe_query("Summarize this article"))
```

## 

Next steps

- [Stream responses in real-time](/docs/en/agent-sdk/streaming-output): access raw API events including `message_delta` as they arrive
- [Structured outputs](/docs/en/agent-sdk/structured-outputs): get typed JSON responses from the agent
- [Tracking costs and usage](/docs/en/agent-sdk/cost-tracking): understand token usage and billing from result messages

Was this page helpful?

- 

- [Reading stop_reason](#reading-stop-reason)

- [Available stop reasons](#available-stop-reasons)

- [Stop reasons on error results](#stop-reasons-on-error-results)

- [Detecting refusals](#detecting-refusals)

- [Next steps](#next-steps)

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
