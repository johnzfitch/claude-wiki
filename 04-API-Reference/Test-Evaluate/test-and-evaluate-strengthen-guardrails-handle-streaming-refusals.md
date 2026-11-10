---
title: "Handle streaming refusals - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals"
category: "04-API-Reference/Test-Evaluate"
fetched_at: "2026-11-05T06:36:36Z"
tags: ["api"]
---

# Handle streaming refusals

Copy page



Detect and handle refusal stop reasons in streaming responses, and retry refused requests on a fallback model.

Copy page



Streaming refusals

[APIs](#feature-availability)  
Messages APIAlways onManaged AgentsAlways on

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableAmazon BedrockAvailableAmazon BedrockInvokeModelAvailableClaude Models on Google CloudGoogle managedAvailableMicrosoft FoundryAvailable

Usage differs by product

Messages API

The stream ends with `stop_reason` `"refusal"`, and `stop_details` (`category` and `explanation`) arrives on the `message_delta` event.

Managed Agents

A refused turn ends, and the session goes idle. Treat a turn as refused if `stop_details.type` or `stop_reason.type` is `"refusal"`.

Starting with Claude 4 models, streaming responses from Claude’s API return **`stop_reason`: `"refusal"`** when streaming classifiers intervene to handle potential policy violations. This safety feature helps maintain content compliance during real-time streaming.



This page covers how refusals appear in streaming responses. For every `stop_reason` value and how to handle it, see [Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md). To retry refused requests on another Claude model, see [Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md).

## API response format

When streaming classifiers detect content that violates Anthropic’s policies, the API returns this response:

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

A `refusal` response from streaming classifiers includes a `stop_details` object with a `category` and a human-readable `explanation` that you can surface to the user. See [What a refusal looks like](../Guides/build-with-claude-refusals-and-fallback.md#refusal-response) for the full response shape and the available categories.

On a refusal the `stop_details` object is always present, but its `category` and `explanation` fields can be `null`, for example when the refusal maps to no named category. Branch on `stop_reason` or `stop_details.type` rather than assuming `category` and `explanation` are populated, and provide your own user-facing messaging when they are `null`.

## Reset context after refusal

When you receive **`stop_reason`: `refusal`**, you must reset the conversation context before continuing. You can remove or rephrase the turn that triggered the refusal, or clear the conversation history entirely. Attempting to continue without resetting will result in continued refusals.



Usage metrics are still provided in the response, even when the response is refused. Whether a refused request is billed depends on when the refusal arrives and its category; see [How refusals are billed](../Guides/build-with-claude-refusals-and-fallback.md#how-refusals-are-billed).



Resetting context is not the only way to recover. You can also retry the refused request on a different Claude model, and the [Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md) page shows how to set that up with server-side fallback, the SDK middleware, or a manual retry.

## Implementation guide

Here’s how to detect and handle streaming refusals in your application:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

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

| Refusal type | Response format | When it occurs |
|----|----|----|
| Streaming classifier refusals | **`stop_reason`: `refusal`** | During streaming when content violates policies |
| API input and copyright validation | 400 error codes | When input fails validation checks |
| Model-generated refusals | Standard text responses | When the model itself refuses |

## Best practices

- **Monitor for refusals:** Include **`stop_reason`: `refusal`** checks in your error handling.
- **Reset automatically:** Implement automatic context reset when refusals are detected.
- **Fall back to another model:** Configure [server-side fallback or the SDK middleware](../Guides/build-with-claude-refusals-and-fallback.md) so refused requests are retried on another Claude model instead of surfacing a refusal to the user. Claude Haiku 5.5 has no server-side fallback, so set up its retry in your client.
- **Redeem fallback credit on manual retries:** If you build the retry yourself, pass the refusal’s [fallback credit](../Guides/build-with-claude-fallback-credit.md) token so the retry doesn’t pay the prompt-cache cost twice. Claude Haiku 5.5 refusals carry no fallback credit.
- **Provide custom messaging:** Create user-friendly messages for better UX when refusals occur.
- **Track refusal patterns:** Monitor refusal frequency to identify potential issues with your prompts.

## Migration notes

If you built refusal handling when this feature first shipped, or you’re adding it to an existing integration, check the following:

- **Refusals are responses, not errors.** A refusal arrives as a successful HTTP 200 response with `stop_reason`: `"refusal"`, so monitoring built only on error rates won’t surface it. Track refusals as their own signal.
- **Refusals include structured detail.** On every model, a refusal also includes a `stop_details` object that identifies the policy category behind the decline. See [What a refusal looks like](../Guides/build-with-claude-refusals-and-fallback.md#refusal-response) for the full response shape.
- **Retry on a different model.** Re-sending a refused request to the same model usually results in another refusal. Instead of only resetting context, retry on a fallback model with [server-side fallback, the SDK middleware, or a manual retry](../Guides/build-with-claude-refusals-and-fallback.md), and redeem [fallback credit](../Guides/build-with-claude-fallback-credit.md) when you build the retry yourself. Claude Haiku 5.5 has no server-side fallback, and its refusals carry no fallback credit, so set up its retry in your client.
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

Serve users across languages with Claude’s cross-lingual capabilities.

## Availability

Streaming refusals are available or in beta, depending on the API.

### API support

[Messages API](../Guides/build-with-claude-working-with-messages.md)

Usage

Always on

The stream ends with `stop_reason` `"refusal"`, and `stop_details` (`category` and `explanation`) arrives on the `message_delta` event.

StatusAvailable

Cloud platforms

- Claude API
- [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)
- [Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md)
- [Amazon Bedrock](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)InvokeModel
- [Claude Models on Google Cloud](../Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)Google managed
- [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Managed Agents](../Other/managed-agents-overview.md)

Usage

Always on

A refused turn ends, and the session goes idle. Treat a turn as refused if `stop_details.type` or `stop_reason.type` on the `session.status_idle` event is `"refusal"`. On a refused turn, `stop_reason.type` can be `"end_turn"`. `stop_details` is `null` on any other turn, and can be `null` on a refused turn too.

StatusBeta

Cloud platforms

- Claude API
- [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)
