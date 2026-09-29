---
title: "Handle streaming refusals - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals"
category: "04-API-Reference/Test-Evaluate"
fetched_at: "2026-09-26T06:39:59Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Ftest-and-evaluate%2Fstrengthen-guardrails%2Fhandle-streaming-refusals)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Model capabilities

# Handle streaming refusals

Copy page



Detect and handle refusal stop reasons in streaming responses, and retry refused requests on a fallback model.

Copy page



Starting with Claude 4 models, streaming responses from Claude's API return **`stop_reason`: `"refusal"`** when streaming classifiers intervene to handle potential policy violations. This safety feature helps maintain content compliance during real-time streaming.



This page covers how refusals appear in streaming responses. For every `stop_reason` value and how to handle it, see [Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md). To retry refused requests on another Claude model, see [Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md).

## API response format

When streaming classifiers detect content that violates Anthropic's policies, the API returns this response:

```python
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello.."
    }
  ],
  "stop_reason": "refusal",
  "stop_details": {
    "type": "refusal",
    "category": "cyber",
    "explanation": "This request was declined because it could enable cyber harm."
  }
}
```



In the event stream, `stop_details` arrives on the `message_delta` event alongside `stop_reason`.



A `refusal` response from streaming classifiers includes a `stop_details` object with a `category` and a human-readable `explanation` that you can surface to the user. See [Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md#refusal-response) for the full response shape and the available categories.

On a refusal the `stop_details` object is always present, but its `category` and `explanation` fields can be `null`, for example when the refusal maps to no named category. Branch on `stop_reason` or `stop_details.type` rather than assuming `category` and `explanation` are populated, and provide your own user-facing messaging when they are `null`.

## Reset context after refusal

When you receive **`stop_reason`: `refusal`**, you must reset the conversation context before continuing. You can remove or rephrase the turn that triggered the refusal, or clear the conversation history entirely. Attempting to continue without resetting will result in continued refusals.



Usage metrics are still provided in the response, even when the response is refused. Whether a refused request is billed depends on when the refusal arrives and its category; see [How refusals are billed](../Guides/build-with-claude-refusals-and-fallback.md#how-refusals-are-billed).



Resetting context is not the only way to recover. You can also retry the refused request on a different Claude model, and the [Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md) page shows how to set that up with server-side fallback, the SDK middleware, or a manual retry.

## Implementation guide

Here's how to detect and handle streaming refusals in your application:

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
messages = []


def reset_conversation():
    """Reset conversation context after refusal"""
    global messages
    messages = []
    print("Conversation reset due to refusal")


try:
    with client.messages.stream(
        max_tokens=1024,
        messages=messages + [{"role": "user", "content": "Hello"}],
        model="claude-opus-5-5",
    ) as stream:
        for event in stream:
            # Check for refusal in message delta
            if event.type == "message_delta":
                if event.delta.stop_reason == "refusal":
                    reset_conversation()
                    break
except Exception as e:
    print(f"Error: {e}")
```

## Current refusal types

The API currently handles refusals in three different ways:

| Refusal type                       | Response format              | When it occurs                                  |
|------------------------------------|------------------------------|-------------------------------------------------|
| Streaming classifier refusals      | **`stop_reason`: `refusal`** | During streaming when content violates policies |
| API input and copyright validation | 400 error codes              | When input fails validation checks              |
| Model-generated refusals           | Standard text responses      | When the model itself refuses                   |

## Best practices

- **Monitor for refusals:** Include **`stop_reason`: `refusal`** checks in your error handling
- **Reset automatically:** Implement automatic context reset when refusals are detected
- **Fall back to another model:** Configure [server-side fallback or the SDK middleware](../Guides/build-with-claude-refusals-and-fallback.md) so refused requests are retried on another Claude model instead of surfacing a refusal to the user
- **Redeem fallback credit on manual retries:** If you build the retry yourself, pass the refusal's [fallback credit](../Guides/build-with-claude-fallback-credit.md) token so the retry doesn't pay the prompt-cache cost twice
- **Provide custom messaging:** Create user-friendly messages for better UX when refusals occur
- **Track refusal patterns:** Monitor refusal frequency to identify potential issues with your prompts

## Migration notes

If you built refusal handling when this feature first shipped, or you're adding it to an existing integration, check the following:

- **Refusals are responses, not errors.** A refusal arrives as a successful HTTP 200 response with `stop_reason`: `"refusal"`, so monitoring built only on error rates won't surface it. Track refusals as their own signal.
- **Refusals include structured detail.** On every model, a refusal also includes a `stop_details` object that identifies the policy category behind the decline. See [Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md#refusal-response) for the full response shape.
- **Retry on a different model.** Re-sending a refused request to the same model usually results in another refusal. Instead of only resetting context, retry on a fallback model with [server-side fallback, the SDK middleware, or a manual retry](../Guides/build-with-claude-refusals-and-fallback.md), and redeem [fallback credit](../Guides/build-with-claude-fallback-credit.md) when you build the retry yourself.
- **Check batch results for refusals.** A refused request in a [Message Batch](../Guides/build-with-claude-batch-processing.md) is returned as a succeeded result with `stop_reason`: `"refusal"`, not as an errored result.
- **Centralize handling on `stop_reason`.** The API continues to consolidate refusal handling around `stop_reason`: `"refusal"`, so branch on the stop reason rather than on model-specific behavior.

## Next steps



[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)

Retry refused requests on another Claude model, server-side or in your client.



[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)

Every `stop_reason` value and how to handle it.



[Streaming messages](../Guides/build-with-claude-streaming.md)

Stream responses and read `stop_reason` from `message_delta` events as they arrive.



[Multilingual support](../Guides/build-with-claude-multilingual-support.md)

Serve users across languages with Claude's cross-lingual capabilities.
