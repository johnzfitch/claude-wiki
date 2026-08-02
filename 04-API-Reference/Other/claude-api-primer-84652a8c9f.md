---
title: "API usage primer for Claude - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/claude_api_primer"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:36Z"
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


[](/login)




Browse

Documentation

# API usage primer for Claude




This guide is designed to give Claude the basics of using the Claude API. It gives explanation and examples of model IDs/the basic messages API, tool use, streaming, thinking, and nothing else.







API usage primer for Claude

> This guide is designed to give Claude the basics of using the Claude API. It gives explanation and examples of model IDs/the basic messages API, tool use, streaming, thinking, and nothing else.




Models

```python
For complex agentic coding and enterprise work: Claude Opus 5: claude-opus-5
Previous Opus model: Claude Opus 4.8: claude-opus-4-8
Smart model: Claude Sonnet 5: claude-sonnet-5
For fast, cost-effective tasks: Claude Haiku 4.5: claude-haiku-4-5-20251001
```






Calling the API




Basic request and response

CLI

Python



```python
import anthropic
import os

message = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
).messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message)
```

Output



```python
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello!"
    }
  ],
  "model": "claude-opus-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 6
  }
}
```




Multiple conversational turns

The Messages API is stateless, which means that you always send the full conversational history to the API. You can use this pattern to build up a conversation over time. Earlier conversational turns don't necessarily need to actually originate from Claude. You can use synthetic `assistant` messages.

CLI

Python



```python
import anthropic

message = anthropic.Anthropic().messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Can you describe LLMs to me?"},
    ],
)
print(message)
```




Prefilling Claude's response

You can pre-fill part of Claude's response in the last position of the input messages list. This can be used to shape Claude's response. The following example uses `"max_tokens": 1` to get a single multiple choice answer from Claude.



Claude 4.6 and later models and Claude Mythos Preview do not support assistant message prefill; requests to those models must end with a user message. The examples below use a model that supports prefill.

CLI

Python



```python
import anthropic

message = anthropic.Anthropic().messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1,
    messages=[
        {
            "role": "user",
            "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae",
        },
        {"role": "assistant", "content": "The answer is ("},
    ],
)
print(message.content[0].text)
```




Vision

Claude can read both text and images in requests. Both `base64` and `url` source types are supported for images, along with the `image/jpeg`, `image/png`, `image/gif`, and `image/webp` media types.

CLI

Python



```python
import anthropic
import base64
import httpx

# Option 1: Base64-encoded image
image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

message = anthropic.Anthropic().messages.create(
    model="claude-opus-5",
    max_tokens=1024,
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
                {"type": "text", "text": "What is in the above image?"},
            ],
        }
    ],
)
print(next(block.text for block in message.content if block.type == "text"))

# Option 2: URL-referenced image
message_from_url = anthropic.Anthropic().messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                    },
                },
                {"type": "text", "text": "What is in the above image?"},
            ],
        }
    ],
)
print(next(block.text for block in message_from_url.content if block.type == "text"))
```




Thinking

Thinking can sometimes help Claude with very hard tasks. The current mechanism is [adaptive thinking](/docs/en/build-with-claude/thinking) (`thinking: {"type": "adaptive"}`): Claude decides when and how much to think, and you steer thinking depth with the [`effort`](/docs/en/build-with-claude/effort) parameter rather than a token budget. Adaptive thinking is supported on Claude 4.6 and later models and Claude Mythos Preview. On Claude 5 models and Claude Mythos Preview, thinking is on by default when the `thinking` parameter is omitted.

Temperature must be set to 1 (or left unset) whenever thinking is enabled, on all models. On Claude 4.7 and later models and Claude Mythos Preview, `temperature` is deprecated and only its default value is accepted, even when thinking is off.

Thinking is supported in the following models:

- Claude Opus 5 (claude-opus-5, adaptive thinking only, on by default)
- Claude Sonnet 5 (`claude-sonnet-5`, adaptive thinking only, on by default)
- Claude Opus 4.8 (claude-opus-4-8, adaptive thinking only)
- Claude Opus 4.7 (`claude-opus-4-7`, adaptive thinking only)
- Claude Opus 4.6 (`claude-opus-4-6`, adaptive or legacy manual thinking)
- Claude Sonnet 4.6 (`claude-sonnet-4-6`, adaptive or legacy manual thinking)
- Claude Opus 4.5 (`claude-opus-4-5-20251101`, legacy manual thinking only)
- Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`, legacy manual thinking only)
- Claude Haiku 4.5 (`claude-haiku-4-5-20251001`, legacy manual thinking only)



On Claude 4.7 and later models, manual extended thinking (`type: enabled` with a `budget_tokens` value) is not supported and returns a 400 error. Use [adaptive thinking](/docs/en/build-with-claude/thinking) (`type: adaptive`) instead.




How thinking works

When thinking is on, Claude creates `thinking` content blocks where it outputs its internal reasoning. The API response includes `thinking` content blocks, followed by `text` content blocks.

CLI

Python



```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    messages=[
        {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
        }
    ],
)

# The response will contain summarized thinking blocks and text blocks
for block in response.content:
    if block.type == "thinking":
        print(f"\nThinking summary: {block.thinking}")
    elif block.type == "text":
        print(f"\nResponse: {block.text}")
```

Manual extended thinking (`thinking: {"type": "enabled", "budget_tokens": N}`) is the legacy mechanism. It works only on Claude 4 through 4.6 models that support thinking; Claude 4.7 and later models reject `type: enabled` with a 400 error and use [adaptive thinking](/docs/en/build-with-claude/thinking) instead. With manual extended thinking, `budget_tokens` sets the maximum number of tokens Claude is allowed to use for its internal reasoning process; the limit applies to full thinking tokens, not to the summarized output. Unless you are using [interleaved thinking](#interleaved-thinking), `budget_tokens` must be less than `max_tokens` so that Claude has space to write its response after thinking is complete.




Thinking with tool use

Thinking can be used alongside tool use, allowing Claude to reason through tool selection and results processing.

Important limitations:

1.  **Tool choice limitation:** Only supports `tool_choice: {"type": "auto"}` (default) or `tool_choice: {"type": "none"}`.
2.  **Preserving thinking blocks:** During tool use, you must pass `thinking` blocks back to the API for the last assistant message.




Preserving thinking blocks

CLI

Python



```python
import anthropic

client = anthropic.Anthropic()

weather_tool = {
    "name": "get_weather",
    "description": "Get the current weather for a location.",
    "input_schema": {
        "type": "object",
        "properties": {"location": {"type": "string", "description": "The city name."}},
        "required": ["location"],
    },
}

weather_data = {"temperature": 72}

# First request - Claude responds with thinking and tool request
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    tools=[weather_tool],
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
)

# Extract thinking block and tool use block
thinking_block = next(
    (block for block in response.content if block.type == "thinking"), None
)
tool_use_block = next(
    (block for block in response.content if block.type == "tool_use"), None
)

# Second request - Include thinking block and tool result
continuation = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    tools=[weather_tool],
    messages=[
        {"role": "user", "content": "What's the weather in Paris?"},
        # Notice that the thinking_block is passed in as well as the tool_use_block
        {"role": "assistant", "content": [thinking_block, tool_use_block]},
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": f"Current temperature: {weather_data['temperature']}°F",
                }
            ],
        },
    ],
)

for block in continuation.content:
    if block.type == "text":
        print(block.text)
```




Interleaved thinking

Interleaved thinking enables Claude to think between tool calls, reasoning about tool results before deciding the next step.



On models with [adaptive thinking](/docs/en/build-with-claude/thinking) (`thinking: {type: "adaptive"}`), interleaved thinking is automatically enabled. No beta header is needed. Sonnet 4.6 supports both the `interleaved-thinking-2025-05-14` beta header with manual extended thinking and adaptive thinking.

On older models that use manual extended thinking (Claude 4, 4.5, and Sonnet 4.6 models), enable interleaved thinking by adding the beta header `interleaved-thinking-2025-05-14` to your API request:

CLI

Python



```python
import anthropic

client = anthropic.Anthropic()

calculator_tool = {
    "name": "calculator",
    "description": "Perform arithmetic calculations.",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The math expression to evaluate.",
            }
        },
        "required": ["expression"],
    },
}

database_tool = {
    "name": "database_query",
    "description": "Query the product database.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The database query."}
        },
        "required": ["query"],
    },
}

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    tools=[calculator_tool, database_tool],
    messages=[
        {
            "role": "user",
            "content": "What's the total revenue if we sold 150 units of product A at $50 each?",
        }
    ],
    betas=["interleaved-thinking-2025-05-14"],
)

for block in response.content:
    if block.type == "thinking":
        print(f"Thinking: {block.thinking}")
    elif block.type == "tool_use":
        print(f"Tool call: {block.name}({block.input})")
    elif block.type == "text":
        print(f"Response: {block.text}")
```

With interleaved thinking and ONLY with interleaved thinking (not regular manual extended thinking), the `budget_tokens` can exceed the `max_tokens` parameter, as `budget_tokens` in this case represents the total budget across all thinking blocks within one assistant turn.




Tool use




Specifying client tools

Client tools are specified in the `tools` top-level parameter of the API request. Each tool definition includes:

| Parameter      | Description                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------|
| `name`         | The name of the tool. Must match the regex `^[a-zA-Z0-9_-]{1,64}$`.                                 |
| `description`  | A detailed plaintext description of what the tool does, when it should be used, and how it behaves. |
| `input_schema` | A [JSON Schema](https://json-schema.org/) object defining the expected parameters for the tool.     |

```python
{
  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state, e.g. San Francisco, CA"
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
      }
    },
    "required": ["location"]
  }
}
```






Best practices for tool definitions

**Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including:

- What the tool does
- When it should be used (and when it shouldn't)
- What each parameter means and how it affects the tool's behavior
- Any important caveats or limitations

**Consider using `input_examples` for complex tools.** For tools with nested objects, optional parameters, or format-sensitive inputs, you can provide concrete examples using the `input_examples` field (beta). This helps Claude understand expected input patterns. See [Providing tool use examples](/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples) for details.

Example of a good tool description:

```python
{
  "name": "get_stock_price",
  "description": "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.",
  "input_schema": {
    "type": "object",
    "properties": {
      "ticker": {
        "type": "string",
        "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
      }
    },
    "required": ["ticker"]
  }
}
```






Controlling Claude's output




Forcing tool use

You can force Claude to use a specific tool by specifying the tool in the `tool_choice` field:

```python
tool_choice = {"type": "tool", "name": "get_weather"}
```



When working with the `tool_choice` parameter, there are four possible options:

- `auto` allows Claude to decide whether to call any provided tools or not (default).
- `any` tells Claude that it must use one of the provided tools.
- `tool` forces Claude to always use a particular tool.
- `none` prevents Claude from using any tools.




JSON output

Tools do not necessarily need to be client functions. You can use tools anytime you want the model to return JSON output that follows a provided schema.




Chain of thought

When using tools, Claude often shows its "chain of thought," that is, the step-by-step reasoning it uses to break down the problem and decide which tools to use.

```python
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "<thinking>To answer this question, I will: 1. Use the get_weather tool to get the current weather in San Francisco. 2. Use the get_time tool to get the current time in the America/Los_Angeles timezone, which covers San Francisco, CA.</thinking>"
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": { "location": "San Francisco, CA" }
    }
  ]
}
```






Parallel tool use

By default, Claude may use multiple tools to answer a user query. You can disable this behavior by setting `disable_parallel_tool_use=true`.




Handling tool use and tool result content blocks




Handling results from client tools

The response has a `stop_reason` of `tool_use` and one or more `tool_use` content blocks that include:

- `id`: A unique identifier for this particular tool use block.
- `name`: The name of the tool being used.
- `input`: An object containing the input being passed to the tool.

When you receive a tool use response, you should:

1.  Extract the `name`, `id`, and `input` from the `tool_use` block.
2.  Run the actual tool in your code base corresponding to that tool name.
3.  Continue the conversation by sending a new message with a `tool_result`:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "15 degrees"
    }
  ]
}
```






Handling the `max_tokens` stop reason

If Claude's response is cut off because it hits the `max_tokens` limit during tool use, retry the request with a higher `max_tokens` value.




Handling the `pause_turn` stop reason

When using server tools such as web search, the API may return a `pause_turn` stop reason. Continue the conversation by passing the paused response back as-is in a subsequent request.




Troubleshooting errors




Tool execution error

If the tool itself throws an error during execution, return the error message with `"is_error": true`:

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "ConnectionError: the weather service API is not available (HTTP 500)",
      "is_error": true
    }
  ]
}
```






Invalid tool name

If Claude's attempted use of a tool is invalid (for example, missing required parameters), try the request again with more-detailed `description` values in your tool definitions.




Streaming messages

When creating a Message, you can set `"stream": true` to incrementally stream the response using server-sent events (SSE).




Streaming with SDKs

CLI

Python



```python
import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    model="claude-opus-5",
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```




Event types

Each server-sent event includes a named event type and associated JSON data. Each stream uses the following event flow:

1.  `message_start`: contains a `Message` object with empty `content`.
2.  A series of content blocks, each with `content_block_start`, one or more `content_block_delta` events, and `content_block_stop`.
3.  One or more `message_delta` events, indicating top-level changes to the final `Message` object.
4.  A final `message_stop` event.

**Warning:** The token counts shown in the `usage` field of the `message_delta` event are *cumulative*.




Content block delta types




Text delta

```python
{
  "type": "content_block_delta",
  "index": 0,
  "delta": { "type": "text_delta", "text": "Hello frien" }
}
```






Input JSON delta

For `tool_use` content blocks, deltas are *partial JSON strings*:

```python
{"type": "content_block_delta","index": 1,"delta": {"type": "input_json_delta","partial_json": "{\"location\": \"San Fra"}}}
```






Thinking delta

When using thinking with streaming:

```python
{
  "type": "content_block_delta",
  "index": 0,
  "delta": {
    "type": "thinking_delta",
    "thinking": "Let me solve this step by step..."
  }
}
```






Basic streaming request example

```python
event: message_start
data: {"type": "message_start", "message": {"id": "msg_1nZdL29xx5MUA1yADyHTEsnR8uuvGzszyY", "type": "message", "role": "assistant", "content": [], "model": "claude-opus-5", "stop_reason": null, "stop_sequence": null, "usage": {"input_tokens": 25, "output_tokens": 1}}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "Hello"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "!"}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: message_delta
data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence":null}, "usage": {"output_tokens": 15}}

event: message_stop
data: {"type": "message_stop"}
```


