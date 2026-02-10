---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:07Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons"
title: "Handling stop reasons - Claude API Docs"
---

Build with Claude

# Handling stop reasons

Copy page

Copy page

When you make a request to the Messages API, Claude's response includes a `stop_reason` field that indicates why the model stopped generating its response. Understanding these values is crucial for building robust applications that handle different response types appropriately.

For details about `stop_reason` in the API response, see the [Messages API reference](/docs/en/api/messages).

## 

What is stop_reason?

The `stop_reason` field is part of every successful Messages API response. Unlike errors, which indicate failures in processing your request, `stop_reason` tells you why Claude successfully completed its response generation.

Example response

``` shiki
{
  "id": "msg_01234",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Here's the answer to your question..."
    }
  ],
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 100,
    "output_tokens": 50
  }
}
```

## 

Stop reason values

### 

end_turn

The most common stop reason. Indicates Claude finished its response naturally.

``` shiki
if response.stop_reason == "end_turn":
    # Process the complete response
    print(response.content[0].text)
```

#### 

Empty responses with end_turn

Sometimes Claude returns an empty response (exactly 2-3 tokens with no content) with `stop_reason: "end_turn"`. This typically happens when Claude interprets that the assistant turn is complete, particularly after tool results.

**Common causes:**

- Adding text blocks immediately after tool results (Claude learns to expect the user to always insert text after tool results, so it ends its turn to follow the pattern)
- Sending Claude's completed response back without adding anything (Claude already decided it's done, so it will remain done)

**How to prevent empty responses:**

``` shiki
# INCORRECT: Adding text immediately after tool_result
messages = [
    {"role": "user", "content": "Calculate the sum of 1234 and 5678"},
    {"role": "assistant", "content": [
        {
            "type": "tool_use",
            "id": "toolu_123",
            "name": "calculator",
            "input": {"operation": "add", "a": 1234, "b": 5678}
        }
    ]},
    {"role": "user", "content": [
        {
            "type": "tool_result",
            "tool_use_id": "toolu_123",
            "content": "6912"
        },
        {
            "type": "text",
            "text": "Here's the result"  # Don't add text after tool_result
        }
    ]}
]

# CORRECT: Send tool results directly without additional text
messages = [
    {"role": "user", "content": "Calculate the sum of 1234 and 5678"},
    {"role": "assistant", "content": [
        {
            "type": "tool_use",
            "id": "toolu_123",
            "name": "calculator",
            "input": {"operation": "add", "a": 1234, "b": 5678}
        }
    ]},
    {"role": "user", "content": [
        {
            "type": "tool_result",
            "tool_use_id": "toolu_123",
            "content": "6912"
        }
    ]}  # Just the tool_result, no additional text
]

# If you still get empty responses after fixing the above:
def handle_empty_response(client, messages):
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=messages
    )

    # Check if response is empty
    if (response.stop_reason == "end_turn" and
        not response.content:

        # INCORRECT: Don't just retry with the empty response
        # This won't work because Claude already decided it's done

        # CORRECT: Add a continuation prompt in a NEW user message
        messages.append({"role": "user", "content": "Please continue"})

        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1024,
            messages=messages
        )

    return response
```

**Best practices:**

1.  **Never add text blocks immediately after tool results** - This teaches Claude to expect user input after every tool use
2.  **Don't retry empty responses without modification** - Simply sending the empty response back won't help
3.  **Use continuation prompts as a last resort** - Only if the above fixes don't resolve the issue

### 

max_tokens

Claude stopped because it reached the `max_tokens` limit specified in your request.

``` shiki
# Request with limited tokens
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=10,
    messages=[{"role": "user", "content": "Explain quantum physics"}]
)

if response.stop_reason == "max_tokens":
    # Response was truncated
    print("Response was cut off at token limit")
    # Consider making another request to continue
```

### 

stop_sequence

Claude encountered one of your custom stop sequences.

``` shiki
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    stop_sequences=["END", "STOP"],
    messages=[{"role": "user", "content": "Generate text until you say END"}]
)

if response.stop_reason == "stop_sequence":
    print(f"Stopped at sequence: {response.stop_sequence}")
```

### 

tool_use

Claude is calling a tool and expects you to execute it.

For most tool use implementations, we recommend using the [tool runner](/docs/en/agents-and-tools/tool-use/implement-tool-use#tool-runner-beta) which automatically handles tool execution, result formatting, and conversation management.

``` shiki
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=[weather_tool],
    messages=[{"role": "user", "content": "What's the weather?"}]
)

if response.stop_reason == "tool_use":
    # Extract and execute the tool
    for content in response.content:
        if content.type == "tool_use":
            result = execute_tool(content.name, content.input)
            # Return result to Claude for final response
```

### 

pause_turn

Used with server tools like web search when Claude needs to pause a long-running operation.

``` shiki
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=[{"type": "web_search_20250305", "name": "web_search"}],
    messages=[{"role": "user", "content": "Search for latest AI news"}]
)

if response.stop_reason == "pause_turn":
    # Continue the conversation
    messages = [
        {"role": "user", "content": original_query},
        {"role": "assistant", "content": response.content}
    ]
    continuation = client.messages.create(
        model="claude-opus-4-6",
        messages=messages,
        tools=[{"type": "web_search_20250305", "name": "web_search"}]
    )
```

### 

refusal

Claude refused to generate a response due to safety concerns.

``` shiki
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "[Unsafe request]"}]
)

if response.stop_reason == "refusal":
    # Claude declined to respond
    print("Claude was unable to process this request")
    # Consider rephrasing or modifying the request
```

If you encounter `refusal` stop reasons frequently while using Claude Sonnet 4.5 or Opus 4.1, you can try updating your API calls to use Sonnet 4 (`claude-sonnet-4-20250514`), which has different usage restrictions. Learn more about [understanding Sonnet 4.5's API safety filters](https://support.claude.com/en/articles/12449294-understanding-sonnet-4-5-s-api-safety-filters).

To learn more about refusals triggered by API safety filters for Claude Sonnet 4.5, see [Understanding Sonnet 4.5's API Safety Filters](https://support.claude.com/en/articles/12449294-understanding-sonnet-4-5-s-api-safety-filters).

### 

model_context_window_exceeded

Claude stopped because it reached the model's context window limit. This allows you to request the maximum possible tokens without knowing the exact input size.

``` shiki
# Request with maximum tokens to get as much as possible
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=64000,  # Model's maximum output tokens
    messages=[{"role": "user", "content": "Large input that uses most of context window..."}]
)

if response.stop_reason == "model_context_window_exceeded":
    # Response hit context window limit before max_tokens
    print("Response reached model's context window limit")
    # The response is still valid but was limited by context window
```

This stop reason is available by default in Sonnet 4.5 and newer models. For earlier models, use the beta header `model-context-window-exceeded-2025-08-26` to enable this behavior.

## 

Best practices for handling stop reasons

### 

1\. Always check stop_reason

Make it a habit to check the `stop_reason` in your response handling logic:

``` shiki
def handle_response(response):
    if response.stop_reason == "tool_use":
        return handle_tool_use(response)
    elif response.stop_reason == "max_tokens":
        return handle_truncation(response)
    elif response.stop_reason == "model_context_window_exceeded":
        return handle_context_limit(response)
    elif response.stop_reason == "pause_turn":
        return handle_pause(response)
    elif response.stop_reason == "refusal":
        return handle_refusal(response)
    else:
        # Handle end_turn and other cases
        return response.content[0].text
```

### 

2\. Handle truncated responses gracefully

When a response is truncated due to token limits or context window:

``` shiki
def handle_truncated_response(response):
    if response.stop_reason in ["max_tokens", "model_context_window_exceeded"]:
        # Option 1: Warn the user about the specific limit
        if response.stop_reason == "max_tokens":
            message = "[Response truncated due to max_tokens limit]"
        else:
            message = "[Response truncated due to context window limit]"
        return f"{response.content[0].text}\n\n{message}"

        # Option 2: Continue generation
        messages = [
            {"role": "user", "content": original_prompt},
            {"role": "assistant", "content": response.content[0].text}
        ]
        continuation = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1024,
            messages=messages + [{"role": "user", "content": "Please continue"}]
        )
        return response.content[0].text + continuation.content[0].text
```

### 

3\. Implement retry logic for pause_turn

For server tools that may pause:

``` shiki
def handle_paused_conversation(initial_response, max_retries=3):
    response = initial_response
    messages = [{"role": "user", "content": original_query}]
    
    for attempt in range(max_retries):
        if response.stop_reason != "pause_turn":
            break
            
        messages.append({"role": "assistant", "content": response.content})
        response = client.messages.create(
            model="claude-opus-4-6",
            messages=messages,
            tools=original_tools
        )
    
    return response
```

## 

Stop reasons vs. errors

It's important to distinguish between `stop_reason` values and actual errors:

### 

Stop reasons (successful responses)

- Part of the response body
- Indicate why generation stopped normally
- Response contains valid content

### 

Errors (failed requests)

- HTTP status codes 4xx or 5xx
- Indicate request processing failures
- Response contains error details

``` shiki
try:
    response = client.messages.create(...)
    
    # Handle successful response with stop_reason
    if response.stop_reason == "max_tokens":
        print("Response was truncated")
    
except anthropic.APIError as e:
    # Handle actual errors
    if e.status_code == 429:
        print("Rate limit exceeded")
    elif e.status_code == 500:
        print("Server error")
```

## 

Streaming considerations

When using streaming, `stop_reason` is:

- `null` in the initial `message_start` event
- Provided in the `message_delta` event
- Not provided in any other events

``` shiki
with client.messages.stream(...) as stream:
    for event in stream:
        if event.type == "message_delta":
            stop_reason = event.delta.stop_reason
            if stop_reason:
                print(f"Stream ended with: {stop_reason}")
```

## 

Common patterns

### 

Handling tool use workflows

**Simpler with tool runner**: The example below shows manual tool handling. For most use cases, the [tool runner](/docs/en/agents-and-tools/tool-use/implement-tool-use#tool-runner-beta) automatically handles tool execution with much less code.

``` shiki
def complete_tool_workflow(client, user_query, tools):
    messages = [{"role": "user", "content": user_query}]

    while True:
        response = client.messages.create(
            model="claude-opus-4-6",
            messages=messages,
            tools=tools
        )

        if response.stop_reason == "tool_use":
            # Execute tools and continue
            tool_results = execute_tools(response.content)
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
        else:
            # Final response
            return response
```

### 

Ensuring complete responses

``` shiki
def get_complete_response(client, prompt, max_attempts=3):
    messages = [{"role": "user", "content": prompt}]
    full_response = ""

    for _ in range(max_attempts):
        response = client.messages.create(
            model="claude-opus-4-6",
            messages=messages,
            max_tokens=4096
        )

        full_response += response.content[0].text

        if response.stop_reason != "max_tokens":
            break

        # Continue from where it left off
        messages = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": full_response},
            {"role": "user", "content": "Please continue from where you left off."}
        ]

    return full_response
```

### 

Getting maximum tokens without knowing input size

With the `model_context_window_exceeded` stop reason, you can request the maximum possible tokens without calculating input size:

``` shiki
def get_max_possible_tokens(client, prompt):
    """
    Get as many tokens as possible within the model's context window
    without needing to calculate input token count
    """
    response = client.messages.create(
        model="claude-opus-4-6",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=64000  # Set to model's maximum output tokens
    )

    if response.stop_reason == "model_context_window_exceeded":
        # Got the maximum possible tokens given input size
        print(f"Generated {response.usage.output_tokens} tokens (context limit reached)")
    elif response.stop_reason == "max_tokens":
        # Got exactly the requested tokens
        print(f"Generated {response.usage.output_tokens} tokens (max_tokens reached)")
    else:
        # Natural completion
        print(f"Generated {response.usage.output_tokens} tokens (natural completion)")

    return response.content[0].text
```

By properly handling `stop_reason` values, you can build more robust applications that gracefully handle different response scenarios and provide better user experiences.

Was this page helpful?

- 

- [What is stop_reason?](#what-is-stop-reason)

- [Stop reason values](#stop-reason-values)

- [end_turn](#end-turn)

- [max_tokens](#max-tokens)

- [stop_sequence](#stop-sequence)

- [tool_use](#tool-use)

- [pause_turn](#pause-turn)

- [refusal](#refusal)

- [model_context_window_exceeded](#model-context-window-exceeded)

- [Best practices for handling stop reasons](#best-practices-for-handling-stop-reasons)

- [1. Always check stop_reason](#1-always-check-stop-reason)

- [2. Handle truncated responses gracefully](#2-handle-truncated-responses-gracefully)

- [3. Implement retry logic for pause_turn](#3-implement-retry-logic-for-pause-turn)

- [Stop reasons vs. errors](#stop-reasons-vs-errors)

- [Stop reasons (successful responses)](#stop-reasons-successful-responses)

- [Errors (failed requests)](#errors-failed-requests)

- [Streaming considerations](#streaming-considerations)

- [Common patterns](#common-patterns)

- [Handling tool use workflows](#handling-tool-use-workflows)

- [Ensuring complete responses](#ensuring-complete-responses)

- [Getting maximum tokens without knowing input size](#getting-maximum-tokens-without-knowing-input-size)

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
